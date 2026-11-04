---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_DIGEST_VERIFIERS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_DIGEST_VERIFIERS` enables the database administrator to check which users have Digest verifiers stored on disk and the type of hashing algorithm used for the verifiers.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(128)` |  | Name of the user |
| `HAS_DIGEST_VERIFIERS` | `VARCHAR2(3)` |  | `YES` if a Digest verifier exists, `NO` otherwise |
| `DIGEST_TYPE` | `CHAR(3)` |  | The type of hashing algorithm used for the Digest verifier. For instance, `MD5` for users with MD5 Digest verifiers. If no Digest verifier exists, this column is `NULL`. |