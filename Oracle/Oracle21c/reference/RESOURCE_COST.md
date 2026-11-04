---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESOURCE_COST.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.234 RESOURCE\_COST

`RESOURCE_COST` lists the cost for each resource.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Name of the resource |
| `UNIT_COST` | `NUMBER` | `NOT NULL` | Cost of the resource |