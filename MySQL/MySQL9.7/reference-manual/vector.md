---
title: "13.3.5 The VECTOR Type"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/vector.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 13.3.5 The VECTOR Type

A `VECTOR` is a structure that can hold up to a specified number of entries *`N`*, defined as shown here:

```
VECTOR(N)
```

Each entry is a 4-byte (single-precision) floating-point value.

The default length is 2048; the maximum is 16383 entries. To declare a `VECTOR` column of the default length, define it as `VECTOR` with no parentheses following; trying to define a column as `VECTOR()` (with empty parentheses) raises a syntax error.

A `VECTOR` cannot be compared to any other type. It can be compared to another `VECTOR` for equality, but no other comparison is possible.

A `VECTOR` column cannot be used as any type of key. This includes all of the following types:

- Primary key
- Foreign key
- Unique key
- Partitioning key

A `VECTOR` column also cannot be used as a histogram source.

#### VECTOR Supported and Unsupported Functions

`VECTOR` values can be used with the MySQL string functions [`BIT_LENGTH()`](string-functions.md), [`CHAR_LENGTH()`](string-functions.md), [`HEX()`](string-functions.md), [`LENGTH()`](string-functions.md), and [`TO_BASE64()`](string-functions.md). Other string functions do not accept the `VECTOR` type as an argument.

`VECTOR` can be used as an argument to any of the encryption functions [`AES_ENCRYPT()`](encryption-functions.md), [`COMPRESS()`](encryption-functions.md), and [`SHA2()`](encryption-functions.md). `VECTOR` is not supported as an argument type by any other encryption functions.

`VECTOR` can be used as an argument to the [`CASE`](flow-control-functions.md) operator and related flow-control functions, including [`COALESCE()`](comparison-operators.md), [`IFNULL()`](flow-control-functions.md), [`NULLIF()`](flow-control-functions.md), and [`IF()`](flow-control-functions.md).

`VECTOR` can be used as the argument to [``CAST(*`expression`*         AS BINARY``](cast-functions.md)); the result is a binary string with the same contents as the `VECTOR` argument. Casting to `VECTOR` with `CAST` is not supported; you can convert a suitable string to `VECTOR` using [`STRING_TO_VECTOR()`](vector-functions.md).

`VECTOR` data types cannot be used as arguments to aggregate functions or window functions other than [`COUNT`](aggregate-functions.md) `[DISTINCT]`.

`VECTOR` cannot be used as an argument to any of the following types of functions and operators:

For more information, see [Section 14.21, “Vector Functions”](vector-functions.md).

`VECTOR` values are supported by JavaScript stored programs. See [Section 27.3.4, “JavaScript Stored Program Data Types and Argument Handling”](srjs-data-arguments.md), for more information.