---
title: "MySQL :: MySQL 26.10 Reference Manual :: 13.8 Choosing the Right Type for a Column"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/choosing-types.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 13.8 Choosing the Right Type for a Column

For optimum storage, you should try to use the most precise type in all cases. For example, if an integer column is used for values in the range from `1` to `99999`, `MEDIUMINT UNSIGNED` is the best type. Of the types that represent all the required values, this type uses the least amount of storage.

All basic calculations (`+`, `-`, `*`, and `/`) with [`DECIMAL`](fixed-point-types.md) columns are done with precision of 65 decimal (base 10) digits. See [Section 13.1.1, “Numeric Data Type Syntax”](numeric-type-syntax.md).

If accuracy is not too important or if speed is the highest priority, the [`DOUBLE`](floating-point-types.md) type may be good enough. For high precision, you can always convert to a fixed-point type stored in a [`BIGINT`](integer-types.md). This enables you to do all calculations with 64-bit integers and then convert results back to floating-point values as necessary.