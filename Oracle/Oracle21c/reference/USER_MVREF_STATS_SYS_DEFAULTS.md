---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_MVREF_STATS_SYS_DEFAULTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.581 USER\_MVREF\_STATS\_SYS\_DEFAULTS

`USER_MVREF_STATS_SYS_DEFAULTS` displays the system-wide defaults for the refresh history statistics properties for materialized views accessible to the current user. These values can be altered with the `SET_SYSTEM_DEFAULTS` procedure by a database administrator.

Its columns are the same as those in `DBA_MVREF_STATS_SYS_DEFAULTS`.

This view contains exactly two rows corresponding to the collection-level and retention-period properties; their initial values are `TYPICAL` and `31` respectively.

See Also:

" [DBA\_MVREF\_STATS\_SYS\_DEFAULTS](DBA_MVREF_STATS_SYS_DEFAULTS.md) "