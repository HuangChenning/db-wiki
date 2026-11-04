---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DEPTREE.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.180 DEPTREE

This view, created by `utldtree.sql`, contains information on the object dependency tree.

For user `SYS`, this view displays shared cursors (and only shared cursors) that depend on the object. For all other users, it displays objects other than shared cursors. Other users can access `SYS`.`DEPTREE` for information on shared cursors.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NESTED_LEVEL` | `NUMBER` |  | Nesting level in the dependency tree |
| `TYPE` | `VARCHAR2(23)` |  | Object type |
| `SCHEMA` | `VARCHAR2(128)` |  | Object schema |
| `NAME` | `VARCHAR2(1002)` |  | Object name |
| `SEQ#` | `NUMBER` |  | Sequence number in the dependency tree. Used for ordering queries.  See Also: " [IDEPTREE](IDEPTREE.md) " |