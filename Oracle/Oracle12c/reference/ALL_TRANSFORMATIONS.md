---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_TRANSFORMATIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_TRANSFORMATIONS` displays information about all transformations accessible to the current user.

These transformations can be specified with Advanced Queuing operations such as enqueue, dequeue, and subscribe to automatically integrate transformations in AQ messaging.

Related Views

- `DBA_TRANSFORMATIONS` displays information about all transformations in the database.
- `USER_TRANSFORMATIONS` displays information about transformations owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TRANSFORMATION_ID` | `NUMBER` | `NOT NULL` | Unique identifier for the transformation |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owning user of the transformation |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Transformation name |
| `FROM_TYPE` | `VARCHAR2(128)` |  | Source type name |
| `TO_TYPE` | `VARCHAR2(256)` |  | Target type name |

See Also:

- " [DBA\_TRANSFORMATIONS](DBA_TRANSFORMATIONS.md) "
- " [USER\_TRANSFORMATIONS](USER_TRANSFORMATIONS.md) "