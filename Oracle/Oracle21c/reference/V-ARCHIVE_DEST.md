---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ARCHIVE_DEST.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.37 V$ARCHIVE\_DEST

`V$ARCHIVE_DEST` displays, for the current instance, all of the destinations in the Data Guard configuration, including each destination's current value, mode, and status.

| Column | Datatype | Description |
| --- | --- | --- |
| `DEST_ID` | `NUMBER` | Log archive destination parameter identifier (`1` to `31`) |
| `DEST_NAME` | `VARCHAR2(256)` | Log archive destination parameter name |
| `STATUS` | `VARCHAR2(9)` | Identifies the current status of the destination:  - `VALID` - Initialized and available - `INACTIVE` - No destination information - `DEFERRED` - Manually disabled by the user - `ERROR` - Error during open or copy - `DISABLED` - Disabled after error - `BAD PARAM` - Parameter has errors - `ALTERNATE` - Destination is available as an alternate - `FULL` - Exceeded quota size for the destination |
| `BINDING` | `VARCHAR2(9)` | Specifies how failure will affect the archival operation:  - `MANDATORY` - Successful archival is required - `OPTIONAL` - Successful archival is not required (depends on `LOG_ARCHIVE_MIN_SUCCEED_DEST`) |
| `NAME_SPACE` | `VARCHAR2(7)` | Identifies the scope of parameter setting:  - `SYSTEM` - System definition - `SESSION` - Session definition |
| `TARGET` | `VARCHAR2(7)` | For a primary database, this column specifies whether the archive destination is local or remote to the primary database:  - `PRIMARY` - local - `STANDBY` - remote  For a standby database, this column specifies whether the archive destination is local or remote to the standby database:  - `LOCAL` - local - `REMOTE` - remote |
| `ARCHIVER` | `VARCHAR2(10)` | Identifies the archiver process relative to the database where the query is issued:  - `ARC` `n` - `FOREGROUND` - `LGWR` - `RFS` |
| `SCHEDULE` | `VARCHAR2(8)` | Indicates whether the archival of this destination is `INACTIVE`, `PENDING`, `ACTIVE`, or `LATENT` |
| `DESTINATION` | `VARCHAR2(256)` | Specifies the location where the archived redo logs are to be archived |
| `LOG_SEQUENCE` | `NUMBER` | Identifies the sequence number of the last archived redo log to be archived |
| `REOPEN_SECS` | `NUMBER` | Identifies the retry time (in seconds) after error |
| `DELAY_MINS` | `NUMBER` | Identifies the delay interval (in minutes) before the archived redo log is automatically applied to a standby database |
| `NET_TIMEOUT` | `NUMBER` | Number of seconds the log writer process will wait for status from the network server of a network operation issued by the log writer process |
| `PROCESS` | `VARCHAR2(10)` | Identifies the archiver process relative to the primary database, even if the query is issued on the standby database:  - `ARC` `n` - `FOREGROUND` - `LGWR` |
| `REGISTER` | `VARCHAR2(3)` | Indicates whether the archived redo log is registered in the remote destination control file (`YES`) or not (`NO`). If the archived redo log is registered, it is available to log apply services. |
| `FAIL_DATE` | `DATE` | Date and time of last error |
| `FAIL_SEQUENCE` | `NUMBER` | Sequence number of the archived redo log being archived when the last error occurred |
| `FAIL_BLOCK` | `NUMBER` | Block number of the archived redo log being archived when the last error occurred |
| `FAILURE_COUNT` | `NUMBER` | Current number of contiguous archival operation failures that have occurred for the destination |
| `MAX_FAILURE` | `NUMBER` | Allows you to control the number of times log transport services will attempt to reestablish communication and resume archival operations with a failed destination |
| `ERROR` | `VARCHAR2(256)` | Displays the error text |
| `ALTERNATE` | `VARCHAR2(256)` | Alternate destination, if any |
| `DEPENDENCY` | `VARCHAR2(256)` | Reserved for future use |
| `REMOTE_TEMPLATE` | `VARCHAR2(256)` | Specifies the template to be used to derive the location to be recorded |
| `QUOTA_SIZE` | `NUMBER` | Destination quotas, expressed in bytes |
| `QUOTA_USED` | `NUMBER` | Size of all the archived redo logs currently residing on the specified destination |
| `MOUNTID` | `NUMBER` | Instance mount identifier |
| `TRANSMIT_MODE` | `VARCHAR2(12)` | Specifies network transmission mode:  - `SYNCHRONOUS` - `PARALLELSYNC` - `ASYNCHRONOUS` |
| `ASYNC_BLOCKS` | `NUMBER` | Number of blocks specified for the `ASYNC` attribute |
| `AFFIRM` | `VARCHAR2(3)` | Specifies disk I/O mode |
| `TYPE` | `VARCHAR2(7)` | Indicates whether the archived log destination definition is `PUBLIC` or `PRIVATE`. Only `PUBLIC` destinations can be modified at run time using the `ALTER SYSTEM SET` or `ALTER SESSION SET` statements. By default, all archived log destinations are `PUBLIC`. |
| `VALID_NOW` | `VARCHAR2(16)` | Indicates whether the destination is valid right now for archival operations:  - `YES` - Redo log type and database role for this destination are valid for the current database - `WRONG VALID_TYPE` - Redo log type specified for this destination is not valid for the current database role. For example, `WRONG VALID_TYPE` would be returned if a destination specified with the `VALID_FOR=(STANDBY_LOGFILE,STANDBY_ROLE)` attribute is running in the standby database role but does not have standby redo logs implemented. - `WRONG VALID_ROLE` - Database role specified for this destination is not the role in which the database is currently running. For example, the WRONG `VALID_ROLE` would be returned when a destination defined with the `VALID_FOR=(ONLINE_LOGFILE,STANDBY_ROLE)` attribute is running in the primary database role. - `INACTIVE` - Destination is inactive, probably due to an error |
| `VALID_TYPE` | `VARCHAR2(15)` | Redo log type or types that are valid for the destination:  - `ONLINE_LOGFILE` - `STANDBY_LOGFILE` - `ALL_LOGFILES` |
| `VALID_ROLE` | `VARCHAR2(12)` | Database role or roles that are valid for the destination:  - `PRIMARY_ROLE` - `STANDBY_ROLE` - `ALL_ROLES` |
| `DB_UNIQUE_NAME` | `VARCHAR2(30)` | Unique database name |
| `VERIFY` | `VARCHAR2(3)` | Indicates whether the value of the `VERIFY` attribute on the `LOG_ARCHIVE_DEST_` `n` parameter is verified (`YES`) or not verified (`NO`) |
| `COMPRESSION` | `VARCHAR2(7)` | Indicates whether network compression is `ENABLED` or `DISABLED`, or whether the `ZLIB` or `LZO` algorithm is in use. These values correspond to the values accepted by the `COMPRESSION` attribute for the database initialization parameter `LOG_ARCHIVE_DEST_n`. The possible values include: - `DISABLE`: Compression is disabled. - `ENABLE`: Compression is enabled. The `ZLIB` compression algorithm is used. - `ZLIB`: `ZLIB` compression is used. - `LZO`: `LZO` compression is used. |
| `APPLIED_SCN` | `NUMBER` | For a destination that corresponds to a physical or logical standby database, the SCN of the last applied redo. For a destination that corresponds to a snapshot standby database, the SCN of the last redo applied before conversion to a snapshot standby database. This column is only valid for enabled and active standby database destinations on a primary or cascading standby database. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `ENCRYPTION` | `VARCHAR2(7)` | Indicates whether encryption of the redo stream sent to Zero Data Loss Recovery Appliance (Recovery Appliance) is enabled (`ENABLED`) or not (`DISABLED`) |