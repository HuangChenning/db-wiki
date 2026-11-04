---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_PROCESS_MEM_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.28 DBA\_HIST\_PROCESS\_MEM\_SUMMARY

`DBA_HIST_PROCESS_MEM_SUMMARY` displays historical information about dynamic PGA memory usage by named component categories for each process.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `CATEGORY` | `VARCHAR2(15)` | `NOT NULL` | Category name. Categories include "SQL", "PL/SQL", "OLAP" and "JAVA". Special categories are "Freeable" and "Other". Freeable memory has been allocated to the process by the operating system, but has not been allocated to a category. "Other" memory has been allocated to a category, but not to one of the named categories |
| `IS_INSTANCE_WIDE` | `NUMBER` |  | This column shows whether the process memory detail is for only this container or for the whole instance. If the value is `1`, the detail is for the whole instance. Any other value is the container ID for the container to which the detail pertains, as seen in the `CON_ID` column. |
| `NUM_PROCESSES` | `NUMBER` |  | Number of processes |
| `NON_ZERO_ALLOCS` | `NUMBER` |  | Number of processes with nonzero allocations |
| `USED_TOTAL` | `NUMBER` |  | Bytes of PGA memory used by the process for the category |
| `ALLOCATED_TOTAL` | `NUMBER` |  | Total number of bytes of PGA memory allocated by the process for the category. |
| `ALLOCATED_AVG` | `NUMBER` |  | Average number of bytes of PGA memory allocated by the process for the category |
| `ALLOCATED_STDDEV` | `NUMBER` |  | Standard deviation of the number of bytes of PGA memory allocated by the process for the category |
| `ALLOCATED_MAX` | `NUMBER` |  | Maximum bytes of PGA memory ever allocated by the process for the category |
| `MAX_ALLOCATED_MAX` | `NUMBER` |  | Maximum bytes of PGA memory that can be allocated by the process for the category |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |