---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_TAB_COLS.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_TAB_COLS` describes the columns of the tables, views, and clusters owned by the current user.

Its columns (except for `OWNER`) are the same as those in `ALL_TAB_COLS`.

To gather statistics for this view, use the `DBMS_STATS` package.

This view differs from `USER_TAB_COLUMNS` in that system-generated hidden columns are not filtered out.

See Also:

- " [ALL\_TAB\_COLS](ALL_TAB_COLS.md) "
- " [USER\_TAB\_COLUMNS](USER_TAB_COLUMNS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS059) for more information about the `DBMS_STATS` package