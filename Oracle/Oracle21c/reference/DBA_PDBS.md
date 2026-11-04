---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_PDBS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.240 DBA\_PDBS

`DBA_PDBS` describes PDBs belonging to a given CDB.

When queried from a CDB root, this view describes all PDBs that belong to the CDB. When queried from an application root, it describes all PDBs that belong to the application container. When queried from a regular PDB or from an application PDB, it describes the regular PDB or the application PDB.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PDB_ID` | `NUMBER` | `NOT NULL` | Container ID of the PDB |
| `PDB_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the PDB |
| `DBID` | `NUMBER` | `NOT NULL` | PDB identifier calculated when the PDB is created and stored in all file headers associated with the PDB |
| `CON_UID` | `NUMBER` | `NOT NULL` | Unique identifier associated with the container |
| `GUID` | `RAW(16)` |  | Globally unique immutable ID assigned to the PDB at creation time |
| `STATUS` | `VARCHAR2(10)` |  | State of the PDB. Possible values:  - `NEW` - The PDB has never been opened since it was created. It must be opened in `READ WRITE` mode for Oracle to perform processing needed to complete the integration of the PDB into the CDB and mark it `NORMAL`. An error will be thrown if an attempt is made to open the PDB read only. - `NORMAL` - The PDB is ready to be used. - `UNPLUGGED` - The PDB has been unplugged. The only operation that can be performed on it is `DROP PLUGGABLE DATABASE`. - `RELOCATING`: The PDB is in the process of being relocated to a different CDB. - `RELOCATED`: The PDB has been relocated to a different CDB. - `REFRESHING`: The PDB is a refresh PDB. - `STANDBY`: The PDB is a Data Guard standby PDB. - `UNDEFINED`: The PDB is in an undefined state. - `UNUSABLE` - The PDB is being created or an unrecoverable error was encountered during its creation. The PDB cannot be opened while its state is set to `UNUSABLE`. If the PDB remains in this state because of an error encountered during its creation, it can only be dropped. The alert log can be checked to determine if there was an error during PDB creation. |
| `CREATION_SCN` | `NUMBER` |  | Creation SCN |
| `VSN` | `NUMBER` |  | The version number of the PDB |
| `LOGGING` | `VARCHAR2(9)` |  | Shows the current logging mode for the PDB. Possible values:  - `LOGGING` - `NOLOGGING` |
| `FORCE_LOGGING` | `VARCHAR2(3)` |  | Specifies whether force logging is turned on for the PDB. Possible values:  - `NO` - `YES` |
| `FORCE_NOLOGGING` | `VARCHAR2(3)` |  | Specifies whether force nologging is turned on for the PDB. Possible values:  - `NO` - `YES` |
| `APPLICATION_ROOT` | `VARCHAR2(3)` |  | Indicates whether the PDB is an application root. |
| `APPLICATION_PDB` | `VARCHAR2(3)` |  | Indicates whether a PDB is an application PDB |
| `APPLICATION_SEED` | `VARCHAR2(3)` |  | Indicates whether a PDB is an application seed (an application seed is also an application PDB) |
| `APPLICATION_ROOT_CON_ID` | `NUMBER` |  | If this PDB is an application PDB, the container ID of an application root to which this application PDB belongs.  If this PDB is an application root clone, the container ID of an application root to which this application root clone belongs.  Otherwise, NULL. |
| `IS_PROXY_PDB` | `VARCHAR2(3)` |  | Indicates whether this PDB is a proxy PDB |
| `CON_ID` | `NUMBER` | `NOT NULL` | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `UPGRADE_PRIORITY` | `NUMBER` |  | The upgrade priority of the PDB. |
| `APPLICATION_CLONE` | `VARCHAR2(3)` |  | Indicates whether this PDB is an application root clone (`YES`) or not (`NO`) |
| `FOREIGN_CDB_DBID` | `NUMBER ` |  | The foreign CDB’s DBID |
| `UNPLUG_SCN` | `NUMBER` |  | SCN at which the PDB was unplugged |
| `FOREIGN_PDB_ID` | `NUMBER` |  | The foreign PDB ID |
| `CREATION_TIME` | `DATE` | `NOT NULL` | PDB creation timestamp |
| `REFRESH_MODE` | `VARCHAR2(6)` |  | PDB refresh mode. Possible values:  - `MANUAL` - `AUTO` |
| `REFRESH_INTERVAL` | `NUMBER` |  | PDB refresh interval. This is applicable only when `REFRESH_MODE` is `AUTO`. |
| `TEMPLATE` | `VARCHAR2(3)` |  | For internal use only |
| `LAST_REFRESH_SCN` | `NUMBER` |  | System change number (SCN) of the last refresh operation |
| `TENANT_ID` | `VARCHAR2(255)` |  | Pluggable database tenant key |
| `SNAPSHOT_MODE` | `VARCHAR2(6)` |  | Pluggable database snapshot mode |
| `SNAPSHOT_INTERVAL` | `NUMBER` |  | Pluggable database snapshot interval, in minutes |
| `CREDENTIAL_NAME` | `VARCHAR2(262)` |  | Credential object name associated with the PDB |
| `LAST_REFRESH_TIME` <sup>Foot 1</sup> | `DATE` |  | Time of the last refresh operation |
| `CLOUD_IDENTITY` <sup>Foot 1</sup> | `VARCHAR2(4000)` |  | Cloud identifier for the PDB |
| `SOURCE_PDB_NAME` <sup>Foot 1</sup> | `VARCHAR2(128)` |  | Name of the source PDB |
| `SOURCE_DB_LINK` <sup>Foot 1</sup> | `VARCHAR2(128)` |  | Name of the source database link |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.