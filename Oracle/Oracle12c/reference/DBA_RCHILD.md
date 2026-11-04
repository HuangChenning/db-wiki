---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_RCHILD.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_RCHILD` displays all the children in any refresh group.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REFGROUP` | `NUMBER` |  | Internal identifier of the refresh group |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object in the refresh group |
| `NAME ` | `VARCHAR2(128)` | `NOT NULL` | Name of the object in the refresh group |
| `TYPE#` | `VARCHAR2(128)` |  | Type of the object in the refresh group |