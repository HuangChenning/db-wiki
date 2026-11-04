---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/USER_RESOURCE_LIMITS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.621 USER\_RESOURCE\_LIMITS

`USER_RESOURCE_LIMITS` displays the resource limits for the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Name of the resource |
| `LIMIT` | `VARCHAR2(40)` |  | Limit placed on this resource |