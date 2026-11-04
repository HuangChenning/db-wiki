---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_PRIVILEGE_MAP.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.621 USER\_PRIVILEGE\_MAP

`USER_PRIVILEGE_MAP` shows privilege (auditing option) type codes for object privileges that can be granted on a user.

This table can be used to map privilege type numbers to type names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PRIVILEGE` | `NUMBER` | `NOT NULL` | A numeric privilege (auditing option) type code |
| `NAME` | `VARCHAR2(40)` | `NOT NULL` | Name of the type of privilege (auditing option) |