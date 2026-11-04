---
title: DBA_CPOOL_INFO
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3122.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_CPOOL_INFO` displays configuration information about all Database Resident Connection Pools in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CONNECTION_POOL` | `VARCHAR2(128)` |  | Name of the connection pool |
| `STATUS` | `VARCHAR2(16)` |  | Status of the pool: |
| `MINSIZE` | `NUMBER` |  | Minimum number of pooled servers that are always alive in the pool |
| `MAXSIZE` | `NUMBER` |  | Maximum number of pooled servers in the pool |
| `INCRSIZE` | `NUMBER` |  | Number of pooled servers by which the pool is incremented if servers are unavailable when a client application request is received |
| `SESSION_CACHED_CURSORS` | `NUMBER` |  | Number of session cursors to cache in each pooled server |
| `INACTIVITY_TIMEOUT` | `NUMBER` |  | Maximum time (in seconds) that the pooled server can stay idle in the pool. After this time, the server is terminated. |
| `MAX_THINK_TIME` | `NUMBER` |  | Maximum time of inactivity (in seconds) for a client after obtaining a pooled server from the pool. After obtaining a pooled server from the pool, if the client application does not issue a database call for the time specified by this column, then the pooled server is freed and the client connection is terminated. |
| `MAX_USE_SESSION` | `NUMBER` |  | Number of times a pooled server can be taken and released to the pool |
| `MAX_LIFETIME_SESSION` | `NUMBER` |  | Time (in seconds) for a pooled server to live in the pool |
| `NUM_CBROK` | `NUMBER` |  | Number of connection brokers spawned per instance |
| `MAXCONN_CBROK` | `NUMBER` |  | Maximum number of connections per connection broker |