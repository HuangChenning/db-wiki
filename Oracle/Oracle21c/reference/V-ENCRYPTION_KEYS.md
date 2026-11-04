---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ENCRYPTION_KEYS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.198 V$ENCRYPTION\_KEYS

Note that, even if Transparent Data Encryption (TDE) is not configured in the database, a query of `V$ENCRYPTION_KEYS` checks for TDE configuration validity and may print warnings in alert log.

| Column | Datatype | Description |
| --- | --- | --- |
| `KEY_ID` | `VARCHAR2(78)` | Master key identifier |
| `HEX_MKID` | `VARCHAR2(78)` | Master key identifier, in hex format |
| `TAG` | `VARCHAR2(4000)` | Associated user-defined Information with the master key |
| `CREATION_TIME` | `TIMESTAMP(6) WITH TIME ZONE` | Time that the master key was created |
| `ACTIVATION_TIME` | `TIMESTAMP(6) WITH TIME ZONE` | Time that the master key was put into use |
| `CREATOR` | `VARCHAR2(128)` | User that created the master key |
| `CREATOR_ID` | `NUMBER` | User ID that created the master key |
| `USER` | `VARCHAR2(128)` | User that activated the master key |
| `USER_ID` | `NUMBER` | User ID that activated the master key |
| `KEY_USE` | `VARCHAR2(10)` | Indicates whether the master key is used for TDE operations in a PDB or not |
| `KEYSTORE_TYPE` | `VARCHAR2(17)` | Master key is in:  - `OKV` - Oracle Key Vault - `SOFTWARE KEYSTORE` - `UNDEFINED` - This value is shown if the database has no information about the type of keystore where the master key resides |
| `ORIGIN` | `VARCHAR2(41)` | Provides information about the origin of the master key:  - `LOCAL` - The master key was created locally in this database - `IMPORTED` - The master key was imported from another database - `IMPORTED BUT KEY METADATA CREATED LOCALLY` - The master key was imported from another database, but the key metadata was created locally due to activation - `UNKNOWN BUT KEY METADATA CREATED LOCALLY` - It is unknown whether the master key was imported from another database or created locally, but the key metadata was created locally due to activation - `UNDEFINED` - The status of the master key is unknown |
| `BACKED_UP` | `VARCHAR2(9)` | Indicates whether the key has been backed up or not |
| `CREATOR_DBNAME` | `VARCHAR2(128)` | Database that created the key |
| `CREATOR_DBID` | `NUMBER` | Database ID where the key was created |
| `CREATOR_INSTANCE_NAME` | `VARCHAR2(30)` | Instance name of the instance where the key was created |
| `CREATOR_INSTANCE_NUMBER` | `NUMBER` | Instance number of the instance where the key was created |
| `CREATOR_INSTANCE_SERIAL` | `NUMBER` | Serial number of the instance where the key was created |
| `CREATOR_PDBNAME` | `VARCHAR2(128)` | PDB where the key was created |
| `CREATOR_PDBID` | `NUMBER` | PDB ID where the key was created |
| `CREATOR_PDBUID` | `NUMBER` | PDB UID where the key was created |
| `CREATOR_PDBGUID` | `RAW(16)` | PDB GUID where the key was created |
| `ACTIVATING_DBNAME` | `VARCHAR2(128)` | Database that activated the key |
| `ACTIVATING_DBID` | `NUMBER` | Database ID where the key was activated |
| `ACTIVATING_INSTANCE_NAME` | `VARCHAR2(30)` | Instance name of the instance where the key was activated |
| `ACTIVATING_INSTANCE_NUMBER` | `NUMBER` | Instance number of the instance where the key was activated |
| `ACTIVATING_INSTANCE_SERIAL` | `NUMBER` | Serial number of the instance where the key was activated |
| `ACTIVATING_PDBNAME` | `VARCHAR2(128)` | PDB where the key was activated |
| `ACTIVATING_PDBID` | `NUMBER` | PDB ID where the key was activated |
| `ACTIVATING_PDBUID` | `NUMBER` | PDB UID where the key was activated |
| `ACTIVATING_PDBGUID` | `RAW(16)` | PDB GUID where the key was activated |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ASOAG10311) for information about keystore management