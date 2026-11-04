---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LIBCACHE_LOCKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.35 V$LIBCACHE\_LOCKS

`V$LIBCACHE_LOCKS` displays information about the library cache locks and pins. Locks and pins are distinguished based on the value of the `TYPE` column.

| Column | Datatype | Description |
| --- | --- | --- |
| `TYPE` | `VARCHAR2(4)` | `LOCK` or `PIN` |
| `ADDR` | `RAW(4 \| 8)` | Address of the lock/pin |
| `HOLDING_USER_SESSION` | `RAW(4 \| 8)` | User session holding this lock/pin |
| `HOLDING_SESSION` | `RAW(4 \| 8)` | Session holding this lock/pin |
| `OBJECT_HANDLE` | `RAW(4 \| 8)` | Handle address for which the lock/pin is acquired |
| `LOCK_HELD` | `RAW(4 \| 8)` | If the type is `LOCK`, then `LOCK_HELD` represents the pin that is pinning the object.  If the type is `PIN`, then `LOCK_HELD` represents the lock that is locking the object. |
| `REFCOUNT` | `NUMBER` | Reference count for this lock/pin |
| `MODE_HELD` | `NUMBER` | Lock/pin mode held:  - `0` - No lock/pin held - `1` - Null mode - `2` - Share mode - `3` - Exclusive mode |
| `MODE_REQUESTED` | `NUMBER` | Lock/pin mode requested:  - `0` - No lock/pin requested - `1` - Null mode - `2` - Share mode - `3` - Exclusive mode |
| `SAVEPOINT_NUMBER` | `NUMBER` | Kernel transaction savepoint number at the time the lock/pin was acquired |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |