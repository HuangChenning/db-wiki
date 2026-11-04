---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/USER_TAB_MODIFICATIONS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.702 USER\_TAB\_MODIFICATIONS

`USER_TAB_MODIFICATIONS` describes modifications to all tables owned by the current user that have been modified since the last time statistics were gathered on the tables. Its columns are the same as those in `ALL_TAB_MODIFICATIONS`.

Note:

For performance reasons, Oracle Database does not populate this view immediately when the actual modifications occur.

See Also:

" [ALL\_TAB\_MODIFICATIONS](ALL_TAB_MODIFICATIONS.md) "