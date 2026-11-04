---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MEASURE_FOLDERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.268 ALL\_MEASURE\_FOLDERS

`ALL_MEASURE_FOLDERS` describes the OLAP measure folders accessible to the current user.

Related Views

- `DBA_MEASURE_FOLDERS` describes all OLAP measure folders in the database.
- `USER_MEASURE_FOLDERS` describes the OLAP measure folders owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the measure folder |
| `MEASURE_FOLDER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a measure folder |
| `MEASURE_FOLDER_ID` | `NUMBER` | `NOT NULL` | ID of a measure folder |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the measure folder in the session language |

See Also:

- " [DBA\_MEASURE\_FOLDERS](DBA_MEASURE_FOLDERS.md) "
- " [USER\_MEASURE\_FOLDERS](USER_MEASURE_FOLDERS.md) "