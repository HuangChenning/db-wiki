---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LIBRARYCACHE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.37 V$LIBRARYCACHE

`V$LIBRARYCACHE` contains statistics about library cache performance and activity.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(64)` | Library cache namespace |
| `GETS` | `NUMBER` | Number of times a lock was requested for objects of this namespace |
| `GETHITS` | `NUMBER` | Number of times an object's handle was found in memory |
| `GETHITRATIO` | `NUMBER` | Ratio of `GETHITS` to `GETS` |
| `PINS` | `NUMBER` | Number of times a PIN was requested for objects of this namespace |
| `PINHITS` | `NUMBER` | Number of times all of the metadata pieces of the library object were found in memory |
| `PINHITRATIO` | `NUMBER` | Ratio of `PINHITS` to `PINS` |
| `RELOADS` | `NUMBER` | Any `PIN` of an object that is not the first `PIN` performed since the object handle was created, and which requires loading the object from disk |
| `INVALIDATIONS` | `NUMBER` | Total number of times objects in this namespace were marked invalid because a dependent object was modified |
| `DLM_LOCK_REQUESTS` | `NUMBER` | Number of `GET` requests lock instance locks |
| `DLM_PIN_REQUESTS` | `NUMBER` | Number of PIN requests lock instance locks |
| `DLM_PIN_RELEASES` | `NUMBER` | Number of release requests PIN instance locks |
| `DLM_INVALIDATION_REQUESTS` | `NUMBER` | Number of `GET` requests for invalidation instance locks |
| `DLM_INVALIDATIONS` | `NUMBER` | Number of invalidation pings received from other instances |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |