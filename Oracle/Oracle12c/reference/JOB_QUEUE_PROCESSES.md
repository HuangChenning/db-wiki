---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/JOB_QUEUE_PROCESSES.html
tags:
  - oracle
  - 12c
  - reference
---

`JOB_QUEUE_PROCESSES` specifies the maximum number of job slaves per instance that can be created for the execution of `DBMS_JOB` jobs and Oracle Scheduler (`DBMS_SCHEDULER`) jobs.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `4000` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to `4000` |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

`DBMS_JOB` and Oracle Scheduler share the same job coordinator and job slaves, and they are both controlled by the `JOB_QUEUE_PROCESSES` parameter. The actual number of job slaves created for Oracle Scheduler jobs is auto-tuned by the Scheduler depending on several factors, including available resources, Resource Manager settings, and currently running jobs. However, the combined total number of job slaves running `DBMS_JOB` jobs and Oracle Scheduler jobs on an instance can never exceed the value of `JOB_QUEUE_PROCESSES` for that instance.

- In a non-CDB:
	Set `JOB_QUEUE_PROCESSES` to the maximum number of job slaves that can be used simultaneously in the entire database instance. If `JOB_QUEUE_PROCESSES` is `0`, then `DBMS_JOB` jobs and Oracle Scheduler jobs will not run in the database instance.
- In a CDB root:
	Set `JOB_QUEUE_PROCESSES` to the maximum number of job slaves that can be used simultaneously in the entire CDB. If `JOB_QUEUE_PROCESSES` is `0` in a CDB root, then `DBMS_JOB` and Oracle Scheduler jobs cannot run in the CDB root or in any PDB, regardless of the `JOB_QUEUE_PROCESSES` setting at the PDB level.
- In a PDB:
	Set `JOB_QUEUE_PROCESSES` to the maximum number of job slaves that can be used simultaneously in the PDB. The actual number depends on the resources assigned by Resource Manager and the demand in other containers. When multiple PDBs request jobs, Oracle Scheduler attempts to give all PDBs a fair share of the processes. If `JOB_QUEUE_PROCESSES` is `0` in a PDB, then `DBMS_JOB` and Oracle Scheduler jobs cannot run in the PDB, regardless of the `JOB_QUEUE_PROCESSES` setting in the CDB root.

Oracle Streams Advanced Queuing uses Oracle Scheduler for message propagation. Materialized views use Oracle Scheduler for automatic refreshes. Setting `JOB_QUEUE_PROCESS` to `0` will disable these features and any other features that use Oracle Scheduler or `DBMS_JOB`.

Note:

`DBMS_JOB` is deprecated in Oracle Database 12c Release 2 (12.2.0.1) and may be removed in a future release. Oracle recommends that you use `DBMS_SCHEDULER` instead.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS72235) for more information on the `DBMS_SCHEDULER` package
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DWHSG8369) for more information on managing materialized views
- [Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADQUE2532) for more information about job queue processes
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN13490) for more information about the maximum number of scheduler job processes