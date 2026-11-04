---
title: ALL_TRIGGER_COLS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2119.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TRIGGER_COLS` describes the use of columns in the triggers accessible to the current user and in triggers on tables accessible to the current user. If the user has the `CREATE ANY TRIGGER` privilege, then this view describes the use of columns in all triggers in the database.

Related Views

- `DBA_TRIGGER_COLS` describes the use of columns in all triggers in the database.
- `USER_TRIGGER_COLS` describes the use of columns in the triggers owned by the current user and in triggers on tables owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TRIGGER_OWNER` | `VARCHAR2(30)` |  | Owner of the trigger |
| `TRIGGER_NAME` | `VARCHAR2(30)` |  | Name of the trigger |
| `TABLE_OWNER` | `VARCHAR2(30)` |  | Owner of the table on which the trigger is defined |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Table on which the trigger is defined |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column used in the trigger |
| `COLUMN_LIST` | `VARCHAR2(3)` |  | Indicates whether the column is specified in the `UPDATE` clause (`YES`) or not (`NO`) |
| `COLUMN_USAGE` | `VARCHAR2(17)` |  | How the column is used in the trigger: |

See Also:

- ["DBA\_TRIGGER\_COLS"](statviews_5065.md)
- ["USER\_TRIGGER\_COLS"](statviews_5493.md)