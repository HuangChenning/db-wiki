---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/IDEPTREE.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.205 IDEPTREE

This view, created by `utldtree.sql`, lists the indented dependency tree. It is a pre-sorted, pretty-print version of `DEPTREE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NESTED_LEVEL` | `NUMBER` |  | Nesting level in the dependency tree |
| `TYPE` | `VARCHAR2(23)` |  | Object type |
| `OWNER` | `VARCHAR2(28)` |  | Object schema |
| `NAME` | `VARCHAR2(1002)` |  | Object name |