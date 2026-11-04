---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_BLOCKCHAIN_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.116 ALL\_BLOCKCHAIN\_TABLES

`ALL_BLOCKCHAIN_TABLES` describes the blockchain tables accessible to the current user.

Related Views

- `DBA_BLOCKCHAIN_TABLES` describes all blockchain tables in the database.
- `USER_BLOCKCHAIN_TABLES` describes the blockchain tables owned by the current user. This view does not display the `SCHEMA_NAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEMA_NAME` | `VARCHAR2(128)` | `NOT NULL` | The schema containing the blockchain table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the blockchain table |
| `ROW_RETENTION` | `NUMBER` |  | Row retention period for the blockchain table, that is, the minimum number of days a row must be retained and cannot be deleted after it is inserted into the table  If the value of this column is NULL, then rows can never be deleted from the table. |
| `ROW_RETENTION_LOCKED` | `VARCHAR2(3)` |  | Indicates whether the row retention period for the blockchain table is locked. Possible values:  - `YES`: The row retention period is locked. You cannot change the row retention period - `NO`: The row retention period is not locked. You can change the row retention period to a value higher than the current value with the SQL statement `ALTER` `TABLE` … `NO` `DELETE` `UNTIL` `n` `DAYS` `AFTER` `INSERT` |
| `TABLE_INACTIVITY_RETENTION` | `NUMBER` |  | Number of days for which the blockchain table must be inactive before it can be dropped, that is, the number of days that must pass after the most recent row insertion before the table can be dropped  A table with no rows can be dropped at any time, regardless of this column value. |
| `HASH_ALGORITHM` | `VARCHAR2(8)` |  | Algorithm used for computing the hash value for each table row |

See Also:

- " [DBA\_BLOCKCHAIN\_TABLES](DBA_BLOCKCHAIN_TABLES.md) "
- " [USER\_BLOCKCHAIN\_TABLES](USER_BLOCKCHAIN_TABLES.md) "