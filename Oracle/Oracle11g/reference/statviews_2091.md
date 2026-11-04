---
title: ALL_SUBPART_KEY_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2091.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SUBPART_KEY_COLUMNS` displays subpartitioning key columns for composite-partitioned tables (and local indexes on composite-partitioned tables) accessible to the current user.

Related Views

- `DBA_SUBPART_KEY_COLUMNS` displays this information for all subpartitions in the database.
- `USER_SUBPART_KEY_COLUMNS` displays this information for subpartitions of all partitioned objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the partitioned table or index |
| `NAME` | `VARCHAR2(30)` |  | Name of the partitioned table or index |
| `OBJECT_TYPE` | `CHAR(5)` |  | Object type: |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Column name |
| `COLUMN_POSITION` | `NUMBER` |  | Position of the column within the subpartitioning key |

See Also:

- ["DBA\_SUBPART\_KEY\_COLUMNS"](statviews_5031.md)
- ["USER\_SUBPART\_KEY\_COLUMNS"](statviews_5466.md)