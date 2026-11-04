---
title: ALL_TRIGGER_ORDERING
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2120.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TRIGGER_ORDERING` describes the triggers accessible to the current user that have `FOLLOWS` or `PRECEDES` ordering.

Related Views

- `DBA_TRIGGER_ORDERING` describes all triggers in the database that have `FOLLOWS` or `PRECEDES` ordering.
- `USER_TRIGGER_ORDERING` describes the triggers owned by the current user that have `FOLLOWS` or `PRECEDES` ordering. This view does not display the `TRIGGER_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TRIGGER_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the trigger |
| `TRIGGER_NAME` | `VARCHAR2(30)` |  | Name of the trigger |
| `REFERENCED_TRIGGER_OWNER` | `VARCHAR2(30)` |  | Owner of the referenced trigger |
| `REFERENCED_TRIGGER_NAME` | `VARCHAR2(30)` |  | Name of the referenced trigger |
| `ORDERING_TYPE` | `VARCHAR2(8)` |  | Type of the ordering between the trigger and the referenced trigger: |

See Also:

- ["DBA\_TRIGGER\_ORDERING"](statviews_5066.md)
- ["USER\_TRIGGER\_ORDERING"](statviews_5494.md)