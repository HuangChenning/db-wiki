---
title: Displaying Statistics
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/stats001.htm
tags:
  - oracle
  - 11g
  - reference
---

The `V$SESSTAT` view displays statistics on a per-session basis and is valid only for the session currently connected. When a session disconnects, all statistics for the session are updated in `V$SYSSTAT`. The values for the statistics are cleared until the next session uses them.

The `V$STATNAME` view contains all of the statistics for an Oracle release.

Many of these statistics are tied to the internal implementation of Oracle and therefore are subject to change or deletion without notice, even between patch releases. Application developers should be aware of this and write their code to tolerate missing or extra statistics.

See Also:

["V$SESSTAT"](dynviews_3028.md), ["V$STATNAME"](dynviews_3076.md), and ["V$SYSSTAT"](dynviews_3093.md) for more information on these views

Press the "Next" button to go to the statistics descriptions.