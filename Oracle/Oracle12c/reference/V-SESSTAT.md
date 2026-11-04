---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-SESSTAT.html
tags:
  - oracle
  - 12c
  - reference
---

To find the name of the statistic associated with each statistic number (`STATISTIC#`), query the `V$STATNAME` view.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier |
| `STATISTIC#` | `NUMBER` | Statistic number  Note: Statistics numbers are not guaranteed to remain constant from one release to another. Therefore, you should rely on the statistics name rather than its number in your applications. |
| `VALUE` | `NUMBER` | Statistic value |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$STATNAME](V-STATNAME.md) " and " [Statistics Descriptions](statistics-descriptions.md) "