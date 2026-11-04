---
title: DBA_RCHILD
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4195.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RCHILD` displays all the children in any refresh group.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REFGROUP` | `NUMBER` |  | Internal identifier of the refresh group |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object in the refresh group |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object in the refresh group |
| `TYPE#` | `VARCHAR2(30)` |  | Type of the object in the refresh group |