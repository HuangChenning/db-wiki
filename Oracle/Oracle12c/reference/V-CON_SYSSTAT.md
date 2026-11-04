---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-CON_SYSSTAT.html
tags:
  - oracle
  - 12c
  - reference
---

`V$CON_SYSSTAT` displays system statistics, including OLAP kernel statistics for the container from which it is queried. To find the name of the statistic associated with each statistic number (`STATISTIC#`), query the `V$STATNAME` view.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC#` | `NUMBER` | Statistic number  Note: Statistics numbers are not guaranteed to remain constant from one release to another. Therefore, you should rely on the statistics name rather than its number in your applications. |
| `NAME` | `VARCHAR2(64)` | Statistic name. You can get a complete listing of statistic names by querying the `V$STATNAME` view. |
| `CLASS` | `NUMBER` | A number representing one or more statistics class. The following class numbers are additive:  - `1` - User - `2` - Redo - `4` - Enqueue - `8` - Cache - `16` - OS - `32` - Real Application Clusters - `64` - SQL - `128` - Debug |
| `VALUE` | `NUMBER` | Statistic value |
| `STAT_ID` | `NUMBER` | Identifier of the statistic |
| `CON_ID` | `NUMBER` | When queried from a non-CDB, the statistics in that instance are returned, and the `CON_ID` value is `0`.  When queried from the root of a CDB, the statistics in every container are returned, and the `CON_ID` value indicates the container to which the statistics belong.  When queried from a PDB, statistics in that PDB are returned, and the `CON_ID` value is the container ID for that PDB. |

See Also:

" [V$STATNAME](V-STATNAME.md) " and " [Statistics Descriptions](statistics-descriptions.md) "