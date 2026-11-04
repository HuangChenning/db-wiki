---
title: ALL_STAT_EXTENSIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2075.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_STAT_EXTENSIONS` displays information about the optimizer statistics extensions accessible to the current user.

Related Views

- `DBA_STAT_EXTENSIONS` displays information about all optimizer statistics extensions in the database.
- `USER_STAT_EXTENSIONS` displays information about the optimizer statistics extensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the extension |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table to which the extension belongs |
| `EXTENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the statistics extension |
| `EXTENSION` | `CLOB` |  | Extension (the expression or column group) |
| `CREATOR` | `VARCHAR2(6)` |  | Creator of the extension: |
| `DROPPABLE` | `VARCHAR2(3)` |  | Indicates whether the extension is droppable using `DBMS_STATS.DROP_EXTENDED_STATS` (`YES`) or not (`NO`) |

See Also:

- ["DBA\_STAT\_EXTENSIONS"](statviews_4293.md)
- ["USER\_STAT\_EXTENSIONS"](statviews_5462.md)