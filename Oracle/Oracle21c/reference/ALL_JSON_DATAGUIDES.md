---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_JSON_DATAGUIDES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.258 ALL\_JSON\_DATAGUIDES

`ALL_JSON_DATAGUIDES` provides information on the JavaScript Object Notation (JSON) columns accessible to the current user that have data guide enabled.

Related Views

- `DBA_JSON_DATAGUIDES` provides information on all JavaScript Object Notation (JSON) columns in the database that have data guide enabled.
- `USER_JSON_DATAGUIDES` provides information on the JavaScript Object Notation (JSON) columns owned by the current user that have data guide enabled. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table containing the JSON column |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table containing the JSON column |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the JSON column that has data guide enabled |
| `DATAGUIDE` | `CLOB` |  | The data guide of the JSON column in flat format |

See Also:

- " [DBA\_JSON\_DATAGUIDES](DBA_JSON_DATAGUIDES.md) "
- " [USER\_JSON\_DATAGUIDES](USER_JSON_DATAGUIDES.md) "