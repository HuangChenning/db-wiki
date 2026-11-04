---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/GLOBAL_CONTEXT.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.190 GLOBAL\_CONTEXT

`GLOBAL_CONTEXT` displays the values of global context attributes, which are accessible for the current session, based on the `CLIENT_IDENTIFIER` value.

`GLOBAL_CONTEXT` is similar to `SESSION_CONTEXT`, which lists the values of session (or local) context attributes set under the current session.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(31)` |  | Namespace of the globally accessible context |
| `ATTRIBUTE` | `VARCHAR2(31)` |  | Attribute of the globally accessible context |
| `VALUE` | `VARCHAR2(4000)` |  | Value of the attribute of the globally accessible context |
| `USERNAME` | `VARCHAR2(31)` |  | Username for which globally accessible context value is applicable |
| `CLIENT_IDENTIFIER` | `VARCHAR2(65)` |  | Client identifier of the globally accessible context |

See Also:

- " [SESSION\_CONTEXT](SESSION_CONTEXT.md) "
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG70005) for more information about using global application contexts