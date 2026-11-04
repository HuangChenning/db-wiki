---
title: ALL_STREAMS_TRANSFORM_FUNCTION
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2087.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_STREAMS_TRANSFORM_FUNCTION` displays information about the rule-based transformation functions accessible to the current user.

Related View

`DBA_STREAMS_TRANSFORM_FUNCTION` displays information about all rule-based transformation functions in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rule associated with the transformation function |
| `RULE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rule associated with the transformation function |
| `VALUE_TYPE` | `VARCHAR2(4000)` |  | Type of the transformation function name. This type must be `VARCHAR2` for a rule-based transformation to work properly. |
| `TRANSFORM_FUNCTION_NAME` | `VARCHAR2(4000)` |  | Name of the transformation function (NULL if `VALUE_TYPE` is not `VARCHAR2`) |
| `CUSTOM_TYPE` | `VARCHAR2(11)` |  | Type of the transformation function: |

See Also:

- ["DBA\_STREAMS\_TRANSFORM\_FUNCTION"](statviews_5026.md)
- [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_transform.htm#STRMS160) for more information about custom rule-based transformation