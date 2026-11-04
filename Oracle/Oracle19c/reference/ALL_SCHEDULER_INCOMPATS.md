---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_SCHEDULER_INCOMPATS.html
tags:
  - oracle
  - 19c
  - reference
---

## 3.47 ALL\_SCHEDULER\_INCOMPATS

`ALL_SCHEDULER_INCOMPATS` displays all Scheduler incompatibility resource objects accessible to the current user.

Related Views

- `DBA_SCHEDULER_INCOMPATS` displays all Scheduler incompatibility resource objects in the database.
- `USER_SCHEDULER_INCOMPATS` displays all Scheduler incompatibility resource objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the incompatibility resource object |
| `INCOMPATIBILITY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the incompatibility resource object |
| `CONSTRAINT_LEVEL` | `VARCHAR2(13)` |  | `JOB_LEVEL` or `PROGRAM_LEVEL`  The default value `JOB_LEVEL` indicates that only a single job that is based on the program (or programs) mentioned in the `object_name` argument of the `DBMS_SCHEDULER.CREATE_INCOMPATIBILITY` procedure can run at one time.  The value `PROGRAM_LEVEL` indicates that the programs are incompatible, but the jobs based on the same program are not incompatible. |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether the incompatibility is enabled (`TRUE`) or not (`FALSE`) |
| `JOBS_RUNNING_COUNT` | `NUMBER` |  | Current number of running jobs using the incompatibility resource object |