---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PDBS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.114 V$PDBS

`V$PDBS` displays information about PDBs associated with the current instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `DBID` | `NUMBER` | PDB identifier calculated when the PDB is created and stored in all file headers associated with the PDB |
| `CON_UID` | `NUMBER` | Unique identifier associated with the PDB |
| `GUID` | `RAW(16)` | Globally unique identifier (GUID) of this PDB |
| `NAME` | `VARCHAR2(128)` | Name of the PDB |
| `OPEN_MODE` | `VARCHAR2(10)` | Open mode information. Possible values:  - `MOUNTED` - `READ WRITE` - `READ ONLY` - `MIGRATE` |
| `RESTRICTED` | `VARCHAR2(3)` | Indicates whether only users possessing `RESTRICTED SESSION` privilege can connect to the PDB. Possible values:  - `YES` - `NO` - `NULL` |
| `OPEN_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Date and time when the database was last opened |
| `CREATE_SCN` | `NUMBER` | System change number (SCN) for the creation of this PDB |
| `TOTAL_SIZE` | `NUMBER` | Shows the disk space (in bytes) used by the PDB, including both data and temp files. |
| `BLOCK_SIZE` | `NUMBER` | The current block size for the PDB |
| `RECOVERY_STATUS` | `VARCHAR2(26)` | Shows the recovery status for the PDB. Possible values:  - `DISABLED`: The PDB is offline. This is similar to all files belonging to this PDB being offline, except that all files to be added to this PDB in the future will also be offline to begin with. - `DISABLED` `AUTOMATIC` `RECOVER`: Same as `DISABLED`, except that standby Active Data Guard recovery will automatically attempt to spawn PDB recovery isolation for the PDB and transition the PDB into `ENABLED`. - `ENABLED`: The PDB is not offline at the PDB level. Individual files in the PDB may be online or offline at the file level. |
| `SNAPSHOT_PARENT_CON_ID` | `NUMBER` | This column shows the container ID of the PDB that this PDB is a snapshot clone of. This column shows a nonzero value only if the PDB is a snapshot clone. For all other cases, it shows a value of 0. |
| `APPLICATION_ROOT` | `VARCHAR2(3)` | Indicates whether the PDB is an application root |
| `APPLICATION_PDB` | `VARCHAR2(3)` | Indicates whether the PDB is an application PDB |
| `APPLICATION_SEED` | `VARCHAR2(3)` | Indicates whether the PDB is an application seed (an application seed is also an application PDB) |
| `APPLICATION_ROOT_CON_ID` | `NUMBER` | If this PDB is an application PDB, the container ID of an application root to which this application PDB belongs.  If this PDB is an application root clone, the container ID of an application root to which this application root clone belongs.  Otherwise, NULL. |
| `APPLICATION_ROOT_CLONE` | `VARCHAR2(3)` | Indicates whether this PDB is an application root clone (`YES`) or not (`NO`) |
| `PROXY_PDB` | `VARCHAR2(3)` | Indicates whether this PDB is a proxy PDB (`YES`) or not (`NO`) |
| `LOCAL_UNDO` | `NUMBER` | Shows whether the PDB is in local undo. Possible values:  - `1` – PDB is in local undo mode - `0` – PDB is in shared undo mode  This column is not relevant for CDB$ROOT. |
| `UNDO_SCN` | `NUMBER` | System change number (SCN) at which the PDB was last converted from shared to local undo, or from local to shared undo.  This column is not relevant for CDB$ROOT. |
| `UNDO_TIMESTAMP` | `DATE` | Date and time at which the PDB was last converted from shared to local undo, or from local to shared undo.  This column is not relevant for CDB$ROOT. |
| `CREATION_TIME` | `DATE` | Date and time at which the PDB was created. |
| `DIAGNOSTICS_SIZE` | `NUMBER` | Shows the current disk space usage (in bytes) of the diagnostic traces generated in the PDB, which is represented by the `CON_ID` column of the row |
| `PDB_COUNT` | `NUMBER` | The number of user-created PDBs belonging to a given application root or CDB$ROOT. For all other containers, its value is 0. |
| `AUDIT_FILES_SIZE` | `NUMBER` | Shows the current disk space usage (in bytes) by Unified Audit files (.bin format) in the current PDB. |
| `MAX_SIZE` | `NUMBER` | Shows the maximum amount of disk space (in bytes) that can be used by data and temp files in the PDB |
| `MAX_DIAGNOSTICS_SIZE` | `NUMBER` | Shows the maximum amount of disk space (in bytes) that can be used by diagnostic traces generated in the PDB |
| `MAX_AUDIT_SIZE` | `NUMBER` | Shows the maximum amount of disk space (in bytes) that can be used by Unified Audit files (.bin format) in the PDB |
| `LAST_CHANGED_BY` | `VARCHAR2(11)` | Indicates what type of user last changed the PDB. Possible values:  - `COMMON USER` - `LOCAL USER` |
| `TEMPLATE` | `VARCHAR2(3)` | For internal use only |
| `TENANT_ID` | `VARCHAR2(256)` | Pluggable database tenant key |
| `UPGRADE_LEVEL` | `NUMBER` | For internal use only |
| `GUID_BASE64` | `VARCHAR2(30)` | The GUID of the PDB, encoded in base64 |
| `RECOVERY_TARGET_PDB_INCARNATION#` <sup>Foot 1</sup> | `NUMBER` | The incarnation number to which all datafiles belonging to the PDB would be recovered by the `RECOVER` `PLUGGABLE` `DATABASE` command |
| `CLOUD_IDENTITY` <sup>Foot 1</sup> | `VARCHAR2(4000)` | Cloud identifier for the PDB |
| `CLOSE_TIME` <sup>Foot 1</sup> | `TIMESTAMP(3) WITH TIME ZONE` | Date and time when the database was last closed |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.