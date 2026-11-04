---
title: UTL_RECOMP
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/u_recomp.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 234 UTL\_RECOMP

The UTL\_RECOMP package recompiles invalid PL/SQL modules, invalid views, Java classes, indextypes and operators in a database, either sequentially or in parallel.

This chapter contains the following topics:

- Using UTL\_RECOMP
- Summary of UTL\_RECOMP Subprograms

---

## Using UTL\_RECOMP

---

### Overview

This script is particularly useful after a major-version upgrade that typically invalidates all PL/SQL and Java objects. Although invalid objects are recompiled automatically on use, it is useful to run this script prior to operation because this will either eliminate or minimize subsequent latencies due to on-demand automatic recompilation at runtime.

Parallel recompilation can exploit multiple CPUs to reduce the time taken to recompile invalid objects. The degree of parallelism is specified by the first argument to RECOMP\_PARALLEL Procedure.

In general, a parallelism setting of one thread for each available CPU provides a good initial setting. However, please note that the process of recompiling an invalid object writes a significant amount of data to system tables and is fairly I/O intensive. A slow disk system may be a significant bottleneck and limit speedups available from a higher degree of parallelism.

---

### Operational Notes

- This package uses the job queue for parallel recompilation.
- This package must be run using `SQL*PLUS`.
- You must be connected `AS` `SYSDBA` to run this script.
- This package expects the following packages to have been created with VALID status:
	- `STANDARD` (`standard`.`sql`)
		- `DBMS_STANDARD` (`dbmsstdx`.`sql`)
		- `DBMS_JOB` (`dbmsjob`.`sql`)
		- `DBMS_RANDOM (dbmsrand.sql)`
- There should be no other DDL on the database while running entries in this package. Not following this recommendation may lead to deadlocks.

---

### Examples

Recompile all objects sequentially:

```
EXECUTE UTL_RECOMP.RECOMP_SERIAL();
```

Recompile objects in schema `SCOTT` sequentially:

```
EXECUTE UTL_RECOMP.RECOMP_SERIAL('SCOTT');
```

Recompile all objects using 4 parallel threads:

```
EXECUTE UTL_RECOMP.RECOMP_PARALLEL(4);
```

Recompile objects in schema JOE using the number of threads specified in the parameter `JOB_QUEUE_PROCESSES`:

```
EXECUTE UTL_RECOMP.RECOMP_PARALLEL(NULL, 'JOE');
```

---

## Summary of UTL\_RECOMP Subprograms

Table 234-1 UTL\_RECOMP Package Subprograms

| Subprogram | Description |
| --- | --- |
| RECOMP\_PARALLEL Procedure | Recompiles invalid objects in a given schema, or all invalid objects in the database, in parallel |
| RECOMP\_SERIAL Procedure | Recompiles invalid objects in a given schema or all invalid objects in the database |

---

### RECOMP\_PARALLEL Procedure

This procedure uses the information exposed in the `DBA_Dependencies` view to recompile invalid objects in the database, or in a given schema, in parallel.

Syntax

```
UTL_RECOMP.RECOMP_PARALLEL(
   threads  IN   PLS_INTEGER DEFAULT NULL,
   schema   IN   VARCHAR2    DEFAULT NULL,
   flags    IN   PLS_INTEGER DEFAULT 0);
```

Parameters

Table 234-2 RECOMP\_PARALLEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `threads` | The number of recompile threads to run in parallel. If `NULL`, use the value of ' `job_queue_processes` '. |
| `schema` | The schema in which to recompile invalid objects. If `NULL`, all invalid objects in the database are recompiled. |
| `flags` | Flag values are intended for internal testing and diagnosability only. |

Usage Notes

The parallel recompile exploits multiple CPUs to reduce the time taken to recompile invalid objects. However, please note that recompilation writes significant amounts of data to system tables, so the disk system may be a bottleneck and prevent significant speedups.

---

### RECOMP\_SERIAL Procedure

This procedure recompiles invalid objects in a given schema or all invalid objects in the database.

Syntax

```
UTL_RECOMP.RECOMP_SERIAL(
   schema   IN   VARCHAR2    DEFAULT NULL,
   flags    IN   PLS_INTEGER DEFAULT 0);
```

Parameters

Table 234-3 RECOMP\_SERIAL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema` | The schema in which to recompile invalid objects. If `NULL`, all invalid objects in the database are recompiled. |
| `flags` | Flag values are intended for internal testing and diagnosability only. |