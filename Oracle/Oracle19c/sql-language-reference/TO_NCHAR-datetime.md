---
title: TO_NCHAR (datetime)
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/TO_NCHAR-datetime.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

## to\_nchar\_date::=

![to_nchar_date](img/to_nchar_date.gif)

> ```
> TO_NCHAR({ datetime | interval }
>          [, fmt [, 'nlsparam' ] ]
>         )
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration to\_nchar\_date.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/to_nchar_date.html)

## Purpose

`TO_NCHAR` (datetime) converts a datetime or interval value of `DATE`, `TIMESTAMP`, `TIMESTAMP` `WITH` `TIME` `ZONE`, `TIMESTAMP` `WITH` `LOCAL` `TIME` `ZONE`, `INTERVAL` `MONTH` `TO` `YEAR`, or `INTERVAL` `DAY` `TO` `SECOND` data type from the database character set to the national character set.

**See Also:**

- “ [Security Considerations for Data Conversion](Data-Type-Comparison-Rules.md) ”
- in [*Oracle Database Globalization Support Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules, which define the collation assigned to the character return value of this function

## Examples

The following example converts the `order_date` of all orders whose status is `9` to the national character set:

```md
SELECT TO_NCHAR(ORDER_DATE) AS order_date
   FROM ORDERS
   WHERE ORDER_STATUS > 9
   ORDER BY order_date;

ORDER_DATE
--------------------------------------------------------------------------
06-DEC-99 02.22.34.225609 PM
13-SEP-99 10.19.00.654279 AM
14-SEP-99 09.53.40.223345 AM
26-JUN-00 10.19.43.190089 PM
27-JUN-00 09.53.32.335522 PM
```