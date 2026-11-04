---
title: ALL_VIEWS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2133.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_VIEWS` describes the views accessible to the current user.

Related Views

- `DBA_VIEWS` describes all views in the database.
- `USER_VIEWS` describes the views owned by the current user. This view does not display the `OWNER` column.

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
| `VIEW_TYPE_OWNER` | `VARCHAR2(30)` |  | Owner of the type of the view if the view is a typed view |
| `VIEW_TYPE` | `VARCHAR2(30)` |  | Type of the view if the view is a typed view |
| `SUPERVIEW_NAME` | `VARCHAR2(30)` |  | Name of the superview |
| `EDITIONING_VIEW` | `VARCHAR2(1)` |  | Reserved for future use |
| `READ_ONLY` | `VARCHAR2(1)` |  | Indicates whether the view is read-only (`Y`) or not (`N`) |

See Also:

- ["DBA\_VIEWS"](statviews_5085.md)
- ["USER\_VIEWS"](statviews_5509.md)