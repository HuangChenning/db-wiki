---
title: AUDIT_ACTIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2147.htm
tags:
  - oracle
  - 11g
  - reference
---

`AUDIT_ACTIONS` describes audit trail action type codes. This table can be used to map action type numbers to action type names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ACTION` | `NUMBER` | `NOT NULL` | Numeric audit trail action type code. |
| `NAME` | `VARCHAR2(28)` | `NOT NULL` | Name of the type of audit trail action |