---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESOURCE_MAP.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.235 RESOURCE\_MAP

`RESOURCE_MAP` describes resources. This table can be used to map resource names to resource numbers.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE#` | `NUMBER` | `NOT NULL` | Numeric resource code |
| `TYPE#` | `NUMBER` | `NOT NULL` | Numeric type code |
| `NAME ` | `VARCHAR2(32)` | `NOT NULL` | Name of the resource |