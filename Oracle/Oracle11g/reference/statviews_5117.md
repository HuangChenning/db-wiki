---
title: DEPTREE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5117.htm
tags:
  - oracle
  - 11g
  - reference
---

This view, created by `utldtree.sql`, contains information on the object dependency tree. For user `SYS`, this view displays shared cursors (and only shared cursors) that depend on the object. For all other users, it displays objects other than shared cursors. Other users can access `SYS`.`DEPTREE` for information on shared cursors.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NESTED_LEVEL` | `NUMBER` |  | Nesting level in the dependency tree |
| `TYPE` | `VARCHAR2(15)` |  | Object type |
| `OWNER` | `VARCHAR2(30)` |  | Object owner |
| `NAME` | `VARCHAR2(1002)` |  | Object name |
| `SEQ#` | `NUMBER` |  | Sequence number in the dependency tree. Used for ordering queries.  See Also: ["IDEPTREE"](statviews_5141.md) |