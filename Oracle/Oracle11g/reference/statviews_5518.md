---
title: XS_SESSION_ROLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5518.htm
tags:
  - oracle
  - 11g
  - reference
---

`XS_SESSION_ROLES` describes the enabled roles in the current lightweight user session for the current request.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROLE` | `VARCHAR2(1025)` |  | Name of the role |
| `UUID` | `VARCHAR2(33)` |  | UUID of the role |
| `DBID` | `NUMBER` |  | Database ID of the role |
| `FLAGS` | `NUMBER` |  | Status flags |