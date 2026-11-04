---
title: "V$CPOOL_CC_INFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1091.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$CPOOL_CC_INFO` displays information about the pool-to-connection class mapping for the Database Resident Connection Pool per instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `POOL_NAME` | `VARCHAR2(1024)` | Name of the Database Resident Connection Pool |
| `CCLASS_NAME` | `VARCHAR2(1024)` | Name of the connection class |