---
title: ALL_REFS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2023.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_REFS` describes the `REF` columns and `REF` attributes in object type columns accessible to the current user.

Related Views

- `DBA_REFS` describes all `REF` columns and `REF` attributes in the database.
- `USER_REFS` describes the `REF` columns and `REF` attributes in object type columns owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the `REF` column or attribute. If it is not a top-level attribute, the value of `COLUMN_NAME` should be a path name starting with the column name. |
| `WITH_ROWID` | `VARCHAR2(3)` |  | Indicates whether the `REF` value is stored with `ROWID` (`YES`) or not (`NO`) |
| `IS_SCOPED` | `VARCHAR2(3)` |  | Indicates whether the `REF` column is scoped (`YES`) or not (`NO`) |
| `SCOPE_TABLE_OWNER` | `VARCHAR2(30)` |  | Owner of the scope table, if it exists and is accessible by the user |
| `SCOPE_TABLE_NAME` | `VARCHAR2(30)` |  | Name of the scope table, if it exists and is accessible by the user |
| `OBJECT_ID_TYPE` | `VARCHAR2(33)` |  | Indicates whether the object ID (OID) is `USER-DEFINED` or `SYSTEM GENERATED` |