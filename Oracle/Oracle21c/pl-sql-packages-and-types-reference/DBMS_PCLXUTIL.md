---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_PCLXUTIL.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 129 DBMS\_PCLXUTIL

The `DBMS_PCLXUTIL` package provides intra-partition parallelism for creating partition-wise local indexes. `DBMS_PCLXUTIL` circumvents the limitation that, for local index creation, the degree of parallelism is restricted to the number of partitions as only one parallel execution server process for each partition is used.

See Also:

There are several rules concerning partitions and indexes. For more information, see [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=CNCPT-GUID-54C48ABE-E589-428A-849F-B8746C9D276A) and [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-1DF51F9B-86E9-4E40-A30E-00714E7C0003).

This chapter contains the following topics:

### 129.1 DBMS\_PCLXUTIL Overview

`DBMS_PCLXUTIL` uses the `DBMS_JOB` package to provide a greater degree of parallelism for creating a local index for a partitioned table. This is achieved by asynchronous inter-partition parallelism using the background processes (with `DBMS_SCHEDULER`), in combination with intra-partition parallelism using the parallel execution server.

`DBMS_PCLXUTIL` works with both range and range-hash composite partitioning.

The `DBMS_PCLXUTIL` package can be used during the following DBA tasks:

1. Local index creation
	The procedure `BUILD_PART_INDEX` assumes that the dictionary information for the local index already exists. This can be done by issuing the create index SQL command with the `UNUSABLE` option.
	```
	CREATE INDEX <idx_name> on <tab_name>(...) local(...) unusable;
	```
	This causes the dictionary entries to be created without "building" the index itself, the time consuming part of creating an index. Now, invoking the procedure `BUILD_PART_INDEX` causes a concurrent build of local indexes with the specified degree of parallelism.
	```
	EXECUTE dbms_pclxutil.build_part_index(4,4,<tab_name>,<idx_name>,FALSE);
	```
	For composite partitions, the procedure automatically builds local indexes for all subpartitions of the composite table.
2. Local index maintenance
	By marking desired partitions usable or unusable, the `BUILD_PART_INDEX` procedure also enables selective rebuilding of local indexes. The `force_opt` parameter provides a way to override this and build local indexes for all partitions.
	```
	ALTER INDEX <idx_name> local(...) unusable;
	```
	Rebuild only the desired (sub)partitions (that are marked unusable):
	```
	EXECUTE dbms_pclxutil.build_part_index(4,4,<tab_name>,<idx_name>,FALSE);
	```
	Rebuild all (sub)partitions using `force_opt` = `TRUE`:
	```
	EXECUTE dbms_pclxutil.build_part_index(4,4,<tab_name>,<idx_name>,TRUE);
	```
	A progress report is produced, and the output appears on screen when the program is ended (because the `DBMS_OUTPUT` package writes messages to a buffer first, and flushes the buffer to the screen only upon termination of the program).

### 129.2 DBMS\_PCLXUTIL Security Model

This utility can be run only as table owner, and not as any other user.

### 129.3 DBMS\_PCLXUTIL Operational Notes

`DBMS_PCLXUTIL` submits a job for each partition. It is the responsibility of the user/dba to control the number of concurrent jobs by setting the `INIT`.`ORA` parameter `JOB_QUEUE_PROCESSES` correctly. There is minimal error checking for correct syntax. Any errors are reported in the job queue process trace files.

### 129.4 DBMS\_PCLXUTIL Rules and Limits

Because `DBMS_PCLXUTIL` uses the `DBMS_JOB` package, you must be aware of the following limitations pertaining to `DBMS_JOB`:

- You must decide appropriate values for the `job_queue_processes` initialization parameter. Clearly, if the job processes are not started before calling `BUILD_PART_INDEX` (), then the package will not function properly. The background processes are specified by the following `init`.`ora` parameters:
```
job_queue_processes=n   #the number of background processes = n
```
- Failure conditions are reported only in the trace files (a `DBMS_JOB` limitation), making it impossible to give interactive feedback to the user. This package prints a failure message, removes unfinished jobs from the queue, and requests the user to take a look at the `j*.trc` trace files.

Note:

For range partitioning, the minimum compatibility mode is 8.0; for range-hash composite partitioning, the minimum compatibility mode is 8i.

### 129.5 Summary of DBMS\_PCLXUTIL Subprograms

The `DBMS_PCLXUTIL` package has one subprogram, the `BUILD_PART_INDEX` procedure.

Table 129-1 DBMS\_PCLXUTIL Package Subprograms

| Subprogram | Description |
| --- | --- |
| BUILD\_PART\_INDEX Procedure | Provides intra-partition parallelism for creating partition-wise local indexes |

#### 129.5.1 BUILD\_PART\_INDEX Procedure

This procedure provides intra-partition parallelism for creating partition-wise local indexes.

Syntax

```
DBMS_PCLXUTIL.BUILD_PART_INDEX ( 
   jobs_per_batch  IN NUMBER   DEFAULT 1,
   procs_per_job   IN NUMBER   DEFAULT 1, 
   tab_name        IN VARCHAR2 DEFAULT NULL, 
   idx_name        IN VARCHAR2 DEFAULT NULL, 
   force_opt       IN BOOLEAN  DEFAULT FALSE);
```

Parameters

Table 129-2 BUILD\_PART\_INDEX Procedure Parameters

| Parameter | Description |
| --- | --- |
| `jobs_per_batch` | The number of concurrent partition-wise "local index builds". |
| `procs_per_job` | The number of parallel execution servers to be utilized for each local index build (1 <= `procs_per_job` <= `max_slaves`). |
| `tab_name` | The name of the partitioned table (an exception is raised if the table does not exist or not partitioned). |
| `idx_name` | The name given to the local index (an exception is raised if a local index is not created on the table `tab_name`). |
| `force_opt` | If `TRUE`, then force rebuild of all partitioned indexes; otherwise, rebuild only the partitions marked ' `UNUSABLE` '. |

Usage Notes

This utility can be run only as table owner, and not as any other user.

Examples

Suppose a table `PROJECT` is created with two partitions `PROJ001` and `PROJ002`, along with a local index `IDX`.

A call to the procedure `BUILD_PART_INDEX(2,4,'PROJECT','IDX',TRUE)` produces the following output:

```
SQLPLUS> EXECUTE dbms_pclxutil.build_part_index(2,4,'PROJECT','IDX',TRUE); 
Statement processed. 
INFO: Job #21 created for partition PROJ002 with 4 slaves 
INFO: Job #22 created for partition PROJ001 with 4 slaves
```