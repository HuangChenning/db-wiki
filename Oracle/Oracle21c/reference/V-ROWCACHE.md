---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ROWCACHE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.186 V$ROWCACHE

`V$ROWCACHE` displays statistics for data dictionary activity. Each row contains statistics for one data dictionary cache.

| Column | Datatype | Description |
| --- | --- | --- |
| `CACHE#` | `NUMBER` | Row cache ID number |
| `TYPE` | `VARCHAR2(11)` | Parent or subordinate row cache type |
| `SUBORDINATE#` | `NUMBER` | Subordinate set number |
| `PARAMETER` | `VARCHAR2(32)` | Name of the initialization parameter that determines the number of entries in the data dictionary cache |
| `COUNT` | `NUMBER` | Total number of entries in the cache |
| `USAGE` | `NUMBER` | Number of cache entries that contain valid data |
| `FIXED` | `NUMBER` | Number of fixed entries in the cache |
| `GETS` | `NUMBER` | Total number of requests for information on the data object |
| `FASTGETS` | `NUMBER` | Reserved for internal use |
| `GETMISSES` | `NUMBER` | Number of data requests resulting in cache misses |
| `SCANS` | `NUMBER` | Number of scan requests |
| `SCANMISSES` | `NUMBER` | Number of times a scan failed to find the data in the cache |
| `SCANCOMPLETES` | `NUMBER` | For a list of subordinate entries, the number of times the list was scanned completely |
| `MODIFICATIONS` | `NUMBER` | Number of inserts, updates, and deletions |
| `FLUSHES` | `NUMBER` | Number of times flushed to disk |
| `DLM_REQUESTS` | `NUMBER` | Number of DLM requests |
| `DLM_CONFLICTS` | `NUMBER` | Number of DLM conflicts  This column is obsolete and is maintained for backward compatibility. |
| `DLM_RELEASES` | `NUMBER` | Number of DLM releases  This column is obsolete and is maintained for backward compatibility. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |