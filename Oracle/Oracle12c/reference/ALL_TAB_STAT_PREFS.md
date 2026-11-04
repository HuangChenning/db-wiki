---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_TAB_STAT_PREFS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_TAB_STAT_PREFS` displays information about statistics preferences for the tables accessible to the current user.

Related Views

- `DBA_TAB_STAT_PREFS` displays information about statistics preferences for all tables in the database.
- `USER_TAB_STAT_PREFS` displays information about statistics preferences for the tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `PREFERENCE_NAME` | `VARCHAR2(30)` |  | Name of the preference |
| `PREFERENCE_VALUE` | `VARCHAR2(4000)` |  | Value of the preference |

See Also:

- " [DBA\_TAB\_STAT\_PREFS](DBA_TAB_STAT_PREFS.md) "
- " [USER\_TAB\_STAT\_PREFS](USER_TAB_STAT_PREFS.md) "