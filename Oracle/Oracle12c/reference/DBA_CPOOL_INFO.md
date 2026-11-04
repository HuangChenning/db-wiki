---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_CPOOL_INFO.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_CPOOL_INFO` displays configuration information about all Database Resident Connection Pools in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CONNECTION_POOL` | `VARCHAR2(128)` |  | Name of the connection pool |
| `STATUS` | `VARCHAR2(16)` |  | Status of the pool:  - `ACTIVE` - `INACTIVE` |
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
| `MAX_TXN_THINK_TIME` | `NUMBER` |  | Maximum time of inactivity (in seconds) for a client after it obtains a pooled server from the pool and starts a transaction. If the client application does not issue a database call for the time specified by `MAX_TXN_THINK_TIME` while in a transaction, the pooled server is freed, the transaction is rolled back, and the client connection is terminated. The default value is `0`, which means `MAX_THINK_TIME` applies for all connections, irrespective of transactions being open or not in those connections. Care should be taken while setting the two parameters `MAX_THINK_TIME` and `MAX_TXN_THINK_TIME` to higher values, as it would mean the servers are not released to the pool for a longer time, even if clients are not responding for any reason, thereby making other users wait unnecessarily.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN13016) for more information about the configuration parameters for Database Resident Connection Pooling
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS215) for more information on the `DBMS_CONNECTION_POOL` package