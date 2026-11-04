---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/DROP-CONTEXT.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Purpose

Use the `DROP` `CONTEXT` statement to remove a context namespace from the database.

Removing a context namespace does not invalidate any context under that namespace that has been set for a user session. However, the context will be invalid when the user next attempts to set that context.

See Also:

[CREATE CONTEXT](CREATE-CONTEXT.md) and [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sqlrf&id=DBSEG70071) for more information on contexts

Prerequisites

You must have the `DROP` `ANY` `CONTEXT` system privilege.

Syntax

drop\_context::=

![drop_context](img/drop_context.gif)

> ```
> DROP CONTEXT namespace ;
> ```


Semantics

namespace

Specify the name of the context namespace to drop. You cannot drop the built-in namespace `USERENV`.

See Also:

[SYS\_CONTEXT](SYS_CONTEXT.md) for information on the `USERENV` namespace

Examples

Dropping an Application Context: Example

The following statement drops the context created in [CREATE CONTEXT](CREATE-CONTEXT.md):

```
DROP CONTEXT hr_context;
```