---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MEASURE_FOLDER_SUBFOLDERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.267 ALL\_MEASURE\_FOLDER\_SUBFOLDERS

`ALL_MEASURE_FOLDER_SUBFOLDERS` describes the OLAP measure folders contained within the OLAP measure folders accessible to the user.

Related Views

- `DBA_MEASURE_FOLDER_SUBFOLDERS` describes the OLAP measure folders contained within the database OLAP measure folders.
- `USER_MEASURE_FOLDER_SUBFOLDERS` describes the OLAP measure folders contained within the OLAP measure folders owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the OLAP measure folder that contains a subfolder |
| `MEASURE_FOLDER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the OLAP measure folder that contains a subfolder |
| `MEASURE_SUBFOLDER_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the OLAP measure folder subfolder |
| `MEASURE_SUBFOLDER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the owning OLAP measure folder subfolder |

See Also:

- " [DBA\_MEASURE\_FOLDER\_SUBFOLDERS](DBA_MEASURE_FOLDER_SUBFOLDERS.md) "
- " [USER\_MEASURE\_FOLDER\_SUBFOLDERS](USER_MEASURE_FOLDER_SUBFOLDERS.md) "