---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_GOLDENGATE_NOT_UNIQUE.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.346 DBA\_GOLDENGATE\_NOT\_UNIQUE

`DBA_GOLDENGATE_NOT_UNIQUE` displays all tables that have no primary and no non-null unique indexes.

Most of the tables displayed by this view are supported because their columns contain enough information to be maintained by Oracle GoldenGate. Some tables, however, cannot be supported because their columns do not contain the necessary information. Unsupported tables usually contain a column defined using an unsupported data type.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Schema name of the non-unique table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Table name of the non-unique table |
| `BAD_COLUMN` | `VARCHAR2(1)` |  | Indicates that the table has a column not useful in the where clause. Possible values:  - `Y` - Table column is defined using an unbounded data type, such as `LONG` or `BLOB`. If two rows in the table match except in their LOB columns, then the table cannot be maintained properly. Log apply services will attempt to maintain these tables, but you must ensure the application does not allow uniqueness only in the unbounded columns. - `N` - Enough column information is present to maintain the table in Oracle GoldenGate but the log transport services and log apply services would run more efficiently if you added a primary key. You should consider adding a disabled `RELY` constraint to these tables. |