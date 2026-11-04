---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/DROP-SYNONYM.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## DROP SYNONYM

Purpose

Use the `DROP` `SYNONYM` statement to remove a synonym from the database or to change the definition of a synonym by dropping and re-creating it.

See Also:

[CREATE SYNONYM](CREATE-SYNONYM.md) for more information on synonyms

Prerequisites

To drop a private synonym, either the synonym must be in your own schema or you must have the `DROP` `ANY` `SYNONYM` system privilege.

To drop a `PUBLIC` synonym, you must have the `DROP` `PUBLIC` `SYNONYM` system privilege.

Syntax

drop\_synonym::=

drop\_synonym::=

![drop_synonym](img/drop_synonym.gif)

> ```
> DROP [PUBLIC] SYNONYM [ schema. ] synonym [FORCE] ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

PUBLIC

You must specify `PUBLIC` to drop a public synonym. You cannot specify `schema` if you have specified `PUBLIC`.

schema

Specify the schema containing the synonym. If you omit `schema`, then Oracle Database assumes the synonym is in your own schema.

synonym

Specify the name of the synonym to be dropped.

If you drop a synonym for the master table of a materialized view, and if the defining query of the materialized view specified the synonym rather than the actual table name, then Oracle Database marks the materialized view unusable.

If an object type synonym has any dependent tables or user-defined types, then you cannot drop the synonym unless you also specify `FORCE`.

FORCE

Specify `FORCE` to drop the synonym even if it has dependent tables or user-defined types.

Note:

Oracle does not recommend that you specify `FORCE` to drop object type synonyms with dependencies. This operation can result in invalidation of other user-defined types or marking `UNUSED` the table columns that depend on the synonym. For information about type dependencies, see [Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=ADOBJ00402).

Examples

Dropping a Synonym: Example

To drop the public synonym named `customers`, which was created in " [Oracle Database Resolution of Synonyms: Example](CREATE-SYNONYM.md) ", issue the following statement:

```
DROP PUBLIC SYNONYM customers;
```