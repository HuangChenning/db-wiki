---
title: DBA_HIST_DATABASE_INSTANCE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3215.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_DATABASE_INSTANCE` displays the databases and instances in the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number |
| `STARTUP_TIME` | `TIMESTAMP(3)` | `NOT NULL` | Startup time of the instance |
| `PARALLEL` | `VARCHAR2(3)` | `NOT NULL` | Indicates whether the instance is running in an Oracle Real Application Clusters (Oracle RAC) environment (`YES`) or not (`NO`) |
| `VERSION` | `VARCHAR2(17)` | `NOT NULL` | Database version |
| `DB_NAME` | `VARCHAR2(9)` |  | Name of the database |
| `INSTANCE_NAME` | `VARCHAR2(16)` |  | Name of the instance |
| `HOST_NAME` | `VARCHAR2(64)` |  | Name of the host |
| `LAST_ASH_SAMPLE_ID` | `NUMBER` | `NOT NULL` | Last sample ID for the active session history |