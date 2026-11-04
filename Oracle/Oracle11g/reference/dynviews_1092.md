---
title: "V$CPOOL_CC_STATS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1092.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$CPOOL_CC_STATS` displays information about the connection class level statistics for the Database Resident Connection Pool per instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `CCLASS_NAME` | `VARCHAR2(1024)` | Name of the connection class |
| `NUM_REQUESTS` | `NUMBER` | Number of session requests |
| `NUM_HITS` | `NUMBER` | Total number of times a session that matches with the request was found in the pool |
| `NUM_MISSES` | `NUMBER` | Total number of times an exact match to the request was not found in the pool and a new session had to be created |
| `NUM_WAITS` | `NUMBER` | Total number of times session requests had to wait before getting served |
| `WAIT_TIME` | `NUMBER` | Reserved for future use |
| `CLIENT_REQ_TIMEOUTS` | `NUMBER` | Reserved for future use |
| `NUM_AUTHENTICATIONS` | `NUMBER` | Total number of authentications of clients done by the pool |