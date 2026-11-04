---
title: DBMS_SHARED_POOL
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_shared_pool.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 133 DBMS\_SHARED\_POOL

The `DBMS_SHARED_POOL` package provides access to the shared pool, which is the shared memory area where cursors and PL/SQL objects are stored. `DBMS_SHARED_POOL` enables you to display the sizes of objects in the shared pool, and mark them for keeping or not-keeping in order to reduce memory fragmentation.

This chapter contains the following topics:

- Using DBMS\_SHARED\_POOL
- Summary of DBMS\_SHARED\_POOL Subprograms

---

## Summary of DBMS\_SHARED\_POOL Subprograms

Table 133-1 DBMS\_SHARED\_POOL Package Subprograms

| Subprogram | Description |
| --- | --- |
| ABORTED\_REQUEST\_THRESHOLD Procedure | Sets the aborted request threshold for the shared pool |
| KEEP Procedure | Keeps an object in the shared pool |
| MARKHOT Procedure | Marks a library cache object as a hot object |
| PURGE Procedure | Purges the named object or specified heap(s) of the object |
| SIZES Procedure | Shows objects in the shared pool that are larger than the specified size |
| UNKEEP Procedure | Unkeeps the named object |
| UNMARKHOT Procedure | Unmarks a library cache object as a hot object |

---

### ABORTED\_REQUEST\_THRESHOLD Procedure

This procedure sets the aborted request threshold for the shared pool.

Syntax

```
DBMS_SHARED_POOL.ABORTED_REQUEST_THRESHOLD (
   threshold_size NUMBER);
```

Parameters

Table 133-2 ABORTED\_REQUEST\_THRESHOLD Procedure Parameters

| Parameter | Description |
| --- | --- |
| `threshold_size` | Size, in bytes, of a request which does not try to free unpinned (not "unkeep-ed") memory within the shared pool. The range of `threshold_size` is 5000 to ~2 GB inclusive. |

Exceptions

An exception is raised if the threshold is not in the valid range.

Usage Notes

Usually, if a request cannot be satisfied on the free list, then the RDBMS tries to reclaim memory by freeing objects from the LRU list and checking periodically to see if the request can be fulfilled. After finishing this step, the RDBMS has performed a near equivalent of an ' `ALTER` `SYSTEM` `FLUSH` `SHARED_POOL` '.

Because this impacts all users on the system, this procedure "localizes" the impact to the process failing to find a piece of shared pool memory of size greater than `thresh_hold` size. This user gets the 'out of memory' error without attempting to search the LRU list.

---

### KEEP Procedure

This procedure keeps an object in the shared pool. Once an object has been kept in the shared pool, it is not subject to aging out of the pool. This may be useful for frequently used large objects. When large objects are brought into the shared pool, several objects may need to be aged out to create a contiguous area large enough.

Syntax

```
DBMS_SHARED_POOL.KEEP (
   name VARCHAR2, 
   flag CHAR      DEFAULT 'P');
```

Parameters

Table 133-3 KEEP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Name of the object to keep.  The value for this identifier is the concatenation of the address and `hash_value` columns from the `v$sqlarea` view. This is displayed by the `SIZES` procedure.  Currently, `TABLE` and `VIEW` objects may not be kept. |
| `flag` | (Optional) If this is not specified, then the package assumes that the first parameter is the name of a package/procedure/function and resolves the name.  Set to `'P'` or `'p'` to fully specify that the input is the name of a package/procedure/function.  Set to `'T'` or `'t'` to specify that the input is the name of a type.  Set to `'R'` or `'r'` to specify that the input is the name of a trigger.  Set to `'Q'` or `'q'` to specify that the input is the name of a sequence.  In case the first argument is a cursor address and hash-value, the parameter should be set to any character except `'P'` or `'p'` or `'Q'` or `'q'` or `'R'` or `'r'` or `'T'` or `'t'`. |

Exceptions

An exception is raised if the named object cannot be found.

Usage Notes

There are two kinds of objects:

- PL/SQL objects, triggers, sequences, and types which are specified by name
- SQL cursor objects which are specified by a two-part number (indicating a location in the shared pool).

For example:

```
DBMS_SHARED_POOL.KEEP('scott.hispackage')
```

This keeps package `HISPACKAGE`, owned by `SCOTT`. The names for PL/SQL objects follow SQL rules for naming objects (for example, delimited identifiers and multibyte names are allowed). A cursor can be kept by `DBMS_SHARED_POOL`.`KEEP('0034CDFF, 20348871','C')`, `0034CDFF` being the `ADDRESS` and `20348871` the `HASH_VALUE`. Note that the complete hexadecimal address must be in the first 8 characters.

---

### MARKHOT Procedure

This procedure marks a library cache object as a hot object.

Syntax

```
DBMS_SHARED_POOL.MARKHOT (
   schema         VARCHAR2, 
   objname        VARCHAR2,
   namespace      NUMBER DEFAULT 1,   global         BOOLEAN DEFAULT TRUE);

DBMS_SHARED_POOL.MARKHOT (
   hash          VARCHAR2, 
   namespace     NUMBER DEFAULT 1,
   global        BOOLEAN DEFAULT TRUE);
```

Parameters

Table 133-4 MARKHOT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema` | User name or the schema to which the object belongs |
| `objname` | Name of the object |
| `namespace` | Number indicating the library cache namespace in which the object is to be searched. Views such as `USER_OBJECTS` and `DBA_OBJECTS` reflect the namespace as a number column, as do most dictionary tables such as `obj$`. |
| `global` | If `TRUE` (default), mark the object hot on all OracleRAC instances |
| `hash` | 16-byte hash value for the object |

Exceptions

`ORA-06502`: An exception is raised if the named object cannot be found due to incorrect input

`ORA-04043`: An exception is raised if the named object cannot be found (bad namespace, or hash input)

---

### PURGE Procedure

This procedure purges the named object or specified heap(s) of the object.

Syntax

```
DBMS_SHARED_POOL.PURGE (
   name         VARCHAR2, 
   flag         CHAR DEFAULT 'P', 
   heaps        NUMBER DEFAULT 1);

DBMS_SHARED_POOL.PURGE (
   schema       VARCHAR2,
   objname      VARCHAR2,
   namespace    NUMBER,
   heaps        NUMBER);
 
DBMS_SHARED_POOL.PURGE (
   hash         VARCHAR2,
   namespace    NUMBER,
   heaps        NUMBER);
```

Parameters

Table 133-5 PURGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Name of the object to purge.  The value for this identifier is the concatenation of the address and `hash_value` columns from the `v$sqlarea` view. This is displayed by the `SIZES` procedure.  Currently, `TABLE` and `VIEW` objects may not be purged. |
| `flag` | (Optional) If this is not specified, then the package assumes that the first parameter is the name of a package/procedure/function and resolves the name.  Set to 'P' or 'p' to fully specify that the input is the name of a package/procedure/function.  Set to 'T' or 't' to specify that the input is the name of a type.  Set to 'R' or 'r' to specify that the input is the name of a trigger.  Set to 'Q' or 'q' to specify that the input is the name of a sequence.  In case the first argument is a cursor address and hash-value, the parameter should be set to any character except 'P' or 'p' or 'Q' or 'q' or 'R' or 'r' or 'T' or 't'. |
| `heaps` | Heaps to be purged. For example, if heap 0 and heap 6 are to be purged:  1<<0 \| 1<<6 => hex 0x41 => decimal 65, so specify heaps =>65.Default is 1, that is, heap 0 which means the whole object would be purged |
| `schema` | User name or the schema to which the object belongs |
| `objname` | Name of the object to purge |
| `namespace` | Parameter is a number indicating the library cache namespace in which the object is to be searched |
| `hash` | 16-byte hash value for the object |

Exceptions

`ORA-6570`: An exception is raised if the named object cannot be found

`ORA-6570`: An object cannot be purged it marked as permanently kept

Usage Notes

All objects supported by the KEEP Procedure are supported for `PURGE`.

---

### SIZES Procedure

This procedure shows objects in the `shared_pool` that are larger than the specified size. The name of the object is also given, which can be used as an argument to either the `KEEP` or `UNKEEP` calls.

Syntax

```
DBMS_SHARED_POOL.SIZES ( 
   minsize NUMBER);
```

Parameters

Table 133-6 SIZES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `minsize` | Size, in kilobytes, over which an object must be occupying in the shared pool, in order for it to be displayed. |

Usage Notes

Issue the SQLDBA or SQLPLUS `'SET` `SERVEROUTPUT` `ON` `SIZE` `XXXXX'` command prior to using this procedure so that the results are displayed.

---

### UNKEEP Procedure

This procedure unkeeps the named object.

Syntax

```
DBMS_SHARED_POOL.UNKEEP (
   name VARCHAR2, 
   flag CHAR     DEFAULT 'P');
```

Caution:

This procedure may not be supported in the future if automatic mechanisms are implemented to make this unnecessary.

Parameters

Table 133-7 UNKEEP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Name of the object to unkeep. See description of the `name` object for the `KEEP` procedure. |
| `flag` | See description of the flag parameter for the `KEEP` procedure. |

Exceptions

An exception is raised if the named object cannot be found.

---

### UNMARKHOT Procedure

This procedure unmarks a library cache object as a hot object.

Syntax

```
DBMS_SHARED_POOL.UNMARKHOT (
   schema         VARCHAR2, 
   objname        VARCHAR2,
   namespace      NUMBER DEFAULT 1,   global         BOOLEAN DEFAULT TRUE);

DBMS_SHARED_POOL.UNMARKHOT (
   hash          VARCHAR2, 
   namespace     NUMBER DEFAULT 1,
   global        BOOLEAN DEFAULT TRUE);
```

Parameters

Table 133-8 UNMARKHOT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema` | User name or the schema to which the object belongs |
| `objname` | Name of the object |
| `namespace` | Number indicating the library cache namespace in which the object is to be searched |
| `global` | If `TRUE` (default), unmark the object hot on all Oracle RAC instances |
| `hash` | 16-byte hash value for the object |

Exceptions

`ORA-06502`: An exception is raised if the named object cannot be found due to incorrect input

`ORA-04043`: An exception is raised if the named object cannot be found (bad namespace, or hash input, or non-existent object)