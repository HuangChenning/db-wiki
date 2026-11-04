---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_ROWCACHE_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.38 DBA\_HIST\_ROWCACHE\_SUMMARY

`DBA_HIST_ROWCACHE_SUMMARY` displays historical summary statistics for data dictionary activity.

This view contains snapshots of `V$ROWCACHE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `PARAMETER` | `VARCHAR2(32)` | `NOT NULL` | Name of the initialization parameter that determines the number of entries in the data dictionary cache |
| `TOTAL_USAGE` | `NUMBER` |  | Sum of the total number of entries in the cache |
| `USAGE` | `NUMBER` |  | Number of cache entries that contain valid data |
| `GETS` | `NUMBER` |  | Total number of requests for information on the data object |
| `GETMISSES` | `NUMBER` |  | Number of data requests resulting in cache misses |
| `SCANS` | `NUMBER` |  | Number of scan requests |
| `SCANMISSES` | `NUMBER` |  | Number of times a scan failed to find the data in the cache |
| `SCANCOMPLETES` | `NUMBER` |  | For a list of subordinate entries, the number of times the list was scanned completely |
| `MODIFICATIONS` | `NUMBER` |  | Number of inserts, updates, and deletions |
| `FLUSHES` | `NUMBER` |  | Number of times flushed to disk |
| `DLM_REQUESTS` | `NUMBER` |  | Number of DLM requests |
| `DLM_CONFLICTS` | `NUMBER` |  | Number of DLM conflicts |
| `DLM_RELEASES` | `NUMBER` |  | Number of DLM releases |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$ROWCACHE](V-ROWCACHE.md) "