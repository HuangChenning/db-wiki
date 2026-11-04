---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_CPOOL_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.248 DBA\_CPOOL\_INFO

`DBA_CPOOL_INFO` displays configuration information about all Database Resident Connection Pools in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CONNECTION_POOL` | `VARCHAR2(128)` |  | Name of the connection pool |
| `STATUS` | `VARCHAR2(16)` |  | Status of the pool:  - `ACTIVE` - `INACTIVE` |
| `MINSIZE` | `NUMBER` |  | Minimum number of pooled servers that are always running in the pool |
| `MAXSIZE` | `NUMBER` |  | Maximum number of pooled servers in the pool |
| `INCRSIZE` | `NUMBER` |  | Number of pooled servers by which the pool is incremented if servers are unavailable when a client application request is received |
| `SESSION_CACHED_CURSORS` | `NUMBER` |  | Number of session cursors to cache in each pooled server |
| `INACTIVITY_TIMEOUT` | `NUMBER` |  | Maximum time (in seconds) that the pooled server can stay idle in the pool. After this time, the server is terminated. |
| `MAX_THINK_TIME` | `NUMBER` |  | Maximum time of inactivity (in seconds) for a client after obtaining a pooled server from the pool. After obtaining a pooled server from the pool, if the client application does not issue a database call for the time specified by this column, then the pooled server is freed and the client connection is terminated. |
| `MAX_USE_SESSION` | `NUMBER` |  | Maximum number of acquire-and-release cycles allowed for a pooled server before it is terminated and replaced  The default value is `500000`. A value of `0` indicates that the usage limit is disabled. |
| `MAX_LIFETIME_SESSION` | `NUMBER` |  | Maximum lifetime (in seconds) for a pooled server  If the lifetime expires for a server that is being returned to the pool or is free in the pool, it is removed from the pool and cleaned up.  The default value is `86400`. A value of `0` indicates that the lifetime limit is disabled. |
| `NUM_CBROK` | `NUMBER` |  | Number of connection brokers spawned per instance |
| `MAXCONN_CBROK` | `NUMBER` |  | Maximum number of connections per connection broker |
| `MAX_TXN_THINK_TIME` | `NUMBER` |  | Maximum time of inactivity (in seconds) for a client after it obtains a pooled server from the pool and starts a transaction. If the client application does not issue a database call for the time specified by `MAX_TXN_THINK_TIME` while in a transaction, the pooled server is freed, the transaction is rolled back, and the client connection is terminated. The default value is `0`, which means `MAX_THINK_TIME` applies for all connections, irrespective of transactions being open or not in those connections. Care should be taken while setting the two parameters `MAX_THINK_TIME` and `MAX_TXN_THINK_TIME` to higher values, as it would mean the servers are not released to the pool for a longer time, even if clients are not responding for any reason, thereby making other users wait unnecessarily. |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN13016) for more information about the configuration parameters for Database Resident Connection Pooling
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS215) for more information on the `DBMS_CONNECTION_POOL` package