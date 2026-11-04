---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/PUBLIC_DEPENDENCY.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.220 PUBLIC\_DEPENDENCY

`PUBLIC_DEPENDENCY` lists dependencies to and from objects, by object number.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_ID` | `NUMBER` | `NOT NULL` | Object number |
| `REFERENCED_OBJECT_ID` | `NUMBER` | `NOT NULL` | Referenced object (the parent object) |