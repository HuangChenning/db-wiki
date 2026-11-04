---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-RSRCPDBMETRIC_HISTORY.html
tags:
  - oracle
  - 12c
  - reference
---

`V$RSRCPDBMETRIC_HISTORY` displays a history (the last one hour) of resource manager metrics for a PDB, taken from `V$RSRCPDBMETRIC`. When a resource plan is set, this history is cleared and restarted. This view provides information about resources consumed and wait times per consumer group.

The columns for `V$RSRCPDBMETRIC_HISTORY` are the same as those for `V$RSRCPDBMETRIC`.

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

" [V$RSRCPDBMETRIC](V-RSRCPDBMETRIC.md) "