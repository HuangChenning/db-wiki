---
title: DBA_TRANSFORMATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5064.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_TRANSFORMATIONS` displays information about all transformations in the database. These transformations can be specified with Advanced Queuing operations such as enqueue, dequeue, and subscribe to automatically integrate transformations in AQ messaging. Its columns are the same as those in `ALL_TRANSFORMATIONS`.

Related Views

`ALL_TRANSFORMATIONS` displays information about all transformations accessible to the current user.

`USER_TRANSFORMATIONS` displays information about transformations owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TRANSFORMATION_ID` | `NUMBER` | `NOT NULL` | Unique identifier for the transformation |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owning user of the transformation |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Transformation name |
| `FROM_TYPE` | `VARCHAR2(61)` |  | Source type name |
| `TO_TYPE` | `VARCHAR2(91)` |  | Target type name |

See Also:

- ["ALL\_TRANSFORMATIONS"](statviews_2118.md)
- ["USER\_TRANSFORMATIONS"](statviews_5492.md)