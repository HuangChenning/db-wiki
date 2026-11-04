---
title: DBA_OPTSTAT_OPERATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4165.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_OPTSTAT_OPERATIONS` contains a history of statistics operations performed at the schema and database level using the `DBMS_STATS` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OPERATION` | `VARCHAR2(64)` |  | Operation name |
| `TARGET` | `VARCHAR2(64)` |  | Target on which the operation was performed |
| `START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time at which the operation started |
| `END_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time at which the operation ended |