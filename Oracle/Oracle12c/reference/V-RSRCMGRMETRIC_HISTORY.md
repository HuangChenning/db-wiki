---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-RSRCMGRMETRIC_HISTORY.html
tags:
  - oracle
  - 12c
  - reference
---

`V$RSRCMGRMETRIC_HISTORY` displays a history (the last one hour) of resource manager metrics, taken from `V$RSRCMGRMETRIC`. When a resource plan is set, this history is cleared and restarted. This view provides information about resources consumed and wait times per consumer group.

The columns for `V$RSRCMGRMETRIC_HISTORY` are the same as those for `V$RSRCMGRMETRIC`.

See Also:

" [V$RSRCMGRMETRIC](V-RSRCMGRMETRIC.md) "