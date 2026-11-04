---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SYSTEM_PRIVILEGE_MAP.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.254 SYSTEM\_PRIVILEGE\_MAP

`SYSTEM_PRIVILEGE_MAP` describes privilege (auditing option) type codes.

This table can be used to map privilege (auditing option) type numbers to type names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PRIVILEGE` | `NUMBER` | `NOT NULL` | Numeric privilege (auditing option) type code |
| `NAME` | `VARCHAR2(40)` | `NOT NULL` | Name of the type of privilege (auditing option).  See [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF55037) for a list of valid system privileges. |
| `PROPERTY` | `NUMBER` | `NOT NULL` | Property flag of the privilege (auditing option):  - `0` - Indicates a privilege that can be granted with a SQL GRANT statement - `1` - Indicates a privilege that can only be granted using a PL/SQL package |