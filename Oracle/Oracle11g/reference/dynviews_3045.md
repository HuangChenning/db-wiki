---
title: "V$SQL_BIND_DATA"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3045.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQL_BIND_DATA` describes, for each distinct bind variable in each cursor owned by the session querying this view:

- Actual bind data, if the bind variable is user defined
- The underlying literal, if the `CURSOR_SHARING` parameter is set to `FORCE` and the bind variable is system generated. (System-generated binds have a value of `256` in the `SHARED_FLAG2` column.)

| Column | Datatype | Description |
| --- | --- | --- |
| `CURSOR_NUM` | `NUMBER` | Cursor number for this bind |
| `POSITION` | `NUMBER` | Bind position |
| `DATATYPE` | `NUMBER` | Bind datatype |
| `SHARED_MAX_LEN` | `NUMBER` | Shared maximum length for this bind from the shared cursor object associated with this bind |
| `PRIVATE_MAX_LEN` | `NUMBER` | Private maximum length for this bind sent from the client |
| `ARRAY_SIZE` | `NUMBER` | Maximum number of array elements (for array binds only) |
| `PRECISION` | `NUMBER` | Precision (for numeric binds) |
| `SCALE` | `NUMBER` | Scale (for numeric binds) |
| `SHARED_FLAG` | `NUMBER` | Shared bind data flags |
| `SHARED_FLAG2` | `NUMBER` | Shared bind data flags (continued) |
| `BUF_ADDRESS` | `RAW(4 \| 8)` | Bind buffer memory address |
| `BUF_LENGTH` | `NUMBER` | Bind buffer length |
| `VAL_LENGTH` | `NUMBER` | Actual bind value length |
| `BUF_FLAG` | `NUMBER` | Bind buffer flags |
| `INDICATOR` | `NUMBER` | Bind indicator |
| `VALUE` | `VARCHAR2(4000)` | Contents of the bind buffer |