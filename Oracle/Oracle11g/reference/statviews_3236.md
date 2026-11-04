---
title: DBA_HIST_JAVA_POOL_ADVICE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3236.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_JAVA_POOL_ADVICE` displays historical information about estimated parse time in the Java pool for different pool sizes. This view contains snapshots of `V$JAVA_POOL_ADVICE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `JAVA_POOL_SIZE_FOR_ESTIMATE` | `NUMBER` | `NOT NULL` | Java pool size for the estimate (in megabytes) |
| `JAVA_POOL_SIZE_FACTOR` | `NUMBER` |  | Size factor with respect to the current Java pool size |
| `ESTD_LC_SIZE` | `NUMBER` |  | Estimated memory in use by the library cache (in megabytes) |
| `ESTD_LC_MEMORY_OBJECTS` | `NUMBER` |  | Estimated number of library cache memory objects in the Java pool of the specified size |
| `ESTD_LC_TIME_SAVED` | `NUMBER` |  | Estimated elapsed parse time saved (in seconds), owing to library cache memory objects being found in a Java pool of the specified size. This is the time that would have been spent in reloading the required objects in the Java pool had they been aged out due to insufficient amount of available free memory. |
| `ESTD_LC_TIME_SAVED_FACTOR` | `NUMBER` |  | Estimated parse time saved factor with respect to the current Java pool size |
| `ESTD_LC_LOAD_TIME` | `NUMBER` |  | Estimated elapsed time (in seconds) for parsing in a Java pool of the specified size. |
| `ESTD_LC_LOAD_TIME_FACTOR` | `NUMBER` |  | Estimated load time factor with respect to the current Java pool size |
| `ESTD_LC_MEMORY_OBJECT_HITS` | `NUMBER` |  | Estimated number of times a library cache memory object was found in a Java pool of the specified size |