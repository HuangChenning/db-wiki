---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DB_OBJECT_CACHE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.165 V$DB\_OBJECT\_CACHE

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
| `EXECUTIONS` | `NUMBER` | Not used  See Also: " [V$SQLAREA](V-SQLAREA.md) " to see actual execution counts |
| `LOCKS` | `NUMBER` | Number of users currently locking this object |
| `PINS` | `NUMBER` | Number of users currently pinning this object |
| `KEPT` | `VARCHAR2(3)` | (`YES` \| `NO`) Depends on whether this object has been "kept" (permanently pinned in memory) with the PL/SQL procedure `DBMS_SHARED_POOL.KEEP` |
| `CHILD_LATCH` | `NUMBER` | Child latch number that is protecting the object. This column is obsolete and maintained for backward compatibility. |
| `INVALIDATIONS` | `NUMBER` | Total number of times objects in the namespace were marked invalid because a dependent object was modified |
| `HASH_VALUE` | `NUMBER` | Hash value of the object |
| `LOCK_MODE` | `VARCHAR2(9)` | Current lock mode of the object |
| `PIN_MODE` | `VARCHAR2(9)` | Current pin mode of the object |
| `STATUS` | `VARCHAR2(19)` | Status of the object |
| `TIMESTAMP` | `VARCHAR2(19)` | Timestamp for the specification of the object |
| `PREVIOUS_TIMESTAMP` | `VARCHAR2(19)` | Previous timestamp for the specification of the object |
| `LOCKED_TOTAL` | `NUMBER` | Total number of times the object has been locked |
| `PINNED_TOTAL` | `NUMBER` | Total number of times the object has been pinned |
| `PROPERTY` | `VARCHAR2(80)` | Property of the object. Possible values include `HOT` or `HOTCOPY` when the library cache hot copy feature is used using `DBMS_SHARED_POOL.MARKHOT`. |
| `FULL_HASH_VALUE` | `VARCHAR2(32)` | Full hash value of the object |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `CON_NAME` | `VARCHAR2(64)` | Container name of the object. The value of this column is `NULL` in non-CDBs. |
| `ADDR` | `RAW(8)` | Address of the handle for this object |
| `EDITION` | `VARCHAR2(138)` | Edition name |

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS68083) for more information about the `DBMS_SHARED_POOL.KEEP` procedure
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS68085) for more information about the `DBMS_SHARED_POOL.MARKHOT` procedure