---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_BIND_DATA.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.48 V$SQL\_BIND\_DATA

`V$SQL_BIND_DATA` describes information related to bind variables.

`V$SQL_BIND_DATA` describes, for each distinct bind variable in each cursor owned by the session querying this view:

- Actual bind data, if the bind variable is user defined
- The underlying literal, if the `CURSOR_SHARING` parameter is set to `FORCE` and the bind variable is system generated. (System-generated binds have a value of `256` in the `SHARED_FLAG2` column.)

| Column | Datatype | Description |
| --- | --- | --- |
| `CURSOR_NUM` | `NUMBER` | Cursor number for this bind |
| `POSITION` | `NUMBER` | Bind position |
| `DATATYPE` | `NUMBER` | Internal identifier for the bind data type. Beginning in Oracle Database 12c, a number representing a PL/SQL data type can appear in this column. |
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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [CURSOR\_SHARING](CURSOR_SHARING.md) "