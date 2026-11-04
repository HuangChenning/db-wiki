---
title: DBA_HIST_ROWCACHE_SUMMARY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4028.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_ROWCACHE_SUMMARY` displays historical summary statistics for data dictionary activity. This view contains snapshots of `V$ROWCACHE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `PARAMETER` | `VARCHAR2(32)` |  | Name of the initialization parameter that determines the number of entries in the data dictionary cache |
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