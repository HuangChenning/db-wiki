---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_ACTIVE_SESS_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.372 DBA\_HIST\_ACTIVE\_SESS\_HISTORY

`DBA_HIST_ACTIVE_SESS_HISTORY` displays the history of the contents of the in-memory active session history of recent system activity.

`DBA_HIST_ACTIVE_SESS_HISTORY` contains snapshots of `V$ACTIVE_SESSION_HISTORY`. See " [V$ACTIVE\_SESSION\_HISTORY](V-ACTIVE_SESSION_HISTORY.md) " for further interpretation details for many of these columns (except `SNAP_ID`, `DBID`, and `INSTANCE_NUMBER`).

Note:

If you want to perform a join with the snapshots view, use the `DBA_HIST_ASH_SNAPSHOT` view instead of the `DBA_HIST_SNAPSHOT` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `SAMPLE_ID` | `NUMBER` | `NOT NULL` | ID of the sample |
| `SAMPLE_TIME` | `TIMESTAMP(3)` | `NOT NULL` | Time of the sample |
| `SAMPLE_TIME_UTC` | `TIMESTAMP(3)` |  | `SAMPLE_TIME` in UTC |
| `USECS_PER_ROW` | `NUMBER` |  | Time in microseconds since the last active session history sample |
| `SESSION_ID` | `NUMBER` | `NOT NULL` | Session identifier |
| `SESSION_SERIAL#` | `NUMBER` |  | Session serial number (used to uniquely identify a session's objects) |
| `SESSION_TYPE` | `VARCHAR2(10)` |  | Session type:  - `FOREGROUND` - `BACKGROUND` |
| `FLAGS` | `NUMBER` |  | Reserved for future use |
| `USER_ID` | `NUMBER` |  | Oracle user identifier |
| `SQL_ID` | `VARCHAR2(13)` |  | SQL identifier of the SQL statement that is currently being executed |
| `IS_SQLID_CURRENT` | `VARCHAR2(1)` |  | Indicates whether the SQL identifier in the `SQL_ID` column is being executed (`Y`) or not (`N`) |
| `SQL_CHILD_NUMBER` | `NUMBER` |  | Child number of the SQL statement that is currently being executed |
| `SQL_OPCODE` | `NUMBER` |  | Indicates what phase of operation the SQL statement is in |
| `SQL_OPNAME` | `VARCHAR2(64)` |  | SQL command name |
| `FORCE_MATCHING_SIGNATURE` | `NUMBER` |  | Signature used when the `CURSOR_SHARING` parameter is set to `FORCE` |
| `TOP_LEVEL_SQL_ID` | `VARCHAR2(13)` |  | SQL identifier of the top level SQL statement |
| `TOP_LEVEL_SQL_OPCODE` | `NUMBER` |  | Indicates what phase of operation the top level SQL statement was in |
| `SQL_PLAN_HASH_VALUE` | `NUMBER` |  | Numerical representation of the SQL plan for the cursor |
| `SQL_FULL_PLAN_HASH_VALUE` | `NUMBER` |  | Numerical representation of the complete SQL plan for the cursor being executed by this session |
| `SQL_ADAPTIVE_PLAN_RESOLVED` | `NUMBER` |  | Indicates whether the SQL plan of the sampled database session is a resolved adaptive plan or not |
| `SQL_PLAN_LINE_ID` | `NUMBER` |  | SQL plan line ID |
| `SQL_PLAN_OPERATION` | `VARCHAR2(64)` |  | Plan operation name |
| `SQL_PLAN_OPTIONS` | `VARCHAR2(64)` |  | Plan operation options |
| `SQL_EXEC_ID` | `NUMBER` |  | SQL execution identifier |
| `SQL_EXEC_START` | `DATE` |  | Time when the execution of the SQL started |
| `PLSQL_ENTRY_OBJECT_ID` | `NUMBER` |  | Object ID of the top-most PL/SQL subprogram on the stack (or NULL if there is no PL/SQL subprogram on the stack) |
| `PLSQL_ENTRY_SUBPROGRAM_ID` | `NUMBER` |  | Subprogram ID of the top-most PL/SQL subprogram on the stack (or NULL if there is no PL/SQL subprogram on the stack) |
| `PLSQL_OBJECT_ID` | `NUMBER` |  | Object ID of the currently executing PL/SQL subprogram (or NULL if executing SQL) |
| `PLSQL_SUBPROGRAM_ID` | `NUMBER` |  | Subprogram ID of the currently executing PL/SQL object (or NULL if executing SQL) |
| `QC_INSTANCE_ID` | `NUMBER` |  | Query coordinator instance ID |
| `QC_SESSION_ID` | `NUMBER` |  | Query coordinator session ID |
| `QC_SESSION_SERIAL#` | `NUMBER` |  | Query coordinator session serial number |
| `PX_FLAGS` | `NUMBER` |  | Reserved for internal use |
| `EVENT` | `VARCHAR2(64)` |  | If `SESSION_STATE = WAITING`, then the event for which the session was waiting at the time of sampling.  If `SESSION_STATE = ON CPU`, then this column will be NULL. |
| `EVENT_ID` | `NUMBER` |  | Identifier of the resource or event for which the session is waiting or for which the session last waited |
| `SEQ#` | `NUMBER` |  | Sequence number that uniquely identifies the wait (incremented for each wait) |
| `P1TEXT` | `VARCHAR2(64)` |  | Text of first additional parameter |
| `P1` | `NUMBER` |  | First additional parameter |
| `P2TEXT` | `VARCHAR2(64)` |  | Text of second additional parameter |
| `P2` | `NUMBER` |  | Second additional parameter |
| `P3TEXT` | `VARCHAR2(64)` |  | Text of third additional parameter |
| `P3` | `NUMBER` |  | Third additional parameter |
| `WAIT_CLASS` | `VARCHAR2(64)` |  | Wait class name of the event for which the session was waiting at the time of sampling. Interpretation is similar to that of the `EVENT` column. Maps to `V$SESSION.WAIT_CLASS`. |
| `WAIT_CLASS_ID` | `NUMBER` |  | Wait class identifier of the event for which the session was waiting at the time of sampling. Interpretation is similar to that of the `EVENT` column. Maps to `V$SESSION.WAIT_CLASS_ID`. |
| `WAIT_TIME` | `NUMBER` |  | Total wait time (in microseconds) for the event for which the session last waited (`0` if currently waiting) |
| `SESSION_STATE` | `VARCHAR2(7)` |  | Session state:  - `WAITING` - `ON` `CPU` |
| `TIME_WAITED` | `NUMBER` |  | Time that the current session actually spent waiting for the event (in microseconds). This column is set for waits that were in progress at the time the sample was taken. |
| `BLOCKING_SESSION_STATUS` | `VARCHAR2(11)` |  | Status of the blocking session:  - `VALID` - `NO HOLDER` - `GLOBAL` - `NOT IN WAIT` - `UNKNOWN` |
| `BLOCKING_SESSION` | `NUMBER` |  | Session identifier of the blocking session. Populated only when the session was waiting for enqueues or a "buffer busy" wait. Maps to `V$SESSION.BLOCKING_SESSION`. |
| `BLOCKING_SESSION_SERIAL#` | `NUMBER` |  | Serial number of the blocking session |
| `BLOCKING_INST_ID` | `NUMBER` |  | Instance number of the blocker shown in `BLOCKING_SESSION` |
| `BLOCKING_HANGCHAIN_INFO` | `VARCHAR2(1)` |  | Indicates whether the information about `BLOCKING_SESSION` comes from the hang chain (`Y`) or not (`N`) |
| `CURRENT_OBJ#` | `NUMBER` |  | Object ID of the object that the session is currently referencing. This information is only available if the session was waiting for Application, Cluster, Concurrency, and User I/O wait events. Maps to `V$SESSION.ROW_WAIT_OBJ#`. |
| `CURRENT_FILE#` | `NUMBER` |  | File number of the file containing the block that the session is currently referencing. This information is only available if the session was waiting for Cluster, Concurrency, and User I/O wait events. Maps to `V$SESSION.ROW_WAIT_FILE#`. |
| `CURRENT_BLOCK#` | `NUMBER` |  | ID of the block that the session is currently referencing |
| `CURRENT_ROW#` | `NUMBER` |  | Row identifier that the session is referencing |
| `TOP_LEVEL_CALL#` | `NUMBER` |  | Oracle top level call number |
| `TOP_LEVEL_CALL_NAME` | `VARCHAR2(64)` |  | Oracle top level call name |
| `CONSUMER_GROUP_ID` | `NUMBER` |  | Consumer group ID |
| `XID` | `RAW(8)` |  | Transaction ID that the session was working on at the time of sampling. `V$SESSION` does not contain this information. |
| `REMOTE_INSTANCE#` | `NUMBER` |  | Remote instance identifier that will serve the block that this session is waiting for. This information is only available if the session was waiting for cluster events. |
| `TIME_MODEL` | `NUMBER` |  | Time model information |
| `IN_CONNECTION_MGMT` | `VARCHAR2(1)` |  | Indicates whether the session was doing connection management at the time of sampling (`Y`) or not (`N`) |
| `IN_PARSE` | `VARCHAR2(1)` |  | Indicates whether the session was parsing at the time of sampling (`Y`) or not (`N`) |
| `IN_HARD_PARSE` | `VARCHAR2(1)` |  | Indicates whether the session was hard parsing at the time of sampling (`Y`) or not (`N`) |
| `IN_SQL_EXECUTION` | `VARCHAR2(1)` |  | Indicates whether the session was executing SQL statements at the time of sampling (`Y`) or not (`N`) |
| `IN_PLSQL_EXECUTION` | `VARCHAR2(1)` |  | Indicates whether the session was executing PL/SQL at the time of sampling (`Y`) or not (`N`) |
| `IN_PLSQL_RPC` | `VARCHAR2(1)` |  | Indicates whether the session was executing inbound PL/SQL RPC calls at the time of sampling (`Y`) or not (`N`) |
| `IN_PLSQL_COMPILATION` | `VARCHAR2(1)` |  | Indicates whether the session was compiling PL/SQL at the time of sampling (`Y`) or not (`N`) |
| `IN_JAVA_EXECUTION` | `VARCHAR2(1)` |  | Indicates whether the session was executing Java at the time of sampling (`Y`) or not (`N`) |
| `IN_BIND` | `VARCHAR2(1)` |  | Indicates whether the session was doing bind operations at the time of sampling (`Y`) or not (`N`) |
| `IN_CURSOR_CLOSE` | `VARCHAR2(1)` |  | Indicates whether the session was closing a cursor at the time of sampling (`Y`) or not (`N`) |
| `IN_SEQUENCE_LOAD` | `VARCHAR2(1)` |  | Indicates whether the session is loading in sequence (in sequence load code) (`Y`) or not (`N`) |
| `IN_INMEMORY_QUERY` | `VARCHAR2(1)` |  | Indicates whether the session was querying the In-Memory Column Store (IM column store) at the time of sampling (`Y`) or not (`N`) |
| `IN_INMEMORY_POPULATE` | `VARCHAR2(1)` |  | Indicates whether the session was populating the IM column store at the time of sampling (`Y`) or not (`N`) |
| `IN_INMEMORY_PREPOPULATE` | `VARCHAR2(1)` |  | Indicates whether the session was prepopulating the IM column store at the time of sampling (`Y`) or not (`N`) |
| `IN_INMEMORY_REPOPULATE` | `VARCHAR2(1)` |  | Indicates whether the session was repopulating the IM column store at the time of sampling (`Y`) or not (`N`) |
| `IN_INMEMORY_TREPOPULATE` | `VARCHAR2(1)` |  | Indicates whether the session was trickle repopulating the IM column store at the time of sampling (`Y`) or not (`N`) |
| `IN_TABLESPACE_ENCRYPTION` | `VARCHAR2(1)` |  | Indicates whether encryption or decryption of a tablespace occurred at the time of sampling (`Y`) or not (`N`) |
| `CAPTURE_OVERHEAD` | `VARCHAR2(1)` |  | Indicates whether the session is executing capture code (`Y`) or not (`N`) |
| `REPLAY_OVERHEAD` | `VARCHAR2(1)` |  | Indicates whether the session is executing replay code (`Y`) or not (`N`) |
| `IS_CAPTURED` | `VARCHAR2(1)` |  | Indicates whether the session is being captured (`Y`) or not (`N`) |
| `IS_REPLAYED` | `VARCHAR2(1)` |  | Indicates whether the session is being replayed (`Y`) or not (`N`) |
| `IS_REPLAY_SYNC_TOKEN_HOLDER` | `VARCHAR2(1)` |  | Indicates whether the session is holding a synchronization token (`Y`) or not (`N`) during workload replay |
| `SERVICE_HASH` | `NUMBER` |  | Hash that identifies the Service |
| `PROGRAM` | `VARCHAR2(84)` |  | Name of the operating system program |
| `MODULE` | `VARCHAR2(64)` |  | Name of the currently executing module as set by the `DBMS_APPLICATION_INFO.SET_MODULE` procedure |
| `ACTION` | `VARCHAR2(64)` |  | Name of the currently executing action as set by the `DBMS_APPLICATION_INFO.SET_ACTION` procedure |
| `CLIENT_ID` | `VARCHAR2(64)` |  | Client identifier of the session |
| `MACHINE` | `VARCHAR2(64)` |  | Client's operating system machine name |
| `PORT` | `NUMBER` |  | Client port number |
| `ECID` | `VARCHAR2(64)` |  | Execution context identifier (sent by Application Server) |
| `DBREPLAY_FILE_ID` | `NUMBER` |  | If the session is being captured or replayed, then `DBREPLAY_FILE_ID` is the file ID for the workload capture or workload replay; otherwise it is NULL. |
| `DBREPLAY_CALL_COUNTER` | `NUMBER` |  | If the session is being captured or replayed, then `DBREPLAY_CALL_COUNTER` is the call counter of the user call that is being captured or replayed; otherwise it is NULL. |
| `TM_DELTA_TIME` | `NUMBER` |  | Time interval (in microseconds) over which `TM_DELTA_CPU_TIME` and `TM_DELTA_DB_TIME` are accumulated |
| `TM_DELTA_CPU_TIME` | `NUMBER` |  | Amount of time this session spent on CPU over the last `TM_DELTA_TIME` microseconds |
| `TM_DELTA_DB_TIME` | `NUMBER` |  | Amount of time spent by this session in database calls over the last `TM_DELTA_TIME` microseconds |
| `DELTA_TIME` | `NUMBER` |  | Time interval (in microseconds) since the last time this session was sampled or created, over which the next five statistics are accumulated |
| `DELTA_READ_IO_REQUESTS` | `NUMBER` |  | Number of read I/O requests made by this session over the last `DELTA_TIME` microseconds |
| `DELTA_WRITE_IO_REQUESTS` | `NUMBER` |  | Number of write I/O requests made by this session over the last `DELTA_TIME` microseconds |
| `DELTA_READ_IO_BYTES` | `NUMBER` |  | Number of I/O bytes read by this session over the last `DELTA_TIME` microseconds |
| `DELTA_WRITE_IO_BYTES` | `NUMBER` |  | Number of I/O bytes written by this session over the last `DELTA_TIME` microseconds |
| `DELTA_INTERCONNECT_IO_BYTES` | `NUMBER` |  | Number of I/O bytes sent over the I/O interconnect over the last `DELTA_TIME` microseconds |
| `PGA_ALLOCATED` | `NUMBER` |  | Amount of PGA memory (in bytes) consumed by this session at the time this sample was taken |
| `TEMP_SPACE_ALLOCATED` | `NUMBER` |  | Amount of TEMP memory (in bytes) consumed by this session at the time this sample was taken |
| `DBOP_NAME` | `VARCHAR2(64)` |  | Database operation name. If the type is SQL, the `DBOP_NAME` will be `NULL`. |
| `DBOP_EXEC_ID` | `NUMBER` |  | Database operation execution identifier for the current execution. If the type is SQL, the `DBOP_EXEC_ID` will be `NULL`. |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [DBA\_HIST\_ASH\_SNAPSHOT](DBA_HIST_ASH_SNAPSHOT.md) "
- " [DBA\_HIST\_SNAPSHOT](DBA_HIST_SNAPSHOT.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS003) for more information about the `DBMS_APPLICATION_INFO` package