---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_RCHILD.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.264 DBA\_RCHILD

`DBA_RCHILD` displays all the children in any refresh group.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REFGROUP` | `NUMBER` |  | Internal identifier of the refresh group |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object in the refresh group |
| `NAME ` | `VARCHAR2(128)` | `NOT NULL` | Name of the object in the refresh group |
| `TYPE#` | `VARCHAR2(128)` |  | Type of the object in the refresh group |