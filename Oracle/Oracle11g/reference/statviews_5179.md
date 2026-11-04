---
title: STMT_AUDIT_OPTION_MAP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5179.htm
tags:
  - oracle
  - 11g
  - reference
---

`STMT_AUDIT_OPTION_MAP` describes auditing option type codes. This table can be used to map auditing option type numbers to type names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OPTION#` | `NUMBER` | `NOT NULL` | Numeric auditing option type code |
| `NAME` | `VARCHAR2(40)` | `NOT NULL` | Name of the type of auditing option |
| `PROPERTY` | `NUMBER` | `NOT NULL` | Property flag of the auditing option |