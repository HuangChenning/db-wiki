---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ATTRIBUTE_TRANSFORMATIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.110 ALL\_ATTRIBUTE\_TRANSFORMATIONS

`ALL_ATTRIBUTE_TRANSFORMATIONS` describes the transformation functions for the transformations accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_TRANSFORMATIONS` describes the transformation functions for all transformations in the database.
- `USER_ATTRIBUTE_TRANSFORMATIONS` describes the transformation functions for the transformations owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TRANSFORMATION_ID` | `NUMBER` | `NOT NULL` | Unique identifier for the transformation |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owning user of the transformation |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Transformation name |
| `FROM_TYPE` | `VARCHAR2(257)` |  | Source type name |
| `TO_TYPE` | `VARCHAR2(385)` |  | Target type name |
| `ATTRIBUTE` | `NUMBER` | `NOT NULL` | Target type attribute number |
| `ATTRIBUTE_TRANSFORMATION` | `VARCHAR2(4000)` |  | Transformation function for the attribute |

See Also:

- " [DBA\_ATTRIBUTE\_TRANSFORMATIONS](DBA_ATTRIBUTE_TRANSFORMATIONS.md) "
- " [USER\_ATTRIBUTE\_TRANSFORMATIONS](USER_ATTRIBUTE_TRANSFORMATIONS.md) "