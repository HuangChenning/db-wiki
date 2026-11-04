---
title: USER_RESOURCE_LIMITS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5413.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_RESOURCE_LIMITS` displays the resource limits for the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE_NAME` | `VARCHAR2(32)` | `NOT NULL` | Name of the resource |
| `LIMIT` | `VARCHAR2(40)` |  | Limit placed on this resource |