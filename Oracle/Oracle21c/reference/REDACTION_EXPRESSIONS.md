---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/REDACTION_EXPRESSIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.228 REDACTION\_EXPRESSIONS

`REDACTION_EXPRESSIONS` shows all the Data Redaction named Policy Expressions in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `POLICY_EXPRESSION_NAME` | `VARCHAR2(256)` |  | Customer-specified name of the named Policy Expression |
| `EXPRESSION` | `VARCHAR2(4000)` |  | The SQL expression defined for this Data Redaction named Policy Expression |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Owner of the table or view which this named Policy Expression is associated with |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the table or view which this named Policy Expression is associated with |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the column which this named Policy Expression is associated with |
| `POLICY_EXPRESSION_DESCRIPTION` | `VARCHAR2(4000)` |  | Description of this named Policy Expression |

See Also:

[Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ASOAG10135) for more information about Oracle Data Redaction