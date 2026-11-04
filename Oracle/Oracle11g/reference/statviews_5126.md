---
title: GLOBAL_CONTEXT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5126.htm
tags:
  - oracle
  - 11g
  - reference
---

`GLOBAL_CONTEXT` displays the values of global context attributes, which are accessible for the current session, based on the `CLIENT_IDENTIFIER` value. This view is similar to `SESSION_CONTEXT`, which lists the values of session (or local) context attributes set under the current session.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(31)` |  | Namespace of the globally accessible context |
| `ATTRIBUTE` | `VARCHAR2(31)` |  | Attribute of the globally accessible context |
| `VALUE` | `VARCHAR2(4000)` |  | Value of the attribute of the globally accessible context |
| `USERNAME` | `VARCHAR2(31)` |  | Username for which globally accessible context value is applicable |
| `CLIENT_IDENTIFIER` | `VARCHAR2(65)` |  | Client identifier of the globally accessible context |

See Also:

- ["SESSION\_CONTEXT"](statviews_5175.md)
- [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/app_context.htm#DBSEG70005) for more information about using global application contexts