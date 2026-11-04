---
title: ALL_IDENTIFIERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1102.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_IDENTIFIERS` displays information about the identifiers in the stored objects accessible to the current user.

Related Views

- `DBA_IDENTIFIERS` displays information about the identifiers in all stored objects in the database.
- `USER_IDENTIFIERS` displays information about the identifiers in the stored objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the identifier |
| `NAME` | `VARCHAR2(30)` |  | Name of the identifier |
| `SIGNATURE` | `VARCHAR2(32)` |  | Signature of the identifier |
| `TYPE` | `VARCHAR2(18)` |  | Type of the identifier |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object where the identifier action occurred |
| `OBJECT_TYPE` | `VARCHAR2(13)` |  | Type of the object where the identifier action occurred |
| `USAGE` | `VARCHAR2(11)` |  | Type of the identifier usage: |
| `USAGE_ID` | `NUMBER` |  | Unique key for the identifier usage within the object |
| `LINE` | `NUMBER` |  | Line number of the identifier action |
| `COL` | `NUMBER` |  | Column number of the identifier action |
| `USAGE_CONTEXT_ID` | `NUMBER` |  | Context `USAGE_ID` of the identifier usage |

See Also:

- ["DBA\_IDENTIFIERS"](statviews_4074.md)
- ["USER\_IDENTIFIERS"](statviews_5316.md)