---
title: DBMS_CONNECTION_POOL
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_connection_pool.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 37 DBMS\_CONNECTION\_POOL

The DBMS\_CONNECTION\_POOL package provides an interface to manage Database Resident Connection Pool.

See Also:

Oracle Database Concepts for more information on ["Database Resident Connection Pooling"](https://docs.oracle.com/cd/E11882_01/server.112/e40540/dist_pro.htm#CNCPT1896)

This chapter contains the following topic:

- Summary of DBMS\_CONNECTION\_POOL Subprograms

---

## Summary of DBMS\_CONNECTION\_POOL Subprograms

Table 37-1 DBMS\_CONNECTION\_POOL Package Subprograms

| Subprogram | Description |
| --- | --- |
| ALTER\_PARAM Procedure | Alters a specific configuration parameter as a standalone unit and does not affect other parameters |
| CONFIGURE\_POOL Procedure | Configures the pool with advanced options |
| START\_POOL Procedure | Starts the pool for operations. It is only after this call that the pool could be used by connection clients for creating sessions |
| STOP\_POOL Procedure | Stops the pool and makes it unavailable for the registered connection clients |
| RESTORE\_DEFAULTS Procedure | Restores the pool to default settings |

---

### ALTER\_PARAM Procedure

This procedure alters a specific configuration parameter as a standalone unit and does not affect other parameters.

Syntax

```
DBMS_CONNECTION_POOL.ALTER_PARAM (
   pool_name     IN  VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL',   param_name    IN  VARCHAR2,   param_value   IN  VARCHAR2);
```

Parameters

Table 37-2 ALTER\_PARAM Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pool_name` | Pool to be configured. Currently only the default pool name is supported. |
| `param_name` | Any parameter name from `CONFIGURE_POOL` |
| `param_value` | Parameter value for `param_name`. |

Exceptions

Table 37-3 ALTER\_PARAM Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-56500` | Connection pool not found |
| `ORA-56504` | Invalid connection pool configuration parameter name |
| `ORA-56505` | Invalid connection pool configuration parameter value |
| `ORA-56507` | Connection pool alter configuration failed |

Examples

```
DBMS_CONNECTION_POOL.ALTER_PARAM(
   'SYS_DEFAULT_CONNECTION_POOL', 'MAX_LIFETIME_SESSION', '120');
```

---

### CONFIGURE\_POOL Procedure

This procedure configures the pool with advanced options.

Syntax

```
DBMS_CONNECTION_POOL.CONFIGURE_POOL (
   pool_name                IN VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL',
   minsize                  IN NUMBER   DEFAULT 4,
   maxsize                  IN NUMBER   DEFAULT 40,
   incrsize                 IN NUMBER   DEFAULT 2,
   session_cached_cursors   IN NUMBER   DEFAULT 20,
   inactivity_timeout       IN NUMBER   DEFAULT 300,
   max_think_time           IN NUMBER   DEFAULT 120,
   max_use_session          IN NUMBER   DEFAULT 500000,
   max_lifetime_session     IN NUMBER   DEFAULT 86400);
```

Parameters

Table 37-4 CONFIGURE\_POOL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pool_name` | Pool to be configured. Currently only the default pool name is supported. |
| `minsize` | Minimum number of pooled servers in the pool |
| `maxsize` | Maximum allowed pooled servers in the pool |
| `incrsize` | Pool would increment by this number of pooled server when pooled server are unavailable at application request time |
| `session_cached_cursors` | Turn on `SESSION_CACHED_CURSORS` for all connections in the pool. This is an existing `init`.`ora` parameter |
| `inactivity_timeout` | `TTL` (Time to live) for an idle session in the pool. This parameter helps to shrink the pool when it is not used to its maximum capacity. If a connection remains in the pool idle for this time, it is killed. |
| `max_think_time` | Maximum time of inactivity by the client after getting a session from the pool. If the client does not issue a database call after grabbing a server from the pool, the client will be forced to relinquish control of the pooled server and will get an `ORA` - `xxxxx` error. The freed up server may or may not be returned to the pool. |
| `max_use_session` | Maximum number of times a connection can be taken and released to the pool |
| `max_lifetime_session` | `TTL` (Time to live) for a pooled session |

Exceptions

Table 37-5 CONFIGURE\_POOL Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-56500` | Connection pool not found |
| `ORA-56507` | Connection pool alter configuration failed |

Usage Notes

- All expressions of time are in seconds
- All of the parameters should be set based on statistical request patterns.
- `minsize` should be set keeping in mind that it puts a lower bound on server resource consumption. This is to prevent the timeout from dragging the pool too low, because of a brief period of inactivity.
- `maxsize` should be set keeping in mind that it puts an upper bound on concurrency and response-times and also server resource consumption.
- `session_cached_cursors` is typically set to the number of most frequently used statements. It occupies cursor resource on the server
- In doubt, do not set the `increment` and `inactivity_timeout`. The pool will have reasonable defaults.
- `max_use_session` and `max_lifetime_session` allow for software rejuvenation or defensive approaches to potential bugs, leaks, accumulations, and like problems, by getting brand new sessions once in a while.
- The connection pool reserves 5% of the pooled servers for authentication, and at least one pooled server is always reserved for authentication. When setting the `maxsize` parameter, ensure that there are enough pooled servers for both authentication and connections.

---

### START\_POOL Procedure

This procedure starts the pool for operations. It is only after this call that the pool could be used by connection classes for creating sessions.

Syntax

```
DBMS_CONNECTION_POOL.START_POOL (
   pool_name  IN  VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL');
```

Parameters

Table 37-6 START\_POOL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pool_name` | Pool to be started. Currently only the default pool name is supported. |

Exceptions

Table 37-7 START\_POOL Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-56500` | Connection pool not found |
| `ORA-56501` | Connection pool startup failed |

Usage Notes

If the instance is restarted (shutdown followed by startup), the pool is automatically started.

---

### STOP\_POOL Procedure

This procedure stops the pool and makes it unavailable for the registered connection classes.

Syntax

```
DBMS_CONNECTION_POOL.STOP_POOL (
   pool_name   IN   VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL');
```

Parameters

Table 37-8 STOP\_POOL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pool_name` | Pool to be stopped. Currently only the default pool name is supported. |

Exceptions

Table 37-9 STOP\_POOL Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-56500` | Connection pool not found |
| `ORA-56506` | Connection pool shutdown failed |

Usage Notes

This stops the pool and takes it offline. This does not destroy the persistent data (such as, the pool name and configuration parameters) associated with the pool.

---

### RESTORE\_DEFAULTS Procedure

This procedure restores the pool to default settings.

Syntax

```
DBMS_CONNECTION_POOL.RESTORE_DEFAULTS (
   pool_name   IN  VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL');
```

Parameters

Table 37-10 RESTORE\_DEFAULTS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pool_name` | Pool to be restored. Currently only the default pool name is supported. |

Exceptions

Table 37-11 RESTORE\_DEFAULTS Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-56500` | Connection pool not found |
| `ORA-56507` | Connection pool alter configuration failed |

Usage Notes

If the instance is restarted (shutdown followed by startup), the pool is automatically started.