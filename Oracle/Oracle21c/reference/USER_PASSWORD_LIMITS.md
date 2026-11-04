---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_PASSWORD_LIMITS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.610 USER\_PASSWORD\_LIMITS

`USER_PASSWORD_LIMITS` describes the password profile parameters that are assigned to the user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Name of the password resource |
| `LIMIT` | `VARCHAR2(40)` |  | Value of the resource limit |