---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/DROP-DATABASE-LINK.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Purpose

Use the `DROP` `DATABASE` `LINK` statement to remove a database link from the database.

See Also:

[CREATE DATABASE LINK](CREATE-DATABASE-LINK.md) for information on creating database links

Prerequisites

A private database link must be in your own schema. To drop a `PUBLIC` database link, you must have the `DROP` `PUBLIC` `DATABASE` `LINK` system privilege.

Syntax

drop\_database\_link::=

![drop_database_link](img/drop_database_link.gif)

> ```
> DROP [ PUBLIC ] DATABASE LINK dblink ;
> ```


Semantics

PUBLIC

You must specify `PUBLIC` to drop a `PUBLIC` database link.

dblink

Specify the name of the database link to be dropped.

Restriction on Dropping Database Links

You cannot drop a database link in another user's schema, and you cannot qualify `dblink` with the name of a schema, because periods are permitted in names of database links. Therefore, Oracle Database interprets the entire name, such as `ralph.linktosales`, as the name of a database link in your schema rather than as a database link named `linktosales` in the schema `ralph`.

Examples

Dropping a Database Link: Example

The following statement drops the public database link named `remote`, which was created in " [Defining a Public Database Link: Example](CREATE-DATABASE-LINK.md) ":

```
DROP PUBLIC DATABASE LINK remote;
```