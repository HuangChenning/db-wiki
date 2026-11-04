---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/USER_PASSWORD_LIMITS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.597 USER\_PASSWORD\_LIMITS

`USER_PASSWORD_LIMITS` describes the password profile parameters that are assigned to the user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Name of the password resource |
| `LIMIT` | `VARCHAR2(40)` |  | Value of the resource limit |