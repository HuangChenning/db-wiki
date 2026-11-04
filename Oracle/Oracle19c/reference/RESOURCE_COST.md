---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/RESOURCE_COST.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.231 RESOURCE\_COST

`RESOURCE_COST` lists the cost for each resource.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Name of the resource |
| `UNIT_COST` | `NUMBER` | `NOT NULL` | Cost of the resource |