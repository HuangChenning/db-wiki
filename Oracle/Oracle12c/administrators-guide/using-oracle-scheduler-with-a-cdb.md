---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/using-oracle-scheduler-with-a-cdb.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

You can use Oracle Scheduler to schedule jobs in a multitenant container database (CDB).

Before using Oracle Scheduler with a CDB, meet the following requirements:

- You understand how to configure and manage a CDB. See [Managing a Multitenant Environment](managing-a-multitenant-environment.md) for an overview and related information.
- You understand how to use Oracle Scheduler to schedule jobs in a non-CDB. See [Oracle Scheduler Concepts](oracle-scheduler-concepts.md), [Scheduling Jobs with Oracle Scheduler](scheduling-jobs-with-oracle-scheduler.md), and [Administering Oracle Scheduler](administering-oracle-scheduler.md) for information.

- DBMS\_SCHEDULER Invocations in a CDB  
	Most scheduler calls work exactly the same way as they did in non-CDBs, with the exception of two scheduler global attributes.
- Job Coordinator and Slave Processes in a CDB  
	The major CDB-related changes are to the job coordinator process.
- Using DBMS\_JOB  
	You can create a job using `DBMS_JOB` within a PDB, and it will work as before. However, `DBMS_JOB` has been desupported and using it is not recommended. Oracle plans to remove `DBMS_JOB` completely in the version after Oracle Database 12c Release 2 (12.2). You should switch from `DBMS_JOB` to `DBMS_SCHEDULER`.
- Processes to Close a PDB  
	If a PDB is closed with the immediate option, then the coordinator terminates jobs running in the PDB, and the jobs must be recovered before they can run again.
- New and Changed Views  
	With the CDB, changes have been made to existing views and new views have been added.

**Parent topic:** [Managing a Multitenant Environment](managing-a-multitenant-environment.md)

### 48.1 DBMS\_SCHEDULER Invocations in a CDB

Most scheduler calls work exactly the same way as they did in non-CDBs, with the exception of two scheduler global attributes.

To limit job slaves, set the value of the `JOB_QUEUE_PROCESSES` initialization parameter. In the CDB root, set `JOB_QUEUE_PROCESSES` to the maximum number of job slaves that can be used simultaneously in the entire CDB. If `JOB_QUEUE_PROCESSES` is set to 0 in the CDB root, then `DBMS_JOBS` and Oracle Scheduler jobs cannot run in the CDB root, regardless of the `JOB_QUEUE_PROCESSES` setting at the PDB level. In a PDB, set `JOB_QUEUE_PROCESSES` to the maximum number of job slaves that can be used simultaneously in the PDB. The actual number depends on the resources assigned by Resource Manager and the demand in other containers. If `JOB_QUEUE_PROCESSES` is 0 in a PDB, then `DBMS_JOBS` and Oracle Scheduler jobs cannot run in the PDB, regardless of the `JOB_QUEUE_PROCESSES` setting in the CDB root.

For all other global attribute settings, you must be at the pluggable database (PDB) level only. For example, if you set the `EMAIL_SENDER` attribute in the root database, it applies to the jobs that run in the root, not the jobs running in a specific PDB. If you want to pick a new `EMAIL_SENDER` for a PDB, then you must set the global attribute in that PDB.

**Parent topic:** Using Oracle Scheduler with a CDB

### 48.2 Job Coordinator and Slave Processes in a CDB

The major CDB-related changes are to the job coordinator process.

In a non-CDB, the coordinator looks at all jobs that are ready to run, picks a subset of them to run, and assigns them to job slaves. It also opens and closes windows, which changes the resource plan in effect for the database.

That is essentially what happens inside a CDB except for the following:

- Jobs are selected from all PDBs
	The coordinator looks at the root database and all the child PDBs and selects jobs based on the job priority, the job scheduled start time, and the availability of resources to run the job. The latter criterion depends on the consumer group of the job and the resource plan currently in effect. The coordinator makes no attempt to be fair to every PDB. The only way to ensure that jobs from a PDB are not starved is to allocate enough resources to it.
- Windows are open in the PDB and root database levels
	In a non-CDB, only one window can be open at any given time. In a CDB, there are two levels of windows. At the PDB level, windows can be used to set resource plans that allocate resources among consumer groups belonging to that PDB. At the root database level, windows can be used to allocate resources to various different PDBs. Therefore, at any time, there can be a window open in the root database and one in each PDB.
- Job slave switches to the specific PDB it belongs to
	The job slaves are essentially the same as in a non-CDB, except that when a slave executes a job, it switches to the PDB that the job belongs to and then executes it. The rest of the code is essentially unchanged.

**Parent topic:** Using Oracle Scheduler with a CDB

### 48.3 Using DBMS\_JOB

You can create a job using `DBMS_JOB` within a PDB, and it will work as before. However, `DBMS_JOB` has been desupported and using it is not recommended. Oracle plans to remove `DBMS_JOB` completely in the version after Oracle Database 12c Release 2 (12.2). You should switch from `DBMS_JOB` to `DBMS_SCHEDULER`.

For the scheduler, the coordinator now selects jobs to run from every single PDB and not just a single database as was the case before. Also, for the scheduler, the slave will switch into a PDB before executing a job; otherwise, the code is essentially unchanged.

See Also:

[Support for DBMS\_JOB](support-for-DBMS_JOB.md)

**Parent topic:** Using Oracle Scheduler with a CDB

### 48.4 Processes to Close a PDB

If a PDB is closed with the immediate option, then the coordinator terminates jobs running in the PDB, and the jobs must be recovered before they can run again.

In an Oracle RAC database, the coordinator can, in most cases, recover the jobs on another instance where that PDB is open. So, if the coordinator on the first instance can find another instance where the PDB is still open, it moves the jobs there. In certain cases, moving the jobs to another instance may not be possible. For example, if the PDB in question is not open anywhere else, the jobs cannot be moved. Also, moving a job to another instance is not possible when the job has the `INSTANCE_ID` attribute set. In this case the job cannot run until the PDB on that instance is open again.

In a non-Oracle RAC case, the question of moving jobs does not arise. Terminated jobs can only be recovered after the PDB is opened again.

**Parent topic:** Using Oracle Scheduler with a CDB

### 48.5 New and Changed Views

With the CDB, changes have been made to existing views and new views have been added.

See Oracle Database Reference for details.

- `V$` and `GV` $ views now have an additional column (`CON_ID`) which identifies a container whose data a given `CDB_*` row represents. In non-CDBs, this column is `NULL`.
- There are `CDB_*` views corresponding to all Scheduler `DBA_*` views.
	In a PDB, these views only show objects visible through a corresponding `DBA_* view`, but all objects can be viewed by the root database. The `CDB_*` view contains all columns found in a given `DBA_*` view and the column (`CON_ID`). In non-CDBs, this column is `NULL`.

**Parent topic:** Using Oracle Scheduler with a CDB