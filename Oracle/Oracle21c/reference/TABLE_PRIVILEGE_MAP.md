---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/TABLE_PRIVILEGE_MAP.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.257 TABLE\_PRIVILEGE\_MAP

`TABLE_PRIVILEGE_MAP` describes privilege (auditing option) type codes.

This table can be used to map privilege (auditing option) type numbers to type names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PRIVILEGE` | `NUMBER` | `NOT NULL` | Numeric privilege (auditing option) type code |
| `NAME ` | `VARCHAR2(40)` | `NOT NULL` | Name of the type of privilege (auditing option) |