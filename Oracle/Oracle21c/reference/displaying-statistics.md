---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/displaying-statistics.html
tags:
  - oracle
  - 21c
  - reference
---

## E.1 Displaying Statistics

The `V$SESSTAT` view displays statistics on a per-session basis and is valid only for the session currently connected. When a session disconnects, all statistics for the session are updated in `V$SYSSTAT`. The values for the statistics are cleared until the next session uses them.

The `V$STATNAME` view contains all of the statistics for an Oracle release.

Many of these statistics are tied to the internal implementation of Oracle and therefore are subject to change or deletion without notice, even between patch releases. Application developers should be aware of this and write their code to tolerate missing or extra statistics.

See Also:

" [V$SESSTAT](V-SESSTAT.md) ", " [V$STATNAME](V-STATNAME.md) ", and " [V$SYSSTAT](V-SYSSTAT.md) " for more information on these views