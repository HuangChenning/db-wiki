---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/RESOURCE_MAP.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.232 RESOURCE\_MAP

`RESOURCE_MAP` describes resources. This table can be used to map resource names to resource numbers.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE#` | `NUMBER` | `NOT NULL` | Numeric resource code |
| `TYPE#` | `NUMBER` | `NOT NULL` | Numeric type code |
| `NAME ` | `VARCHAR2(32)` | `NOT NULL` | Name of the resource |