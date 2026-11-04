---
title: XMLCONCAT
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/XMLCONCAT.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![xmlconcat](img/xmlconcat.gif)

> ```
> XMLCONCAT(XMLType_instance [, XMLType_instance ]...)
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration xmlconcat.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/xmlconcat.html)

## Purpose

`XMLConcat` takes as input a series of `XMLType` instances, concatenates the series of elements for each row, and returns the concatenated series. `XMLConcat` is the inverse of `XMLSequence`.

Null expressions are dropped from the result. If all the value expressions are null, then the function returns null.

**See Also:** [XMLSEQUENCE](XMLSEQUENCE.md)

## Examples

The following example creates XML elements for the first and last names of a subset of employees, and then concatenates and returns those elements:

```md
SELECT XMLCONCAT(XMLELEMENT("First", e.first_name),
   XMLELEMENT("Last", e.last_name)) AS "Result"
   FROM employees e
   WHERE e.employee_id > 202;

Result
----------------------------------------------------------------
<First>Susan</First>
<Last>Mavris</Last>

<First>Hermann</First>
<Last>Baer</Last>

<First>Shelley</First>
<Last>Higgins</Last>

<First>William</First>
<Last>Gietz</Last>

4 rows selected.
```