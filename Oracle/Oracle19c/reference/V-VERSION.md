---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-VERSION.html
tags:
  - oracle
  - 19c
  - reference
---

## 9.128 V$VERSION

`V$VERSION` displays the version number of Oracle Database. The database components have the same version number as the database, so the version number is returned only once.

| Column | Datatype | Description |
| --- | --- | --- |
| `BANNER` | `VARCHAR2(80)` | Component name and version number |
| `BANNER_FULL` | `VARCHAR2(160)` | The new 2 line banner format introduced in Oracle Database 18c. The banner displays the database release and version number. |
| `BANNER_LEGACY` | `VARCHAR2(80)` | The legacy 1 line banner used before Oracle Database 18c. This column displays the same value as the `BANNER` column. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |