---
title: "V$TABLESPACE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3100.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TABLESPACE` displays tablespace information from the control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `TS#` | `NUMBER` | Tablespace number |
| `NAME` | `VARCHAR2(30)` | Tablespace name |
| `INCLUDED_IN_DATABASE_BACKUP` | `VARCHAR2(3)` | Indicates whether the tablespace is included in full database backups using the `BACKUP DATABASE` RMAN command (`YES`) or not (`NO`); `NO` only if the `CONFIGURE EXCLUDE` RMAN command was used for this tablespace |
| `BIGFILE` | `VARCHAR2(3)` | Indicates whether the tablespace is a bigfile tablespace (`YES`) or a smallfile tablespace (`NO`) |
| `FLASHBACK_ON` | `VARCHAR2(3)` | Indicates whether the tablespace participates in `FLASHBACK DATABASE` operations (`YES`) or not (`NO`) |
| `ENCRYPT_IN_BACKUP` | `VARCHAR2(3)` | Indicates whether encryption is turned ON or off at the tablespace level: - `ON` - Encryption is turned ON at the tablespace level - `OFF` - Encryption is turned OFF at the tablespace level - NULL - Encryption is neither explicitly turned on nor off at the tablespace level (default or when cleared) |