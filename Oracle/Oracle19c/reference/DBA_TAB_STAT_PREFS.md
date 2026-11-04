---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_TAB_STAT_PREFS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.42 DBA\_TAB\_STAT\_PREFS

`DBA_TAB_STAT_PREFS` displays information about statistics preferences for all tables in the database. Its columns are the same as those in `ALL_TAB_STAT_PREFS`.

Note:

In earlier releases, this view could be queried by any user with the `PUBLIC` role. Starting with Oracle Database 19c, Release Update 19.28, this view adheres to the convention for `DBA_` views, that is, it can be queried only by users with the `SYSDBA` system privilege or `SELECT` `ANY` `DICTIONARY` privilege, or `SELECT_CATALOG_ROLE` role, or by users with direct privileges granted to them. This change improves access control for optimizer and statistics metadata and reduces information disclosure.

See Also:

" [ALL\_TAB\_STAT\_PREFS](ALL_TAB_STAT_PREFS.md) ".