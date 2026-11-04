---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ARCHIVE_DEST_STATUS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.38 V$ARCHIVE\_DEST\_STATUS

`V$ARCHIVE_DEST_STATUS` displays run time and configuration information for the archived redo log destinations.

The information in this view does not persist across an instance shutdown.

| Column | Datatype | Description |
| --- | --- | --- |
| `DEST_ID` | `NUMBER` | Identifies the log archive destination parameter (1 to 31) |
| `DEST_NAME` | `VARCHAR2(256)` | Log archive destination parameter name |
| `STATUS` | `VARCHAR2(9)` | Current status of the destination:  - `ALTERNATE` - Destination is in an alternate state - `BAD` `PARAM` - Parameter has errors - `DEFERRED` - Manually disabled by the user - `DISABLED` - Disabled after error - `ERROR` - Error during open or copy - `FULL` - Exceeded quota size for the destination - `IDLE` - Destination is idle - `INACTIVE` - No destination information - `VALID` - Initialized and available |
| `TYPE` | `VARCHAR2(16)` | Type of archival destination database:  - `BACKUP` `APPLIANCE` - Backup appliance - `CROSS-INSTANCE` - An instance of the primary - `DOWNSTREAM` - Streams downstream capture database - `FAR` `SYNC` - Far Sync Instance - `LOCAL` - Local to primary database - `LOGICAL` - Logical standby - `PHYSICAL` - Physical standby - `SNAPSHOT` - Snapshot standby database |
| `DATABASE_MODE` | `VARCHAR2(15)` | Current mode of the archival destination database:  - `STARTED` - Instance started, not mounted - `MOUNTED` - Mounted - `MOUNTED-STANDBY` - Mounted standby - `OPEN` - Open read/write - `OPEN_READ-ONLY` - Open read-only |
| `RECOVERY_MODE` | `VARCHAR2(34)` | Current apply mode at the archival destination:  - `IDLE` - Managed recovery is not active - `LOGICAL` `APPLY` - SQL Apply - `LOGICAL` `REAL` `TIME` `APPLY` - Real time SQL Apply - `MANAGED` - Managed recovery is active. This value is used when the standby database is mounted. In this recovery mode, users cannot query data on the standby. - `MANAGED` `REAL` `TIME` `APPLY` - In this recovery mode, log apply services recover redo data from standby redo logs at the same time the logs are being written to, as opposed to recovering redo from archived redo logs when a log switch occurs. In this recovery mode, users cannot query data on the standby. - `MANAGED` `REAL` `TIME` `APPLY` `WITH` `QUERY` - In this recovery mode, log apply services recover redo data from standby redo logs at the same time the logs are being written to, as opposed to recovering redo from archived redo logs when a log switch occurs. In a non-CDB, this mode is used when the database is open, and users can query data on the standby. In a CDB, this value is used when one or more PDBs in the CDB are open, and users can query data on the standby. - `MANAGED` `WITH` `QUERY` - Managed recovery is active in this recovery mode. In a non-CDB, this value is used when the database is open, and users can query data on the standby. In a CDB, this value is used when one or more PDBs in the CDB are open, and users can query data on the standby. |
| `PROTECTION_MODE` | `VARCHAR2(20)` | Indicates how the database is protected:  - `MAXIMUM` `AVAILABILITY` - `MAXIMUM` `PERFORMANCE` - `MAXIMUM` `PROTECTION` - `RESYNCHRONIZATION` |
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
| `SYNCHRONIZATION_STATUS` | `VARCHAR2(22)` | Possible values for this column are as follows:  - `CHECK` `CONFIGURATION` - Synchronization with this destination is not possible because this database is either not in `MAXIMUM` `PROTECTION` or `MAXIMUM` `AVAILABILITY` data protection mode, or the `LOG_ARCHIVE_DEST_` `n` parameter associated with this destination has not been configured with the `SYNC` and `AFFIRM` attributes. - `CHECK` `CONNECTIVITY` - One or more instances of this database cannot send redo data to this destination. - `CHECK` `STANDBY` `REDO` `LOG` - The standby redo log at this destination is configured improperly. - `DESTINATION` `HAS` `A` `GAP` - This destination is missing redo data needed for synchronization with this database. - `OK` - This destination is synchronized with this database. - `STATUS` `NOT` `AVAILABLE` - Synchronization status is not available.  See Also: [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB00400) for more information about redo transport configuration |
| `SYNCHRONIZED` | `VARCHAR2(3)` | Possible values are:  - `YES` - This destination is synchronized with the primary database. - `NO` - The destination is not synchronized with the primary database. - `UNKNOWN` - The synchronization status of this destination cannot be determined. |
| `GAP_STATUS` | `VARCHAR2(24)` | Redo gap status:  - `LOCALLY` `UNRESOLVABLE` `GAP` - Destination has a redo gap that cannot be automatically resolved by fetching the missing redo from this database. It may be possible to resolve the gap by fetching the missing redo from another destination. - `LOG` `SWITCH` `GAP` - Destination has not yet received all of the redo from the previous log file. - `NO` `GAP` - Destination does not have a redo gap. - `RESOLVABLE` `GAP` - Destination has a redo gap that can be automatically resolved by fetching the missing redo from this database. - `UNRESOLVABLE` `GAP` - Destination has a redo gap that cannot be automatically resolved by fetching the missing redo from this database and there are no other destinations from which redo can be fetched. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |