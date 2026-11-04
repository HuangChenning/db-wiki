---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADDM_TASK_DIRECTIVES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.16 DBA\_ADDM\_TASK\_DIRECTIVES

`DBA_ADDM_TASK_DIRECTIVES` displays information about all ADDM task directives in the database.

Related View

`USER_ADDM_TASK_DIRECTIVES` displays information about ADDM task directives owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER` |  | An ADDM advisor task identifier to which the directive instance is associated |
| `TASK_NAME` | `VARCHAR2(128)` |  | An ADDM advisor task to which the directive instance is associated |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | Database user who owns the ADDM task instance |
| `SEQ_ID` | `NUMBER` | `NOT NULL` | Unique ID for the directive instance. The directive management engine automatically generates ID numbers. |
| `INSTANCE_NAME` | `VARCHAR2(128)` | `NOT NULL` | A user-assigned name for the ADDM task directive instance |
| `DIRECTIVE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Any value that further classifies this directive within a domain. The domain and the name form a unique key for the directive. |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Description of the ADDM task directive, shown in the language used by the current session |

See Also:

" [USER\_ADDM\_TASK\_DIRECTIVES](USER_ADDM_TASK_DIRECTIVES.md) "