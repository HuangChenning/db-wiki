---
title: JOB_QUEUE_PROCESSES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams112.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1000` |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `0` to `1000` |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

`JOB_QUEUE_PROCESSES` specifies the maximum number of job slaves per instance that can be created for the execution of `DBMS_JOB` jobs and Oracle Scheduler (`DBMS_SCHEDULER`) jobs. `DBMS_JOB` and Oracle Scheduler share the same job coordinator and job slaves, and they are both controlled by the `JOB_QUEUE_PROCESSES` parameter.

If the value of `JOB_QUEUE_PROCESSES` is set to 0, then `DBMS_JOB` jobs and Oracle Scheduler jobs will not run on the instance.

If `JOB_QUEUE_PROCESSES` is set to a value in the range of `1` to `1000`, then `DBMS_JOB` jobs and Oracle Scheduler jobs will run. The actual number of job slaves created for Oracle Scheduler jobs is auto-tuned by the Scheduler depending on several factors, including available resources, Resource Manager settings, and currently running jobs. However, the combined total number of job slaves running `DBMS_JOB` jobs and Oracle Scheduler jobs on an instance can never exceed the value of `JOB_QUEUE_PROCESSES` for that instance.

Advanced replication uses Oracle Scheduler for data refreshes. Oracle Streams Advanced Queuing uses Oracle Scheduler for message propagation. Materialized views use Oracle Scheduler for automatic refreshes. Setting `JOB_QUEUE_PROCESS` to 0 will disable these features as well as any other features that use Oracle Scheduler or `DBMS_JOB`.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_sched.htm#ARPLS72235) for more information on the `DBMS_SCHEDULER` package
- [Oracle Database Advanced Replication](https://docs.oracle.com/cd/E11882_01/server.112/e10706/toc.htm) and [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/toc.htm) for more information on managing materialized views
- [Oracle Streams Advanced Queuing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11013/toc.htm) for more information on message propagation
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/schedover.htm#ADMIN13490) for more information about the maximum number of scheduler job processes