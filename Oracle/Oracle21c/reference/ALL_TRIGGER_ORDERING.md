---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TRIGGER_ORDERING.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.125 ALL\_TRIGGER\_ORDERING

`ALL_TRIGGER_ORDERING` describes the triggers accessible to the current user that have `FOLLOWS` or `PRECEDES` ordering.

Related Views

- `DBA_TRIGGER_ORDERING` describes all triggers in the database that have `FOLLOWS` or `PRECEDES` ordering.
- `USER_TRIGGER_ORDERING` describes the triggers owned by the current user that have `FOLLOWS` or `PRECEDES` ordering. This view does not display the `TRIGGER_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TRIGGER_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the trigger |
| `TRIGGER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the trigger |
| `REFERENCED_TRIGGER_OWNER` | `VARCHAR2(128)` |  | Owner of the referenced trigger |
| `REFERENCED_TRIGGER_NAME` | `VARCHAR2(128)` |  | Name of the referenced trigger |
| `ORDERING_TYPE` | `VARCHAR2(8)` |  | Type of the ordering between the trigger and the referenced trigger:  - `FOLLOWS` - `PRECEDES` |

See Also:

- " [DBA\_TRIGGER\_ORDERING](DBA_TRIGGER_ORDERING.md) "
- " [USER\_TRIGGER\_ORDERING](USER_TRIGGER_ORDERING.md) "