---
title: ALL_VIEWS_AE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2134.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_VIEWS_AE` describes the views (across all editions) accessible to the current user.

Related Views

- `DBA_VIEWS_AE` describes all views (across all editions) in the database.
- `USER_VIEWS_AE` describes the views (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the view |
| `VIEW_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the view |
| `TEXT_LENGTH` | `NUMBER` |  | Length of the view text |
| `TEXT` | `LONG` |  | View text |
| `TYPE_TEXT_LENGTH` | `NUMBER` |  | Length of the type clause of the typed view |
| `TYPE_TEXT` | `VARCHAR2(4000)` |  | Type clause of the typed view |
| `OID_TEXT_LENGTH` | `NUMBER` |  | Length of the `WITH OID` clause of the typed view |
| `OID_TEXT` | `VARCHAR2(4000)` |  | `WITH OID` clause of the typed view |
| `VIEW_TYPE_OWNER` | `VARCHAR2(30)` |  | Owner of the type of the view if the view is an typed view |
| `VIEW_TYPE` | `VARCHAR2(30)` |  | Type of the view if the view is a typed view |
| `SUPERVIEW_NAME` | `VARCHAR2(30)` |  | Name of the superview, if the view is a subview |
| `EDITIONING_VIEW` | `VARCHAR2(1)` |  | Indicates whether the view is an editioning view (`Y`) or not (`N`) |
| `READ_ONLY` | `VARCHAR2(1)` |  | Indicates whether the view is read-only (`Y`) or not (`N`) |
| `EDITION_NAME` | `VARCHAR2(30)` |  | Name of the application edition where the object is defined |

See Also:

- ["DBA\_VIEWS\_AE"](statviews_5086.md)
- ["USER\_VIEWS\_AE"](statviews_5510.md)