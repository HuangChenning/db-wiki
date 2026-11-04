---
title: "V$RULE_SET_AGGREGATE_STATS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2167.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RULE_SET_AGGREGATE_STATS` displays statistics aggregated over all evaluations on all rule sets. This view has a row for each type of statistic.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(80)` | Name of the statistic: - `rule set evaluations (all)` - Total number of evaluations on all rule sets - `rule set evaluations (first_hit)` - Total number of evaluations on rule sets with `stop_on_first_hit` set to `TRUE` - `rule set evaluations (simple_rules_only)` - Total number of evaluations on rule sets with `simple_rules_only` set to `TRUE` - `rule set evaluations (SQL free)` - Total number of evaluations on rule sets which did not internally issue SQL to evaluate rules - `rule set evaluation time (CPU)` - Total CPU time (in hundredths of a second) spent in evaluations on rule sets - `rule set evaluation time (elapsed)` - Total elapsed time (in hundredths of a second) spent in evaluations on rule sets - `rule set SQL executions` - Total number of SQL statements executed during evaluations on rule sets - `rule set conditions processed` - Total number of fast (indexed) conditions processed during evaluations on rule sets - `rule set true rules` - Total number of `TRUE` rules returned during evaluations on rule sets - `rule set maybe rules` - Total number of `MAYBE` rules returned during evaluations on rule sets - `rule set user function calls (variable value function)` - Total number of calls made to user-defined functions to retrieve variable values (specified by the `variable_value_function` field in `RE$VARIABLE_TYPE`) made during evaluations on rule sets - `rule set user function calls (variable method function)` - Total number of calls made to user-defined functions to retrieve variable method values (specified by the `variable_method_function` field in `RE$VARIABLE_TYPE`) made during evaluations on rule sets - `rule set user function calls (evaluation function)` - Total number of calls made to user-defined evaluation functions (specified as the `evaluation_function` argument to the `DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT` procedure) made during evaluations on rule sets |
| `VALUE` | `NUMBER` | Statistic value |