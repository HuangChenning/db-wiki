---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_STREAMS_TRANSFORM_FUNCTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.94 ALL\_STREAMS\_TRANSFORM\_FUNCTION

`ALL_STREAMS_TRANSFORM_FUNCTION` displays information about the rule-based transformation functions accessible to the current user.

Related View

`DBA_STREAMS_TRANSFORM_FUNCTION` displays information about all rule-based transformation functions in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the rule associated with the transformation function |
| `RULE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the rule associated with the transformation function |
| `VALUE_TYPE` | `VARCHAR2(4000)` |  | Type of the transformation function name. This type must be `VARCHAR2` for a rule-based transformation to work properly. |
| `TRANSFORM_FUNCTION_NAME` | `VARCHAR2(4000)` |  | Name of the transformation function (NULL if `VALUE_TYPE` is not `VARCHAR2`) |
| `CUSTOM_TYPE` | `VARCHAR2(11)` |  | Type of the transformation function:  - `ONE TO ONE` - One-to-one transformations - `ONE TO MANY` - One-to-many transformations |

See Also:

" [DBA\_STREAMS\_TRANSFORM\_FUNCTION](DBA_STREAMS_TRANSFORM_FUNCTION.md) "