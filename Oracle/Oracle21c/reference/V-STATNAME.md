---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-STATNAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.83 V$STATNAME

`V$STATNAME` displays decoded statistic names for the statistics shown in the `V$SESSTAT` and `V$SYSSTAT` tables.

On some platforms, the `NAME` and `CLASS` columns contain additional operating system-specific statistics.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC#` | `NUMBER` | Statistic number  Note: Statistics numbers are not guaranteed to remain constant from one release to another. Therefore, you should rely on the statistics name rather than its number in your applications. |
| `NAME` | `VARCHAR2(64)` | Statistic name. Names that appear in this column remain stable across Oracle Database releases, and they can be relied on by customer scripts. |
| `CLASS` | `NUMBER` | A number representing one or more statistics classes. The following class numbers are additive:  - `1` - User - `2` - Redo - `4` - Enqueue - `8` - Cache - `16` - OS - `32` - Real Application Clusters - `64` - SQL - `128` - Debug - `256` - Instance level |
| `STAT_ID` | `NUMBER` | Identifier of the statistic |
| `DISPLAY_NAME` | `VARCHAR2(64)` | A clearer and more descriptive name for the statistic that appears in the `NAME` column. Names that appear in the `DISPLAY_NAME` column can change across Oracle Database releases, therefore customer scripts should not rely on names that appear in the `DISPLAY_NAME` column across releases. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$SESSTAT](V-SESSTAT.md) " and " [V$SYSSTAT](V-SYSSTAT.md) "
- " [Statistics Descriptions](statistics-descriptions.md) " for statistic descriptions
- Your operating system-specific Oracle documentation