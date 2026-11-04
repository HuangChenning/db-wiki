---
title: ALL_SEC_RELEVANT_COLS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2060.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SEC_RELEVANT_COLS` describes the security relevant columns of the security policies for the tables and views accessible to the current user.

Related Views

- `DBA_SEC_RELEVANT_COLS` describes the security relevant columns of all security policies in the database.
- `USER_SEC_RELEVANT_COLS` describes the security relevant columns of the security policies for the tables and views owned by the current user. This view does not display the `OBJECT_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(30)` |  | Owner of the table or view |
| `OBJECT_NAME` | `VARCHAR2(30)` |  | Name of the table or view |
| `POLICY_GROUP` | `VARCHAR2(30)` |  | Name of the policy group |
| `POLICY_NAME` | `VARCHAR2(30)` |  | Name of the policy |
| `SEC_REL_COLUMN` | `VARCHAR2(30)` |  | Name of the security relevant column |
| `COLUMN_OPTION` | `VARCHAR2(8)` |  | Option of the security relevant column: |

See Also:

- ["DBA\_SEC\_RELEVANT\_COLS"](statviews_4265.md)
- ["USER\_SEC\_RELEVANT\_COLS"](statviews_5443.md)