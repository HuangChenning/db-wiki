---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/RESOURCE_MAP.html
tags:
  - oracle
  - 12c
  - reference
---

`RESOURCE_MAP` describes resources. This table can be used to map resource names to resource numbers.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE#` | `NUMBER` | `NOT NULL` | Numeric resource code |
| `TYPE#` | `NUMBER` | `NOT NULL` | Numeric type code |
| `NAME ` | `VARCHAR2(32)` | `NOT NULL` | Name of the resource |