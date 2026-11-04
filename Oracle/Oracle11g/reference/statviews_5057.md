---
title: DBA_TABLESPACE_GROUPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5057.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_TABLESPACE_GROUPS` describes all tablespace groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace group |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace |