---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SHARED_POOL_ADVICE.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.39 V$SHARED\_POOL\_ADVICE

The sizes range from 10% of the current shared pool size or the amount of pinned library cache memory (whichever is higher) to 200% of the current shared pool size, in equal intervals. The value of the interval depends on the current size of the shared pool.

| Column | Datatype | Description |
| --- | --- | --- |
| `SHARED_POOL_SIZE_FOR_ESTIMATE` | `NUMBER` | Shared pool size for the estimate (in megabytes) |
| `SHARED_POOL_SIZE_FACTOR` | `NUMBER` | Size factor with respect to the current shared pool size |
| `ESTD_LC_SIZE` | `NUMBER` | Estimated memory in use by the library cache (in megabytes) |
| `ESTD_LC_MEMORY_OBJECTS` | `NUMBER` | Estimated number of library cache memory objects in the shared pool of the specified size |
| `ESTD_LC_TIME_SAVED` | `NUMBER` | Estimated elapsed parse time saved (in seconds), owing to library cache memory objects being found in a shared pool of the specified size. This is the time that would have been spent in reloading the required objects in the shared pool had they been aged out due to insufficient amount of available free memory. |
| `ESTD_LC_TIME_SAVED_FACTOR` | `NUMBER` | Estimated parse time saved factor with respect to the current shared pool size |
| `ESTD_LC_LOAD_TIME` | `NUMBER` | Estimated elapsed time (in seconds) for parsing in a shared pool of the specified size |
| `ESTD_LC_LOAD_TIME_FACTOR` | `NUMBER` | Estimated load time factor with respect to the current shared pool size |
| `ESTD_LC_MEMORY_OBJECT_HITS` | `NUMBER` | Estimated number of times a library cache memory object was found in a shared pool of the specified size |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |