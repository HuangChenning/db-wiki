---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_STREAMS_RULES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_STREAMS_RULES` displays information about the rules used by the Streams processes accessible to the current user.

Related View

`DBA_STREAMS_RULES` displays information about the rules used by all Streams processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STREAMS_TYPE` | `VARCHAR2(12)` |  | Type of the Streams process:  - `CAPTURE` - `PROPAGATION` - `APPLY` - `DEQUEUE` - `SYNC_CAPTURE` |
| `STREAMS_NAME` | `VARCHAR2(128)` |  | Name of the Streams process |
| `RULE_SET_OWNER` | `VARCHAR2(128)` |  | Owner of the rule set |
| `RULE_SET_NAME` | `VARCHAR2(128)` |  | Name of the rule set |
| `RULE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the rule |
| `RULE_CONDITION` | `CLOB` |  | Current rule condition |
| `RULE_SET_TYPE` | `CHAR(8)` |  | Type of the rule set:  - `POSITIVE` - `NEGATIVE` |
| `STREAMS_RULE_TYPE` | `VARCHAR2(9)` |  | For global, schema, or table rules, the type of the rule:  - `TABLE` - `SCHEMA` - `GLOBAL` |
| `SCHEMA_NAME` | `VARCHAR2(128)` |  | For table and schema rules, the schema name |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | For table rules, the table name |
| `SUBSETTING_OPERATION` | `VARCHAR2(6)` |  | For subset rules, the type of operation:  - `INSERT` - `UPDATE` - `DELETE` |
| `DML_CONDITION` | `VARCHAR2(4000)` |  | For subset rules, the row subsetting condition |
| `INCLUDE_TAGGED_LCR` | `VARCHAR2(3)` |  | For global, schema, or table rules, indicates whether to include tagged logical change records (LCRs) (`YES`) or not (`NO`) |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | For global, schema, or table rules, the global name of the database where the logical change records (LCRs) originated |
| `RULE_TYPE` | `VARCHAR2(9)` |  | For global, schema, or table rules, the type of the rule:  - `DML` - `DDL` |
| `MESSAGE_TYPE_OWNER` | `VARCHAR2(128)` |  | For message rules, the owner of the message type |
| `MESSAGE_TYPE_NAME` | `VARCHAR2(128)` |  | For message rules, the name of the message type |
| `MESSAGE_RULE_VARIABLE` | `VARCHAR2(128)` |  | For message rules, the name of the variable in the message rule |
| `ORIGINAL_RULE_CONDITION` | `VARCHAR2(4000)` |  | For rules created by Streams administrative APIs, the original rule condition when the rule was created |
| `SAME_RULE_CONDITION` | `VARCHAR2(3)` |  | For rules created by Streams administrative APIs, indicates whether the current rule condition is the same as the original rule condition (`YES`) or not (`NO`) |

See Also:

" [DBA\_STREAMS\_RULES](DBA_STREAMS_RULES.md) "