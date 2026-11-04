---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RULE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.202 V$RULE

`V$RULE` displays rule statistics. This view has a row for every rule loaded into shared memory.

| Column | Datatype | Description |
| --- | --- | --- |
| `RULE_SET_OBJECT_ID` | `NUMBER` | Rule set object ID |
| `EVALUATION_CONTEXT_OBJECT_ID` | `NUMBER` | Evaluation context object ID |
| `RULE_OWNER` | `VARCHAR2(128)` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(128)` | Name of the rule |
| `RULE_CONDITION` | `VARCHAR2(200)` | Rule condition |
| `TRUE_HITS` | `NUMBER` | Number of times the rule evaluated to `TRUE` |
| `MAYBE_HITS` | `NUMBER` | Number of times the rule evaluated to `MAYBE` |
| `SQL_EVALUATIONS` | `NUMBER` | Number of evaluations of the rule that were performed by issuing SQL |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |