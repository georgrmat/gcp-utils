"""Helpers to read and store data from/to Google Cloud Storage."""
import json
from typing import Any, Optional, Union

from google.cloud import storage


def _blob(bucket_name: str, blob_name: str, client: Optional[storage.Client] = None):
    client = client or storage.Client()
    return client.bucket(bucket_name).blob(blob_name)


def read_blob(bucket_name: str, blob_name: str, client: Optional[storage.Client] = None) -> bytes:
    """Download an object's content as bytes."""
    return _blob(bucket_name, blob_name, client).download_as_bytes()


def write_blob(
    bucket_name: str,
    blob_name: str,
    data: Union[bytes, str],
    content_type: str = "application/octet-stream",
    client: Optional[storage.Client] = None,
) -> None:
    """Upload bytes or a string as an object."""
    _blob(bucket_name, blob_name, client).upload_from_string(data, content_type=content_type)


def read_json(bucket_name: str, blob_name: str, client: Optional[storage.Client] = None) -> Any:
    """Download and parse a JSON object."""
    return json.loads(read_blob(bucket_name, blob_name, client).decode("utf-8"))


def write_json(bucket_name: str, blob_name: str, obj: Any, client: Optional[storage.Client] = None) -> None:
    """Serialize obj as JSON and upload it."""
    write_blob(bucket_name, blob_name, json.dumps(obj), "application/json", client)
