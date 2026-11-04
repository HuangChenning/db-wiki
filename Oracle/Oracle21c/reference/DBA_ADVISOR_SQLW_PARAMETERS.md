---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_SQLW_PARAMETERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.45 DBA\_ADVISOR\_SQLW\_PARAMETERS

`DBA_ADVISOR_SQLW_PARAMETERS` displays all workload parameters and their current values in the database.

Related View

`USER_ADVISOR_SQLW_PARAMETERS` displays the workload parameters and their current values owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task or workload object |
| `WORKLOAD_ID` | `NUMBER` | `NOT NULL` | Unique identifier number of the workload object |
| `WORKLOAD_NAME` | `VARCHAR2(128)` |  | Name of the workload object |
| `PARAMETER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the parameter |
| `PARAMETER_VALUE` | `VARCHAR2(4000)` | `NOT NULL` | Value of the parameter. Numeric parameter values are converted to a string equivalent.  Possible keywords as values:  - `ALL` - `UNLIMITED` - `UNUSED` |
| `PARAMETER_TYPE` | `VARCHAR2(10)` |  | Datatype of the parameter:  - `NUMBER` - Numeric value - `STRING` - String value. If the string contains special characters, then it will be enclosed in single quotes. - `STRINGLIST` - Comma-separated list of string elements. If a string element contains a comma or other special characters, then the element will be enclosed in single quotes. - `TABLE` - Single table reference. A reference contains a schema name, followed by an optional table name. 	If the table name is omitted or is the character `%`, then the table name is interpreted as a wildcard. SQL quoted identifiers are supported. - `TABLELIST` - List of one or more comma-separated table references. A reference contains a schema name, followed by an optional table name. 	If the table name is omitted or is the character `%`, then the table name is interpreted as a wildcard. SQL quoted identifiers are supported. |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Parameter description |

See Also:

" [USER\_ADVISOR\_SQLW\_PARAMETERS](USER_ADVISOR_SQLW_PARAMETERS.md) "