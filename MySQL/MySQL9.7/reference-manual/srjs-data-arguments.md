---
title: "27.3.4 JavaScript Stored Program Data Types and Argument Handling"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/srjs-data-arguments.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 27.3.4 JavaScript Stored Program Data Types and Argument Handling

Most MySQL data types are supported for MLE stored program input and output arguments, as well as for return data types. The data types are listed here:

- *Integer*: All variants and aliases of MySQL integer data types are supported, including [`TINYINT`](integer-types.md), [`SMALLINT`](integer-types.md), [`MEDIUMINT`](integer-types.md), [`INT`](integer-types.md), and [`BIGINT`](integer-types.md).
	`SIGNED` and `UNSIGNED` are supported for all these types.
	[`BOOL`](integer-types.md) and [`SERIAL`](integer-types.md) are also supported, and treated as integer types.
- *String*: The [`CHAR`](char.md), [`VARCHAR`](char.md), [`TEXT`](blob.md), and [`BLOB`](blob.md) string types are supported.
	These types are supported as in the MySQL server with the following exceptions:
	1. String argument and return types can use the `utf8mb4` or binary character sets; use of other character sets for these raises an error. This restriction applies to argument and return type declarations; the server attempts to convert argument *values* using other character sets to `utfmb4` whenever necessary, as with SQL stored programs.
	2. The maximum supported length for a [`LONGTEXT`](blob.md) value is 1073741799 (2 <sup>30</sup> - 2 <sup>4</sup> - 2 <sup>3</sup> - 1) characters; for [`LONGBLOB`](blob.md), the maximum supported length is 2147483639 (2 <sup>31</sup> - 2 <sup>8</sup> - 1).
	Support for `BLOB` types includes support for [`BINARY`](binary-varbinary.md) and [`VARBINARY`](binary-varbinary.md).
	The MySQL [`JSON`](json.md) data type is also supported.
- *Floating point*: [`FLOAT`](floating-point-types.md) and [`DOUBLE`](floating-point-types.md) are supported along with their aliases. [`REAL`](floating-point-types.md) is also treated as floating point, but `UNSIGNED           FLOAT` and `UNSIGNED DOUBLE` are deprecated in MySQL, and are not supported by MLE.
- *Temporal types*: [`DATE`](datetime.md), [`DATETIME`](datetime.md), and [`TIMESTAMP`](datetime.md) are supported, and are converted to JavaScript `Date` values. [`TIME`](time.md) values are treated as strings; [`YEAR`](year.md) values are treated as numbers.
	The first time a given JavaScript stored procedure is executed, it is associated with the current MySQL session time zone, and this time zone continues to be used by the stored program, even if the MySQL session time zone is changed concurrently, for the duration of the MLE component session, or until [`mle_session_reset()`](srjs-session-info.md) is invoked. More more information, see Time zone support, later in this section.
- The [`VECTOR`](vector.md), [`DECIMAL`](fixed-point-types.md), [`NUMERIC`](fixed-point-types.md), and [`BIT`](bit-type.md) types are all supported in MySQL 9.7.

Input arguments (`IN` and `INOUT` parameters) are automatically converted into JavaScript types based on the mapping shown in the following table:

**Table 27.1 Conversion of MySQL data types to JavaScript types**

| MySQL Type | JavaScript Type |
| --- | --- |
| `TINYINT`, `SMALLINT`, `MEDIUMINT`, `INT`, `BOOL`, `BIGINT`, or `SERIAL` | If safe: `Number`; otherwise: `String` |
| `FLOAT` or `DOUBLE` | `Number` |
| `CHAR`, `VARCHAR`, `TINYTEXT`, `TEXT`, `MEDIUMTEXT`, or `LONGTEXT` | `String` |
| `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, `LONGBLOB`, `BINARY`, or `VARBINARY` | `Uint8Array` |
| `DATE`, `DATETIME`, or `TIMESTAMP` | `Date` |
| `TIME` | `String` |
| `YEAR` | `Number` |
| `VECTOR` | `Float32Array` |
| `DECIMAL` | `String` or `Number` depending on the value of `session.options.decimalType` (`STRING` or `NUMBER`, respectively). By default, converted to `String`. |
| ``BIT(*`M`*)`` | - ``BIT(*`M`*)`` <= `JavaScript.MAX_SAFE_INTEGER`: `Number` - ``BIT(*`M`*)`` > `JavaScript.MAX_SAFE_INTEGER`: `BigInt` |

Conversion to or from a MySQL integer whose value lies outside the range -(2 <sup>53</sup> -1) (-9007199254740991) to 2 <sup>53</sup> -1 (9007199254740991) is lossy. How conversion from MySQL integers to JavaScript is performed can be changed for the current session using [`mle_set_session_state()`](srjs-session-info.md); the default behavior is equivalent to calling this function using `UNSAFE_STRING` as the value for `integer_type`. See the description of that function for more information.

SQL `NULL` is supported for all the types listed, and is converted to and from JavaScript `null` as required.

JavaScript (unlike SQL) is a dynamically typed language, which means that return types are known only at execution time. JavaScript return value and output arguments (`OUT` and `INOUT` parameters) are automatically converted back into the expected MySQL type based on the mappings shown in the following table:

**Table 27.2 Type Conversion: JavaScript to MySQL**

| From JavaScript Type | To MySQL `TINYINT`, `SMALLINT`, `MEDIUMINT`, `INT`, `BIGINT`, `BOOLEAN`, or `SERIAL` | To MySQL `CHAR` or `VARCHAR` | To MySQL `FLOAT` or `DOUBLE` | To MySQL `TINYTEXT`, `TEXT`, `MEDIUMTEXT`, or `LONGTEXT` | To MySQL `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, `LONGBLOB`, `BINARY`, `VARBINARY` | To MySQL `VECTOR` | To MySQL `DECIMAL` (`NUMERIC`) | To MySQL `BIT` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Boolean` | Cast to `Integer` | Convert to `String`; check whether length of result is within expected range | Cast to `Float` | If JavaScript `Boolean` `true`: convert to “true”; if JavaScript `Boolean` `false`: convert to “false” | Error | Error | Convert to `Decimal` | Convert to `Bit` |
| `Number` | Round value to `Integer`; check whether value is out of range | Convert to `String`; check whether length of result is within expected range | Retain value; check whether this is out of range | Convert to `String`; check whether length of result is within expected range | Error | Error | Convert to `Decimal` | Convert to `Bit` |
| `BigInteger` | Retain value; check whether out of range | Convert to `String`; check whether length of result is within expected range | Cast to `Float`; check whether result is out of range | Convert to `String`; check whether length of result is within expected range | Error | Error | Convert to `Decimal` | Convert to `Bit` |
| `String` | Parse as number and round to `Integer`; check for value out of range | Retain value; check whether length is within range | Parse value to `Float`; check for value out of range values | Use existing string value; check whether length of string is within expected range | Error | Error | Convert to `Decimal` | Convert to `Bit` |
| `Symbol` or `Object` | Raise invalid type conversion error | Convert to `String`; check whether length of result is within expected range | Raise invalid type conversion error | Convert to `String`; check whether length of result is within expected range | Error | Error | Error | Error |
| Typed `Array` | Raise invalid type conversion error | Convert to `String`; check whether length of result is within expected range | Raise invalid type conversion error | Convert to `String`; check whether length of result is within expected range | Convert to byte array; check whether result is within expected size | Treat as `Float32Array`; convert to byte array, checking whether it is within the expected `VECTOR` field size | Error | Error |
| `null` or `undefined` | `NULL` | `NULL` | `NULL` | `NULL` | `NULL` | `NULL` | `NULL` | `NULL` |

Notes:

- JavaScript `Infinity` and `-Infinity` are treated as out-of-range values.
- JavaScript `NaN` raises an invalid type conversion error.
- All rounding is performed using `Math.round()`.
- Attempting to cast a `BigInt` or `String` having a non-numeric value to MySQL `FLOAT` raises an invalid type conversion error.
- The maximum supported length for strings is 1073741799.
- The maximum supported length for `BLOB` values is 2147483639.
- `JavaScript.MAX_SAFE_INTEGER` is equal to 9007199254740991 (2 <sup>53</sup> -1).

**Table 27.3 Type Conversion: JavaScript Dates to MySQL**

| JavaScript Type | MySQL `DATE` | MySQL `DATETIME`, `TIMESTAMP` | MySQL YEAR |
| --- | --- | --- | --- |
| `null` or `undefined` | `NULL` | `NULL` | `NULL` |
| `Date` | Retain value as is, rounding off any time part to the closest second. | Keep value as is. | Extract year from the `Date` |
| Type convertible to JavaScript `Date` (formatted string) | Cast value to JavaScript `Date` and handle accordingly | Cast value to JavaScript `Date` and handle accordingly | If value contains 4-digit year, use it. |
| Type not convertible to JavaScript `Date` | Invalid type conversion error | Invalid type conversion error | If value contains 4-digit year, use it. |

Passing a MySQL zero date (`00-00-0000`) or zero-in-date value (such as `00-01-2023`) leads to the creation of an `Invalid Date` instance of `Date`. When passed a MySQL date which is invalid (for example, 31 February), MLE calls a JavaScript `Date` constructor with invalid individual date and time component values.

The MySQL [`TIME`](time.md) type is handled as a string, and is validated inside MySQL. See [Section 13.2.3, “The TIME Type”](time.md), for more information.

**Table 27.4 Conversion of MySQL JSON types to JavaScript**

| MySQL JSON Type | JavaScript Type |
| --- | --- |
| `NULL`, `JSON NULL` | `null` |
| `JSON OBJECT` | `Object` |
| `JSON ARRAY` | `Array` |
| `JSON BOOLEAN` | `Boolean` |
| `JSON INTEGER`, `JSON DOUBLE`, `JSON DECIMAL` | `Number` |
| `JSON STRING` | `String` |
| `JSON DATETIME`, `JSON DATE`, `JSON TIME` | `String` |
| `JSON BLOB`, `JSON OPAQUE` | `String` |

Note

A MySQL JSON string, when converted to a JavaScript string, becomes unquoted.

**Table 27.5 Conversion of JavaScript types to MySQL JSON**

| JavaScript Type | MySQL JSON Type |
| --- | --- |
| `null`, `undefined` | `NULL` |
| `Boolean` | Error |
| `Number` | Error |
| `String` | - Can be parsed as JSON: JSON string, JSON object, or JSON array - Cannot be parsed as JSON: Error - `'null'`: JSON `null` |
| `BigInt` | Error |
| `Object` | JSON object or error (see text following table) |
| `Array` | JSON array |
| `Symbol` | - Inside an object: ignored - Inside an array: JSON `null`  Scalar value: Error |

Notes:

- A value within a container such as a JSON array or JSON object is converted (loss of precision is possible for `Number` values). A scalar value throws an error.
- JavaScript `BigInt` values cannot be converted to MySQL JSON; attempting to perform such a conversion always raises an error, regardless of whether the value is inside a container or not.
- It may or may not be possible to convert a JavaScript `Object` to MySQL JSON, depending on how `toJSON()` is implemented for the object in question. Some examples are listed here:
	- The `toJSON()` method of the JavaScript `Date` class converts a `Date` to a string having invalid JSON syntax, thus throwing a conversion error.
	- For the `Set` class, `toJSON()` returns `"{}"` which is a valid JSON string.
	- For JSON-like objects, `toJSON()` returns a valid JSON string.

**Conversion to and from MySQL ENUM and SET.** `ENUM` converts to a JavaScript `String`; `SET` converts to a JavaScript `Set` object, as shown in the following table:

**Table 27.6 Conversion of the MySQL ENUM and SET types to JavaScript**

| MySQL Type | JavaScript Type |
| --- | --- |
| [`ENUM`](enum.md) | `String` |
| [`SET`](set.md) | `Set` |

The following table shows rules for converting a JavaScript type to a MySQL `ENUM` or `SET` type:

**Table 27.7 Type Conversion: JavaScript types to MySQL ENUM and SET**

| JavaScript Type | To MySQL `ENUM` | To MySQL `SET` |
| --- | --- | --- |
| String | Preserve value; check whether string is valid `ENUM` value | Preserve value; check whether string is valid `SET` value |
| `null`, `undefined` | `NULL` | `NULL` |
| `Set` | Error | Convert to comma-separated string; check whether string is valid `SET` value |
| Any other type | Error | Error |

Additional notes

- All values used in or for `ENUM` or `SET` values or their JavaScript equivalents must employ the `utf8mb4` character set. See [Section 12.9.1, “The utf8mb4 Character Set (4-Byte UTF-8 Unicode Encoding)”](charset-unicode-utf8mb4.md), for more information.
- The server SQL mode can affect how an invalid JavaScript value is handled when attempting to insert it into an `ENUM` or `SET` column. When strict mode is in effect (the default), an invalid value throws an error; otherwise, an empty string is inserted, with a warning. See [Section 7.1.11, “Server SQL Modes”](sql-mode.md).

**Conversion to and from MySQL DECIMAL and NUMERIC.** MySQL decimal types ([`DECIMAL`](fixed-point-types.md) and [`NUMERIC`](fixed-point-types.md)) are converted to either of JavaScript `String` or `Number`, depending on the value of `session.options.decimalType` (`STRING` or `NUMBER`, respectively). The default behavior is to convert such values to `String`.

To set this variable on the session level so that MySQL decimal types are converted to `Number` by default instead, call [`mle_set_session_state()`](srjs-session-info.md) like this:

```
mle_set_session_state("decimalType":"NUMBER")
```

The MLE stored program cache must be empty when this function is invoked; it is not empty, you can clear it using [`mle_session_reset()`](srjs-session-info.md). See the description of [`mle_set_session_state()`](srjs-session-info.md) for more information.

To set the `decimalType` option within a JavaScript stored routine, use [`Session.setOptions()`](srjsapi-session.md), as shown here:

```
session.setOptions('{"decimalType":"mysql.DecimalType.NUMBER"}')
```

This sets the default for conversion of MySQL decimal values to `Number` for the lifetime of the routine. Use `mysql.DecimalType.STRING` to make `String` the default.

Rules for conversion of JavaScript values to the MySQL `DECIMAL` type (or its alias `NUMERIC`) are shown in the following table:

**Table 27.8 Type Conversion: JavaScript types to MySQL DECIMAL**

| JavaScript Type | Returns |
| --- | --- |
| `Object`, `Array`, or `Symbol` | Error: Conversion not supported |
| `Boolean`, `Number`, `String`, or `BigInt` | `DECIMAL` value |
| `null`, `undefined` | SQL `NULL` |

The maximum which a decimal value can hold is determined by the precision and scale of ``DECIMAL(*`M`*,       *`D`*)``, where *`M`* is the precision (maximum number of digits) in the range 1-65, and *`D`* is scale (the number of digits to the right of the decimal point, with the range 0-30. In addition, *`M`* must be greater than or equal to *`D`*. (See [Section 13.1.3, “Fixed-Point Types (Exact Value) - DECIMAL, NUMERIC”](fixed-point-types.md), for more information.)

In the event that a decimal value exceeds the range specified by ``DECIMAL(*`M`*,       *`D`*)`` or cannot be stored within the constraints of ``DECIMAL(*`M`*,       *`D`*)``, the behavior depends on the server SQL mode (see [Section 7.1.11, “Server SQL Modes”](sql-mode.md)), as follows:

- *Strict SQL Mode*: An error is raised, and the operation fails.
- *Otherwise*: The value is automatically capped to the nearest valid minimum or maximum value for the range given, and a warning is issued.

**Time zone support.** A JavaScript stored program uses the MySQL session timezone in effect at the time it is first invoked. This time zone remains in effect for this stored program for the duration of the session in the session.

Changing the MySQL session time zone is not automatically reflected in stored programs which have been used and thus are already cached. To make them use the new time zone, call [`mle_session_reset()`](srjs-session-info.md) to clear the cache; after this, stored programs use the new time zone.

Supported time zone types are listed here:

- Time zone offsets from UTC, such as `+11:00` or `-07:15`.
- Timezones defined in the [IANA time zone database](https://www.iana.org/time-zones) are supported, with the exception of configurations using leap seconds. For example, `Pacific/Nauru`, `Japan`, and `MET` are supported, while `leap/Pacific/Nauru` and `right/Pacific/Nauru` are not.

Range checks and invalid type conversion checks are performed following stored program execution. Casting is done inside JavaScript using type constructors such as `Number()` and `String()`; rounding to `Integer` is performed using `Math.round()`.

An input argument (`IN` or `INOUT` parameter) named in a JavaScript stored program definition is accessible from within the routine body using the same argument identifier. Output arguments (`INOUT` and `OUT` parameters) are also available in JavaScript stored procedures. The same argument identifier can be used to set the value using the JavaScript assignment (`=`) operator. As with SQL stored procedure `OUT` arguments, the initial value is set to JavaScript `null`.

You should *not* override program arguments using `let`, `var`, or `const` inside JavaScript stored programs. Doing so turns them into variables which are local to the program, and makes any values passed into the program using the same-named parameters inaccessible.

Example:

```
mysql> CREATE FUNCTION myfunc(x INT)
    ->   RETURNS INT LANGUAGE JAVASCRIPT AS
    -> $$
    $>   var x
    $>   
    $>   return 2*x
    $> $$
    -> ;
Query OK, 0 rows affected (0.03 sec)

mysql> SELECT myfunc(10);
ERROR 6000 (HY000): MLE-Type> Cannot convert value 'NaN' to INT 
from MLE in 'myfunc(10)'
```

The JavaScript `return` statement should be used to return scalar values in stored functions. In stored procedures, this statement does not return a value, and merely exits the code block (this may or may not also exit the routine depending on program flow). `return` cannot be used to set stored procedure `OUT` or `INOUT` argument values; these must be set explicitly within the routine.

For information about accessing MySQL stored procedures and stored functions from within JavaScript stored routines, see [Section 27.3.6.10, “Stored Routine API”](srjsapi-routines.md).