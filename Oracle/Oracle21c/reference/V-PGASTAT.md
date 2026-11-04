---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PGASTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.121 V$PGASTAT

`V$PGASTAT` displays PGA memory usage statistics as well as statistics about the automatic PGA memory manager when it is enabled (that is, when `PGA_AGGREGATE_TARGET` is set). Cumulative values in `V$PGASTAT` are accumulated since instance startup.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(64)` | Name of the statistic (see Table 9-4) |
| `VALUE` | `NUMBER` | Statistic value |
| `UNIT` | `VARCHAR2(12)` | Unit for the value:  - `bytes` - `microseconds` - `percent` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Table 9-4 V$PGASTAT Statistics

| Statistic Name | Description |
| --- | --- |
| aggregate PGA auto target | Amount of PGA memory the Oracle Database can use for work areas running in automatic mode. This amount is dynamically derived from the value of the `PGA_AGGREGATE_TARGET` initialization parameter and the current work area workload, and continuously adjusted by the Oracle Database.  If this value is small compared to the value of `PGA_AGGREGATE_TARGET`, then a large amount of PGA memory is used by other components of the system (for example, PL/SQL or Java memory) and little is left for work areas. The DBA must ensure that enough PGA memory is left for work areas running in automatic mode. |
| aggregate PGA target parameter | Current value of the `PGA_AGGREGATE_TARGET` initialization parameter. If this parameter is not set, then its value is `0` and automatic management of PGA memory is disabled. |
| bytes processed | Number of bytes processed by memory intensive SQL operators, cumulated since instance startup. |
| cache hit percentage | A metric computed by the Oracle Database to reflect the performance of the PGA memory component, cumulative since instance startup. A value of 100% means that all work areas executed by the system since instance startup have used an optimal amount of PGA memory.  When a work area cannot run optimal, one or more extra passes is performed over the input data. This will reduce the cache hit percentage in proportion to the size of the input data and the number of extra passes performed. |
| extra bytes read/written | Number of bytes processed during extra passes of the input data, cumulated since instance startup. When a work area cannot run optimal, one or more of these extra passes is performed. |
| global memory bound | Maximum size of a work area executed in automatic mode. This value is continuously adjusted by the Oracle Database to reflect the current state of the work area workload. The global memory bound generally decreases when the number of active work areas is increasing in the system.  If the value of the global bound decreases below 1 MB, then the value of `PGA_AGGREGATE_TARGET` should be increased. |
| max processes count | Maximum number of processes active at any one time since instance startup. |
| maximum PGA allocated | Maximum number of bytes of PGA memory allocated at one time since instance startup. |
| maximum PGA used for auto workareas | Maximum amount of PGA memory consumed at one time by work areas running under the automatic memory management mode since instance startup. |
| maximum PGA used for manual workareas | Maximum amount of PGA memory consumed at one time by work areas running under the manual memory management mode since instance startup. |
| over allocation count | This statistic is cumulative since instance startup. Over allocating PGA memory can happen if the value of `PGA_AGGREGATE_TARGET` is too small. When this happens, the Oracle Database cannot honor the value of `PGA_AGGREGATE_TARGET` and extra PGA memory needs to be allocated.  If over allocation occurs, then increase the value of `PGA_AGGREGATE_TARGET` using the information provided by the `V$PGA_TARGET_ADVICE` view. |
| PGA memory freed back to OS | Number of bytes of PGA memory freed back to the operating system, cumulated since instance startup. |
| process count | Number of processes active within up to the last 3 seconds. |
| recompute count (total) | Number of times the instance bound, which is a cap on the maximum size of each active work area, has been recomputed since instance startup. Generally, the instance bound is recomputed in the background every 3 seconds, but it could be recomputed by a foreground process when the number of work areas changes rapidly in a short period of time. |
| total freeable PGA memory | Number of bytes of PGA memory in all processes that could be freed back to the operating system. |
| total PGA allocated | Current amount of PGA memory allocated by the instance. The Oracle Database attempts to keep this number below the value of the `PGA_AGGREGATE_TARGET` initialization parameter. However, it is possible for the PGA allocated to exceed that value by a small percentage and for a short period of time when the work area workload is increasing very rapidly or when `PGA_AGGREGATE_TARGET` is set to a small value. |
| total PGA inuse | Indicates how much PGA memory is currently consumed by work areas. This number can be used to determine how much memory is consumed by other consumers of the PGA memory (for example, PL/SQL or Java). |
| total PGA used for auto workareas | Indicates how much PGA memory is currently consumed by work areas running under the automatic memory management mode. This number can be used to determine how much memory is consumed by other consumers of the PGA memory (for example, PL/SQL or Java). |
| total PGA used for manual workareas | Indicates how much PGA memory is currently consumed by work areas running under the manual memory management mode. This number can be used to determine how much memory is consumed by other consumers of the PGA memory (for example, PL/SQL or Java). |

See Also:

" [PGA\_AGGREGATE\_TARGET](PGA_AGGREGATE_TARGET.md) "