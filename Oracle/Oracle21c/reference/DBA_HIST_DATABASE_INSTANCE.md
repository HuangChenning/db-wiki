---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_DATABASE_INSTANCE.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.395 DBA\_HIST\_DATABASE\_INSTANCE

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
| `CDB` | `VARCHAR2(3)` |  | Possible values are:  - `YES` if the database is a CDB - `NO` if the database is not a CDB |
| `EDITION` | `VARCHAR2(7)` |  | The edition of the database:  - `PO`: Personal Edition - `XE`: Express Edition - `SE2`: Standard Edition or Standard Edition 2 - `EE`: Enterprise Edition - `HP`: Enterprise Edition - High Performance - `XP`: Enterprise Edition - Extreme Performance |
| `DB_UNIQUE_NAME` | `VARCHAR2(30)` |  | Unique database name |
| `DATABASE_ROLE` | `VARCHAR2(16)` |  | Current role of the database:  - `SNAPSHOT` `STANDBY` - `LOGICAL` `STANDBY` - `PHYSICAL` `STANDBY` - `PRIMARY` - `FAR SYNC` |
| `CDB_ROOT_DBID` | `NUMBER` |  | The database ID of the CDB root for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `STARTUP_TIME_TZ` | `TIMESTAMP(3) WITH TIME ZONE` |  | Startup time of the instance |

See Also:

" [DB\_UNIQUE\_NAME](DB_UNIQUE_NAME.md) "