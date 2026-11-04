---
title: "14.24.2 DECIMAL Data Type Characteristics"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/precision-math-decimal-characteristics.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 14.24.2 DECIMAL Data Type Characteristics

This section discusses the characteristics of the [`DECIMAL`](fixed-point-types.md) data type (and its synonyms), with particular regard to the following topics:

- Maximum number of digits
- Storage format
- Storage requirements
- The nonstandard MySQL extension to the upper range of [`DECIMAL`](fixed-point-types.md) columns

The declaration syntax for a [`DECIMAL`](fixed-point-types.md) column is ``DECIMAL(*`M`*,*`D`*)``. The ranges of values for the arguments are as follows:

- *`M`* is the maximum number of digits (the precision). It has a range of 1 to 65.
- *`D`* is the number of digits to the right of the decimal point (the scale). It has a range of 0 to 30 and must be no larger than *`M`*.

If *`D`* is omitted, the default is 0. If *`M`* is omitted, the default is 10.

The maximum value of 65 for *`M`* means that calculations on [`DECIMAL`](fixed-point-types.md) values are accurate up to 65 digits. This limit of 65 digits of precision also applies to exact-value numeric literals, so the maximum range of such literals differs from before. (There is also a limit on how long the text of [`DECIMAL`](fixed-point-types.md) literals can be; see [Section 14.24.3, “Expression Handling”](precision-math-expressions.md).)

Values for [`DECIMAL`](fixed-point-types.md) columns are stored using a binary format that packs nine decimal digits into 4 bytes. The storage requirements for the integer and fractional parts of each value are determined separately. Each multiple of nine digits requires 4 bytes, and any remaining digits left over require some fraction of 4 bytes. The storage required for remaining digits is given by the following table.

| Leftover Digits | Number of Bytes |
| --- | --- |
| 0 | 0 |
| 1–2 | 1 |
| 3–4 | 2 |
| 5–6 | 3 |
| 7–9 | 4 |

For example, a `DECIMAL(18,9)` column has nine digits on either side of the decimal point, so the integer part and the fractional part each require 4 bytes. A `DECIMAL(20,6)` column has fourteen integer digits and six fractional digits. The integer digits require four bytes for nine of the digits and 3 bytes for the remaining five digits. The six fractional digits require 3 bytes.

[`DECIMAL`](fixed-point-types.md) columns do not store a leading `+` character or `-` character or leading `0` digits. If you insert `+0003.1` into a `DECIMAL(5,1)` column, it is stored as `3.1`. For negative numbers, a literal `-` character is not stored.

[`DECIMAL`](fixed-point-types.md) columns do not permit values larger than the range implied by the column definition. For example, a `DECIMAL(3,0)` column supports a range of `-999` to `999`. A ``DECIMAL(*`M`*,*`D`*)`` column permits up to *`M`* - *`D`* digits to the left of the decimal point.

The SQL standard requires that the precision of ``NUMERIC(*`M`*,*`D`*)`` be *exactly* *`M`* digits. For ``DECIMAL(*`M`*,*`D`*)``, the standard requires a precision of at least *`M`* digits but permits more. In MySQL, ``DECIMAL(*`M`*,*`D`*)`` and ``NUMERIC(*`M`*,*`D`*)`` are the same, and both have a precision of exactly *`M`* digits.

For a full explanation of the internal format of `DECIMAL` values, see the file `strings/decimal.c` in a MySQL source distribution. The format is explained (with an example) in the `decimal2bin()` function.