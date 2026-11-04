---
title: "V$RULE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2165.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RULE` displays rule statistics. This view has a row for every rule loaded into shared memory.

| Column | Datatype | Description |
| --- | --- | --- |
| `RULE_SET_OBJECT_ID` | `NUMBER` | Rule set object ID |
| `EVALUATION_CONTEXT_OBJECT_ID` | `NUMBER` | Evaluation context object ID |
| `RULE_OWNER` | `VARCHAR2(30)` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(30)` | Name of the rule |
| `RULE_CONDITION` | `VARCHAR2(200)` | Rule condition |
| `TRUE_HITS` | `NUMBER` | Number of times the rule evaluated to `TRUE` |
| `MAYBE_HITS` | `NUMBER` | Number of times the rule evaluated to `MAYBE` |
| `SQL_EVALUATIONS` | `NUMBER` | Number of evaluations of the rule that were performed by issuing SQL |