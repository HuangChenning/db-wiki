---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_TAB_MODIFICATIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.717 USER\_TAB\_MODIFICATIONS

`USER_TAB_MODIFICATIONS` describes modifications to all tables owned by the current user that have been modified since the last time statistics were gathered on the tables. Its columns are the same as those in `ALL_TAB_MODIFICATIONS`.

Note:

For performance reasons, Oracle Database does not populate this view immediately when the actual modifications occur.

See Also:

" [ALL\_TAB\_MODIFICATIONS](ALL_TAB_MODIFICATIONS.md) "