---
title: DBA_HIST_PROCESS_MEM_SUMMARY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4026.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_PROCESS_MEM_SUMMARY` displays historical information about dynamic PGA memory usage by named component categories for each process.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `CATEGORY` | `VARCHAR2(15)` | `NOT NULL` | Category name. Categories include "SQL", "PL/SQL", "OLAP" and "JAVA". Special categories are "Freeable" and "Other". Freeable memory has been allocated to the process by the operating system, but has not been allocated to a category. "Other" memory has been allocated to a category, but not to one of the named categories |
| `NUM_PROCESSES` | `NUMBER` |  | Number of processes |
| `NON_ZERO_ALLOCS` | `NUMBER` |  | Number of processes with non-zero allocations |
| `USED_TOTAL` | `NUMBER` |  | Bytes of PGA memory used by the process for the category |
| `ALLOCATED_TOTAL` | `NUMBER` |  | Total number of bytes of PGA memory allocated by the process for the category. |
| `ALLOCATED_AVG` | `NUMBER` |  | Average number of bytes of PGA memory allocated by the process for the category |
| `ALLOCATED_STDDEV` | `NUMBER` |  | Standard deviation of the number of bytes of PGA memory allocated by the process for the category |
| `ALLOCATED_MAX` | `NUMBER` |  | Maximum bytes of PGA memory ever allocated by the process for the category |
| `MAX_ALLOCATED_MAX` | `NUMBER` |  | Maximum bytes of PGA memory that can be allocated by the process for the category |