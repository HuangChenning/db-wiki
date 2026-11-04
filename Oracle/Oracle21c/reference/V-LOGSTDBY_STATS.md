---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGSTDBY_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.63 V$LOGSTDBY\_STATS

`V$LOGSTDBY_STATS` displays statistics, current state, and status information related to SQL Apply.

No rows are returned from this view when SQL Apply is not running. This view is only meaningful in the context of a logical standby database.

All statistics shown in this view are reinitialized at each SQL Apply start.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(64)` | Name of the statistic, state, or status:  Note: Many of the following statistics are subject to change or deletion; programmers should write application code to tolerate missing or extra statistics.  - id of the logminer session used by SQL Apply to mine the redo logs. - number of preparers - number of appliers - server processes in use for SQL Apply - maximum SGA (in MBytes) for LCR cache - whether SQL Apply is preserving the commit order seen at the primary database while applying changes - maximum events recorded in the DBA\_LOGSTDBY\_EVENTS table - whether SQL Apply is logging errors that are skipped in the DBA\_LOGSTDBY\_EVENTS table - whether SQL Apply is logging DDLs that are skipped in the DBA\_LOGSTDBY\_EVENTS table - whether SQL Apply is logging DDLs that are applied in the DBA\_LOGSTDBY\_EVENTS table - whether SQL Apply is logging unsupported operations that are encountered in the DBA\_LOGSTDBY\_EVENTS table - whether or not real time apply is on - value of apply delay (in minutes) - coordinator state - coordinator uptime in seconds - time of the most recent start of SQL Apply - number of transactions mined and made available for apply - number of transactions applied - number of rolled back transactions mined - number of DDL txns mined - number of CTAS (Create Table as Select) txns mined - number of thread enable events encountered in the redo stream - number of thread disable events encountered in the redo stream - bytes of redo records mined - bytes paged out - seconds spent in pageout activity - bytes checkpointed - seconds spent in checkpointing activity - seconds SQL Apply is idle - number of times a complete standby redo logs are mined without having to mine the corresponding archived log - number of times SQL Apply had to switch from a standby redo log to the corresponding archived log - number of times SQL Apply mined redo from the archived logs - number of archived logs that arrived at the standby via gap fetch mechanism (gap fetched logs mined) - number of failed attempts to open a logfile - amount of time spent in waiting for the current gap to resolve if SQL Apply is running in real time mode (current logfile wait) <sup>Foot 1</sup> - time spent in waiting for gap to resolve if SQL Apply is running in real time mode (total logfile wait) <sup>Foot 2</sup> |
| `VALUE` | `VARCHAR2(64)` | Value of the statistic or state information |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

<sup>Footnote 1</sup>

In case SQL Apply is not running in real time mode, this may not reflect time spent in gap resolution, but simply the time spent waiting for the most recent archived log to show up at the logical standby.

<sup>Footnote 2</sup>

In case SQL Apply is not running in real time mode, this will include time that SQL Apply spent every time it finished processing all archived logs registered with it, and waited for the next log to be archived.