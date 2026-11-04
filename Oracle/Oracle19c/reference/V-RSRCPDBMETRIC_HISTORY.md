---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-RSRCPDBMETRIC_HISTORY.html
tags:
  - oracle
  - 19c
  - reference
---

## 8.198 V$RSRCPDBMETRIC\_HISTORY

`V$RSRCPDBMETRIC_HISTORY` displays a history (the last one hour) of resource manager metrics for a PDB, taken from `V$RSRCPDBMETRIC`. When a resource plan is set, this history is cleared and restarted. This view provides information about resources consumed and wait times per consumer group.

The columns for `V$RSRCPDBMETRIC_HISTORY` are the same as those for `V$RSRCPDBMETRIC`.

See Also:

" [V$RSRCPDBMETRIC](V-RSRCPDBMETRIC.md) "