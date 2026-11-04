---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_LOGSTDBY_PARAMETERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.164 DBA\_LOGSTDBY\_PARAMETERS

`DBA_LOGSTDBY_PARAMETERS` displays the list of parameters used by SQL apply for logical standby databases.

This view is for logical standby databases only.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(64)` |  | Name of the parameter:  - `MAX_SGA` - System global area (SGA) allocated for the log apply services cache (in megabytes) - `MAX_SERVERS` - Number of processes used by SQL Apply services - `PREPARE_SERVERS` - Controls the number of parallel execution servers used to prepare changes - `APPLY_SERVERS` - Controls the number of parallel execution servers used to apply changes - `MAX_EVENTS_RECORDED` - Number of events stored in the `DBA_LOGSTDBY_EVENTS` view - `RECORD_SKIP_ERRORS` - Indicates records that are skipped - `RECORD_SKIP_DDL` - Indicates skipped DDL statements - `RECORD_APPLIED_DDL` - Indicates applied DDL statements - `RECORD_UNSUPPORTED_OPERATIONS` - Shows whether SQL Apply will capture information about transactions that did unsupported operations at the primary database in the `DBA_LOGSTDBY_EVENTS` view - `EVENT_LOG_DEST` - Indicates where SQL Apply records the occurrence of an interesting event - `LOG_AUTO_DELETE` - Shows whether SQL Apply will automatically delete remote archived logs received from the primary database, once the contents of the logs are applied at the logical standby database. - `LOG_AUTO_DEL_RETENTION_TARGET` - How many minutes a remote archived log received from the primary database will be retained at the logical standby database, once the contents of the log are applied by SQL Apply. - `PRESERVE_COMMIT_ORDER` - Shows whether transactions are committed at the logical standby database in the same order that they were committed at the primary database |
| `VALUE` | `VARCHAR2(2000)` |  | Value of the parameter |
| `UNIT` | `VARCHAR2(64)` |  | Unit of the value, if applicable |
| `SETTING` | `VARCHAR2(64)` |  | Possible values are as follows:  - `SYSTEM` - Parameter value was not explicitly set by the user. However, the user can change it with an appropriate call to the `APPLY_SET` procedure. - `USER` - Parameter value was explicitly set by the user |
| `DYNAMIC` | `VARCHAR2(64)` |  | `YES` if the parameter can be set dynamically (that is, without having to stop SQL Apply)  `NO` if setting the parameter requires that SQL Apply be stopped |

Note:

In a CDB, this view shows data when queried in the root.