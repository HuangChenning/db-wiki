---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ATTRIBUTE_DIM_ORDER_ATTRS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.105 ALL\_ATTRIBUTE\_DIM\_ORDER\_ATTRS

`ALL_ATTRIBUTE_DIM_ORDER_ATTRS` describes the order attributes of the attribute dimensions accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIM_ORDER_ATTRS` describes the order attributes of all attribute dimensions in the database.
- `USER_ATTRIBUTE_DIM_ORDER_ATTRS` describes the order attributes of the attribute dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the attribute dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension |
| `LEVEL_NAME` | `VARCHAR2(128)` |  | Name of the level to order or the name of the level that has the `ORDER` `BY` clause |
| `AGG_FUNC` | `VARCHAR2(3)` |  | Aggregation function of the `ORDER` `BY` clause: - `MIN` - `MAX` |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` |  | Name of the order attribute |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order number of the attribute in the list of order attributes |
| `CRITERIA` | `VARCHAR2(4)` |  | Criteria of the ordering, either ascending or descending: - `ASC` - `DESC` |
| `NULLS_POSITION` | `VARCHAR2(5)` |  | Position of `ORDER` `BY` values in the orderings:  - `FIRST` - `LAST` |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

See Also:

- " [DBA\_ATTRIBUTE\_DIM\_ORDER\_ATTRS](DBA_ATTRIBUTE_DIM_ORDER_ATTRS.md) "
- " [USER\_ATTRIBUTE\_DIM\_ORDER\_ATTRS](USER_ATTRIBUTE_DIM_ORDER_ATTRS.md) "