---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_LOGSTDBY_SKIP.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.168 DBA\_LOGSTDBY\_SKIP

`DBA_LOGSTDBY_SKIP` displays the skip rules that are used by SQL Apply.

This view is for logical standby databases only.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ERROR` | `VARCHAR2(1)` |  | Indicates how the skip rule was created:  - `Y` - For rules from `DBMS_LOGSTDBY.SKIP_ERROR` - `N` - For rules from `DBMS_LOGSTDBY.SKIP` |
| `STATEMENT_OPT` | `VARCHAR2(128)` |  | Specifies the type of statement that should be skipped |
| `OWNER` | `VARCHAR2(128)` |  | Name of the schema under which the skip option should be used |
| `NAME` | `VARCHAR2(261)` |  | Name of the object that is being skipped |
| `USE_LIKE` | `VARCHAR2(1)` |  | Indicates whether the statement should use a SQL wildcard search when matching names (`Y`) or not (`N`) |
| `ESC` | `VARCHAR2(1)` |  | Escape character used when performing wildcard matches |
| `PROC` | `VARCHAR2(392)` |  | Name of a stored procedure that will be executed when processing the skip option |

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS66855) for more information about the `DBMS_LOGSTDBY.SKIP_ERROR` procedure
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS66850) for more information about the `DBMS_LOGSTDBY.SKIP` procedure