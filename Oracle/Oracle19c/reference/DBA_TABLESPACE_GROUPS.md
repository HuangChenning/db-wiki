---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_TABLESPACE_GROUPS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.46 DBA\_TABLESPACE\_GROUPS

`DBA_TABLESPACE_GROUPS` describes all tablespace groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace group |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace |