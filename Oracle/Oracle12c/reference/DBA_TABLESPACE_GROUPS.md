---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_TABLESPACE_GROUPS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_TABLESPACE_GROUPS` describes all tablespace groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace group |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace |