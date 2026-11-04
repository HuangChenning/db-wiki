---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PUBLIC_DEPENDENCY.html
tags:
  - oracle
  - 12c
  - reference
---

`PUBLIC_DEPENDENCY` lists dependencies to and from objects, by object number.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_ID` | `NUMBER` | `NOT NULL` | Object number |
| `REFERENCED_OBJECT_ID` | `NUMBER` | `NOT NULL` | Referenced object (the parent object) |