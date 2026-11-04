---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_IMMUTABLE_TABLES.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.221 ALL\_IMMUTABLE\_TABLES

`ALL_IMMUTABLE_TABLES` describes the immutable tables accessible to the current user.

Related Views

- `DBA_IMMUTABLE_TABLES` describes all immutable tables in the database.
- `USER_IMMUTABLE_TABLES` describes the immutable tables owned by the current user. This view does not display the `SCHEMA_NAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEMA_NAME` | `VARCHAR2(128)` | `NOT NULL` | The schema containing the immutable table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the immutable table |
| `ROW_RETENTION` | `NUMBER` |  | Row retention period for the immutable table, that is, the minimum number of days a row must be retained and cannot be deleted after it is inserted into the table  If the value of this column is NULL, then rows can never be deleted from the table. |
| `ROW_RETENTION_LOCKED` | `VARCHAR2(3)` |  | Indicates whether the row retention period for the immutable table is locked. Possible values:  - `YES`: The row retention period is locked. You cannot change the row retention period - `NO`: The row retention period is not locked. You can change the row retention period to a value higher than the current value with the SQL statement `ALTER` `TABLE` … `NO` `DELETE` `UNTIL` `n` `DAYS` `AFTER` `INSERT` |
| `TABLE_INACTIVITY_RETENTION` | `NUMBER` |  | Number of days for which the immutable table must be inactive before it can be dropped, that is, the number of days that must pass after the most recent row insertion before the table can be dropped  A table with no rows can be dropped at any time, regardless of this column value. |

Note:

This view is available starting with Oracle Database 19c, Release Update 19.11.

See Also:

- " [DBA\_IMMUTABLE\_TABLES](DBA_IMMUTABLE_TABLES.md) "
- " [USER\_IMMUTABLE\_TABLES](USER_IMMUTABLE_TABLES.md) "