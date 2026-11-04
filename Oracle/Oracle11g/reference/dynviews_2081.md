---
title: "V$OBSOLETE_PARAMETER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2081.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$OBSOLETE_PARAMETER` displays information about obsolete initialization parameters. If any row of the view contains `TRUE` in the `ISSPECIFIED` column, then you should examine why.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(64)` | Name of the parameter |
| `ISSPECIFIED` | `VARCHAR2(5)` | Indicates whether the parameter was specified in the parameter file (`TRUE`) or not (`FALSE`) |