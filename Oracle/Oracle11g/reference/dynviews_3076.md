---
title: "V$STATNAME"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3076.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$STATNAME` displays decoded statistic names for the statistics shown in the `V$SESSTAT` and `V$SYSSTAT` tables.

On some platforms, the `NAME` and `CLASS` columns contain additional operating system-specific statistics.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC#` | `NUMBER` | Statistic number  Note: Statistics numbers are not guaranteed to remain constant from one release to another. Therefore, you should rely on the statistics name rather than its number in your applications. |
| `NAME` | `VARCHAR2(64)` | Statistic name |
| `CLASS` | `NUMBER` | A number representing one or more statistics classes. The following class numbers are additive: |
| `STAT_ID` | `NUMBER` | Identifier of the statistic |

See Also:

- ["V$SESSTAT"](dynviews_3028.md) and ["V$SYSSTAT"](dynviews_3093.md)
- [Appendix E, "Statistics Descriptions"](stats.md) for a description of each statistic
- Your operating system-specific Oracle documentation