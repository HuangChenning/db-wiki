---
title: ALL_STREAMS_RULES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2082.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_STREAMS_RULES` displays information about the rules used by the Streams processes accessible to the current user.

Related View

`DBA_STREAMS_RULES` displays information about the rules used by all Streams processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STREAMS_TYPE` | `VARCHAR2(12)` |  | Type of the Streams process: |
| `STREAMS_NAME` | `VARCHAR2(30)` |  | Name of the Streams process |
| `RULE_SET_OWNER` | `VARCHAR2(30)` |  | Owner of the rule set |
| `RULE_SET_NAME` | `VARCHAR2(30)` |  | Name of the rule set |
| `RULE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rule |
| `RULE_CONDITION` | `CLOB` |  | Current rule condition |
| `RULE_SET_TYPE` | `CHAR(8)` |  | Type of the rule set: - `POSITIVE` - `NEGATIVE` |
| `STREAMS_RULE_TYPE` | `VARCHAR2(6)` |  | For global, schema, or table rules, the type of the rule: - `TABLE` - `SCHEMA` - `GLOBAL` |
| `SCHEMA_NAME` | `VARCHAR2(30)` |  | For table and schema rules, the schema name |
| `OBJECT_NAME` | `VARCHAR2(30)` |  | For table rules, the table name |
| `SUBSETTING_OPERATION` | `VARCHAR2(6)` |  | For subset rules, the type of operation: - `INSERT` - `UPDATE` - `DELETE` |
| `DML_CONDITION` | `VARCHAR2(4000)` |  | For subset rules, the row subsetting condition |
| `INCLUDE_TAGGED_LCR` | `VARCHAR2(3)` |  | For global, schema, or table rules, indicates whether to include tagged logical change records (LCRs) (`YES`) or not (`NO`) |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | For global, schema, or table rules, the name of the database where the logical change records (LCRs) originated |
| `RULE_TYPE` | `VARCHAR2(3)` |  | For global, schema, or table rules, the type of the rule: - `DML` - `DDL` |
| `MESSAGE_TYPE_OWNER` | `VARCHAR2(30)` |  | For message rules, the owner of the message type |
| `MESSAGE_TYPE_NAME` | `VARCHAR2(30)` |  | For message rules, the name of the message type |
| `MESSAGE_RULE_VARIABLE` | `VARCHAR2(30)` |  | For message rules, the name of the variable in the message rule |
| `ORIGINAL_RULE_CONDITION` | `VARCHAR2(4000)` |  | For rules created by Streams administrative APIs, the original rule condition when the rule was created |
| `SAME_RULE_CONDITION` | `VARCHAR2(3)` |  | For rules created by Streams administrative APIs, indicates whether the current rule condition is the same as the original rule condition (`YES`) or not (`NO`) |

See Also:

["DBA\_STREAMS\_RULES"](statviews_5013.md)