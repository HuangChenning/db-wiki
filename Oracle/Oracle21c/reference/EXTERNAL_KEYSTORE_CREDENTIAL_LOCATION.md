---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/EXTERNAL_KEYSTORE_CREDENTIAL_LOCATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.129 EXTERNAL\_KEYSTORE\_CREDENTIAL\_LOCATION

`EXTERNAL_KEYSTORE_CREDENTIAL_LOCATION` specifies the location of the secure external keystore.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `EXTERNAL_KEYSTORE_CREDENTIAL_LOCATION = file-location` |
| Default value | No default value |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | This parameter can be set on each instance. Oracle recommends that if the instances have a shared location, then use a directory on the shared location for this parameter and set the same value on all Oracle RAC instances. If the database does not have a shared location, then each instance of the database will have its own directory and the value should be set per-instance. |

TDE keystore credentials can be stored in a secure external keystore to automate Transparent Data Encryption (TDE) operations.

To automate the setting of the Master Key in a newly-provisioned PDB, set `EXTERNAL_KEYSTORE_CREDENTIAL_LOCATION` so that the CDB knows the location of the secure external keystore.

When a file specification is set with this parameter, the secure external keystore is looked for in that location. If the secure external keystore is not found in that location, then this parameter is ignored.

See Also:

[Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ASOAG-GUID-4F6206B6-A33F-4FB1-9223-DD61FFAD3F12) for more information about using TDE