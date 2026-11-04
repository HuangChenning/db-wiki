---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_CPU_USAGE_STATISTICS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_CPU_USAGE_STATISTICS` displays database CPU usage statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `VERSION` | `VARCHAR2(17)` | `NOT NULL` | Database version |
| `TIMESTAMP` | `DATE` | `NOT NULL` | Time at which the CPU usage changed |
| `CPU_COUNT` | `NUMBER` |  | CPU count of the database |
| `CPU_CORE_COUNT` | `NUMBER` |  | CPU core count of the database |
| `CPU_SOCKET_COUNT` | `NUMBER` |  | CPU socket count of the database |