---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/JSON_TRANSFORM.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## JSON\_TRANSFORM

Syntax

![json_transform](img/json_transform.gif)

> ```
> JSON_TRANSFORM ( input_expr , operation [ , operation ]...
>     [ JSON_passing_clause ] 
>     [ JSON_TRANSFORM_returning_clause ] )
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


JSON\_TRANSFORM\_returning\_clause::=

![json_transform_returning_clause](img/json_transform_returning_clause.gif)

> ```
> RETURNING ( 
>      VARCHAR2 [ ( size [BYTE | CHAR] ) ]
>      | CLOB
>      | BLOB
>      | JSON
>     )
>    [ (ALLOW | DISALLOW) ]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


JSON\_passing\_clause::=

For details on `JSON_passing_clause` see [JSON\_EXISTS Condition](SQL-JSON-Conditions.md).

operation::=

![operation](img/operation.gif)

> ```
> removeOp
> | insertOp
> | replaceOp 
> | appendOp
> | setOp
> | renameOp
> | keepOp
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


removeOp::=

![remove_op](img/remove_op.gif)

> ```
> REMOVE pathExpr [ (IGNORE | ERROR) ON MISSING ]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


insertOp::=

![insert_op](img/insert_op.gif)

> ```
> INSERT pathExpr = rhsExpr [ ( REPLACE | IGNORE | ERROR) ON EXISTING ]
>      [ ( NULL | IGNORE | ERROR | REMOVE ) ON NULL ]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


replaceOp::=

![replace_op](img/replace_op.gif)

> ```
> REPLACE pathExpr = rhsExpr [ ( CREATE | IGNORE | ERROR) ON MISSING ]
>     [ ( NULL | IGNORE | ERROR | REMOVE ) ON NULL ]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


rhsExpr::=

![rhs_expr](img/rhs_expr.gif)

> ```
> sqlExpr [ FORMAT JSON ]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


appendOp::=

![append_op](img/append_op.gif)

> ```
> APPEND pathExpr = rhsExpr [ ( CREATE | IGNORE | ERROR) ON MISSING ]
>     [ ( NULL | IGNORE | ERROR) ON NULL ]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


setOp::=

![set_op](img/set_op.gif)

> ```
> SET pathExpr = rhsExpr [ (IGNORE | ERROR | REPLACE) ON EXISTING ]
>     [ ( CREATE | IGNORE | ERROR) ON MISSING ] [ ( NULL | IGNORE | ERROR) ON NULL ]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


renameOp::=

![rename_op](img/rename_op.gif)

> ```
> RENAME pathExpr WITH stringLiteral [ (IGNORE | ERROR) ON MISSING ]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


keepOp::=

![keep_op](img/keep_op.gif)

> ```
> KEEP ( pathExpr [( IGNORE | ERROR ) ON MISSING ] ) ...
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Purpose

You can use the `JSON_TRANSFORM ` function to change input JSON data (or pieces of JSON data), by specifying one or more modifying operations that perform changes to the JSON data. You will get the modified JSON as output.

The input to the function is a SQL expression that contains a JSON value. For example, the input can be a `JSON` type instance, a `VARCHAR2` column with or without an `IS JSON` check constraint, or a function call returning JSON data.

Examples

Example 1: Update a JSON Column with a Timestamp

```
UPDATE t SET jcol = JSON_TRANSFORM(jcol, SET '$.lastUpdated' = SYSTIMESTAMP)
```

Example 2: Remove a Social Security Number before Shipping JSON to a Client

```
SELECT JSON_TRANSFORM (jcol, REMOVE '$.ssn') FROM t WHERE …
```

JSON\_TRANSFORM\_returning\_clause

If the input data is JSON, then the output data type is also JSON. For all other input types, the default output data type is `VARCHAR2(4000)`.

For a fuller discussion of `JSON_TRANSFORM ` with examples, see [Oracle SQL Function JSON\_TRANSFORM](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=ADJSN-GUID-7BED994B-EAA3-4FF0-824D-C12ADAB862C1).