---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_LOGSTDBY_EDS_TABLES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_LOGSTDBY_EDS_TABLES` lists the tables that have EDS-based replication for Logical Standby.

In a CDB, the data displayed pertains to the container in which the view is queried.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Schema name of supportable table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Table name of supportable table |
| `CTIME` | `TIMESTAMP(6)` |  | Time that the table had EDS added |