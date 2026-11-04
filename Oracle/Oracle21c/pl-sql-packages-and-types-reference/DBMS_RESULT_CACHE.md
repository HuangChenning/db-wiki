---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_RESULT_CACHE.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 150 DBMS\_RESULT\_CACHE

The `DBMS_RESULT_CACHE` package provides an interface to allow the DBA to administer that part of the shared pool that is used by the SQL result cache and the PL/SQL function result cache.

Both these caches use the same infrastructure. Therefore, for example, `DBMS_RESULT_CACHE`.`BYPASS` determines whether both caches are bypassed or both caches are used, and `DBMS_RESULT_CACHE`.`FLUSH` flushes both all the cached results for SQL queries and all the cached results for PL/SQL functions.

This chapter contains the following topics:

See Also:

- Oracle Database Performance Tuning Guide, for more information about ["Result Cache Concepts"](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=TGDBA638)
- Oracle Database PL/SQL Language Reference, for more information about PL/SQL function Result Cache ["Using the Cross-Session PL/SQL Function Result Cache"](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=LNPLS00817)
- Database PL/SQL Language Reference, for more information about [Result Cache Management](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=LNPLS-GUID-4051143D-CABC-4395-BF7C-915253CA4CAB).

### 150.1 DBMS\_RESULT\_CACHE Security Model

Only database administrators should be granted the `EXECUTE` privilege for this package.

### 150.2 DBMS\_RESULT\_CACHE Constants

The `DBMS_RESULT_CACHE` package defines several constants for specifying parameter values.

The following table describes these constants.

Table 150-1 DBMS\_RESULT\_CACHE Constants

| Constant | Definition | Description |
| --- | --- | --- |
| `STATUS_BYPS` | `CONSTANT VARCHAR2(10) := 'BYPASS';` | Cache has been made temporarilyunavailable. |
| `STATUS_CORR` | `CONSTANT VARCHAR2(10) := 'CORRUPT';` | The result cache is in an unusable state. |
| `STATUS_DISA` | `CONSTANT VARCHAR2(10) :=                                 'DISABLED';` | Cache is not available. |
| `STATUS_ENAB` | `CONSTANT VARCHAR2(10) := 'ENABLED';` | Cache is available. |
| `STATUS_SYNC` | `CONSTANT VARCHAR2(10) := 'SYNC'; ` | Cache is available, but synchronizing with Oracle RAC nodes. |

### 150.3 Summary of DBMS\_RESULT\_CACHE Subprograms

This table lists the `DBMS_RESULT_CACHE` subprograms and briefly describes them.

Table 150-2 DBMS\_RESULT\_CACHE Package Subprograms

| Subprogram | Description |
| --- | --- |
| BLACK\_LIST Function | Returns all the blocklisted cache ids of a local instance. |
| BLACK\_LIST\_ADD Procedure | Adds a `cache_id` to the blocklist. |
| BLACK\_LIST\_CLEAR Procedure | Removes all cache\_ids from the blocklist. |
| BLACK\_LIST\_REMOVE Procedure | Removes the `cache_id` from the blocklist. |
| BYPASS Procedure | Sets the bypass mode for the result cache. |
| DELETE\_DEPENDENCY Functions & Procedures | Deletes the specified dependency object from the result cache, while invalidating all results that used that dependency object. |
| FLUSH Function & Procedure | Attempts to remove all the objects from the result cache, and depending on the arguments retains or releases the memory and retains or clears the statistics. |
| INVALIDATE Functions & Procedures | Invalidates all the result-set objects that are dependent upon the specified dependency object. |
| INVALIDATE\_OBJECT Functions & Procedures | Invalidates the specified result-set object(s) |
| MEMORY\_REPORT Procedure | Produces the memory usage report for the result cache. |
| OBJECT\_BLACK\_LIST Function | Returns all the object numbers currently in the blocklist |
| OBJECT\_BLACK\_LIST\_ADD Procedure | Adds objects to the object blocklist |
| OBJECT\_BLACK\_LIST\_CLEAR Procedure | Clears the entire blocklist |
| OBJECT\_BLACK\_LIST\_REMOVE Procedure | Removes objects from the object blocklist. |
| STATUS Function | Checks the status of the result cache. |

#### 150.3.1 BLACK\_LIST Function

This table function returns all the blocklisted cache ids of a local instance.

Syntax

```
DBMS_RESULT_CACHE.BLACK_LIST
   RETURN BL_TABT;
```

#### 150.3.2 BLACK\_LIST\_ADD Procedure

This procedure adds a cache\_id to the blocklist.

Syntax

```
DBMS_RESULT_CACHE.BLACK_LIST_ADD (
   cache_id   IN  VARCHAR2,
   global     IN  BOOLEAN DEFAULT FALSE);
```

Parameters

Table 150-3 BLACK\_LIST\_ADD Procedure Parameters

| Parameter | Description |
| --- | --- |
| `cache_id` | The `cache_id` is added to the blocklist. |
| `global` | `TRUE` — applies to all caches in a RAC cluster.  `FALSE` (default) — applies only to the local instance cache. |

#### 150.3.3 BLACK\_LIST\_CLEAR Procedure

This procedure removes all cache\_ids from the blocklist.

Syntax

```
DBMS_RESULT_CACHE.BLACK_LIST_CLEAR (
   global   IN  BOOLEAN DEFAULT FALSE);
```

Parameters

Table 150-4 BLACK\_LIST\_CLEAR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `global` | `TRUE` — applies to all caches in a RAC cluster.  `FALSE` (default) — applies only to the local instance cache. |

#### 150.3.4 BLACK\_LIST\_REMOVE Procedure

This procedures removes the cache\_id from the blocklist.

Syntax

```
DBMS_RESULT_CACHE.BLACK_LIST_REMOVE (
   cache_id   IN  VARCHAR2,
   global     IN  BOOLEAN DEFAULT FALSE);
```

Parameters

Table 150-5 BLACK\_LIST\_REMOVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `cache_id` | The `cache_id` is removed from the blocklist. |
| `global` | `TRUE` — applies to all caches in a RAC cluster.  `FALSE` (default) — applies only to the local instance cache. |

#### 150.3.5 BYPASS Procedure

This procedure sets the bypass mode for the Result Cache.

It sets one of the following bypass modes:

- When bypass mode is turned on, it implies that cached results are no longer used and that no new results are saved in the cache.
- When bypass mode is turned off, the cache resumes normal operation.

Syntax

```
DBMS_RESULT_CACHE.BYPASS (
   bypass_mode    IN   BOOLEAN,
   session        IN   BOOLEAN);
```

Parameters

Table 150-6 BYPASS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `bypass_mode` | - `TRUE` => Result Cache usage is bypassed - `FALSE` => Result Cache usage is turned on |
| `session` | - `TRUE` => Applies to current session - `FALSE` (default) => Applies to all sessions |

Usage Notes

This operation is database instance specific.

Examples

This operation can be used when there is a need to hot patch PL/SQL code in a running system. If a code-patch is applied to a PL/SQL module on which a result cached function directly or transitively depends, then the cached results associated with the result cache function are not automatically flushed (if the instance is not restarted/bounced). This must be manually achieved.

To ensure correctness during the patching process follow these steps:

1. Place the result cache in bypass mode, and flush existing result.
	```
	BEGIN
	   DBMS_RESULT_CACHE.BYPASS(TRUE);
	   DBMS_RESULT_CACHE.FLUSH;
	END;
	/
	```
	This step must be performed on each instance if in a Oracle Real Application Clusters environment.
2. Apply the PL/SQL code patches.
3. Resume use of the result cache, by turning off the cache bypass mode.
	```
	BEGIN
	   DBMS_RESULT_CACHE.BYPASS(FALSE);
	END;
	/
	```
	This step must be performed on each instance if in a Oracle Real Application Clusters environment.

#### 150.3.6 DELETE\_DEPENDENCY Functions & Procedures

These functions and procedures delete the specified dependency object from the result cache, while invalidating all results that used that dependency object.

Syntax

```
DBMS_RESULT_CACHE.DELETE_DEPENDENCY (
   owner        IN  VARCHAR2, 
   name         IN  VARCHAR2) 
 RETURN NUMBER;
```
```
DBMS_RESULT_CACHE.DELETE_DEPENDENCY (
   owner       IN  VARCHAR2, 
   name        IN  VARCHAR2);
```
```
DBMS_RESULT_CACHE.DELETE_DEPENDENCY (
  object_id    IN BINARY_INTEGER) 
 RETURN NUMBER;
```
```
DBMS_RESULT_CACHE.DELETE_DEPENDENCY (
   object_id    IN BINARY_INTEGER);
```

Parameters

Table 150-7 DELETE\_DEPENDENCY Function & Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner` | Schema name |
| `name` | Object name |
| `object_id` | Dictionary object number |

Return Values

The number of objects deleted.

Note:

Unlike `INVALIDATE`, `DELETE_DEPENDENCY` is used to remove a dependency object from the result cache. For example, when a query result is cached, the tables involved in that query are added to certain result cache data structures. In RAC, every time a transaction commits on those tables, extra processing occurs. If this overhead grows too large, it can cause slowdowns or brownouts. `DELETE_DEPENDENCY` lets you remove a table from the result cache data structures, stopping the extra work and preventing brownouts.

#### 150.3.7 FLUSH Function & Procedure

This function and procedure attempts to remove all the objects from the Result Cache, and depending on the arguments retains or releases the memory and retains or clears the statistics.

Syntax

```
DBMS_RESULT_CACHE.FLUSH (
   retainMem  IN  BOOLEAN DEFAULT FALSE,
   retainSta  IN  BOOLEAN DEFAULT FALSE,
   global     IN  BOOLEAN DEFAULT FALSE)
  RETURN BOOLEAN;
```
```
DBMS_RESULT_CACHE.FLUSH (
   retainMem  IN  BOOLEAN DEFAULT FALSE,
   retainSta  IN  BOOLEAN DEFAULT FALSE,
   global     IN  BOOLEAN DEFAULT FALSE);
```

Parameters

Table 150-8 FLUSH Function & Procedure Parameters

| Parameter | Description |
| --- | --- |
| `retainMem` | - `TRUE` => retains the free memory in the cache - `FALSE` (default) => releases the free memory to the system |
| `retainSta` | - `TRUE` => retains the existing cache statistics - `FALSE` (default) => clears the existing cache statistics |
| `global` | - `TRUE` => flushes all caches in the RAC cluster - `FALSE` (default) => flushes only the local instance cache |

Return Values

`TRUE` if successful in removing all the objects.

#### 150.3.8 INVALIDATE Functions & Procedures

This function and procedure invalidates all the result-set objects that dependent upon the specified dependency object.

Syntax

```
DBMS_RESULT_CACHE.INVALIDATE (
   owner        IN  VARCHAR2, 
   name         IN  VARCHAR2) 
 RETURN NUMBER;
```
```
DBMS_RESULT_CACHE.INVALIDATE (
   owner       IN  VARCHAR2, 
   name        IN  VARCHAR2);
```
```
DBMS_RESULT_CACHE.INVALIDATE (
  object_id    IN BINARY_INTEGER) 
 RETURN NUMBER;
```
```
DBMS_RESULT_CACHE.INVALIDATE (
   object_id    IN BINARY_INTEGER);
```

Parameters

Table 150-9 INVALIDATE Function & Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner` | Schema name |
| `name` | Object name |
| `object_id` | Dictionary object number |

Return Values

The number of objects invalidated.

#### 150.3.9 INVALIDATE\_OBJECT Functions & Procedures

This function and procedure invalidates the specified result-set object(s).

Syntax

```
DBMS_RESULT_CACHE.INVALIDATE_OBJECT (
   id          IN  BINARY_INTEGER) 
 RETURN NUMBER;
```
```
DBMS_RESULT_CACHE.INVALIDATE_OBJECT (
   id          IN  BINARY_INTEGER);
```
```
DBMS_RESULT_CACHE.INVALIDATE_OBJECT (
  cache_id     IN  VARCHAR2) 
 RETURN NUMBER;
```
```
DBMS_RESULT_CACHE.INVALIDATE_OBJECT (
   cache_id   IN  VARCHAR2);
```

Parameters

Table 150-10 INVALIDATE\_OBJECT Function & Procedure Parameters

| Parameter | Description |
| --- | --- |
| `id` | Address of the cache object in the Result Cache |
| `cache_id` | Result cache identifier of a SQL cursor or PL/SQL function. |

Return Values

The number of objects invalidated.

#### 150.3.10 MEMORY\_REPORT Procedure

This procedure produces the memory usage report for the Result Cache.

Syntax

```
DBMS_RESULT_CACHE.MEMORY_REPORT (
   detailed   IN   BOOLEAN DEFAULT FALSE);
```

Parameters

Table 150-11 MEMORY\_REPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `detailed` | - `TRUE` => produces a more detailed report - `FALSE` (default) => produces the standard report |

Usage Notes

Invoking this procedure from SQL\*Plus requires that the serveroutput be turned on.

Examples

```
SET SERVEROUTPUT ON

EXECUTE DBMS_RESULT_CACHE.MEMORY_REPORT;
```

#### 150.3.11 OBJECT\_BLACK\_LIST Function

This table function returns all the object numbers currently in the blocklist.

Syntax

```
DBMS_RESULT_CACHE.OBJECT_BLACK_LIST ()
   RETURN NATURALN;
```

#### 150.3.12 OBJECT\_BLACK\_LIST\_ADD Procedure

This procedures adds objects to the object blacklist. These procedures only have to be run once in the cluster as they take effect everywhere at once. However, they do not persist between cluster shutdowns and startups.

Syntax

```
DBMS_RESULT_CACHE.OBJECT_BLACK_LIST_ADD (
   objNo       IN  BINARY_INTEGER);
```
```
DBMS_RESULT_CACHE.OBJECT_BLACK_LIST_ADD (
   owner       IN  VARCHAR2,
   name        IN  VARCHAR2);
```

Parameters

Table 150-12 OBJECT\_BLACK\_LIST\_ADD Procedure Parameters

| Parameter | Description |
| --- | --- |
| `objNo` | The object number. |
| `owner` | The owner of the object. |
| `name` | The name of the table. |

#### 150.3.13 OBJECT\_BLACK\_LIST\_CLEAR Procedure

This procedure clears the entire blacklist.

Syntax

```
DBMS_RESULT_CACHE.OBJECT_BLACK_LIST_CLEAR ();
```

#### 150.3.14 OBJECT\_BLACK\_LIST\_REMOVE Procedure

This procedures removes objects from the object blacklist.

Syntax

```
DBMS_RESULT_CACHE.OBJECT_BLACK_LIST_REMOVE (
   objNo       IN  BINARY_INTEGER);
```
```
DBMS_RESULT_CACHE.OBJECT_BLACK_LIST_REMOVE (
   owner       IN  VARCHAR2,
   name        IN  VARCHAR2);
```

Parameters

Table 150-13 OBJECT\_BLACK\_LIST\_REMOVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `objNo` | The object number. |
| `owner` | The owner of the object. |
| `name` | The name of the table. |

#### 150.3.15 STATUS Function

This function checks the status of the Result Cache.

Syntax

```
DBMS_RESULT_CACHE.STATUS
   RETURN VARCHAR2;
```

Note:

For more information on the constants, see DBMS\_RESULT\_CACHE Constants.