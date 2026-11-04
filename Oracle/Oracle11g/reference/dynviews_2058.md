---
title: "V$MAP_SUBELEMENT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2058.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MAP_SUBELEMENT` displays a list of all subelement mapping structures in the shared memory of the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `CHILD_IDX` | `NUMBER` | Index in `V$MAP_ELEMENT` corresponding to the child element |
| `PARENT_IDX` | `NUMBER` | Index in `V$MAP_ELEMENT` corresponding to the parent element |
| `SUB_NUM` | `NUMBER` | Subelement number |
| `SUB_SIZE` | `NUMBER` | Subelement size in HKB |
| `ELEM_OFFSET` | `NUMBER` | Offset in HKB on the child element |
| `SUB_FLAGS` | `NUMBER` | Subelement flags (currently unused) |