---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-ASM_ACFSREPL.html
tags:
  - oracle
  - 12c
  - reference
---

`V$ASM_ACFSREPL` displays information for Oracle ACFS file systems that are initialized for replication.

| Column | Datatype | Description |
| --- | --- | --- |
| `FSNAME` | `VARCHAR2(1024)` | File system mount point (foreign key to `V$ASM_FILESYSTEM`) |
| `VOLDEV` | `VARCHAR2(256)` | Name of the Oracle ADVM device |
| `SITE` | `VARCHAR2(7)` | Replication site role:  - `PRIMARY` - File system is initialized as a primary - `STANDBY` - File system is initialized as a standby |
| `LAG` | `VARCHAR2(128)` | Amount of time standby is behind primary in hours:minutes:seconds (primary only) |
| `STATUS` | `VARCHAR2(12)` | Replication primary or standby status:  - `ONLINE` - Replication is initialized and processing real-time changes - `INITIALIZING` - Replication is still processing files on the primary that existed before replication started - `PAUSED` - The primary is not sending logs to the standby or the standby is not applying logged changes |
| `INITSTATUS` | `VARCHAR2(11)` | Replication primary or standby initialization status:  - `NONE` - Replication is `ONLINE` and not initializing - `DIRECTORIES` - Directories are being initialized - `FILES` - Files are being initialized |
| `DIRSSCAN` | `NUMBER` | Number of directories scanned and logged (primary only) |
| `PERCENT` | `NUMBER` | Percentage of files initialized that existed before replication started (primary only) |
| `LASTSYNC` | `DATE` | Time of last apply on the standby site (standby only) |
| `CRSRUN` | `NUMBER` | Number of Cluster Ready Services replication daemons currently running |
| `CRSTOTAL` | `NUMBER` | Number of Cluster Ready Services replication daemons expected to be running |
| `PMNTPT` | `VARCHAR2(1024)` | Replication primary site mount point |
| `SMNTPT` | `VARCHAR2(1024)` | Replication standby site mount point |
| `PSVCNAME` | `VARCHAR2(1024)` | Replication primary site service name |
| `SSVCNAME` | `VARCHAR2(1024)` | Replication standby site service name |
| `PHOST` | `VARCHAR2(1024)` | A replication primary cluster host name |
| `SHOST` | `VARCHAR2(1024)` | A replication standby cluster host name |
| `REMALIAS` | `VARCHAR2(4096)` | Replication remote alias name |
| `TAGS` | `NUMBER` | `TRUE` (`1`) if replicating tagged files |
| `COMPRESSION` | `VARCHAR2(3)` | Replication log compression status:  - `OFF` - Replication logs are not being compressed - `ON` - Replication logs are being compressed |
| `DBGLVL` | `NUMBER` | Replication trace log debug level |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

Note:

This view only contains records for Oracle ASM releases prior to Oracle Database 12c Release 2 (12.2.0.1). To display Oracle ACFS replication information for Oracle Database 12c Release 2 (12.2.0.1) or higher, use the `acfsutil repl info` command.

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=OSTMG30000) for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS)
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=OSTMG95490) for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information

Note:

To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=OSTMG-GUID-DE759521-9CF3-45D9-9123-7159C9ED4D30).