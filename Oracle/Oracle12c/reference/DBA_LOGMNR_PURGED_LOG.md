---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_LOGMNR_PURGED_LOG.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_LOGMNR_PURGED_LOG` displays archived redo log files that have been applied to the logical standby database and can be deleted because they are no longer needed.

Files in this view are refreshed as a result of executing the `DBMS_LOGSTDBY.PURGE_SESSION` PL/SQL procedure for Oracle Data Guard SQL Apply:

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_NAME` | `VARCHAR2(513)` |  | Fully qualified names of the archived redo log files that are no longer needed by SQL Apply and can be deleted from the operating system |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS66844) for more information about the `DBMS_LOGSTDBY.PURGE_SESSION` procedure