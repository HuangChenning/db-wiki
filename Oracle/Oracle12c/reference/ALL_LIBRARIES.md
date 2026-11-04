---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_LIBRARIES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_LIBRARIES` describes the libraries accessible to the current user.

Related Views

- `DBA_LIBRARIES` describes all libraries in the database.
- `USER_LIBRARIES` describes the libraries owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the library |
| `LIBRARY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Library name |
| `FILE_SPEC` | `VARCHAR2(2000)` |  | Operating system file specification associated with the library |
| `DYNAMIC` | `VARCHAR2(1)` |  | Indicates whether the library is dynamically loadable (`Y`) or not (`N`) |
| `STATUS` | `VARCHAR2(7)` |  | Status of the library:  - `N/A` - `VALID` - `INVALID` |
| `AGENT` | `VARCHAR2(128)` |  | Agent of the library |
| `LEAF_FILENAME` | `VARCHAR2(2000)` |  | Leaf filename of the library |
| `ORIGIN_CON_ID` | `VARCHAR2(256)` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root) |

See Also:

- " [DBA\_LIBRARIES](DBA_LIBRARIES.md) "
- " [USER\_LIBRARIES](USER_LIBRARIES.md) "