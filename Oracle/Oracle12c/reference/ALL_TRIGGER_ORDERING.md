---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_TRIGGER_ORDERING.html
tags:
  - oracle
  - 12c
  - reference
---

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