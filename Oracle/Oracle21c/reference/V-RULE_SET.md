---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RULE_SET.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.203 V$RULE\_SET

`V$RULE_SET` displays rule set statistics. This view has a row for every rule set loaded into shared memory.

Note:

Querying the `V$RULE_SET` view may have a negative impact on performance if a database has a large library cache.

| Column | Datatype | Description |
| --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | Owner of the rule set |
| `NAME` | `VARCHAR2(128)` | Name of the rule set |
| `CPU_TIME` | `NUMBER` | Total CPU time (in hundredths of a second) spent in evaluation of the rule set |
| `ELAPSED_TIME` | `NUMBER` | Total elapsed time (in hundredths of a second) spent in evaluation of the rule set |
| `FIRST_LOAD_TIME` | `DATE` | First time the current cached copy of the rule set was loaded |
| `LAST_LOAD_TIME` | `DATE` | Last time the current cached copy of the rule set was loaded |
| `LAST_LOADING_TIME` | `NUMBER` | Total elapsed time (in hundredths of a second) spent to load the rule set the last time it was loaded |
| `SHARABLE_MEM` | `NUMBER` | Shared memory (in bytes) used by the rule set |
| `RELOADS` | `NUMBER` | Number of times the rule set object was reloaded in shared memory |
| `INVALIDATIONS` | `NUMBER` | Number of times the rule set object was invalidated |
| `EVALUATIONS` | `NUMBER` | Number of evaluations on the rule set |
| `FIRST_HIT_EVALUATIONS` | `NUMBER` | Number of evaluations on the rule set, with `stop_on_first_hit` set to `TRUE` |
| `SIMPLE_RULES_ONLY_EVALUATIONS` | `NUMBER` | Number of evaluations on the rule set, with `simple_rules_only` set to `TRUE` |
| `SQL_FREE_EVALUATIONS` | `NUMBER` | Number of evaluations on the rule set which did not internally issue SQL to evaluate rules |
| `SQL_EXECUTIONS` | `NUMBER` | Total number of SQL statements executed during evaluation of the rule set |
| `CONDITIONS_PROCESSED` | `NUMBER` | Total number of fast (indexed) conditions processed during evaluation of the rule set |
| `TRUE_RULES` | `NUMBER` | Total number of `TRUE` rules returned during evaluation of the rule set |
| `MAYBE_RULES` | `NUMBER` | Total number of `MAYBE` rules returned during evaluation of the rule set |
| `VARIABLE_VALUE_FUNCTION_CALLS` | `NUMBER` | Total number of calls made to user-defined functions to retrieve variable values (specified by the `variable_value_function` field in `RE$VARIABLE_TYPE`) made during evaluation of the rule set |
| `VARIABLE_METHOD_FUNCTION_CALLS` | `NUMBER` | Total number of calls made to user-defined functions to retrieve variable method values (specified by the `variable_method_function` field in `RE$VARIABLE_TYPE`) made during evaluation of the rule set |
| `EVALUATION_FUNCTION_CALLS` | `NUMBER` | Total number of calls made to user-defined evaluation functions (specified as the `evaluation_function` argument to the `DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT` procedure) made during evaluation of the rule set |
| `RESULT_CACHE_HITS` | `NUMBER` | Number of result cache hits across all the sessions evaluating this rule set |
| `IS_RESULT_CACHE` | `VARCHAR2(3)` | Indicates whether this rule set result can be cached (`YES`) or not (`NO`) |
| `RESULT_CACHE_ELEMENTS` | `NUMBER` | Number of elements cached within the result cache |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS327) for more information about the `DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT` procedure