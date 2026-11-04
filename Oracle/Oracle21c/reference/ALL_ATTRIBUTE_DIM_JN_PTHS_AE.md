---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ATTRIBUTE_DIM_JN_PTHS_AE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.91 ALL\_ATTRIBUTE\_DIM\_JN\_PTHS\_AE

`ALL_ATTRIBUTE_DIM_JN_PTHS_AE` describes the join paths for the attribute dimensions (across all editions) accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIM_JN_PTHS_AE` describes the join paths for all attribute dimensions (across all editions) in the database.
- `USER_ATTRIBUTE_DIM_JN_PTHS_AE` describes the join paths for the attribute dimensions (across all editions) owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the attribute dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension |
| `JOIN_PATH_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the join path |
| `ON_CONDITION` | `VARCHAR2(4000)` |  | Join condition specified in the `ON` clause |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the classification in the list of classifications associated with the attribute dimension |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the attribute dimension is defined |

Note:

This view is available starting with Oracle Database 21c, Release Update 21.5.

See Also:

- " [DBA\_ATTRIBUTE\_DIM\_JN\_PTHS\_AE](DBA_ATTRIBUTE_DIM_JN_PTHS_AE.md) "
- " [USER\_ATTRIBUTE\_DIM\_JN\_PTHS\_AE](USER_ATTRIBUTE_DIM_JN_PTHS_AE.md) "