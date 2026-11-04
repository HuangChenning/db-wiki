---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_GOLDENGATE_RULES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.203 ALL\_GOLDENGATE\_RULES

`ALL_GOLDENGATE_RULES` displays information about the GoldenGate rules accessible to the current user.

Related View

`DBA_GOLDENGATE_RULES` displays information about all GoldenGate server rules in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPONENT_NAME` | `VARCHAR2(128)` |  | Name of the GoldenGate process |
| `COMPONENT_TYPE` | `VARCHAR2(12)` |  | Type of the GoldenGate process:  - `CAPTURE` - `APPLY` |
| `COMPONENT_RULE_TYPE` | `VARCHAR2(9)` |  | For global, schema or table rules, the GoldenGate type of the rule:  - `TABLE` - `SCHEMA` - `GLOBAL` |
| `RULE_SET_OWNER` | `VARCHAR2(128)` |  | Owner of the rule set |
| `RULE_SET_NAME` | `VARCHAR2(128)` |  | Name of the rule set |
| `RULE_SET_TYPE` | `CHAR(8)` |  | Type of the rule set:  - `POSITIVE` - `NEGATIVE` |
| `RULE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the rule |
| `RULE_TYPE` | `VARCHAR2(9)` |  | For global, schema or table rules, the type of the rule:  - `DML` - `DDL` |
| `RULE_CONDITION` | `VARCHAR2(1)` |  | This column is obsolete |
| `SCHEMA_NAME` | `VARCHAR2(128)` |  | For table and schema rules, the schema name |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | For table rules, the table name |
| `INCLUDE_TAGGED_LCR` | `VARCHAR2(3)` |  | For global, schema or table rules, indicates whether to include tagged LCRs (`YES`) or not (`NO`) |
| `SUBSETTING_OPERATION` | `VARCHAR2(6)` |  | For subset rules, the type of operation:  - `INSERT` - `UPDATE` - `DELETE` |
| `DML_CONDITION` | `VARCHAR2(4000)` |  | For subset rules, the row subsetting condition |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | For global, schema or table rules, the name of the database where the LCRs originated |
| `ORIGINAL_RULE_CONDITION` | `VARCHAR2(4000)` |  | For rules created by GoldenGate administrative APIs, the original rule condition when the rule was created |
| `SAME_RULE_CONDITION` | `VARCHAR2(3)` |  | For rules created by GoldenGate administrative APIs, indicates whether the current rule condition is the same as the original rule condition (`YES`) or not (`NO`) |
| `SOURCE_ROOT_NAME` | `VARCHAR2(128)` |  | The global name of the source root database where the transactions originated |
| `SOURCE_CONTAINER_NAME` | `VARCHAR2(128)` |  | The container name of the database where the transactions originated |

See Also:

" [DBA\_GOLDENGATE\_RULES](DBA_GOLDENGATE_RULES.md) "