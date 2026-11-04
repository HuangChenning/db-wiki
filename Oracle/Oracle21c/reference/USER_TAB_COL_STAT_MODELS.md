---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_TAB_COL_STAT_MODELS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.709 USER\_TAB\_COL\_STAT\_MODELS

`USER_TAB_COL_STAT_MODELS` describes real-time statistics models for all tables owned by the current user. Its columns (except for `OWNER`) are the same as those in `ALL_TAB_COL_STAT_MODELS`.

Real-time statistics models use machine learning algorithms to predict the number of distinct values (NDV) for table columns.

Note:

This view is available starting with Oracle Database 21c.

See Also:

" [ALL\_TAB\_COL\_STAT\_MODELS](ALL_TAB_COL_STAT_MODELS.md) "