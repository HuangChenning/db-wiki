---
title: "V$SESSION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3016.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SESSION` displays session information for each current session.

| Column | Datatype | Description |
| --- | --- | --- |
| `SADDR` | `RAW(4 \| 8)` | Session address |
| `SID` | `NUMBER` | Session identifier |
| `SERIAL#` | `NUMBER` | Session serial number. Used to uniquely identify a session's objects. Guarantees that session-level commands are applied to the correct session objects if the session ends and another session begins with the same session ID. |
| `AUDSID` | `NUMBER` | Auditing session ID |
| `PADDR` | `RAW(4 \| 8)` | Address of the process that owns the session |
| `USER#` | `NUMBER` | Oracle user identifier |
| `USERNAME` | `VARCHAR2(30)` | Oracle username |
| `COMMAND` | `NUMBER` | Command in progress (last statement parsed).  You can find the command name for any value n returned in this `COMMAND` column by running this SQL query:  ``` SELECT command_name    FROM v$sqlcommand    WHERE command_type = n ; ```  A value of `0` in this `COMMAND` column means the command is not recorded in `V$SESSION`. |
| `OWNERID` | `NUMBER` | Identifier of the user who owns the migratable session; the column contents are invalid if the value is `2147483644`  For operations using Parallel Slaves, interpret this value as a 4-byte value. The low-order 2 bytes represent the session number and the high-order bytes represent the instance ID of the query coordinator. |
| `TADDR` | `VARCHAR2(8)` | Address of the transaction state object |
| `LOCKWAIT` | `VARCHAR2(8)` | Address of the lock the session is waiting for; NULL if none |
| `STATUS` | `VARCHAR2(8)` | Status of the session: - `ACTIVE` - Session currently executing SQL - `INACTIVE` - Session which is inactive and either has no configured limits or has not yet exceeded the configured limits - `KILLED` - Session marked to be killed - `CACHED` - Session temporarily cached for use by Oracle\*XA - `SNIPED` - An inactive session that has exceeded some configured limits (for example, resource limits specified for the resource manager consumer group or idle\_time specified in the user's profile). Such sessions will not be allowed to become active again. |
| `SERVER` | `VARCHAR2(9)` | Server type: - `DEDICATED` - `SHARED` - `PSEUDO` - `POOLED` - `NONE` |
| `SCHEMA#` | `NUMBER` | Schema user identifier |
| `SCHEMANAME` | `VARCHAR2(30)` | Schema user name |
| `OSUSER` | `VARCHAR2(30)` | Operating system client user name |
| `PROCESS` | `VARCHAR2(24)` | Operating system client process ID |
| `MACHINE` | `VARCHAR2(64)` | Operating system machine name |
| `PORT` | `NUMBER` | Client port number |
| `TERMINAL` | `VARCHAR2(30)` | Operating system terminal name |
| `PROGRAM` | `VARCHAR2(48)` | Operating system program name |
| `TYPE` | `VARCHAR2(10)` | Session type |
| `SQL_ADDRESS` | `RAW(4 \| 8)` | Used with `SQL_HASH_VALUE` to identify the SQL statement that is currently being executed |
| `SQL_HASH_VALUE` | `NUMBER` | Used with `SQL_ADDRESS` to identify the SQL statement that is currently being executed |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the SQL statement that is currently being executed |
| `SQL_CHILD_NUMBER` | `NUMBER` | Child number of the SQL statement that is currently being executed |
| `SQL_EXEC_START` | `DATE` | Time when the execution of the SQL currently executed by this session started; NULL if `SQL_ID` is NULL |
| `SQL_EXEC_ID` | `NUMBER` | SQL execution identifier; NULL if `SQL_ID` is NULL or if the execution of that SQL has not yet started (see `V$SQL_MONITOR`) |
| `PREV_SQL_ADDR` | `RAW(4 \| 8)` | Used with `PREV_HASH_VALUE` to identify the last SQL statement executed |
| `PREV_HASH_VALUE` | `NUMBER` | Used with `SQL_HASH_VALUE` to identify the last SQL statement executed |
| `PREV_SQL_ID` | `VARCHAR2(13)` | SQL identifier of the last SQL statement executed |
| `PREV_CHILD_NUMBER` | `NUMBER` | Child number of the last SQL statement executed |
| `PREV_EXEC_START` | `DATE` | SQL execution start of the last executed SQL statement |
| `PREV_EXEC_ID` | `NUMBER` | SQL execution identifier of the last executed SQL statement |
| `PLSQL_ENTRY_OBJECT_ID` | `NUMBER` | Object ID of the top-most PL/SQL subprogram on the stack; NULL if there is no PL/SQL subprogram on the stack |
| `PLSQL_ENTRY_SUBPROGRAM_ID` | `NUMBER` | Subprogram ID of the top-most PL/SQL subprogram on the stack; NULL if there is no PL/SQL subprogram on the stack |
| `PLSQL_OBJECT_ID` | `NUMBER` | Object ID of the currently executing PL/SQL subprogram; NULL if executing SQL |
| `PLSQL_SUBPROGRAM_ID` | `NUMBER` | Subprogram ID of the currently executing PL/SQL object; NULL if executing SQL |
| `MODULE` <sup>Foot 1</sup> | `VARCHAR2(48)` | Name of the currently executing module as set by calling the `DBMS_APPLICATION_INFO.SET_MODULE` procedure |
| `MODULE_HASH` | `NUMBER` | Hash value of the `MODULE` column |
| `ACTION` <sup>Footref 1</sup> | `VARCHAR2(32)` | Name of the currently executing action as set by calling the `DBMS_APPLICATION_INFO.SET_ACTION` procedure |
| `ACTION_HASH` | `NUMBER` | Hash value of the `ACTION` column |
| `CLIENT_INFO` | `VARCHAR2(64)` | Information set by the `DBMS_APPLICATION_INFO.SET_CLIENT_INFO` procedure |
| `FIXED_TABLE_SEQUENCE` | `NUMBER` | This contains a number that increases every time the session completes a call to the database and there has been an intervening select from a dynamic performance table. This column can be used by performance monitors to monitor statistics in the database. Each time the performance monitor looks at the database, it only needs to look at sessions that are currently active or have a higher value in this column than the highest value that the performance monitor saw the last time. All the other sessions have been idle since the last time the performance monitor looked at the database. |
| `ROW_WAIT_OBJ#` | `NUMBER` | Object ID for the table containing the row specified in `ROW_WAIT_ROW#` |
| `ROW_WAIT_FILE#` | `NUMBER` | Identifier for the datafile containing the row specified in `ROW_WAIT_ROW#`. This column is valid only if the session is currently waiting for another transaction to commit and the value of `ROW_WAIT_OBJ#` is not `-1`. |
| `ROW_WAIT_BLOCK#` | `NUMBER` | Identifier for the block containing the row specified in `ROW_WAIT_ROW#`. This column is valid only if the session is currently waiting for another transaction to commit and the value of `ROW_WAIT_OBJ#` is not `-1`. |
| `ROW_WAIT_ROW#` | `NUMBER` | Current row being locked. This column is valid only if the session is currently waiting for another transaction to commit and the value of `ROW_WAIT_OBJ#` is not `-1`. |
| `TOP_LEVEL_CALL#` | `NUMBER` | Oracle top level call number |
| `LOGON_TIME` | `DATE` | Time of logon |
| `LAST_CALL_ET` | `NUMBER` | If the session `STATUS` is currently `ACTIVE`, then the value represents the elapsed time (in seconds) since the session has become active.  If the session `STATUS` is currently `INACTIVE`, then the value represents the elapsed time (in seconds) since the session has become inactive. |
| `PDML_ENABLED` | `VARCHAR2(3)` | This column has been replaced by the `PDML_STATUS` column |
| `FAILOVER_TYPE` | `VARCHAR2(13)` | Indicates whether and to what extent transparent application failover (TAF) is enabled for the session: - `NONE` - Failover is disabled for this session - `SESSION` - Client is able to fail over its session following a disconnect - `SELECT` - Client is able to fail over queries in progress as well  See Also:  - [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for more information on TAF - [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for information on configuring TAF |
| `FAILOVER_METHOD` | `VARCHAR2(10)` | Indicates the transparent application failover method for the session: - `NONE` - Failover is disabled for this session - `BASIC` - Client itself reconnects following a disconnect - `PRECONNECT` - Backup instance can support all connections from every instance for which it is backed up |
| `FAILED_OVER` | `VARCHAR2(3)` | Indicates whether the session is running in failover mode and failover has occurred (`YES`) or not (`NO`) |
| `RESOURCE_CONSUMER_GROUP` | `VARCHAR2(32)` | Name of the session's current resource consumer group |
| `PDML_STATUS` | `VARCHAR2(8)` | If `ENABLED`, the session is in a `PARALLEL` `DML` enabled mode. If `DISABLED`, `PARALLEL` `DML` enabled mode is not supported for the session. If `FORCED`, the session has been altered to force `PARALLEL` `DML`. |
| `PDDL_STATUS` | `VARCHAR2(8)` | If `ENABLED`, the session is in a `PARALLEL` `DDL` enabled mode. If `DISABLED`, `PARALLEL` `DDL` enabled mode is not supported for the session. If `FORCED`, the session has been altered to force `PARALLEL` `DDL`. |
| `PQ_STATUS` | `VARCHAR2(8)` | If `ENABLED`, the session is in a `PARALLEL` `QUERY` enabled mode. If `DISABLED`, `PARALLEL` `QUERY` enabled mode is not supported for the session. If `FORCED`, the session has been altered to force `PARALLEL` `QUERY`. |
| `CURRENT_QUEUE_DURATION` | `NUMBER` | If queued (`1`), the current amount of time the session has been queued. If not currently queued, the value is `0`. |
| `CLIENT_IDENTIFIER` | `VARCHAR2(64)` | Client identifier of the session |
| `BLOCKING_SESSION_STATUS` | `VARCHAR2(11)` | This column provides details on whether there is a blocking session: - `VALID` - there is a blocking session, and it is identified in the `BLOCKING_INSTANCE` and `BLOCKING_SESSION` columns - `NO HOLDER` - there is no session blocking this session - `NOT IN WAIT` - this session is not in a wait - `UNKNOWN` - the blocking session is unknown |
| `BLOCKING_INSTANCE` | `NUMBER` | Instance identifier of the blocking session. This column is valid only if `BLOCKING_SESSION_STATUS` has the value `VALID`. |
| `BLOCKING_SESSION` | `NUMBER` | Session identifier of the blocking session. This column is valid only if `BLOCKING_SESSION_STATUS` has the value `VALID`. |
| `FINAL_BLOCKING_SESSION_STATUS` | `VARCHAR2(11)` | The final blocking session is the final element in the wait chain constructed by following the sessions that are blocked by one another starting with this session. In the case of a cyclical wait chain, one of the sessions in the wait chain will be chosen as the final blocker.  This column provides details on whether there is a final blocking session:  - `VALID` - there is a final blocking session and it is identified in the `FINAL_BLOCKING_INSTANCE` and `FINAL_BLOCKING_SESSION` columns - `NO HOLDER` - there is no session blocking this session - `NOT IN WAIT` - this session is not in a wait - `UNKNOWN` - the final blocking session is unknown |
| `FINAL_BLOCKING_INSTANCE` | `NUMBER` | Instance identifier of the final blocking session. This column is valid only if `FINAL_BLOCKING_SESSION_STATUS` has the value `VALID`. |
| `FINAL_BLOCKING_SESSION` | `NUMBER` | Session identifier of the blocking session. This column is valid only if `FINAL_BLOCKING_SESSION_STATUS` has the value `VALID`. |
| `SEQ#` | `NUMBER` | A number that uniquely identifies the current or last wait (incremented for each wait) |
| `EVENT#` | `NUMBER` | Event number |
| `EVENT` | `VARCHAR2(64)` | Resource or event for which the session is waiting  See Also: [Appendix C, "Oracle Wait Events"](waitevents.md) |
| `P1TEXT` | `VARCHAR2(64)` | Description of the first wait event parameter |
| `P1` | `NUMBER` | First wait event parameter (in decimal) |
| `P1RAW` | `RAW(8)` | First wait event parameter (in hexadecimal) <sup>Foot 2</sup> |
| `P2TEXT` | `VARCHAR2(64)` | Description of the second wait event parameter |
| `P2` | `NUMBER` | Second wait event parameter (in decimal) |
| `P2RAW` | `RAW(8)` | Second wait event parameter (in hexadecimal) <sup>Footref 2</sup> |
| `P3TEXT` | `VARCHAR2(64)` | Description of the third wait event parameter |
| `P3` | `NUMBER` | Third wait event parameter (in decimal) |
| `P3RAW` | `RAW(8)` | Third wait event parameter (in hexadecimal) <sup>Footref 2</sup> |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the class of the wait event |
| `WAIT_CLASS#` | `NUMBER` | Number of the class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` | Name of the class of the wait event |
| `WAIT_TIME` | `NUMBER` | If the session is currently waiting, then the value is `0`. If the session is not in a wait, then the value is as follows: - \> `0` - Value is the duration of the last wait in hundredths of a second - `-1` - Duration of the last wait was less than a hundredth of a second - `-2` - Parameter `TIMED_STATISTICS` was set to `false`  This column has been deprecated in favor of the columns `WAIT_TIME_MICRO` and `STATE`. |
| `SECONDS_IN_WAIT` | `NUMBER` | If the session is currently waiting, then the value is the amount of time waited for the current wait. If the session is not in a wait, then the value is the amount of time since the start of the last wait.  This column has been deprecated in favor of the columns `WAIT_TIME_MICRO` and `TIME_SINCE_LAST_WAIT_MICRO`. |
| `STATE` | `VARCHAR2(19)` | Wait state: - `WAITING` - Session is currently waiting - `WAITED UNKNOWN TIME` - Duration of the last wait is unknown; this is the value when the parameter `TIMED_STATISTICS` is set to `false` - `WAITED SHORT TIME` - Last wait was less than a hundredth of a second - `WAITED KNOWN TIME` - Duration of the last wait is specified in the `WAIT_TIME` column |
| `WAIT_TIME_MICRO` | `NUMBER` | Amount of time waited (in microseconds). If the session is currently waiting, then the value is the time spent in the current wait. If the session is currently not in a wait, then the value is the amount of time waited in the last wait. |
| `TIME_REMAINING_MICRO` | `NUMBER` | Value is interpreted as follows: - \> `0` - Amount of time remaining for the current wait (in microseconds) - `0` - Current wait has timed out - `-1` - Session can indefinitely wait in the current wait - NULL - Session is not currently waiting |
| `TIME_SINCE_LAST_WAIT_MICRO` | `NUMBER` | Time elapsed since the end of the last wait (in microseconds). If the session is currently in a wait, then the value is `0`. |
| `SERVICE_NAME` | `VARCHAR2(64)` | Service name of the session |
| `SQL_TRACE` | `VARCHAR2(8)` | Indicates whether SQL tracing is enabled (`ENABLED`) or disabled (`DISABLED`) |
| `SQL_TRACE_WAITS` | `VARCHAR2(5)` | Indicates whether wait tracing is enabled (`TRUE`) or not (`FALSE`) |
| `SQL_TRACE_BINDS` | `VARCHAR2(5)` | Indicates whether bind tracing is enabled (`TRUE`) or not (`FALSE`) |
| `SQL_TRACE_PLAN_STATS` | `VARCHAR2(10)` | Frequency at which row source statistics are dumped in the trace files for each cursor: - `never` - `first_execution` - `all_executions` |
| `SESSION_EDITION_ID` | `NUMBER` | Shows the value that, in the session, would be reported by `sys_context('USERENV', 'SESSION_EDITION_ID')` |
| `CREATOR_ADDR` | `RAW(4 \| 8)` | Address of the creating process or circuit |
| `CREATOR_SERIAL#` | `NUMBER` | Serial number of the creating process or circuit |
| `ECID` | `VARCHAR2(64)` | Execution context identifier (sent by Application Server) |

<sup>Footnote 1</sup> The datatype of this column is `VARCHAR2(64)` starting with Oracle Database 11g Release 2 (11.2.0.2).

<sup>Footnote 2</sup> The `P1RAW`, `P2RAW`, and `P3RAW` columns display the same values as the `P1`, `P2`, and `P3` columns, except that the numbers are displayed in hexadecimal.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/instance_tune.htm#PFGRF94483) for an example of using `V$SESSION` to determine which sessions are waiting for I/O
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/instance_tune.htm#PFGRF94473) for an example of using `V$SESSION` to help identify an object that is waiting for buffer busy waits