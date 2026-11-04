---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_RESOURCE_LIMITS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.635 USER\_RESOURCE\_LIMITS

`USER_RESOURCE_LIMITS` displays the resource limits for the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Name of the resource |
| `LIMIT` | `VARCHAR2(40)` |  | Limit placed on this resource |