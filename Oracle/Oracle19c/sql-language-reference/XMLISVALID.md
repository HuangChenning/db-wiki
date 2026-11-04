---
title: XMLISVALID
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/XMLISVALID.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![xmlisvalid](img/xmlisvalid.gif)

> ```
> XMLISVALID ( XMLType_instance [, XMLSchema_URL [, element ]] )
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration xmlisvalid.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/xmlisvalid.html)

## Purpose

`XMLISVALID` checks whether the input *XMLType\_instance* conforms to the relevant XML schema. It does not change the validation status recorded for *XMLType\_instance*.

If the input XML document is determined to be valid, then `XMLISVALID` returns 1; otherwise, it returns 0. If you provide *XMLSchema\_URL* as an argument, then that is used to check conformance. Otherwise, the XML schema specified by the XML document is used to check conformance.

- *XMLType\_instance* is the XMLType instance to be validated.
- *XMLSchema\_URL* is the URL of the XML schema against which to check conformance.
- *element* is the element of the specified schema against which to check conformance. Use this if you have an XML schema that defines more than one top level element, and you want to check conformance against a specific one of those elements. **See Also:** [*Oracle XML DB Developer’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=ADXDB4105) for information on the use of this function, including examples