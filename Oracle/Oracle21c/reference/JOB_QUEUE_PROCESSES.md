---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/JOB_QUEUE_PROCESSES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.171 JOB\_QUEUE\_PROCESSES

`JOB_QUEUE_PROCESSES` specifies the maximum number of job workers per CDB or PDB that can be created for the execution of `DBMS_JOB` jobs and Oracle Scheduler (`DBMS_SCHEDULER`) jobs.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Derived. The lesser value of:  - `CPU_COUNT` \* 20 - `SESSIONS` / 4  If the result of the above derivation is less than twice the number of open containers in the CDB, then the value of this parameter is adjusted to equal twice the number of open containers in the CDB. Containers include `CDB$ROOT`, `PDB$SEED`, PDBs, application roots, application seeds, and application PDBs. You can obtain the number of open containers in a CDB with the following query: ``` SELECT COUNT(*) FROM V$CONTAINERS   WHERE open_mode != 'MOUNTED'; ``` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to `4000` |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

`DBMS_JOB` and Oracle Scheduler share the same job coordinator and job workers, and they are both controlled by the `JOB_QUEUE_PROCESSES` parameter. The actual number of job workers created for Oracle Scheduler jobs is auto-tuned by the Scheduler depending on several factors, including available resources, Resource Manager settings, and currently running jobs. However, the combined total number of job workers running `DBMS_JOB` jobs and Oracle Scheduler jobs in a CDB or PDB can never exceed the value of `JOB_QUEUE_PROCESSES` for that CDB or PDB.

The default value for `JOB_QUEUE_PROCESSES` provides a compromise between quality of service for applications and reasonable use of system resources. However, it is possible that the default value does not suit every environment. In such cases, you can use the following guidelines to fine tune this parameter:

- In a CDB root:
	Set `JOB_QUEUE_PROCESSES` to the maximum number of job workers that can be used simultaneously in the entire CDB. Oracle recommends that you set the value of this parameter to at least twice the number of open containers in the CDB, otherwise, there might be severe starvation between PDBs trying to run multiple jobs. If `JOB_QUEUE_PROCESSES` is set to `0` in a CDB root, then `DBMS_JOB` and Oracle Scheduler jobs cannot run in the CDB root or in any PDB, regardless of the `JOB_QUEUE_PROCESSES` setting at the PDB level.
- In a PDB:
	Set `JOB_QUEUE_PROCESSES` to the maximum number of job workers that can be used simultaneously in the PDB. The actual number depends on the resources assigned by Resource Manager and the demand in other containers. When multiple PDBs request jobs, Oracle Scheduler attempts to give all PDBs a fair share of the processes. Oracle recommends that you set the value of this parameter to at least `2` in a PDB. However, if you do not want to run `DBMS_JOB` and Oracle Scheduler jobs in a PDB, then set `JOB_QUEUE_PROCESSES` to `0` in the PDB.

Materialized views and AutoTask use Oracle Scheduler for automatic refreshes. Setting `JOB_QUEUE_PROCESS` to `0` will disable these features and any other features that use Oracle Scheduler or `DBMS_JOB`.

Note:

`DBMS_JOB` is deprecated in Oracle Database 12c Release 2 (12.2.0.1) and may be removed in a future release. Oracle recommends that you use `DBMS_SCHEDULER` instead.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS72235) for more information on the `DBMS_SCHEDULER` package
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DWHSG8369) for more information on managing materialized views
- [Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE2532) for more information about job queue processes
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN13490) for more information about the maximum number of scheduler job processes