---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DATABASE_KEY_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.156 V$DATABASE\_KEY\_INFO

`V$DATABASE_KEY_INFO` provides the information of the default database key used to encrypt data blocks. Oracle uses the database key to encrypt sensitive information in SYSTEM, UNDO, and TEMP tablespaces when such data has dependency from encrypted tablespaces or encrypted columns

`V$DATABASE_KEY_INFO` reflects the database key information stored in the control file. Generally it is the same as the system tablespace key recorded in the system tablespace. If the system tablespace is encrypted, it will also appear in `V$ENCRYPTED_TABLESPACES`. If the system tablespace is not encrypted, this is the only view providing this information.

| Column | Datatype | Description |
| --- | --- | --- |
| `ENCRYPTIONALG` | `VARCHAR2(7)` | Encryption algorithm:  - `NONE` - `3DES168` - `AES128` - `AES192` - `AES256`  `AES128` is the default encryption algorithm. |
| `ENCRYPTEDKEY` | `RAW(48)` | Encrypted version of the database key |
| `MASTERKEYID` | `RAW(16)` | ID of the master key that was used to encrypt the database key |
| `MASTERKEY_ACTIVATED` | `VARCHAR2(3)` | Indicates whether the master key has been set (`YES`) or not (`NO`) for this database or container in the Oracle Key Store. In other words, indicates whether Transparent Data Encryption (TDE) has been activated for this database or container |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$ENCRYPTED\_TABLESPACES](V-ENCRYPTED_TABLESPACES.md) "