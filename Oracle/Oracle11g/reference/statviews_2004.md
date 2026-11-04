---
title: ALL_PART_KEY_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2004.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_PART_KEY_COLUMNS` describes the partitioning key columns for the partitioned objects accessible to the current user.

Related Views

- `DBA_PART_KEY_COLUMNS` describes the partitioning key columns for all partitioned objects in the database.
- `USER_PART_KEY_COLUMNS` describes the partitioning key columns for the partitioned objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the partitioned table or index |
| `NAME` | `VARCHAR2(30)` |  | Name of the partitioned table or index |
| `OBJECT_TYPE` | `CHAR(5)` |  | Object type: |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column |
| `COLUMN_POSITION` | `NUMBER` |  | Position of the column within the partitioning key |

See Also:

- ["DBA\_PART\_KEY\_COLUMNS"](statviews_4175.md)
- ["USER\_PART\_KEY\_COLUMNS"](statviews_5390.md)