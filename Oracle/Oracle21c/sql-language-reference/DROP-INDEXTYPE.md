---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/DROP-INDEXTYPE.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## DROP INDEXTYPE

Purpose

Use the `DROP` `INDEXTYPE` statement to drop an indextype as well as any association with a statistics type.

See Also:

[CREATE INDEXTYPE](CREATE-INDEXTYPE.md) for more information on indextypes

Prerequisites

The indextype must be in your own schema or you must have the `DROP` `ANY` `INDEXTYPE` system privilege.

Syntax

drop\_indextype::=

![drop_indextype](img/drop_indextype.gif)

> ```
> DROP INDEXTYPE [ schema. ] indextype [ FORCE ] ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

schema

Specify the schema containing the indextype. If you omit `schema`, then Oracle Database assumes the indextype is in your own schema.

indextype

Specify the name of the indextype to be dropped.

If any statistics types have been associated with indextype, then the database disassociates the statistics type from the indextype and drops any statistics that have been collected using the statistics type.

See Also:

[ASSOCIATE STATISTICS](ASSOCIATE-STATISTICS.md) and [DISASSOCIATE STATISTICS](DISASSOCIATE-STATISTICS.md) for more information on statistics associations

FORCE

Specify `FORCE` to drop the indextype even if the indextype is currently being referenced by one or more domain indexes. Oracle Database marks those domain indexes `INVALID`. Without `FORCE`, you cannot drop an indextype if any domain indexes reference the indextype.

Examples

Dropping an Indextype: Example

The following statement drops the indextype `position_indextype`, created in " [Using Extensible Indexing](Using-Extensible-Indexing.md) ", and marks `INVALID` any domain indexes defined on this indextype:

```
DROP INDEXTYPE position_indextype FORCE;
```