---
title: RESOURCE_COST
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5167.htm
tags:
  - oracle
  - 11g
  - reference
---

`RESOURCE_COST` lists the cost for each resource.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Name of the resource |
| `UNIT_COST` | `NUMBER` | `NOT NULL` | Cost of the resource |