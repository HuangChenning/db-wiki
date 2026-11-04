---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_JSON_DATAGUIDE_FIELDS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.257 ALL\_JSON\_DATAGUIDE\_FIELDS

`ALL_JSON_DATAGUIDE_FIELDS` extracts the path and type information from the data guides accessible to the current user, which are the data guides returned to the user by the `ALL_JSON_DATAGUIDE` view.

Related Views

- `DBA_JSON_DATAGUIDE_FIELDS` extracts the path and type information from all the data guides in the database, which are the data guides returned by the `DBA_JSON_DATAGUIDE` view.
- `USER_JSON_DATAGUIDE_FIELDS` extracts the path and type information from all the data guides in the current user’s schema, which are the data guides returned to the user by the `USER_JSON_DATAGUIDE` view. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table containing the JSON column |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table containing the JSON column |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the JSON column that has data guide enabled |
| `PATH` | `VARCHAR2(4000)` |  | Path to the JSON field in the data guide |
| `TYPE` | `VARCHAR2(40)` |  | Type of the JSON field in the data guide |
| `LENGTH` | `NUMBER` |  | Maximum length of the JSON field value, in bytes |