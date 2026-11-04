---
title: "V$SQL_BIND_METADATA"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3046.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQL_BIND_METADATA` describes, for each distinct bind variable in each cursor owned by the session querying this view:

- Bind metadata provided by the client, if the bind variable is user defined
- Metadata based on the underlying literal, if the `CURSOR_SHARING` parameter is set to `FORCE` and the bind variable is system-generated.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Memory address of the child cursor that owns this bind variable |
| `POSITION` | `NUMBER` | Bind position |
| `DATATYPE` | `NUMBER` | Bind datatype |
| `MAX_LENGTH` | `NUMBER` | Maximum length of the bind value |
| `ARRAY_LEN` | `NUMBER` | Maximum number of array elements (for array binds only) |
| `BIND_NAME` | `VARCHAR2(30)` | User-defined or system-generated bind variable name (if used) |