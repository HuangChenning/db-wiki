---
title: "13.9 Using Data Types from Other Database Engines"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/other-vendor-data-types.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

To facilitate the use of code written for SQL implementations from other vendors, MySQL maps data types as shown in the following table. These mappings make it easier to import table definitions from other database systems into MySQL.

| Other Vendor Type | MySQL Type |
| --- | --- |
| [`BOOL`](integer-types.md) | [`TINYINT`](integer-types.md) |
| [`BOOLEAN`](integer-types.md) | [`TINYINT`](integer-types.md) |
| ``CHARACTER VARYING(*`M`*)`` | ``VARCHAR(*`M`*)`` |
| [`FIXED`](fixed-point-types.md) | [`DECIMAL`](fixed-point-types.md) |
| [`FLOAT4`](floating-point-types.md) | [`FLOAT`](floating-point-types.md) |
| [`FLOAT8`](floating-point-types.md) | [`DOUBLE`](floating-point-types.md) |
| [`INT1`](integer-types.md) | [`TINYINT`](integer-types.md) |
| [`INT2`](integer-types.md) | [`SMALLINT`](integer-types.md) |
| [`INT3`](integer-types.md) | [`MEDIUMINT`](integer-types.md) |
| [`INT4`](integer-types.md) | [`INT`](integer-types.md) |
| `INT8` | [`BIGINT`](integer-types.md) |
| `LONG VARBINARY` | [`MEDIUMBLOB`](blob.md) |
| `LONG VARCHAR` | [`MEDIUMTEXT`](blob.md) |
| `LONG` | [`MEDIUMTEXT`](blob.md) |
| [`MIDDLEINT`](integer-types.md) | [`MEDIUMINT`](integer-types.md) |
| [`NUMERIC`](fixed-point-types.md) | [`DECIMAL`](fixed-point-types.md) |

Data type mapping occurs at table creation time, after which the original type specifications are discarded. If you create a table with types used by other vendors and then issue a ``DESCRIBE *`tbl_name`*`` statement, MySQL reports the table structure using the equivalent MySQL types. For example:

```
mysql> CREATE TABLE t (a BOOL, b FLOAT8, c LONG VARCHAR, d NUMERIC);
Query OK, 0 rows affected (0.00 sec)

mysql> DESCRIBE t;
+-------+---------------+------+-----+---------+-------+
| Field | Type          | Null | Key | Default | Extra |
+-------+---------------+------+-----+---------+-------+
| a     | tinyint(1)    | YES  |     | NULL    |       |
| b     | double        | YES  |     | NULL    |       |
| c     | mediumtext    | YES  |     | NULL    |       |
| d     | decimal(10,0) | YES  |     | NULL    |       |
+-------+---------------+------+-----+---------+-------+
4 rows in set (0.01 sec)
```