---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ENCRYPTED_TABLESPACES.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.197 V$ENCRYPTED\_TABLESPACES

`V$ENCRYPTED_TABLESPACES` displays information about tablespaces that are encrypted.

The information displayed by this view is meaningful only for tablespaces in open containers and for the data files that are online. This is because the information is derived after the file headers making up a tablespace have been examined during the open operation.

During an encryption or decryption operation, the encryption or decryption progress can be obtained by comparing the values of the `BLOCKS_ENCRYPTED` and `BLOCKS_DECRYPTED` columns in this view with the value of the `BLOCKS` column in the `DBA_DATA_FILES` view.

| Column | Datatype | Description |
| --- | --- | --- |
| `TS#` | `NUMBER` | Tablespace number |
| `ENCRYPTIONALG` | `VARCHAR2(7)` | Encryption algorithm:  - `NONE` - `3DES168` - `AES128` - `AES192` - `AES256` |
| `ENCRYPTEDTS` | `VARCHAR2(3)` | Indicates whether the tablespace is encrypted (`YES`) or not (`NO`) |
| `ENCRYPTEDKEY` | `RAW(32)` | Encrypted version of the tablespace key for the encrypted tablespace |
| `MASTERKEYID` | `RAW(16)` | ID of the master key that was used to encrypt the tablespace key |
| `BLOCKS_ENCRYPTED` | `NUMBER` | Number of tablespace blocks that have been encrypted during the lifetime of this instance |
| `BLOCKS_DECRYPTED` | `NUMBER` | Number of tablespace blocks that have been decrypted during the lifetime of this instance |
| `KEY_VERSION` | `NUMBER` | Every encrypt/decrypt/rekey of a tablespace adds a carnation/version of the tablespace key, and the key version is incremented. A decrypted tablespace could still have a none-zero key version. In certain scenarios, however, the tablespace key version might reset to `0`; for example, when a tablespace or a pluggable database (PDB) is plugged into a foreign database, or if the control file is recreated. |
| `STATUS` | `VARCHAR2(10)` | Shows the status of a tablespace. Possible values:  - `NORMAL`: Used when the tablespace is not in one of the other statuses. - `REKEYING`: Used when a rekey operation is taking place - `ENCRYPTING`: Used when an encrypt operation is taking place - `DECRYPTING`: Used when a decrypt operation is taking place - `UNKNOWN`: Used when the database is mounted but not open (before the datafile is online and the key is known to the database)  Note: The `REKEYING`, `ENCRYPTING`, and `DECRYPTING` values can also be reported after a datafile, whose encryption state is different from the tablespace definition, is restored. In such cases, the value represents the operation that is required to make all datafiles in the tablespace consistent by using the `FINISH` clause of the `ALTER` `TABLESPACE` `ENCRYPTION` statement. See [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ASOAG-GUID-1CA947A5-164A-4AA9-AD75-F7D9D4F6FFF8) for information about changing the encryption state of a tablespace. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$DATABASE\_KEY\_INFO](V-DATABASE_KEY_INFO.md) "