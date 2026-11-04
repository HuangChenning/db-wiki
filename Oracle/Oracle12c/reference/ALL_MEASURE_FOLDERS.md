---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_MEASURE_FOLDERS.html
tags:
  - oracle
  - 12c
  - reference
---

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