---
title: ALL_OPANCILLARY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1160.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_OPANCILLARY` describes operators whose bindings are ancillary to other (primary) operators.

Related Views

- `DBA_OPANCILLARY` describes such information about all operators in the database.
- `USER_OPANCILLARY` describes such information about operators owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the ancillary operator |
| `OPERATOR_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the ancillary operator |
| `BINDING#` | `NUMBER` | `NOT NULL` | Binding number the of ancillary operator |
| `PRIMOP_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the primary operator |
| `PRIMOP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the primary operator |
| `PRIMOP_BIND#` | `NUMBER` | `NOT NULL` | Binding number of the primary operator |