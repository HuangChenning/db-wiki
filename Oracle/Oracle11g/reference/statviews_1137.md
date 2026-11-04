---
title: ALL_MEASURE_FOLDERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1137.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_MEASURE_FOLDERS` describes the OLAP measure folders accessible to the current user.

Related Views

- `DBA_MEASURE_FOLDERS` describes all OLAP measure folders in the database.
- `USER_MEASURE_FOLDERS` describes the OLAP measure folders owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the measure folder |
| `MEASURE_FOLDER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a measure folder |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the measure folder in the session language |

See Also:

- ["DBA\_MEASURE\_FOLDERS"](statviews_4131.md)
- ["USER\_MEASURE\_FOLDERS"](statviews_5352.md)