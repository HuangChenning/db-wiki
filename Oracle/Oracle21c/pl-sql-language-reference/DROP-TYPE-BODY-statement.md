---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/DROP-TYPE-BODY-statement.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The `DROP` `TYPE` `BODY` statement drops the body of an ADT, `VARRAY` type, or nested table type.

When you drop a type body, the type specification still exists, and you can re-create the type body. Prior to re-creating the body, you can still use the type, although you cannot invoke its member functions.

Topics

Prerequisites

The type body must be in your schema or you must have the `DROP` `ANY` `TYPE` system privilege.

Syntax

drop\_type\_body::=

![drop_type_body](img/drop_type_body.gif)

> ```
> DROP TYPE BODY [ schema. ] type_name ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

schema

Name of the schema containing the type. Default: your schema.

type\_name

Name of the type body to be dropped.

Restriction on type\_name

You can drop a type body only if it has no type or table dependencies.

Example

Example 15-41 Dropping an ADT Body

This statement removes the ADT body `data_typ1`. See " [CREATE TYPE Statement](CREATE-TYPE-statement.md) " for the example that creates this ADT.

```
DROP TYPE BODY data_typ1;
```