---
title: ALL_XSTREAM_RULES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2146.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_XSTREAM_RULES` displays information about the XStream rules accessible to the current user.

Related View

`DBA_XSTREAM_RULES` displays information about all XStream server rules in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STREAMS_NAME` | `VARCHAR2(30)` |  | Name of the Streams process |
| `STREAMS_TYPE` | `VARCHAR2(12)` |  | Type of the Streams process: |
| `STREAMS_RULE_TYPE` | `VARCHAR2(6)` |  | The Streams type of the rule: |
| `RULE_SET_OWNER` | `VARCHAR2(30)` |  | Owner of the rule set |
| `RULE_SET_NAME` | `VARCHAR2(30)` |  | Name of the rule set |
| `RULE_SET_TYPE` | `CHAR(8)` |  | Type of the rule set: - `POSITIVE` - `NEGATIVE` |
| `RULE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rule |
| `RULE_TYPE` | `VARCHAR2(3)` |  | The type of the rule: - `DML` - `DDL` |
| `RULE_CONDITION` | `CLOB` |  | Current rule condition |
| `SCHEMA_NAME` | `VARCHAR2(30)` |  | For table and schema rules, the schema name |
| `OBJECT_NAME` | `VARCHAR2(30)` |  | For table rules, the table name |
| `INCLUDE_TAGGED_LCR` | `VARCHAR2(3)` |  | Indicates whether to include tagged LCRs (`YES`) or not (`NO`) |
| `SUBSETTING_OPERATION` | `VARCHAR2(6)` |  | For subset rules, the type of operation: - `INSERT` - `UPDATE` - `DELETE` |
| `DML_CONDITION` | `VARCHAR2(4000)` |  | For subset rules, the row subsetting condition |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | The name of the database where the LCRs originated |
| `ORIGINAL_RULE_CONDITION` | `VARCHAR2(4000)` |  | For rules created by Streams administrative APIs, the original rule condition when the rule was created |
| `SAME_RULE_CONDITION` | `VARCHAR2(3)` |  | For rules created by Streams administrative APIs, indicates whether the current rule condition is the same as the original rule condition (`YES`) or not (`NO`) |

See Also:

["DBA\_XSTREAM\_RULES"](statviews_5112.md)