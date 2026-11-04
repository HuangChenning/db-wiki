---
title: "V$SYSSTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3093.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SYSSTAT` displays system statistics. To find the name of the statistic associated with each statistic number (`STATISTIC#`), query the `V$STATNAME` view.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC#` | `NUMBER` | Statistic number  Note: Statistics numbers are not guaranteed to remain constant from one release to another. Therefore, you should rely on the statistics name rather than its number in your applications. |
| `NAME` | `VARCHAR2(64)` | Statistic name. You can get a complete listing of statistic names by querying the `V$STATNAME` view. |
| `CLASS` | `NUMBER` | A number representing one or more statistics class. The following class numbers are additive: |
| `VALUE` | `NUMBER` | Statistic value |
| `STAT_ID` | `NUMBER` | Identifier of the statistic |

See Also:

["V$STATNAME"](dynviews_3076.md) and [Appendix E, "Statistics Descriptions"](stats.md)