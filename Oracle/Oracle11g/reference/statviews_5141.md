---
title: IDEPTREE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5141.htm
tags:
  - oracle
  - 11g
  - reference
---

This view, created by `utldtree.sql`, lists the indented dependency tree. It is a pre-sorted, pretty-print version of `DEPTREE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NESTED_LEVEL` | `NUMBER` |  | Nesting level in the dependency tree |
| `TYPE` | `VARCHAR2(15)` |  | Object type |
| `OWNER` | `VARCHAR2(30)` |  | Object owner |
| `NAME` | `VARCHAR2(1002)` |  | Object name |