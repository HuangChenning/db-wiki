---
title: "V$ARCHIVE_DEST_STATUS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1013.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ARCHIVE_DEST_STATUS` displays runtime and configuration information for the archived redo log destinations. The information in this view does not persist across an instance shutdown.

| Column | Datatype | Description |
| --- | --- | --- |
| `DEST_ID` | `NUMBER` | Identifies the log archive destination parameter (1 to 31) |
| `DEST_NAME` | `VARCHAR2(256)` | Log archive destination parameter name |
| `STATUS` | `VARCHAR2(9)` | Current status of the destination: - `VALID` - Initialized and available - `INACTIVE` - No destination information - `DEFERRED` - Manually disabled by the user - `ERROR` - Error during open or copy - `DISABLED` - Disabled after error - `BAD PARAM` - Parameter has errors - `ALTERNATE` - Destination is in an alternate state - `FULL` - Exceeded quota size for the destination |
| `TYPE` | `VARCHAR2(14)` | Type of archival destination database: - `LOCAL` - Local to primary database - `PHYSICAL` - Physical standby - `CROSS-INSTANCE` - An instance of the primary - `LOGICAL` - Logical standby - `SNAPSHOT` - Snapshot standby database - `DOWNSTREAM` - Streams downstream capture database |
| `DATABASE_MODE` | `VARCHAR2(15)` | Current mode of the archival destination database: - `STARTED` - Instance started, not mounted - `MOUNTED` - Mounted - `MOUNTED-STANDBY` - Mounted standby - `OPEN` - Open read/write - `OPEN_READ-ONLY` - Open read-only |
| `RECOVERY_MODE` | `VARCHAR2(23)` | Current apply mode at the archival destination: - `IDLE` - Managed recovery is not active - `MANAGED` - Managed recovery is active - `MANAGED REAL TIME APPLY` - Log apply services recover redo data from standby redo logs at the same time the logs are being written to, as opposed to recovering redo from archived redo logs when a log switch occurs - `LOGICAL REAL TIME APPLY` - Real time SQL Apply - `LOGICAL APPLY` - SQL Apply |
| `PROTECTION_MODE` | `VARCHAR2(20)` | Indicates whether the database is protected: - `MAXIMUM PROTECTION` - `MAXIMUM AVAILABILITY` - `RESYNCHRONIZATION` - `MAXIMUM PERFORMANCE` - `UNPROTECTED` |
| `DESTINATION` | `VARCHAR2(256)` | Specifies the location where the redo data is to be archived |
| `STANDBY_LOGFILE_COUNT` | `NUMBER` | Indicates the total number of standby redo logs created on the standby database |
| `STANDBY_LOGFILE_ACTIVE` | `NUMBER` | Indicates the total number of standby redo logs on the standby database that are active and contain primary database online redo log information |
| `ARCHIVED_THREAD#` | `NUMBER` | Identifies the thread number of the most recent archived redo log received at the destination |
| `ARCHIVED_SEQ#` | `NUMBER` | Identifies the log sequence number of the most recent archived redo log received at the destination |
| `APPLIED_THREAD#` | `NUMBER` | Identifies the thread number of the most recent applied redo log received at the destination |
| `APPLIED_SEQ#` | `NUMBER` | Identifies the log sequence number of the most recent applied redo log received at the destination |
| `ERROR` | `VARCHAR2(256)` | Displays the error text |
| `SRL` | `VARCHAR2(3)` | Indicates whether standby redo logfiles are used on the standby database (`YES`) or not (`NO`) |
| `DB_UNIQUE_NAME` | `VARCHAR2(30)` | Specifies the unique database name of the current instance that was defined with the `DB_UNIQUE_NAME` attribute on the `LOG_ARCHIVE_DEST_` `n` parameter |
| `SYNCHRONIZATION_STATUS` | `VARCHAR2(22)` | Possible values for this column are as follows: - `CHECK CONFIGURATION` - Synchronization with this destination is not possible because this database is either not in `MAXIMUM` `PROTECTION` or `MAXIMUM` `PERFORMANCE` data protection mode, or the `LOG_ARCHIVE_DEST_` `n` parameter associated with this destination has not been configured with the `SYNC` and `AFFIRM` attributes. - `CHECK STANDBY REDO LOG` - The standby redo log at this destination is configured improperly. - `CHECK NETWORK` - One or more instances of this database cannot send redo data to this destination. - `DESTINATION HAS A GAP` - This destination is missing redo data needed for synchronization with this database. - `OK` - This destination is synchronized with this database. - `NOT AVAILABLE` - Synchronization status is not available.  See Also: [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/log_transport.htm#SBYDB00400) for more information about redo transport configuration |
| `SYNCHRONIZED` | `VARCHAR2(3)` | Possible values are: - `YES` - This destination is synchronized with the primary database. - `NO` - The destination is not synchronized with the primary database. - `UNKNOWN` - The synchronization status of this destination cannot be determined. |
| `GAP_STATUS` | `VARCHAR2(24)` | Redo gap status: - `NO GAP` - Destination does not have a redo gap. - `LOG SWITCH GAP` - Destination has not yet received all of the redo from the previous log file. - `RESOLVABLE GAP` - Destination has a redo gap that can be automatically resolved by fetching the missing redo from this database. - `UNRESOLVABLE GAP` - Destination has a redo gap that cannot be automatically resolved by fetching the missing redo from this database and there are no other destinations from which redo can be fetched. - `LOCALLY UNRESOLVABLE GAP` - Destination has a redo gap that cannot be automatically resolved by fetching the missing redo from this database. It may be possible to resolve the gap by fetching the missing redo from another destination. |