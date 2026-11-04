---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_DIRECTORIES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_DIRECTORIES` describes all directories accessible to the current user.

Related View

`DBA_DIRECTORIES` describes all directories in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the directory (always `SYS`) |
| `DIRECTORY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the directory |
| `DIRECTORY_PATH` | `VARCHAR2(4000)` |  | Operating system pathname for the directory |
| `ORIGIN_CON_ID` | `VARCHAR2(256)` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root) |

See Also:

" [DBA\_DIRECTORIES](DBA_DIRECTORIES.md) "