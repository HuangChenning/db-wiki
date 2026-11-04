---
title: "V$JAVA_LIBRARY_CACHE_MEMORY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2013.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$JAVA_LIBRARY_CACHE_MEMORY` displays information about memory allocated to library cache memory objects in different namespaces for Java objects. A memory object is an internal grouping of memory for efficient management. A library cache object may consist of one or more memory objects.

| Column | Datatype | Description |
| --- | --- | --- |
| `LC_NAMESPACE` | `VARCHAR2(15)` | Library cache namespace |
| `LC_INUSE_MEMORY_OBJECTS` | `NUMBER` | Number of library cache memory objects currently in use in the Java pool |
| `LC_INUSE_MEMORY_SIZE` | `NUMBER` | Total size of library cache in-use memory objects (in megabytes) |
| `LC_FREEABLE_MEMORY_OBJECTS` | `NUMBER` | Number of freeable library cache memory objects in the Java pool |
| `LC_FREEABLE_MEMORY_SIZE` | `NUMBER` | Size of library cache freeable memory objects (in megabytes) |