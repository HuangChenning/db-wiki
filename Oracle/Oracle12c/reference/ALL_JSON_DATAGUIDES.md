---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_JSON_DATAGUIDES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_JSON_DATAGUIDES` provides information on the JavaScript Object Notation (JSON) columns accessible to the current user that have data guide enabled.

Related Views

- `DBA_JSON_DATAGUIDES` provides information on the JavaScript Object Notation (JSON) columns in the database that have data guide enabled. Its columns are the same as those in `ALL_JSON_DATAGUIDES`.
- `USER_JSON_DATAGUIDES` provides information on the JavaScript Object Notation (JSON) columns owned by the current user that have data guide enabled. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table containing the JSON column |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table containing the JSON column |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the JSON column that has data guide enabled |
| `DATAGUIDE` | `CLOB` |  | The data guide of the JSON column in flat format |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_JSON\_DATAGUIDES](DBA_JSON_DATAGUIDES.md) "
- " [USER\_JSON\_DATAGUIDES](USER_JSON_DATAGUIDES.md) "