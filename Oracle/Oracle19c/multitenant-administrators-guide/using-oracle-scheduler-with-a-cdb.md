---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: E96136-19
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/using-oracle-scheduler-with-a-cdb.html
tags:
  - oracle
  - 19c
  - multitenant-administrators-guide
---

## 23 Using Oracle Scheduler with a CDB

You can use Oracle Scheduler to schedule jobs in a multitenant container database (CDB).

Before using Oracle Scheduler with a CDB, meet the following requirements:

- You understand how to configure and manage a CDB.
- You understand how to use Oracle Scheduler to schedule jobs in a non-CDB.

- DBMS\_SCHEDULER Invocations in a CDB  
	Most scheduler calls work the same way as they do in non-CDBs, except for two scheduler global attributes.
- Job Coordinator and Slave Processes in a CDB  
	The major CDB-related changes are to the job coordinator process.
- DBMS\_JOB and DBMS\_SCHEDULER  
	You can use `DBMS_JOB` within a PDB only if you grant the `CREATE JOB` privilege to the schemas that submit `DBMS_JOB` jobs.
- Processes to Close a PDB  
	If a PDB is closed with the immediate option, then the coordinator terminates jobs running in the PDB, and the jobs must be recovered before they can run again.
- New and Changed CDB Views  
	Some CDB views are specific to CDBs, whereas others have a CDB-specific column.

See Also:

- " [Administering a Multitenant Environment](managing-a-multitenant-environment.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-6B8C0335-D36B-44D3-95BC-82FA2141D967)

**Parent topic:** [Using Oracle Features in a Multitenant Environment](using-oracle-features-in-a-multitenant-environment.md)

### DBMS\_SCHEDULER Invocations in a CDB

Most scheduler calls work the same way as they do in non-CDBs, except for two scheduler global attributes.

The `JOB_QUEUE_PROCESSES` initialization parameter specifies the maximum number of job slaves per instance that can be created for the execution of `DBMS_JOB` jobs and Oracle Scheduler (`DBMS_SCHEDULER`) jobs. The range of values is `0` to `4000` (default).

To limit job slaves in a CDB environment, you can set `JOB_QUEUE_PROCESSES` in the following locations:

- CDB root
	Set `JOB_QUEUE_PROCESSES` to the maximum number of slave processes that Scheduler can use simultaneously in the entire database instance.
	If `JOB_QUEUE_PROCESSES` is `0` in the CDB root, then `DBMS_JOB` and Oracle Scheduler jobs cannot run in the root or any PDB, regardless of the `JOB_QUEUE_PROCESSES` setting at the PDB level.
- PDB
	Set `JOB_QUEUE_PROCESSES` to the maximum number of simultaneous jobs for this PDB. The actual number depends on the resources assigned by Resource Manager and the demand in other containers. When multiple PDBs request jobs, Oracle Scheduler attempts to give all PDBs a fair share of the processes.
	If `JOB_QUEUE_PROCESSES` is `0` in a PDB, then `DBMS_JOB` and Oracle Scheduler jobs cannot run in this PDB, regardless of the `JOB_QUEUE_PROCESSES` setting in the CDB root.

You must set all global Oracle Scheduler attributes at the PDB level. For example, if you set the `EMAIL_SENDER` attribute in the root database using `DBMS_SCHEDULER.SET_ATTRIBUTE`, then it applies to the jobs that run in the root, not the jobs running in a specific PDB. If you choose a new `EMAIL_SENDER` for a PDB, then you must set the global attribute in this PDB.

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=GUID-B8B68D16-00A3-43DD-BE39-01F877880955) to learn more about `JOB_QUEUE_PROCESSES`

**Parent topic:** Using Oracle Scheduler with a CDB

### Job Coordinator and Slave Processes in a CDB

The major CDB-related changes are to the job coordinator process.

In a non-CDB, the coordinator looks at all jobs that are ready to run, picks a subset of them to run, and assigns them to job slaves. It also opens and closes windows, which changes the resource plan in effect for the database.

That is essentially what happens inside a CDB except for the following:

- Jobs are selected from all PDBs
	The coordinator looks at the root database and all the child PDBs and selects jobs based on the job priority, the job scheduled start time, and the availability of resources to run the job. The latter criterion depends on the consumer group of the job and the resource plan currently in effect. The coordinator makes no attempt to be fair to every PDB. The only way to ensure that jobs from a PDB are not starved is to allocate enough resources to it.
- Windows are open in the PDB and root database levels
	In a non-CDB, only one window can be open at any given time. In a CDB, there are two levels of windows. At the PDB level, windows can be used to set resource plans that allocate resources among consumer groups belonging to that PDB. At the root database level, windows can allocate resources to different PDBs. Therefore, at any time, there can be a window open in the root database and one in each PDB.
- Job slave switches to the specific PDB it belongs to
	The job slaves are essentially the same as in a non-CDB, except that when a slave executes a job, it switches to the PDB that the job belongs to and then executes it. The rest of the code is essentially unchanged.

**Parent topic:** Using Oracle Scheduler with a CDB

### DBMS\_JOB and DBMS\_SCHEDULER

You can use `DBMS_JOB` within a PDB only if you grant the `CREATE JOB` privilege to the schemas that submit `DBMS_JOB` jobs.

The `DBMS_JOB` interface is implemented using `DBMS_SCHEDULER`. For this reason, Oracle recommends that you switch from `DBMS_JOB` to `DBMS_SCHEDULER`.

For the scheduler, the coordinator selects jobs to run from every PDB. Also, for the scheduler, the slave process switches into a PDB before executing a job; otherwise, the code is essentially unchanged.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-CC42E8DA-7203-449E-BCEA-8187ECC4BCDF) for information about support for `DBMS_JOB`

**Parent topic:** Using Oracle Scheduler with a CDB

### Processes to Close a PDB

If a PDB is closed with the immediate option, then the coordinator terminates jobs running in the PDB, and the jobs must be recovered before they can run again.

In an Oracle RAC database, the coordinator can, in most cases, recover the jobs on another instance where that PDB is open. So, if the coordinator on the first instance can find another instance where the PDB is still open, it moves the jobs there. In certain cases, moving the jobs to another instance may not be possible. For example, if the PDB in question is not open anywhere else, the jobs cannot be moved. Also, moving a job to another instance is not possible when the job has the `INSTANCE_ID` attribute set. In this case the job cannot run until the PDB on that instance is open again.

In a non-Oracle RAC case, the question of moving jobs does not arise. Terminated jobs can only be recovered after the PDB is opened again.

**Parent topic:** Using Oracle Scheduler with a CDB

### New and Changed CDB Views

Some CDB views are specific to CDBs, whereas others have a CDB-specific column.

- `V$` and `GV$` views have a `CON_ID` column that identifies a container whose data is represented by a `CDB_*` row. In non-CDBs, the `CON_ID` column is `NULL`.
- `CDB_*` views correspond to all Scheduler `DBA_*` views.
	In a PDB, these views only show objects visible through a corresponding `DBA_*` view, but all objects are visible in the root. The `CDB_*` view contains all columns found in a given `DBA_*` view and the column (`CON_ID`). In non-CDBs, this column is `NULL`.

**Parent topic:** Using Oracle Scheduler with a CDB