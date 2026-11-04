---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RESULT_SUBCACHE_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.174 V$RESULT\_SUBCACHE\_STATISTICS

`V$RESULT_SUBCACHE_STATISTICS` displays various result cache settings and usage statistics on a per subcache basis.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Statistic number |
| `NAME` | `VARCHAR2(128)` | Name of the statistic  This view displays the same statistics as the `V$RESULT_CACHE_STATISTICS` view. See [Table 9-6](V-RESULT_CACHE_STATISTICS.md) in the documentation for V$RESULT\_CACHE\_STATISTICS. |
| `VALUE` | `VARCHAR2(81)` | Value of the statistic |
| `SUBCACHE_ID` | `NUMBER` | Subcache ID |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.

See Also:

" [V$RESULT\_CACHE\_STATISTICS](V-RESULT_CACHE_STATISTICS.md) "