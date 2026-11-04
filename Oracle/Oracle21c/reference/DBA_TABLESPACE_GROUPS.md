---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_TABLESPACE_GROUPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.47 DBA\_TABLESPACE\_GROUPS

`DBA_TABLESPACE_GROUPS` describes all tablespace groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace group |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace |