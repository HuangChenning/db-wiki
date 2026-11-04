---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_PASSWORD_LIMITS.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_PASSWORD_LIMITS` describes the password profile parameters that are assigned to the user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Name of the password resource |
| `LIMIT` | `VARCHAR2(40)` |  | Value of the resource limit |