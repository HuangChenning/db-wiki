---
title: ALL_MEASURE_FOLDER_CONTENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1136.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_MEASURE_FOLDER_CONTENTS` describes the contents of the OLAP measure folders accessible to the current user.

Related Views

- `DBA_MEASURE_FOLDER_CONTENTS` describes the contents of all OLAP measure folders in the database.
- `USER_MEASURE_FOLDER_CONTENTS` describes the contents of the OLAP measure folders owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the measure folder |
| `MEASURE_FOLDER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a measure folder |
| `CUBE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the cube |
| `CUBE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a cube included in the measure folder |
| `MEASURE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a measure in the cube |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order number of the measure in the folder |

See Also:

- ["DBA\_MEASURE\_FOLDER\_CONTENTS"](statviews_4130.md)
- ["USER\_MEASURE\_FOLDER\_CONTENTS"](statviews_5351.md)