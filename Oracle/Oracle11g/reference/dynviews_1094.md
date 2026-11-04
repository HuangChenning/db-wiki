---
title: "V$CPOOL_STATS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1094.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$CPOOL_STATS` displays information about the Database Resident Connection Pool statistics for an instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `POOL_NAME` | `VARCHAR2(1024)` | Name of the Database Resident Connection Pool |
| `NUM_OPEN_SERVERS` | `NUMBER` | Total number of busy and free servers in the pool (including the authentication servers) |
| `NUM_BUSY_SERVERS` | `NUMBER` | Total number of busy servers in the pool (not including the authentication servers) |
| `NUM_AUTH_SERVERS` | `NUMBER` | Number of authentication servers in the pool |
| `NUM_REQUESTS` | `NUMBER` | Number of client requests |
| `NUM_HITS` | `NUMBER` | Total number of times client requests found matching pooled servers in the pool |
| `NUM_MISSES` | `NUMBER` | Total number of times client requests could not find a matching pooled server in the pool |
| `NUM_WAITS` | `NUMBER` | Total number of client requests that had to wait due to non-availability of free pooled servers |
| `WAIT_TIME` | `NUMBER` | Reserved for future use |
| `CLIENT_REQ_TIMEOUTS` | `NUMBER` | Reserved for future use |
| `NUM_AUTHENTICATIONS` | `NUMBER` | Total number of authentications of clients done by the pool |
| `NUM_PURGED` | `NUMBER` | Total number of sessions purged by the pool |
| `HISTORIC_MAX` | `NUMBER` | Maximum size that the pool has ever reached |