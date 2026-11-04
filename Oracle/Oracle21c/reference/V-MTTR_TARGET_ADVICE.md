---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-MTTR_TARGET_ADVICE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.84 V$MTTR\_TARGET\_ADVICE

`V$MTTR_TARGET_ADVICE` displays rows that predict the number of physical I/Os for the MTTR corresponding to each row.

The rows also compute a physical I/O factor, which is the ratio of the number of estimated I/Os to the number of I/Os actually performed by the current MTTR setting during the measurement interval.

The content of the view is empty if MTTR advisory has not been turned on since database startup. Otherwise, it returns the advisory information collected. If advisory is currently off, then this information comes from the last time MTTR advisory was on. `FAST_START_MTTR_TARGET` must be set to a nonzero value if the `STATISTICS_LEVEL` parameter is dynamically modified to turn MTTR advisory on.

If the `FAST_START_MTTR_TARGET` parameter is changed while MTTR advisory is on, then MTTR advisory is temporarily turned off until the new `FAST_START_MTTR_TARGET` setting takes effect. During this transition period, the contents of `V$MTTR_TARGET_ADVICE` reflect the simulation result for the old MTTR setting.

| Column | Datatype | Description |
| --- | --- | --- |
| `MTTR_TARGET_FOR_ESTIMATE` | `NUMBER` | MTTR setting being simulated. Equal to the current MTTR setting if this is the first row of the view. |
| `ADVICE_STATUS` | `VARCHAR2(5)` | Current status of MTTR simulation:  - `ON` - `READY` - `OFF` |
| `DIRTY_LIMIT` | `NUMBER` | Dirty buffer limit derived from the MTTR being simulated |
| `ESTD_CACHE_WRITES` | `NUMBER` | Estimated number of cache physical writes under this MTTR |
| `ESTD_CACHE_WRITE_FACTOR` | `NUMBER` | Estimated cache physical write ratio under this MTTR. It is the ratio of the estimated number of cache writes to the number of cache writes under the current MTTR setting. |
| `ESTD_TOTAL_WRITES` | `NUMBER` | Estimated total number of physical writes under this MTTR |
| `ESTD_TOTAL_WRITE_FACTOR` | `NUMBER` | Estimated total physical write ratio under this MTTR. It is the ratio of the estimated total number of physical writes to the total number of physical writes under the current MTTR setting. |
| `ESTD_TOTAL_IOS` | `NUMBER` | Estimated total number of I/Os under this MTTR |
| `ESTD_TOTAL_IO_FACTOR` | `NUMBER` | Estimated total I/O ratio under this MTTR. It is the ratio of the estimated total number of I/Os to the total number of I/Os under the current MTTR setting. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [FAST\_START\_MTTR\_TARGET](FAST_START_MTTR_TARGET.md) "
- " [STATISTICS\_LEVEL](STATISTICS_LEVEL.md) "