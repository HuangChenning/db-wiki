---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SYSSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.98 V$SYSSTAT

`V$SYSSTAT` displays system statistics. To find the name of the statistic associated with each statistic number (`STATISTIC#`), query the `V$STATNAME` view.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC#` | `NUMBER` | Statistic number  Note: Statistics numbers are not guaranteed to remain constant from one release to another. Therefore, you should rely on the statistics name rather than its number in your applications. |
| `NAME` | `VARCHAR2(64)` | Statistic name. You can get a complete listing of statistic names by querying the `V$STATNAME` view. |
| `CLASS` | `NUMBER` | A number representing one or more statistics class. The following class numbers are additive:  - `1` - User - `2` - Redo - `4` - Enqueue - `8` - Cache - `16` - OS - `32` - Real Application Clusters - `64` - SQL - `128` - Debug - `256` - Instance level |
| `VALUE` | `NUMBER` | Statistic value |
| `STAT_ID` | `NUMBER` | Identifier of the statistic |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view returns instance-wide data and a value of `0` in the `CON_ID` column when queried from the root of a CDB.

See Also:

" [V$STATNAME](V-STATNAME.md) " and " [Statistics Descriptions](statistics-descriptions.md) "