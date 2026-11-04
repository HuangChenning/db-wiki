---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CLIENT_SECRETS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.125 V$CLIENT\_SECRETS

`V$CLIENT_SECRETS` lists the secrets that are present in the keystore.

Only `SYS`, `SYSKM`, and users with the `ADMINISTER KEY MANAGEMENT` privilege can access this view.

| Column | Datatype | Description |
| --- | --- | --- |
| `CLIENT` | `VARCHAR2(2000)` | Name provided by the client |
| `SECRET_TAG` | `VARCHAR2(4000)` | Associated information with the client |
| `CREATION_TIME` | `TIMESTAMP(6) WITH TIME ZONE` | Time when the secret was created |
| `ACTIVATION_TIME` | `TIMESTAMP(6) WITH TIME ZONE` | Time when the secret was actually put to use |
| `OWNER` | `VARCHAR2(128)` | User who created the secret |
| `OWNER_ID` | `NUMBER` | User ID of the user who created the secret |
| `KEYSTORE_TYPE` | `VARCHAR2(17)` | Type of keystore in which the secret is stored:  - `OKV` - Oracle Key Vault - `SOFTWARE` `KEYSTORE` - `UNDEFINED` - This value is shown if the database has no information about the type of keystore where the master key resides |
| `BACKED_UP` | `VARCHAR2(9)` | Indicates whether the secret has been backed up or not |
| `OWNER_DBNAME` | `VARCHAR2(128)` | Database that created the secret |
| `OWNER_DBID` | `NUMBER` | Database ID where the secret was created |
| `OWNER_INSTANCE_NAME` | `VARCHAR2(30)` | Instance name of the instance where the secret was created |
| `OWNER_INSTANCE_NUMBER` | `NUMBER` | Instance number of the instance where the secret was created |
| `OWNER_INSTANCE_SERIAL` | `NUMBER` | Serial number of the instance where the secret was created |
| `OWNER_PDBNAME` | `VARCHAR2(128)` | Pluggable database (PDB) where the secret was created |
| `OWNER_PDBID` | `NUMBER` | PDB ID where the secret was created |
| `OWNER_PDBUID` | `NUMBER` | PDB UID where the secret was created |
| `OWNER_PDBGUID` | `RAW(16)` | PDB GUID where the secret was created |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ASOAG10311) for information about keystore management