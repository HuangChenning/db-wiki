---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ENCRYPTED_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.181 ALL\_ENCRYPTED\_COLUMNS

`ALL_ENCRYPTED_COLUMNS` displays encryption algorithm information for the encrypted columns in the tables accessible to the current user.

Related Views

- `DBA_ENCRYPTED_COLUMNS` displays encryption algorithm information for all encrypted columns in the database.
- `USER_ENCRYPTED_COLUMNS` displays encryption algorithm information for the encrypted columns in the tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the column |
| `ENCRYPTION_ALG` | `VARCHAR2(29)` |  | Encryption algorithm used to protect secrecy of data in this column:  - `3 Key Triple DES 168 bits key` - `AES 128 bits key` - `AES 192 bits key` - `AES 256 bits key` |
| `SALT` | `VARCHAR2(3)` |  | Indicates whether the column is encrypted with SALT (`YES`) or not (`NO`) |
| `INTEGRITY_ALG` | `VARCHAR2(12)` |  | Integrity algorithm used for the column:  - `SHA-1` - `NOMAC` |

See Also:

- " [DBA\_ENCRYPTED\_COLUMNS](DBA_ENCRYPTED_COLUMNS.md) "
- " [USER\_ENCRYPTED\_COLUMNS](USER_ENCRYPTED_COLUMNS.md) "