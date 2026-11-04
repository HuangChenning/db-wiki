---
title: SESSION_CONTEXT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5175.htm
tags:
  - oracle
  - 11g
  - reference
---

`SESSION_CONTEXT` describes the context attributes and their values set for the current session.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(30)` |  | Namespace that the active attribute is in |
| `ATTRIBUTE` | `VARCHAR2(30)` |  | Name of the active attribute |
| `VALUE` | `VARCHAR2(4000)` |  | Value of the active attribute |

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for information on the predefined attributes of the current session