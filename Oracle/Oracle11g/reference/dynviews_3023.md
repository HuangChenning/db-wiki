---
title: "V$SESSION_OBJECT_CACHE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3023.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SESSION_OBJECT_CACHE` displays object cache statistics for the current user session on the local server (instance).

| Column | Datatype | Description |
| --- | --- | --- |
| `PINS` | `NUMBER` | Number of object pins or look-ups in the cache |
| `HITS` | `NUMBER` | Number of object pins that found the object already in the cache |
| `TRUE_HITS` | `NUMBER` | Number of object pins that found the object already in the cache and in the desired state (thus, not requiring refresh from the database) |
| `HIT_RATIO` | `NUMBER` | Ratio of `HITS` / `PINS` |
| `TRUE_HIT_RATIO` | `NUMBER` | Ratio of `TRUE_HITS` / `PINS` |
| `OBJECT_REFRESHES` | `NUMBER` | Number of objects in the cache that were refreshed with a new value from the database |
| `CACHE_REFRESHES` | `NUMBER` | Number of times the whole cache (all objects) were refreshed |
| `OBJECT_FLUSHES` | `NUMBER` | Number of objects in the cache that were flushed to the database |
| `CACHE_FLUSHES` | `NUMBER` | Number of times the whole cache (all objects) were flushed to the database |
| `CACHE_SHRINKS` | `NUMBER` | Number of times the cache was shrunk to the optimal size |
| `CACHED_OBJECTS` | `NUMBER` | Number of objects currently cached |
| `PINNED_OBJECTS` | `NUMBER` | Number of objects currently pinned |
| `CACHE_SIZE` | `NUMBER` | Current size of the cache (in bytes) |
| `OPTIMAL_SIZE` | `NUMBER` | Optimal size of the cache (in bytes) |
| `MAXIMUM_SIZE` | `NUMBER` | Maximum size of the cache (in bytes) |