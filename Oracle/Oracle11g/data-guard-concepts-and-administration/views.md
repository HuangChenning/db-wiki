---
title: Views Relevant to Oracle Data Guard
book: Data Guard Concepts and Administration
doc_id: E41134-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41134/views.htm
tags:
  - oracle
  - 11g
  - data-guard-concepts-and-administration
---

## 17 Views Relevant to Oracle Data Guard

This chapter describes the views that are especially useful when monitoring a Data Guard environment. The view described in this chapter are a subset of the views that are available for Oracle databases.

Table 17-1 describes the views and indicates if a view applies to physical standby databases, logical standby databases, snapshot standby databases, or primary databases. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for complete information about views.

Table 17-1 Views That Are Pertinent to Data Guard Configurations

| View | Database | Description |
| --- | --- | --- |
| [`DBA_LOGSTDBY_EVENTS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4120.htm#REFRN23121) | Logical only | Contains information about the activity of a logical standby database. It can be used to determine the cause of failures that occur when SQL Apply is applying redo to a logical standby database. |
| [`DBA_LOGSTDBY_HISTORY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4121.htm#REFRN23362) | Logical only | Displays the history of switchovers and failovers for logical standby databases in a Data Guard configuration. It does this by showing the complete sequence of redo log streams processed or created on the local system, across all role transitions. (After a role transition, a new log stream is started and the log stream sequence number is incremented by the new primary database.) |
| [`DBA_LOGSTDBY_LOG`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4122.htm#REFRN23122) | Logical only | Shows the log files registered for logical standby databases. |
| [`DBA_LOGSTDBY_NOT_UNIQUE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4123.htm#REFRN23123) | Logical only | Identifies tables that have no primary and no non-null unique indexes. |
| [`DBA_LOGSTDBY_PARAMETERS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4124.htm#REFRN23124) | Logical only | Contains the list of parameters used by SQL Apply. |
| [`DBA_LOGSTDBY_SKIP`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4126.htm#REFRN23126) | Logical only | Lists the tables that will be skipped by SQL Apply. |
| [`DBA_LOGSTDBY_SKIP_TRANSACTION`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4127.htm#REFRN23127) | Logical only | Lists the skip settings chosen. |
| [`DBA_LOGSTDBY_UNSUPPORTED`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4128.htm#REFRN23128) | Logical only | Identifies the schemas and tables (and columns in those tables) that contain unsupported data types. Use this view when you are preparing to create a logical standby database. |
| [`V$ARCHIVE_DEST`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1012.htm#REFRN30007) | Primary, physical, snapshot, and logical | Describes all of the destinations in the Data Guard configuration, including each destination's current value, mode, and status.  Note: The information in this view does not persist across an instance shutdown. |
| [`V$ARCHIVE_DEST_STATUS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1013.htm#REFRN30008) | Primary, physical, snapshot, and logical | Displays runtime and configuration information for the archived redo log destinations.  Note: The information in this view does not persist across an instance shutdown. |
| [`V$ARCHIVE_GAP`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1014.htm#REFRN30009) | Physical, snapshot, and logical | Displays information to help you identify a gap in the archived redo log files. |
| [`V$ARCHIVED_LOG`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1016.htm#REFRN30011) | Primary, physical, snapshot, and logical | Displays archive redo log information from the control file, including names of the archived redo log files. |
| [`V$DATABASE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1097.htm#REFRN30047) | Primary, physical, snapshot, and logical | Provides database information from the control file. Includes information about fast-start failover (available only with the Data Guard broker). |
| [`V$DATABASE_INCARNATION`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1099.htm#REFRN30049) | Primary, physical, snapshot, and logical | Displays information about all database incarnations. Oracle Database creates a new incarnation whenever a database is opened with the `RESETLOGS` option. Records about the current and the previous incarnation are also contained in the `V$DATABASE` view. |
| [`V$DATAFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1100.htm#REFRN30050) | Primary, physical, snapshot, and logical | Provides datafile information from the control file. |
| [`V$DATAGUARD_CONFIG`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1103.htm#REFRN30053) | Primary, physical, snapshot, and logical | Lists the unique database names defined with the `DB_UNIQUE_NAME` and `LOG_ARCHIVE_CONFIG` initialization parameters. |
| [`V$DATAGUARD_STATS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1104.htm#REFRN30413) | Primary, physical, snapshot, and logical | Displays various Data Guard statistics, including apply lag and transport lag. This view can be queried on any instance of a standby database. No rows are returned if queried on a primary database. See also [Section 8.1.2](role_management.md) for an example and more information. |
| [`V$DATAGUARD_STATUS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1105.htm#REFRN30054) | Primary, physical, snapshot, and logical | Displays and records events that would typically be triggered by any message to the alert log or server process trace files. |
| [`V$FS_FAILOVER_STATS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1150.htm#REFRN30484) | Primary | Displays statistics about fast-start failover occurring on the system. |
| [`V$LOG`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2031.htm#REFRN30127) | Primary, physical, snapshot, and logical | Contains log file information from the online redo log files. |
| [`V$LOGFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2033.htm#REFRN30129) | Primary, physical, snapshot, and logical | Contains information about the online redo log files and standby redo log files. |
| [`V$LOG_HISTORY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2034.htm#REFRN30130) | Primary, physical, snapshot, and logical | Contains log history information from the control file. |
| [`V$LOGSTDBY_PROCESS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2045.htm#REFRN30379) | Logical only | Provides dynamic information about what is happening with SQL Apply. This view is very helpful when you are diagnosing performance problems during SQL Apply on the logical standby database, and it can be helpful for other problems. |
| [`V$LOGSTDBY_PROGRESS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2046.htm#REFRN30380) | Logical only | Displays the progress of SQL Apply on the logical standby database. |
| [`V$LOGSTDBY_STATE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2047.htm#REFRN30381) | Logical only | Consolidates information from the `V$LOGSTDBY_PROCESS` and `V$LOGSTDBY_STATS` views about the running state of SQL Apply and the logical standby database. |
| [`V$LOGSTDBY_STATS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2048.htm#REFRN30143) | Logical only | Displays LogMiner statistics, current state, and status information for a logical standby database during SQL Apply. If SQL Apply is not running, the values for the statistics are cleared. |
| [`V$LOGSTDBY_TRANSACTION`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2049.htm#REFRN30382) | Logical only | Displays information about all active transactions being processed by SQL Apply on the logical standby database. |
| [`V$MANAGED_STANDBY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2050.htm#REFRN30144) | Physical and snapshot | Displays current status information for Oracle database processes related to physical standby databases.  Note: The information in this view does not persist across an instance shutdown. |
| [`V$REDO_DEST_RESP_HISTOGRAM`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2130.htm#REFRN30435) | Primary | Contains the response time information for destinations that are configured for `SYNC` transport.  Note: The information in this view does not persist across an instance shutdown. |
| [`V$STANDBY_EVENT_HISTOGRAM`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3073.htm#REFRN30513) | Physical | Contains a histogram of apply lag values for the physical standby. An entry is made in the corresponding apply lag bucket by the Redo Apply process every second. (This view returns rows only on a physical standby database that has been open in real-time query mode.)  Note: The information in this view does not persist across an instance shutdown. |
| [`V$STANDBY_LOG`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3074.htm#REFRN30263) | Physical, snapshot, and logical | Contains log file information from the standby redo log files. |