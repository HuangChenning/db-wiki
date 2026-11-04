---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-JAVA_LIBRARY_CACHE_MEMORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.23 V$JAVA\_LIBRARY\_CACHE\_MEMORY

`V$JAVA_LIBRARY_CACHE_MEMORY` displays information about memory allocated to library cache memory objects in different namespaces for Java objects.

A memory object is an internal grouping of memory for efficient management. A library cache object may consist of one or more memory objects.

| Column | Datatype | Description |
| --- | --- | --- |
| `LC_NAMESPACE` | `VARCHAR2(15)` | Library cache namespace |
| `LC_INUSE_MEMORY_OBJECTS` | `NUMBER` | Number of library cache memory objects currently in use in the Java pool |
| `LC_INUSE_MEMORY_SIZE` | `NUMBER` | Total size of library cache in-use memory objects (in megabytes) |
| `LC_FREEABLE_MEMORY_OBJECTS` | `NUMBER` | Number of freeable library cache memory objects in the Java pool |
| `LC_FREEABLE_MEMORY_SIZE` | `NUMBER` | Size of library cache freeable memory objects (in megabytes) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |