---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-TABLESPACE.html
tags:
  - oracle
  - 12c
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
| `ENCRYPT_IN_BACKUP` | `VARCHAR2(3)` | Indicates whether encryption is turned ON or off at the tablespace level:  - `ON` - Encryption is turned ON at the tablespace level - `OFF` - Encryption is turned OFF at the tablespace level - NULL - Encryption is neither explicitly turned on nor off at the tablespace level (default or when cleared) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |