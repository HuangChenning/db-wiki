---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_LIBRARYCACHE.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.6 DBA\_HIST\_LIBRARYCACHE

`DBA_HIST_LIBRARYCACHE` displays historical statistics about library cache performance and activity.

This view contains snapshots of `V$LIBRARYCACHE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `NAMESPACE` | `VARCHAR2(15)` | `NOT NULL` | Library cache namespace |
| `GETS` | `NUMBER` |  | Number of times a lock was requested for objects of the namespace |
| `GETHITS` | `NUMBER` |  | Number of times an object's handle was found in memory |
| `PINS` | `NUMBER` |  | Number of times a PIN was requested for objects of the namespace |
| `PINHITS` | `NUMBER` |  | Number of times all of the metadata pieces of the library object were found in memory |
| `RELOADS` | `NUMBER` |  | Any PIN of an object that is not the first PIN performed since the object handle was created, and which requires loading the object from disk |
| `INVALIDATIONS` | `NUMBER` |  | Total number of times objects in the namespace were marked invalid because a dependent object was modified |
| `DLM_LOCK_REQUESTS` | `NUMBER` |  | Number of GET requests lock instance locks |
| `DLM_PIN_REQUESTS` | `NUMBER` |  | Number of PIN requests lock instance locks |
| `DLM_PIN_RELEASES` | `NUMBER` |  | Number of release requests PIN instance locks |
| `DLM_INVALIDATION_REQUESTS` | `NUMBER` |  | Number of GET requests for invalidation instance locks |
| `DLM_INVALIDATIONS` | `NUMBER` |  | Number of invalidation pings received from other instances |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$LIBRARYCACHE](V-LIBRARYCACHE.md) "