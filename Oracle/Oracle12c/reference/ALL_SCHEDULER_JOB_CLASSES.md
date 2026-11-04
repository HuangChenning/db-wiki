---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_SCHEDULER_JOB_CLASSES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_SCHEDULER_JOB_CLASSES` displays information about the Scheduler job classes accessible to the current user.

Related View

`DBA_SCHEDULER_JOB_CLASSES` displays information about all Scheduler job classes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the Scheduler job class |
| `JOB_CLASS_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the Scheduler job class |
| `RESOURCE_CONSUMER_GROUP` | `VARCHAR2(128)` |  | Resource consumer group associated with the class |
| `SERVICE` | `VARCHAR2(64)` |  | Name of the service the class is associated with |
| `LOGGING_LEVEL` | `VARCHAR2(11)` |  | Amount of logging that will be done pertaining to the class:  - `OFF` - `RUNS` - `FAILED RUNS` - `FULL` |
| `LOG_HISTORY` | `NUMBER` |  | History (in days) to maintain in the job log for the class |