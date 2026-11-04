---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-INSTANCE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.8 V$INSTANCE

`V$INSTANCE` displays the state of the current instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `INSTANCE_NUMBER` | `NUMBER` | Instance number used for instance registration (corresponds to the `INSTANCE_NUMBER` initialization parameter)  See Also: " [INSTANCE\_NUMBER](INSTANCE_NUMBER.md) " |
| `INSTANCE_NAME` | `VARCHAR2(16)` | Name of the instance |
| `HOST_NAME` | `VARCHAR2(64)` | Name of the host machine |
| `VERSION` | `VARCHAR2(17)` | Database version |
| `VERSION_LEGACY` | `VARCHAR2(17)` | The legacy database version used before Oracle Database 18c. This column displays the same value as the `VERSION` column |
| `VERSION_FULL` | `VARCHAR2(17)` | The version string with the new Oracle Database version scheme introduced in Oracle Database 18c. |
| `STARTUP_TIME` | `DATE` | Time when the instance was started |
| `STATUS` | `VARCHAR2(12)` | Status of the instance:  - `STARTED` - After `STARTUP NOMOUNT` - `MOUNTED` - After `STARTUP MOUNT` or `ALTER DATABASE CLOSE` - `OPEN` - After `STARTUP` or `ALTER DATABASE OPEN` - `OPEN MIGRATE` - After `ALTER DATABASE OPEN { UPGRADE \| DOWNGRADE }` |
| `PARALLEL` | `VARCHAR2(3)` | Indicates whether the instance is mounted in cluster database mode (`YES`) or not (`NO`) |
| `THREAD#` | `NUMBER` | Redo thread opened by the instance |
| `ARCHIVER` | `VARCHAR2(7)` | Automatic archiving status:  - `STOPPED` - `STARTED` - `FAILED` - Archiver failed to archive a log last time but will try again within 5 minutes |
| `LOG_SWITCH_WAIT` | `VARCHAR2(15)` | Event that log switching is waiting for:  - `ARCHIVE LOG` - `CLEAR LOG` - `CHECKPOINT` - NULL - `ALTER SYSTEM SWITCH LOGFILE` is hung but there is room in the current online redo log |
| `LOGINS` | `VARCHAR2(10)` | Indicates whether the instance is in unrestricted mode, allowing logins by all users (`ALLOWED`, or in restricted mode, allowing logins by database administrators only (`RESTRICTED`) |
| `SHUTDOWN_PENDING` | `VARCHAR2(3)` | Indicates whether a shutdown is pending (`YES`) or not (`NO`) |
| `DATABASE_STATUS` | `VARCHAR2(17)` | Status of the database:  - `ACTIVE` - `SUSPENDED` - `INSTANCE RECOVERY` |
| `INSTANCE_ROLE` | `VARCHAR2(18)` | Indicates whether the instance is an active instance (`PRIMARY_INSTANCE`) or an inactive secondary instance (`SECONDARY_INSTANCE`), or `UNKNOWN` if the instance has been started but not mounted |
| `ACTIVE_STATE` | `VARCHAR2(9)` | Quiesce state of the instance:  - `NORMAL` - Database is in a normal state. - `QUIESCING` - `ALTER SYSTEM QUIESCE RESTRICTED` has been issued: no new user transactions, queries, or PL/SQL statements are processed in this instance. User transactions, queries, or PL/SQL statements issued before the `ALTER SYSTEM QUIESCE RESTRICTED` statement are unaffected. DBA transactions, queries, or PL/SQL statements are also unaffected. - `QUIESCED` - `ALTER SYSTEM QUIESCE RESTRICTED` has been issued: no user transactions, queries, or PL/SQL statements are processed. DBA transactions, queries, or PL/SQL statements are unaffected. User transactions, queries, or PL/ SQL statements issued after the `ALTER SYSTEM QUIESCE RESTRICTED` statement are not processed.  A single `ALTER SYSTEM QUIESCE RESTRICTED` statement quiesces all instances in an Oracle RAC environment. After this statement has been issued, some instances may enter into a quiesced state before other instances; the system is quiesced when all instances enter the quiesced state. |
| `BLOCKED` | `VARCHAR2(3)` | Indicates whether all services are blocked (`YES`) or not (`NO`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `INSTANCE_MODE` | `VARCHAR2(11)` | The instance mode of the current instance:  - `REGULAR`: A regular Oracle RAC instance. This value is also always used for any non-Oracle RAC instance. - `READ MOSTLY`: An Oracle RAC instance that performs very few database writes - `READ ONLY`: A read-only Oracle RAC instance |
| `EDITION` | `VARCHAR2(7)` | The edition of the database:  - `PO`: Personal Edition - `XE`: Express Edition - `SE2`: Standard Edition or Standard Edition 2 - `EE`: Enterprise Edition - `HP`: Enterprise Edition - High Performance - `XP`: Enterprise Edition - Extreme Performance |
| `FAMILY` | `VARCHAR2(80)` | For internal use only. |
| `DATABASE_TYPE` | `VARCHAR2(15)` | Database type:  - `RAC`: If the database is a regular Oracle RAC database which may have multiple instances. - `RACONENODE`: If the database is Oracle RAC, but allows only one instance to run at any time - the RAC One Node mode. - `SINGLE`: If the database is running as a single instance. - `UNKNOWN`: If the database's type can't be determined. This might happen when the database is registered as a DB resource with CRS but the CRS service has failed to return valid database type information. Typically, this indicates that either the CRS service is down or it is in a faulty state. |