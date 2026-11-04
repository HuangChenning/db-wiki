---
title: DROP CONTEXT
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8008.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `DROP` `CONTEXT` statement to remove a context namespace from the database.

Removing a context namespace does not invalidate any context under that namespace that has been set for a user session. However, the context will be invalid when the user next attempts to set that context.

See Also:

[CREATE CONTEXT](statements_5002.md) and [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/app_context.htm#DBSEG70071) for more information on contexts

Prerequisites

You must have the `DROP` `ANY` `CONTEXT` system privilege.

Syntax

drop\_context::=

  
[Description of the illustration ''drop\_context.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/drop_context.htm)  

Semantics

namespace

Specify the name of the context namespace to drop. You cannot drop the built-in namespace `USERENV`.

See Also:

[SYS\_CONTEXT](functions184.md) for information on the `USERENV` namespace

Examples

Dropping an Application Context: Example The following statement drops the context created in [CREATE CONTEXT](statements_5002.md):

```
DROP CONTEXT hr_context;
```