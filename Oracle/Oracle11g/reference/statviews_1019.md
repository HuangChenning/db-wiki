---
title: ALL_ATTRIBUTE_TRANSFORMATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1019.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_ATTRIBUTE_TRANSFORMATIONS` displays information about the transformation functions for the transformations accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_TRANSFORMATIONS` displays information about the transformation functions for all transformations in the database.
- `USER_ATTRIBUTE_TRANSFORMATIONS` displays information about the transformation functions for the transformations owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TRANSFORMATION_ID` | `NUMBER` | `NOT NULL` | Unique identifier for the transformation |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owning user of the transformation |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Transformation name |
| `FROM_TYPE` | `VARCHAR2(61)` |  | Source type name |
| `TO_TYPE` | `VARCHAR2(91)` |  | Target type name |
| `ATTRIBUTE` | `NUMBER` | `NOT NULL` | Target type attribute number |
| `ATTRIBUTE_TRANSFORMATION` | `VARCHAR2(4000)` |  | Transformation function for the attribute |

See Also:

- ["DBA\_ATTRIBUTE\_TRANSFORMATIONS"](statviews_3070.md)