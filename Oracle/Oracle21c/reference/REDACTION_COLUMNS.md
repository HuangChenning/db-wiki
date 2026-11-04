---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/REDACTION_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.227 REDACTION\_COLUMNS

`REDACTION_COLUMNS` describes all redacted columns in the database, giving the owner of the table or view within which the column resides, the object name, the column name, the type of redaction function, the parameters to the redaction function (if any), and an optional user-provided description of the redaction function that is performed on the column.

| Column | Datatype | NULL | ullDescription |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object that is redacted |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object that is redacted |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the column that is redacted |
| `FUNCTION_TYPE` | `VARCHAR2(27)` |  | Redaction function for this column |
| `FUNCTION_PARAMETERS` | `VARCHAR2(1000)` |  | Redaction function\_parameters for this column |
| `REGEXP_PATTERN` | `VARCHAR2(512)` |  | Regular expression pattern to search for |
| `REGEXP_REPLACE_STRING` | `VARCHAR2(4000)` |  | Replacement string (up to 4000 characters in length) with up to 500 back-references to subexpressions in the form `\n`, (where `n` is a number from 1 to 9) |
| `REGEXP_POSITION` | `NUMBER` |  | Integer counting from 1, giving the position where the search should begin |
| `REGEXP_OCCURRENCE` | `NUMBER` |  | Either `0` (to replace all occurrences of the match), or a positive integer `n` (to replace the `n` th occurrence of the match) |
| `REGEXP_MATCH_PARAMETER` | `VARCHAR2(10)` |  | To change the default matching behavior, possible values are a combination of `i`, `c`, `n`, `m`, and `x`. See the documentation of the `match_parameter` in the `REGEXP_REPLACE` section of the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF06302). |
| `COLUMN_DESCRIPTION` | `VARCHAR2(4000)` |  | User-provided description of the redaction function that is performed on the column. For example, for a Social Security Number column, the description might be: "redact SSN to XXX-XX-(last 4 digits)". |

See Also:

[Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ASOAG10135) for more information about Oracle Data Redaction