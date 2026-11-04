---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_LOGSTDBY_EDS_SUPPORTED.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_LOGSTDBY_EDS_SUPPORTED` lists the tables that are candidates for EDS-based replication for Logical Standby based on the data types they contain.

In a CDB, the data displayed pertains to the container in which the view is queried.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Table owner |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Table name |