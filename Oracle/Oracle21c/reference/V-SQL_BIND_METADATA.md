---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_BIND_METADATA.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.49 V$SQL\_BIND\_METADATA

`V$SQL_BIND_METADATA` describes metadata related to bind variables.

`V$SQL_BIND_METADATA` describes, for each distinct bind variable in each cursor owned by the session querying this view:

- Bind metadata provided by the client, if the bind variable is user defined
- Metadata based on the underlying literal, if the `CURSOR_SHARING` parameter is set to `FORCE ` and the bind variable is system-generated.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Memory address of the child cursor that owns this bind variable |
| `POSITION` | `NUMBER` | Bind position |
| `DATATYPE` | `NUMBER` | Internal identifier for the bind data type. Beginning in Oracle Database 12c, a number representing a PL/SQL data type can appear in this column. |
| `MAX_LENGTH` | `NUMBER` | Maximum length of the bind value |
| `ARRAY_LEN` | `NUMBER` | Maximum number of array elements (for array binds only) |
| `BIND_NAME` | `VARCHAR2(128)` | User-defined or system-generated bind variable name (if used) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [CURSOR\_SHARING](CURSOR_SHARING.md) "