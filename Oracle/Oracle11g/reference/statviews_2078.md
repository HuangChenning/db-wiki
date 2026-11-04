---
title: ALL_STREAMS_GLOBAL_RULES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2078.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_STREAMS_GLOBAL_RULES` displays information about the following types of rules:

- Global rules created for the Streams capture processes that enqueue the captured changes into queues accessible to the current user
- Global rules created for the Streams propagations that have a source queue accessible to the current user
- Global rules created for the Streams apply processes that dequeue events from queues accessible to the current user

This view only contains information about rules created using the `ADD_GLOBAL_RULES` or `ADD_GLOBAL_PROPAGATION_RULES` procedures in the `DBMS_STREAMS_ADM` package. It does not contain information about rules created using the `DBMS_RULE_ADM` package.

Related View

`DBA_STREAMS_GLOBAL_RULES` displays information about the global rules created for all Streams capture processes, propagations, and apply processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STREAMS_NAME` | `VARCHAR2(30)` |  | Name of the Streams process or propagation |
| `STREAMS_TYPE` | `VARCHAR2(11)` |  | Type of the Streams process or propagation: - `CAPTURE` - `PROPAGATION` - `APPLY` |
| `RULE_TYPE` | `VARCHAR2(7)` |  | Type of the rule: - `DML` - `DDL` |
| `INCLUDE_TAGGED_LCR` | `VARCHAR2(3)` |  | Indicates whether a redo entry or logical change record (LCR) with a non-NULL tag is considered for capture, propagation, or apply (`YES`) or not (`NO`) |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | Source database in the rule condition. The rule evaluates to `true` for a redo entry or logical change record (LCR) only if the redo entry or LCR contains this source database. |
| `RULE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rule |
| `RULE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rule |
| `RULE_CONDITION` | `VARCHAR2(4000)` |  | First 4000 bytes of the system-generated rule condition evaluated by the rules engine |

See Also:

["DBA\_STREAMS\_GLOBAL\_RULES"](statviews_5005.md)