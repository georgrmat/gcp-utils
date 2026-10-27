# gcp-utils
Helpers for reading and storing data from/to Google Cloud Storage:

```python
from gcp_utils import read_blob, write_blob, read_json, write_json

write_json("my-bucket", "path/data.json", {"a": 1})
data = read_json("my-bucket", "path/data.json")
```

Install with `pip install -r requirements.txt`.
