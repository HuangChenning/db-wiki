---
title: "V$STATISTICS_LEVEL"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3075.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$STATISTICS_LEVEL` displays the status of the statistics/advisories controlled by `STATISTICS_LEVEL`.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTICS_NAME` | `VARCHAR2(64)` | Name of the statistic/advisory |
| `DESCRIPTION` | `VARCHAR2(4000)` | Description of the statistic/advisory |
| `SESSION_STATUS` | `VARCHAR2(8)` | Status of the statistic/advisory for the session: |
| `SYSTEM_STATUS` | `VARCHAR2(8)` | System-wide status of the statistic/advisory: |
| `ACTIVATION_LEVEL` | `VARCHAR2(7)` | Indicates the level of `STATISTICS_LEVEL` that enables the statistic/advisory: |
| `STATISTICS_VIEW_NAME` | `VARCHAR2(64)` | If there is a single view externalizing the statistic/advisory, then this column contains the name of that view. If there is no such view, then this column is null. If there are multiple views involved, then the `DESCRIPTION` column mentions the view names. |
| `SESSION_SETTABLE` | `VARCHAR2(3)` | Indicates whether the statistic/advisory can be set at the session level (`YES`) or not (`NO`) |

See Also:

["STATISTICS\_LEVEL"](initparams254.md)