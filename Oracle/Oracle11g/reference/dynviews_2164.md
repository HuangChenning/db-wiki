---
title: "V$RSRCMGRMETRIC_HISTORY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2164.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RSRCMGRMETRIC_HISTORY` displays a history (the last one hour) of resource manager metrics, taken from `V$RSRCMGRMETRIC`. When a resource plan is set, this history is cleared and restarted. This view provides information about resources consumed and wait times per consumer group.

The columns for `V$RSRCMGRMETRIC_HISTORY` are the same as those for `V$RSRCMGRMETRIC`.

See Also:

["V$RSRCMGRMETRIC"](dynviews_2163.md)