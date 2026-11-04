---
title: "11.3.1 String Data Type Syntax"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/string-type-syntax.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 11.3.1 String Data Type Syntax

The string data types are [`CHAR`](char.md), [`VARCHAR`](char.md), [`BINARY`](binary-varbinary.md), [`VARBINARY`](binary-varbinary.md), [`BLOB`](blob.md), [`TEXT`](blob.md), [`ENUM`](enum.md), and [`SET`](set.md).

In some cases, MySQL may change a string column to a type different from that given in a [`CREATE         TABLE`](create-table.md) or [`ALTER TABLE`](alter-table.md) statement. See [Section 13.1.18.6, “Silent Column Specification Changes”](silent-column-changes.md).

For definitions of character string columns ([`CHAR`](char.md), [`VARCHAR`](char.md), and the [`TEXT`](blob.md) types), MySQL interprets length specifications in character units. For definitions of binary string columns ([`BINARY`](binary-varbinary.md), [`VARBINARY`](binary-varbinary.md), and the [`BLOB`](blob.md) types), MySQL interprets length specifications in byte units.

Column definitions for character string data types [`CHAR`](char.md), [`VARCHAR`](char.md), the [`TEXT`](blob.md) types, [`ENUM`](enum.md), [`SET`](set.md), and any synonyms) can specify the column character set and collation:

- `CHARACTER SET` specifies the character set. If desired, a collation for the character set can be specified with the `COLLATE` attribute, along with any other attributes. For example:
	```
	CREATE TABLE t
	(
	    c1 VARCHAR(20) CHARACTER SET utf8,
	    c2 TEXT CHARACTER SET latin1 COLLATE latin1_general_cs
	);
	```
	This table definition creates a column named `c1` that has a character set of `utf8` with the default collation for that character set, and a column named `c2` that has a character set of `latin1` and a case-sensitive (`_cs`) collation.
	The rules for assigning the character set and collation when either or both of `CHARACTER SET` and the `COLLATE` attribute are missing are described in [Section 10.3.5, “Column Character Set and Collation”](charset-column.md).
	`CHARSET` is a synonym for `CHARACTER SET`.
- Specifying the `CHARACTER SET binary` attribute for a character string data type causes the column to be created as the corresponding binary string data type: [`CHAR`](char.md) becomes [`BINARY`](binary-varbinary.md), [`VARCHAR`](char.md) becomes [`VARBINARY`](binary-varbinary.md), and [`TEXT`](blob.md) becomes [`BLOB`](blob.md). For the [`ENUM`](enum.md) and [`SET`](set.md) data types, this does not occur; they are created as declared. Suppose that you specify a table using this definition:
	```
	CREATE TABLE t
	(
	  c1 VARCHAR(10) CHARACTER SET binary,
	  c2 TEXT CHARACTER SET binary,
	  c3 ENUM('a','b','c') CHARACTER SET binary
	);
	```
	The resulting table has this definition:
	```
	CREATE TABLE t
	(
	  c1 VARBINARY(10),
	  c2 BLOB,
	  c3 ENUM('a','b','c') CHARACTER SET binary
	);
	```
- The `BINARY` attribute is a nonstandard MySQL extension that is shorthand for specifying the binary (`_bin`) collation of the column character set (or of the table default character set if no column character set is specified). In this case, comparison and sorting are based on numeric character code values. Suppose that you specify a table using this definition:
	```
	CREATE TABLE t
	(
	  c1 VARCHAR(10) CHARACTER SET latin1 BINARY,
	  c2 TEXT BINARY
	) CHARACTER SET utf8mb4;
	```
	The resulting table has this definition:
	```
	CREATE TABLE t (
	  c1 VARCHAR(10) CHARACTER SET latin1 COLLATE latin1_bin,
	  c2 TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin
	) CHARACTER SET utf8mb4;
	```
- The `ASCII` attribute is shorthand for `CHARACTER SET latin1`.
- The `UNICODE` attribute is shorthand for `CHARACTER SET ucs2`.

Character column comparison and sorting are based on the collation assigned to the column. For the [`CHAR`](char.md), [`VARCHAR`](char.md), [`TEXT`](blob.md), [`ENUM`](enum.md), and [`SET`](set.md) data types, you can declare a column with a binary (`_bin`) collation or the `BINARY` attribute to cause comparison and sorting to use the underlying character code values rather than a lexical ordering.

For additional information about use of character sets in MySQL, see [Chapter 10, *Character Sets, Collations, Unicode*](charset.md).

- ``[NATIONAL] CHAR[(*`M`*)]             [CHARACTER SET *`charset_name`*]             [COLLATE             *`collation_name`*]``
	A fixed-length string that is always right-padded with spaces to the specified length when stored. *`M`* represents the column length in characters. The range of *`M`* is 0 to 255. If *`M`* is omitted, the length is 1.
	Note
	Trailing spaces are removed when [`CHAR`](char.md) values are retrieved unless the [`PAD_CHAR_TO_FULL_LENGTH`](sql-mode.md) SQL mode is enabled.
	[`CHAR`](char.md) is shorthand for [`CHARACTER`](char.md). [`NATIONAL CHAR`](char.md) (or its equivalent short form, [`NCHAR`](char.md)) is the standard SQL way to define that a [`CHAR`](char.md) column should use some predefined character set. MySQL uses `utf8` as this predefined character set. [Section 10.3.7, “The National Character Set”](charset-national.md).
	The [`CHAR BYTE`](binary-varbinary.md) data type is an alias for the [`BINARY`](binary-varbinary.md) data type. This is a compatibility feature.
	MySQL permits you to create a column of type `CHAR(0)`. This is useful primarily when you must be compliant with old applications that depend on the existence of a column but that do not actually use its value. `CHAR(0)` is also quite nice when you need a column that can take only two values: A column that is defined as `CHAR(0) NULL` occupies only one bit and can take only the values `NULL` and `''` (the empty string).
- ``[NATIONAL] VARCHAR(*`M`*)             [CHARACTER SET *`charset_name`*]             [COLLATE             *`collation_name`*]``
	A variable-length string. *`M`* represents the maximum column length in characters. The range of *`M`* is 0 to 65,535. The effective maximum length of a [`VARCHAR`](char.md) is subject to the maximum row size (65,535 bytes, which is shared among all columns) and the character set used. For example, `utf8` characters can require up to three bytes per character, so a [`VARCHAR`](char.md) column that uses the `utf8` character set can be declared to be a maximum of 21,844 characters. See [Section 8.4.7, “Limits on Table Column Count and Row Size”](column-count-limit.md).
	MySQL stores [`VARCHAR`](char.md) values as a 1-byte or 2-byte length prefix plus data. The length prefix indicates the number of bytes in the value. A [`VARCHAR`](char.md) column uses one length byte if values require no more than 255 bytes, two length bytes if values may require more than 255 bytes.
	Note
	MySQL follows the standard SQL specification, and does *not* remove trailing spaces from [`VARCHAR`](char.md) values.
	[`VARCHAR`](char.md) is shorthand for [`CHARACTER VARYING`](char.md). [`NATIONAL VARCHAR`](char.md) is the standard SQL way to define that a [`VARCHAR`](char.md) column should use some predefined character set. MySQL uses `utf8` as this predefined character set. [Section 10.3.7, “The National Character Set”](charset-national.md). [`NVARCHAR`](char.md) is shorthand for [`NATIONAL VARCHAR`](char.md).
- [``BINARY[(*`M`*)]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/binary-varbinary.html "11.3.3 The BINARY and VARBINARY Types")
	The [`BINARY`](binary-varbinary.md) type is similar to the [`CHAR`](char.md) type, but stores binary byte strings rather than nonbinary character strings. An optional length *`M`* represents the column length in bytes. If omitted, *`M`* defaults to 1.
- [``VARBINARY(*`M`*)``](binary-varbinary.md)
	The [`VARBINARY`](binary-varbinary.md) type is similar to the [`VARCHAR`](char.md) type, but stores binary byte strings rather than nonbinary character strings. *`M`* represents the maximum column length in bytes.
- [`TINYBLOB`](blob.md)
	A [`BLOB`](blob.md) column with a maximum length of 255 (2 <sup>8</sup> − 1) bytes. Each [`TINYBLOB`](blob.md) value is stored using a 1-byte length prefix that indicates the number of bytes in the value.
- [``TINYTEXT             [CHARACTER SET *`charset_name`*]             [COLLATE             *`collation_name`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/blob.html "11.3.4 The BLOB and TEXT Types")
	A [`TEXT`](blob.md) column with a maximum length of 255 (2 <sup>8</sup> − 1) characters. The effective maximum length is less if the value contains multibyte characters. Each [`TINYTEXT`](blob.md) value is stored using a 1-byte length prefix that indicates the number of bytes in the value.
- [``BLOB[(*`M`*)]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/blob.html "11.3.4 The BLOB and TEXT Types")
	A [`BLOB`](blob.md) column with a maximum length of 65,535 (2 <sup>16</sup> − 1) bytes. Each [`BLOB`](blob.md) value is stored using a 2-byte length prefix that indicates the number of bytes in the value.
	An optional length *`M`* can be given for this type. If this is done, MySQL creates the column as the smallest [`BLOB`](blob.md) type large enough to hold values *`M`* bytes long.
- [``TEXT[(*`M`*)]             [CHARACTER SET *`charset_name`*]             [COLLATE             *`collation_name`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/blob.html "11.3.4 The BLOB and TEXT Types")
	A [`TEXT`](blob.md) column with a maximum length of 65,535 (2 <sup>16</sup> − 1) bytes. The effective maximum length is less if the value contains multibyte characters. Each [`TEXT`](blob.md) value is stored using a 2-byte length prefix that indicates the number of bytes in the value.
	An optional length *`M`* can be given for this type. If this is done, MySQL creates the column as the smallest [`TEXT`](blob.md) type large enough to hold values *`M`* characters long.
- [`MEDIUMBLOB`](blob.md)
	A [`BLOB`](blob.md) column with a maximum length of 16,777,215 (2 <sup>24</sup> − 1) bytes. Each [`MEDIUMBLOB`](blob.md) value is stored using a 3-byte length prefix that indicates the number of bytes in the value.
- [``MEDIUMTEXT             [CHARACTER SET *`charset_name`*]             [COLLATE             *`collation_name`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/blob.html "11.3.4 The BLOB and TEXT Types")
	A [`TEXT`](blob.md) column with a maximum length of 16,777,215 (2 <sup>24</sup> − 1) characters. The effective maximum length is less if the value contains multibyte characters. Each [`MEDIUMTEXT`](blob.md) value is stored using a 3-byte length prefix that indicates the number of bytes in the value.
- [`LONGBLOB`](blob.md)
	A [`BLOB`](blob.md) column with a maximum length of 4,294,967,295 or 4GB (2 <sup>32</sup> − 1) bytes. The effective maximum length of [`LONGBLOB`](blob.md) columns depends on the configured maximum packet size in the client/server protocol and available memory. Each [`LONGBLOB`](blob.md) value is stored using a 4-byte length prefix that indicates the number of bytes in the value.
- [``LONGTEXT             [CHARACTER SET *`charset_name`*]             [COLLATE             *`collation_name`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/blob.html "11.3.4 The BLOB and TEXT Types")
	A [`TEXT`](blob.md) column with a maximum length of 4,294,967,295 or 4GB (2 <sup>32</sup> − 1) characters. The effective maximum length is less if the value contains multibyte characters. The effective maximum length of [`LONGTEXT`](blob.md) columns also depends on the configured maximum packet size in the client/server protocol and available memory. Each [`LONGTEXT`](blob.md) value is stored using a 4-byte length prefix that indicates the number of bytes in the value.
- [``ENUM('*`value1`*','*`value2`*',...)             [CHARACTER SET *`charset_name`*]             [COLLATE             *`collation_name`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/enum.html "11.3.5 The ENUM Type")
	An enumeration. A string object that can have only one value, chosen from the list of values ``'*`value1`*'``, ``'*`value2`*'``, `...`, `NULL` or the special `''` error value. [`ENUM`](enum.md) values are represented internally as integers.
	An [`ENUM`](enum.md) column can have a maximum of 65,535 distinct elements. (The practical limit is less than 3000.) A table can have no more than 255 unique element list definitions among its [`ENUM`](enum.md) and [`SET`](set.md) columns considered as a group. For more information on these limits, see [Limits Imposed by.frm File Structure](create-table-files.md).
- [``SET('*`value1`*','*`value2`*',...)             [CHARACTER SET *`charset_name`*]             [COLLATE             *`collation_name`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/set.html "11.3.6 The SET Type")
	A set. A string object that can have zero or more values, each of which must be chosen from the list of values ``'*`value1`*'``, ``'*`value2`*'``, `...` [`SET`](set.md) values are represented internally as integers.
	A [`SET`](set.md) column can have a maximum of 64 distinct members. A table can have no more than 255 unique element list definitions among its [`ENUM`](enum.md) and [`SET`](set.md) columns considered as a group. For more information on this limit, see [Limits Imposed by.frm File Structure](create-table-files.md).