---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_RESOURCE_LIMITS.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_RESOURCE_LIMITS` displays the resource limits for the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Name of the resource |
| `LIMIT` | `VARCHAR2(40)` |  | Limit placed on this resource |