---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_STAT_EXTENSIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.86 ALL\_STAT\_EXTENSIONS

`ALL_STAT_EXTENSIONS` displays information about the optimizer statistics extensions accessible to the current user.

Related Views

- `DBA_STAT_EXTENSIONS` displays information about all optimizer statistics extensions in the database.
- `USER_STAT_EXTENSIONS` displays information about the optimizer statistics extensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the extension |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table to which the extension belongs |
| `EXTENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the statistics extension |
| `EXTENSION` | `CLOB` |  | Extension (the expression or column group) |
| `CREATOR` | `VARCHAR2(6)` |  | Creator of the extension:  - `USER` - `SYSTEM` |
| `DROPPABLE` | `VARCHAR2(3)` |  | Indicates whether the extension is droppable using `DBMS_STATS.DROP_EXTENDED_STATS` (`YES`) or not (`NO`) |

See Also:

- " [DBA\_STAT\_EXTENSIONS](DBA_STAT_EXTENSIONS.md) "
- " [USER\_STAT\_EXTENSIONS](USER_STAT_EXTENSIONS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS-GUID-64714B2B-E5CE-4C10-9F1E-25A9F254F6B1) for more information about the `DBMS_STATS.DROP_EXTENDED_STATS` procedure