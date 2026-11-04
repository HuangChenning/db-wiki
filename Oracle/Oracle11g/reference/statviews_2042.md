---
title: ALL_SCHEDULER_JOB_CLASSES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2042.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_JOB_CLASSES` displays information about the Scheduler job classes accessible to the current user.

Related View

`DBA_SCHEDULER_JOB_CLASSES` displays information about all Scheduler job classes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB_CLASS_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the Scheduler job class |
| `RESOURCE_CONSUMER_GROUP` | `VARCHAR2(30)` |  | Resource consumer group associated with the class |
| `SERVICE` | `VARCHAR2(64)` |  | Name of the service the class is associated with |
| `LOGGING_LEVEL` | `VARCHAR2(11)` |  | Amount of logging that will be done pertaining to the class: |
| `LOG_HISTORY` | `NUMBER` |  | History (in days) to maintain in the job log for the class |
| `COMMENTS` | `VARCHAR2(240)` |  | Comments on the class |

See Also:

["DBA\_SCHEDULER\_JOB\_CLASSES"](statviews_4246.md)