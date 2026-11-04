---
title: "V$AW_AGGREGATE_OP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1038.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$AW_AGGREGATE_OP` displays the aggregation operators available in analytic workspaces. You can use this view in an application to provide a list of choices.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(14)` | Keyword for the aggregation operator |
| `LONGNAME` | `VARCHAR2(30)` | Descriptive name for the operator |
| `DEFAULT_WEIGHT` | `NUMBER` | Default weight factor for weighted operators |