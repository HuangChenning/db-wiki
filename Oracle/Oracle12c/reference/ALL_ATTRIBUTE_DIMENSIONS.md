---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_ATTRIBUTE_DIMENSIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_ATTRIBUTE_DIMENSIONS` describes the attribute dimensions accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIMENSIONS` describes all attribute dimensions in the database.
- `USER_ATTRIBUTE_DIMENSIONS` describes the attribute dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of attribute dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension |
| `DIMENSION_TYPE` | `VARCHAR2(8)` |  | Type of the attribute dimension: - `TIME` - `STANDARD` |
| `ALL_MEMBER_NAME` | `CLOB)` | `NOT NULL` | An expression for the name of the ALL member for the attribute dimension |
| `ALL_MEMBER_CAPTION` | `CLOB` |  | An expression for the caption for the ALL member of the attribute dimension, or `NULL` if not specified |
| `ALL_MEMBER_DESCRIPTION` | `CLOB` |  | An expression for the description for the ALL member of the attribute dimension |
| `COMPILE_STATE` | `VARCHAR2(7)` |  | Compile status of the attribute dimension:  - `VALID` - `INVALID` |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_ATTRIBUTE\_DIMENSIONS](DBA_ATTRIBUTE_DIMENSIONS.md) "
- " [USER\_ATTRIBUTE\_DIMENSIONS](USER_ATTRIBUTE_DIMENSIONS.md) "