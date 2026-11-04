---
title: USER_PASSWORD_LIMITS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5394.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_PASSWORD_LIMITS` describes the password profile parameters that are assigned to the user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Name of the password resource |
| `LIMIT` | `VARCHAR2(40)` |  | Value of the resource limit |