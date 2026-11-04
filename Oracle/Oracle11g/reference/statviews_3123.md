---
title: DBA_CPU_USAGE_STATISTICS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3123.htm
tags:
  - oracle
  - 11g
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