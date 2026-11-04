---
title: "V$AW_ALLOCATE_OP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1039.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$AW_ALLOCATE_OP` displays the allocation operators available in analytic workspaces. You can use this view in an application to provide a list of choices.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(14)` | Keyword for the allocation operator |
| `LONGNAME` | `VARCHAR2(30)` | Descriptive name for the operator |