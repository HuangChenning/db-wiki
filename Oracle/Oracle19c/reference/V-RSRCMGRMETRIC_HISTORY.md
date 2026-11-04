---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-RSRCMGRMETRIC_HISTORY.html
tags:
  - oracle
  - 19c
  - reference
---

## 8.196 V$RSRCMGRMETRIC\_HISTORY

`V$RSRCMGRMETRIC_HISTORY` displays a history (the last one hour) of resource manager metrics, taken from `V$RSRCMGRMETRIC`. When a resource plan is set, this history is cleared and restarted. This view provides information about resources consumed and wait times per consumer group.

The columns for `V$RSRCMGRMETRIC_HISTORY` are the same as those for `V$RSRCMGRMETRIC`.

See Also:

" [V$RSRCMGRMETRIC](V-RSRCMGRMETRIC.md) "