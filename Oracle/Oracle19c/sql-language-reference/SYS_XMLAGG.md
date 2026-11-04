---
title: SYS_XMLAGG
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/SYS_XMLAGG.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![sys_xmlagg](img/sys_xmlagg.gif)

> ```
> SYS_XMLAGG(expr [, fmt ])
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration sys\_xmlagg.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/sys_xmlagg.html)

## Purpose

`SYS_XMLAgg` aggregates all of the XML documents or fragments represented by *expr* and produces a single XML document. It adds a new enclosing element with a default name `ROWSET`. If you want to format the XML document differently, then specify *fmt*, which is an instance of the `XMLFormat` object.

**See Also:** [SYS\_XMLGEN](SYS_XMLGEN.md) and “ [XML Format Model](Format-Models.md) ” for using the attributes of the `XMLFormat` type to format `SYS_XMLAgg` results

## Examples

The following example uses the `SYS_XMLGen` function to generate an XML document for each row of the sample table `employees` where the employee’s last name begins with the letter R, and then aggregates all of the rows into a single XML document in the default enclosing element `ROWSET`:

```md
SELECT SYS_XMLAGG(SYS_XMLGEN(last_name)) XMLAGG
   FROM employees
   WHERE last_name LIKE 'R%'
   ORDER BY xmlagg;

XMLAGG
--------------------------------------------------------------------------------
<?xml version="1.0"?>
<ROWSET>
<LAST_NAME>Rajs</LAST_NAME>
<LAST_NAME>Raphaely</LAST_NAME>
<LAST_NAME>Rogers</LAST_NAME>
<LAST_NAME>Russell</LAST_NAME>
</ROWSET>
```