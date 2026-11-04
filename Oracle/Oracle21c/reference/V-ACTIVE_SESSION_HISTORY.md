---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ACTIVE_SESSION_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.8 V$ACTIVE\_SESSION\_HISTORY

`V$ACTIVE_SESSION_HISTORY` displays sampled session activity in the database.

It contains snapshots of active database sessions taken once a second. A database session is considered active if it was on the CPU or was waiting for an event that didn't belong to the `Idle` wait class. Refer to the `V$EVENT_NAME` view for more information on wait classes.

This view contains one row for each active session per sample and returns the latest session sample rows first. A majority of the columns describing the session in the active session history are present in the `V$SESSION` view.

| Column | Datatype | Description |
| --- | --- | --- |
| `SAMPLE_ID` | `NUMBER` | ID of the sample |
| `SAMPLE_TIME` | `TIMESTAMP(3)` | Time at which the sample was taken |
| `SAMPLE_TIME_UTC` | `TIMESTAMP(3)` | Time at which the sample was taken in UTC (Coordinated Universal Time) time zone |
| `USECS_PER_ROW` | `NUMBER` | Time in microseconds since the last sample was taken |
| `IS_AWR_SAMPLE` | `VARCHAR2(1)` | Indicates whether this sample has been flushed or will be flushed to the Automatic Workload Repository (`DBA_HIST_ACTIVE_SESS_HISTORY`) (`Y`) or not (`N`) |
| `SESSION_ID` | `NUMBER` | Session identifier; maps to `V$SESSION.SID` |
| `SESSION_SERIAL#` | `NUMBER` | Session serial number (used to uniquely identify a session's objects); maps to `V$SESSION.SERIAL#` |
| `SESSION_TYPE` | `VARCHAR2(10)` | Session type:  - `FOREGROUND` - `BACKGROUND` |
| `FLAGS` | `NUMBER` | Reserved for future use |
| `USER_ID` | `NUMBER` | Oracle user identifier; maps to `V$SESSION.USER#` |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the SQL statement that the session was executing at the time of sampling |
| `IS_SQLID_CURRENT` | `VARCHAR2(1)` | Indicates whether the SQL identifier in the `SQL_ID` column is being executed (`Y`) or not (`N`) |
| `SQL_CHILD_NUMBER` | `NUMBER` | Child number of the SQL statement that the session was executing at the time of sampling |
| `SQL_OPCODE` | `NUMBER` | Indicates what phase of operation the SQL statement was in; maps to `V$SESSION.COMMAND`  See Also: " [V$SESSION](V-SESSION.md) " for information on interpreting this column |
| `SQL_OPNAME` | `VARCHAR2(64)` | SQL command name |
| `FORCE_MATCHING_SIGNATURE` | `NUMBER` | Signature used when the `CURSOR_SHARING` parameter is set to `FORCE` |
| `TOP_LEVEL_SQL_ID` | `VARCHAR2(13)` | SQL identifier of the top level SQL statement |
| `TOP_LEVEL_SQL_OPCODE` | `NUMBER` | Indicates what phase of operation the top level SQL statement was in |
| `SQL_ADAPTIVE_PLAN_RESOLVED` | `NUMBER` | Indicates whether the SQL plan of the sampled database session is a resolved adaptive plan or not |
| `SQL_FULL_PLAN_HASH_VALUE` | `NUMBER` | Numerical representation of the complete SQL plan for the cursor being executed by this session |
| `SQL_PLAN_HASH_VALUE` | `NUMBER` | Numeric representation of the SQL plan for the cursor. This information might not be available for all session samples. `V$SESSION` does not contain this information. |
| `SQL_PLAN_LINE_ID` | `NUMBER` | SQL plan line ID |
| `SQL_PLAN_OPERATION` | `VARCHAR2(30)` | Plan operation name |
| `SQL_PLAN_OPTIONS` | `VARCHAR2(30)` | Plan operation options |
| `SQL_EXEC_ID` | `NUMBER` | SQL execution identifier |
| `SQL_EXEC_START` | `DATE` | Time when the execution of the SQL started |
| `PLSQL_ENTRY_OBJECT_ID` | `NUMBER` | Object ID of the top-most PL/SQL subprogram on the stack; NULL if there is no PL/SQL subprogram on the stack. Maps to DBA\_OBJECTS.OBJECT\_ID. |
| `PLSQL_ENTRY_SUBPROGRAM_ID` | `NUMBER` | Subprogram ID of the top-most PL/SQL subprogram on the stack. Maps to DBA\_OBJECTS.DATA\_OBJECT\_ID. |
| `PLSQL_OBJECT_ID` | `NUMBER` | Object ID of the currently executing PL/SQL subprogram. Maps to DBA\_OBJECTS.OBJECT\_ID. |
| `PLSQL_SUBPROGRAM_ID` | `NUMBER` | Subprogram ID of the currently executing PL/SQL object; NULL if executing SQL. Maps to DBA\_OBJECTS.DATA\_OBJECT\_ID. |
| `QC_INSTANCE_ID` | `NUMBER` | Query coordinator instance ID. This information is only available if the sampled session is a parallel query worker. For all other sessions, the value is `0`. |
| `QC_SESSION_ID` | `NUMBER` | Query coordinator session ID. This information is only available if the sampled session is a parallel query worker. For all other sessions, the value is `0`. |
| `QC_SESSION_SERIAL#` | `NUMBER` | Query coordinator session serial number. This information is only available if the sampled session is a parallel query worker. For all other sessions, the value is `0`. |
| `PX_FLAGS` | `NUMBER` | Reserved for internal use |
| `EVENT` | `VARCHAR2(64)` | If `SESSION_STATE` = `WAITING`, then the event for which the session was waiting for at the time of sampling.  If `SESSION_STATE` = `ON CPU`, then this column is NULL.  See Also: [Oracle Wait Events](oracle-wait-events.md) |
| `EVENT_ID` | `NUMBER` | Identifier of the resource or event for which the session is waiting or for which the session last waited. Interpretation is similar to that of the `EVENT` column. |
| `EVENT#` | `NUMBER` | Number of the resource or event for which the session is waiting or for which the session last waited. Interpretation is similar to that of the `EVENT` column. |
| `SEQ#` | `NUMBER` | Sequence number that uniquely identifies the wait (incremented for each wait) |
| `P1TEXT` | `VARCHAR2(64)` | Text of the first additional parameter |
| `P1` | `NUMBER` | First additional parameter |
| `P2TEXT` | `VARCHAR2(64)` | Text of the second additional parameter |
| `P2` | `NUMBER` | Second additional parameter |
| `P3TEXT` | `VARCHAR2(64)` | Text of the third additional parameter |
| `P3` | `NUMBER` | Third additional parameter |
| `WAIT_CLASS` | `VARCHAR2(64)` | Wait class name of the event for which the session was waiting at the time of sampling. Interpretation is similar to that of the `EVENT` column. Maps to `V$SESSION.WAIT_CLASS`. |
| `WAIT_CLASS_ID` | `NUMBER` | Wait class identifier of the event for which the session was waiting at the time of sampling. Interpretation is similar to that of the `EVENT` column. Maps to `V$SESSION.WAIT_CLASS_ID`. |
| `WAIT_TIME` | `NUMBER` | Total wait time for the event for which the session last waited if the session was on the CPU when sampled; `0` if the session was waiting at the time of sampling  Note: Whether or not `WAIT_TIME` = `0` is what is useful to find the `SESSION_STATE` at the time of sampling, rather than the actual value of `WAIT_TIME` itself. Maps to `V$SESSION.WAIT_TIME`. |
| `SESSION_STATE` | `VARCHAR2(7)` | Session state:  - `WAITING` - `ON CPU` |
| `TIME_WAITED` | `NUMBER` | If `SESSION_STATE` = `WAITING`, then the time that the session actually spent waiting for that event (in microseconds). This column is set for waits that were in progress at the time the sample was taken.  If a wait event lasted for more than a second and was caught waiting in more than one session sample row, then the actual time spent waiting for that wait event will be populated in the last of those session sample rows. At any given time, this information will not be available for the latest session sample. |
| `BLOCKING_SESSION_STATUS` | `VARCHAR2(11)` | Status of the blocking session:  - `VALID` - `NO` `HOLDER` - `GLOBAL` - `NOT IN WAIT` - `UNKNOWN` |
| `BLOCKING_SESSION` | `NUMBER` | Session identifier of the blocking session. Populated only if the blocker is on the same instance and the session was waiting for enqueues or a "buffer busy" wait. Maps to `V$SESSION.BLOCKING_SESSION`. |
| `BLOCKING_SESSION_SERIAL#` | `NUMBER` | Serial number of the blocking session |
| `BLOCKING_INST_ID` | `NUMBER` | Instance number of the blocker shown in `BLOCKING_SESSION` |
| `BLOCKING_HANGCHAIN_INFO` | `VARCHAR2(1)` | Indicates whether the information about `BLOCKING_SESSION` comes from the hang chain (`Y`) or not (`N`) |
| `CURRENT_OBJ#` | `NUMBER` | Object ID of the object that the session is referencing. This information is only available if the session was waiting for application, cluster, concurrency, and user I/O wait events. Maps to `V$SESSION.ROW_WAIT_OBJ#`. |
| `CURRENT_FILE#` | `NUMBER` | File number of the file containing the block that the session is referencing. This information is only available if the session was waiting for cluster, concurrency, and user I/O wait events. Maps to `V$SESSION.ROW_WAIT_FILE#`. |
| `CURRENT_BLOCK#` | `NUMBER` | ID of the block that the session is referencing. This information is only available if the session was waiting for cluster, concurrency, and user I/O wait events. Maps to `V$SESSION.ROW_WAIT_BLOCK#`. |
| `CURRENT_ROW#` | `NUMBER` | Row identifier that the session is referencing. This information is only available if the session was waiting for cluster, concurrency, and user I/O wait events. Maps to `V$SESSION.ROW_WAIT_ROW#`. |
| `TOP_LEVEL_CALL#` | `NUMBER` | Oracle top level call number |
| `TOP_LEVEL_CALL_NAME` | `VARCHAR2(64)` | Oracle top level call name |
| `CONSUMER_GROUP_ID` | `NUMBER` | Consumer group ID |
| `XID` | `RAW(8)` | Transaction ID that the session was working on at the time of sampling. `V$SESSION` does not contain this information. |
| `REMOTE_INSTANCE#` | `NUMBER` | Remote instance identifier that will serve the block that this session is waiting for. This information is only available if the session was waiting for cluster events. |
| `TIME_MODEL` | `NUMBER` | Time model information |
| `IN_CONNECTION_MGMT` | `VARCHAR2(1)` | Indicates whether the session was doing connection management at the time of sampling (`Y`) or not (`N`) |
| `IN_PARSE` | `VARCHAR2(1)` | Indicates whether the session was parsing at the time of sampling (`Y`) or not (`N`) |
| `IN_HARD_PARSE` | `VARCHAR2(1)` | Indicates whether the session was hard parsing at the time of sampling (`Y`) or not (`N`) |
| `IN_SQL_EXECUTION` | `VARCHAR2(1)` | Indicates whether the session was executing SQL statements at the time of sampling (`Y`) or not (`N`) |
| `IN_PLSQL_EXECUTION` | `VARCHAR2(1)` | Indicates whether the session was executing PL/SQL at the time of sampling (`Y`) or not (`N`) |
| `IN_PLSQL_RPC` | `VARCHAR2(1)` | Indicates whether the session was executing inbound PL/SQL RPC calls at the time of sampling (`Y`) or not (`N`) |
| `IN_PLSQL_COMPILATION` | `VARCHAR2(1)` | Indicates whether the session was compiling PL/SQL at the time of sampling (`Y`) or not (`N`) |
| `IN_JAVA_EXECUTION` | `VARCHAR2(1)` | Indicates whether the session was executing Java at the time of sampling (`Y`) or not (`N`) |
| `IN_BIND` | `VARCHAR2(1)` | Indicates whether the session was doing bind operations at the time of sampling (`Y`) or not (`N`) |
| `IN_CURSOR_CLOSE` | `VARCHAR2(1)` | Indicates whether the session was closing a cursor at the time of sampling (`Y`) or not (`N`) |
| `IN_SEQUENCE_LOAD` | `VARCHAR2(1)` | Indicates whether the session is loading in sequence (in sequence load code) (`Y`) or not (`N`) |
| `IN_INMEMORY_QUERY` | `VARCHAR2(1)` | Indicates whether the session was querying the In-Memory Column Store (IM column store) at the time of sampling (`Y`) or not (`N`) |
| `IN_INMEMORY_POPULATE` | `VARCHAR2(1)` | Indicates whether the session was populating the IM column store at the time of sampling (`Y`) or not (`N`) |
| `IN_INMEMORY_PREPOPULATE` | `VARCHAR2(1)` | Indicates whether the session was prepopulating the IM column store at the time of sampling (`Y`) or not (`N`) |
| `IN_INMEMORY_REPOPULATE` | `VARCHAR2(1)` | Indicates whether the session was repopulating the IM column store at the time of sampling (`Y`) or not (`N`) |
| `IN_INMEMORY_TREPOPULATE` | `VARCHAR2(1)` | Indicates whether the session was trickle repopulating the IM column store at the time of sampling (`Y`) or not (`N`) |
| `IN_TABLESPACE_ENCRYPTION` | `VARCHAR2(1)` | Indicates whether encryption or decryption of a tablespace occurred at the time of sampling (`Y`) or not (`N`) |
| `CAPTURE_OVERHEAD` | `VARCHAR2(1)` | Indicates whether the session is executing capture code (`Y`) or not (`N`) |
| `REPLAY_OVERHEAD` | `VARCHAR2(1)` | Indicates whether the session is executing replay code (`Y`) or not (`N`) |
| `IS_CAPTURED` | `VARCHAR2(1)` | Indicates whether the session is being captured (`Y`) or not (`N`) |
| `IS_REPLAYED` | `VARCHAR2(1)` | Indicates whether the session is being replayed (`Y`) or not (`N`) |
| `IS_REPLAY_SYNC_TOKEN_HOLDER` | `VARCHAR2(1)` | Indicates whether the session is holding a synchronization token (`Y`) or not (`N`) during workload replay |
| `SERVICE_HASH` | `NUMBER` | Hash that identifies the Service; maps to `V$ACTIVE_SERVICES.NAME_HASH` |
| `PROGRAM` | `VARCHAR2(84)` | Name of the operating system program |
| `MODULE` | `VARCHAR2(64)` | Name of the executing module when sampled, as set by the `DBMS_APPLICATION_INFO.SET_MODULE` procedure |
| `ACTION` | `VARCHAR2(64)` | Name of the executing module when sampled, as set by the `DBMS_APPLICATION_INFO.SET_ACTION` procedure |
| `CLIENT_ID` | `VARCHAR2(64)` | Client identifier of the session; maps to `V$SESSION.CLIENT_IDENTIFIER` |
| `MACHINE` | `VARCHAR2(64)` | Client's operating system machine name |
| `PORT` | `NUMBER` | Client port number |
| `ECID` | `VARCHAR2(64)` | Execution context identifier (sent by Application Server) |
| `DBREPLAY_FILE_ID` | `NUMBER` | If the session is being captured or replayed, then `DBREPLAY_FILE_ID` is the file ID for the workload capture or workload replay; otherwise it is NULL. |
| `DBREPLAY_CALL_COUNTER` | `NUMBER` | If the session is being captured or replayed, then `DBREPLAY_CALL_COUNTER` is the call counter of the user call that is being captured or replayed; otherwise it is NULL. |
| `TM_DELTA_TIME` | `NUMBER` | Time interval (in microseconds) over which `TM_DELTA_CPU_TIME` and `TM_DELTA_DB_TIME` are accumulated |
| `TM_DELTA_CPU_TIME` | `NUMBER` | Amount of time this session spent on CPU over the last `TM_DELTA_TIME` microseconds |
| `TM_DELTA_DB_TIME` | `NUMBER` | Amount of time spent by this session in database calls over the last `TM_DELTA_TIME` microseconds |
| `DELTA_TIME` | `NUMBER` | Time interval (in microseconds) since the last time this session was sampled or created, over which the next five statistics are accumulated |
| `DELTA_READ_IO_REQUESTS` | `NUMBER` | Number of read I/O requests made by this session over the last `DELTA_TIME` microseconds |
| `DELTA_WRITE_IO_REQUESTS` | `NUMBER` | Number of write I/O requests made by this session over the last `DELTA_TIME` microseconds |
| `DELTA_READ_IO_BYTES` | `NUMBER` | Number of I/O bytes read by this session over the last `DELTA_TIME` microseconds |
| `DELTA_WRITE_IO_BYTES` | `NUMBER` | Number of I/O bytes written by this session over the last `DELTA_TIME` microseconds |
| `DELTA_INTERCONNECT_IO_BYTES` | `NUMBER` | Number of I/O bytes sent over the I/O interconnect over the last `DELTA_TIME` microseconds |
| `DELTA_READ_MEM_BYTES` | `NUMBER` | Number of read bytes through the buffer cache |
| `PGA_ALLOCATED` | `NUMBER` | Amount of PGA memory (in bytes) consumed by this session at the time this sample was taken |
| `TEMP_SPACE_ALLOCATED` | `NUMBER` | Amount of TEMP memory (in bytes) consumed by this session at the time this sample was taken |
| `CON_DBID` | `NUMBER` | The database ID of the pluggable database (PDB) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `DBOP_NAME` | `VARCHAR2(30)` | Database operation name. If the type is SQL, the `DBOP_NAME` will be `NULL`. |
| `DBOP_EXEC_ID` | `NUMBER` | Database operation execution identifier for the current execution. If the type is SQL, the `DBOP_EXEC_ID` will be `NULL`. |

See Also:

- " [V$SESSION](V-SESSION.md) "
- " [V$ALL\_ACTIVE\_SESSION\_HISTORY](V-ALL_ACTIVE_SESSION_HISTORY.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS65239) for more information about the `DBMS_APPLICATION_INFO.SET_MODULE` procedure
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS65235) for more information about the `DBMS_APPLICATION_INFO.SET_ACTION` procedure