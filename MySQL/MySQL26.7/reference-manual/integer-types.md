---
title: "MySQL :: MySQL 26.7 Reference Manual :: 13.1.2 Integer Types (Exact Value) - INTEGER, INT, SMALLINT, TINYINT,\n        MEDIUMINT, BIGINT"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/integer-types.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 13.1.2 Integer Types (Exact Value) - INTEGER, INT, SMALLINT, TINYINT, MEDIUMINT, BIGINT

MySQL supports the SQL standard integer types `INTEGER` (or `INT`) and `SMALLINT`. As an extension to the standard, MySQL also supports the integer types `TINYINT`, `MEDIUMINT`, and `BIGINT`. The following table shows the required storage and range for each integer type.

**Table 13.1 Required Storage and Range for Integer Types Supported by MySQL**

| Type | Storage (Bytes) | Minimum Value Signed | Minimum Value Unsigned | Maximum Value Signed | Maximum Value Unsigned |
| --- | --- | --- | --- | --- | --- |
| `TINYINT` | 1 | `-128` | `0` | `127` | `255` |
| `SMALLINT` | 2 | `-32768` | `0` | `32767` | `65535` |
| `MEDIUMINT` | 3 | `-8388608` | `0` | `8388607` | `16777215` |
| `INT` | 4 | `-2147483648` | `0` | `2147483647` | `4294967295` |
| `BIGINT` | 8 | `-2<sup>63</sup>` | `0` | `2<sup>63</sup>-1` | `2<sup>64</sup>-1` |