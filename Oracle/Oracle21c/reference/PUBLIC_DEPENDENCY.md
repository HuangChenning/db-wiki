---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PUBLIC_DEPENDENCY.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.223 PUBLIC\_DEPENDENCY

`PUBLIC_DEPENDENCY` lists dependencies to and from objects, by object number.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_ID` | `NUMBER` | `NOT NULL` | Object number |
| `REFERENCED_OBJECT_ID` | `NUMBER` | `NOT NULL` | Referenced object (the parent object) |