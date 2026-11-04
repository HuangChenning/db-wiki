---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_ADVISOR_OBJECT_TYPES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_ADVISOR_OBJECT_TYPES` displays information about the object types used by all advisors in the database.

In addition to the regular database object types (such as `TABLE` and `INDEX`), the following types are defined:

- `SYSTEM`
- `I/O`
- `SGA`
- `PGA`
- `SHARED POOL`
- `BUFFER CACHE`
- `LIBRARY CACHE`
- `PROCESS`
- `SESSION`
- `ENQUEUE`
- `LATCH`
- `ROLLBACK SEGMENT`
- `FILE`
- `PARAMETER`
- `CURSOR`
- `SQL`
- `SQL WORKLOAD`

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_TYPE_ID` | `NUMBER` |  | Type identifier |
| `OBJECT_TYPE` | `VARCHAR2(64)` |  | Type name |