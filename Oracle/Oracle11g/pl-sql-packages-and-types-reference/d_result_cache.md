---
title: DBMS_RESULT_CACHE
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_result_cache.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 122 DBMS\_RESULT\_CACHE

The `DBMS_RESULT_CACHE` package provides an interface to allow the DBA to administer that part of the shared pool that is used by the SQL result cache and the PL/SQL function result cache. Both these caches use the same infrastructure. Therefore, for example, `DBMS_RESULT_CACHE`.`BYPASS` determines whether both caches are bypassed or both caches are used, and `DBMS_RESULT_CACHE`.`FLUSH` flushes both all the cached results for SQL queries and all the cached results for PL/SQL functions.

See Also:

- Oracle Database PL/SQL Language Reference for more information about ["Using the Cross-Session PL/SQL Function Result Cache"](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/subprograms.htm#LNPLS00817)
- Oracle Database Performance Tuning Guide for more information about ["Result Cache Concepts"](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF985)

This chapter contains the following topics:

- Using DBMS\_RESULT\_CACHE
	- Constants
- Summary of DBMS\_RESULT\_CACHE Subprograms

---

## Using DBMS\_RESULT\_CACHE

- Constants

---

### Constants

Table 122-1 DBMS\_RESULT\_CACHE Constants

| Constant | Definition |
| --- | --- |
| `STATUS_BYPS` | `CONSTANT VARCHAR(10) := 'BYPASS';` |
| `STATUS_CORR` | `CONSTANT VARCHAR(10) := 'CORRUPT';` |
| `STATUS_DISA` | `CONSTANT VARCHAR(10) := 'DISABLED';` |
| `STATUS_ENAB` | `CONSTANT VARCHAR(10) := 'ENABLED';` |
| `STATUS_SYNC` | `CONSTANT VARCHAR(10) := 'SYNC';` |

---

## Summary of DBMS\_RESULT\_CACHE Subprograms

Table 122-2 DBMS\_RESULT\_CACHE Package Subprograms

| Subprogram | Description |
| --- | --- |
| BYPASS Procedure | Sets the bypass mode for the Result Cache |
| FLUSH Function & Procedure | Attempts to remove all the objects from the Result Cache, and depending on the arguments retains or releases the memory and retains or clears the statistics |
| INVALIDATE Functions & Procedures | Invalidates all the result-set objects that dependent upon the specified dependency object |
| INVALIDATE\_OBJECT Functions & Procedures | Invalidates the specified result-set object(s) |
| MEMORY\_REPORT Procedure | Produces the memory usage report for the Result Cache |
| STATUS Function | Checks the status of the Result Cache |

---

### BYPASS Procedure

This procedure sets the bypass mode for the Result Cache:

- When bypass mode is turned on, it implies that cached results are no longer used and that no new results are saved in the cache.
- When bypass mode is turned off, the cache resumes normal operation.

Syntax

```
DBMS_RESULT_CACHE.BYPASS (
   bypass_mode    IN   BOOLEAN,
   session        IN   BOOLEAN);
```

Parameters

Table 122-3 BYPASS Procedure Parameters

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

---

### FLUSH Function & Procedure

This function and procedure attempts to remove all the objects from the Result Cache, and depending on the arguments retains or releases the memory and retains or clears the statistics.

Syntax

```
DBMS_RESULT_CACHE.FLUSH (
   retainMem  IN  BOOLEAN DEFAULT FALSE,
   retainSta  IN  BOOLEAN DEFAULT FALSE) 
  RETURN BOOLEAN;
```
```
DBMS_RESULT_CACHE.FLUSH (
   retainMem  IN  BOOLEAN DEFAULT FALSE,
   retainSta  IN  BOOLEAN DEFAULT FALSE);
```

Parameters

Table 122-4 FLUSH Function & Procedure Parameters

| Parameter | Description |
| --- | --- |
| `retainMem` | - `TRUE` => retains the free memory in the cache - `FALSE` (default) => releases the free memory to the system |
| `retainSta` | - `TRUE` => retains the existing cache statistics - `FALSE` (default) => clears the existing cache statistics |

Return Values

`TRUE` if successful in removing all the objects.

---

### INVALIDATE Functions & Procedures

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

Table 122-5 INVALIDATE Function & Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner` | Schema name |
| `name` | Object name |
| `object_id` | Dictionary object number |

Return Values

The number of objects invalidated.

---

### INVALIDATE\_OBJECT Functions & Procedures

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

Table 122-6 INVALIDATE Function & Procedure Parameters

| Parameter | Description |
| --- | --- |
| `id` | Address of the cache object in the Result Cache |
| `cache_id` | Cache-id |

Return Values

The number of objects invalidated.

---

### MEMORY\_REPORT Procedure

This procedure produces the memory usage report for the Result Cache.

Syntax

```
DBMS_RESULT_CACHE.MEMORY_REPORT (
   detailed   IN   BOOLEAN DEFAULT FALSE);
```

Parameters

Table 122-7 MEMORY\_REPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `detailed` | - `TRUE` => produces a more detailed report - `FALSE` (default) => produces the standard report |

Usage Notes

Invoking this procedure from SQL\*Plus requires that the serveroutput be turned on.

---

### STATUS Function

This function checks the status of the Result Cache.

Syntax

```
DBMS_RESULT_CACHE.STATUS
   RETURN VARCHAR2;
```

Return Values

One of the following values:

- `STATUS_DISA` - Cache is not available
- `STATUS_ENAB` - Cache is available
- `STATUS_BYPS`: Cache has been made temporarilyunavailable.
- `STATUS_SYNC` - Cache is available, but synchronizing with Oracle RAC nodes