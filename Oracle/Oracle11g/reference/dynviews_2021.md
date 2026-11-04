---
title: "V$LIBCACHE_LOCKS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2021.htm
tags:
  - oracle
  - 11g
  - reference
---

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
| `MODE_HELD` | `NUMBER` | Lock/pin mode held: |
| `MODE_REQUESTED` | `NUMBER` | Lock/pin mode requested: |
| `SAVEPOINT_NUMBER` | `NUMBER` | Kernel transaction savepoint number at the time the lock/pin was acquired |