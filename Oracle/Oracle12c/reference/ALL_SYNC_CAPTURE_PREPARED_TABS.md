---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_SYNC_CAPTURE_PREPARED_TABS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_SYNC_CAPTURE_PREPARED_TABS` displays information about the tables accessible to the current user that are prepared for synchronous capture instantiation.

Related View

`DBA_SYNC_CAPTURE_PREPARED_TABS` displays information about all tables in the database that are prepared for synchronous capture instantiation.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table prepared for synchronous capture instantiation |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table prepared for synchronous capture instantiation |
| `SCN` | `NUMBER` | `NOT NULL` | SCN from which changes can be captured |
| `TIMESTAMP` | `DATE` |  | Time at which the table was ready to be instantiated |

See Also:

" [DBA\_SYNC\_CAPTURE\_PREPARED\_TABS](DBA_SYNC_CAPTURE_PREPARED_TABS.md) "