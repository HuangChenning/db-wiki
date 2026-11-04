---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-STATISTICS_LEVEL.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.82 V$STATISTICS\_LEVEL

`V$STATISTICS_LEVEL` displays the status of the statistics/advisories controlled by `STATISTICS_LEVEL`.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTICS_NAME` | `VARCHAR2(64)` | Name of the statistic/advisory |
| `DESCRIPTION` | `VARCHAR2(4000)` | Description of the statistic/advisory |
| `SESSION_STATUS` | `VARCHAR2(8)` | Status of the statistic/advisory for the session:  - `ENABLED` - `DISABLED` |
| `SYSTEM_STATUS` | `VARCHAR2(8)` | System-wide status of the statistic/advisory:  - `ENABLED` - `DISABLED` |
| `ACTIVATION_LEVEL` | `VARCHAR2(7)` | Indicates the level of `STATISTICS_LEVEL` that enables the statistic/advisory:  - `BASIC` - `TYPICAL` - `ALL` |
| `STATISTICS_VIEW_NAME` | `VARCHAR2(64)` | If there is a single view externalizing the statistic/advisory, then this column contains the name of that view. If there is no such view, then this column is null. If there are multiple views involved, then the `DESCRIPTION` column mentions the view names. |
| `SESSION_SETTABLE` | `VARCHAR2(3)` | Indicates whether the statistic/advisory can be set at the session level (`YES`) or not (`NO`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [STATISTICS\_LEVEL](STATISTICS_LEVEL.md) "