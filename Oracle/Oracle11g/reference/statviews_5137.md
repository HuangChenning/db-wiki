---
title: HS_FDS_INST
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5137.htm
tags:
  - oracle
  - 11g
  - reference
---

`HS_FDS_INST` contains information about non-Oracle (FDS) instances.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FDS_INST_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the FDS instance |
| `FDS_INST_COMMENTS` | `VARCHAR2(255)` |  | Text description of the non-Oracle instance |
| `FDS_CLASS_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the FDS class |
| `FDS_INST_ID` | `NUMBER` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |
| `FDS_CLASS_ID` | `NUMBER` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |