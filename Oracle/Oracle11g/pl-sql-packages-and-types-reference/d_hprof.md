---
title: DBMS_HPROF
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_hprof.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 73 DBMS\_HPROF

The `DBMS_HPROF` package provides an interface for profiling the execution of PL/SQL applications. It provides services for collecting the hierarchical profiler data, analyzing the raw profiler output and profiling information generation.

See Also:

Oracle Database Advanced Application Developer's Guide for more information about the ["PL/SQL Hierarchical Profiler"](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_profiler.htm#ADFNS023)

This chapter contains the following topic:

- Summary of DBMS\_HPROF Subprograms

---

## Summary of DBMS\_HPROF Subprograms

This table list the package subprograms in alphabetical order.

Table 73-1 DBMS\_HPROF Package Subprograms

| Subprogram | Description |
| --- | --- |
| ANALYZE Function | Analyzes the raw profiler output and produces hierarchical profiler information in database tables |
| START\_PROFILING Procedure | Starts hierarchical profiler data collection in the user's session |
| STOP\_PROFILING Procedure | Stops profiler data collection in the user's session.s |

---

### ANALYZE Function

This function analyzes the raw profiler output and produces hierarchical profiler information in database tables.

Syntax

```
DBMS_HPROF.ANALYZE (
   location         VARCHAR2,
   filename         VARCHAR2,
   summary_mode     BOOLEAN     DEFAULT FALSE,
   trace            VARCHAR2    DEFAULT NULL,
   skip             PLS_INTEGER DEFAULT 0,
   collect          PLS_INTEGER DEFAULT NULL,
   run_comment      VARCHAR2    DEFAULT NULL)
  RETURN NUMBER;
```

Parameters

Table 73-2 ANALYZE Function Parameters

| Parameter | Description |
| --- | --- |
| `location` | Name of a directory object. The raw profiler data file is read from the file system directory mapped to this directory object. Output files are also written to this directory. |
| `filename` | Name of the raw profiler data file to be analyzed. The file must exist in the directory specified by the `location` parameter. |
| `summary_mode` | By default (that is, when `summary_mode` is `FALSE`), the detailed analysis is done.When `summary_mode` is `TRUE`, only top-level summary information is generated into the database table. |
| `trace` | Analyze only the subtrees rooted at the specified trace entry. By default (when trace is `NULL`), the analysis/reporting is generated for the entire run.  The trace entry must be specified in a special quoted qualified format (including the schema name, module name & function name) as in for example, '" `SCOTT` "." `PKG` "." `FOO` "' or '"".""." `__plsql_vm` "'. If multiple overloads exist for the specified name, all of them will be analyzed. |
| `skip` | Used only when `trace` is specified.Analyze only the subtrees rooted at the specified trace, but ignore the first `skip` invocations to trace. The default value for skip is 0. |
| `collect` | Used only when `trace` is specified.  Analyze `collect` number of invocations of traces (starting from `skip` +1'th invocation). By default only 1 invocation is collected. |
| `run_comment` | User-provided comment for this run |

Return Values

A unique run identifier for this run of the analyzer. This can then be used to look up the results corresponding to this run from the hierarchical profiler tables.

Usage Notes

- Use the `dbmshptab`.`sql` script located in the `rdbms` / `admin` directory to create the hierarchical profiler database tables and other data structures required for persistently storing the results of analyzing the raw profiler data.
- Running `dbmshptab`.`sql` drops the any previously created hierarchical profiler tables.

Examples

The following snippet installs the hierarchical profiler tables in HR schema.

```
connect HR/HR;
@?/rdbms/admin/dbmshptab.sql
```

---

### START\_PROFILING Procedure

This procedure starts hierarchical profiler data collection in the user's session.

Syntax

```
DBMS_HPROF.START_PROFILING (
   location    VARCHAR2 DEFAULT NULL,
   filename    VARCHAR2 DEFAULT NULL,
   max_depth   PLS_INTEGER DEFAULT NULL);
```

Parameters

Table 73-3 START\_PROFILING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `location` | Name of a directory object. The file system directory mapped to this directory object is where the raw profiler output is generated. |
| `filename` | Output filename for the raw profiler data. The file is created in the directory specified by the `location` parameter. |
| `max_depth` | By default (that is, when `max_depth` value is `NULL`) profile information is gathered for all functions irrespective of their call depth. When a non- `NULL` value is specified for `max_depth`, the profiler collects data only for functions up to a call depth level of `max_depth`. |

Usage Notes

Even though the profiler does not individually track functions at depth greater than max\_depth, the time spent in such functions is charged to the ancestor function at depth max\_depth.

---

### STOP\_PROFILING Procedure

This procedure stops profiler data collection in the user's session. This subprogram also has the side effect of flushing data collected so far in the session, and it signals the end of a run.

Syntax

```
DBMS_HPROF.STOP_PROFILING;
```