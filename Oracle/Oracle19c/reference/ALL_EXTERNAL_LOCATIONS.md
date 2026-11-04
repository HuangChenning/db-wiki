---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_EXTERNAL_LOCATIONS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.181 ALL\_EXTERNAL\_LOCATIONS

`ALL_EXTERNAL_LOCATIONS` describes the locations (data sources) of the external tables accessible to the current user.

Related Views

- `DBA_EXTERNAL_LOCATIONS` describes the locations (data sources) of all external tables in the database.
- `USER_EXTERNAL_LOCATIONS` describes the locations (data sources) of the external tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the external table location |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the corresponding external table |
| `LOCATION` | `VARCHAR2(4000)` |  | External table location clause |
| `DIRECTORY_OWNER` | `CHAR(3)` |  | Owner of the directory containing the external table location |
| `DIRECTORY_NAME` | `VARCHAR2(128)` |  | Name of the directory containing the external table location |

See Also:

- " [DBA\_EXTERNAL\_LOCATIONS](DBA_EXTERNAL_LOCATIONS.md) "
- " [USER\_EXTERNAL\_LOCATIONS](USER_EXTERNAL_LOCATIONS.md) "