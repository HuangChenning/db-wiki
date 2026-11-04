---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_STREAMS_SCHEMA_RULES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.92 ALL\_STREAMS\_SCHEMA\_RULES

`ALL_STREAMS_SCHEMA_RULES` displays information about several types of schema rules.

`ALL_STREAMS_SCHEMA_RULES` displays information about these types of schema rules:

- Schema rules created for the capture processes that enqueue the captured changes into queues accessible to the current user
- Schema rules created for the propagations that have a source queue accessible to the current user
- Schema rules created for the apply processes that dequeue events from queues accessible to the current user

This view does not contain information about rules created using the `DBMS_RULE_ADM` package.

Related View

`DBA_STREAMS_SCHEMA_RULES` displays information about the schema rules created for all capture processes, propagations, and apply processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STREAMS_NAME` | `VARCHAR2(128)` |  | Name of the Replication process or propagation |
| `STREAMS_TYPE` | `VARCHAR2(11)` |  | Type of the Replication process or propagation:  - `CAPTURE` - `PROPAGATION` - `APPLY` |
| `SCHEMA_NAME` | `VARCHAR2(128)` |  | Schema name in the rule condition. The rule evaluates to `true` for a redo entry or logical change record (LCR) only if the redo entry or LCR contains this schema name. |
| `RULE_TYPE` | `VARCHAR2(7)` |  | Type of the rule:  - `DML` - `DDL` |
| `INCLUDE_TAGGED_LCR` | `VARCHAR2(3)` |  | Indicates whether a redo entry or logical change record (LCR) with a non-NULL tag is considered for capture, propagation, or apply (`YES`) or not (`NO`) |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | Source database in the rule condition. The rule evaluates to `true` for a redo entry or logical change record (LCR) only if the redo entry or LCR contains this source database. |
| `RULE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the rule |
| `RULE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the rule |
| `RULE_CONDITION` | `VARCHAR2(4000)` |  | First 4000 bytes of the system-generated rule condition evaluated by the rules engine |

See Also:

- " [DBA\_STREAMS\_SCHEMA\_RULES](DBA_STREAMS_SCHEMA_RULES.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS304) for more information about the `DBMS_RULE_ADM` package