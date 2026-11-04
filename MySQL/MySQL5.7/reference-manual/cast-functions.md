---
title: "12.10 Cast Functions and Operators"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/cast-functions.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

**Table 12.15 Cast Functions and Operators**

| Name | Description |
| --- | --- |
| `BINARY` | Cast a string to a binary string |
| `CAST()` | Cast a value as a certain type |
| `CONVERT()` | Cast a value as a certain type |

Cast functions and operators enable conversion of values from one data type to another.

### Cast Function and Operator Descriptions

- `BINARY` *`expr`*
	The `BINARY` operator converts the expression to a binary string (a string that has the `binary` character set and `binary` collation). A common use for `BINARY` is to force a character string comparison to be done byte by byte using numeric byte values rather than character by character. The `BINARY` operator also causes trailing spaces in comparisons to be significant. For information about the differences between the `binary` collation of the `binary` character set and the `_bin` collations of nonbinary character sets, see [Section 10.8.5, “The binary Collation Compared to \_bin Collations”](charset-binary-collations.md).
	```
	mysql> SELECT 'a' = 'A';
	        -> 1
	mysql> SELECT BINARY 'a' = 'A';
	        -> 0
	mysql> SELECT 'a' = 'a ';
	        -> 1
	mysql> SELECT BINARY 'a' = 'a ';
	        -> 0
	```
	In a comparison, `BINARY` affects the entire operation; it can be given before either operand with the same result.
	To convert a string expression to a binary string, these constructs are equivalent:
	```
	CONVERT(expr USING BINARY)
	CAST(expr AS BINARY)
	BINARY expr
	```
	If a value is a string literal, it can be designated as a binary string without converting it by using the `_binary` character set introducer:
	```
	mysql> SELECT 'a' = 'A';
	        -> 1
	mysql> SELECT _binary 'a' = 'A';
	        -> 0
	```
	For information about introducers, see [Section 10.3.8, “Character Set Introducers”](charset-introducer.md).
	The `BINARY` operator in expressions differs in effect from the `BINARY` attribute in character column definitions. For a character column defined with the `BINARY` attribute, MySQL assigns the table default character set and the binary (`_bin`) collation of that character set. Every nonbinary character set has a `_bin` collation. For example, if the table default character set is `utf8`, these two column definitions are equivalent:
	```
	CHAR(10) BINARY
	CHAR(10) CHARACTER SET utf8 COLLATE utf8_bin
	```
	The use of `CHARACTER SET binary` in the definition of a [`CHAR`](char.md), [`VARCHAR`](char.md), or [`TEXT`](blob.md) column causes the column to be treated as the corresponding binary string data type. For example, the following pairs of definitions are equivalent:
	```
	CHAR(10) CHARACTER SET binary
	BINARY(10)
	VARCHAR(10) CHARACTER SET binary
	VARBINARY(10)
	TEXT CHARACTER SET binary
	BLOB
	```
	If `BINARY` is invoked from within the [**mysql**](mysql.md) client, binary strings display using hexadecimal notation, depending on the value of the [`--binary-as-hex`](mysql-command-options.md). For more information about that option, see [Section 4.5.1, “mysql — The MySQL Command-Line Client”](mysql.md).
- ``CAST(*`expr`* AS             *`type`*)``
	``CAST(*`expr`* AS             *`type`*`` takes an expression of any type and produces a result value of the specified type. This operation may also be expressed as ``CONVERT(*`expr`*,             *`type`*)``, which is equivalent.
	These *`type`* values are permitted:
	- ``BINARY[(*`N`*)]``
		Produces a string with the [`VARBINARY`](binary-varbinary.md) data type, except that when the expression *`expr`* is empty (zero length), the result type is `BINARY(0)`. If the optional length *`N`* is given, ``BINARY(*`N`*)`` causes the cast to use no more than *`N`* bytes of the argument. Values shorter than *`N`* bytes are padded with `0x00` bytes to a length of *`N`*. If the optional length *`N`* is not given, MySQL calculates the maximum length from the expression. If the supplied or calculated length is greater than an internal threshold, the result type is `BLOB`. If the length is still too long, the result type is `LONGBLOB`.
		For a description of how casting to `BINARY` affects comparisons, see [Section 11.3.3, “The BINARY and VARBINARY Types”](binary-varbinary.md).
	- ``CHAR[(*`N`*)]                 [*`charset_info`*]``
		Produces a string with the [`VARCHAR`](char.md) data type, unless the expression *`expr`* is empty (zero length), in which case the result type is `CHAR(0)`. If the optional length *`N`* is given, ``CHAR(*`N`*)`` causes the cast to use no more than *`N`* characters of the argument. No padding occurs for values shorter than *`N`* characters. If the optional length *`N`* is not given, MySQL calculates the maximum length from the expression. If the supplied or calculated length is greater than an internal threshold, the result type is `TEXT`. If the length is still too long, the result type is `LONGTEXT`.
		With no *`charset_info`* clause, `CHAR` produces a string with the default character set. To specify the character set explicitly, these *`charset_info`* values are permitted:
		- ``CHARACTER SET                     *`charset_name`*``: Produces a string with the given character set.
		- `ASCII`: Shorthand for `CHARACTER SET latin1`.
		- `UNICODE`: Shorthand for `CHARACTER SET ucs2`.
		In all cases, the string has the character set default collation.
	- `DATE`
		Produces a [`DATE`](datetime.md) value.
	- ``DATETIME[(*`M`*)]``
		Produces a [`DATETIME`](datetime.md) value. If the optional *`M`* value is given, it specifies the fractional seconds precision.
	- ``DECIMAL[(*`M`*[,*`D`*])]``
		Produces a [`DECIMAL`](fixed-point-types.md) value. If the optional *`M`* and *`D`* values are given, they specify the maximum number of digits (the precision) and the number of digits following the decimal point (the scale). If *`D`* is omitted, 0 is assumed. If *`M`* is omitted, 10 is assumed.
	- `JSON`
		Produces a [`JSON`](json.md) value. For details on the rules for conversion of values between [`JSON`](json.md) and other types, see [Comparison and Ordering of JSON Values](json.md).
	- ``NCHAR[(*`N`*)]``
		Like `CHAR`, but produces a string with the national character set. See [Section 10.3.7, “The National Character Set”](charset-national.md).
		Unlike `CHAR`, `NCHAR` does not permit trailing character set information to be specified.
	- `SIGNED [INTEGER]`
		Produces a signed [`BIGINT`](integer-types.md) value.
	- ``TIME[(*`M`*)]``
		Produces a [`TIME`](time.md) value. If the optional *`M`* value is given, it specifies the fractional seconds precision.
	- `UNSIGNED [INTEGER]`
		Produces an unsigned [`BIGINT`](integer-types.md) value.
- ``CONVERT(*`expr`*             USING *`transcoding_name`*)``
	``CONVERT(*`expr`*,*`type`*)``
	``CONVERT(*`expr`*             USING *`transcoding_name`*)`` is standard SQL syntax. The non- `USING` form of `CONVERT()` is ODBC syntax.
	``CONVERT(*`expr`*             USING *`transcoding_name`*)`` converts data between different character sets. In MySQL, transcoding names are the same as the corresponding character set names. For example, this statement converts the string `'abc'` in the default character set to the corresponding string in the `utf8` character set:
	```
	SELECT CONVERT('abc' USING utf8);
	```
	``CONVERT(*`expr`*,             *`type`*)`` syntax (without `USING`) takes an expression and a *`type`* value specifying a result type, and produces a result value of the specified type. This operation may also be expressed as ``CAST(*`expr`* AS             *`type`*)``, which is equivalent. For more information, see the description of `CAST()`.

### Character Set Conversions

`CONVERT()` with a `USING` clause converts data between character sets:

```
CONVERT(expr USING transcoding_name)
```

In MySQL, transcoding names are the same as the corresponding character set names.

Examples:

```
SELECT CONVERT('test' USING utf8);
SELECT CONVERT(_latin1'Müller' USING utf8);
INSERT INTO utf8_table (utf8_column)
    SELECT CONVERT(latin1_column USING utf8) FROM latin1_table;
```

To convert strings between character sets, you can also use ``CONVERT(*`expr`*,         *`type`*)`` syntax (without `USING`), or ``CAST(*`expr`* AS         *`type`*)``, which is equivalent:

```
CONVERT(string, CHAR[(N)] CHARACTER SET charset_name)
CAST(string AS CHAR[(N)] CHARACTER SET charset_name)
```

Examples:

```
SELECT CONVERT('test', CHAR CHARACTER SET utf8);
SELECT CAST('test' AS CHAR CHARACTER SET utf8);
```

If you specify ``CHARACTER SET         *`charset_name`*`` as just shown, the character set and collation of the result are *`charset_name`* and the default collation of *`charset_name`*. If you omit ``CHARACTER SET         *`charset_name`*``, the character set and collation of the result are defined by the [`character_set_connection`](server-system-variables.md) and [`collation_connection`](server-system-variables.md) system variables that determine the default connection character set and collation (see [Section 10.4, “Connection Character Sets and Collations”](charset-connection.md)).

A `COLLATE` clause is not permitted within a `CONVERT()` or `CAST()` call, but you can apply it to the function result. For example, these are legal:

```
SELECT CONVERT('test' USING utf8) COLLATE utf8_bin;
SELECT CONVERT('test', CHAR CHARACTER SET utf8) COLLATE utf8_bin;
SELECT CAST('test' AS CHAR CHARACTER SET utf8) COLLATE utf8_bin;
```

But these are illegal:

```
SELECT CONVERT('test' USING utf8 COLLATE utf8_bin);
SELECT CONVERT('test', CHAR CHARACTER SET utf8 COLLATE utf8_bin);
SELECT CAST('test' AS CHAR CHARACTER SET utf8 COLLATE utf8_bin);
```

For string literals, another way to specify the character set is to use a character set introducer. `_latin1` and `_latin2` in the preceding example are instances of introducers. Unlike conversion functions such as `CAST()`, or `CONVERT()`, which convert a string from one character set to another, an introducer designates a string literal as having a particular character set, with no conversion involved. For more information, see [Section 10.3.8, “Character Set Introducers”](charset-introducer.md).

### Character Set Conversions for String Comparisons

Normally, you cannot compare a [`BLOB`](blob.md) value or other binary string in case-insensitive fashion because binary strings use the `binary` character set, which has no collation with the concept of lettercase. To perform a case-insensitive comparison, first use the `CONVERT()` or `CAST()` function to convert the value to a nonbinary string. Comparisons of the resulting string use its collation. For example, if the conversion result collation is not case-sensitive, a [`LIKE`](string-comparison-functions.md) operation is not case-sensitive. That is true for the following operation because the default `latin1` collation (`latin1_swedish_ci`) is not case-sensitive:

```
SELECT 'A' LIKE CONVERT(blob_col USING latin1)
  FROM tbl_name;
```

To specify a particular collation for the converted string, use a `COLLATE` clause following the `CONVERT()` call:

```
SELECT 'A' LIKE CONVERT(blob_col USING latin1) COLLATE latin1_german1_ci
  FROM tbl_name;
```

To use a different character set, substitute its name for `latin1` in the preceding statements (and similarly to use a different collation).

`CONVERT()` and `CAST()` can be used more generally for comparing strings represented in different character sets. For example, a comparison of these strings results in an error because they have different character sets:

```
mysql> SET @s1 = _latin1 'abc', @s2 = _latin2 'abc';
mysql> SELECT @s1 = @s2;
ERROR 1267 (HY000): Illegal mix of collations (latin1_swedish_ci,IMPLICIT)
and (latin2_general_ci,IMPLICIT) for operation '='
```

Converting one of the strings to a character set compatible with the other enables the comparison to occur without error:

```
mysql> SELECT @s1 = CONVERT(@s2 USING latin1);
+---------------------------------+
| @s1 = CONVERT(@s2 USING latin1) |
+---------------------------------+
|                               1 |
+---------------------------------+
```

Character set conversion is also useful preceding lettercase conversion of binary strings. [`LOWER()`](string-functions.md) and [`UPPER()`](string-functions.md) are ineffective when applied directly to binary strings because the concept of lettercase does not apply. To perform lettercase conversion of a binary string, first convert it to a nonbinary string using a character set appropriate for the data stored in the string:

```
mysql> SET @str = BINARY 'New York';
mysql> SELECT LOWER(@str), LOWER(CONVERT(@str USING latin1));
+-------------+-----------------------------------+
| LOWER(@str) | LOWER(CONVERT(@str USING latin1)) |
+-------------+-----------------------------------+
| New York    | new york                          |
+-------------+-----------------------------------+
```

Be aware that if you apply `BINARY`, `CAST()`, or `CONVERT()` to an indexed column, MySQL may not be able to use the index efficiently.

### Other Uses for Cast Operations

The cast functions are useful for creating a column with a specific type in a [`CREATE TABLE ...         SELECT`](create-table.md) statement:

```
mysql> CREATE TABLE new_table SELECT CAST('2000-01-01' AS DATE) AS c1;
mysql> SHOW CREATE TABLE new_table\G
*************************** 1. row ***************************
       Table: new_table
Create Table: CREATE TABLE \`new_table\` (
  \`c1\` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

The cast functions are useful for sorting [`ENUM`](enum.md) columns in lexical order. Normally, sorting of [`ENUM`](enum.md) columns occurs using the internal numeric values. Casting the values to [`CHAR`](char.md) results in a lexical sort:

```
SELECT enum_col FROM tbl_name ORDER BY CAST(enum_col AS CHAR);
```

`CAST()` also changes the result if you use it as part of a more complex expression such as [`CONCAT('Date: ',CAST(NOW() AS         DATE))`](string-functions.md).

For temporal values, there is little need to use `CAST()` to extract data in different formats. Instead, use a function such as [`EXTRACT()`](date-and-time-functions.md), [`DATE_FORMAT()`](date-and-time-functions.md), or [`TIME_FORMAT()`](date-and-time-functions.md). See [Section 12.7, “Date and Time Functions”](date-and-time-functions.md).

To cast a string to a number, it normally suffices to use the string value in numeric context:

```
mysql> SELECT 1+'1';
       -> 2
```

That is also true for hexadecimal and bit literals, which are binary strings by default:

```
mysql> SELECT X'41', X'41'+0;
        -> 'A', 65
mysql> SELECT b'1100001', b'1100001'+0;
        -> 'a', 97
```

A string used in an arithmetic operation is converted to a floating-point number during expression evaluation.

A number used in string context is converted to a string:

```
mysql> SELECT CONCAT('hello you ',2);
        -> 'hello you 2'
```

For information about implicit conversion of numbers to strings, see [Section 12.3, “Type Conversion in Expression Evaluation”](type-conversion.md).

MySQL supports arithmetic with both signed and unsigned 64-bit values. For numeric operators (such as [`+`](arithmetic-functions.md) or [`-`](arithmetic-functions.md)) where one of the operands is an unsigned integer, the result is unsigned by default (see [Section 12.6.1, “Arithmetic Operators”](arithmetic-functions.md)). To override this, use the `SIGNED` or `UNSIGNED` cast operator to cast a value to a signed or unsigned 64-bit integer, respectively.

```
mysql> SELECT 1 - 2;
        -> -1
mysql> SELECT CAST(1 - 2 AS UNSIGNED);
        -> 18446744073709551615
mysql> SELECT CAST(CAST(1 - 2 AS UNSIGNED) AS SIGNED);
        -> -1
```

If either operand is a floating-point value, the result is a floating-point value and is not affected by the preceding rule. (In this context, [`DECIMAL`](fixed-point-types.md) column values are regarded as floating-point values.)

```
mysql> SELECT CAST(1 AS UNSIGNED) - 2.0;
        -> -1.0
```

The SQL mode affects the result of conversion operations (see [Section 5.1.10, “Server SQL Modes”](sql-mode.md)). Examples:

- For conversion of a “zero” date string to a date, `CONVERT()` and `CAST()` return `NULL` and produce a warning when the [`NO_ZERO_DATE`](sql-mode.md) SQL mode is enabled.
- For integer subtraction, if the [`NO_UNSIGNED_SUBTRACTION`](sql-mode.md) SQL mode is enabled, the subtraction result is signed even if any operand is unsigned.