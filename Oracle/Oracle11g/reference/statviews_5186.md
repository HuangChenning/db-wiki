---
title: SYSTEM_PRIVILEGE_MAP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5186.htm
tags:
  - oracle
  - 11g
  - reference
---

`SYSTEM_PRIVILEGE_MAP` describes privilege type codes. This table can be used to map privilege type numbers to type names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PRIVILEGE` | `NUMBER` | `NOT NULL` | Numeric privilege type code |
| `NAME` | `VARCHAR2(40)` | `NOT NULL` | Name of the type of privilege.  See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9013.htm#SQLRF55037) for a list of valid system privileges. |
| `PROPERTY` | `NUMBER` | `NOT NULL` | Property flag of the privilege |