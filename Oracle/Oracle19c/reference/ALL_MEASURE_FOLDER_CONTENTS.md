---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_MEASURE_FOLDER_CONTENTS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.258 ALL\_MEASURE\_FOLDER\_CONTENTS

`ALL_MEASURE_FOLDER_CONTENTS` describes the contents of the OLAP measure folders accessible to the current user.

Related Views

- `DBA_MEASURE_FOLDER_CONTENTS` describes the contents of all OLAP measure folders in the database.
- `USER_MEASURE_FOLDER_CONTENTS` describes the contents of the OLAP measure folders owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the measure folder |
| `MEASURE_FOLDER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a measure folder |
| `CUBE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the cube |
| `CUBE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a cube included in the measure folder |
| `MEASURE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a measure in the cube |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order number of the measure in the folder |

See Also:

- " [DBA\_MEASURE\_FOLDER\_CONTENTS](DBA_MEASURE_FOLDER_CONTENTS.md) "
- " [USER\_MEASURE\_FOLDER\_CONTENTS](USER_MEASURE_FOLDER_CONTENTS.md) "