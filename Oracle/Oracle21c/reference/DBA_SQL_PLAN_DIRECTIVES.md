---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SQL_PLAN_DIRECTIVES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.368 DBA\_SQL\_PLAN\_DIRECTIVES

`DBA_SQL_PLAN_DIRECTIVES` displays information about the SQL plan directives in the system.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DIRECTIVE_ID` | `NUMBER` | `NOT NULL` | The identifier of the SQL plan directive |
| `TYPE` | `VARCHAR2(16)` |  | The type of the SQL plan directive:  - `DYNAMIC SAMPLING`: SQL plan directive - `DYNAMIC SAMPLING RESULT`: Dynamic sampling query results. This value appears only in Oracle Database 12c Release 2 (12.2.0.1) and later releases. - `UNKNOWN`: Unknown |
| `ENABLED` | `VARCHAR2(3)` |  | Indicates whether the SQL plan directive is enabled. Possible values:  - `YES`: The SQL plan directive is enabled. - `NO`: The SQL plan directive is not enabled. |
| `STATE` | `VARCHAR2(10)` |  | The state of the SQL plan directive. Possible values include:  - `SUPERSEDED`: This value indicates that the corresponding column or groups have an extension or histogram, or that another SQL plan directive exists that can be used for the directive. - `USABLE`: This value indicates that the SQL plan directive is usable for the optimizer. |
| `AUTO_DROP` | `VARCHAR2(3)` |  | If `YES`, the SQL plan directive gets dropped when unused beyond `SPD_RETENTION_WEEKS` |
| `REASON` | `VARCHAR2(36)` |  | The reason for creating the SQL plan directive |
| `CREATED` | `TIMESTAMP(6)` |  | The creation timestamp of the SQL plan directive |
| `LAST_MODIFIED` | `TIMESTAMP(6)` |  | The timestamp of most recent modification of the SQL plan directive |
| `LAST_USED` | `TIMESTAMP(9)` |  | The timestamp of most recent usage of the SQL plan directive |
| `NOTES` | `XMLTYPE` |  | Extra information about the SQL plan directive |

See Also:

- " [DBA\_SQL\_PLAN\_DIR\_OBJECTS](DBA_SQL_PLAN_DIR_OBJECTS.md) "
- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL347) for more information about SQL plan directives