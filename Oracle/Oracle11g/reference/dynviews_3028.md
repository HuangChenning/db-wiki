---
title: "V$SESSTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3028.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SESSTAT` displays user session statistics. To find the name of the statistic associated with each statistic number (`STATISTIC#`), query the `V$STATNAME` view.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier |
| `STATISTIC#` | `NUMBER` | Statistic number  Note: Statistics numbers are not guaranteed to remain constant from one release to another. Therefore, you should rely on the statistics name rather than its number in your applications. |
| `VALUE` | `NUMBER` | Statistic value |

See Also:

["V$STATNAME"](dynviews_3076.md) and [Appendix E, "Statistics Descriptions"](stats.md)