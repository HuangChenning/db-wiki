---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/XMLTABLE.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## XMLTABLE

Syntax

![xmltable](img/xmltable.gif)

> ```
> XMLTABLE
>  ( 
>   [ XMLnamespaces_clause , ] XQuery_string XMLTABLE_options 
>  )
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


XMLnamespaces\_clause::=

![xmlnamespaces_clause](img/xmlnamespaces_clause.gif)

> ```
> XMLNAMESPACES
>   ( { string AS identifier } | { DEFAULT string }
>       [, { string AS identifier } | { DEFAULT string } ]...
>   )
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Note:

You can specify at most one `DEFAULT` `string` clause.

XMLTABLE\_options::=

![xmltable_options](img/xmltable_options.gif)

> ```
> [ XML_passing_clause ]
> [ RETURNING SEQUENCE BY REF ]
> [ COLUMNS XML_table_column [, XML_table_column]...]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


XML\_passing\_clause::=

![xml_passing_clause](img/xml_passing_clause.gif)

> ```
> PASSING [ BY VALUE ] 
>     expr [ AS identifier ]
>       [, expr [ AS identifier ] 
>       ]...
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


XML\_table\_column::=

![xml_table_column](img/xml_table_column.gif)

> ```
> column
>   { FOR ORDINALITY 
>   | { datatype | XMLTYPE [ (SEQUENCE) BY REF ] }
>     [ PATH string ] [ DEFAULT expr ]
>   }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Purpose

`XMLTable` maps the result of an XQuery evaluation into relational rows and columns. You can query the result returned by the function as a virtual relational table using SQL.

- The `XMLNAMESPACES` clause contains a set of XML namespace declarations. These declarations are referenced by the XQuery expression (the evaluated `XQuery_string`), which computes the row, and by the XPath expression in the `PATH` clause of `XML_table_column`, which computes the columns for the entire `XMLTable` function. If you want to use qualified names in the `PATH` expressions of the `COLUMNS` clause, then you need to specify the `XMLNAMESPACES` clause.
- `XQuery_string` is a literal string. It is a complete XQuery expression and can include prolog declarations. The value of XQuery\_string serves as input to the XMLTable function; it is this XQuery result that is decomposed and stored as relational data.
- The `expr` in the `XML_passing_clause` is an expression returning an `XMLType` or an instance of a SQL scalar data type that is used as the context for evaluating the XQuery expression. You can specify only one `expr` in the `PASSING` clause without an identifier. The result of evaluating each `expr` is bound to the corresponding identifier in the `XQuery_string`. If any `expr` that is not followed by an `AS` clause, then the result of evaluating that expression is used as the context item for evaluating the `XQuery_string`. This clause supports only passing by value, not passing by reference. Therefore, the `BY` `VALUE` keywords are optional and are provided for semantic clarity.
- The optional `RETURNING` `SEQUENCE` `BY` `REF` clause causes the result of the XQuery evaluation to be returned by reference. This allows you to refer to any part of the source data in the `XML_table_column` clause.
	If you omit this clause, then the result of the XQuery evaluation is returned by value. That is, a copy of the targeted nodes is returned instead of a reference to the actual nodes. In this case, you cannot refer to any data that is not in the returned copy in the `XML_table_column` clause. In particular, you cannot refer to data that precedes the targeted nodes in the source data.
- The optional `COLUMNS` clause defines the columns of the virtual table to be created by `XMLTable`.
	- If you omit the `COLUMNS` clause, then `XMLTable` returns a row with a single `XMLType` pseudocolumn named `COLUMN_VALUE`.
		- `FOR` `ORDINALITY` specifies that `column` is to be a column of generated row numbers. There must be at most one `FOR` `ORDINALITY` clause. It is created as a `NUMBER` column.
		- For each resulting column except the `FOR` `ORDINALITY` column, you must specify the column data type, which can be `XMLType` or any other data type.
		If the column data type is `XMLType`, then specify the `XMLTYPE` clause. If you specify the optional `(SEQUENCE)` `BY` `REF` clause, then a reference to the source data targeted by the `PATH` expression is returned as the column content. Otherwise, `column` contains a copy of that targeted data.
		Returning the `XMLType` data by reference lets you specify other columns whose paths target nodes in the source data that are outside those targeted by the `PATH` expression for column.
		If the column data type is any other data type, then specify `datatype`.
		- The optional `PATH` clause specifies that the portion of the XQuery result that is addressed by XQuery expression string is to be used as the column content.
		If you omit `PATH`, then the XQuery expression `column` is assumed. For example:
		```
		XMLTable(... COLUMNS xyz)
		```
		is equivalent to
		```
		XMLTable(... COLUMNS xyz PATH 'XYZ')
		```
		You can use different `PATH` clauses to split the XQuery result into different virtual-table columns.
		- The optional `DEFAULT` clause specifies the value to use when the `PATH` expression results in an empty sequence. Its `expr` is an XQuery expression that is evaluated to produce the default value.

See Also:

- [Oracle XML DB Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=ADXDB1700) for more information on the `XMLTable` function, including additional examples, and on XQuery in general
- Appendix C in [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules, which define the collation assigned to each character data type column in the table generated by `XMLTABLE`

Examples

The following example converts the result of applying the XQuery `'/Warehouse'` to each value in the `warehouse_spec` column of the `warehouses` table into a virtual relational table with columns `Water` and `Rail`:

```
SELECT warehouse_name warehouse,
   warehouse2."Water", warehouse2."Rail"
   FROM warehouses,
   XMLTABLE('/Warehouse'
      PASSING warehouses.warehouse_spec
      COLUMNS 
         "Water" varchar2(6) PATH 'WaterAccess',
         "Rail" varchar2(6) PATH 'RailAccess') 
      warehouse2;

WAREHOUSE                           Water  Rail
----------------------------------- ------ ------
Southlake, Texas                    Y      N
San Francisco                       Y      N
New Jersey                          N      N
Seattle, Washington                 N      Y
```