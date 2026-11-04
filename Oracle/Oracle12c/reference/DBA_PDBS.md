---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_PDBS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_PDBS` describes PDBs belonging to a given CDB.

When queried from a CDB root, this view describes all PDBs that belong to the CDB. When queried from an application root, it describes all PDBs that belong to the application container. When queried from a regular PDB or from an application PDB, it describes the regular PDB or the application PDB.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PDB_ID` | `NUMBER` | `NOT NULL` | Container ID of the PDB |
| `PDB_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the PDB |
| `DBID` | `NUMBER` | `NOT NULL` | PDB identifier calculated when the PDB is created and stored in all file headers associated with the PDB |
| `CON_UID` | `NUMBER` | `NOT NULL` | Unique identifier associated with the container |
| `GUID` | `RAW(16)` |  | Globally unique immutable ID assigned to the PDB at creation time |
| `STATUS` | `VARCHAR2(10)` |  | State of the PDB. Possible values:  - `NEW` - The PDB has never been opened since it was created. It must be opened in `READ WRITE` mode for Oracle to perform processing needed to complete the integration of the PDB into the CDB and mark it `NORMAL`. An error will be thrown if an attempt is made to open the PDB read only. - `NORMAL` - The PDB is ready to be used. - `UNPLUGGED` - The PDB has been unplugged. The only operation that can be performed on it is `DROP PLUGGABLE DATABASE`. - `RELOCATING`: The PDB is in the process of being relocated to a different CDB. - `RELOCATED`: The PDB has been relocated to a different CDB. - `REFRESHING`: The PDB is a refresh PDB. - `UNDEFINED`: The PDB is in an undefined state. - `UNUSABLE` - The PDB is being created or an unrecoverable error was encountered during its creation. The PDB cannot be opened while its state is set to `UNUSABLE`. If the PDB remains in this state because of an error encountered during its creation, it can only be dropped. The alert log can be checked to determine if there was an error during PDB creation. |
| `CREATION_SCN` | `NUMBER` |  | Creation SCN |
| `VSN` | `NUMBER` |  | The version number of the PDB |
| `LOGGING` | `VARCHAR2(9)` |  | Shows the current logging mode for the PDB. Possible values:  - `LOGGING` - `NOLOGGING` |
| `FORCE_LOGGING` | `VARCHAR2(3)` |  | Specifies whether force logging is turned on for the PDB. Possible values:  - `NO` - `YES` |
| `FORCE_NOLOGGING` | `VARCHAR2(3)` |  | Specifies whether force nologging is turned on for the PDB. Possible values:  - `NO` - `YES` |
| `APPLICATION_ROOT` | `VARCHAR2(3)` |  | Indicates whether the PDB is an application root.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `APPLICATION_PDB` | `VARCHAR2(3)` |  | Indicates whether a PDB is an application PDB  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `APPLICATION_SEED` | `VARCHAR2(3)` |  | Indicates whether a PDB is an application seed (an application seed is also an application PDB)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `APPLICATION_ROOT_CON_ID` | `NUMBER` |  | If this PDB is an application PDB, the container ID of an application root to which this application PDB belongs.  If this PDB is an application root clone, the container ID of an application root to which this application root clone belongs.  Otherwise, NULL.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `IS_PROXY_PDB` | `VARCHAR2(3)` |  | Indicates whether this PDB is a proxy PDB  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `CON_ID` | `NUMBER` | `NOT NULL` | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `UPGRADE_PRIORITY` | `NUMBER` |  | The upgrade priority of the PDB.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `APPLICATION_CLONE` | `VARCHAR2(3)` |  | Indicates whether this PDB is an application root clone (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `FOREIGN_CDB_DBID` | `NUMBER ` |  | The foreign CDB’s DBID  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `UNPLUG_SCN` | `NUMBER` |  | SCN at which the PDB was unplugged  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `FOREIGN_PDB_ID` | `NUMBER` |  | The foreign PDB ID  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `CREATION_TIME` | `DATE` | `NOT NULL` | PDB creation timestamp  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `REFRESH_MODE` | `VARCHAR2(6)` |  | PDB refresh mode. Possible values:  - `MANUAL` - `AUTO`  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `REFRESH_INTERVAL` | `NUMBER` |  | PDB refresh interval. This is applicable only when `REFRESH_MODE` is `AUTO`.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |