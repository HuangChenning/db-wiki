---
title: ALL_EXTERNAL_LOCATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1091.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_EXTERNAL_LOCATIONS` describes the locations (data sources) of the external tables accessible to the current user.

Related Views

- `DBA_EXTERNAL_LOCATIONS` describes the locations (data sources) of all external tables in the database.
- `USER_EXTERNAL_LOCATIONS` describes the locations (data sources) of the external tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the external table location |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the corresponding external table |
| `LOCATION` | `VARCHAR2(4000)` |  | External table location clause |
| `DIRECTORY_OWNER` | `CHAR(3)` |  | Owner of the directory containing the external table location |
| `DIRECTORY_NAME` | `VARCHAR2(30)` |  | Name of the directory containing the external table location |

See Also:

- ["DBA\_EXTERNAL\_LOCATIONS"](statviews_3179.md)
- ["USER\_EXTERNAL\_LOCATIONS"](statviews_5302.md)