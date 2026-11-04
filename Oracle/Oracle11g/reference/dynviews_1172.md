---
title: "V$HANG_STATISTICS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1172.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$HANG_STATISTICS` displays statistics about hangs found on the cluster.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC#` | `NUMBER` | Statistic number |
| `NAME` | `VARCHAR2(45)` | Name of the statistic |
| `VALUE` | `NUMBER` | Value associated with the statistic |

See Also:

- ["V$HANG\_INFO"](dynviews_1170.md)
- ["V$HANG\_SESSION\_INFO"](dynviews_1171.md)