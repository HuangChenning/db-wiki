---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RSRCMGRMETRIC_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.199 V$RSRCMGRMETRIC\_HISTORY

`V$RSRCMGRMETRIC_HISTORY` displays a history (the last one hour) of resource manager metrics, taken from `V$RSRCMGRMETRIC`. When a resource plan is set, this history is cleared and restarted. This view provides information about resources consumed and wait times per consumer group.

The columns for `V$RSRCMGRMETRIC_HISTORY` are the same as those for `V$RSRCMGRMETRIC`.

See Also:

" [V$RSRCMGRMETRIC](V-RSRCMGRMETRIC.md) "