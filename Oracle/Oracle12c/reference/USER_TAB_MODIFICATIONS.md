---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_TAB_MODIFICATIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_TAB_MODIFICATIONS` describes modifications to all tables owned by the current user that have been modified since the last time statistics were gathered on the tables. Its columns are the same as those in `ALL_TAB_MODIFICATIONS`.

Note:

For performance reasons, Oracle Database does not populate this view immediately when the actual modifications occur.

See Also:

" [ALL\_TAB\_MODIFICATIONS](ALL_TAB_MODIFICATIONS.md) "