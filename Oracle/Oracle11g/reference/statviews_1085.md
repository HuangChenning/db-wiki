---
title: ALL_ENCRYPTED_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1085.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_ENCRYPTED_COLUMNS` displays encryption algorithm information for the encrypted columns in the tables accessible to the current user.

Related Views

- `DBA_ENCRYPTED_COLUMNS` displays encryption algorithm information for all encrypted columns in the database.
- `USER_ENCRYPTED_COLUMNS` displays encryption algorithm information for the encrypted columns in the tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the column |
| `ENCRYPTION_ALG` | `VARCHAR2(29)` |  | Encryption algorithm used to protect secrecy of data in this column: |
| `SALT` | `VARCHAR2(3)` |  | Indicates whether the column is encrypted with SALT (`YES`) or not (`NO`) |
| `INTEGRITY_ALG` | `VARCHAR2(12)` |  | Integrity algorithm used for the column: |