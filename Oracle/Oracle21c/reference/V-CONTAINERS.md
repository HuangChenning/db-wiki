---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CONTAINERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.140 V$CONTAINERS

`V$CONTAINERS` displays information about PDBs and the root associated with the current instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `DBID` | `NUMBER` | PDB identifier calculated when the PDB is created and stored in all file headers associated with the PDB |
| `CON_UID` | `NUMBER` | Unique identifier associated with the PDB |
| `GUID` | `RAW(16)` | Globally unique identifier (GUID) of this PDB |
| `NAME` | `VARCHAR2(128)` | Name of the PDB |
| `OPEN_MODE` | `VARCHAR2(10)` | Open mode information. Possible values:  - `MOUNTED` - `READ WRITE` - `READ ONLY` - `MIGRATE` |
| `RESTRICTED` | `VARCHAR2(3)` | Indicates whether only users possessing `RESTRICTED SESSION` privilege can connect to the PDB |
| `OPEN_TIME` | `TIMESTAMP(3)` | Date and time when the database was last opened |
| `CREATE_SCN` | `NUMBER` | System change number (SCN) for the creation of this PDB |
| `TOTAL_SIZE` | `NUMBER` | If a PDB is opened, disk space (in bytes) used by the container, including both data and temp files. If a PDB is closed, will be set to `0`. |
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
| `PDB_COUNT` | `NUMBER` | The number of user-created PDBs belonging to a given application root or CDB$ROOT. For all other containers, its value is 0. |
| `AUDIT_FILES_SIZE` | `NUMBER` | Shows the current disk space usage (in bytes) by Unified Audit files (.bin format) in the container |
| `MAX_SIZE` | `NUMBER` | Shows the maximum amount of disk space (in bytes) that can be used by data and temp files in the container |
| `MAX_DIAGNOSTICS_SIZE` | `NUMBER` | Shows the maximum amount of disk space (in bytes) that can be used by diagnostic traces generated in the container |
| `MAX_AUDIT_SIZE` | `NUMBER` | Shows the maximum amount of disk space (in bytes) that can be used by Unified Audit files (.bin format) in the container |
| `LAST_CHANGED_BY` | `VARCHAR2(11)` | Indicates what type of user last changed the PDB. Possible values:  - `COMMON USER` - `LOCAL USER` |
| `MEMBER_CDB` | `VARCHAR2(3)` | Indicates whether the row corresponds to a Member CDB part of the CDB Fleet (`YES`) or not (`NO`). This column is only meaningful in the Lead CDB of a CDB Fleet, which keeps track of other CDBs as containers in the CDB Fleet. |
| `TENANT_ID` | `VARCHAR2(256)` | Pluggable database tenant key |
| `UPGRADE_LEVEL` | `NUMBER` | For internal use only |
| `GUID_BASE64` | `VARCHAR2(30)` | The GUID of the PDB, encoded in base64 |
| `CLOUD_IDENTITY` <sup>Foot 1</sup> | `VARCHAR2(4000)` | Cloud identifier for the PDB |
| `CLOSE_TIME` <sup>Foot 1</sup> | `TIMESTAMP(3)` | Date and time when the database was last closed |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.