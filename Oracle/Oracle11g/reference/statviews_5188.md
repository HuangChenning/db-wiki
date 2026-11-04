---
title: TABLE_PRIVILEGE_MAP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5188.htm
tags:
  - oracle
  - 11g
  - reference
---

`TABLE_PRIVILEGE_MAP` describes privilege (auditing option) type codes. This table can be used to map privilege (auditing option) type numbers to type names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PRIVILEGE` | `NUMBER` | `NOT NULL` | Numeric privilege (auditing option) type code |
| `NAME` | `VARCHAR2(40)` | `NOT NULL` | Name of the type of privilege (auditing option) |