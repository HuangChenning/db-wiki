---
title: "13.1.5 Bit-Value Type"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/bit-type.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 13.1.5 Bit-Value Type - BIT

The `BIT` data type is used to store bit values. A type of ``BIT(*`M`*)`` enables storage of *`M`* -bit values. *`M`* can range from 1 to 64.

To specify bit values, ``b'*`value`*'`` notation can be used. *`value`* is a binary value written using zeros and ones. For example, `b'111'` and `b'10000000'` represent 7 and 128, respectively. See [Section 11.1.5, “Bit-Value Literals”](bit-value-literals.md).

If you assign a value to a ``BIT(*`M`*)`` column that is less than *`M`* bits long, the value is padded on the left with zeros. For example, assigning a value of `b'101'` to a `BIT(6)` column is, in effect, the same as assigning `b'000101'`.

**NDB Cluster.** The maximum combined size of all `BIT` columns used in a given [`NDB`](mysql-cluster.md) table must not exceed 4096 bits.