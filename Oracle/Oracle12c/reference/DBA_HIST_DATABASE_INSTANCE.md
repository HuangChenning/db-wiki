---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_HIST_DATABASE_INSTANCE.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_HIST_DATABASE_INSTANCE` displays the databases and instances in the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number |
| `STARTUP_TIME` | `TIMESTAMP(3)` | `NOT NULL` | Startup time of the instance |
| `PARALLEL` | `VARCHAR2(3)` | `NOT NULL` | Indicates whether the instance is running in an Oracle Real Application Clusters (Oracle RAC) environment (`YES`) or not (`NO`) |
| `VERSION` | `VARCHAR2(17)` | `NOT NULL` | Database version |
| `DB_NAME` | `VARCHAR2(9)` |  | Name of the database |
| `INSTANCE_NAME` | `VARCHAR2(16)` |  | Name of the instance |
| `HOST_NAME` | `VARCHAR2(64)` |  | Name of the host |
| `LAST_ASH_SAMPLE_ID` | `NUMBER` | `NOT NULL` | Last sample ID for the active session history |
| `PLATFORM_NAME` | `VARCHAR2(101)` |  | Platform on which the instance is running |
| `CDB` | `VARCHAR2(3)` |  | Possible values are:  - `YES` if the database is a CDB - `NO` if the database is not a CDB  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `EDITION` | `VARCHAR2(7)` |  | The edition of the database.  Possible values include:  - `CORE EE`: CORE Enterprise Edition - `EE`: Enterprise Edition - `PO`: Personal Edition - `XE`: Express Edition  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `DB_UNIQUE_NAME` | `VARCHAR2(30)` |  | Unique database name  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `DATABASE_ROLE` | `VARCHAR2(16)` |  | Current role of the database:  - `SNAPSHOT STANDBY` - ``` 	LOGICAL STANDBY 	``` - `PHYSICAL STANDBY` - `PRIMARY` - `FAR SYNC`  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `CDB_ROOT_DBID` | `NUMBER` |  | The database ID of the CDB root for the sampled session  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [DB\_UNIQUE\_NAME](DB_UNIQUE_NAME.md) "