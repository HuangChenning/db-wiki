---
title: "V$ACTIVE_INSTANCES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1004.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ACTIVE_INSTANCES` displays the mapping between instance names and instance numbers for all instances that have the database currently mounted.

| Column | Datatype | Description |
| --- | --- | --- |
| `INST_NUMBER` | `NUMBER` | Instance number |
| `INST_NAME` | `VARCHAR2(60)` | Instance name |