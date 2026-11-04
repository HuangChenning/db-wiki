---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RMAN_ENCRYPTION_ALGORITHMS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.180 V$RMAN\_ENCRYPTION\_ALGORITHMS

It is used by the RMAN client to validate user-requested algorithms. This view will list AES128, AES192, and AES256 encryption algorithms for the current release. The default algorithm is AES128.

| Column | Datatype | Description |
| --- | --- | --- |
| `ALGORITHM_ID` | `NUMBER` | Number to identify the algorithm |
| `ALGORITHM_NAME` | `VARCHAR2(64)` | Name of the algorithm (for example, AES128, AES192, or AES256) |
| `ALGORITHM_DESCRIPTION` | `VARCHAR2(64)` | Description of the algorithm |
| `IS_DEFAULT` | `VARCHAR2(3)` | Indicates whether this is the default encryption algorithm (`YES`) or not (`NO`). This value is set by Oracle Database and may vary for each Release (that is, it is not dependent on user-specified RMAN configuration). |
| `RESTORE_ONLY` | `VARCHAR2(3)` | Indicates whether this algorithm can be used for restore only (`YES`) or not (`NO`). If the value is `NO`, then the algorithm is also allowed for backup. This column is useful in determining whether an encryption algorithm is deprecated for backup purpose. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |