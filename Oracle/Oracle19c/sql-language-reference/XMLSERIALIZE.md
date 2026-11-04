---
title: XMLSERIALIZE
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/XMLSERIALIZE.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![xmlserialize](img/xmlserialize.gif)

> ```
> XMLSERIALIZE
>   ( { DOCUMENT | CONTENT } value_expr [ AS datatype ]
>     [ ENCODING xml_encoding_spec ]
>     [ VERSION string_literal ]
>     [ NO INDENT | { INDENT [SIZE = number] } ]
>     [ { HIDE | SHOW } DEFAULTS ]
>   )
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration xmlserialize.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/xmlserialize.html)

## Purpose

`XMLSerialize` creates a string or LOB containing the contents of *value\_expr*.

Any lob returned by `XMLSERIALIZE` will be read-only.

- If you specify `DOCUMENT`, then the *value\_expr* must be a valid XML document.
- If you specify `CONTENT`, then the *value\_expr* need not be a singly rooted XML document. However it must be valid XML content.
- The *datatype* specified can be a string type (`VARCHAR2` or `VARCHAR`, but not `NVARCHAR2`), `BLOB`, or `CLOB`. The default is `CLOB`.
- If *datatype* is `BLOB`, then you can specify the `ENCODING` clause to use the specified encoding in the prolog. The *xml\_encoding\_spec* is an XML encoding declaration (`encoding="..."`).
- Specify the `VERSION` clause to use the version you provide as *string\_literal* in the XML declaration (`<?xml version="..." ...?>`).
- Specify `NO` `INDENT` to strip all insignificant whitespace from the output. Specify `INDENT SIZE = ` *N*, where *N* is a whole number, for output that is pretty-printed using a relative indentation of *N* spaces. If *N* is `0`, then pretty-printing inserts a newline character after each element, placing each element on a line by itself, but omitting all other insignificant whitespace in the output. If `INDENT` is present without a `SIZE` specification, then 2-space indenting is used. If you omit this clause, then the behavior (pretty-printing or not) is indeterminate.
- `HIDE DEFAULTS` and `SHOW DEFAULTS` apply only to XML schema-based data. If you specify `SHOW DEFAULTS` and the input data is missing any optional elements or attributes for which the XML schema defines default values, then those elements or attributes are included in the output with their default values. If you specify `HIDE DEFAULTS`, then no such elements or attributes are included in the output. `HIDE DEFAULTS` is the default behavior.

**See Also:**

- [*Oracle XML DB Developer’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=ADXDB1620) for more information on this function
- in [*Oracle Database Globalization Support Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules, which define the collation assigned to the character return value of `XMLSERIALIZE`

## Examples

The following statement uses the `DUAL` table to illustrate the syntax of `XMLSerialize`:

```md
SELECT XMLSERIALIZE(CONTENT XMLTYPE('<Owner>Grandco</Owner>')) AS xmlserialize_doc
   FROM DUAL;

XMLSERIALIZE_DOC
----------------
<Owner>Grandco</Owner>
```