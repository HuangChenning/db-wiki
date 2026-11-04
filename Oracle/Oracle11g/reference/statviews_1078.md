---
title: ALL_DIRECTORIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1078.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_DIRECTORIES` describes all directories accessible to the current user.

Related View

`DBA_DIRECTORIES` describes all directories in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the directory (always `SYS`) |
| `DIRECTORY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the directory |
| `DIRECTORY_PATH` | `VARCHAR2(4000)` |  | Operating system pathname for the directory |