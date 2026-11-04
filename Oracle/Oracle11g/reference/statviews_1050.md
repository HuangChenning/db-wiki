---
title: ALL_CUBE_ATTRIBUTES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1050.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_ATTRIBUTES` describes the attributes for the OLAP cube dimensions accessible to the current user.

Related Views

- `DBA_CUBE_ATTRIBUTES` describes the attributes for all OLAP cube dimensions in the database.
- `USER_CUBE_ATTRIBUTES` describes the attributes for the OLAP cube dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the cube dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a cube dimension (such as `TIME`) |
| `ATTRIBUTE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of an attribute of the dimension (such as `LONG_DESCRIPTION` or `END_DATE`) |
| `TARGET_DIMENSION_NAME` | `VARCHAR2(30)` |  | Name of the target dimension of the attribute |
| `ATTRIBUTE_ROLE` | `VARCHAR2(17)` |  | Special role this attribute plays; NULL if none: |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the attribute in the session language |
| `DATA_TYPE` | `VARCHAR2(106)` |  | Data type of the attribute, (such as `VARCHAR2` or `FLOAT`) |
| `DATA_LENGTH` | `NUMBER` | `NOT NULL` | Length of a text data type |
| `DATA_PRECISION` | `NUMBER` |  | Precision of a numeric data type |
| `DATA_SCALE` | `NUMBER` |  | Scale of a numeric data type |

See Also:

- ["DBA\_CUBE\_ATTRIBUTES"](statviews_3126.md)
- ["USER\_CUBE\_ATTRIBUTES"](statviews_5262.md)