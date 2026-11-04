---
title: "V$SHARED_POOL_ADVICE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3037.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SHARED_POOL_ADVICE` displays information about estimated parse time in the shared pool for different pool sizes. The sizes range from 10% of the current shared pool size or the amount of pinned library cache memory (whichever is higher) to 200% of the current shared pool size, in equal intervals. The value of the interval depends on the current size of the shared pool.

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