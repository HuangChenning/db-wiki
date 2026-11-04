---
title: "V$DB_OBJECT_CACHE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1107.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DB_OBJECT_CACHE` displays database objects that are cached in the library cache. Objects include tables, indexes, clusters, synonym definitions, PL/SQL procedures and packages, and triggers.

| Column | Datatype | Description |
| --- | --- | --- |
| `OWNER` | `VARCHAR2(64)` | Owner of the object |
| `NAME` | `VARCHAR2(1000)` | Name of the object |
| `DB_LINK` | `VARCHAR2(64)` | Database link name, if any |
| `NAMESPACE` | `VARCHAR2(64)` | Library cache namespace of the object: `TABLE/PROCEDURE, BODY, TRIGGER, INDEX, CLUSTER, OBJECT` |
| `TYPE` | `VARCHAR2(64)` | Type of the object: `INDEX, TABLE, CLUSTER, VIEW, SET, SYNONYM, SEQUENCE, PROCEDURE, FUNCTION, PACKAGE, PACKAGE BODY, TRIGGER, CLASS, OBJECT, USER, DBLINK` |
| `SHARABLE_MEM` | `NUMBER` | Amount of sharable memory in the shared pool consumed by the object |
| `LOADS` | `NUMBER` | Number of times the object has been loaded. This count also increases when an object has been invalidated. |
| `EXECUTIONS` | `NUMBER` | Not used  See Also: ["V$SQLAREA"](dynviews_3064.md) to see actual execution counts |
| `LOCKS` | `NUMBER` | Number of users currently locking this object |
| `PINS` | `NUMBER` | Number of users currently pinning this object |
| `KEPT` | `VARCHAR2(3)` | (`YES` \| `NO`) Depends on whether this object has been "kept" (permanently pinned in memory) with the PL/SQL procedure `DBMS_SHARED_POOL.KEEP` |
| `CHILD_LATCH` | `NUMBER` | Child latch number that is protecting the object. This column is obsolete and maintained for backward compatibility. |
| `INVALIDATIONS` | `NUMBER` | Total number of times objects in the namespace were marked invalid because a dependent object was modified |
| `HASH_VALUE` | `NUMBER` | Hash value of the object |
| `LOCK_MODE` | `VARCHAR2(9)` | Current lock mode of the object |
| `PIN_MODE` | `VARCHAR2(9)` | Current pin mode of the object |
| `STATUS` | `VARCHAR2(19)` | Status of the object |
| `TIMESTAMP` | `VARCHAR2(19)` | Timestamp for the specification of the objec |
| `PREVIOUS_TIMESTAMP` | `VARCHAR2(19)` | Previous timestamp for the specification of the object |
| `LOCKED_TOTAL` | `NUMBER` | Total number of times the object has been locked |
| `PINNED_TOTAL` | `NUMBER` | Total number of times the object has been pinned |