from unittest.mock import MagicMock

from gcp_utils import read_blob, read_json, write_blob, write_json


def _client():
    client = MagicMock()
    return client, client.bucket.return_value.blob.return_value


def test_write_and_read_blob():
    client, blob = _client()
    write_blob("b", "o", "hi", client=client)
    blob.upload_from_string.assert_called_once_with("hi", content_type="application/octet-stream")
    blob.download_as_bytes.return_value = b"hi"
    assert read_blob("b", "o", client=client) == b"hi"
    client.bucket.assert_called_with("b")


def test_json_roundtrip():
    client, blob = _client()
    write_json("b", "o", {"a": 1}, client=client)
    blob.upload_from_string.assert_called_once_with('{"a": 1}', content_type="application/json")
    blob.download_as_bytes.return_value = b'{"a": 1}'
    assert read_json("b", "o", client=client) == {"a": 1}
