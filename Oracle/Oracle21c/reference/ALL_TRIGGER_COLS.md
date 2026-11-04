---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TRIGGER_COLS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.124 ALL\_TRIGGER\_COLS

`ALL_TRIGGER_COLS` describes the use of columns in the triggers accessible to the current user and in triggers on tables accessible to the current user.

If the user has the `CREATE ANY TRIGGER` privilege, then this view describes the use of columns in all triggers in the database.

Related Views

- `DBA_TRIGGER_COLS` describes the use of columns in all triggers in the database.
- `USER_TRIGGER_COLS` describes the use of columns in the triggers owned by the current user and in triggers on tables owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TRIGGER_OWNER` | `VARCHAR2(128)` |  | Owner of the trigger |
| `TRIGGER_NAME` | `VARCHAR2(128)` |  | Name of the trigger |
| `TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the table on which the trigger is defined |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Table on which the trigger is defined |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column used in the trigger |
| `COLUMN_LIST` | `VARCHAR2(3)` |  | Indicates whether the column is specified in the `UPDATE` clause (`YES`) or not (`NO`) |
| `COLUMN_USAGE` | `VARCHAR2(17)` |  | How the column is used in the trigger:  - `NEW IN` - `OLD IN` - `NEW IN OLD IN` - `NEW OUT` - `NEW IN OUT` - `NEW OUT OLD IN` - `NEW IN OUT OLD IN` - `PARENT IN` |

See Also:

- " [DBA\_TRIGGER\_COLS](DBA_TRIGGER_COLS.md) "
- " [USER\_TRIGGER\_COLS](USER_TRIGGER_COLS.md) "