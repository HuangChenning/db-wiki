---
title: Chapter 12 Functions and Operators
book: MySQL 5.6 Reference Manual
version: "5.6"
source: "MySQL/MySQL5.6/sources/refman-5.6-en.pdf#page=1451"
tags:
  - mysql
  - mysql-5.6
  - reference-manual
---

## Table of Contents

12.1 Built-In Function and Operator Reference .............................................................................. 1424

12.2 Loadable Function Reference ................................................................................................ 1442

12.3 Type Conversion in Expression Evaluation ............................................................................. 1442

12.4 Operators ............................................................................................................................. 1445

12.4.1 Operator Precedence ................................................................................................. 1446

12.4.2 Comparison Functions and Operators ......................................................................... 1447

12.4.3 Logical Operators ....................................................................................................... 1454

12.4.4 Assignment Operators ................................................................................................ 1456

12.5 Flow Control Functions .......................................................................................................... 1457

12.6 Numeric Functions and Operators .......................................................................................... 1459

12.6.1 Arithmetic Operators ................................................................................................... 1460

12.6.2 Mathematical Functions .............................................................................................. 1462

12.7 Date and Time Functions ...................................................................................................... 1471

12.8 String Functions and Operators ............................................................................................. 1493

12.8.1 String Comparison Functions and Operators ................................................................ 1510

12.8.2 Regular Expressions .................................................................................................. 1513

12.8.3 Character Set and Collation of Function Results .......................................................... 1519

12.9 What Calendar Is Used By MySQL? ...................................................................................... 1520

12.10 Full-Text Search Functions .................................................................................................. 1521

12.10.1 Natural Language Full-Text Searches ........................................................................ 1522

12.10.2 Boolean Full-Text Searches ...................................................................................... 1525

12.10.3 Full-Text Searches with Query Expansion .................................................................. 1531

12.10.4 Full-Text Stopwords .................................................................................................. 1532

12.10.5 Full-Text Restrictions ................................................................................................ 1536

12.10.6 Fine-Tuning MySQL Full-Text Search ........................................................................ 1537

12.10.7 Adding a User-Defined Collation for Full-Text Indexing ............................................... 1540

12.11 Cast Functions and Operators ............................................................................................. 1541

12.12 XML Functions .................................................................................................................... 1548

12.13 Bit Functions and Operators ................................................................................................ 1559

12.14 Encryption and Compression Functions ................................................................................ 1561

12.15 Locking Functions ............................................................................................................... 1571

12.16 Information Functions .......................................................................................................... 1572

12.17 Spatial Analysis Functions ................................................................................................... 1583

12.17.1 Spatial Function Reference ....................................................................................... 1583

12.17.2 Argument Handling by Spatial Functions ................................................................... 1586

12.17.3 Functions That Create Geometry Values from WKT Values ........................................ 1587

12.17.4 Functions That Create Geometry Values from WKB Values ........................................ 1589

12.17.5 MySQL-Specific Functions That Create Geometry Values ........................................... 1590

12.17.6 Geometry Format Conversion Functions .................................................................... 1591

12.17.7 Geometry Property Functions .................................................................................... 1592

12.17.8 Spatial Operator Functions ........................................................................................ 1600

12.17.9 Functions That Test Spatial Relations Between Geometry Objects .............................. 1601

12.18 Functions Used with Global Transaction IDs ......................................................................... 1605

12.19 Aggregate Functions ........................................................................................................... 1607

12.19.1 Aggregate Function Descriptions ............................................................................... 1607

12.19.2 GROUP BY Modifiers ............................................................................................... 1612

12.19.3 MySQL Handling of GROUP BY ............................................................................... 1615

12.20 Miscellaneous Functions ...................................................................................................... 1616 Built-In Function and Operator Reference

12.21 Precision Math .................................................................................................................... 1623

12.21.1 Types of Numeric Values .......................................................................................... 1624

12.21.2 DECIMAL Data Type Characteristics ......................................................................... 1624

12.21.3 Expression Handling ................................................................................................. 1625

12.21.4 Rounding Behavior ................................................................................................... 1627

12.21.5 Precision Math Examples .......................................................................................... 1628 Expressions can be used at several points in SQL statements, such as in the `ORDER BY` or `HAVING`clauses of `SELECT` statements, in the `WHERE` clause of a `SELECT`, `DELETE`, or `UPDATE` statement, or in`SET` statements. Expressions can be written using values from several sources, such as literal values,column values, `NULL`, variables, built-in functions and operators, loadable functions, and stored functions(a type of stored object).

This chapter describes the built-in functions and operators that are permitted for writing expressions in MySQL. For information about loadable functions and stored functions, see Section 5.6, “MySQL Server Loadable Functions”, and Section 20.2, “Using Stored Routines”. For the rules describing how the server interprets references to different kinds of functions, see Section 9.2.5, “Function Name Parsing and Resolution”.

An expression that contains `NULL` always produces a `NULL` value unless otherwise indicated in the documentation for a particular function or operator.

Note By default, there must be no whitespace between a function name and the parenthesis following it. This helps the MySQL parser distinguish between function calls and references to tables or columns that happen to have the same name as a function. However, spaces around function arguments are permitted.

To tell the MySQL server to accept spaces after function names by starting it with the `--sql-mode=IGNORE_SPACE` option. (See Section 5.1.10, “Server SQL Modes”.) Individual client programs can request this behavior by using the`CLIENT_IGNORE_SPACE` option for `mysql_real_connect()`. In either case, all function names become reserved words.

For the sake of brevity, some examples in this chapter display the output from the `mysql` program in abbreviated form. Rather than showing examples in this format:

```
mysql> SELECT MOD(29,9);
+-----------+
| mod(29,9) |
+-----------+
|         2 |
+-----------+
1 rows in set (0.00 sec)
```

This format is used instead:

```
mysql> SELECT MOD(29,9);
-> 2
```

## 12.1 Built-In Function and Operator Reference

The following table lists each built-in (native) function and operator and provides a short description of each one. For a table listing functions that are loadable at runtime, see Section 12.2, “Loadable Function Reference”.

Built-In Function and Operator Reference Table 12.1 Built-In Functions and Operators Name Description Introduced Deprecated& Bitwise AND> Greater than operator`>>` Right shift`>=` Greater than or equal operator< Less than operator`<>`, `!=` Not equal operator`<<` Left shift`<=` Less than or equal operator`<=>` NULL-safe equal to operator%, `MOD` Modulo operator* Multiplication operator+ Addition operator

-  Minus operator
-  Change the sign of the

argument/ Division operator`:=` Assign a value= Assign a value (as part of a `SET` statement, or as part of the `SET` clause in an `UPDATE` statement)= Equal operator^ Bitwise XOR`ABS()` Return the absolute value`ACOS()` Return the arc cosine`ADDDATE()` Add time values(intervals) to a date value`ADDTIME()` Add time`AES_DECRYPT()` Decrypt using AES`AES_ENCRYPT()` Encrypt using AES`AND`, `&&` Logical AND`Area()` Return Polygon or MultiPolygon area`AsBinary()`, `AsWKB()` Convert from internal geometry format to WKB`ASCII()` Return numeric value of left-most character Built-In Function and Operator Reference Name Description Introduced Deprecated`ASIN()` Return the arc sine`AsText()`, `AsWKT()` Convert from internal geometry format to WKT`ATAN()` Return the arc tangent`ATAN2()`, `ATAN()` Return the arc tangent of the two arguments`AVG()` Return the average value of the argument`BENCHMARK()` Repeatedly execute an expression`BETWEEN ... AND ...` Whether a value is within a range of values`BIN()` Return a string containing binary representation of a number`BINARY` Cast a string to a binary string`BIT_AND()` Return bitwise AND`BIT_COUNT()` Return the number of bits that are set`BIT_LENGTH()` Return length of argument in bits`BIT_OR()` Return bitwise OR`BIT_XOR()` Return bitwise XOR`Buffer()` Return geometry of points within given distance from geometry`CASE` Case operator`CAST()` Cast a value as a certain type`CEIL()` Return the smallest integer value not less than the argument`CEILING()` Return the smallest integer value not less than the argument`Centroid()` Return centroid as a point`CHAR()` Return the character for each integer passed`CHAR_LENGTH()` Return number of characters in argument`CHARACTER_LENGTH()` Synonym for CHAR_LENGTH()Built-In Function and Operator Reference Name Description Introduced Deprecated`CHARSET()` Return the character set of the argument`COALESCE()` Return the first non-NULL argument`COERCIBILITY()` Return the collation coercibility value of the string argument`COLLATION()` Return the collation of the string argument`COMPRESS()` Return result as a binary string`CONCAT()` Return concatenated string`CONCAT_WS()` Return concatenate with separator`CONNECTION_ID()` Return the connection ID (thread ID) for the connection`Contains()` Whether MBR of one geometry contains MBR of another`CONV()` Convert numbers between different number bases`CONVERT()` Cast a value as a certain type`CONVERT_TZ()` Convert from one time zone to another`COS()` Return the cosine`COT()` Return the cotangent`COUNT()` Return a count of the number of rows returned`COUNT(DISTINCT)` Return the count of a number of different values`CRC32()` Compute a cyclic redundancy check value`Crosses()` Whether one geometry crosses another`CURDATE()` Return the current date`CURRENT_DATE()`, Synonyms for`CURRENT_DATE` CURDATE()`CURRENT_TIME()`, Synonyms for`CURRENT_TIME` CURTIME()Built-In Function and Operator Reference Name Description Introduced Deprecated`CURRENT_TIMESTAMP()`, Synonyms for NOW()

```
CURRENT_TIMESTAMP
```

`CURRENT_USER()`, The authenticated user`CURRENT_USER` name and host name`CURTIME()` Return the current time`DATABASE()` Return the default(current) database name`DATE()` Extract the date part of a date or datetime expression`DATE_ADD()` Add time values(intervals) to a date value`DATE_FORMAT()` Format date as specified`DATE_SUB()` Subtract a time value(interval) from a date`DATEDIFF()` Subtract two dates`DAY()` Synonym for DAYOFMONTH()`DAYNAME()` Return the name of the weekday`DAYOFMONTH()` Return the day of the month (0-31)`DAYOFWEEK()` Return the weekday index of the argument`DAYOFYEAR()` Return the day of the year (1-366)`DECODE()` Decode a string encrypted using ENCODE()`DEFAULT()` Return the default value for a table column`DEGREES()` Convert radians to degrees`DES_DECRYPT()` Decrypt a string`DES_ENCRYPT()` Encrypt a string`Dimension()` Dimension of geometry`Disjoint()` Whether MBRs of two geometries are disjoint`DIV` Integer division`ELT()` Return string at index number`ENCODE()` Encode a string`ENCRYPT()` Encrypt a string Built-In Function and Operator Reference Name Description Introduced Deprecated`EndPoint()` End Point of LineString`Envelope()` Return MBR of geometry`Equals()` Whether MBRs of two geometries are equal`EXP()` Raise to the power of`EXPORT_SET()` Return a string such that for every bit set in the value bits, you get an on string and for every unset bit, you get an off string`ExteriorRing()` Return exterior ring of Polygon`EXTRACT()` Extract part of a date`ExtractValue()` Extract a value from an XML string using XPath notation`FIELD()` Index (position) of first argument in subsequent arguments`FIND_IN_SET()` Index (position) of first argument within second argument`FLOOR()` Return the largest integer value not greater than the argument`FORMAT()` Return a number formatted to specified number of decimal places`FOUND_ROWS()` For a SELECT with a LIMIT clause, the number of rows that would be returned were there no LIMIT clause`FROM_BASE64()` Decode base64 encoded string and return result`FROM_DAYS()` Convert a day number to a date`FROM_UNIXTIME()` Format Unix timestamp as a date`GeomCollFromText()`, Return geometry`GeometryCollectionFromText()`collection from WKT`GeomCollFromWKB()`, Return geometry`GeometryCollectionFromWKB()`collection from WKB Built-In Function and Operator Reference Name Description Introduced Deprecated`GeometryCollection()`Construct geometry collection from geometries`GeometryN()` Return N-th geometry from geometry collection`GeometryType()` Return name of geometry type`GeomFromText()`, Return geometry from

```
GeometryFromText() WKT
```

`GeomFromWKB()`, Return geometry from

```
GeometryFromWKB()  WKB
```

`GET_FORMAT()` Return a date format string`GET_LOCK()` Get a named lock`GLength()` Return length of LineString`GREATEST()` Return the largest argument`GROUP_CONCAT()` Return a concatenated string`GTID_SUBSET()` Return true if all GTIDs in subset are also in set;

otherwise false.

`GTID_SUBTRACT()` Return all GTIDs in set that are not in subset.

`HEX()` Hexadecimal representation of decimal or string value`HOUR()` Extract the hour`IF()` If/else construct`IFNULL()` Null if/else construct`IN()` Whether a value is within a set of values`INET_ATON()` Return the numeric value of an IP address`INET_NTOA()` Return the IP address from a numeric value`INET6_ATON()` Return the numeric value of an IPv6 address`INET6_NTOA()` Return the IPv6 address from a numeric value`INSERT()` Insert substring at specified position up Built-In Function and Operator Reference Name Description Introduced Deprecated to specified number of characters`INSTR()` Return the index of the first occurrence of substring`InteriorRingN()` Return N-th interior ring of Polygon`Intersects()` Whether MBRs of two geometries intersect`INTERVAL()` Return the index of the argument that is less than the first argument`IS` Test a value against a boolean`IS_FREE_LOCK()` Whether the named lock is free`IS_IPV4()` Whether argument is an IPv4 address`IS_IPV4_COMPAT()` Whether argument is an IPv4-compatible address`IS_IPV4_MAPPED()` Whether argument is an IPv4-mapped address`IS_IPV6()` Whether argument is an IPv6 address`IS NOT` Test a value against a boolean`IS NOT NULL` NOT NULL value test`IS NULL` NULL value test`IS_USED_LOCK()` Whether the named lock is in use; return connection identifier if true`IsClosed()` Whether a geometry is closed and simple`IsEmpty()` Whether a geometry is empty`ISNULL()` Test whether the argument is NULL`IsSimple()` Whether a geometry is simple`LAST_DAY` Return the last day of the month for the argument`LAST_INSERT_ID()` Value of the AUTOINCREMENT Built-In Function and Operator Reference Name Description Introduced Deprecated column for the last INSERT`LCASE()` Synonym for LOWER()`LEAST()` Return the smallest argument`LEFT()` Return the leftmost number of characters as specified`LENGTH()` Return the length of a string in bytes`LIKE` Simple pattern matching`LineFromText()`, Construct LineString from

```
LineStringFromText()WKT
```

`LineFromWKB()`, Construct LineString from

```
LineStringFromWKB() WKB
```

`LineString()` Construct LineString from Point values`LN()` Return the natural logarithm of the argument`LOAD_FILE()` Load the named file`LOCALTIME()`, Synonym for NOW()

```
LOCALTIME
```

`LOCALTIMESTAMP`, Synonym for NOW()

```
LOCALTIMESTAMP()
```

`LOCATE()` Return the position of the first occurrence of substring`LOG()` Return the natural logarithm of the first argument`LOG10()` Return the base-10 logarithm of the argument`LOG2()` Return the base-2 logarithm of the argument`LOWER()` Return the argument in lowercase`LPAD()` Return the string argument, left-padded with the specified string`LTRIM()` Remove leading spaces`MAKE_SET()` Return a set of comma-separated strings that have the corresponding bit in bits set Built-In Function and Operator Reference Name Description Introduced Deprecated`MAKEDATE()` Create a date from the year and day of year`MAKETIME()` Create time from hour,minute, second`MASTER_POS_WAIT()` Block until the replica has read and applied all updates up to the specified position`MATCH()` Perform full-text search`MAX()` Return the maximum value`MBRContains()` Whether MBR of one geometry contains MBR of another`MBRDisjoint()` Whether MBRs of two geometries are disjoint`MBREqual()` Whether MBRs of two geometries are equal`MBRIntersects()` Whether MBRs of two geometries intersect`MBROverlaps()` Whether MBRs of two geometries overlap`MBRTouches()` Whether MBRs of two geometries touch`MBRWithin()` Whether MBR of one geometry is within MBR of another`MD5()` Calculate MD5 checksum`MICROSECOND()` Return the microseconds from argument`MID()` Return a substring starting from the specified position`MIN()` Return the minimum value`MINUTE()` Return the minute from the argument`MLineFromText()`, Construct MultiLineString

```
MultiLineStringFromText()from WKT
```

`MLineFromWKB()`, Construct MultiLineString

```
MultiLineStringFromWKB()from WKB
```

`MOD()` Return the remainder`MONTH()` Return the month from the date passed Built-In Function and Operator Reference Name Description Introduced Deprecated`MONTHNAME()` Return the name of the month`MPointFromText()`, Construct MultiPoint from

```
MultiPointFromText()WKT
```

`MPointFromWKB()`, Construct MultiPoint from

```
MultiPointFromWKB() WKB
```

`MPolyFromText()`, Construct MultiPolygon`MultiPolygonFromText()`from WKT`MPolyFromWKB()`, Construct MultiPolygon`MultiPolygonFromWKB()`from WKB`MultiLineString()` Contruct MultiLineString from LineString values`MultiPoint()` Construct MultiPoint from Point values`MultiPolygon()` Construct MultiPolygon from Polygon values`NAME_CONST()` Cause the column to have the given name`NOT`, ! Negates value`NOT BETWEEN ...` Whether a value is not`AND ...` within a range of values`NOT IN()` Whether a value is not within a set of values`NOT LIKE` Negation of simple pattern matching`NOT REGEXP` Negation of REGEXP`NOW()` Return the current date and time`NULLIF()` Return NULL if expr1 =expr2`NumGeometries()` Return number of geometries in geometry collection`NumInteriorRings()` Return number of interior rings in Polygon`NumPoints()` Return number of points in LineString`OCT()` Return a string containing octal representation of a number`OCTET_LENGTH()` Synonym for LENGTH()`OLD_PASSWORD()` Return the value of the Yes pre-4.1 implementation of PASSWORD Built-In Function and Operator Reference Name Description Introduced Deprecated`OR`, `||` Logical OR`ORD()` Return character code for leftmost character of the argument`Overlaps()` Whether MBRs of two geometries overlap`PASSWORD()` Calculate and return a password string`PERIOD_ADD()` Add a period to a year-month`PERIOD_DIFF()` Return the number of months between periods`PI()` Return the value of pi`Point()` Construct Point from coordinates`PointFromText()` Construct Point from WKT`PointFromWKB()` Construct Point from WKB`PointN()` Return N-th point from LineString`PolyFromText()`, Construct Polygon from

```
PolygonFromText()  WKT
```

`PolyFromWKB()`, Construct Polygon from

```
PolygonFromWKB()  WKB
```

`Polygon()` Construct Polygon from LineString arguments`POSITION()` Synonym for LOCATE()`POW()` Return the argument raised to the specified power`POWER()` Return the argument raised to the specified power`PROCEDURE ANALYSE()` Analyze the results of a query`QUARTER()` Return the quarter from a date argument`QUOTE()` Escape the argument for use in an SQL statement`RADIANS()` Return argument converted to radians`RAND()` Return a random floating-point value Built-In Function and Operator Reference Name Description Introduced Deprecated`RANDOM_BYTES()` Return a random byte 5.6.17 vector`REGEXP` Whether string matches regular expression`RELEASE_LOCK()` Release the named lock`REPEAT()` Repeat a string the specified number of times`REPLACE()` Replace occurrences of a specified string`REVERSE()` Reverse the characters in a string`RIGHT()` Return the specified rightmost number of characters`RLIKE` Whether string matches regular expression`ROUND()` Round the argument`ROW_COUNT()` The number of rows updated`RPAD()` Append string the specified number of times`RTRIM()` Remove trailing spaces`SCHEMA()` Synonym for DATABASE()`SEC_TO_TIME()` Converts seconds to'hh:mm:ss' format`SECOND()` Return the second (0-59)`SESSION_USER()` Synonym for USER()`SHA1()`, `SHA()` Calculate an SHA-1 160-bit checksum`SHA2()` Calculate an SHA-2 checksum`SIGN()` Return the sign of the argument`SIN()` Return the sine of the argument`SLEEP()` Sleep for a number of seconds`SOUNDEX()` Return a soundex string`SOUNDS LIKE` Compare sounds`SPACE()` Return a string of the specified number of spaces Built-In Function and Operator Reference Name Description Introduced Deprecated`SQL_THREAD_WAIT_AFTER_GTIDS()`Obsolete. Use Yes

```
WAIT_FOR_EXECUTED_GTID_SET().
```

`SQRT()` Return the square root of the argument`SRID()` Return spatial reference system ID for geometry`ST_Area()` Return Polygon or MultiPolygon area`ST_AsBinary()`, Convert from internal`ST_AsWKB()` geometry format to WKB`ST_AsText()`, Convert from internal`ST_AsWKT()` geometry format to WKT`ST_Buffer()` Return geometry of points within given distance from geometry`ST_Centroid()` Return centroid as a point`ST_Contains()` Whether one geometry contains another`ST_Crosses()` Whether one geometry crosses another`ST_Difference()` Return point set difference of two geometries`ST_Dimension()` Dimension of geometry`ST_Disjoint()` Whether one geometry is disjoint from another`ST_Distance()` The distance of one geometry from another`ST_EndPoint()` End Point of LineString`ST_Envelope()` Return MBR of geometry`ST_Equals()` Whether one geometry is equal to another`ST_ExteriorRing()` Return exterior ring of Polygon`ST_GeomCollFromText()`,Return geometry`ST_GeometryCollectionFromText()`,collection from WKT

```
ST_GeomCollFromTxt()
```

`ST_GeomCollFromWKB()`,Return geometry`ST_GeometryCollectionFromWKB()`collection from WKB`ST_GeometryN()` Return N-th geometry from geometry collection`ST_GeometryType()` Return name of geometry type Built-In Function and Operator Reference Name Description Introduced Deprecated`ST_GeomFromText()`, Return geometry from

```
ST_GeometryFromText()WKT
```

`ST_GeomFromWKB()`, Return geometry from

```
ST_GeometryFromWKB()WKB
```

`ST_InteriorRingN()` Return N-th interior ring of Polygon`ST_Intersection()` Return point set intersection of two geometries`ST_Intersects()` Whether one geometry intersects another`ST_IsClosed()` Whether a geometry is closed and simple`ST_IsEmpty()` Whether a geometry is empty`ST_IsSimple()` Whether a geometry is simple`ST_LineFromText()`, Construct LineString from

```
ST_LineStringFromText()WKT
```

`ST_LineFromWKB()`, Construct LineString from

```
ST_LineStringFromWKB()WKB
```

`ST_NumGeometries()` Return number of geometries in geometry collection`ST_NumInteriorRing()`,Return number of interior`ST_NumInteriorRings()`rings in Polygon`ST_NumPoints()` Return number of points in LineString`ST_Overlaps()` Whether one geometry overlaps another`ST_PointFromText()` Construct Point from WKT`ST_PointFromWKB()` Construct Point from WKB`ST_PointN()` Return N-th point from LineString`ST_PolyFromText()`, Construct Polygon from

```
ST_PolygonFromText()WKT
```

`ST_PolyFromWKB()`, Construct Polygon from

```
ST_PolygonFromWKB() WKB
```

`ST_SRID()` Return spatial reference system ID for geometry`ST_StartPoint()` Start Point of LineString Built-In Function and Operator Reference Name Description Introduced Deprecated`ST_SymDifference()` Return point set symmetric difference of two geometries`ST_Touches()` Whether one geometry touches another`ST_Union()` Return point set union of two geometries`ST_Within()` Whether one geometry is within another`ST_X()` Return X coordinate of Point`ST_Y()` Return Y coordinate of Point`StartPoint()` Start Point of LineString`STD()` Return the population standard deviation`STDDEV()` Return the population standard deviation`STDDEV_POP()` Return the population standard deviation`STDDEV_SAMP()` Return the sample standard deviation`STR_TO_DATE()` Convert a string to a date`STRCMP()` Compare two strings`SUBDATE()` Synonym for DATE_SUB() when invoked with three arguments`SUBSTR()` Return the substring as specified`SUBSTRING()` Return the substring as specified`SUBSTRING_INDEX()` Return a substring from a string before the specified number of occurrences of the delimiter`SUBTIME()` Subtract times`SUM()` Return the sum`SYSDATE()` Return the time at which the function executes`SYSTEM_USER()` Synonym for USER()`TAN()` Return the tangent of the argument Built-In Function and Operator Reference Name Description Introduced Deprecated`TIME()` Extract the time portion of the expression passed`TIME_FORMAT()` Format as time`TIME_TO_SEC()` Return the argument converted to seconds`TIMEDIFF()` Subtract time`TIMESTAMP()` With a single argument,this function returns the date or datetime expression; with two arguments, the sum of the arguments`TIMESTAMPADD()` Add an interval to a datetime expression`TIMESTAMPDIFF()` Return the difference of two datetime expressions, using the units specified`TO_BASE64()` Return the argument converted to a base-64 string`TO_DAYS()` Return the date argument converted to days`TO_SECONDS()` Return the date or datetime argument converted to seconds since Year 0`Touches()` Whether one geometry touches another`TRIM()` Remove leading and trailing spaces`TRUNCATE()` Truncate to specified number of decimal places`UCASE()` Synonym for UPPER()`UNCOMPRESS()` Uncompress a string compressed`UNCOMPRESSED_LENGTH()`Return the length of a string before compression`UNHEX()` Return a string containing hex representation of a number`UNIX_TIMESTAMP()` Return a Unix timestamp`UpdateXML()` Return replaced XML fragment Built-In Function and Operator Reference Name Description Introduced Deprecated`UPPER()` Convert to uppercase`USER()` The user name and host name provided by the client`UTC_DATE()` Return the current UTC date`UTC_TIME()` Return the current UTC time`UTC_TIMESTAMP()` Return the current UTC date and time`UUID()` Return a Universal Unique Identifier (UUID)`UUID_SHORT()` Return an integer-valued universal identifier`VALIDATE_PASSWORD_STRENGTH()`Determine strength of password`VALUES()` Define the values to be used during an INSERT`VAR_POP()` Return the population standard variance`VAR_SAMP()` Return the sample variance`VARIANCE()` Return the population standard variance`VERSION()` Return a string that indicates the MySQL server version

```
WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS()Use
WAIT_FOR_EXECUTED_GTID_SET().
```

`WEEK()` Return the week number`WEEKDAY()` Return the weekday index`WEEKOFYEAR()` Return the calendar week of the date (1-53)`WEIGHT_STRING()` Return the weight string for a string`Within()` Whether MBR of one geometry is within MBR of another`X()` Return X coordinate of Point`XOR` Logical XOR`Y()` Return Y coordinate of Point Loadable Function Reference Name Description Introduced Deprecated`YEAR()` Return the year`YEARWEEK()` Return the year and week| Bitwise OR~ Bitwise inversion

## 12.2 Loadable Function Reference

The following table lists each function that is loadable at runtime and provides a short description of each one. For a table listing built-in functions and operators, see Section 12.1, “Built-In Function and Operator Reference”For general information about loadable functions, see Section 5.6, “MySQL Server Loadable Functions”.

Table 12.2 Loadable Functions Name Description Introduced`asymmetric_decrypt()` Decrypt ciphertext using private or 5.6.21 public key`asymmetric_derive()` Derive symmetric key from 5.6.21 asymmetric keys`asymmetric_encrypt()` Encrypt cleartext using private or 5.6.21 public key`asymmetric_sign()` Generate signature from digest 5.6.21`asymmetric_verify()` Verify that signature matches 5.6.21 digest`create_asymmetric_priv_key()`Create private key 5.6.21`create_asymmetric_pub_key()`Create public key 5.6.21`create_dh_parameters()` Generate shared DH secret 5.6.21`create_digest()` Generate digest from string 5.6.21`mysql_firewall_flush_status()`Reset firewall status variables`normalize_statement()` Normalize SQL statement to digest form`read_firewall_users()` Update firewall account profile cache`read_firewall_whitelist()` Update firewall account profile recorded-statement cache`set_firewall_mode()` Establish firewall account profile operational mode

## 12.3 Type Conversion in Expression Evaluation

When an operator is used with operands of different types, type conversion occurs to make the operands compatible. Some conversions occur implicitly. For example, MySQL automatically converts strings to numbers as necessary, and vice versa.

Type Conversion in Expression Evaluation

```
mysql> SELECT 1+'1';
-> 2
mysql> SELECT CONCAT(2,' test');
-> '2 test'
```

It is also possible to convert a number to a string explicitly using the `CAST()` function. Conversion occurs implicitly with the `CONCAT()` function because it expects string arguments.

```
mysql> SELECT 38.8, CAST(38.8 AS CHAR);
-> 38.8, '38.8'
mysql> SELECT 38.8, CONCAT(38.8);
-> 38.8, '38.8'
```

See later in this section for information about the character set of implicit number-to-string conversions,and for modified rules that apply to `CREATE TABLE ... SELECT` statements.

The following rules describe how conversion occurs for comparison operations:

- If one or both arguments are `NULL`, the result of the comparison is `NULL`, except for the `NULL`-safe `<=>`

equality comparison operator. For `NULL <=> NULL`, the result is true. No conversion is needed.

- If both arguments in a comparison operation are strings, they are compared as strings.
- If both arguments are integers, they are compared as integers.
- Hexadecimal values are treated as binary strings if not compared to a number.
- If one of the arguments is a `TIMESTAMP` or `DATETIME` column and the other argument is a constant,

the constant is converted to a timestamp before the comparison is performed. This is done to be more ODBC-friendly. This is not done for the arguments to `IN()`. To be safe, always use complete datetime, date, or time strings when doing comparisons. For example, to achieve best results when using `BETWEEN` with date or time values, use `CAST()` to explicitly convert the values to the desired data type.

A single-row subquery from a table or tables is not considered a constant. For example, if a subquery returns an integer to be compared to a `DATETIME` value, the comparison is done as two integers.

The integer is not converted to a temporal value. To compare the operands as `DATETIME` values, use`CAST()` to explicitly convert the subquery value to `DATETIME`.

- If one of the arguments is a decimal value, comparison depends on the other argument. The arguments

are compared as decimal values if the other argument is a decimal or integer value, or as floating-point values if the other argument is a floating-point value.

- In all other cases, the arguments are compared as floating-point (double-precision) numbers. For

example, a comparison of string and numeric operands takes place as a comparison of floating-point numbers.

For information about conversion of values from one temporal type to another, see Section 11.2.8,“Conversion Between Date and Time Types”.

The following examples illustrate conversion of strings to numbers for comparison operations:

```
mysql> SELECT 1 > '6x';
-> 0
mysql> SELECT 7 > '6x';
-> 1
mysql> SELECT 0 > 'x6';
-> 0
mysql> SELECT 0 = 'x6';
-> 1
```

Type Conversion in Expression Evaluation For comparisons of a string column with a number, MySQL cannot use an index on the column to look up the value quickly. If `str_col` is an indexed string column, the index cannot be used when performing the lookup in the following statement:

```
SELECT * FROM tbl_name WHERE str_col=1;
```

The reason for this is that there are many different strings that may convert to the value 1, such as `'1'`, '`1'`, or `'1a'`.

Comparisons between floating-point numbers and large values of `INTEGER` type are approximate because the integer is converted to double-precision floating point before comparison, which is not capable of representing all 64-bit integers exactly. For example, the integer value 253 + 1 is not representable as a float, and is rounded to 253 or 253 + 2 before a float comparison, depending on the platform.

To illustrate, only the first of the following comparisons compares equal values, but both comparisons return true (1):

```
mysql> SELECT '9223372036854775807' = 9223372036854775807;
-> 1
mysql> SELECT '9223372036854775807' = 9223372036854775806;
-> 1
```

When conversions from string to floating-point and from integer to floating-point occur, they do not necessarily occur the same way. The integer may be converted to floating-point by the CPU, whereas the string is converted digit by digit in an operation that involves floating-point multiplications. Also, results can be affected by factors such as computer architecture or the compiler version or optimization level. One way to avoid such problems is to use `CAST()` so that a value is not converted implicitly to a float-point number:

```
mysql> SELECT CAST('9223372036854775807' AS UNSIGNED) = 9223372036854775806;
-> 0
```

For more information about floating-point comparisons, see Section B.3.4.8, “Problems with Floating-Point Values”.

The server includes `dtoa`, a conversion library that provides the basis for improved conversion between string or `DECIMAL` values and approximate-value (`FLOAT`/`DOUBLE`) numbers:

- Consistent conversion results across platforms, which eliminates, for example, Unix versus Windows

conversion differences.

- Accurate representation of values in cases where results previously did not provide sufficient precision,

such as for values close to IEEE limits.

- Conversion of numbers to string format with the best possible precision. The precision of `dtoa` is always

the same or better than that of the standard C library functions.

Because the conversions produced by this library differ in some cases from non-`dtoa` results, the potential exists for incompatibilities in applications that rely on previous results. For example, applications that depend on a specific exact result from previous conversions might need adjustment to accommodate additional precision.

The `dtoa` library provides conversions with the following properties. D represents a value with a `DECIMAL`or string representation, and F represents a floating-point number in native binary (IEEE) format.

- F -> D conversion is done with the best possible precision, returning D as the shortest string that yields F

when read back in and rounded to the nearest value in native binary format as specified by IEEE.

- D -> F conversion is done such that F is the nearest native binary number to the input decimal string D.

Operators These properties imply that F -> D -> F conversions are lossless unless F is `-inf`, `+inf`, or `NaN`. The latter values are not supported because the SQL standard defines them as invalid values for `FLOAT` or `DOUBLE`.

For D -> F -> D conversions, a sufficient condition for losslessness is that D uses 15 or fewer digits of precision, is not a denormal value, `-inf`, `+inf`, or `NaN`. In some cases, the conversion is lossless even if D has more than 15 digits of precision, but this is not always the case.

Implicit conversion of a numeric or temporal value to string produces a value that has a character set and collation determined by the `character_set_connection` and `collation_connection` system variables. (These variables commonly are set with `SET NAMES`. For information about connection character sets, see Section 10.4, “Connection Character Sets and Collations”.)This means that such a conversion results in a character (nonbinary) string (a `CHAR`, `VARCHAR`, or`LONGTEXT` value), except in the case that the connection character set is set to `binary`. In that case, the conversion result is a binary string (a `BINARY`, `VARBINARY`, or `LONGBLOB` value).

For integer expressions, the preceding remarks about expression evaluation apply somewhat differently for expression assignment; for example, in a statement such as this:

```
CREATE TABLE t SELECT integer_expr;
```

In this case, the table in the column resulting from the expression has type `INT` or `BIGINT` depending on the length of the integer expression. If the maximum length of the expression does not fit in an `INT`,`BIGINT` is used instead. The length is taken from the `max_length` value of the `SELECT` result set metadata (see C API Basic Data Structures). This means that you can force a `BIGINT` rather than `INT` by use of a sufficiently long expression:

```
CREATE TABLE t SELECT 000000000000000000000;
```

## 12.4 Operators

Table 12.3 Operators Name Description& Bitwise AND> Greater than operator`>>` Right shift`>=` Greater than or equal operator< Less than operator`<>`, `!=` Not equal operator`<<` Left shift`<=` Less than or equal operator`<=>` NULL-safe equal to operator%, `MOD` Modulo operator* Multiplication operator+ Addition operator

-  Minus operator
-  Change the sign of the argument

/ Division operator Operator Precedence Name Description`:=` Assign a value= Assign a value (as part of a `SET` statement, or as part of the `SET` clause in an `UPDATE` statement)= Equal operator^ Bitwise XOR`AND`, `&&` Logical AND`BETWEEN ... AND ...` Whether a value is within a range of values`BINARY` Cast a string to a binary string`CASE` Case operator`DIV` Integer division`IN()` Whether a value is within a set of values`IS` Test a value against a boolean`IS NOT` Test a value against a boolean`IS NOT NULL` NOT NULL value test`IS NULL` NULL value test`LIKE` Simple pattern matching`NOT`, ! Negates value`NOT BETWEEN ... AND ...` Whether a value is not within a range of values`NOT IN()` Whether a value is not within a set of values`NOT LIKE` Negation of simple pattern matching`NOT REGEXP` Negation of REGEXP`OR`, `||` Logical OR`REGEXP` Whether string matches regular expression`RLIKE` Whether string matches regular expression`SOUNDS LIKE` Compare sounds`XOR` Logical XOR| Bitwise OR~ Bitwise inversion

### 12.4.1 Operator Precedence

Operator precedences are shown in the following list, from highest precedence to the lowest. Operators that are shown together on a line have the same precedence.

```
INTERVAL
BINARY, COLLATE
!
- (unary minus), ~ (unary bit inversion)
^
*, /, DIV, %, MOD
-, +
<<, >>
&
|
= (comparison), <=>, >=, >, <=, <, <>, !=, IS, LIKE, REGEXP, IN
```

Comparison Functions and Operators

```
BETWEEN, CASE, WHEN, THEN, ELSE
NOT
AND, &&
XOR
OR, ||
= (assignment), :=
```

The precedence of = depends on whether it is used as a comparison operator (=) or as an assignment operator (=). When used as a comparison operator, it has the same precedence as `<=>`, `>=`, >, `<=`, <, `<>`,`!=`, `IS`, `LIKE`, `REGEXP`, and `IN()`. When used as an assignment operator, it has the same precedence as`:=`. Section 13.7.4.1, “SET Syntax for Variable Assignment”, and Section 9.4, “User-Defined Variables”,explain how MySQL determines which interpretation of = should apply.

For operators that occur at the same precedence level within an expression, evaluation proceeds left to right, with the exception that assignments evaluate right to left.

The precedence and meaning of some operators depends on the SQL mode:

- By default, `||` is a logical `OR` operator. With `PIPES_AS_CONCAT` enabled, `||` is string concatenation,

with a precedence between ^ and the unary operators.

- By default, ! has a higher precedence than `NOT`. With `HIGH_NOT_PRECEDENCE` enabled, ! and `NOT`

have the same precedence.

See Section 5.1.10, “Server SQL Modes”.

The precedence of operators determines the order of evaluation of terms in an expression. To override this order and group terms explicitly, use parentheses. For example:

```
mysql> SELECT 1+2*3;
-> 7
mysql> SELECT (1+2)*3;
-> 9
```

### 12.4.2 Comparison Functions and Operators

Table 12.4 Comparison Operators Name Description> Greater than operator`>=` Greater than or equal operator< Less than operator`<>`, `!=` Not equal operator`<=` Less than or equal operator`<=>` NULL-safe equal to operator= Equal operator`BETWEEN ... AND ...` Whether a value is within a range of values`COALESCE()` Return the first non-NULL argument`GREATEST()` Return the largest argument`IN()` Whether a value is within a set of values`INTERVAL()` Return the index of the argument that is less than the first argument Comparison Functions and Operators Name Description`IS` Test a value against a boolean`IS NOT` Test a value against a boolean`IS NOT NULL` NOT NULL value test`IS NULL` NULL value test`ISNULL()` Test whether the argument is NULL`LEAST()` Return the smallest argument`LIKE` Simple pattern matching`NOT BETWEEN ... AND ...` Whether a value is not within a range of values`NOT IN()` Whether a value is not within a set of values`NOT LIKE` Negation of simple pattern matching`STRCMP()` Compare two strings Comparison operations result in a value of 1 (`TRUE`), 0 (`FALSE`), or `NULL`. These operations work for both numbers and strings. Strings are automatically converted to numbers and numbers to strings as necessary.

The following relational comparison operators can be used to compare not only scalar operands, but row operands:

```
=  >  <  >=  <=  <>  !=
```

The descriptions for those operators later in this section detail how they work with row operands. For additional examples of row comparisons in the context of row subqueries, see Section 13.2.10.5, “Row Subqueries”.

Some of the functions in this section return values other than 1 (`TRUE`), 0 (`FALSE`), or `NULL`. `LEAST()` and`GREATEST()` are examples of such functions; Section 12.3, “Type Conversion in Expression Evaluation”,describes the rules for comparison operations performed by these and similar functions for determining their return values.

To convert a value to a specific type for comparison purposes, you can use the `CAST()` function. String values can be converted to a different character set using `CONVERT()`. See Section 12.11, “Cast Functions and Operators”.

By default, string comparisons are not case-sensitive and use the current character set. The default is`latin1` (cp1252 West European), which also works well for English.

- =

Equal:

```
mysql> SELECT 1 = 0;
-> 0
mysql> SELECT '0' = 0;
-> 1
mysql> SELECT '0.0' = 0;
-> 1
mysql> SELECT '0.01' = 0;
-> 0
mysql> SELECT '.01' = 0.01;
-> 1
```

Comparison Functions and Operators For row comparisons, `(a, b) = (x, y)` is equivalent to:

```
(a = x) AND (b = y)
- <=>
```

`NULL`-safe equal. This operator performs an equality comparison like the = operator, but returns 1 rather than `NULL` if both operands are `NULL`, and 0 rather than `NULL` if one operand is `NULL`.

The `<=>` operator is equivalent to the standard SQL `IS NOT DISTINCT FROM` operator.

```
mysql> SELECT 1 <=> 1, NULL <=> NULL, 1 <=> NULL;
-> 1, 1, 0
mysql> SELECT 1 = 1, NULL = NULL, 1 = NULL;
-> 1, NULL, NULL
```

For row comparisons, `(a, b) <=> (x, y)` is equivalent to:

```
(a <=> x) AND (b <=> y)
```

- `<>`, `!=`

Not equal:

```
mysql> SELECT '.01' <> '0.01';
-> 1
mysql> SELECT .01 <> '0.01';
-> 0
mysql> SELECT 'zapp' <> 'zappp';
-> 1
```

For row comparisons, `(a, b) <> (x, y)` and `(a, b) != (x, y)` are equivalent to:

```
(a <> x) OR (b <> y)
```

- `<=`

Less than or equal:

```
mysql> SELECT 0.1 <= 2;
-> 1
```

For row comparisons, `(a, b) <= (x, y)` is equivalent to:

```
(a < x) OR ((a = x) AND (b <= y))
```

- <

Less than:

```
mysql> SELECT 2 < 2;
-> 0
```

For row comparisons, `(a, b) < (x, y)` is equivalent to:

```
(a < x) OR ((a = x) AND (b < y))
```

- `>=`

Greater than or equal:

```
mysql> SELECT 2 >= 2;
```

Comparison Functions and Operators

```
-> 1
```

For row comparisons, `(a, b) >= (x, y)` is equivalent to:

```
(a > x) OR ((a = x) AND (b >= y))
```

- >

Greater than:

```
mysql> SELECT 2 > 2;
-> 0
```

For row comparisons, `(a, b) > (x, y)` is equivalent to:

```
(a > x) OR ((a = x) AND (b > y))
- expr BETWEEN min AND max
```

If `expr` is greater than or equal to `min` and `expr` is less than or equal to `max`, `BETWEEN` returns 1,otherwise it returns 0. This is equivalent to the expression `(min <= expr AND expr <= max)` if all the arguments are of the same type. Otherwise type conversion takes place according to the rules described in Section 12.3, “Type Conversion in Expression Evaluation”, but applied to all the three arguments.

```
mysql> SELECT 2 BETWEEN 1 AND 3, 2 BETWEEN 3 and 1;
-> 1, 0
mysql> SELECT 1 BETWEEN 2 AND 3;
-> 0
mysql> SELECT 'b' BETWEEN 'a' AND 'c';
-> 1
mysql> SELECT 2 BETWEEN 2 AND '3';
-> 1
mysql> SELECT 2 BETWEEN 2 AND 'x-3';
-> 0
```

For best results when using `BETWEEN` with date or time values, use `CAST()` to explicitly convert the values to the desired data type. Examples: If you compare a `DATETIME` to two `DATE` values, convert the`DATE` values to `DATETIME` values. If you use a string constant such as `'2001-1-1'` in a comparison to a `DATE`, cast the string to a `DATE`.

```
- expr NOT BETWEEN min AND max
```

This is the same as `NOT (expr BETWEEN min AND max)`.

```
- COALESCE(value,...)
```

Returns the first non-`NULL` value in the list, or `NULL` if there are no non-`NULL` values.

The return type of `COALESCE()` is the aggregated type of the argument types.

```
mysql> SELECT COALESCE(NULL,1);
-> 1
mysql> SELECT COALESCE(NULL,NULL,NULL);
-> NULL
- GREATEST(value1,value2,...)
```

With two or more arguments, returns the largest (maximum-valued) argument. The arguments are compared using the same rules as for `LEAST()`.

```
mysql> SELECT GREATEST(2,0);
```

Comparison Functions and Operators

```
-> 2
mysql> SELECT GREATEST(34.0,3.0,5.0,767.0);
-> 767.0
mysql> SELECT GREATEST('B','A','C');
-> 'C'
```

`GREATEST()` returns `NULL` if any argument is `NULL`.

```
- expr IN (value,...)
```

Returns 1 (true) if `expr` is equal to any of the values in the `IN()` list, else returns 0 (false).

Type conversion takes place according to the rules described in Section 12.3, “Type Conversion in Expression Evaluation”, applied to all the arguments. If no type conversion is needed for the values in the `IN()` list, they are all constants of the same type, and `expr` can be compared to each of them as a value of the same type (possibly after type conversion), an optimization takes place. The values the list are sorted and the search for `expr` is done using a binary search, which makes the `IN()` operation very quick.

```
mysql> SELECT 2 IN (0,3,5,7);
-> 0
mysql> SELECT 'wefwf' IN ('wee','wefwf','weg');
-> 1
```

`IN()` can be used to compare row constructors:

```
mysql> SELECT (3,4) IN ((1,2), (3,4));
-> 1
mysql> SELECT (3,4) IN ((1,2), (3,5));
-> 0
```

You should never mix quoted and unquoted values in an `IN()` list because the comparison rules for quoted values (such as strings) and unquoted values (such as numbers) differ. Mixing types may therefore lead to inconsistent results. For example, do not write an `IN()` expression like this:

```
SELECT val1 FROM tbl1 WHERE val1 IN (1,2,'a');
```

Instead, write it like this:

```
SELECT val1 FROM tbl1 WHERE val1 IN ('1','2','a');
```

Implicit type conversion may produce nonintuitive results:

```
mysql> SELECT 'a' IN (0), 0 IN ('b');
-> 1, 1
```

In both cases, the comparison values are converted to floating-point values, yielding 0.0 in each case,and a comparison result of 1 (true).

The number of values in the `IN()` list is only limited by the `max_allowed_packet` value.

To comply with the SQL standard, `IN()` returns `NULL` not only if the expression on the left hand side is`NULL`, but also if no match is found in the list and one of the expressions in the list is `NULL`.

`IN()` syntax can also be used to write certain types of subqueries. See Section 13.2.10.3, “Subqueries with ANY, IN, or SOME”.

```
- expr NOT IN (value,...)
```

This is the same as `NOT (expr IN (value,...))`.

Comparison Functions and Operators

```
- INTERVAL(N,N1,N2,N3,...)
```

Returns 0 if N < `N1`, 1 if N < `N2` and so on or `-1` if N is `NULL`. All arguments are treated as integers. It is required that `N1` < `N2` < `N3` < `...` < `Nn` for this function to work correctly. This is because a binary search is used (very fast).

```
mysql> SELECT INTERVAL(23, 1, 15, 17, 30, 44, 200);
-> 3
mysql> SELECT INTERVAL(10, 1, 10, 100, 1000);
-> 2
mysql> SELECT INTERVAL(22, 23, 30, 44, 200);
-> 0
- IS boolean_value
```

Tests a value against a boolean value, where `boolean_value` can be `TRUE`, `FALSE`, or `UNKNOWN`.

```
mysql> SELECT 1 IS TRUE, 0 IS FALSE, NULL IS UNKNOWN;
-> 1, 1, 1
- IS NOT boolean_value
```

Tests a value against a boolean value, where `boolean_value` can be `TRUE`, `FALSE`, or `UNKNOWN`.

```
mysql> SELECT 1 IS NOT UNKNOWN, 0 IS NOT UNKNOWN, NULL IS NOT UNKNOWN;
-> 1, 1, 0
- IS NULL
```

Tests whether a value is `NULL`.

```
mysql> SELECT 1 IS NULL, 0 IS NULL, NULL IS NULL;
-> 0, 0, 1
```

To work well with ODBC programs, MySQL supports the following extra features when using `IS NULL`:

- If `sql_auto_is_null` variable is set to 1, then after a statement that successfully inserts an

automatically generated `AUTO_INCREMENT` value, you can find that value by issuing a statement of the following form:

```
SELECT * FROM tbl_name WHERE auto_col IS NULL
```

If the statement returns a row, the value returned is the same as if you invoked the`LAST_INSERT_ID()` function. For details, including the return value after a multiple-row insert, see Comparison Functions and Operators Section 12.16, “Information Functions”. If no `AUTO_INCREMENT` value was successfully inserted, the`SELECT` statement returns no row.

The behavior of retrieving an `AUTO_INCREMENT` value by using an `IS NULL` comparison can be disabled by setting `sql_auto_is_null = 0`. See Section 5.1.7, “Server System Variables”.

The default value of `sql_auto_is_null` is 0.

- For `DATE` and `DATETIME` columns that are declared as `NOT NULL`, you can find the special date

`'0000-00-00'` by using a statement like this:

```
SELECT * FROM tbl_name WHERE date_column IS NULL
```

This is needed to get some ODBC applications to work because ODBC does not support a`'0000-00-00'` date value.

See Obtaining Auto-Increment Values, and the description for the `FLAG_AUTO_IS_NULL` option at Connector/ODBC Connection Parameters.

```
- IS NOT NULL
```

Tests whether a value is not `NULL`.

```
mysql> SELECT 1 IS NOT NULL, 0 IS NOT NULL, NULL IS NOT NULL;
-> 1, 1, 0
- ISNULL(expr)
```

If `expr` is `NULL`, `ISNULL()` returns 1, otherwise it returns 0.

```
mysql> SELECT ISNULL(1+1);
-> 0
mysql> SELECT ISNULL(1/0);
-> 1
```

`ISNULL()` can be used instead of = to test whether a value is `NULL`. (Comparing a value to `NULL` using= always yields `NULL`.)The `ISNULL()` function shares some special behaviors with the `IS NULL` comparison operator. See the description of `IS NULL`.

Logical Operators

```
- LEAST(value1,value2,...)
```

With two or more arguments, returns the smallest (minimum-valued) argument. The arguments are compared using the following rules:

- If any argument is `NULL`, the result is `NULL`. No comparison is needed.
- If all arguments are integer-valued, they are compared as integers.
- If at least one argument is double precision, they are compared as double-precision values.

Otherwise, if at least one argument is a `DECIMAL` value, they are compared as `DECIMAL` values.

- If the arguments comprise a mix of numbers and strings, they are compared as numbers.
- If any argument is a nonbinary (character) string, the arguments are compared as nonbinary strings.
- In all other cases, the arguments are compared as binary strings.

The return type of `LEAST()` is the aggregated type of the comparison argument types.

```
mysql> SELECT LEAST(2,0);
-> 0
mysql> SELECT LEAST(34.0,3.0,5.0,767.0);
-> 3.0
mysql> SELECT LEAST('B','A','C');
-> 'A'
```

### 12.4.3 Logical Operators

Table 12.5 Logical Operators Name Description`AND`, `&&` Logical AND`NOT`, ! Negates value`OR`, `||` Logical OR`XOR` Logical XOR In SQL, all logical operators evaluate to `TRUE`, `FALSE`, or `NULL` (`UNKNOWN`). In MySQL, these are implemented as 1 (`TRUE`), 0 (`FALSE`), and `NULL`. Most of this is common to different SQL database servers, although some servers may return any nonzero value for `TRUE`.

MySQL evaluates any nonzero, non-`NULL` value to `TRUE`. For example, the following statements all assess to `TRUE`:

```
mysql> SELECT 10 IS TRUE;
-> 1
mysql> SELECT -10 IS TRUE;
-> 1
mysql> SELECT 'string' IS NOT NULL;
-> 1
```

- `NOT`, !

Logical NOT. Evaluates to 1 if the operand is 0, to 0 if the operand is nonzero, and `NOT NULL` returns

```
NULL.
mysql> SELECT NOT 10;
-> 0
mysql> SELECT NOT 0;
```

Logical Operators

```
-> 1
mysql> SELECT NOT NULL;
-> NULL
mysql> SELECT ! (1+1);
-> 0
mysql> SELECT ! 1+1;
-> 1
```

The last example produces 1 because the expression evaluates the same way as `(!1)+1`.

- `AND`, `&&`

Logical AND. Evaluates to 1 if all operands are nonzero and not `NULL`, to 0 if one or more operands are 0, otherwise `NULL` is returned.

```
mysql> SELECT 1 AND 1;
-> 1
mysql> SELECT 1 AND 0;
-> 0
mysql> SELECT 1 AND NULL;
-> NULL
mysql> SELECT 0 AND NULL;
-> 0
mysql> SELECT NULL AND 0;
-> 0
```

- `OR`, `||`

Logical OR. When both operands are non-`NULL`, the result is 1 if any operand is nonzero, and 0 otherwise. With a `NULL` operand, the result is 1 if the other operand is nonzero, and `NULL` otherwise. If both operands are `NULL`, the result is `NULL`.

```
mysql> SELECT 1 OR 1;
-> 1
mysql> SELECT 1 OR 0;
-> 1
mysql> SELECT 0 OR 0;
-> 0
mysql> SELECT 0 OR NULL;
-> NULL
mysql> SELECT 1 OR NULL;
-> 1
```

Note If the `PIPES_AS_CONCAT` SQL mode is enabled, `||` signifies the SQL-standard string concatenation operator (like `CONCAT()`).

```
- XOR
```

Logical XOR. Returns `NULL` if either operand is `NULL`. For non-`NULL` operands, evaluates to 1 if an odd number of operands is nonzero, otherwise 0 is returned.

```
mysql> SELECT 1 XOR 1;
-> 0
mysql> SELECT 1 XOR 0;
-> 1
mysql> SELECT 1 XOR NULL;
-> NULL
mysql> SELECT 1 XOR 1 XOR 1;
-> 1
```

`a XOR b` is mathematically equal to `(a AND (NOT b)) OR ((NOT a) and b)`.

Assignment Operators

### 12.4.4 Assignment Operators

Table 12.6 Assignment Operators Name Description`:=` Assign a value= Assign a value (as part of a `SET` statement, or as part of the `SET` clause in an `UPDATE` statement)

- `:=`

Assignment operator. Causes the user variable on the left hand side of the operator to take on the value to its right. The value on the right hand side may be a literal value, another variable storing a value, or any legal expression that yields a scalar value, including the result of a query (provided that this value is a scalar value). You can perform multiple assignments in the same `SET` statement. You can perform multiple assignments in the same statement.

Unlike =, the `:=` operator is never interpreted as a comparison operator. This means you can use `:=` in any valid SQL statement (not just in `SET` statements) to assign a value to a variable.

```
mysql> SELECT @var1, @var2;
-> NULL, NULL
mysql> SELECT @var1 := 1, @var2;
-> 1, NULL
mysql> SELECT @var1, @var2;
-> 1, NULL
mysql> SELECT @var1, @var2 := @var1;
-> 1, 1
mysql> SELECT @var1, @var2;
-> 1, 1
mysql> SELECT @var1:=COUNT(*) FROM t1;
-> 4
mysql> SELECT @var1;
-> 4
```

You can make value assignments using `:=` in other statements besides `SELECT`, such as `UPDATE`, as shown here:

```
mysql> SELECT @var1;
-> 4
mysql> SELECT * FROM t1;
-> 1, 3, 5, 7
mysql> UPDATE t1 SET c1 = 2 WHERE c1 = @var1:= 1;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0
mysql> SELECT @var1;
-> 1
mysql> SELECT * FROM t1;
-> 2, 3, 5, 7
```

While it is also possible both to set and to read the value of the same variable in a single SQL statement using the `:=` operator, this is not recommended. Section 9.4, “User-Defined Variables”, explains why you should avoid doing this.

- =

This operator is used to perform value assignments in two cases, described in the next two paragraphs.

Flow Control Functions Within a `SET` statement, = is treated as an assignment operator that causes the user variable on the left hand side of the operator to take on the value to its right. (In other words, when used in a `SET`statement, = is treated identically to `:=`.) The value on the right hand side may be a literal value, another variable storing a value, or any legal expression that yields a scalar value, including the result of a query(provided that this value is a scalar value). You can perform multiple assignments in the same `SET`statement.

In the `SET` clause of an `UPDATE` statement, = also acts as an assignment operator; in this case,however, it causes the column named on the left hand side of the operator to assume the value given to the right, provided any `WHERE` conditions that are part of the `UPDATE` are met. You can make multiple assignments in the same `SET` clause of an `UPDATE` statement.

In any other context, = is treated as a comparison operator.

```
mysql> SELECT @var1, @var2;
-> NULL, NULL
mysql> SELECT @var1 := 1, @var2;
-> 1, NULL
mysql> SELECT @var1, @var2;
-> 1, NULL
mysql> SELECT @var1, @var2 := @var1;
-> 1, 1
mysql> SELECT @var1, @var2;
-> 1, 1
```

For more information, see Section 13.7.4.1, “SET Syntax for Variable Assignment”, Section 13.2.11,“UPDATE Statement”, and Section 13.2.10, “Subqueries”.

## 12.5 Flow Control Functions

Table 12.7 Flow Control Operators Name Description`CASE` Case operator`IF()` If/else construct`IFNULL()` Null if/else construct`NULLIF()` Return NULL if expr1 = expr2

```
- CASE value WHEN compare_value THEN result [WHEN compare_value THEN result
...] [ELSE result] END
CASE WHEN condition THEN result [WHEN condition THEN result ...] [ELSE
result] END
```

The first `CASE` syntax returns the `result` for the first `value=compare_value` comparison that is true.

The second syntax returns the result for the first condition that is true. If no comparison or condition is true, the result after `ELSE` is returned, or `NULL` if there is no `ELSE` part.

Note The syntax of the `CASE` operator described here differs slightly from that of the SQL `CASE` statement described in Section 13.6.5.1, “CASE Statement”, for use inside stored programs. The `CASE` statement cannot have an `ELSE NULL` clause,and it is terminated with `END CASE` instead of `END`.

Flow Control Functions The return type of a `CASE` expression result is the aggregated type of all result values.

```
mysql> SELECT CASE 1 WHEN 1 THEN 'one'
->     WHEN 2 THEN 'two' ELSE 'more' END;
-> 'one'
mysql> SELECT CASE WHEN 1>0 THEN 'true' ELSE 'false' END;
-> 'true'
mysql> SELECT CASE BINARY 'B'
->     WHEN 'a' THEN 1 WHEN 'b' THEN 2 END;
-> NULL
- IF(expr1,expr2,expr3)
```

If `expr1` is `TRUE` (`expr1 <> 0` and `expr1 IS NOT NULL`), `IF()` returns `expr2`. Otherwise, it returns

```
expr3.
```

Note There is also an `IF` statement, which differs from the `IF()` function described here. See Section 13.6.5.2, “IF Statement”.

If only one of `expr2` or `expr3` is explicitly `NULL`, the result type of the `IF()` function is the type of the non-`NULL` expression.

The default return type of `IF()` (which may matter when it is stored into a temporary table) is calculated as follows:

- If `expr2` or `expr3` produce a string, the result is a string.

If `expr2` and `expr3` are both strings, the result is case-sensitive if either string is case-sensitive.

- If `expr2` or `expr3` produce a floating-point value, the result is a floating-point value.
- If `expr2` or `expr3` produce an integer, the result is an integer.

```
mysql> SELECT IF(1>2,2,3);
-> 3
mysql> SELECT IF(1<2,'yes','no');
-> 'yes'
mysql> SELECT IF(STRCMP('test','test1'),'no','yes');
-> 'no'
- IFNULL(expr1,expr2)
```

If `expr1` is not `NULL`, `IFNULL()` returns `expr1`; otherwise it returns `expr2`.

```
mysql> SELECT IFNULL(1,0);
-> 1
mysql> SELECT IFNULL(NULL,10);
-> 10
mysql> SELECT IFNULL(1/0,10);
-> 10
mysql> SELECT IFNULL(1/0,'yes');
-> 'yes'
```

The default return type of `IFNULL(expr1,expr2)` is the more “general” of the two expressions, in the order `STRING`, `REAL`, or `INTEGER`. Consider the case of a table based on expressions or where MySQL must internally store a value returned by `IFNULL()` in a temporary table:

```
mysql> CREATE TABLE tmp SELECT IFNULL(1,'test') AS test;
```

Numeric Functions and Operators

```
mysql> DESCRIBE tmp;
+-------+--------------+------+-----+---------+-------+
| Field | Type         | Null | Key | Default | Extra |
+-------+--------------+------+-----+---------+-------+
| test  | varbinary(4) | NO   |     |         |       |
+-------+--------------+------+-----+---------+-------+
```

In this example, the type of the `test` column is `VARBINARY(4)` (a string type).

```
- NULLIF(expr1,expr2)
```

Returns `NULL` if `expr1 = expr2` is true, otherwise returns `expr1`. This is the same as `CASE WHEN`

```
expr1 = expr2 THEN NULL ELSE expr1 END.
```

The return value has the same type as the first argument.

```
mysql> SELECT NULLIF(1,1);
-> NULL
mysql> SELECT NULLIF(1,2);
-> 1
```

Note MySQL evaluates `expr1` twice if the arguments are not equal.

## 12.6 Numeric Functions and Operators

Table 12.8 Numeric Functions and Operators Name Description%, `MOD` Modulo operator* Multiplication operator+ Addition operator

-  Minus operator
-  Change the sign of the argument

/ Division operator`ABS()` Return the absolute value`ACOS()` Return the arc cosine`ASIN()` Return the arc sine`ATAN()` Return the arc tangent`ATAN2()`, `ATAN()` Return the arc tangent of the two arguments`CEIL()` Return the smallest integer value not less than the argument`CEILING()` Return the smallest integer value not less than the argument`CONV()` Convert numbers between different number bases`COS()` Return the cosine`COT()` Return the cotangent`CRC32()` Compute a cyclic redundancy check value`DEGREES()` Convert radians to degrees Arithmetic Operators Name Description`DIV` Integer division`EXP()` Raise to the power of`FLOOR()` Return the largest integer value not greater than the argument`LN()` Return the natural logarithm of the argument`LOG()` Return the natural logarithm of the first argument`LOG10()` Return the base-10 logarithm of the argument`LOG2()` Return the base-2 logarithm of the argument`MOD()` Return the remainder`PI()` Return the value of pi`POW()` Return the argument raised to the specified power`POWER()` Return the argument raised to the specified power`RADIANS()` Return argument converted to radians`RAND()` Return a random floating-point value`ROUND()` Round the argument`SIGN()` Return the sign of the argument`SIN()` Return the sine of the argument`SQRT()` Return the square root of the argument`TAN()` Return the tangent of the argument`TRUNCATE()` Truncate to specified number of decimal places

### 12.6.1 Arithmetic Operators

Table 12.9 Arithmetic Operators Name Description%, `MOD` Modulo operator* Multiplication operator+ Addition operator

-  Minus operator
-  Change the sign of the argument

/ Division operator`DIV` Integer division The usual arithmetic operators are available. The result is determined according to the following rules:

- In the case of -, +, and *, the result is calculated with `BIGINT` (64-bit) precision if both operands are

integers.

- If both operands are integers and any of them are unsigned, the result is an unsigned integer. For

subtraction, if the `NO_UNSIGNED_SUBTRACTION` SQL mode is enabled, the result is signed even if any operand is unsigned.

- If any of the operands of a +, -, /, *, % is a real or string value, the precision of the result is the precision

of the operand with the maximum precision.

Arithmetic Operators

- In division performed with /, the scale of the result when using two exact-value operands is the scale

of the first operand plus the value of the `div_precision_increment` system variable (which is 4 by default). For example, the result of the expression `5.05 / 0.014` has a scale of six decimal places

```
(360.714286).
```

These rules are applied for each operation, such that nested calculations imply the precision of each component. Hence, `(14620 / 9432456) / (24250 / 9432456)`, resolves first to `(0.0014) /``(0.0026)`, with the final result having 8 decimal places (`0.60288653`).

Because of these rules and the way they are applied, care should be taken to ensure that components and subcomponents of a calculation use the appropriate level of precision. See Section 12.11, “Cast Functions and Operators”.

For information about handling of overflow in numeric expression evaluation, see Section 11.1.7, “Out-of-Range and Overflow Handling”.

Arithmetic operators apply to numbers. For other types of values, alternative operations may be available.

For example, to add date values, use `DATE_ADD()`; see Section 12.7, “Date and Time Functions”.

- +

Addition:

```
mysql> SELECT 3+5;
-> 8
```

- -

Subtraction:

```
mysql> SELECT 3-5;
-> -2
```

- -

Unary minus. This operator changes the sign of the operand.

```
mysql> SELECT - 2;
-> -2
```

Note If this operator is used with a `BIGINT`, the return value is also a `BIGINT`. This means that you should avoid using - on integers that may have the value of −263.

- *

Multiplication:

```
mysql> SELECT 3*5;
-> 15
mysql> SELECT 18014398509481984*18014398509481984.0;
-> 324518553658426726783156020576256.0
mysql> SELECT 18014398509481984*18014398509481984;
-> out-of-range error
```

The last expression produces an error because the result of the integer multiplication exceeds the 64-bit range of `BIGINT` calculations. (See Section 11.1, “Numeric Data Types”.)

- /

Mathematical Functions Division:

```
mysql> SELECT 3/5;
-> 0.60
```

Division by zero produces a `NULL` result:

```
mysql> SELECT 102/(1-1);
-> NULL
```

A division is calculated with `BIGINT` arithmetic only if performed in a context where its result is converted to an integer.

```
- DIV
```

Integer division. Discards from the division result any fractional part to the right of the decimal point.

If either operand has a noninteger type, the operands are converted to `DECIMAL` and divided using`DECIMAL` arithmetic before converting the result to `BIGINT`. If the result exceeds `BIGINT` range, an error occurs.

```
mysql> SELECT 5 DIV 2, -5 DIV 2, 5 DIV -2, -5 DIV -2;
-> 2, -2, -2, 2
- N % M, N MOD M
```

Modulo operation. Returns the remainder of N divided by M. For more information, see the description for the `MOD()` function in Section 12.6.2, “Mathematical Functions”.

### 12.6.2 Mathematical Functions

Table 12.10 Mathematical Functions Name Description`ABS()` Return the absolute value`ACOS()` Return the arc cosine`ASIN()` Return the arc sine`ATAN()` Return the arc tangent`ATAN2()`, `ATAN()` Return the arc tangent of the two arguments`CEIL()` Return the smallest integer value not less than the argument`CEILING()` Return the smallest integer value not less than the argument`CONV()` Convert numbers between different number bases`COS()` Return the cosine`COT()` Return the cotangent`CRC32()` Compute a cyclic redundancy check value`DEGREES()` Convert radians to degrees`EXP()` Raise to the power of`FLOOR()` Return the largest integer value not greater than the argument Mathematical Functions Name Description`LN()` Return the natural logarithm of the argument`LOG()` Return the natural logarithm of the first argument`LOG10()` Return the base-10 logarithm of the argument`LOG2()` Return the base-2 logarithm of the argument`MOD()` Return the remainder`PI()` Return the value of pi`POW()` Return the argument raised to the specified power`POWER()` Return the argument raised to the specified power`RADIANS()` Return argument converted to radians`RAND()` Return a random floating-point value`ROUND()` Round the argument`SIGN()` Return the sign of the argument`SIN()` Return the sine of the argument`SQRT()` Return the square root of the argument`TAN()` Return the tangent of the argument`TRUNCATE()` Truncate to specified number of decimal places All mathematical functions return `NULL` in the event of an error.

```
- ABS(X)
```

Returns the absolute value of X, or `NULL` if X is `NULL`.

The result type is derived from the argument type. An implication of this is that`ABS(-9223372036854775808)` produces an error because the result cannot be stored in a signed`BIGINT` value.

```
mysql> SELECT ABS(2);
-> 2
mysql> SELECT ABS(-32);
-> 32
```

This function is safe to use with `BIGINT` values.

```
- ACOS(X)
```

Returns the arc cosine of X, that is, the value whose cosine is X. Returns `NULL` if X is not in the range `-1`to 1.

```
mysql> SELECT ACOS(1);
-> 0
mysql> SELECT ACOS(1.0001);
-> NULL
mysql> SELECT ACOS(0);
-> 1.5707963267949
- ASIN(X)
```

Returns the arc sine of X, that is, the value whose sine is X. Returns `NULL` if X is not in the range `-1` to 1.

```
mysql> SELECT ASIN(0.2);
```

Mathematical Functions

```
-> 0.20135792079033
mysql> SELECT ASIN('foo');
+-------------+
| ASIN('foo') |
+-------------+
|           0 |
+-------------+
1 row in set, 1 warning (0.00 sec)
mysql> SHOW WARNINGS;
+---------+------+-----------------------------------------+
| Level   | Code | Message                                 |
+---------+------+-----------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: 'foo' |
+---------+------+-----------------------------------------+
- ATAN(X)
```

Returns the arc tangent of X, that is, the value whose tangent is X.

```
mysql> SELECT ATAN(2);
-> 1.1071487177941
mysql> SELECT ATAN(-2);
-> -1.1071487177941
- ATAN(Y,X), ATAN2(Y,X)
```

Returns the arc tangent of the two variables X and Y. It is similar to calculating the arc tangent of `Y / X`,except that the signs of both arguments are used to determine the quadrant of the result.

```
mysql> SELECT ATAN(-2,2);
-> -0.78539816339745
mysql> SELECT ATAN2(PI(),0);
-> 1.5707963267949
- CEIL(X)
```

`CEIL()` is a synonym for `CEILING()`.

```
- CEILING(X)
```

Returns the smallest integer value not less than X.

```
mysql> SELECT CEILING(1.23);
-> 2
mysql> SELECT CEILING(-1.23);
-> -1
```

For exact-value numeric arguments, the return value has an exact-value numeric type. For string or floating-point arguments, the return value has a floating-point type.

```
- CONV(N,from_base,to_base)
```

Converts numbers between different number bases. Returns a string representation of the number N, converted from base `from_base` to base `to_base`. Returns `NULL` if any argument is `NULL`. The argument N is interpreted as an integer, but may be specified as an integer or a string. The minimum base is 2 and the maximum base is 36. If `from_base` is a negative number, N is regarded as a signed number. Otherwise, N is treated as unsigned. `CONV()` works with 64-bit precision.

```
mysql> SELECT CONV('a',16,2);
-> '1010'
mysql> SELECT CONV('6E',18,8);
```

Mathematical Functions

```
-> '172'
mysql> SELECT CONV(-17,10,-18);
-> '-H'
mysql> SELECT CONV(10+'10'+'10'+X'0a',10,10);
-> '40'
- COS(X)
```

Returns the cosine of X, where X is given in radians.

```
mysql> SELECT COS(PI());
-> -1
- COT(X)
```

Returns the cotangent of X.

```
mysql> SELECT COT(12);
-> -1.5726734063977
mysql> SELECT COT(0);
-> out-of-range error
- CRC32(expr)
```

Computes a cyclic redundancy check value and returns a 32-bit unsigned value. The result is `NULL` if the argument is `NULL`. The argument is expected to be a string and (if possible) is treated as one if it is not.

```
mysql> SELECT CRC32('MySQL');
-> 3259397556
mysql> SELECT CRC32('mysql');
-> 2501908538
- DEGREES(X)
```

Returns the argument X, converted from radians to degrees.

```
mysql> SELECT DEGREES(PI());
-> 180
mysql> SELECT DEGREES(PI() / 2);
-> 90
- EXP(X)
```

Returns the value of e (the base of natural logarithms) raised to the power of X. The inverse of this function is `LOG()` (using a single argument only) or `LN()`.

```
mysql> SELECT EXP(2);
-> 7.3890560989307
mysql> SELECT EXP(-2);
-> 0.13533528323661
mysql> SELECT EXP(0);
-> 1
- FLOOR(X)
```

Returns the largest integer value not greater than X.

```
mysql> SELECT FLOOR(1.23), FLOOR(-1.23);
-> 1, -2
```

For exact-value numeric arguments, the return value has an exact-value numeric type. For string or floating-point arguments, the return value has a floating-point type.

Mathematical Functions

```
- FORMAT(X,D)
```

Formats the number X to a format like `'#,###,###.##'`, rounded to D decimal places, and returns the result as a string. For details, see Section 12.8, “String Functions and Operators”.

```
- HEX(N_or_S)
```

This function can be used to obtain a hexadecimal representation of a decimal number or a string; the manner in which it does so varies according to the argument's type. See this function's description in Section 12.8, “String Functions and Operators”, for details.

```
- LN(X)
```

Returns the natural logarithm of X; that is, the base-e logarithm of X. If X is less than or equal to 0, then`NULL` is returned.

```
mysql> SELECT LN(2);
-> 0.69314718055995
mysql> SELECT LN(-2);
-> NULL
```

This function is synonymous with `LOG(X)`. The inverse of this function is the `EXP()` function.

```
- LOG(X), LOG(B,X)
```

If called with one parameter, this function returns the natural logarithm of X. If X is less than or equal to 0,then `NULL` is returned.

The inverse of this function (when called with a single argument) is the `EXP()` function.

```
mysql> SELECT LOG(2);
-> 0.69314718055995
mysql> SELECT LOG(-2);
-> NULL
```

If called with two parameters, this function returns the logarithm of X to the base B. If X is less than or equal to 0, or if B is less than or equal to 1, then `NULL` is returned.

```
mysql> SELECT LOG(2,65536);
-> 16
mysql> SELECT LOG(10,100);
-> 2
mysql> SELECT LOG(1,100);
-> NULL
```

`LOG(B,X)` is equivalent to `LOG(X) / LOG(B)`.

```
- LOG2(X)
```

Returns the base-2 logarithm of X.

```
mysql> SELECT LOG2(65536);
-> 16
mysql> SELECT LOG2(-100);
-> NULL
```

`LOG2()` is useful for finding out how many bits a number requires for storage. This function is equivalent to the expression `LOG(X) / LOG(2)`.

Mathematical Functions

```
- LOG10(X)
```

Returns the base-10 logarithm of X.

```
mysql> SELECT LOG10(2);
-> 0.30102999566398
mysql> SELECT LOG10(100);
-> 2
mysql> SELECT LOG10(-100);
-> NULL
```

`LOG10(X)` is equivalent to `LOG(10,X)`.

```
- MOD(N,M), N % M, N MOD M
```

Modulo operation. Returns the remainder of N divided by M.

```
mysql> SELECT MOD(234, 10);
-> 4
mysql> SELECT 253 % 7;
-> 1
mysql> SELECT MOD(29,9);
-> 2
mysql> SELECT 29 MOD 9;
-> 2
```

This function is safe to use with `BIGINT` values.

`MOD()` also works on values that have a fractional part and returns the exact remainder after division:

```
mysql> SELECT MOD(34.5,3);
-> 1.5
```

`MOD(N,0)` returns `NULL`.

```
- PI()
```

Returns the value of π (pi). The default number of decimal places displayed is seven, but MySQL uses the full double-precision value internally.

```
mysql> SELECT PI();
-> 3.141593
mysql> SELECT PI()+0.000000000000000000;
-> 3.141592653589793116
- POW(X,Y)
```

Returns the value of X raised to the power of Y.

```
mysql> SELECT POW(2,2);
-> 4
mysql> SELECT POW(2,-2);
-> 0.25
- POWER(X,Y)
```

This is a synonym for `POW()`.

Mathematical Functions

```
- RADIANS(X)
```

Returns the argument X, converted from degrees to radians.

Noteπ radians equals 180 degrees.

```
mysql> SELECT RADIANS(90);
-> 1.5707963267949
- RAND([N])
```

Returns a random floating-point value v in the range 0 <= v < `1.0`. To obtain a random integer R in the range i <= R < j, use the expression `FLOOR(i + RAND() * (j` − `i))`. For example, to obtain a random integer in the range the range 7 <= R < 12, use the following statement:

```
SELECT FLOOR(7 + (RAND() * 5));
```

If an integer argument N is specified, it is used as the seed value:

- With a constant initializer argument, the seed is initialized once when the statement is prepared, prior

to execution.

- With a nonconstant initializer argument (such as a column name), the seed is initialized with the value

for each invocation of `RAND()`.

One implication of this behavior is that for equal argument values, `RAND(N)` returns the same value each time, and thus produces a repeatable sequence of column values. In the following example, the sequence of values produced by `RAND(3)` is the same both places it occurs.

```
mysql> CREATE TABLE t (i INT);
Query OK, 0 rows affected (0.42 sec)
mysql> INSERT INTO t VALUES(1),(2),(3);
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0
mysql> SELECT i, RAND() FROM t;
+------+------------------+
| i    | RAND()           |
+------+------------------+
|    1 | 0.61914388706828 |
|    2 | 0.93845168309142 |
|    3 | 0.83482678498591 |
+------+------------------+
3 rows in set (0.00 sec)
mysql> SELECT i, RAND(3) FROM t;
+------+------------------+
| i    | RAND(3)          |
+------+------------------+
|    1 | 0.90576975597606 |
|    2 | 0.37307905813035 |
|    3 | 0.14808605345719 |
+------+------------------+
3 rows in set (0.00 sec)
mysql> SELECT i, RAND() FROM t;
+------+------------------+
| i    | RAND()           |
```

Mathematical Functions

```
+------+------------------+
|    1 | 0.35877890638893 |
|    2 | 0.28941420772058 |
|    3 | 0.37073435016976 |
+------+------------------+
3 rows in set (0.00 sec)
mysql> SELECT i, RAND(3) FROM t;
+------+------------------+
| i    | RAND(3)          |
+------+------------------+
|    1 | 0.90576975597606 |
|    2 | 0.37307905813035 |
|    3 | 0.14808605345719 |
+------+------------------+
3 rows in set (0.01 sec)
```

`RAND()` in a `WHERE` clause is evaluated for every row (when selecting from one table) or combination of rows (when selecting from a multiple-table join). Thus, for optimizer purposes, `RAND()` is not a constant value and cannot be used for index optimizations. For more information, see Section 8.2.1.17, “Function Call Optimization”.

Use of a column with `RAND()` values in an `ORDER BY` or `GROUP BY` clause may yield unexpected results because for either clause a `RAND()` expression can be evaluated multiple times for the same row, each time returning a different result. If the goal is to retrieve rows in random order, you can use a statement like this:

```
SELECT * FROM tbl_name ORDER BY RAND();
```

To select a random sample from a set of rows, combine `ORDER BY RAND()` with `LIMIT`:

```
SELECT * FROM table1, table2 WHERE a=b AND c<d ORDER BY RAND() LIMIT 1000;
```

`RAND()` is not meant to be a perfect random generator. It is a fast way to generate random numbers on demand that is portable between platforms for the same MySQL version.

This function is unsafe for statement-based replication. A warning is logged if you use this function when`binlog_format` is set to `STATEMENT`.

```
- ROUND(X), ROUND(X,D)
```

Rounds the argument X to D decimal places. The rounding algorithm depends on the data type of X. D defaults to 0 if not specified. D can be negative to cause D digits left of the decimal point of the value X to become zero. The maximum absolute value for D is 30; any digits in excess of 30 (or -30) are truncated.

```
mysql> SELECT ROUND(-1.23);
-> -1
mysql> SELECT ROUND(-1.58);
-> -2
mysql> SELECT ROUND(1.58);
-> 2
mysql> SELECT ROUND(1.298, 1);
-> 1.3
mysql> SELECT ROUND(1.298, 0);
-> 1
mysql> SELECT ROUND(23.298, -1);
-> 20
mysql> SELECT ROUND(.12345678901234567890123456789012345, 35);
```

Mathematical Functions

```
-> 0.123456789012345678901234567890
```

The return value has the same type as the first argument (assuming that it is integer, double, or decimal). This means that for an integer argument, the result is an integer (no decimal places):

```
mysql> SELECT ROUND(150.000,2), ROUND(150,2);
+------------------+--------------+
| ROUND(150.000,2) | ROUND(150,2) |
+------------------+--------------+
|           150.00 |          150 |
+------------------+--------------+
```

`ROUND()` uses the following rules depending on the type of the first argument:

- For exact-value numbers, `ROUND()` uses the “round half away from zero” or “round toward nearest”

rule: A value with a fractional part of .5 or greater is rounded up to the next integer if positive or down to the next integer if negative. (In other words, it is rounded away from zero.) A value with a fractional part less than .5 is rounded down to the next integer if positive or up to the next integer if negative.

- For approximate-value numbers, the result depends on the C library. On many systems, this means

that `ROUND()` uses the “round to nearest even” rule: A value with a fractional part exactly half way between two integers is rounded to the nearest even integer.

The following example shows how rounding differs for exact and approximate values:

```
mysql> SELECT ROUND(2.5), ROUND(25E-1);
+------------+--------------+
| ROUND(2.5) | ROUND(25E-1) |
+------------+--------------+
| 3          |            2 |
+------------+--------------+
```

For more information, see Section 12.21, “Precision Math”.

```
- SIGN(X)
```

Returns the sign of the argument as `-1`, 0, or 1, depending on whether X is negative, zero, or positive.

```
mysql> SELECT SIGN(-32);
-> -1
mysql> SELECT SIGN(0);
-> 0
mysql> SELECT SIGN(234);
-> 1
- SIN(X)
```

Returns the sine of X, where X is given in radians.

```
mysql> SELECT SIN(PI());
-> 1.2246063538224e-16
mysql> SELECT ROUND(SIN(PI()));
-> 0
- SQRT(X)
```

Returns the square root of a nonnegative number X.

```
mysql> SELECT SQRT(4);
-> 2
mysql> SELECT SQRT(20);
-> 4.4721359549996
```

Date and Time Functions

```
mysql> SELECT SQRT(-16);
-> NULL
- TAN(X)
```

Returns the tangent of X, where X is given in radians.

```
mysql> SELECT TAN(PI());
-> -1.2246063538224e-16
mysql> SELECT TAN(PI()+1);
-> 1.5574077246549
- TRUNCATE(X,D)
```

Returns the number X, truncated to D decimal places. If D is 0, the result has no decimal point or fractional part. D can be negative to cause D digits left of the decimal point of the value X to become zero.

```
mysql> SELECT TRUNCATE(1.223,1);
-> 1.2
mysql> SELECT TRUNCATE(1.999,1);
-> 1.9
mysql> SELECT TRUNCATE(1.999,0);
-> 1
mysql> SELECT TRUNCATE(-1.999,1);
-> -1.9
mysql> SELECT TRUNCATE(122,-2);
-> 100
mysql> SELECT TRUNCATE(10.28*100,0);
-> 1028
```

All numbers are rounded toward zero.

## 12.7 Date and Time Functions

This section describes the functions that can be used to manipulate temporal values. See Section 11.2,“Date and Time Data Types”, for a description of the range of values each date and time type has and the valid formats in which values may be specified.

Table 12.11 Date and Time Functions Name Description`ADDDATE()` Add time values (intervals) to a date value`ADDTIME()` Add time`CONVERT_TZ()` Convert from one time zone to another`CURDATE()` Return the current date`CURRENT_DATE()`, `CURRENT_DATE` Synonyms for CURDATE()`CURRENT_TIME()`, `CURRENT_TIME` Synonyms for CURTIME()`CURRENT_TIMESTAMP()`, `CURRENT_TIMESTAMP` Synonyms for NOW()`CURTIME()` Return the current time`DATE()` Extract the date part of a date or datetime expression`DATE_ADD()` Add time values (intervals) to a date value`DATE_FORMAT()` Format date as specified`DATE_SUB()` Subtract a time value (interval) from a date Date and Time Functions Name Description`DATEDIFF()` Subtract two dates`DAY()` Synonym for DAYOFMONTH()`DAYNAME()` Return the name of the weekday`DAYOFMONTH()` Return the day of the month (0-31)`DAYOFWEEK()` Return the weekday index of the argument`DAYOFYEAR()` Return the day of the year (1-366)`EXTRACT()` Extract part of a date`FROM_DAYS()` Convert a day number to a date`FROM_UNIXTIME()` Format Unix timestamp as a date`GET_FORMAT()` Return a date format string`HOUR()` Extract the hour`LAST_DAY` Return the last day of the month for the argument`LOCALTIME()`, `LOCALTIME` Synonym for NOW()`LOCALTIMESTAMP`, `LOCALTIMESTAMP()` Synonym for NOW()`MAKEDATE()` Create a date from the year and day of year`MAKETIME()` Create time from hour, minute, second`MICROSECOND()` Return the microseconds from argument`MINUTE()` Return the minute from the argument`MONTH()` Return the month from the date passed`MONTHNAME()` Return the name of the month`NOW()` Return the current date and time`PERIOD_ADD()` Add a period to a year-month`PERIOD_DIFF()` Return the number of months between periods`QUARTER()` Return the quarter from a date argument`SEC_TO_TIME()` Converts seconds to 'hh:mm:ss' format`SECOND()` Return the second (0-59)`STR_TO_DATE()` Convert a string to a date`SUBDATE()` Synonym for DATE_SUB() when invoked with three arguments`SUBTIME()` Subtract times`SYSDATE()` Return the time at which the function executes`TIME()` Extract the time portion of the expression passed`TIME_FORMAT()` Format as time`TIME_TO_SEC()` Return the argument converted to seconds`TIMEDIFF()` Subtract time`TIMESTAMP()` With a single argument, this function returns the date or datetime expression; with two arguments,the sum of the arguments`TIMESTAMPADD()` Add an interval to a datetime expression Date and Time Functions Name Description`TIMESTAMPDIFF()` Return the difference of two datetime expressions,using the units specified`TO_DAYS()` Return the date argument converted to days`TO_SECONDS()` Return the date or datetime argument converted to seconds since Year 0`UNIX_TIMESTAMP()` Return a Unix timestamp`UTC_DATE()` Return the current UTC date`UTC_TIME()` Return the current UTC time`UTC_TIMESTAMP()` Return the current UTC date and time`WEEK()` Return the week number`WEEKDAY()` Return the weekday index`WEEKOFYEAR()` Return the calendar week of the date (1-53)`YEAR()` Return the year`YEARWEEK()` Return the year and week Here is an example that uses date functions. The following query selects all rows with a `date_col` value from within the last 30 days:

```
mysql> SELECT something FROM tbl_name
-> WHERE DATE_SUB(CURDATE(),INTERVAL 30 DAY) <= date_col;
```

The query also selects rows with dates that lie in the future.

Functions that expect date values usually accept datetime values and ignore the time part. Functions that expect time values usually accept datetime values and ignore the date part.

Functions that return the current date or time each are evaluated only once per query at the start of query execution. This means that multiple references to a function such as `NOW()` within a single query always produce the same result. (For our purposes, a single query also includes a call to a stored program(stored routine, trigger, or event) and all subprograms called by that program.) This principle also applies to `CURDATE()`, `CURTIME()`, `UTC_DATE()`, `UTC_TIME()`, `UTC_TIMESTAMP()`, and to any of their synonyms.

```
The CURRENT_TIMESTAMP(), CURRENT_TIME(), CURRENT_DATE(), and FROM_UNIXTIME() functions
```

return values in the current session time zone, which is available as the session value of the `time_zone`system variable. In addition, `UNIX_TIMESTAMP()` assumes that its argument is a datetime value in the session time zone. See Section 5.1.13, “MySQL Server Time Zone Support”.

Some date functions can be used with “zero” dates or incomplete dates such as `'2001-11-00'`, whereas others cannot. Functions that extract parts of dates typically work with incomplete dates and thus can return 0 when you might otherwise expect a nonzero value. For example:

```
mysql> SELECT DAYOFMONTH('2001-11-00'), MONTH('2005-00-00');
-> 0, 0
```

Other functions expect complete dates and return `NULL` for incomplete dates. These include functions that perform date arithmetic or that map parts of dates to names. For example:

```
mysql> SELECT DATE_ADD('2006-05-00',INTERVAL 1 DAY);
-> NULL
mysql> SELECT DAYNAME('2006-05-00');
-> NULL
```

Date and Time Functions Several functions are strict when passed a `DATE()` function value as their argument and reject incomplete dates with a day part of zero: `CONVERT_TZ()`, `DATE_ADD()`, `DATE_SUB()`, `DAYOFYEAR()`,

```
TIMESTAMPDIFF(), TO_DAYS(), TO_SECONDS(), WEEK(), WEEKDAY(), WEEKOFYEAR(),
YEARWEEK().
```

Fractional seconds for `TIME`, `DATETIME`, and `TIMESTAMP` values are supported, with up to microsecond precision. Functions that take temporal arguments accept values with fractional seconds. Return values from temporal functions include fractional seconds as appropriate.

```
- ADDDATE(date,INTERVAL expr unit), ADDDATE(expr,days)
```

When invoked with the `INTERVAL` form of the second argument, `ADDDATE()` is a synonym for`DATE_ADD()`. The related function `SUBDATE()` is a synonym for `DATE_SUB()`. For information on the`INTERVAL` `unit` argument, see Temporal Intervals.

```
mysql> SELECT DATE_ADD('2008-01-02', INTERVAL 31 DAY);
-> '2008-02-02'
mysql> SELECT ADDDATE('2008-01-02', INTERVAL 31 DAY);
-> '2008-02-02'
```

When invoked with the `days` form of the second argument, MySQL treats it as an integer number of days to be added to `expr`.

```
mysql> SELECT ADDDATE('2008-01-02', 31);
-> '2008-02-02'
- ADDTIME(expr1,expr2)
```

`ADDTIME()` adds `expr2` to `expr1` and returns the result. `expr1` is a time or datetime expression, and`expr2` is a time expression.

```
mysql> SELECT ADDTIME('2007-12-31 23:59:59.999999', '1 1:1:1.000002');
-> '2008-01-02 01:01:01.000001'
mysql> SELECT ADDTIME('01:00:00.999999', '02:00:00.999998');
-> '03:00:01.999997'
- CONVERT_TZ(dt,from_tz,to_tz)
```

`CONVERT_TZ()` converts a datetime value `dt` from the time zone given by `from_tz` to the time zone given by `to_tz` and returns the resulting value. Time zones are specified as described in Section 5.1.13,“MySQL Server Time Zone Support”. This function returns `NULL` if the arguments are invalid.

If the value falls out of the supported range of the `TIMESTAMP` type when converted from `from_tz` to UTC, no conversion occurs. The `TIMESTAMP` range is described in Section 11.2.1, “Date and Time Data Type Syntax”.

```
mysql> SELECT CONVERT_TZ('2004-01-01 12:00:00','GMT','MET');
-> '2004-01-01 13:00:00'
mysql> SELECT CONVERT_TZ('2004-01-01 12:00:00','+00:00','+10:00');
-> '2004-01-01 22:00:00'
```

Note To use named time zones such as `'MET'` or `'Europe/Amsterdam'`, the time zone tables must be properly set up. For instructions, see Section 5.1.13,“MySQL Server Time Zone Support”.

```
- CURDATE()
```

Date and Time Functions Returns the current date as a value in `'YYYY-MM-DD'` or `YYYYMMDD` format, depending on whether the function is used in string or numeric context.

```
mysql> SELECT CURDATE();
-> '2008-06-13'
mysql> SELECT CURDATE() + 0;
-> 20080613
- CURRENT_DATE, CURRENT_DATE()
```

`CURRENT_DATE` and `CURRENT_DATE()` are synonyms for `CURDATE()`.

```
- CURRENT_TIME, CURRENT_TIME([fsp])
```

`CURRENT_TIME` and `CURRENT_TIME()` are synonyms for `CURTIME()`.

```
- CURRENT_TIMESTAMP, CURRENT_TIMESTAMP([fsp])
```

`CURRENT_TIMESTAMP` and `CURRENT_TIMESTAMP()` are synonyms for `NOW()`.

```
- CURTIME([fsp])
```

Returns the current time as a value in `'hh:mm:ss'` or `hhmmss` format, depending on whether the function is used in string or numeric context. The value is expressed in the session time zone.

If the `fsp` argument is given to specify a fractional seconds precision from 0 to 6, the return value includes a fractional seconds part of that many digits.

```
mysql> SELECT CURTIME();
-> '23:50:26'
mysql> SELECT CURTIME() + 0;
-> 235026.000000
- DATE(expr)
```

Extracts the date part of the date or datetime expression `expr`.

```
mysql> SELECT DATE('2003-12-31 01:02:03');
-> '2003-12-31'
- DATEDIFF(expr1,expr2)
```

`DATEDIFF()` returns `expr1` − `expr2` expressed as a value in days from one date to the other. `expr1`and `expr2` are date or date-and-time expressions. Only the date parts of the values are used in the calculation.

```
mysql> SELECT DATEDIFF('2007-12-31 23:59:59','2007-12-30');
-> 1
mysql> SELECT DATEDIFF('2010-11-30 23:59:59','2010-12-31');
-> -31
- DATE_ADD(date,INTERVAL expr unit), DATE_SUB(date,INTERVAL expr unit)
```

These functions perform date arithmetic. The `date` argument specifies the starting date or datetime value. `expr` is an expression specifying the interval value to be added or subtracted from the starting Date and Time Functions date. `expr` is evaluated as a string; it may start with a - for negative intervals. `unit` is a keyword indicating the units in which the expression should be interpreted.

For more information about temporal interval syntax, including a full list of `unit` specifiers, the expected form of the `expr` argument for each `unit` value, and rules for operand interpretation in temporal arithmetic, see Temporal Intervals.

The return value depends on the arguments:

- `DATE` if the `date` argument is a `DATE` value and your calculations involve only `YEAR`, `MONTH`, and `DAY`

parts (that is, no time parts).

- `DATETIME` if the first argument is a `DATETIME` (or `TIMESTAMP`) value, or if the first argument is a

`DATE` and the `unit` value uses `HOURS`, `MINUTES`, or `SECONDS`.

- String otherwise.

To ensure that the result is `DATETIME`, you can use `CAST()` to convert the first argument to `DATETIME`.

```
mysql> SELECT DATE_ADD('2018-05-01',INTERVAL 1 DAY);
-> '2018-05-02'
mysql> SELECT DATE_SUB('2018-05-01',INTERVAL 1 YEAR);
-> '2017-05-01'
mysql> SELECT DATE_ADD('2020-12-31 23:59:59',
->                 INTERVAL 1 SECOND);
-> '2021-01-01 00:00:00'
mysql> SELECT DATE_ADD('2018-12-31 23:59:59',
->                 INTERVAL 1 DAY);
-> '2019-01-01 23:59:59'
mysql> SELECT DATE_ADD('2100-12-31 23:59:59',
->                 INTERVAL '1:1' MINUTE_SECOND);
-> '2101-01-01 00:01:00'
mysql> SELECT DATE_SUB('2025-01-01 00:00:00',
->                 INTERVAL '1 1:1:1' DAY_SECOND);
-> '2024-12-30 22:58:59'
mysql> SELECT DATE_ADD('1900-01-01 00:00:00',
->                 INTERVAL '-1 10' DAY_HOUR);
-> '1899-12-30 14:00:00'
mysql> SELECT DATE_SUB('1998-01-02', INTERVAL 31 DAY);
-> '1997-12-02'
mysql> SELECT DATE_ADD('1992-12-31 23:59:59.000002',
->            INTERVAL '1.999999' SECOND_MICROSECOND);
-> '1993-01-01 00:00:01.000001'
```

When adding a `MONTH` interval to a `DATE` or `DATETIME` value, and the resulting date includes a day that does not exist in the given month, the day is adjusted to the last day of the month, as shown here:

```
mysql> SELECT DATE_ADD('2024-03-30', INTERVAL 1 MONTH) AS d1,
>        DATE_ADD('2024-03-31', INTERVAL 1 MONTH) AS d2;
+------------+------------+
| d1         | d2         |
+------------+------------+
| 2024-04-30 | 2024-04-30 |
+------------+------------+
1 row in set (0.00 sec)
```

Date and Time Functions

```
- DATE_FORMAT(date,format)
```

Formats the `date` value according to the `format` string.

The specifiers shown in the following table may be used in the `format` string. The % character is required before format specifier characters. The specifiers apply to other functions as well:

```
STR_TO_DATE(), TIME_FORMAT(), UNIX_TIMESTAMP().
```

Specifier Description`%a` Abbreviated weekday name (`Sun`..`Sat`)`%b` Abbreviated month name (`Jan`..`Dec`)`%c` Month, numeric (0..12)`%D` Day of the month with English suffix (`0th`, `1st`,`2nd`, `3rd`, …)`%d` Day of the month, numeric (00..31)`%e` Day of the month, numeric (0..31)`%f` Microseconds (000000..999999)`%H` Hour (00..23)`%h` Hour (01..12)`%I` Hour (01..12)`%i` Minutes, numeric (00..59)`%j` Day of year (001..366)`%k` Hour (0..23)`%l` Hour (1..12)`%M` Month name (`January`..`December`)`%m` Month, numeric (00..12)`%p` `AM` or `PM``%r` Time, 12-hour (`hh:mm:ss` followed by `AM` or `PM`)`%S` Seconds (00..59)`%s` Seconds (00..59)`%T` Time, 24-hour (`hh:mm:ss`)`%U` Week (00..53), where Sunday is the first day of the week; `WEEK()` mode 0`%u` Week (00..53), where Monday is the first day of the week; `WEEK()` mode 1`%V` Week (01..53), where Sunday is the first day of the week; `WEEK()` mode 2; used with `%X``%v` Week (01..53), where Monday is the first day of the week; `WEEK()` mode 3; used with `%x``%W` Weekday name (`Sunday`..`Saturday`)`%w` Day of the week (0=Sunday..6=Saturday)`%X` Year for the week where Sunday is the first day of the week, numeric, four digits; used with `%V`Date and Time Functions Specifier Description`%x` Year for the week, where Monday is the first day of the week, numeric, four digits; used with `%v``%Y` Year, numeric, four digits`%y` Year, numeric (two digits)`%%` A literal % character`%x` x, for any “x” not listed above Ranges for the month and day specifiers begin with zero due to the fact that MySQL permits the storing of incomplete dates such as `'2014-00-00'`.

The language used for day and month names and abbreviations is controlled by the value of the`lc_time_names` system variable (Section 10.16, “MySQL Server Locale Support”).

For the `%U`, `%u`, `%V`, and `%v` specifiers, see the description of the `WEEK()` function for information about the mode values. The mode affects how week numbering occurs.

`DATE_FORMAT()` returns a string with a character set and collation given by`character_set_connection` and `collation_connection` so that it can return month and weekday names containing non-ASCII characters.

```
mysql> SELECT DATE_FORMAT('2009-10-04 22:23:00', '%W %M %Y');
-> 'Sunday October 2009'
mysql> SELECT DATE_FORMAT('2007-10-04 22:23:00', '%H:%i:%s');
-> '22:23:00'
mysql> SELECT DATE_FORMAT('1900-10-04 22:23:00',
->                 '%D %y %a %d %m %b %j');
-> '4th 00 Thu 04 10 Oct 277'
mysql> SELECT DATE_FORMAT('1997-10-04 22:23:00',
->                 '%H %k %I %r %T %S %w');
-> '22 22 10 10:23:00 PM 22:23:00 00 6'
mysql> SELECT DATE_FORMAT('1999-01-01', '%X %V');
-> '1998 52'
mysql> SELECT DATE_FORMAT('2006-06-00', '%d');
-> '00'
- DATE_SUB(date,INTERVAL expr unit)
```

See the description for `DATE_ADD()`.

```
- DAY(date)
```

`DAY()` is a synonym for `DAYOFMONTH()`.

```
- DAYNAME(date)
```

Returns the name of the weekday for `date`. The language used for the name is controlled by the value of the `lc_time_names` system variable (Section 10.16, “MySQL Server Locale Support”).

```
mysql> SELECT DAYNAME('2007-02-03');
-> 'Saturday'
- DAYOFMONTH(date)
```

Returns the day of the month for `date`, in the range 1 to 31, or 0 for dates such as `'0000-00-00'` or`'2008-00-00'` that have a zero day part.

```
mysql> SELECT DAYOFMONTH('2007-02-03');
```

Date and Time Functions

```
-> 3
- DAYOFWEEK(date)
```

Returns the weekday index for `date` (1 = Sunday, 2 = Monday, …, 7 = Saturday). These index values correspond to the ODBC standard.

```
mysql> SELECT DAYOFWEEK('2007-02-03');
-> 7
- DAYOFYEAR(date)
```

Returns the day of the year for `date`, in the range 1 to 366.

```
mysql> SELECT DAYOFYEAR('2007-02-03');
-> 34
- EXTRACT(unit FROM date)
```

The `EXTRACT()` function uses the same kinds of `unit` specifiers as `DATE_ADD()` or `DATE_SUB()`,but extracts parts from the date rather than performing date arithmetic. For information on the `unit`argument, see Temporal Intervals.

```
mysql> SELECT EXTRACT(YEAR FROM '2019-07-02');
-> 2019
mysql> SELECT EXTRACT(YEAR_MONTH FROM '2019-07-02 01:02:03');
-> 201907
mysql> SELECT EXTRACT(DAY_MINUTE FROM '2019-07-02 01:02:03');
-> 20102
mysql> SELECT EXTRACT(MICROSECOND
->                FROM '2003-01-02 10:30:00.000123');
-> 123
- FROM_DAYS(N)
```

Given a day number N, returns a `DATE` value.

```
mysql> SELECT FROM_DAYS(730669);
-> '2000-07-03'
```

Use `FROM_DAYS()` with caution on old dates. It is not intended for use with values that precede the advent of the Gregorian calendar (1582). See Section 12.9, “What Calendar Is Used By MySQL?”.

```
- FROM_UNIXTIME(unix_timestamp[,format])
```

Returns a representation of `unix_timestamp` as a datetime or character string value. The value returned is expressed using the session time zone. (Clients can set the session time zone as described in Section 5.1.13, “MySQL Server Time Zone Support”.) `unix_timestamp` is an internal timestamp value representing seconds since `'1970-01-01 00:00:00'` UTC, such as produced by the`UNIX_TIMESTAMP()` function.

If `format` is omitted, this function returns a `DATETIME` value.

If `unix_timestamp` is an integer, the fractional seconds precision of the `DATETIME` is zero. When`unix_timestamp` is a decimal value, the fractional seconds precision of the `DATETIME` is the same as Date and Time Functions the precision of the decimal value, up to a maximum of 6. When `unix_timestamp` is a floating point number, the fractional seconds precision of the datetime is 6.

`format` is used to format the result in the same way as the format string used for the `DATE_FORMAT()`function. If `format` is supplied, the value returned is a `VARCHAR`.

```
mysql> SELECT FROM_UNIXTIME(1447430881);
-> '2015-11-13 10:08:01'
mysql> SELECT FROM_UNIXTIME(1447430881) + 0;
-> 20151113100801
mysql> SELECT FROM_UNIXTIME(1447430881,
->                      '%Y %D %M %h:%i:%s %x');
-> '2015 13th November 10:08:01 2015'
```

Note If you use `UNIX_TIMESTAMP()` and `FROM_UNIXTIME()` to convert between values in a non-UTC time zone and Unix timestamp values, the conversion is lossy because the mapping is not one-to-one in both directions. For details, see the description of the `UNIX_TIMESTAMP()` function.

```
- GET_FORMAT({DATE|TIME|DATETIME}, {'EUR'|'USA'|'JIS'|'ISO'|'INTERNAL'})
```

Returns a format string. This function is useful in combination with the `DATE_FORMAT()` and the`STR_TO_DATE()` functions.

The possible values for the first and second arguments result in several possible format strings (for the specifiers used, see the table in the `DATE_FORMAT()` function description). ISO format refers to ISO 9075, not ISO 8601.

> Function Call Result

```
GET_FORMAT(DATE,'USA')  '%m.%d.%Y'
GET_FORMAT(DATE,'JIS')  '%Y-%m-%d'
GET_FORMAT(DATE,'ISO')  '%Y-%m-%d'
GET_FORMAT(DATE,'EUR')  '%d.%m.%Y'
GET_FORMAT(DATE,'INTERNAL')  '%Y%m%d'
GET_FORMAT(DATETIME,'USA')  '%Y-%m-%d %H.%i.%s'
GET_FORMAT(DATETIME,'JIS')  '%Y-%m-%d %H:%i:%s'
GET_FORMAT(DATETIME,'ISO')  '%Y-%m-%d %H:%i:%s'
GET_FORMAT(DATETIME,'EUR')  '%Y-%m-%d %H.%i.%s'
GET_FORMAT(DATETIME,'INTERNAL')  '%Y%m%d%H%i%s'
GET_FORMAT(TIME,'USA')  '%h:%i:%s %p'
GET_FORMAT(TIME,'JIS')  '%H:%i:%s'
GET_FORMAT(TIME,'ISO')  '%H:%i:%s'
GET_FORMAT(TIME,'EUR')  '%H.%i.%s'
GET_FORMAT(TIME,'INTERNAL')  '%H%i%s'
```

`TIMESTAMP` can also be used as the first argument to `GET_FORMAT()`, in which case the function returns the same values as for `DATETIME`.

```
mysql> SELECT DATE_FORMAT('2003-10-03',GET_FORMAT(DATE,'EUR'));
```

Date and Time Functions

```
-> '03.10.2003'
mysql> SELECT STR_TO_DATE('10.31.2003',GET_FORMAT(DATE,'USA'));
-> '2003-10-31'
- HOUR(time)
```

Returns the hour for `time`. The range of the return value is 0 to 23 for time-of-day values. However, the range of `TIME` values actually is much larger, so `HOUR` can return values greater than 23.

```
mysql> SELECT HOUR('10:05:03');
-> 10
mysql> SELECT HOUR('272:59:59');
-> 272
- LAST_DAY(date)
```

Takes a date or datetime value and returns the corresponding value for the last day of the month.

Returns `NULL` if the argument is invalid.

```
mysql> SELECT LAST_DAY('2003-02-05');
-> '2003-02-28'
mysql> SELECT LAST_DAY('2004-02-05');
-> '2004-02-29'
mysql> SELECT LAST_DAY('2004-01-01 01:01:01');
-> '2004-01-31'
mysql> SELECT LAST_DAY('2003-03-32');
-> NULL
- LOCALTIME, LOCALTIME([fsp])
```

`LOCALTIME` and `LOCALTIME()` are synonyms for `NOW()`.

```
- LOCALTIMESTAMP, LOCALTIMESTAMP([fsp])
```

`LOCALTIMESTAMP` and `LOCALTIMESTAMP()` are synonyms for `NOW()`.

```
- MAKEDATE(year,dayofyear)
```

Returns a date, given year and day-of-year values. `dayofyear` must be greater than 0 or the result is

```
NULL.
mysql> SELECT MAKEDATE(2011,31), MAKEDATE(2011,32);
-> '2011-01-31', '2011-02-01'
mysql> SELECT MAKEDATE(2011,365), MAKEDATE(2014,365);
-> '2011-12-31', '2014-12-31'
mysql> SELECT MAKEDATE(2011,0);
-> NULL
- MAKETIME(hour,minute,second)
```

Returns a time value calculated from the `hour`, `minute`, and `second` arguments.

The `second` argument can have a fractional part.

```
mysql> SELECT MAKETIME(12,15,30);
-> '12:15:30'
- MICROSECOND(expr)
```

Returns the microseconds from the time or datetime expression `expr` as a number in the range from 0 to 999999.

```
mysql> SELECT MICROSECOND('12:00:00.123456');
```

Date and Time Functions

```
-> 123456
mysql> SELECT MICROSECOND('2019-12-31 23:59:59.000010');
-> 10
- MINUTE(time)
```

Returns the minute for `time`, in the range 0 to 59.

```
mysql> SELECT MINUTE('2008-02-03 10:05:03');
-> 5
- MONTH(date)
```

Returns the month for `date`, in the range 1 to 12 for January to December, or 0 for dates such as`'0000-00-00'` or `'2008-00-00'` that have a zero month part.

```
mysql> SELECT MONTH('2008-02-03');
-> 2
- MONTHNAME(date)
```

Returns the full name of the month for `date`. The language used for the name is controlled by the value of the `lc_time_names` system variable (Section 10.16, “MySQL Server Locale Support”).

```
mysql> SELECT MONTHNAME('2008-02-03');
-> 'February'
- NOW([fsp])
```

Returns the current date and time as a value in `'YYYY-MM-DD hh:mm:ss'` or `YYYYMMDDhhmmss`format, depending on whether the function is used in string or numeric context. The value is expressed in the session time zone.

If the `fsp` argument is given to specify a fractional seconds precision from 0 to 6, the return value includes a fractional seconds part of that many digits.

```
mysql> SELECT NOW();
-> '2007-12-15 23:50:26'
mysql> SELECT NOW() + 0;
-> 20071215235026.000000
```

`NOW()` returns a constant time that indicates the time at which the statement began to execute. (Within a stored function or trigger, `NOW()` returns the time at which the function or triggering statement began to execute.) This differs from the behavior for `SYSDATE()`, which returns the exact time at which it executes.

```
mysql> SELECT NOW(), SLEEP(2), NOW();
+---------------------+----------+---------------------+
| NOW()               | SLEEP(2) | NOW()               |
+---------------------+----------+---------------------+
| 2006-04-12 13:47:36 |        0 | 2006-04-12 13:47:36 |
+---------------------+----------+---------------------+
mysql> SELECT SYSDATE(), SLEEP(2), SYSDATE();
+---------------------+----------+---------------------+
| SYSDATE()           | SLEEP(2) | SYSDATE()           |
+---------------------+----------+---------------------+
| 2006-04-12 13:47:44 |        0 | 2006-04-12 13:47:46 |
+---------------------+----------+---------------------+
```

In addition, the `SET TIMESTAMP` statement affects the value returned by `NOW()` but not by `SYSDATE()`.

This means that timestamp settings in the binary log have no effect on invocations of `SYSDATE()`.

Date and Time Functions Setting the timestamp to a nonzero value causes each subsequent invocation of `NOW()` to return that value. Setting the timestamp to zero cancels this effect so that `NOW()` once again returns the current date and time.

See the description for `SYSDATE()` for additional information about the differences between the two functions.

```
- PERIOD_ADD(P,N)
```

Adds N months to period P (in the format `YYMM` or `YYYYMM`). Returns a value in the format `YYYYMM`.

Note The period argument P is not a date value.

```
mysql> SELECT PERIOD_ADD(200801,2);
-> 200803
- PERIOD_DIFF(P1,P2)
```

Returns the number of months between periods `P1` and `P2`. `P1` and `P2` should be in the format `YYMM` or`YYYYMM`. Note that the period arguments `P1` and `P2` are not date values.

```
mysql> SELECT PERIOD_DIFF(200802,200703);
-> 11
- QUARTER(date)
```

Returns the quarter of the year for `date`, in the range 1 to 4.

```
mysql> SELECT QUARTER('2008-04-01');
-> 2
- SECOND(time)
```

Returns the second for `time`, in the range 0 to 59.

```
mysql> SELECT SECOND('10:05:03');
-> 3
- SEC_TO_TIME(seconds)
```

Returns the `seconds` argument, converted to hours, minutes, and seconds, as a `TIME` value. The range of the result is constrained to that of the `TIME` data type. A warning occurs if the argument corresponds to a value outside that range.

```
mysql> SELECT SEC_TO_TIME(2378);
-> '00:39:38'
mysql> SELECT SEC_TO_TIME(2378) + 0;
-> 3938
- STR_TO_DATE(str,format)
```

This is the inverse of the `DATE_FORMAT()` function. It takes a string `str` and a format string `format`.

`STR_TO_DATE()` returns a `DATETIME` value if the format string contains both date and time parts, or a `DATE` or `TIME` value if the string contains only date or time parts. If the date, time, or datetime value extracted from `str` is illegal, `STR_TO_DATE()` returns `NULL` and produces a warning.

The server scans `str` attempting to match `format` to it. The format string can contain literal characters and format specifiers beginning with %. Literal characters in `format` must match literally in `str`. Format Date and Time Functions specifiers in `format` must match a date or time part in `str`. For the specifiers that can be used in`format`, see the `DATE_FORMAT()` function description.

```
mysql> SELECT STR_TO_DATE('01,5,2013','%d,%m,%Y');
-> '2013-05-01'
mysql> SELECT STR_TO_DATE('May 1, 2013','%M %d,%Y');
-> '2013-05-01'
```

Scanning starts at the beginning of `str` and fails if `format` is found not to match. Extra characters at the end of `str` are ignored.

```
mysql> SELECT STR_TO_DATE('a09:30:17','a%h:%i:%s');
-> '09:30:17'
mysql> SELECT STR_TO_DATE('a09:30:17','%h:%i:%s');
-> NULL
mysql> SELECT STR_TO_DATE('09:30:17a','%h:%i:%s');
-> '09:30:17'
```

Unspecified date or time parts have a value of 0, so incompletely specified values in `str` produce a result with some or all parts set to 0:

```
mysql> SELECT STR_TO_DATE('abc','abc');
-> '0000-00-00'
mysql> SELECT STR_TO_DATE('9','%m');
-> '0000-09-00'
mysql> SELECT STR_TO_DATE('9','%s');
-> '00:00:09'
```

Range checking on the parts of date values is as described in Section 11.2.2, “The DATE, DATETIME,and TIMESTAMP Types”. This means, for example, that “zero” dates or dates with part values of 0 are permitted unless the SQL mode is set to disallow such values.

```
mysql> SELECT STR_TO_DATE('00/00/0000', '%m/%d/%Y');
-> '0000-00-00'
mysql> SELECT STR_TO_DATE('04/31/2004', '%m/%d/%Y');
-> '2004-04-31'
```

If the `NO_ZERO_DATE` SQL mode is enabled, zero dates are disallowed. In that case, `STR_TO_DATE()`returns `NULL` and generates a warning:

```
mysql> SET sql_mode = '';
mysql> SELECT STR_TO_DATE('00/00/0000', '%m/%d/%Y');
+---------------------------------------+
| STR_TO_DATE('00/00/0000', '%m/%d/%Y') |
+---------------------------------------+
| 0000-00-00                            |
+---------------------------------------+
mysql> SET sql_mode = 'NO_ZERO_DATE';
mysql> SELECT STR_TO_DATE('00/00/0000', '%m/%d/%Y');
+---------------------------------------+
| STR_TO_DATE('00/00/0000', '%m/%d/%Y') |
+---------------------------------------+
| NULL                                  |
+---------------------------------------+
mysql> SHOW WARNINGS\G
*************************** 1. row ***************************
Level: Warning
Code: 1411
```

Date and Time Functions

```
Message: Incorrect datetime value: '00/00/0000' for function str_to_date
```

Note You cannot use format `"%X%V"` to convert a year-week string to a date because the combination of a year and week does not uniquely identify a year and month if the week crosses a month boundary. To convert a year-week to a date, you should also specify the weekday:

```
mysql> SELECT STR_TO_DATE('200442 Monday', '%X%V %W');
-> '2004-10-18'
- SUBDATE(date,INTERVAL expr unit), SUBDATE(expr,days)
```

When invoked with the `INTERVAL` form of the second argument, `SUBDATE()` is a synonym for`DATE_SUB()`. For information on the `INTERVAL` `unit` argument, see the discussion for `DATE_ADD()`.

```
mysql> SELECT DATE_SUB('2008-01-02', INTERVAL 31 DAY);
-> '2007-12-02'
mysql> SELECT SUBDATE('2008-01-02', INTERVAL 31 DAY);
-> '2007-12-02'
```

The second form enables the use of an integer value for `days`. In such cases, it is interpreted as the number of days to be subtracted from the date or datetime expression `expr`.

```
mysql> SELECT SUBDATE('2008-01-02 12:00:00', 31);
-> '2007-12-02 12:00:00'
- SUBTIME(expr1,expr2)
```

`SUBTIME()` returns `expr1` − `expr2` expressed as a value in the same format as `expr1`. `expr1` is a time or datetime expression, and `expr2` is a time expression.

```
mysql> SELECT SUBTIME('2007-12-31 23:59:59.999999','1 1:1:1.000002');
-> '2007-12-30 22:58:58.999997'
mysql> SELECT SUBTIME('01:00:00.999999', '02:00:00.999998');
-> '-00:59:59.999999'
- SYSDATE([fsp])
```

Returns the current date and time as a value in `'YYYY-MM-DD hh:mm:ss'` or `YYYYMMDDhhmmss`format, depending on whether the function is used in string or numeric context.

If the `fsp` argument is given to specify a fractional seconds precision from 0 to 6, the return value includes a fractional seconds part of that many digits.

`SYSDATE()` returns the time at which it executes. This differs from the behavior for `NOW()`, which returns a constant time that indicates the time at which the statement began to execute. (Within a stored function or trigger, `NOW()` returns the time at which the function or triggering statement began to execute.)

```
mysql> SELECT NOW(), SLEEP(2), NOW();
+---------------------+----------+---------------------+
| NOW()               | SLEEP(2) | NOW()               |
+---------------------+----------+---------------------+
| 2006-04-12 13:47:36 |        0 | 2006-04-12 13:47:36 |
+---------------------+----------+---------------------+
mysql> SELECT SYSDATE(), SLEEP(2), SYSDATE();
+---------------------+----------+---------------------+
| SYSDATE()           | SLEEP(2) | SYSDATE()           |
+---------------------+----------+---------------------+
| 2006-04-12 13:47:44 |        0 | 2006-04-12 13:47:46 |
```

Date and Time Functions

```
+---------------------+----------+---------------------+
```

In addition, the `SET TIMESTAMP` statement affects the value returned by `NOW()` but not by `SYSDATE()`.

This means that timestamp settings in the binary log have no effect on invocations of `SYSDATE()`.

Because `SYSDATE()` can return different values even within the same statement, and is not affected by`SET TIMESTAMP`, it is nondeterministic and therefore unsafe for replication if statement-based binary logging is used. If that is a problem, you can use row-based logging.

Alternatively, you can use the `--sysdate-is-now` option to cause `SYSDATE()` to be an alias for`NOW()`. This works if the option is used on both the source and the replica.

The nondeterministic nature of `SYSDATE()` also means that indexes cannot be used for evaluating expressions that refer to it.

```
- TIME(expr)
```

Extracts the time part of the time or datetime expression `expr` and returns it as a string.

This function is unsafe for statement-based replication. A warning is logged if you use this function when`binlog_format` is set to `STATEMENT`.

```
mysql> SELECT TIME('2003-12-31 01:02:03');
-> '01:02:03'
mysql> SELECT TIME('2003-12-31 01:02:03.000123');
-> '01:02:03.000123'
- TIMEDIFF(expr1,expr2)
```

`TIMEDIFF()` returns `expr1` − `expr2` expressed as a time value. `expr1` and `expr2` are strings which are converted to `TIME` or `DATETIME` expressions; these must be of the same type following conversion.

The result returned by `TIMEDIFF()` is limited to the range allowed for `TIME` values. Alternatively, you can use either of the functions `TIMESTAMPDIFF()` and `UNIX_TIMESTAMP()`, both of which return integers.

```
mysql> SELECT TIMEDIFF('2000:01:01 00:00:00',
->                 '2000:01:01 00:00:00.000001');
-> '-00:00:00.000001'
mysql> SELECT TIMEDIFF('2008-12-31 23:59:59.000001',
->                 '2008-12-30 01:01:01.000002');
-> '46:58:57.999999'
- TIMESTAMP(expr), TIMESTAMP(expr1,expr2)
```

With a single argument, this function returns the date or datetime expression `expr` as a datetime value.

With two arguments, it adds the time expression `expr2` to the date or datetime expression `expr1` and returns the result as a datetime value.

```
mysql> SELECT TIMESTAMP('2003-12-31');
-> '2003-12-31 00:00:00'
mysql> SELECT TIMESTAMP('2003-12-31 12:00:00','12:00:00');
-> '2004-01-01 00:00:00'
```

Date and Time Functions

```
- TIMESTAMPADD(unit,interval,datetime_expr)
```

Adds the integer expression `interval` to the date or datetime expression `datetime_expr`. The unit for `interval` is given by the `unit` argument, which should be one of the following values:`MICROSECOND` (microseconds), `SECOND`, `MINUTE`, `HOUR`, `DAY`, `WEEK`, `MONTH`, `QUARTER`, or `YEAR`.

The `unit` value may be specified using one of keywords as shown, or with a prefix of `SQL_TSI_`. For example, `DAY` and `SQL_TSI_DAY` both are legal.

```
mysql> SELECT TIMESTAMPADD(MINUTE,1,'2003-01-02');
-> '2003-01-02 00:01:00'
mysql> SELECT TIMESTAMPADD(WEEK,1,'2003-01-02');
-> '2003-01-09'
```

When adding a `MONTH` interval to a `DATE` or `DATETIME` value, and the resulting date includes a day that does not exist in the given month, the day is adjusted to the last day of the month, as shown here:

```
mysql> SELECT TIMESTAMPADD(MONTH, 1, DATE '2024-03-30') AS t1,
>        TIMESTAMPADD(MONTH, 1, DATE '2024-03-31') AS t2;
+------------+------------+
| t1         | t2         |
+------------+------------+
| 2024-04-30 | 2024-04-30 |
+------------+------------+
1 row in set (0.00 sec)
- TIMESTAMPDIFF(unit,datetime_expr1,datetime_expr2)
Returns datetime_expr2 − datetime_expr1, where datetime_expr1 and datetime_expr2
```

are date or datetime expressions. One expression may be a date and the other a datetime; a date value is treated as a datetime having the time part `'00:00:00'` where necessary. The unit for the result (an integer) is given by the `unit` argument. The legal values for `unit` are the same as those listed in the description of the `TIMESTAMPADD()` function.

```
mysql> SELECT TIMESTAMPDIFF(MONTH,'2003-02-01','2003-05-01');
-> 3
mysql> SELECT TIMESTAMPDIFF(YEAR,'2002-05-01','2001-01-01');
-> -1
mysql> SELECT TIMESTAMPDIFF(MINUTE,'2003-02-01','2003-05-01 12:05:55');
-> 128885
```

Note The order of the date or datetime arguments for this function is the opposite of that used with the `TIMESTAMP()` function when invoked with 2 arguments.

```
- TIME_FORMAT(time,format)
```

This is used like the `DATE_FORMAT()` function, but the `format` string may contain format specifiers only for hours, minutes, seconds, and microseconds. Other specifiers produce a `NULL` value or 0.

If the `time` value contains an hour part that is greater than 23, the `%H` and `%k` hour format specifiers produce a value larger than the usual range of `0..23`. The other hour format specifiers produce the hour value modulo 12.

```
mysql> SELECT TIME_FORMAT('100:00:00', '%H %k %h %I %l');
-> '100 100 04 04 4'
- TIME_TO_SEC(time)
```

Returns the `time` argument, converted to seconds.

Date and Time Functions

```
mysql> SELECT TIME_TO_SEC('22:23:00');
-> 80580
mysql> SELECT TIME_TO_SEC('00:39:38');
-> 2378
- TO_DAYS(date)
```

Given a date `date`, returns a day number (the number of days since year 0).

```
mysql> SELECT TO_DAYS(950501);
-> 728779
mysql> SELECT TO_DAYS('2007-10-07');
-> 733321
```

`TO_DAYS()` is not intended for use with values that precede the advent of the Gregorian calendar(1582), because it does not take into account the days that were lost when the calendar was changed.

For dates before 1582 (and possibly a later year in other locales), results from this function are not reliable. See Section 12.9, “What Calendar Is Used By MySQL?”, for details.

Remember that MySQL converts two-digit year values in dates to four-digit form using the rules in Section 11.2, “Date and Time Data Types”. For example, `'2008-10-07'` and `'08-10-07'` are seen as identical dates:

```
mysql> SELECT TO_DAYS('2008-10-07'), TO_DAYS('08-10-07');
-> 733687, 733687
```

In MySQL, the zero date is defined as `'0000-00-00'`, even though this date is itself considered invalid.

This means that, for `'0000-00-00'` and `'0000-01-01'`, `TO_DAYS()` returns the values shown here:

```
mysql> SELECT TO_DAYS('0000-00-00');
+-----------------------+
| to_days('0000-00-00') |
+-----------------------+
|                  NULL |
+-----------------------+
1 row in set, 1 warning (0.00 sec)
mysql> SHOW WARNINGS;
+---------+------+----------------------------------------+
| Level   | Code | Message                                |
+---------+------+----------------------------------------+
| Warning | 1292 | Incorrect datetime value: '0000-00-00' |
+---------+------+----------------------------------------+
1 row in set (0.00 sec)
mysql> SELECT TO_DAYS('0000-01-01');
+-----------------------+
| to_days('0000-01-01') |
+-----------------------+
|                     1 |
+-----------------------+
1 row in set (0.00 sec)
```

This is true whether or not the `ALLOW_INVALID_DATES` SQL server mode is enabled.

```
- TO_SECONDS(expr)
```

Given a date or datetime `expr`, returns the number of seconds since the year 0. If `expr` is not a valid date or datetime value, returns `NULL`.

```
mysql> SELECT TO_SECONDS(950501);
```

Date and Time Functions

```
-> 62966505600
mysql> SELECT TO_SECONDS('2009-11-29');
-> 63426672000
mysql> SELECT TO_SECONDS('2009-11-29 13:43:32');
-> 63426721412
mysql> SELECT TO_SECONDS( NOW() );
-> 63426721458
```

Like `TO_DAYS()`, `TO_SECONDS()` is not intended for use with values that precede the advent of the Gregorian calendar (1582), because it does not take into account the days that were lost when the calendar was changed. For dates before 1582 (and possibly a later year in other locales), results from this function are not reliable. See Section 12.9, “What Calendar Is Used By MySQL?”, for details.

Like `TO_DAYS()`, `TO_SECONDS()`, converts two-digit year values in dates to four-digit form using the rules in Section 11.2, “Date and Time Data Types”.

In MySQL, the zero date is defined as `'0000-00-00'`, even though this date is itself considered invalid.

This means that, for `'0000-00-00'` and `'0000-01-01'`, `TO_SECONDS()` returns the values shown here:

```
mysql> SELECT TO_SECONDS('0000-00-00');
+--------------------------+
| TO_SECONDS('0000-00-00') |
+--------------------------+
|                     NULL |
+--------------------------+
1 row in set, 1 warning (0.00 sec)
mysql> SHOW WARNINGS;
+---------+------+----------------------------------------+
| Level   | Code | Message                                |
+---------+------+----------------------------------------+
| Warning | 1292 | Incorrect datetime value: '0000-00-00' |
+---------+------+----------------------------------------+
1 row in set (0.00 sec)
mysql> SELECT TO_SECONDS('0000-01-01');
+--------------------------+
| TO_SECONDS('0000-01-01') |
+--------------------------+
|                    86400 |
+--------------------------+
1 row in set (0.00 sec)
```

This is true whether or not the `ALLOW_INVALID_DATES` SQL server mode is enabled.

```
- UNIX_TIMESTAMP([date])
```

If `UNIX_TIMESTAMP()` is called with no `date` argument, it returns a Unix timestamp representing seconds since `'1970-01-01 00:00:00'` UTC.

If `UNIX_TIMESTAMP()` is called with a `date` argument, it returns the value of the argument as seconds since `'1970-01-01 00:00:00'` UTC. The server interprets `date` as a value in the session time zone and converts it to an internal Unix timestamp value in UTC. (Clients can set the session time zone as described in Section 5.1.13, “MySQL Server Time Zone Support”.) The `date` argument may be a `DATE`, `DATETIME`, or `TIMESTAMP` string, or a number in `YYMMDD`, `YYMMDDhhmmss`, `YYYYMMDD`, or Date and Time Functions`YYYYMMDDhhmmss` format. If the argument includes a time part, it may optionally include a fractional seconds part.

The return value is an integer if no argument is given or the argument does not include a fractional seconds part, or `DECIMAL` if an argument is given that includes a fractional seconds part.

When the `date` argument is a `TIMESTAMP` column, `UNIX_TIMESTAMP()` returns the internal timestamp value directly, with no implicit “string-to-Unix-timestamp” conversion.

The valid range of argument values is the same as for the `TIMESTAMP` data type: `'1970-01-01``00:00:01.000000'` UTC to `'2038-01-19 03:14:07.999999'` UTC. If you pass an out-of-range date to `UNIX_TIMESTAMP()`, it returns 0.

```
mysql> SELECT UNIX_TIMESTAMP();
-> 1447431666
mysql> SELECT UNIX_TIMESTAMP('2015-11-13 10:20:19');
-> 1447431619
mysql> SELECT UNIX_TIMESTAMP('2015-11-13 10:20:19.012');
-> 1447431619.012
```

If you use `UNIX_TIMESTAMP()` and `FROM_UNIXTIME()` to convert between values in a non-UTC time zone and Unix timestamp values, the conversion is lossy because the mapping is not one-to-one in both directions. For example, due to conventions for local time zone changes such as Daylight Saving Time(DST), it is possible for `UNIX_TIMESTAMP()` to map two values that are distinct in a non-UTC time zone to the same Unix timestamp value. `FROM_UNIXTIME()` maps that value back to only one of the original values. Here is an example, using values that are distinct in the `MET` time zone:

```
mysql> SET time_zone = 'MET';
mysql> SELECT UNIX_TIMESTAMP('2005-03-27 03:00:00');
+---------------------------------------+
| UNIX_TIMESTAMP('2005-03-27 03:00:00') |
+---------------------------------------+
|                            1111885200 |
+---------------------------------------+
mysql> SELECT UNIX_TIMESTAMP('2005-03-27 02:00:00');
+---------------------------------------+
| UNIX_TIMESTAMP('2005-03-27 02:00:00') |
+---------------------------------------+
|                            1111885200 |
+---------------------------------------+
mysql> SELECT FROM_UNIXTIME(1111885200);
+---------------------------+
| FROM_UNIXTIME(1111885200) |
+---------------------------+
| 2005-03-27 03:00:00       |
+---------------------------+
```

Note To use named time zones such as `'MET'` or `'Europe/Amsterdam'`, the time zone tables must be properly set up. For instructions, see Section 5.1.13,“MySQL Server Time Zone Support”.

If you want to subtract `UNIX_TIMESTAMP()` columns, you might want to cast them to signed integers.

See Section 12.11, “Cast Functions and Operators”.

Date and Time Functions

```
- UTC_DATE, UTC_DATE()
```

Returns the current UTC date as a value in `'YYYY-MM-DD'` or `YYYYMMDD` format, depending on whether the function is used in string or numeric context.

```
mysql> SELECT UTC_DATE(), UTC_DATE() + 0;
-> '2003-08-14', 20030814
- UTC_TIME, UTC_TIME([fsp])
```

Returns the current UTC time as a value in `'hh:mm:ss'` or `hhmmss` format, depending on whether the function is used in string or numeric context.

If the `fsp` argument is given to specify a fractional seconds precision from 0 to 6, the return value includes a fractional seconds part of that many digits.

```
mysql> SELECT UTC_TIME(), UTC_TIME() + 0;
-> '18:07:53', 180753.000000
- UTC_TIMESTAMP, UTC_TIMESTAMP([fsp])
```

Returns the current UTC date and time as a value in `'YYYY-MM-DD hh:mm:ss'` or `YYYYMMDDhhmmss`format, depending on whether the function is used in string or numeric context.

If the `fsp` argument is given to specify a fractional seconds precision from 0 to 6, the return value includes a fractional seconds part of that many digits.

```
mysql> SELECT UTC_TIMESTAMP(), UTC_TIMESTAMP() + 0;
-> '2003-08-14 18:08:04', 20030814180804.000000
- WEEK(date[,mode])
```

This function returns the week number for `date`. The two-argument form of `WEEK()` enables you to specify whether the week starts on Sunday or Monday and whether the return value should be in the range from 0 to 53 or from 1 to 53. If the `mode` argument is omitted, the value of the`default_week_format` system variable is used. See Section 5.1.7, “Server System Variables”.

The following table describes how the `mode` argument works.

Mode First day of week Range Week 1 is the first week …0 Sunday 0-53 with a Sunday in this year 1 Monday 0-53 with 4 or more days this year 2 Sunday 1-53 with a Sunday in this year 3 Monday 1-53 with 4 or more days this year 4 Sunday 0-53 with 4 or more days this year 5 Monday 0-53 with a Monday in this year 6 Sunday 1-53 with 4 or more days this year Date and Time Functions Mode First day of week Range Week 1 is the first week …7 Monday 1-53 with a Monday in this year For `mode` values with a meaning of “with 4 or more days this year,” weeks are numbered according to ISO 8601:1988:

- If the week containing January 1 has 4 or more days in the new year, it is week 1.
- Otherwise, it is the last week of the previous year, and the next week is week 1.

```
mysql> SELECT WEEK('2008-02-20');
-> 7
mysql> SELECT WEEK('2008-02-20',0);
-> 7
mysql> SELECT WEEK('2008-02-20',1);
-> 8
mysql> SELECT WEEK('2008-12-31',1);
-> 53
```

If a date falls in the last week of the previous year, MySQL returns 0 if you do not use 2, 3, 6, or 7 as the optional `mode` argument:

```
mysql> SELECT YEAR('2000-01-01'), WEEK('2000-01-01',0);
-> 2000, 0
```

One might argue that `WEEK()` should return 52 because the given date actually occurs in the 52nd week of 1999. `WEEK()` returns 0 instead so that the return value is “the week number in the given year.” This makes use of the `WEEK()` function reliable when combined with other functions that extract a date part from a date.

If you prefer a result evaluated with respect to the year that contains the first day of the week for the given date, use 0, 2, 5, or 7 as the optional `mode` argument.

```
mysql> SELECT WEEK('2000-01-01',2);
-> 52
```

Alternatively, use the `YEARWEEK()` function:

```
mysql> SELECT YEARWEEK('2000-01-01');
-> 199952
mysql> SELECT MID(YEARWEEK('2000-01-01'),5,2);
-> '52'
- WEEKDAY(date)
```

Returns the weekday index for `date` (0 = Monday, 1 = Tuesday, … 6 = Sunday).

```
mysql> SELECT WEEKDAY('2008-02-03 22:23:00');
-> 6
mysql> SELECT WEEKDAY('2007-11-06');
-> 1
- WEEKOFYEAR(date)
```

Returns the calendar week of the date as a number in the range from 1 to 53. `WEEKOFYEAR()` is a compatibility function that is equivalent to `WEEK(date,3)`.

```
mysql> SELECT WEEKOFYEAR('2008-02-20');
```

String Functions and Operators

```
-> 8
- YEAR(date)
```

Returns the year for `date`, in the range 1000 to 9999, or 0 for the “zero” date.

```
mysql> SELECT YEAR('1987-01-01');
-> 1987
- YEARWEEK(date), YEARWEEK(date,mode)
```

Returns year and week for a date. The year in the result may be different from the year in the date argument for the first and the last week of the year.

The `mode` argument works exactly like the `mode` argument to `WEEK()`. For the single-argument syntax,a `mode` value of 0 is used. Unlike `WEEK()`, the value of `default_week_format` does not influence

```
YEARWEEK().
mysql> SELECT YEARWEEK('1987-01-01');
-> 198652
```

The week number is different from what the `WEEK()` function would return (0) for optional arguments 0 or 1, as `WEEK()` then returns the week in the context of the given year.

## 12.8 String Functions and Operators

Table 12.12 String Functions and Operators Name Description`ASCII()` Return numeric value of left-most character`BIN()` Return a string containing binary representation of a number`BIT_LENGTH()` Return length of argument in bits`CHAR()` Return the character for each integer passed`CHAR_LENGTH()` Return number of characters in argument`CHARACTER_LENGTH()` Synonym for CHAR_LENGTH()`CONCAT()` Return concatenated string`CONCAT_WS()` Return concatenate with separator`ELT()` Return string at index number`EXPORT_SET()` Return a string such that for every bit set in the value bits, you get an on string and for every unset bit, you get an off string`FIELD()` Index (position) of first argument in subsequent arguments`FIND_IN_SET()` Index (position) of first argument within second argument`FORMAT()` Return a number formatted to specified number of decimal places`FROM_BASE64()` Decode base64 encoded string and return result`HEX()` Hexadecimal representation of decimal or string value String Functions and Operators Name Description`INSERT()` Insert substring at specified position up to specified number of characters`INSTR()` Return the index of the first occurrence of substring`LCASE()` Synonym for LOWER()`LEFT()` Return the leftmost number of characters as specified`LENGTH()` Return the length of a string in bytes`LIKE` Simple pattern matching`LOAD_FILE()` Load the named file`LOCATE()` Return the position of the first occurrence of substring`LOWER()` Return the argument in lowercase`LPAD()` Return the string argument, left-padded with the specified string`LTRIM()` Remove leading spaces`MAKE_SET()` Return a set of comma-separated strings that have the corresponding bit in bits set`MATCH()` Perform full-text search`MID()` Return a substring starting from the specified position`NOT LIKE` Negation of simple pattern matching`NOT REGEXP` Negation of REGEXP`OCT()` Return a string containing octal representation of a number`OCTET_LENGTH()` Synonym for LENGTH()`ORD()` Return character code for leftmost character of the argument`POSITION()` Synonym for LOCATE()`QUOTE()` Escape the argument for use in an SQL statement`REGEXP` Whether string matches regular expression`REPEAT()` Repeat a string the specified number of times`REPLACE()` Replace occurrences of a specified string`REVERSE()` Reverse the characters in a string`RIGHT()` Return the specified rightmost number of characters`RLIKE` Whether string matches regular expression`RPAD()` Append string the specified number of times`RTRIM()` Remove trailing spaces`SOUNDEX()` Return a soundex string`SOUNDS LIKE` Compare sounds`SPACE()` Return a string of the specified number of spaces String Functions and Operators Name Description`STRCMP()` Compare two strings`SUBSTR()` Return the substring as specified`SUBSTRING()` Return the substring as specified`SUBSTRING_INDEX()` Return a substring from a string before the specified number of occurrences of the delimiter`TO_BASE64()` Return the argument converted to a base-64 string`TRIM()` Remove leading and trailing spaces`UCASE()` Synonym for UPPER()`UNHEX()` Return a string containing hex representation of a number`UPPER()` Convert to uppercase`WEIGHT_STRING()` Return the weight string for a string String-valued functions return `NULL` if the length of the result would be greater than the value of the`max_allowed_packet` system variable. See Section 5.1.1, “Configuring the Server”.

For functions that operate on string positions, the first position is numbered 1.

For functions that take length arguments, noninteger arguments are rounded to the nearest integer.

```
- ASCII(str)
```

Returns the numeric value of the leftmost character of the string `str`. Returns 0 if `str` is the empty string. Returns `NULL` if `str` is `NULL`. `ASCII()` works for 8-bit characters.

```
mysql> SELECT ASCII('2');
-> 50
mysql> SELECT ASCII(2);
-> 50
mysql> SELECT ASCII('dx');
-> 100
```

See also the `ORD()` function.

```
- BIN(N)
```

Returns a string representation of the binary value of N, where N is a longlong (`BIGINT`) number. This is equivalent to `CONV(N,10,2)`. Returns `NULL` if N is `NULL`.

```
mysql> SELECT BIN(12);
-> '1100'
- BIT_LENGTH(str)
```

Returns the length of the string `str` in bits.

```
mysql> SELECT BIT_LENGTH('text');
-> 32
- CHAR(N,... [USING charset_name])
```

`CHAR()` interprets each argument N as an integer and returns a string consisting of the characters given by the code values of those integers. `NULL` values are skipped.

String Functions and Operators

```
mysql> SELECT CHAR(77,121,83,81,'76');
-> 'MySQL'
mysql> SELECT CHAR(77,77.3,'77.3');
-> 'MMM'
```

`CHAR()` arguments larger than 255 are converted into multiple result bytes. For example, `CHAR(256)` is equivalent to `CHAR(1,0)`, and `CHAR(256*256)` is equivalent to `CHAR(1,0,0)`:

```
mysql> SELECT HEX(CHAR(1,0)), HEX(CHAR(256));
+----------------+----------------+
| HEX(CHAR(1,0)) | HEX(CHAR(256)) |
+----------------+----------------+
| 0100           | 0100           |
+----------------+----------------+
mysql> SELECT HEX(CHAR(1,0,0)), HEX(CHAR(256*256));
+------------------+--------------------+
| HEX(CHAR(1,0,0)) | HEX(CHAR(256*256)) |
+------------------+--------------------+
| 010000           | 010000             |
+------------------+--------------------+
```

By default, `CHAR()` returns a binary string. To produce a string in a given character set, use the optional`USING` clause:

```
mysql> SELECT CHARSET(CHAR(X'65')), CHARSET(CHAR(X'65' USING utf8));
+----------------------+---------------------------------+
| CHARSET(CHAR(X'65')) | CHARSET(CHAR(X'65' USING utf8)) |
+----------------------+---------------------------------+
| binary               | utf8                            |
+----------------------+---------------------------------+
```

If `USING` is given and the result string is illegal for the given character set, a warning is issued. Also, if strict SQL mode is enabled, the result from `CHAR()` becomes `NULL`.

If `CHAR()` is invoked from within the `mysql` client, binary strings display using hexadecimal notation,depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

```
- CHAR_LENGTH(str)
```

Returns the length of the string `str`, measured in code points. A multibyte character counts as a single code point. This means that, for a string containing two 3-byte characters, `LENGTH()` returns 6, whereas`CHAR_LENGTH()` returns 2, as shown here:

```
mysql> SET @dolphin:='海豚';
Query OK, 0 rows affected (0.01 sec)
mysql> SELECT LENGTH(@dolphin), CHAR_LENGTH(@dolphin);
+------------------+-----------------------+
| LENGTH(@dolphin) | CHAR_LENGTH(@dolphin) |
+------------------+-----------------------+
|                6 |                     2 |
+------------------+-----------------------+
1 row in set (0.00 sec)
- CHARACTER_LENGTH(str)
```

`CHARACTER_LENGTH()` is a synonym for `CHAR_LENGTH()`.

String Functions and Operators

```
- CONCAT(str1,str2,...)
```

Returns the string that results from concatenating the arguments. May have one or more arguments. If all arguments are nonbinary strings, the result is a nonbinary string. If the arguments include any binary strings, the result is a binary string. A numeric argument is converted to its equivalent nonbinary string form.

`CONCAT()` returns `NULL` if any argument is `NULL`.

```
mysql> SELECT CONCAT('My', 'S', 'QL');
-> 'MySQL'
mysql> SELECT CONCAT('My', NULL, 'QL');
-> NULL
mysql> SELECT CONCAT(14.3);
-> '14.3'
```

For quoted strings, concatenation can be performed by placing the strings next to each other:

```
mysql> SELECT 'My' 'S' 'QL';
-> 'MySQL'
```

If `CONCAT()` is invoked from within the `mysql` client, binary string results display using hexadecimal notation, depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

```
- CONCAT_WS(separator,str1,str2,...)
```

`CONCAT_WS()` stands for Concatenate With Separator and is a special form of `CONCAT()`. The first argument is the separator for the rest of the arguments. The separator is added between the strings to be concatenated. The separator can be a string, as can the rest of the arguments. If the separator is`NULL`, the result is `NULL`.

```
mysql> SELECT CONCAT_WS(',','First name','Second name','Last Name');
-> 'First name,Second name,Last Name'
mysql> SELECT CONCAT_WS(',','First name',NULL,'Last Name');
-> 'First name,Last Name'
```

`CONCAT_WS()` does not skip empty strings. However, it does skip any `NULL` values after the separator argument.

```
- ELT(N,str1,str2,str3,...)
```

`ELT()` returns the Nth element of the list of strings: `str1` if N = 1, `str2` if N = 2, and so on. Returns`NULL` if N is less than 1 or greater than the number of arguments. `ELT()` is the complement of `FIELD()`.

```
mysql> SELECT ELT(1, 'Aa', 'Bb', 'Cc', 'Dd');
-> 'Aa'
mysql> SELECT ELT(4, 'Aa', 'Bb', 'Cc', 'Dd');
-> 'Dd'
- EXPORT_SET(bits,on,off[,separator[,number_of_bits]])
```

Returns a string such that for every bit set in the value `bits`, you get an `on` string and for every bit not set in the value, you get an `off` string. Bits in `bits` are examined from right to left (from low-order to high-order bits). Strings are added to the result from left to right, separated by the `separator` string(the default being the comma character ,). The number of bits examined is given by `number_of_bits`,which has a default of 64 if not specified. `number_of_bits` is silently clipped to 64 if larger than 64. It is treated as an unsigned integer, so a value of −1 is effectively the same as 64.

```
mysql> SELECT EXPORT_SET(5,'Y','N',',',4);
```

String Functions and Operators

```
-> 'Y,N,Y,N'
mysql> SELECT EXPORT_SET(6,'1','0',',',10);
-> '0,1,1,0,0,0,0,0,0,0'
- FIELD(str,str1,str2,str3,...)
```

Returns the index (position) of `str` in the `str1`, `str2`, `str3`, `...` list. Returns 0 if `str` is not found.

If all arguments to `FIELD()` are strings, all arguments are compared as strings. If all arguments are numbers, they are compared as numbers. Otherwise, the arguments are compared as double.

If `str` is `NULL`, the return value is 0 because `NULL` fails equality comparison with any value. `FIELD()` is the complement of `ELT()`.

```
mysql> SELECT FIELD('Bb', 'Aa', 'Bb', 'Cc', 'Dd', 'Ff');
-> 2
mysql> SELECT FIELD('Gg', 'Aa', 'Bb', 'Cc', 'Dd', 'Ff');
-> 0
- FIND_IN_SET(str,strlist)
```

Returns a value in the range of 1 to N if the string `str` is in the string list `strlist` consisting of N substrings. A string list is a string composed of substrings separated by , characters. If the first argument is a constant string and the second is a column of type `SET`, the `FIND_IN_SET()` function is optimized to use bit arithmetic. Returns 0 if `str` is not in `strlist` or if `strlist` is the empty string.

Returns `NULL` if either argument is `NULL`. This function does not work properly if the first argument contains a comma (,) character.

```
mysql> SELECT FIND_IN_SET('b','a,b,c,d');
-> 2
- FORMAT(X,D[,locale])
```

Formats the number X to a format like `'#,###,###.##'`, rounded to D decimal places, and returns the result as a string. If D is 0, the result has no decimal point or fractional part.

The optional third parameter enables a locale to be specified to be used for the result number's decimal point, thousands separator, and grouping between separators. Permissible locale values are the same as the legal values for the `lc_time_names` system variable (see Section 10.16, “MySQL Server Locale Support”). If no locale is specified, the default is `'en_US'`.

```
mysql> SELECT FORMAT(12332.123456, 4);
-> '12,332.1235'
mysql> SELECT FORMAT(12332.1,4);
-> '12,332.1000'
mysql> SELECT FORMAT(12332.2,0);
-> '12,332'
mysql> SELECT FORMAT(12332.2,2,'de_DE');
-> '12.332,20'
- FROM_BASE64(str)
```

Takes a string encoded with the base-64 encoded rules used by `TO_BASE64()` and returns the decoded result as a binary string. The result is `NULL` if the argument is `NULL` or not a valid base-64 string. See the description of `TO_BASE64()` for details about the encoding and decoding rules.

```
mysql> SELECT TO_BASE64('abc'), FROM_BASE64(TO_BASE64('abc'));
```

String Functions and Operators

```
-> 'JWJj', 'abc'
```

If `FROM_BASE64()` is invoked from within the `mysql` client, binary strings display using hexadecimal notation, depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

```
- HEX(str), HEX(N)
```

For a string argument `str`, `HEX()` returns a hexadecimal string representation of `str` where each byte of each character in `str` is converted to two hexadecimal digits. (Multibyte characters therefore become more than two digits.) The inverse of this operation is performed by the `UNHEX()` function.

For a numeric argument N, `HEX()` returns a hexadecimal string representation of the value of N treated as a longlong (`BIGINT`) number. This is equivalent to `CONV(N,10,16)`. The inverse of this operation is performed by `CONV(HEX(N),16,10)`.

```
mysql> SELECT X'616263', HEX('abc'), UNHEX(HEX('abc'));
-> 'abc', 616263, 'abc'
mysql> SELECT HEX(255), CONV(HEX(255),16,10);
-> 'FF', 255
- INSERT(str,pos,len,newstr)
```

Returns the string `str`, with the substring beginning at position `pos` and `len` characters long replaced by the string `newstr`. Returns the original string if `pos` is not within the length of the string. Replaces the rest of the string from position `pos` if `len` is not within the length of the rest of the string. Returns `NULL` if any argument is `NULL`.

```
mysql> SELECT INSERT('Quadratic', 3, 4, 'What');
-> 'QuWhattic'
mysql> SELECT INSERT('Quadratic', -1, 4, 'What');
-> 'Quadratic'
mysql> SELECT INSERT('Quadratic', 3, 100, 'What');
-> 'QuWhat'
```

This function is multibyte safe.

```
- INSTR(str,substr)
```

Returns the position of the first occurrence of substring `substr` in string `str`. This is the same as the two-argument form of `LOCATE()`, except that the order of the arguments is reversed.

```
mysql> SELECT INSTR('foobarbar', 'bar');
-> 4
mysql> SELECT INSTR('xbar', 'foobar');
-> 0
```

This function is multibyte safe, and is case-sensitive only if at least one argument is a binary string.

```
- LCASE(str)
```

`LCASE()` is a synonym for `LOWER()`.

```
- LEFT(str,len)
```

Returns the leftmost `len` characters from the string `str`, or `NULL` if any argument is `NULL`.

```
mysql> SELECT LEFT('foobarbar', 5);
-> 'fooba'
```

This function is multibyte safe.

String Functions and Operators

```
- LENGTH(str)
```

Returns the length of the string `str`, measured in bytes. A multibyte character counts as multiple bytes. This means that for a string containing five 2-byte characters, `LENGTH()` returns 10, whereas`CHAR_LENGTH()` returns 5.

```
mysql> SELECT LENGTH('text');
-> 4
```

Note The `Length()` OpenGIS spatial function is named `GLength()` in MySQL.

```
- LOAD_FILE(file_name)
```

Reads the file and returns the file contents as a string. To use this function, the file must be located on the server host, you must specify the full path name to the file, and you must have the `FILE`privilege. The file must be readable by all and its size less than `max_allowed_packet` bytes. If the`secure_file_priv` system variable is set to a nonempty directory name, the file to be loaded must be located in that directory.

If the file does not exist or cannot be read because one of the preceding conditions is not satisfied, the function returns `NULL`.

The `character_set_filesystem` system variable controls interpretation of file names that are given as literal strings.

```
mysql> UPDATE t
SET blob_col=LOAD_FILE('/tmp/picture')
WHERE id=1;
- LOCATE(substr,str), LOCATE(substr,str,pos)
```

The first syntax returns the position of the first occurrence of substring `substr` in string `str`. The second syntax returns the position of the first occurrence of substring `substr` in string `str`, starting at position `pos`. Returns 0 if `substr` is not in `str`. Returns `NULL` if `substr` or `str` is `NULL`.

```
mysql> SELECT LOCATE('bar', 'foobarbar');
-> 4
mysql> SELECT LOCATE('xbar', 'foobar');
-> 0
mysql> SELECT LOCATE('bar', 'foobarbar', 5);
-> 7
```

This function is multibyte safe, and is case-sensitive only if at least one argument is a binary string.

```
- LOWER(str)
```

Returns the string `str` with all characters changed to lowercase according to the current character set mapping. The default is `latin1` (cp1252 West European).

```
mysql> SELECT LOWER('QUADRATICALLY');
-> 'quadratically'
```

`LOWER()` (and `UPPER()`) are ineffective when applied to binary strings (`BINARY`, `VARBINARY`, `BLOB`).

To perform lettercase conversion of a binary string, first convert it to a nonbinary string using a character set appropriate for the data stored in the string:

```
mysql> SET @str = BINARY 'New York';
mysql> SELECT LOWER(@str), LOWER(CONVERT(@str USING latin1));
```

String Functions and Operators

```
+-------------+-----------------------------------+
| LOWER(@str) | LOWER(CONVERT(@str USING latin1)) |
+-------------+-----------------------------------+
| New York    | new york                          |
+-------------+-----------------------------------+
```

For collations of Unicode character sets, `LOWER()` and `UPPER()` work according to the Unicode Collation Algorithm (UCA) version in the collation name, if there is one, and UCA 4.0.0 if no version is specified. For example, `utf8_unicode_520_ci` works according to UCA 5.2.0, whereas`utf8_unicode_ci` works according to UCA 4.0.0. See Section 10.10.1, “Unicode Character Sets”.

This function is multibyte safe.

```
- LPAD(str,len,padstr)
```

Returns the string `str`, left-padded with the string `padstr` to a length of `len` characters. If `str` is longer than `len`, the return value is shortened to `len` characters.

```
mysql> SELECT LPAD('hi',4,'??');
-> '??hi'
mysql> SELECT LPAD('hi',1,'??');
-> 'h'
- LTRIM(str)
```

Returns the string `str` with leading space characters removed.

```
mysql> SELECT LTRIM('  barbar');
-> 'barbar'
```

This function is multibyte safe.

```
- MAKE_SET(bits,str1,str2,...)
```

Returns a set value (a string containing substrings separated by , characters) consisting of the strings that have the corresponding bit in `bits` set. `str1` corresponds to bit 0, `str2` to bit 1, and so on. `NULL`values in `str1`, `str2`, `...` are not appended to the result.

```
mysql> SELECT MAKE_SET(1,'a','b','c');
-> 'a'
mysql> SELECT MAKE_SET(1 | 4,'hello','nice','world');
-> 'hello,world'
mysql> SELECT MAKE_SET(1 | 4,'hello','nice',NULL,'world');
-> 'hello'
mysql> SELECT MAKE_SET(0,'a','b','c');
-> ''
- MID(str,pos,len)
```

`MID(str,pos,len)` is a synonym for `SUBSTRING(str,pos,len)`.

```
- OCT(N)
```

Returns a string representation of the octal value of N, where N is a longlong (`BIGINT`) number. This is equivalent to `CONV(N,10,8)`. Returns `NULL` if N is `NULL`.

```
mysql> SELECT OCT(12);
-> '14'
- OCTET_LENGTH(str)
```

`OCTET_LENGTH()` is a synonym for `LENGTH()`.

String Functions and Operators

```
- ORD(str)
```

If the leftmost character of the string `str` is a multibyte character, returns the code for that character,calculated from the numeric values of its constituent bytes using this formula:

```
(1st byte code)
+ (2nd byte code * 256)
+ (3rd byte code * 256^2) ...
```

If the leftmost character is not a multibyte character, `ORD()` returns the same value as the `ASCII()`function.

```
mysql> SELECT ORD('2');
-> 50
- POSITION(substr IN str)
```

`POSITION(substr IN str)` is a synonym for `LOCATE(substr,str)`.

```
- QUOTE(str)
```

Quotes a string to produce a result that can be used as a properly escaped data value in an SQL statement. The string is returned enclosed by single quotation marks and with each instance of backslash (\), single quote ('), ASCII `NUL`, and Control+Z preceded by a backslash. If the argument is`NULL`, the return value is the word “NULL” without enclosing single quotation marks.

```
mysql> SELECT QUOTE('Don\'t!');
-> 'Don\'t!'
mysql> SELECT QUOTE(NULL);
-> NULL
```

For comparison, see the quoting rules for literal strings and within the C API in Section 9.1.1, “String Literals”, and mysql_real_escape_string().

```
- REPEAT(str,count)
```

Returns a string consisting of the string `str` repeated `count` times. If `count` is less than 1, returns an empty string. Returns `NULL` if `str` or `count` are `NULL`.

```
mysql> SELECT REPEAT('MySQL', 3);
-> 'MySQLMySQLMySQL'
- REPLACE(str,from_str,to_str)
```

Returns the string `str` with all occurrences of the string `from_str` replaced by the string `to_str`.

`REPLACE()` performs a case-sensitive match when searching for `from_str`.

```
mysql> SELECT REPLACE('www.mysql.com', 'w', 'Ww');
-> 'WwWwWw.mysql.com'
```

This function is multibyte safe.

```
- REVERSE(str)
```

Returns the string `str` with the order of the characters reversed.

```
mysql> SELECT REVERSE('abc');
-> 'cba'
```

This function is multibyte safe.

String Functions and Operators

```
- RIGHT(str,len)
```

Returns the rightmost `len` characters from the string `str`, or `NULL` if any argument is `NULL`.

```
mysql> SELECT RIGHT('foobarbar', 4);
-> 'rbar'
```

This function is multibyte safe.

```
- RPAD(str,len,padstr)
```

Returns the string `str`, right-padded with the string `padstr` to a length of `len` characters. If `str` is longer than `len`, the return value is shortened to `len` characters.

```
mysql> SELECT RPAD('hi',5,'?');
-> 'hi???'
mysql> SELECT RPAD('hi',1,'?');
-> 'h'
```

This function is multibyte safe.

```
- RTRIM(str)
```

Returns the string `str` with trailing space characters removed.

```
mysql> SELECT RTRIM('barbar   ');
-> 'barbar'
```

This function is multibyte safe.

```
- SOUNDEX(str)
```

Returns a soundex string from `str`. Two strings that sound almost the same should have identical soundex strings. A standard soundex string is four characters long, but the `SOUNDEX()` function returns an arbitrarily long string. You can use `SUBSTRING()` on the result to get a standard soundex string.

All nonalphabetic characters in `str` are ignored. All international alphabetic characters outside the A-Z range are treated as vowels.

Important When using `SOUNDEX()`, you should be aware of the following limitations:

- This function, as currently implemented, is intended to work well with strings that are in the English

language only. Strings in other languages may not produce reliable results.

- This function is not guaranteed to provide consistent results with strings that use multibyte character

sets, including `utf-8`. See Bug #22638 for more information.

```
mysql> SELECT SOUNDEX('Hello');
-> 'H400'
mysql> SELECT SOUNDEX('Quadratically');
-> 'Q36324'
```

Note This function implements the original Soundex algorithm, not the more popular enhanced version (also described by D. Knuth). The difference is that original version discards vowels first and duplicates second, whereas the enhanced version discards duplicates first and vowels second.

String Functions and Operators

```
- expr1 SOUNDS LIKE expr2
```

This is the same as `SOUNDEX(expr1) = SOUNDEX(expr2)`.

```
- SPACE(N)
```

Returns a string consisting of N space characters.

```
mysql> SELECT SPACE(6);
-> '      '
- SUBSTR(str,pos), SUBSTR(str FROM pos), SUBSTR(str,pos,len), SUBSTR(str FROM pos
FOR len)
```

`SUBSTR()` is a synonym for `SUBSTRING()`.

```
- SUBSTRING(str,pos), SUBSTRING(str FROM pos), SUBSTRING(str,pos,len),
SUBSTRING(str FROM pos FOR len)
```

The forms without a `len` argument return a substring from string `str` starting at position `pos`. The forms with a `len` argument return a substring `len` characters long from string `str`, starting at position `pos`.

The forms that use `FROM` are standard SQL syntax. It is also possible to use a negative value for `pos`.

In this case, the beginning of the substring is `pos` characters from the end of the string, rather than the beginning. A negative value may be used for `pos` in any of the forms of this function. A value of 0 for`pos` returns an empty string.

For all forms of `SUBSTRING()`, the position of the first character in the string from which the substring is to be extracted is reckoned as 1.

```
mysql> SELECT SUBSTRING('Quadratically',5);
-> 'ratically'
mysql> SELECT SUBSTRING('foobarbar' FROM 4);
-> 'barbar'
mysql> SELECT SUBSTRING('Quadratically',5,6);
-> 'ratica'
mysql> SELECT SUBSTRING('Sakila', -3);
-> 'ila'
mysql> SELECT SUBSTRING('Sakila', -5, 3);
-> 'aki'
mysql> SELECT SUBSTRING('Sakila' FROM -4 FOR 2);
-> 'ki'
```

This function is multibyte safe.

If `len` is less than 1, the result is the empty string.

```
- SUBSTRING_INDEX(str,delim,count)
```

Returns the substring from string `str` before `count` occurrences of the delimiter `delim`. If `count`is positive, everything to the left of the final delimiter (counting from the left) is returned. If `count`is negative, everything to the right of the final delimiter (counting from the right) is returned.

`SUBSTRING_INDEX()` performs a case-sensitive match when searching for `delim`.

```
mysql> SELECT SUBSTRING_INDEX('www.mysql.com', '.', 2);
-> 'www.mysql'
mysql> SELECT SUBSTRING_INDEX('www.mysql.com', '.', -2);
-> 'mysql.com'
```

This function is multibyte safe.

```
- TO_BASE64(str)
```

String Functions and Operators Converts the string argument to base-64 encoded form and returns the result as a character string with the connection character set and collation. If the argument is not a string, it is converted to a string before conversion takes place. The result is `NULL` if the argument is `NULL`. Base-64 encoded strings can be decoded using the `FROM_BASE64()` function.

```
mysql> SELECT TO_BASE64('abc'), FROM_BASE64(TO_BASE64('abc'));
-> 'JWJj', 'abc'
```

Different base-64 encoding schemes exist. These are the encoding and decoding rules used by

```
TO_BASE64() and FROM_BASE64():
```

- The encoding for alphabet value 62 is `'+'`.
- The encoding for alphabet value 63 is `'/'`.
- Encoded output consists of groups of 4 printable characters. Each 3 bytes of the input data are

encoded using 4 characters. If the last group is incomplete, it is padded with `'='` characters to a length of 4.

- A newline is added after each 76 characters of encoded output to divide long output into multiple lines.
- Decoding recognizes and ignores newline, carriage return, tab, and space.

```
- TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM] str), TRIM([remstr FROM] str)
```

Returns the string `str` with all `remstr` prefixes or suffixes removed. If none of the specifiers `BOTH`,`LEADING`, or `TRAILING` is given, `BOTH` is assumed. `remstr` is optional and, if not specified, spaces are removed.

```
mysql> SELECT TRIM('  bar   ');
-> 'bar'
mysql> SELECT TRIM(LEADING 'x' FROM 'xxxbarxxx');
-> 'barxxx'
mysql> SELECT TRIM(BOTH 'x' FROM 'xxxbarxxx');
-> 'bar'
mysql> SELECT TRIM(TRAILING 'xyz' FROM 'barxxyz');
-> 'barx'
```

This function is multibyte safe.

```
- UCASE(str)
```

`UCASE()` is a synonym for `UPPER()`.

```
- UNHEX(str)
```

For a string argument `str`, `UNHEX(str)` interprets each pair of characters in the argument as a hexadecimal number and converts it to the byte represented by the number. The return value is a binary string.

```
mysql> SELECT UNHEX('4D7953514C');
-> 'MySQL'
mysql> SELECT X'4D7953514C';
-> 'MySQL'
mysql> SELECT UNHEX(HEX('string'));
-> 'string'
mysql> SELECT HEX(UNHEX('1267'));
```

String Functions and Operators

```
-> '1267'
```

The characters in the argument string must be legal hexadecimal digits: `'0'` .. `'9'`, `'A'` .. `'F'`, `'a'` ..

`'f'`. If the argument contains any nonhexadecimal digits, the result is `NULL`:

```
mysql> SELECT UNHEX('GG');
+-------------+
| UNHEX('GG') |
+-------------+
| NULL        |
+-------------+
```

A `NULL` result can occur if the argument to `UNHEX()` is a `BINARY` column, because values are padded with `0x00` bytes when stored but those bytes are not stripped on retrieval. For example, `'41'` is stored into a `CHAR(3)` column as `'41 '` and retrieved as `'41'` (with the trailing pad space stripped), so`UNHEX()` for the column value returns `X'41'`. By contrast, `'41'` is stored into a `BINARY(3)` column as `'41\0'` and retrieved as `'41\0'` (with the trailing pad `0x00` byte not stripped). `'\0'` is not a legal hexadecimal digit, so `UNHEX()` for the column value returns `NULL`.

For a numeric argument N, the inverse of `HEX(N)` is not performed by `UNHEX()`. Use`CONV(HEX(N),16,10)` instead. See the description of `HEX()`.

If `UNHEX()` is invoked from within the `mysql` client, binary strings display using hexadecimal notation,depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

```
- UPPER(str)
```

Returns the string `str` with all characters changed to uppercase according to the current character set mapping. The default is `latin1` (cp1252 West European).

```
mysql> SELECT UPPER('Hej');
-> 'HEJ'
```

See the description of `LOWER()` for information that also applies to `UPPER()`. This included information about how to perform lettercase conversion of binary strings (`BINARY`, `VARBINARY`, `BLOB`) for which these functions are ineffective, and information about case folding for Unicode character sets.

This function is multibyte safe.

String Functions and Operators

```
- WEIGHT_STRING(str [AS {CHAR|BINARY}(N)] [LEVEL levels] [flags])
levels: N [ASC|DESC|REVERSE] [, N [ASC|DESC|REVERSE]] ...
```

This function returns the weight string for the input string. The return value is a binary string that represents the comparison and sorting value of the string. It has these properties:

```
- If WEIGHT_STRING(str1) = WEIGHT_STRING(str2), then str1 = str2 (str1 and str2 are
```

considered equal)

- If `WEIGHT_STRING(str1)` < `WEIGHT_STRING(str2)`, then `str1 < str2` (`str1` sorts before

```
str2)
```

`WEIGHT_STRING()` is a debugging function intended for internal use. Its behavior can change without notice between MySQL versions. It can be used for testing and debugging of collations, especially if you are adding a new collation. See Section 10.14, “Adding a Collation to a Character Set”.

This list briefly summarizes the arguments. More details are given in the discussion following the list.

- `str`: The input string expression.
- `AS` clause: Optional; cast the input string to a given type and length.
- `LEVEL` clause: Optional; specify weight levels for the return value.
- `flags`: Optional; unused.

The input string, `str`, is a string expression. If the input is a nonbinary (character) string such as a`CHAR`, `VARCHAR`, or `TEXT` value, the return value contains the collation weights for the string. If the input is a binary (byte) string such as a `BINARY`, `VARBINARY`, or `BLOB` value, the return value is the same as the input (the weight for each byte in a binary string is the byte value). If the input is `NULL`,`WEIGHT_STRING()` returns `NULL`.

Examples:

```
mysql> SET @s = _latin1 'AB' COLLATE latin1_swedish_ci;
mysql> SELECT @s, HEX(@s), HEX(WEIGHT_STRING(@s));
+------+---------+------------------------+
| @s   | HEX(@s) | HEX(WEIGHT_STRING(@s)) |
+------+---------+------------------------+
| AB   | 4142    | 4142                   |
+------+---------+------------------------+
mysql> SET @s = _latin1 'ab' COLLATE latin1_swedish_ci;
mysql> SELECT @s, HEX(@s), HEX(WEIGHT_STRING(@s));
+------+---------+------------------------+
| @s   | HEX(@s) | HEX(WEIGHT_STRING(@s)) |
+------+---------+------------------------+
| ab   | 6162    | 4142                   |
+------+---------+------------------------+
mysql> SET @s = CAST('AB' AS BINARY);
mysql> SELECT @s, HEX(@s), HEX(WEIGHT_STRING(@s));
+------+---------+------------------------+
| @s   | HEX(@s) | HEX(WEIGHT_STRING(@s)) |
+------+---------+------------------------+
| AB   | 4142    | 4142                   |
+------+---------+------------------------+
mysql> SET @s = CAST('ab' AS BINARY);
mysql> SELECT @s, HEX(@s), HEX(WEIGHT_STRING(@s));
```

String Functions and Operators

```
+------+---------+------------------------+
| @s   | HEX(@s) | HEX(WEIGHT_STRING(@s)) |
+------+---------+------------------------+
| ab   | 6162    | 6162                   |
+------+---------+------------------------+
```

The preceding examples use `HEX()` to display the `WEIGHT_STRING()` result. Because the result is a binary value, `HEX()` can be especially useful when the result contains nonprinting values, to display it in printable form:

```
mysql> SET @s = CONVERT(X'C39F' USING utf8) COLLATE utf8_czech_ci;
mysql> SELECT HEX(WEIGHT_STRING(@s));
+------------------------+
| HEX(WEIGHT_STRING(@s)) |
+------------------------+
| 0FEA0FEA               |
+------------------------+
```

For non-`NULL` return values, the data type of the value is `VARBINARY` if its length is within the maximum length for `VARBINARY`, otherwise the data type is `BLOB`.

The `AS` clause may be given to cast the input string to a nonbinary or binary string and to force it to a given length:

- `AS CHAR(N)` casts the string to a nonbinary string and pads it on the right with spaces to a length of N

characters. N must be at least 1. If N is less than the length of the input string, the string is truncated to N characters. No warning occurs for truncation.

- `AS BINARY(N)` is similar but casts the string to a binary string, N is measured in bytes (not

characters), and padding uses `0x00` bytes (not spaces).

```
mysql> SET NAMES 'latin1';
mysql> SELECT HEX(WEIGHT_STRING('ab' AS CHAR(4)));
+-------------------------------------+
| HEX(WEIGHT_STRING('ab' AS CHAR(4))) |
+-------------------------------------+
| 41422020                            |
+-------------------------------------+
mysql> SET NAMES 'utf8';
mysql> SELECT HEX(WEIGHT_STRING('ab' AS CHAR(4)));
+-------------------------------------+
| HEX(WEIGHT_STRING('ab' AS CHAR(4))) |
+-------------------------------------+
| 0041004200200020                    |
+-------------------------------------+
mysql> SELECT HEX(WEIGHT_STRING('ab' AS BINARY(4)));
+---------------------------------------+
| HEX(WEIGHT_STRING('ab' AS BINARY(4))) |
+---------------------------------------+
| 61620000                              |
```

String Functions and Operators

```
+---------------------------------------+
```

The `LEVEL` clause may be given to specify that the return value should contain weights for specific collation levels.

The `levels` specifier following the `LEVEL` keyword may be given either as a list of one or more integers separated by commas, or as a range of two integers separated by a dash. Whitespace around the punctuation characters does not matter.

Examples:

```
LEVEL 1
LEVEL 2, 3, 5
LEVEL 1-3
```

Any level less than 1 is treated as 1. Any level greater than the maximum for the input string collation is treated as maximum for the collation. The maximum varies per collation, but is never greater than 6.

In a list of levels, levels must be given in increasing order. In a range of levels, if the second number is less than the first, it is treated as the first number (for example, 4-2 is the same as 4-4).

If the `LEVEL` clause is omitted, MySQL assumes `LEVEL 1 - max`, where `max` is the maximum level for the collation.

If `LEVEL` is specified using list syntax (not range syntax), any level number can be followed by these modifiers:

- `ASC`: Return the weights without modification. This is the default.
- `DESC`: Return bitwise-inverted weights (for example, `0x78f0 DESC` = `0x870f`).
- `REVERSE`: Return the weights in reverse order (that is,the weights for the reversed string, with the first

character last and the last first).

Examples:

```
mysql> SELECT HEX(WEIGHT_STRING(0x007fff LEVEL 1));
+--------------------------------------+
| HEX(WEIGHT_STRING(0x007fff LEVEL 1)) |
+--------------------------------------+
| 007FFF                               |
+--------------------------------------+
mysql> SELECT HEX(WEIGHT_STRING(0x007fff LEVEL 1 DESC));
+-------------------------------------------+
| HEX(WEIGHT_STRING(0x007fff LEVEL 1 DESC)) |
+-------------------------------------------+
| FF8000                                    |
+-------------------------------------------+
mysql> SELECT HEX(WEIGHT_STRING(0x007fff LEVEL 1 REVERSE));
+----------------------------------------------+
| HEX(WEIGHT_STRING(0x007fff LEVEL 1 REVERSE)) |
+----------------------------------------------+
| FF7F00                                       |
+----------------------------------------------+
mysql> SELECT HEX(WEIGHT_STRING(0x007fff LEVEL 1 DESC REVERSE));
+---------------------------------------------------+
| HEX(WEIGHT_STRING(0x007fff LEVEL 1 DESC REVERSE)) |
+---------------------------------------------------+
| 0080FF                                            |
```

String Comparison Functions and Operators

```
+---------------------------------------------------+
```

The `flags` clause currently is unused.

If `WEIGHT_STRING()` is invoked from within the `mysql` client, binary strings display using hexadecimal notation, depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

### 12.8.1 String Comparison Functions and Operators

Table 12.13 String Comparison Functions and Operators Name Description`LIKE` Simple pattern matching`NOT LIKE` Negation of simple pattern matching`STRCMP()` Compare two strings If a string function is given a binary string as an argument, the resulting string is also a binary string. A number converted to a string is treated as a binary string. This affects only comparisons.

Normally, if any expression in a string comparison is case-sensitive, the comparison is performed in case-sensitive fashion.

If a string function is invoked from within the `mysql` client, binary strings display using hexadecimal notation, depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

```
- expr LIKE pat [ESCAPE 'escape_char']
```

Pattern matching using an SQL pattern. Returns 1 (`TRUE`) or 0 (`FALSE`). If either `expr` or `pat` is `NULL`,the result is `NULL`.

The pattern need not be a literal string. For example, it can be specified as a string expression or table column. In the latter case, the column must be defined as one of the MySQL string types (see Section 11.3, “String Data Types”).

Per the SQL standard, `LIKE` performs matching on a per-character basis, thus it can produce results different from the = comparison operator:

```
mysql> SELECT 'ä' LIKE 'ae' COLLATE latin1_german2_ci;
+-----------------------------------------+
| 'ä' LIKE 'ae' COLLATE latin1_german2_ci |
+-----------------------------------------+
|                                       0 |
+-----------------------------------------+
mysql> SELECT 'ä' = 'ae' COLLATE latin1_german2_ci;
+--------------------------------------+
| 'ä' = 'ae' COLLATE latin1_german2_ci |
+--------------------------------------+
|                                    1 |
+--------------------------------------+
```

In particular, trailing spaces are significant, which is not true for comparisons of nonbinary strings (`CHAR`,`VARCHAR`, and `TEXT` values) performed with the = operator:

```
mysql> SELECT 'a' = 'a ', 'a' LIKE 'a ';
+------------+---------------+
| 'a' = 'a ' | 'a' LIKE 'a ' |
+------------+---------------+
```

String Comparison Functions and Operators

```
|          1 |             0 |
+------------+---------------+
1 row in set (0.00 sec)
```

With `LIKE` you can use the following two wildcard characters in the pattern:

- % matches any number of characters, even zero characters.
- _ matches exactly one character.

```
mysql> SELECT 'David!' LIKE 'David_';
-> 1
mysql> SELECT 'David!' LIKE '%D%v%';
-> 1
```

To test for literal instances of a wildcard character, precede it by the escape character. If you do not specify the `ESCAPE` character, \ is assumed, unless the `NO_BACKSLASH_ESCAPES` SQL mode is enabled. In that case, no escape character is used.

- `\%` matches one % character.
- `\_` matches one _ character.

```
mysql> SELECT 'David!' LIKE 'David\_';
-> 0
mysql> SELECT 'David_' LIKE 'David\_';
-> 1
```

To specify a different escape character, use the `ESCAPE` clause:

```
mysql> SELECT 'David_' LIKE 'David|_' ESCAPE '|';
-> 1
```

The escape sequence should be one character long to specify the escape character, or empty to specify that no escape character is used. The expression must evaluate as a constant at execution time. If the`NO_BACKSLASH_ESCAPES` SQL mode is enabled, the sequence cannot be empty.

The following two statements illustrate that string comparisons are not case-sensitive unless one of the operands is case-sensitive (uses a case-sensitive collation or is a binary string):

```
mysql> SELECT 'abc' LIKE 'ABC';
-> 1
mysql> SELECT 'abc' LIKE _latin1 'ABC' COLLATE latin1_general_cs;
-> 0
mysql> SELECT 'abc' LIKE _latin1 'ABC' COLLATE latin1_bin;
-> 0
mysql> SELECT 'abc' LIKE BINARY 'ABC';
-> 0
```

As an extension to standard SQL, MySQL permits `LIKE` on numeric expressions.

```
mysql> SELECT 10 LIKE '1%';
-> 1
```

MySQL attempts in such cases to perform implicit conversion of the expression to a string. See Section 12.3, “Type Conversion in Expression Evaluation”.

Note MySQL uses C escape syntax in strings (for example, `\n` to represent the newline character). If you want a `LIKE` string to contain a literal \, you must String Comparison Functions and Operators double it. (Unless the `NO_BACKSLASH_ESCAPES` SQL mode is enabled, in which case no escape character is used.) For example, to search for `\n`, specify it as`\\n`. To search for \, specify it as `\\\\`; this is because the backslashes are stripped once by the parser and again when the pattern match is made, leaving a single backslash to be matched against.

Exception: At the end of the pattern string, backslash can be specified as `\\`.

At the end of the string, backslash stands for itself because there is nothing following to escape. Suppose that a table contains the following values:

```
mysql> SELECT filename FROM t1;
+--------------+
| filename     |
+--------------+
| C:           |
| C:\          |
| C:\Programs  |
| C:\Programs\ |
+--------------+
```

To test for values that end with backslash, you can match the values using either of the following patterns:

```
mysql> SELECT filename, filename LIKE '%\\' FROM t1;
+--------------+---------------------+
| filename     | filename LIKE '%\\' |
+--------------+---------------------+
| C:           |                   0 |
| C:\          |                   1 |
| C:\Programs  |                   0 |
| C:\Programs\ |                   1 |
+--------------+---------------------+
mysql> SELECT filename, filename LIKE '%\\\\' FROM t1;
+--------------+-----------------------+
| filename     | filename LIKE '%\\\\' |
+--------------+-----------------------+
| C:           |                     0 |
| C:\          |                     1 |
| C:\Programs  |                     0 |
| C:\Programs\ |                     1 |
+--------------+-----------------------+
- expr NOT LIKE pat [ESCAPE 'escape_char']
```

This is the same as `NOT (expr LIKE pat [ESCAPE 'escape_char'])`.

Note Aggregate queries involving `NOT LIKE` comparisons with columns containing`NULL` may yield unexpected results. For example, consider the following table and data:

```
CREATE TABLE foo (bar VARCHAR(10));
INSERT INTO foo VALUES (NULL), (NULL);
The query SELECT COUNT(*) FROM foo WHERE bar LIKE '%baz%';
```

returns 0. You might assume that `SELECT COUNT(*) FROM foo WHERE bar``NOT LIKE '%baz%';` would return 2. However, this is not the case: The second query returns 0. This is because `NULL NOT LIKE expr` always returns `NULL`,regardless of the value of `expr`. The same is true for aggregate queries involving Regular Expressions`NULL` and comparisons using `NOT RLIKE` or `NOT REGEXP`. In such cases, you must test explicitly for `NOT NULL` using `OR` (and not `AND`), as shown here:

```
SELECT COUNT(*) FROM foo WHERE bar NOT LIKE '%baz%' OR bar IS NULL;
- STRCMP(expr1,expr2)
```

`STRCMP()` returns 0 if the strings are the same, `-1` if the first argument is smaller than the second according to the current sort order, and 1 otherwise.

```
mysql> SELECT STRCMP('text', 'text2');
-> -1
mysql> SELECT STRCMP('text2', 'text');
-> 1
mysql> SELECT STRCMP('text', 'text');
-> 0
```

`STRCMP()` performs the comparison using the collation of the arguments.

```
mysql> SET @s1 = _latin1 'x' COLLATE latin1_general_ci;
mysql> SET @s2 = _latin1 'X' COLLATE latin1_general_ci;
mysql> SET @s3 = _latin1 'x' COLLATE latin1_general_cs;
mysql> SET @s4 = _latin1 'X' COLLATE latin1_general_cs;
mysql> SELECT STRCMP(@s1, @s2), STRCMP(@s3, @s4);
+------------------+------------------+
| STRCMP(@s1, @s2) | STRCMP(@s3, @s4) |
+------------------+------------------+
|                0 |                1 |
+------------------+------------------+
```

If the collations are incompatible, one of the arguments must be converted to be compatible with the other. See Section 10.8.4, “Collation Coercibility in Expressions”.

```
mysql> SELECT STRCMP(@s1, @s3);
ERROR 1267 (HY000): Illegal mix of collations (latin1_general_ci,IMPLICIT)
and (latin1_general_cs,IMPLICIT) for operation 'strcmp'
mysql> SELECT STRCMP(@s1, @s3 COLLATE latin1_general_ci);
+--------------------------------------------+
| STRCMP(@s1, @s3 COLLATE latin1_general_ci) |
+--------------------------------------------+
|                                          0 |
+--------------------------------------------+
```

### 12.8.2 Regular Expressions

Table 12.14 Regular Expression Functions and Operators Name Description`NOT REGEXP` Negation of REGEXP`REGEXP` Whether string matches regular expression`RLIKE` Whether string matches regular expression A regular expression is a powerful way of specifying a pattern for a complex search. This section discusses the operators available for regular expression matching and illustrates, with examples, some of the special characters and constructs that can be used for regular expression operations. See also Section 3.3.4.7,“Pattern Matching”.

MySQL uses Henry Spencer's implementation of regular expressions, which is aimed at conformance with POSIX 1003.2. MySQL uses the extended version to support regular expression pattern-matching operations in SQL statements. This section does not contain all the details that can be found in Henry Regular Expressions Spencer's `regex(7)` manual page. That manual page is included in MySQL source distributions, in the`regex.7` file under the `regex` directory.

- Regular Expression Function and Operator Descriptions
- Regular Expression Syntax

> Regular Expression Function and Operator Descriptions

```
- expr NOT REGEXP pat, expr NOT RLIKE pat
```

This is the same as `NOT (expr REGEXP pat)`.

```
- expr REGEXP pat, expr RLIKE pat
```

Returns 1 if the string `expr` matches the regular expression specified by the pattern `pat`, 0 otherwise. If either `expr` or `pat` is `NULL`, the return value is `NULL`.

`RLIKE` is a synonym for `REGEXP`, provided for `mSQL` compatibility.

The pattern can be an extended regular expression, the syntax for which is discussed in Regular Expression Syntax. The pattern need not be a literal string. For example, it can be specified as a string expression or table column.

Note MySQL uses C escape syntax in strings (for example, `\n` to represent the newline character). If you want your `expr` or `pat` argument to contain a literal \,you must double it. (Unless the `NO_BACKSLASH_ESCAPES` SQL mode is enabled,in which case no escape character is used.)Regular expression operations use the character set and collation of the string expression and pattern arguments when deciding the type of a character and performing the comparison. If the arguments have different character sets or collations, coercibility rules apply as described in Section 10.8.4, “Collation Coercibility in Expressions”. If either argument is a binary string, the arguments are handled in case-sensitive fashion as binary strings.

```
mysql> SELECT 'Michael!' REGEXP '.*';
+------------------------+
| 'Michael!' REGEXP '.*' |
+------------------------+
|                      1 |
+------------------------+
mysql> SELECT 'new*\n*line' REGEXP 'new\\*.\\*line';
+---------------------------------------+
| 'new*\n*line' REGEXP 'new\\*.\\*line' |
+---------------------------------------+
|                                     0 |
+---------------------------------------+
mysql> SELECT 'a' REGEXP '^[a-d]';
+---------------------+
| 'a' REGEXP '^[a-d]' |
+---------------------+
|                   1 |
+---------------------+
```

Warning The `REGEXP` and `RLIKE` operators work in byte-wise fashion, so they are not multibyte safe and may produce unexpected results with multibyte character Regular Expressions sets. In addition, these operators compare characters by their byte values and accented characters may not compare as equal even if a given collation treats them as equal.

> Regular Expression Syntax

A regular expression describes a set of strings. The simplest regular expression is one that has no special characters in it. For example, the regular expression `hello` matches `hello` and nothing else.

Nontrivial regular expressions use certain special constructs so that they can match more than one string.

For example, the regular expression `hello|world` contains the | alternation operator and matches either the `hello` or `world`.

As a more complex example, the regular expression `B[an]*s` matches any of the strings `Bananas`,`Baaaaas`, `Bs`, and any other string starting with a B, ending with an s, and containing any number of a or n characters in between.

A regular expression for the `REGEXP` operator may use any of the following special characters and constructs:

- ^

Match the beginning of a string.

```
mysql> SELECT 'fo\nfo' REGEXP '^fo$';                   -> 0
mysql> SELECT 'fofo' REGEXP '^fo';                      -> 1
```

- $

Match the end of a string.

```
mysql> SELECT 'fo\no' REGEXP '^fo\no$';                 -> 1
mysql> SELECT 'fo\no' REGEXP '^fo$';                    -> 0
```

- .

Match any character (including carriage return and newline).

```
mysql> SELECT 'fofo' REGEXP '^f.*$';                    -> 1
mysql> SELECT 'fo\r\nfo' REGEXP '^f.*$';                -> 1
```

- `a*`

Match any sequence of zero or more a characters.

```
mysql> SELECT 'Ban' REGEXP '^Ba*n';                     -> 1
mysql> SELECT 'Baaan' REGEXP '^Ba*n';                   -> 1
mysql> SELECT 'Bn' REGEXP '^Ba*n';                      -> 1
```

- `a+`

Match any sequence of one or more a characters.

```
mysql> SELECT 'Ban' REGEXP '^Ba+n';                     -> 1
mysql> SELECT 'Bn' REGEXP '^Ba+n';                      -> 0
```

- `a?`

Match either zero or one a character.

```
mysql> SELECT 'Bn' REGEXP '^Ba?n';                      -> 1
mysql> SELECT 'Ban' REGEXP '^Ba?n';                     -> 1
```

Regular Expressions

```
mysql> SELECT 'Baan' REGEXP '^Ba?n';                    -> 0
- de|abc
```

Alternation; match either of the sequences `de` or `abc`.

```
mysql> SELECT 'pi' REGEXP 'pi|apa';                     -> 1
mysql> SELECT 'axe' REGEXP 'pi|apa';                    -> 0
mysql> SELECT 'apa' REGEXP 'pi|apa';                    -> 1
mysql> SELECT 'apa' REGEXP '^(pi|apa)$';                -> 1
mysql> SELECT 'pi' REGEXP '^(pi|apa)$';                 -> 1
mysql> SELECT 'pix' REGEXP '^(pi|apa)$';                -> 0
- (abc)*
```

Match zero or more instances of the sequence `abc`.

```
mysql> SELECT 'pi' REGEXP '^(pi)*$';                    -> 1
mysql> SELECT 'pip' REGEXP '^(pi)*$';                   -> 0
mysql> SELECT 'pipi' REGEXP '^(pi)*$';                  -> 1
- {1}, {2,3}
```

Repetition; `{n}` and `{m,n}` notation provide a more general way of writing regular expressions that match many occurrences of the previous atom (or “piece”) of the pattern. m and n are integers.

- `a*`

Can be written as `a{0,}`.

- `a+`

Can be written as `a{1,}`.

- `a?`

Can be written as `a{0,1}`.

To be more precise, `a{n}` matches exactly n instances of a. `a{n,}` matches n or more instances of a.

`a{m,n}` matches m through n instances of a, inclusive. If both m and n are given, m must be less than or equal to n.

m and n must be in the range from 0 to `RE_DUP_MAX` (default 255), inclusive.

```
mysql> SELECT 'abcde' REGEXP 'a[bcd]{2}e';              -> 0
mysql> SELECT 'abcde' REGEXP 'a[bcd]{3}e';              -> 1
mysql> SELECT 'abcde' REGEXP 'a[bcd]{1,10}e';           -> 1
- [a-dX], [^a-dX]
```

Matches any character that is (or is not, if ^ is used) either a, b, c, d or X. A - character between two other characters forms a range that matches all characters from the first character to the second. For example, `[0-9]` matches any decimal digit. To include a literal ] character, it must immediately follow the opening bracket [. To include a literal - character, it must be written first or last. Any character that does not have a defined special meaning inside a `[]` pair matches only itself.

```
mysql> SELECT 'aXbc' REGEXP '[a-dXYZ]';                 -> 1
mysql> SELECT 'aXbc' REGEXP '^[a-dXYZ]$';               -> 0
mysql> SELECT 'aXbc' REGEXP '^[a-dXYZ]+$';              -> 1
mysql> SELECT 'aXbc' REGEXP '^[^a-dXYZ]+$';             -> 0
mysql> SELECT 'gheis' REGEXP '^[^a-dXYZ]+$';            -> 1
```

Regular Expressions

```
mysql> SELECT 'gheisa' REGEXP '^[^a-dXYZ]+$';           -> 0
- [.characters.]
```

Within a bracket expression (written using [ and ]), matches the sequence of characters of that collating element. `characters` is either a single character or a character name like `newline`. The following table lists the permissible character names.

The following table shows the permissible character names and the characters that they match. For characters given as numeric values, the values are represented in octal.

> Name Character Name Character

```
NUL  0  SOH  001
STX  002  ETX  003
EOT  004  ENQ  005
ACK  006  BEL  007
alert  007  BS  010
backspace  '\b'  HT  011
tab  '\t'  LF  012
newline  '\n'  VT  013
vertical-tab  '\v'  FF  014
form-feed  '\f'  CR  015
carriage-return  '\r'  SO  016
SI  017  DLE  020
DC1  021  DC2  022
DC3  023  DC4  024
NAK  025  SYN  026
ETB  027  CAN  030
EM  031  SUB  032
ESC  033  IS4  034
FS  034  IS3  035
GS  035  IS2  036
RS  036  IS1  037
US  037  space  ' '
exclamation-mark  '!'  quotation-mark  '"'
number-sign  '#'  dollar-sign  '$'
percent-sign  '%'  ampersand  '&'
apostrophe  '\''  left-parenthesis  '('
right-parenthesis  ')'  asterisk  '*'
plus-sign  '+'  comma  ','
hyphen  '-'  hyphen-minus  '-'
period  '.'  full-stop  '.'
```

Regular Expressions Name Character Name Character

```
slash  '/'  solidus  '/'
zero  '0'  one  '1'
two  '2'  three  '3'
four  '4'  five  '5'
six  '6'  seven  '7'
eight  '8'  nine  '9'
colon  ':'  semicolon  ';'
less-than-sign  '<'  equals-sign  '='
greater-than-sign  '>'  question-mark  '?'
commercial-at  '@'  left-square-  '['
bracket
backslash  '\\'  reverse-solidus  '\\'
right-square-  ']'  circumflex  '^'
bracket
circumflex-accent  '^'  underscore  '_'
low-line  '_'  grave-accent  '`'
left-brace  '{'  left-curly-bracket '{'
vertical-line  '|'  right-brace  '}'
right-curly-  '}'  tilde  '~'
bracket
DEL  177
mysql> SELECT '~' REGEXP '[[.~.]]';                     -> 1
mysql> SELECT '~' REGEXP '[[.tilde.]]';                 -> 1
- [=character_class=]
```

Within a bracket expression (written using [ and ]), `[=character_class=]` represents an equivalence class. It matches all characters with the same collation value, including itself. For example,if o and `(+)` are the members of an equivalence class, `[[=o=]]`, `[[=(+)=]]`, and `[o(+)]` are all synonymous. An equivalence class may not be used as an endpoint of a range.

```
- [:character_class:]
```

Within a bracket expression (written using [ and ]), `[:character_class:]` represents a character class that matches all characters belonging to that class. The following table lists the standard class names. These names stand for the character classes defined in the `ctype(3)` manual page. A particular locale may provide other class names. A character class may not be used as an endpoint of a range.

Character Class Name Meaning`alnum` Alphanumeric characters`alpha` Alphabetic characters`blank` Whitespace characters`cntrl` Control characters Character Set and Collation of Function Results Character Class Name Meaning`digit` Digit characters`graph` Graphic characters`lower` Lowercase alphabetic characters`print` Graphic or space characters`punct` Punctuation characters`space` Space, tab, newline, and carriage return`upper` Uppercase alphabetic characters`xdigit` Hexadecimal digit characters

```
mysql> SELECT 'justalnums' REGEXP '[[:alnum:]]+';       -> 1
mysql> SELECT '!!' REGEXP '[[:alnum:]]+';               -> 0
- [[:<:]], [[:>:]]
```

These markers stand for word boundaries. They match the beginning and end of words, respectively. A word is a sequence of word characters that is not preceded by or followed by word characters. A word character is an alphanumeric character in the `alnum` class or an underscore (_).

```
mysql> SELECT 'a word a' REGEXP '[[:<:]]word[[:>:]]';   -> 1
mysql> SELECT 'a xword a' REGEXP '[[:<:]]word[[:>:]]';  -> 0
```

To use a literal instance of a special character in a regular expression, precede it by two backslash (\)characters. The MySQL parser interprets one of the backslashes, and the regular expression library interprets the other. For example, to match the string `1+2` that contains the special + character, only the last of the following regular expressions is the correct one:

```
mysql> SELECT '1+2' REGEXP '1+2';                       -> 0
mysql> SELECT '1+2' REGEXP '1\+2';                      -> 0
mysql> SELECT '1+2' REGEXP '1\\+2';                     -> 1
```

### 12.8.3 Character Set and Collation of Function Results

MySQL has many operators and functions that return a string. This section answers the question: What is the character set and collation of such a string?

For simple functions that take string input and return a string result as output, the output's character set and collation are the same as those of the principal input value. For example, `UPPER(X)` returns a string with the same character string and collation as X. The same applies for `INSTR()`, `LCASE()`, `LOWER()`,

```
LTRIM(), MID(), REPEAT(), REPLACE(), REVERSE(), RIGHT(), RPAD(), RTRIM(), SOUNDEX(),
SUBSTRING(), TRIM(), UCASE(), and UPPER().
```

Note The `REPLACE()` function, unlike all other functions, always ignores the collation of the string input and performs a case-sensitive comparison.

If a string input or function result is a binary string, the string has the `binary` character set and collation.

This can be checked by using the `CHARSET()` and `COLLATION()` functions, both of which return `binary`for a binary string argument:

```
mysql> SELECT CHARSET(BINARY 'a'), COLLATION(BINARY 'a');
+---------------------+-----------------------+
| CHARSET(BINARY 'a') | COLLATION(BINARY 'a') |
+---------------------+-----------------------+
```

What Calendar Is Used By MySQL?

```
| binary              | binary                |
+---------------------+-----------------------+
```

For operations that combine multiple string inputs and return a single string output, the “aggregation rules”of standard SQL apply for determining the collation of the result:

- If an explicit `COLLATE Y` occurs, use Y.
- If explicit `COLLATE Y` and `COLLATE Z` occur, raise an error.
- Otherwise, if all collations are Y, use Y.
- Otherwise, the result has no collation.

For example, with `CASE ... WHEN a THEN b WHEN b THEN c COLLATE X END`, the resulting collation is X. The same applies for `UNION`, `||`, `CONCAT()`, `ELT()`, `GREATEST()`, `IF()`, and `LEAST()`.

For operations that convert to character data, the character set and collation of the strings that result from the operations are defined by the `character_set_connection` and `collation_connection` system variables that determine the default connection character set and collation (see Section 10.4, “Connection Character Sets and Collations”). This applies only to `CAST()`, `CONV()`, `FORMAT()`, `HEX()`, and `SPACE()`.

If there is any question about the character set or collation of the result returned by a string function, use the `CHARSET()` or `COLLATION()` function to find out:

```
mysql> SELECT USER(), CHARSET(USER()), COLLATION(USER());
+----------------+-----------------+-------------------+
| USER()         | CHARSET(USER()) | COLLATION(USER()) |
+----------------+-----------------+-------------------+
| test@localhost | utf8            | utf8_general_ci   |
+----------------+-----------------+-------------------+
mysql> SELECT CHARSET(COMPRESS('abc')), COLLATION(COMPRESS('abc'));
+--------------------------+----------------------------+
| CHARSET(COMPRESS('abc')) | COLLATION(COMPRESS('abc')) |
+--------------------------+----------------------------+
| binary                   | binary                     |
+--------------------------+----------------------------+
```

## 12.9 What Calendar Is Used By MySQL?

MySQL uses what is known as a proleptic Gregorian calendar.

Every country that has switched from the Julian to the Gregorian calendar has had to discard at least ten days during the switch. To see how this works, consider the month of October 1582, when the first Julian-to-Gregorian switch occurred.

Monday Tuesday Wednesday Thursday Friday Saturday Sunday 1 2 3 4 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 There are no dates between October 4 and October 15. This discontinuity is called the cutover. Any dates before the cutover are Julian, and any dates following the cutover are Gregorian. Dates during a cutover are nonexistent.

A calendar applied to dates when it was not actually in use is called proleptic. Thus, if we assume there was never a cutover and Gregorian rules always rule, we have a proleptic Gregorian calendar. This is what is used by MySQL, as is required by standard SQL. For this reason, dates prior to the cutover stored as Full-Text Search Functions MySQL `DATE` or `DATETIME` values must be adjusted to compensate for the difference. It is important to realize that the cutover did not occur at the same time in all countries, and that the later it happened, the more days were lost. For example, in Great Britain, it took place in 1752, when Wednesday September 2 was followed by Thursday September 14. Russia remained on the Julian calendar until 1918, losing 13 days in the process, and what is popularly referred to as its “October Revolution” occurred in November according to the Gregorian calendar.

## 12.10 Full-Text Search Functions

```
MATCH (col1,col2,...) AGAINST (expr [search_modifier])
search_modifier:
{
IN NATURAL LANGUAGE MODE
| IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION
| IN BOOLEAN MODE
| WITH QUERY EXPANSION
}
```

MySQL has support for full-text indexing and searching:

- A full-text index in MySQL is an index of type `FULLTEXT`.
- Full-text indexes can be used only with `InnoDB` or `MyISAM` tables, and can be created only for `CHAR`,

`VARCHAR`, or `TEXT` columns.

- A `FULLTEXT` index definition can be given in the `CREATE TABLE` statement when a table is created, or

added later using `ALTER TABLE` or `CREATE INDEX`.

- For large data sets, it is much faster to load your data into a table that has no `FULLTEXT` index and then

create the index after that, than to load data into a table that has an existing `FULLTEXT` index.

Full-text searching is performed using `MATCH() AGAINST()` syntax. `MATCH()` takes a comma-separated list that names the columns to be searched. `AGAINST` takes a string to search for, and an optional modifier that indicates what type of search to perform. The search string must be a string value that is constant during query evaluation. This rules out, for example, a table column because that can differ for each row.

There are three types of full-text searches:

- A natural language search interprets the search string as a phrase in natural human language (a

phrase in free text). There are no special operators, with the exception of double quote (") characters.

The stopword list applies. For more information about stopword lists, see Section 12.10.4, “Full-Text Stopwords”.

Full-text searches are natural language searches if the `IN NATURAL LANGUAGE MODE` modifier is given or if no modifier is given. For more information, see Section 12.10.1, “Natural Language Full-Text Searches”.

- A boolean search interprets the search string using the rules of a special query language. The string

contains the words to search for. It can also contain operators that specify requirements such that a word must be present or absent in matching rows, or that it should be weighted higher or lower than usual.

Certain common words (stopwords) are omitted from the search index and do not match if present in the search string. The `IN BOOLEAN MODE` modifier specifies a boolean search. For more information, see Section 12.10.2, “Boolean Full-Text Searches”.

- A query expansion search is a modification of a natural language search. The search string is used to

perform a natural language search. Then words from the most relevant rows returned by the search are added to the search string and the search is done again. The query returns the rows from the second Natural Language Full-Text Searches

```
search. The IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION or WITH QUERY EXPANSION
```

modifier specifies a query expansion search. For more information, see Section 12.10.3, “Full-Text Searches with Query Expansion”.

For information about `FULLTEXT` query performance, see Section 8.3.4, “Column Indexes”.

For more information about `InnoDB` `FULLTEXT` indexes, see Section 14.6.2.3, “InnoDB Full-Text Indexes”.

Constraints on full-text searching are listed in Section 12.10.5, “Full-Text Restrictions”.

The `myisam_ftdump` utility dumps the contents of a `MyISAM` full-text index. This may be helpful for debugging full-text queries. See Section 4.6.2, “myisam_ftdump — Display Full-Text Index information”.

### 12.10.1 Natural Language Full-Text Searches

By default or with the `IN NATURAL LANGUAGE MODE` modifier, the `MATCH()` function performs a natural language search for a string against a text collection. A collection is a set of one or more columns included in a `FULLTEXT` index. The search string is given as the argument to `AGAINST()`. For each row in the table, `MATCH()` returns a relevance value; that is, a similarity measure between the search string and the text in that row in the columns named in the `MATCH()` list.

```
mysql> CREATE TABLE articles (
->   id INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
->   title VARCHAR(200),
->   body TEXT,
->   FULLTEXT (title,body)
-> ) ENGINE=InnoDB;
Query OK, 0 rows affected (0.08 sec)
mysql> INSERT INTO articles (title,body) VALUES
->   ('MySQL Tutorial','DBMS stands for DataBase ...'),
->   ('How To Use MySQL Well','After you went through a ...'),
->   ('Optimizing MySQL','In this tutorial, we show ...'),
->   ('1001 MySQL Tricks','1. Never run mysqld as root. 2. ...'),
->   ('MySQL vs. YourSQL','In the following database comparison ...'),
->   ('MySQL Security','When configured properly, MySQL ...');
Query OK, 6 rows affected (0.01 sec)
Records: 6  Duplicates: 0  Warnings: 0
mysql> SELECT * FROM articles
-> WHERE MATCH (title,body)
-> AGAINST ('database' IN NATURAL LANGUAGE MODE);
+----+-------------------+------------------------------------------+
| id | title             | body                                     |
+----+-------------------+------------------------------------------+
|  1 | MySQL Tutorial    | DBMS stands for DataBase ...             |
|  5 | MySQL vs. YourSQL | In the following database comparison ... |
+----+-------------------+------------------------------------------+
2 rows in set (0.00 sec)
```

By default, the search is performed in case-insensitive fashion. To perform a case-sensitive full-text search, use a binary collation for the indexed columns. For example, a column that uses the `latin1`character set of can be assigned a collation of `latin1_bin` to make it case-sensitive for full-text searches.

When `MATCH()` is used in a `WHERE` clause, as in the example shown earlier, the rows returned are automatically sorted with the highest relevance first as long as the following conditions are met:

- There must be no explicit `ORDER BY` clause.
- The search must be performed using a full-text index scan rather than a table scan.

Natural Language Full-Text Searches

- If the query joins tables, the full-text index scan must be the leftmost non-constant table in the join.

Given the conditions just listed, it is usually less effort to specify using `ORDER BY` an explicit sort order when one is necessary or desired.

Relevance values are nonnegative floating-point numbers. Zero relevance means no similarity. Relevance is computed based on the number of words in the row (document), the number of unique words in the row,the total number of words in the collection, and the number of rows that contain a particular word.

Note The term “document” may be used interchangeably with the term “row”, and both terms refer to the indexed part of the row. The term “collection” refers to the indexed columns and encompasses all rows.

To simply count matches, you could use a query like this:

```
mysql> SELECT COUNT(*) FROM articles
-> WHERE MATCH (title,body)
-> AGAINST ('database' IN NATURAL LANGUAGE MODE);
+----------+
| COUNT(*) |
+----------+
|        2 |
+----------+
1 row in set (0.00 sec)
```

You might find it quicker to rewrite the query as follows:

```
mysql> SELECT
-> COUNT(IF(MATCH (title,body) AGAINST ('database' IN NATURAL LANGUAGE MODE), 1, NULL))
-> AS count
-> FROM articles;
+-------+
| count |
+-------+
|     2 |
+-------+
1 row in set (0.03 sec)
```

The first query does some extra work (sorting the results by relevance) but also can use an index lookup based on the `WHERE` clause. The index lookup might make the first query faster if the search matches few rows. The second query performs a full table scan, which might be faster than the index lookup if the search term was present in most rows.

For natural-language full-text searches, the columns named in the `MATCH()` function must be the same columns included in some `FULLTEXT` index in your table. For the preceding query, the columns named in the `MATCH()` function (`title` and `body`) are the same as those named in the definition of the `article`table's `FULLTEXT` index. To search the `title` or `body` separately, you would create separate `FULLTEXT`indexes for each column.

You can also perform a boolean search or a search with query expansion. These search types are described in Section 12.10.2, “Boolean Full-Text Searches”, and Section 12.10.3, “Full-Text Searches with Query Expansion”.

A full-text search that uses an index can name columns only from a single table in the `MATCH()` clause because an index cannot span multiple tables. For `MyISAM` tables, a boolean search can be done in the absence of an index (albeit more slowly), in which case it is possible to name columns from multiple tables.

The preceding example is a basic illustration that shows how to use the `MATCH()` function where rows are returned in order of decreasing relevance. The next example shows how to retrieve the relevance Natural Language Full-Text Searches values explicitly. Returned rows are not ordered because the `SELECT` statement includes neither `WHERE`nor `ORDER BY` clauses:

```
mysql> SELECT id, MATCH (title,body)
-> AGAINST ('Tutorial' IN NATURAL LANGUAGE MODE) AS score
-> FROM articles;
+----+---------------------+
| id | score               |
+----+---------------------+
|  1 | 0.22764469683170319 |
|  2 |                   0 |
|  3 | 0.22764469683170319 |
|  4 |                   0 |
|  5 |                   0 |
|  6 |                   0 |
+----+---------------------+
6 rows in set (0.00 sec)
```

The following example is more complex. The query returns the relevance values and it also sorts the rows in order of decreasing relevance. To achieve this result, specify `MATCH()` twice: once in the `SELECT` list and once in the `WHERE` clause. This causes no additional overhead, because the MySQL optimizer notices that the two `MATCH()` calls are identical and invokes the full-text search code only once.

```
mysql> SELECT id, body, MATCH (title,body)
->   AGAINST ('Security implications of running MySQL as root'
->   IN NATURAL LANGUAGE MODE) AS score
-> FROM articles
->   WHERE MATCH (title,body)
->   AGAINST('Security implications of running MySQL as root'
->   IN NATURAL LANGUAGE MODE);
+----+-------------------------------------+-----------------+
| id | body                                | score           |
+----+-------------------------------------+-----------------+
|  4 | 1. Never run mysqld as root. 2. ... | 1.5219271183014 |
|  6 | When configured properly, MySQL ... | 1.3114095926285 |
+----+-------------------------------------+-----------------+
2 rows in set (0.00 sec)
```

A phrase that is enclosed within double quote (") characters matches only rows that contain the phrase literally, as it was typed. The full-text engine splits the phrase into words and performs a search in the`FULLTEXT` index for the words. Nonword characters need not be matched exactly: Phrase searching requires only that matches contain exactly the same words as the phrase and in the same order. For example, `"test phrase"` matches `"test, phrase"`. If the phrase contains no words that are in the index, the result is empty. For example, if all words are either stopwords or shorter than the minimum length of indexed words, the result is empty.

The MySQL `FULLTEXT` implementation regards any sequence of true word characters (letters, digits, and underscores) as a word. That sequence may also contain apostrophes ('), but not more than one in a row.

This means that `aaa'bbb` is regarded as one word, but `aaa''bbb` is regarded as two words. Apostrophes at the beginning or the end of a word are stripped by the `FULLTEXT` parser; `'aaa'bbb'` would be parsed as `aaa'bbb`.

The `FULLTEXT` parser determines where words start and end by looking for certain delimiter characters;

for example, (space), , (comma), and . (period). If words are not separated by delimiters (as in, for example, Chinese), the `FULLTEXT` parser cannot determine where a word begins or ends. To be able to add words or other indexed terms in such languages to a `FULLTEXT` index, you must preprocess them so that they are separated by some arbitrary delimiter.

It is possible to write a plugin that replaces the built-in full-text parser (only supported with `MyISAM`). For details, see The MySQL Plugin API. For example parser plugin source code, see the `plugin/fulltext`directory of a MySQL source distribution.

Boolean Full-Text Searches Some words are ignored in full-text searches:

- Any word that is too short is ignored. The default minimum length of words that are found by full-text

searches is three characters for `InnoDB` search indexes, or four characters for `MyISAM`. You can control the cutoff by setting a configuration option before creating the index: `innodb_ft_min_token_size`configuration option for `InnoDB` search indexes, or `ft_min_word_len` for `MyISAM`.

- Words in the stopword list are ignored. A stopword is a word such as “the” or “some” that is so

common that it is considered to have zero semantic value. There is a built-in stopword list, but it can be overridden by a user-defined list. The stopword lists and related configuration options are different for `InnoDB` search indexes and `MyISAM` ones. Stopword processing is controlled by the configuration options `innodb_ft_enable_stopword`, `innodb_ft_server_stopword_table`,and `innodb_ft_user_stopword_table` for `InnoDB` search indexes, and `ft_stopword_file` for`MyISAM` ones.

See Section 12.10.4, “Full-Text Stopwords” to view default stopword lists and how to change them. The default minimum word length can be changed as described in Section 12.10.6, “Fine-Tuning MySQL Full-Text Search”.

Every correct word in the collection and in the query is weighted according to its significance in the collection or query. Thus, a word that is present in many documents has a lower weight, because it has lower semantic value in this particular collection. Conversely, if the word is rare, it receives a higher weight.

The weights of the words are combined to compute the relevance of the row. This technique works best with large collections.

MyISAM Limitation For very small tables, word distribution does not adequately reflect their semantic value, and this model may sometimes produce bizarre results for search indexes on`MyISAM` tables. For example, although the word “MySQL” is present in every row of the `articles` table shown earlier, a search for the word in a `MyISAM` search index produces no results:

```
mysql> SELECT * FROM articles
-> WHERE MATCH (title,body)
-> AGAINST ('MySQL' IN NATURAL LANGUAGE MODE);
Empty set (0.00 sec)
```

The search result is empty because the word “MySQL” is present in at least 50% of the rows, and so is effectively treated as a stopword. This filtering technique is more suitable for large data sets, where you might not want the result set to return every second row from a 1GB table, than for small data sets where it might cause poor results for popular terms.

The 50% threshold can surprise you when you first try full-text searching to see how it works, and makes `InnoDB` tables more suited to experimentation with full-text searches. If you create a `MyISAM` table and insert only one or two rows of text into it, every word in the text occurs in at least 50% of the rows. As a result, no search returns any results until the table contains more rows. Users who need to bypass the 50% limitation can build search indexes on `InnoDB` tables, or use the boolean search mode explained in Section 12.10.2, “Boolean Full-Text Searches”.

### 12.10.2 Boolean Full-Text Searches

MySQL can perform boolean full-text searches using the `IN BOOLEAN MODE` modifier. With this modifier,certain characters have special meaning at the beginning or end of words in the search string. In the following query, the + and - operators indicate that a word must be present or absent, respectively, for Boolean Full-Text Searches a match to occur. Thus, the query retrieves all the rows that contain the word “MySQL” but that do not contain the word “YourSQL”:

```
mysql> SELECT * FROM articles WHERE MATCH (title,body)
-> AGAINST ('+MySQL -YourSQL' IN BOOLEAN MODE);
+----+-----------------------+-------------------------------------+
| id | title                 | body                                |
+----+-----------------------+-------------------------------------+
|  1 | MySQL Tutorial        | DBMS stands for DataBase ...        |
|  2 | How To Use MySQL Well | After you went through a ...        |
|  3 | Optimizing MySQL      | In this tutorial, we show ...       |
|  4 | 1001 MySQL Tricks     | 1. Never run mysqld as root. 2. ... |
|  6 | MySQL Security        | When configured properly, MySQL ... |
+----+-----------------------+-------------------------------------+
```

Note In implementing this feature, MySQL uses what is sometimes referred to as implied Boolean logic, in which

- + stands for `AND`
- - stands for `NOT`
- [no operator] implies `OR`

Boolean full-text searches have these characteristics:

- They do not automatically sort rows in order of decreasing relevance.
- `InnoDB` tables require a `FULLTEXT` index on all columns of the `MATCH()` expression to perform boolean

queries. Boolean queries against a `MyISAM` search index can work even without a `FULLTEXT` index,although a search executed in this fashion would be quite slow.

- The minimum and maximum word length full-text parameters apply: `innodb_ft_min_token_size`

and `innodb_ft_max_token_size` for `InnoDB` search indexes, and `ft_min_word_len` and`ft_max_word_len` for `MyISAM` ones.

- The stopword list applies, controlled by `innodb_ft_enable_stopword`,

```
innodb_ft_server_stopword_table, and innodb_ft_user_stopword_table for InnoDB
```

search indexes, and `ft_stopword_file` for `MyISAM` ones.

- `InnoDB` full-text search does not support the use of multiple operators on a single search word, as in

this example: `'++apple'`. MyISAM full-text search successfully processes the same search ignoring all operators except for the operator immediately adjacent to the search word.

- `InnoDB` full-text search only supports leading plus or minus signs. For example, `InnoDB` supports

`'+apple'` but does not support `'apple+'`. Specifying a trailing plus or minus sign causes `InnoDB` to report a syntax error.

- `InnoDB` full-text search does not support the use of a leading plus sign with wildcard (`'+*'`), a plus and

minus sign combination (`'+-'`), or leading a plus and minus sign combination (`'+-apple'`). These invalid queries return a syntax error.

- `InnoDB` full-text search does not support the use of the @ symbol in boolean full-text searches. The @

symbol is reserved for use by the `@distance` proximity search operator.

- They do not use the 50% threshold that applies to `MyISAM` search indexes.

The boolean full-text search capability supports the following operators:Boolean Full-Text Searches

- +

A leading or trailing plus sign indicates that this word must be present in each row that is returned.

`InnoDB` only supports leading plus signs.

- -

A leading or trailing minus sign indicates that this word must not be present in any of the rows that are returned. `InnoDB` only supports leading minus signs.

The - operator acts only to exclude rows that are otherwise matched by other search terms. Thus, a boolean-mode search that contains only terms preceded by - returns an empty result. It does not return“all rows except those containing any of the excluded terms.”

- (no operator)

By default (when neither + nor - is specified), the word is optional, but the rows that contain it are rated higher. This mimics the behavior of `MATCH() AGAINST()` without the `IN BOOLEAN MODE` modifier.

```
- @distance
```

This operator works on `InnoDB` tables only. It tests whether two or more words all start within a specified distance from each other, measured in words. Specify the search words within a double-quoted string immediately before the `@distance` operator, for example, `MATCH(col1) AGAINST('"word1 word2`

```
word3" @8' IN BOOLEAN MODE)
- > <
```

These two operators are used to change a word's contribution to the relevance value that is assigned to a row. The > operator increases the contribution and the < operator decreases it. See the example following this list.

```
- ( )
```

Parentheses group words into subexpressions. Parenthesized groups can be nested.

- ~

A leading tilde acts as a negation operator, causing the word's contribution to the row's relevance to be negative. This is useful for marking “noise” words. A row containing such a word is rated lower than others, but is not excluded altogether, as it would be with the - operator.

- *

The asterisk serves as the truncation (or wildcard) operator. Unlike the other operators, it is appended to the word to be affected. Words match if they begin with the word preceding the * operator.

If a word is specified with the truncation operator, it is not stripped from a boolean query, even if it is too short or a stopword. Whether a word is too short is determined from the `innodb_ft_min_token_size`setting for `InnoDB` tables, or `ft_min_word_len` for `MyISAM` tables. The wildcarded word is considered as a prefix that must be present at the start of one or more words. If the minimum word length is 4, a search for `'+word +the*'` could return fewer rows than a search for `'+word +the'`, because the second query ignores the too-short search term `the`.

- "

A phrase that is enclosed within double quote (") characters matches only rows that contain the phrase literally, as it was typed. The full-text engine splits the phrase into words and performs a search in the Boolean Full-Text Searches`FULLTEXT` index for the words. Nonword characters need not be matched exactly: Phrase searching requires only that matches contain exactly the same words as the phrase and in the same order. For example, `"test phrase"` matches `"test, phrase"`.

If the phrase contains no words that are in the index, the result is empty. The words might not be in the index because of a combination of factors: if they do not exist in the text, are stopwords, or are shorter than the minimum length of indexed words.

The following examples demonstrate some search strings that use boolean full-text operators:

```
- 'apple banana'
```

Find rows that contain at least one of the two words.

```
- '+apple +juice'
```

Find rows that contain both words.

```
- '+apple macintosh'
```

Find rows that contain the word “apple”, but rank rows higher if they also contain “macintosh”.

```
- '+apple -macintosh'
```

Find rows that contain the word “apple” but not “macintosh”.

```
- '+apple ~macintosh'
```

Find rows that contain the word “apple”, but if the row also contains the word “macintosh”, rate it lower than if row does not. This is “softer” than a search for `'+apple -macintosh'`, for which the presence of “macintosh” causes the row not to be returned at all.

```
- '+apple +(>turnover <strudel)'
```

Find rows that contain the words “apple” and “turnover”, or “apple” and “strudel” (in any order), but rank“apple turnover” higher than “apple strudel”.

```
- 'apple*'
```

Find rows that contain words such as “apple”, “apples”, “applesauce”, or “applet”.

```
- '"some words"'
```

Find rows that contain the exact phrase “some words” (for example, rows that contain “some words of wisdom” but not “some noise words”).

Note The " characters that enclose the phrase are operator characters that delimit the phrase. They are not the quotation marks that enclose the search string itself.

> Relevancy Rankings for InnoDB Boolean Mode Search

`InnoDB` full-text search is modeled on the Sphinx full-text search engine, and the algorithms used are based on BM25 and TF-IDF ranking algorithms. For these reasons, relevancy rankings for `InnoDB`boolean full-text search may differ from `MyISAM` relevancy rankings.

`InnoDB` uses a variation of the “term frequency-inverse document frequency” (`TF-IDF`) weighting system to rank a document's relevance for a given full-text search query. The `TF-IDF` weighting is based on how Boolean Full-Text Searches frequently a word appears in a document, offset by how frequently the word appears in all documents in the collection. In other words, the more frequently a word appears in a document, and the less frequently the word appears in the document collection, the higher the document is ranked.

How Relevancy Ranking is Calculated The term frequency (`TF`) value is the number of times that a word appears in a document. The inverse document frequency (`IDF`) value of a word is calculated using the following formula, where`total_records` is the number of records in the collection, and `matching_records` is the number of records that the search term appears in.

```
${IDF} = log10( ${total_records} / ${matching_records} )
```

When a document contains a word multiple times, the IDF value is multiplied by the TF value:

```
${TF} * ${IDF}
```

Using the `TF` and `IDF` values, the relevancy ranking for a document is calculated using this formula:

```
${rank} = ${TF} * ${IDF} * ${IDF}
```

The formula is demonstrated in the following examples.

Relevancy Ranking for a Single Word Search This example demonstrates the relevancy ranking calculation for a single-word search.

```
mysql> CREATE TABLE articles (
id INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
title VARCHAR(200),
body TEXT,
FULLTEXT (title,body)
) ENGINE=InnoDB;
Query OK, 0 rows affected (1.04 sec)
mysql> INSERT INTO articles (title,body) VALUES
('MySQL Tutorial','This database tutorial ...'),
("How To Use MySQL",'After you went through a ...'),
('Optimizing Your Database','In this database tutorial ...'),
('MySQL vs. YourSQL','When comparing databases ...'),
('MySQL Security','When configured properly, MySQL ...'),
('Database, Database, Database','database database database'),
('1001 MySQL Tricks','1. Never run mysqld as root. 2. ...'),
('MySQL Full-Text Indexes', 'MySQL fulltext indexes use a ..');
Query OK, 8 rows affected (0.06 sec)
Records: 8  Duplicates: 0  Warnings: 0
mysql> SELECT id, title, body, MATCH (title,body)  AGAINST ('database' IN BOOLEAN MODE)
AS score FROM articles ORDER BY score DESC;
+----+------------------------------+-------------------------------------+---------------------+
| id | title                        | body                                | score               |
+----+------------------------------+-------------------------------------+---------------------+
|  6 | Database, Database, Database | database database database          |  1.0886961221694946 |
|  3 | Optimizing Your Database     | In this database tutorial ...       | 0.36289870738983154 |
|  1 | MySQL Tutorial               | This database tutorial ...          | 0.18144935369491577 |
|  2 | How To Use MySQL             | After you went through a ...        |                   0 |
|  4 | MySQL vs. YourSQL            | When comparing databases ...        |                   0 |
|  5 | MySQL Security               | When configured properly, MySQL ... |                   0 |
|  7 | 1001 MySQL Tricks            | 1. Never run mysqld as root. 2. ... |                   0 |
|  8 | MySQL Full-Text Indexes      | MySQL fulltext indexes use a ..     |                   0 |
+----+------------------------------+-------------------------------------+---------------------+
8 rows in set (0.00 sec)
```

Boolean Full-Text Searches There are 8 records in total, with 3 that match the “database” search term. The first record (`id 6`) contains the search term 6 times and has a relevancy ranking of `1.0886961221694946`. This ranking value is calculated using a `TF` value of 6 (the “database” search term appears 6 times in record `id 6`) and an `IDF`value of 0.42596873216370745, which is calculated as follows (where 8 is the total number of records and 3 is the number of records that the search term appears in):

```
${IDF} = log10( 8 / 3 ) = 0.42596873216370745
```

The `TF` and `IDF` values are then entered into the ranking formula:

```
${rank} = ${TF} * ${IDF} * ${IDF}
```

Performing the calculation in the MySQL command-line client returns a ranking value of

1.088696164686938.

```
mysql> SELECT 6*log10(8/3)*log10(8/3);
+-------------------------+
| 6*log10(8/3)*log10(8/3) |
+-------------------------+
|       1.088696164686938 |
+-------------------------+
1 row in set (0.00 sec)
```

Note You may notice a slight difference in the ranking values returned by the`SELECT ... MATCH ... AGAINST` statement and the MySQL command-line client (`1.0886961221694946` versus `1.088696164686938`). The difference is due to how the casts between integers and floats/doubles are performed internally by `InnoDB` (along with related precision and rounding decisions), and how they are performed elsewhere, such as in the MySQL command-line client or other types of calculators.

Relevancy Ranking for a Multiple Word Search This example demonstrates the relevancy ranking calculation for a multiple-word full-text search based on the `articles` table and data used in the previous example.

If you search on more than one word, the relevancy ranking value is a sum of the relevancy ranking value for each word, as shown in this formula:

```
${rank} = ${TF} * ${IDF} * ${IDF} + ${TF} * ${IDF} * ${IDF}
```

Performing a search on two terms ('mysql tutorial') returns the following results:

```
mysql> SELECT id, title, body, MATCH (title,body)  AGAINST ('mysql tutorial' IN BOOLEAN MODE)
AS score FROM articles ORDER BY score DESC;
+----+------------------------------+-------------------------------------+----------------------+
| id | title                        | body                                | score                |
+----+------------------------------+-------------------------------------+----------------------+
|  1 | MySQL Tutorial               | This database tutorial ...          |   0.7405621409416199 |
|  3 | Optimizing Your Database     | In this database tutorial ...       |   0.3624762296676636 |
|  5 | MySQL Security               | When configured properly, MySQL ... | 0.031219376251101494 |
|  8 | MySQL Full-Text Indexes      | MySQL fulltext indexes use a ..     | 0.031219376251101494 |
|  2 | How To Use MySQL             | After you went through a ...        | 0.015609688125550747 |
|  4 | MySQL vs. YourSQL            | When comparing databases ...        | 0.015609688125550747 |
|  7 | 1001 MySQL Tricks            | 1. Never run mysqld as root. 2. ... | 0.015609688125550747 |
|  6 | Database, Database, Database | database database database          |                    0 |
+----+------------------------------+-------------------------------------+----------------------+
8 rows in set (0.00 sec)
```

Full-Text Searches with Query Expansion In the first record (`id 8`), 'mysql' appears once and 'tutorial' appears twice. There are six matching records for 'mysql' and two matching records for 'tutorial'. The MySQL command-line client returns the expected ranking value when inserting these values into the ranking formula for a multiple word search:

```
mysql> SELECT (1*log10(8/6)*log10(8/6)) + (2*log10(8/2)*log10(8/2));
+-------------------------------------------------------+
| (1*log10(8/6)*log10(8/6)) + (2*log10(8/2)*log10(8/2)) |
+-------------------------------------------------------+
|                                    0.7405621541938003 |
+-------------------------------------------------------+
1 row in set (0.00 sec)
```

Note The slight difference in the ranking values returned by the `SELECT ...``MATCH ... AGAINST` statement and the MySQL command-line client is explained in the preceding example.

### 12.10.3 Full-Text Searches with Query Expansion

Full-text search supports query expansion (and in particular, its variant “blind query expansion”). This is generally useful when a search phrase is too short, which often means that the user is relying on implied knowledge that the full-text search engine lacks. For example, a user searching for “database” may really mean that “MySQL”, “Oracle”, “DB2”, and “RDBMS” all are phrases that should match “databases” and should be returned, too. This is implied knowledge.

Blind query expansion (also known as automatic relevance feedback) is enabled by adding `WITH QUERY``EXPANSION` or `IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION` following the search phrase.

It works by performing the search twice, where the search phrase for the second search is the original search phrase concatenated with the few most highly relevant documents from the first search. Thus,if one of these documents contains the word “databases” and the word “MySQL”, the second search finds the documents that contain the word “MySQL” even if they do not contain the word “database”. The following example shows this difference:

```
mysql> SELECT * FROM articles
WHERE MATCH (title,body)
AGAINST ('database' IN NATURAL LANGUAGE MODE);
+----+-------------------+------------------------------------------+
| id | title             | body                                     |
+----+-------------------+------------------------------------------+
|  1 | MySQL Tutorial    | DBMS stands for DataBase ...             |
|  5 | MySQL vs. YourSQL | In the following database comparison ... |
+----+-------------------+------------------------------------------+
2 rows in set (0.00 sec)
mysql> SELECT * FROM articles
WHERE MATCH (title,body)
AGAINST ('database' WITH QUERY EXPANSION);
+----+-----------------------+------------------------------------------+
| id | title                 | body                                     |
+----+-----------------------+------------------------------------------+
|  5 | MySQL vs. YourSQL     | In the following database comparison ... |
|  1 | MySQL Tutorial        | DBMS stands for DataBase ...             |
|  3 | Optimizing MySQL      | In this tutorial we show ...             |
|  6 | MySQL Security        | When configured properly, MySQL ...      |
|  2 | How To Use MySQL Well | After you went through a ...             |
|  4 | 1001 MySQL Tricks     | 1. Never run mysqld as root. 2. ...      |
+----+-----------------------+------------------------------------------+
6 rows in set (0.00 sec)
```

Another example could be searching for books by Georges Simenon about Maigret, when a user is not sure how to spell “Maigret”. A search for “Megre and the reluctant witnesses” finds only “Maigret and the Full-Text Stopwords Reluctant Witnesses” without query expansion. A search with query expansion finds all books with the word “Maigret” on the second pass.

Note Because blind query expansion tends to increase noise significantly by returning nonrelevant documents, use it only when a search phrase is short.

### 12.10.4 Full-Text Stopwords

The stopword list is loaded and searched for full-text queries using the server character set and collation (the values of the `character_set_server` and `collation_server` system variables).

False hits or misses might occur for stopword lookups if the stopword file or columns used for full-text indexing or searches have a character set or collation different from `character_set_server` or

```
collation_server.
```

Case sensitivity of stopword lookups depends on the server collation. For example, lookups are case-insensitive if the collation is `latin1_swedish_ci`, whereas lookups are case-sensitive if the collation is

```
latin1_general_cs or latin1_bin.
```

- Stopwords for InnoDB Search Indexes
- Stopwords for MyISAM Search Indexes

> Stopwords for InnoDB Search Indexes

`InnoDB` has a relatively short list of default stopwords, because documents from technical, literary, and other sources often use short words as keywords or in significant phrases. For example, you might search for “to be or not to be” and expect to get a sensible result, rather than having all those words ignored.

To see the default `InnoDB` stopword list, query the Information Schema

```
INNODB_FT_DEFAULT_STOPWORD table.
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_FT_DEFAULT_STOPWORD;
+-------+
| value |
+-------+
| a     |
| about |
| an    |
| are   |
| as    |
| at    |
| be    |
| by    |
| com   |
| de    |
| en    |
| for   |
| from  |
| how   |
| i     |
| in    |
| is    |
| it    |
| la    |
| of    |
| on    |
| or    |
| that  |
```

Full-Text Stopwords

```
| the   |
| this  |
| to    |
| was   |
| what  |
| when  |
| where |
| who   |
| will  |
| with  |
| und   |
| the   |
| www   |
+-------+
36 rows in set (0.00 sec)
```

To define your own stopword list for all `InnoDB` tables, define a table with the same structure as the `INNODB_FT_DEFAULT_STOPWORD` table, populate it with stopwords, and set the value of the`innodb_ft_server_stopword_table` option to a value in the form `db_name/table_name` before creating the full-text index. The stopword table must have a single `VARCHAR` column named `value`. The following example demonstrates creating and configuring a new global stopword table for `InnoDB`.

```
-- Create a new stopword table
mysql> CREATE TABLE my_stopwords(value VARCHAR(30)) ENGINE = INNODB;
Query OK, 0 rows affected (0.01 sec)
-- Insert stopwords (for simplicity, a single stopword is used in this example)
mysql> INSERT INTO my_stopwords(value) VALUES ('Ishmael');
Query OK, 1 row affected (0.00 sec)
-- Create the table
mysql> CREATE TABLE opening_lines (
id INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
opening_line TEXT(500),
author VARCHAR(200),
title VARCHAR(200)
) ENGINE=InnoDB;
Query OK, 0 rows affected (0.01 sec)
-- Insert data into the table
mysql> INSERT INTO opening_lines(opening_line,author,title) VALUES
('Call me Ishmael.','Herman Melville','Moby-Dick'),
('A screaming comes across the sky.','Thomas Pynchon','Gravity\'s Rainbow'),
('I am an invisible man.','Ralph Ellison','Invisible Man'),
('Where now? Who now? When now?','Samuel Beckett','The Unnamable'),
('It was love at first sight.','Joseph Heller','Catch-22'),
('All this happened, more or less.','Kurt Vonnegut','Slaughterhouse-Five'),
('Mrs. Dalloway said she would buy the flowers herself.','Virginia Woolf','Mrs. Dalloway'),
('It was a pleasure to burn.','Ray Bradbury','Fahrenheit 451');
Query OK, 8 rows affected (0.00 sec)
Records: 8  Duplicates: 0  Warnings: 0
-- Set the innodb_ft_server_stopword_table option to the new stopword table
mysql> SET GLOBAL innodb_ft_server_stopword_table = 'test/my_stopwords';
Query OK, 0 rows affected (0.00 sec)
-- Create the full-text index (which rebuilds the table if no FTS_DOC_ID column is defined)
mysql> CREATE FULLTEXT INDEX idx ON opening_lines(opening_line);
Query OK, 0 rows affected, 1 warning (1.17 sec)
Records: 0  Duplicates: 0  Warnings: 1
```

Full-Text Stopwords Verify that the specified stopword ('Ishmael') does not appear by querying the words in Information

```
Schema INNODB_FT_INDEX_TABLE.
```

Note By default, words less than 3 characters in length or greater than 84 characters in length do not appear in an `InnoDB` full-text search index. Maximum and minimum word length values are configurable using the `innodb_ft_max_token_size` and`innodb_ft_min_token_size` variables.

```
mysql> SET GLOBAL innodb_ft_aux_table='test/opening_lines';
Query OK, 0 rows affected (0.00 sec)
mysql> SELECT word FROM INFORMATION_SCHEMA.INNODB_FT_INDEX_TABLE LIMIT 15;
+-----------+
| word      |
+-----------+
| across    |
| all       |
| burn      |
| buy       |
| call      |
| comes     |
| dalloway  |
| first     |
| flowers   |
| happened  |
| herself   |
| invisible |
| less      |
| love      |
| man       |
+-----------+
15 rows in set (0.00 sec)
```

To create stopword lists on a table-by-table basis, create other stopword tables and use the`innodb_ft_user_stopword_table` option to specify the stopword table that you want to use before you create the full-text index.

> Stopwords for MyISAM Search Indexes

The stopword file is loaded and searched using `latin1` if `character_set_server` is `ucs2`, `utf16`,`utf16le`, or `utf32`.

To override the default stopword list for MyISAM tables, set the `ft_stopword_file` system variable.

(See Section 5.1.7, “Server System Variables”.) The variable value should be the path name of the file containing the stopword list, or the empty string to disable stopword filtering. The server looks for the file in the data directory unless an absolute path name is given to specify a different directory. After changing the value of this variable or the contents of the stopword file, restart the server and rebuild your `FULLTEXT`indexes.

The stopword list is free-form, separating stopwords with any nonalphanumeric character such as newline,space, or comma. Exceptions are the underscore character (_) and a single apostrophe (') which are treated as part of a word. The character set of the stopword list is the server's default character set; see Section 10.3.2, “Server Character Set and Collation”.

The following list shows the default stopwords for `MyISAM` search indexes. In a MySQL source distribution,you can find this list in the `storage/myisam/ft_static.c` file.

```
a's           able          about         above         according
accordingly   across        actually      after         afterwards
again         against       ain't         all           allow
```

Full-Text Stopwords

```
allows        almost        alone         along         already
also          although      always        am            among
amongst       an            and           another       any
anybody       anyhow        anyone        anything      anyway
anyways       anywhere      apart         appear        appreciate
appropriate   are           aren't        around        as
aside         ask           asking        associated    at
available     away          awfully       be            became
because       become        becomes       becoming      been
before        beforehand    behind        being         believe
below         beside        besides       best          better
between       beyond        both          brief         but
by            c'mon         c's           came          can
can't         cannot        cant          cause         causes
certain       certainly     changes       clearly       co
com           come          comes         concerning    consequently
consider      considering   contain       containing    contains
corresponding could         couldn't      course        currently
definitely    described     despite       did           didn't
different     do            does          doesn't       doing
don't         done          down          downwards     during
each          edu           eg            eight         either
else          elsewhere     enough        entirely      especially
et            etc           even          ever          every
everybody     everyone      everything    everywhere    ex
exactly       example       except        far           few
fifth         first         five          followed      following
follows       for           former        formerly      forth
four          from          further       furthermore   get
gets          getting       given         gives         go
goes          going         gone          got           gotten
greetings     had           hadn't        happens       hardly
has           hasn't        have          haven't       having
he            he's          hello         help          hence
her           here          here's        hereafter     hereby
herein        hereupon      hers          herself       hi
him           himself       his           hither        hopefully
how           howbeit       however       i'd           i'll
i'm           i've          ie            if            ignored
immediate     in            inasmuch      inc           indeed
indicate      indicated     indicates     inner         insofar
instead       into          inward        is            isn't
it            it'd          it'll         it's          its
itself        just          keep          keeps         kept
know          known         knows         last          lately
later         latter        latterly      least         less
lest          let           let's         like          liked
likely        little        look          looking       looks
ltd           mainly        many          may           maybe
me            mean          meanwhile     merely        might
more          moreover      most          mostly        much
must          my            myself        name          namely
nd            near          nearly        necessary     need
needs         neither       never         nevertheless  new
next          nine          no            nobody        non
none          noone         nor           normally      not
nothing       novel         now           nowhere       obviously
of            off           often         oh            ok
okay          old           on            once          one
ones          only          onto          or            other
others        otherwise     ought         our           ours
ourselves     out           outside       over          overall
own           particular    particularly  per           perhaps
placed        please        plus          possible      presumably
probably      provides      que           quite         qv
rather        rd            re            really        reasonably
regarding     regardless    regards       relatively    respectively
```

Full-Text Restrictions

```
right         said          same          saw           say
saying        says          second        secondly      see
seeing        seem          seemed        seeming       seems
seen          self          selves        sensible      sent
serious       seriously     seven         several       shall
she           should        shouldn't     since         six
so            some          somebody      somehow       someone
something     sometime      sometimes     somewhat      somewhere
soon          sorry         specified     specify       specifying
still         sub           such          sup           sure
t's           take          taken         tell          tends
th            than          thank         thanks        thanx
that          that's        thats         the           their
theirs        them          themselves    then          thence
there         there's       thereafter    thereby       therefore
therein       theres        thereupon     these         they
they'd        they'll       they're       they've       think
third         this          thorough      thoroughly    those
though        three         through       throughout    thru
thus          to            together      too           took
toward        towards       tried         tries         truly
try           trying        twice         two           un
under         unfortunately unless        unlikely      until
unto          up            upon          us            use
used          useful        uses          using         usually
value         various       very          via           viz
vs            want          wants         was           wasn't
way           we            we'd          we'll         we're
we've         welcome       well          went          were
weren't       what          what's        whatever      when
whence        whenever      where         where's       whereafter
whereas       whereby       wherein       whereupon     wherever
whether       which         while         whither       who
who's         whoever       whole         whom          whose
why           will          willing       wish          with
within        without       won't         wonder        would
wouldn't      yes           yet           you           you'd
you'll        you're        you've        your          yours
yourself      yourselves    zero
```

### 12.10.5 Full-Text Restrictions

- Full-text searches are supported for `InnoDB` and `MyISAM` tables only.
- Full-text searches are not supported for partitioned tables. See Section 19.6, “Restrictions and

Limitations on Partitioning”.

- Full-text searches can be used with most multibyte character sets. The exception is that for Unicode, the

`utf8` character set can be used, but not the `ucs2` character set. Although `FULLTEXT` indexes on `ucs2`columns cannot be used, you can perform `IN BOOLEAN MODE` searches on a `ucs2` column that has no such index.

The remarks for `utf8` also apply to `utf8mb4`, and the remarks for `ucs2` also apply to `utf16`, `utf16le`,and `utf32`.

- Ideographic languages such as Chinese and Japanese do not have word delimiters. Therefore, the

`FULLTEXT` parser cannot determine where words begin and end in these and other such languages.

- Although the use of multiple character sets within a single table is supported, all columns in a `FULLTEXT`

index must use the same character set and collation.

Fine-Tuning MySQL Full-Text Search

- The `MATCH()` column list must match exactly the column list in some `FULLTEXT` index definition for the

table, unless this `MATCH()` is `IN BOOLEAN MODE` on a `MyISAM` table. For `MyISAM` tables, boolean-mode searches can be done on nonindexed columns, although they are likely to be slow.

- The argument to `AGAINST()` must be a string value that is constant during query evaluation. This rules

out, for example, a table column because that can differ for each row.

- Index hints are more limited for `FULLTEXT` searches than for non-`FULLTEXT` searches. See

Section 8.9.3, “Index Hints”.

- For `InnoDB`, all DML operations (`INSERT`, `UPDATE`, `DELETE`) involving columns with full-text indexes

are processed at transaction commit time. For example, for an `INSERT` operation, an inserted string is tokenized and decomposed into individual words. The individual words are then added to full-text index tables when the transaction is committed. As a result, full-text searches only return committed data.

- The '%' character is not a supported wildcard character for full-text searches.

### 12.10.6 Fine-Tuning MySQL Full-Text Search

MySQL's full-text search capability has few user-tunable parameters. You can exert more control over full-text searching behavior if you have a MySQL source distribution because some changes require source code modifications. See Section 2.9, “Installing MySQL from Source”.

Full-text search is carefully tuned for effectiveness. Modifying the default behavior in most cases can actually decrease effectiveness. Do not alter the MySQL sources unless you know what you are doing.

Most full-text variables described in this section must be set at server startup time. A server restart is required to change them; they cannot be modified while the server is running.

Some variable changes require that you rebuild the `FULLTEXT` indexes in your tables. Instructions for doing so are given later in this section.

- Configuring Minimum and Maximum Word Length
- Configuring the Natural Language Search Threshold
- Modifying Boolean Full-Text Search Operators
- Character Set Modifications
- Rebuilding InnoDB Full-Text Indexes
- Optimizing InnoDB Full-Text Indexes
- Rebuilding MyISAM Full-Text Indexes

> Configuring Minimum and Maximum Word Length

The minimum and maximum lengths of words to be indexed are defined by the`innodb_ft_min_token_size` and `innodb_ft_max_token_size` for `InnoDB` search indexes, and`ft_min_word_len` and `ft_max_word_len` for `MyISAM` ones. After changing any of these options,rebuild your `FULLTEXT` indexes for the change to take effect. For example, to make two-character words searchable, you could put the following lines in an option file:

```
[mysqld]
innodb_ft_min_token_size=2
ft_min_word_len=2
```

Then restart the server and rebuild your `FULLTEXT` indexes. For `MyISAM` tables, note the remarks regarding `myisamchk` in the instructions that follow for rebuilding `MyISAM` full-text indexes.

Fine-Tuning MySQL Full-Text Search

> Configuring the Natural Language Search Threshold

For `MyISAM` search indexes, the 50% threshold for natural language searches is determined by the particular weighting scheme chosen. To disable it, look for the following line in `storage/myisam/`

```
ftdefs.h:
#define GWS_IN_USE GWS_PROB
```

Change that line to this:

```
#define GWS_IN_USE GWS_FREQ
```

Then recompile MySQL. There is no need to rebuild the indexes in this case.

Note By making this change, you severely decrease MySQL's ability to provide adequate relevance values for the `MATCH()` function. If you really need to search for such common words, it would be better to search using `IN BOOLEAN MODE` instead,which does not observe the 50% threshold.

> Modifying Boolean Full-Text Search Operators

To change the operators used for boolean full-text searches on `MyISAM` tables, set the`ft_boolean_syntax` system variable. (`InnoDB` does not have an equivalent setting.) This variable can be changed while the server is running, but you must have privileges sufficient to set global system variables (see Section 5.1.8.1, “System Variable Privileges”). No rebuilding of indexes is necessary in this case.

> Character Set Modifications

You can change the set of characters that are considered word characters in several ways, as described in the following list. After making the modification, rebuild the indexes for each table that contains any`FULLTEXT` indexes. Suppose that you want to treat the hyphen character ('-') as a word character. Use one of these methods:

- Modify the MySQL source: In `storage/innobase/handler/ha_innodb.cc` (for `InnoDB`), or in

```
storage/myisam/ftdefs.h (for MyISAM), see the true_word_char() and misc_word_char()
```

macros. Add `'-'` to one of those macros and recompile MySQL.

- Modify a character set file: This requires no recompilation. The `true_word_char()` macro uses

a “character type” table to distinguish letters and numbers from other characters. . You can edit the contents of the `<ctype><map>` array in one of the character set XML files to specify that `'-'` is a “letter.” Then use the given character set for your `FULLTEXT` indexes. For information about the`<ctype><map>` array format, see Section 10.13.1, “Character Definition Arrays”.

- Add a new collation for the character set used by the indexed columns, and alter the columns to use

that collation. For general information about adding collations, see Section 10.14, “Adding a Collation to a Character Set”. For an example specific to full-text indexing, see Section 12.10.7, “Adding a User-Defined Collation for Full-Text Indexing”.

> Rebuilding InnoDB Full-Text Indexes

For the changes to take effect, `FULLTEXT` indexes must be rebuilt after modifying any of the following full-text index variables: `innodb_ft_min_token_size`; `innodb_ft_max_token_size`;

```
innodb_ft_server_stopword_table; innodb_ft_user_stopword_table;
innodb_ft_enable_stopword. Modifying innodb_ft_min_token_size or
```

`innodb_ft_max_token_size` requires restarting the server.

Fine-Tuning MySQL Full-Text Search To rebuild `FULLTEXT` indexes for an `InnoDB` table, use `ALTER TABLE` with the `DROP INDEX` and `ADD``INDEX` options to drop and re-create each index.

> Optimizing InnoDB Full-Text Indexes

Running `OPTIMIZE TABLE` on a table with a full-text index rebuilds the full-text index, removing deleted Document IDs and consolidating multiple entries for the same word, where possible.

To optimize a full-text index, enable `innodb_optimize_fulltext_only` and run `OPTIMIZE TABLE`.

```
mysql> set GLOBAL innodb_optimize_fulltext_only=ON;
Query OK, 0 rows affected (0.01 sec)
mysql> OPTIMIZE TABLE opening_lines;
+--------------------+----------+----------+----------+
| Table              | Op       | Msg_type | Msg_text |
+--------------------+----------+----------+----------+
| test.opening_lines | optimize | status   | OK       |
+--------------------+----------+----------+----------+
1 row in set (0.01 sec)
```

To avoid lengthy rebuild times for full-text indexes on large tables, you can use the`innodb_ft_num_word_optimize` option to perform the optimization in stages. The`innodb_ft_num_word_optimize` option defines the number of words that are optimized each time`OPTIMIZE TABLE` is run. The default setting is 2000, which means that 2000 words are optimized each time `OPTIMIZE TABLE` is run. Subsequent `OPTIMIZE TABLE` operations continue from where the preceding `OPTIMIZE TABLE` operation ended.

> Rebuilding MyISAM Full-Text Indexes

If you modify full-text variables that affect indexing (`ft_min_word_len`, `ft_max_word_len`, or`ft_stopword_file`), or if you change the stopword file itself, you must rebuild your `FULLTEXT` indexes after making the changes and restarting the server.

To rebuild the `FULLTEXT` indexes for a `MyISAM` table, it is sufficient to do a `QUICK` repair operation:

```
mysql> REPAIR TABLE tbl_name QUICK;
```

Alternatively, use `ALTER TABLE` as just described. In some cases, this may be faster than a repair operation.

Each table that contains any `FULLTEXT` index must be repaired as just shown. Otherwise, queries for the table may yield incorrect results, and modifications to the table cause the server to see the table as corrupt and in need of repair.

If you use `myisamchk` to perform an operation that modifies `MyISAM` table indexes (such as repair or analyze), the `FULLTEXT` indexes are rebuilt using the default full-text parameter values for minimum word length, maximum word length, and stopword file unless you specify otherwise. This can result in queries failing.

The problem occurs because these parameters are known only by the server. They are not stored in`MyISAM` index files. To avoid the problem if you have modified the minimum or maximum word length or stopword file values used by the server, specify the same `ft_min_word_len`, `ft_max_word_len`, and`ft_stopword_file` values for `myisamchk` that you use for `mysqld`. For example, if you have set the minimum word length to 3, you can repair a table with `myisamchk` like this:

```
myisamchk --recover --ft_min_word_len=3 tbl_name.MYI
```

To ensure that `myisamchk` and the server use the same values for full-text parameters, place each one in both the `[mysqld]` and `[myisamchk]` sections of an option file:Adding a User-Defined Collation for Full-Text Indexing

```
[mysqld]
ft_min_word_len=3
[myisamchk]
ft_min_word_len=3
```

An alternative to using `myisamchk` for `MyISAM` table index modification is to use the `REPAIR TABLE`,`ANALYZE TABLE`, `OPTIMIZE TABLE`, or `ALTER TABLE` statements. These statements are performed by the server, which knows the proper full-text parameter values to use.

### 12.10.7 Adding a User-Defined Collation for Full-Text Indexing

This section describes how to add a user-defined collation for full-text searches using the built-in full-text parser. The sample collation is like `latin1_swedish_ci` but treats the `'-'` character as a letter rather than as a punctuation character so that it can be indexed as a word character. General information about adding collations is given in Section 10.14, “Adding a Collation to a Character Set”; it is assumed that you have read it and are familiar with the files involved.

To add a collation for full-text indexing, use the following procedure. The instructions here add a collation for a simple character set, which as discussed in Section 10.14, “Adding a Collation to a Character Set”,can be created using a configuration file that describes the character set properties. For a complex character set such as Unicode, create collations using C source files that describe the character set properties.

1. Add a collation to the `Index.xml` file. The permitted range of IDs for user-defined collations is given

in Section 10.14.2, “Choosing a Collation ID”. The ID must be unused, so choose a value different from 1025 if that ID is already taken on your system.

```
<charset name="latin1">
...
<collation name="latin1_fulltext_ci" id="1025"/>
</charset>
```

2. Declare the sort order for the collation in the `latin1.xml` file. In this case, the order can be copied

```
from latin1_swedish_ci:
<collation name="latin1_fulltext_ci">
<map>
00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F
20 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E 2F
30 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E 3F
40 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F
50 51 52 53 54 55 56 57 58 59 5A 5B 5C 5D 5E 5F
60 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F
50 51 52 53 54 55 56 57 58 59 5A 7B 7C 7D 7E 7F
80 81 82 83 84 85 86 87 88 89 8A 8B 8C 8D 8E 8F
90 91 92 93 94 95 96 97 98 99 9A 9B 9C 9D 9E 9F
A0 A1 A2 A3 A4 A5 A6 A7 A8 A9 AA AB AC AD AE AF
B0 B1 B2 B3 B4 B5 B6 B7 B8 B9 BA BB BC BD BE BF
41 41 41 41 5C 5B 5C 43 45 45 45 45 49 49 49 49
44 4E 4F 4F 4F 4F 5D D7 D8 55 55 55 59 59 DE DF
41 41 41 41 5C 5B 5C 43 45 45 45 45 49 49 49 49
44 4E 4F 4F 4F 4F 5D F7 D8 55 55 55 59 59 DE FF
</map>
</collation>
```

3. Modify the `ctype` array in `latin1.xml`. Change the value corresponding to 0x2D (which is the code

for the `'-'` character) from 10 (punctuation) to 01 (uppercase letter). In the following array, this is the element in the fourth row down, third value from the end.

```
<ctype>
```

Cast Functions and Operators

```
<map>
00
20 20 20 20 20 20 20 20 20 28 28 28 28 28 20 20
20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20
48 10 10 10 10 10 10 10 10 10 10 10 10 01 10 10
84 84 84 84 84 84 84 84 84 84 10 10 10 10 10 10
10 81 81 81 81 81 81 01 01 01 01 01 01 01 01 01
01 01 01 01 01 01 01 01 01 01 01 10 10 10 10 10
10 82 82 82 82 82 82 02 02 02 02 02 02 02 02 02
02 02 02 02 02 02 02 02 02 02 02 10 10 10 10 20
10 00 10 02 10 10 10 10 10 10 01 10 01 00 01 00
00 10 10 10 10 10 10 10 10 10 02 10 02 00 02 01
48 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
01 01 01 01 01 01 01 10 01 01 01 01 01 01 01 02
02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02
02 02 02 02 02 02 02 10 02 02 02 02 02 02 02 02
</map>
</ctype>
```

4. Restart the server.
5. To employ the new collation, include it in the definition of columns that are to use it:

```
mysql> DROP TABLE IF EXISTS t1;
Query OK, 0 rows affected (0.13 sec)
mysql> CREATE TABLE t1 (
a TEXT CHARACTER SET latin1 COLLATE latin1_fulltext_ci,
FULLTEXT INDEX(a)
) ENGINE=InnoDB;
Query OK, 0 rows affected (0.47 sec)
```

6. Test the collation to verify that hyphen is considered as a word character:

```
mysql> INSERT INTO t1 VALUEs ('----'),('....'),('abcd');
Query OK, 3 rows affected (0.22 sec)
Records: 3  Duplicates: 0  Warnings: 0
mysql> SELECT * FROM t1 WHERE MATCH a AGAINST ('----' IN BOOLEAN MODE);
+------+
| a    |
+------+
| ---- |
+------+
1 row in set (0.00 sec)
```

## 12.11 Cast Functions and Operators

Table 12.15 Cast Functions and Operators Name Description`BINARY` Cast a string to a binary string`CAST()` Cast a value as a certain type`CONVERT()` Cast a value as a certain type Cast functions and operators enable conversion of values from one data type to another.

- Cast Function and Operator Descriptions
- Character Set Conversions

Cast Function and Operator Descriptions

- Character Set Conversions for String Comparisons
- Other Uses for Cast Operations

> Cast Function and Operator Descriptions

```
- BINARY expr
```

The `BINARY` operator converts the expression to a binary string (a string that has the `binary` character set and `binary` collation). A common use for `BINARY` is to force a character string comparison to be done byte by byte using numeric byte values rather than character by character. The `BINARY` operator also causes trailing spaces in comparisons to be significant. For information about the differences between the `binary` collation of the `binary` character set and the `_bin` collations of nonbinary character sets, see Section 10.8.5, “The binary Collation Compared to _bin Collations”.

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

If a value is a string literal, it can be designated as a binary string without converting it by using the`_binary` character set introducer:

```
mysql> SELECT 'a' = 'A';
-> 1
mysql> SELECT _binary 'a' = 'A';
-> 0
```

For information about introducers, see Section 10.3.8, “Character Set Introducers”.

The `BINARY` operator in expressions differs in effect from the `BINARY` attribute in character column definitions. For a character column defined with the `BINARY` attribute, MySQL assigns the table default character set and the binary (`_bin`) collation of that character set. Every nonbinary character set has a`_bin` collation. For example, if the table default character set is `utf8`, these two column definitions are equivalent:

```
CHAR(10) BINARY
CHAR(10) CHARACTER SET utf8 COLLATE utf8_bin
```

The use of `CHARACTER SET binary` in the definition of a `CHAR`, `VARCHAR`, or `TEXT` column causes the column to be treated as the corresponding binary string data type. For example, the following pairs of definitions are equivalent:

```
CHAR(10) CHARACTER SET binary
BINARY(10)
VARCHAR(10) CHARACTER SET binary
VARBINARY(10)
```

Cast Function and Operator Descriptions

```
TEXT CHARACTER SET binary
BLOB
```

If `BINARY` is invoked from within the `mysql` client, binary strings display using hexadecimal notation,depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

Cast Function and Operator Descriptions

```
- CAST(expr AS type)
```

`CAST(expr AS type` takes an expression of any type and produces a result value of the specified type. This operation may also be expressed as `CONVERT(expr, type)`, which is equivalent.

These `type` values are permitted:

```
- BINARY[(N)]
```

Produces a string with the `BINARY` data type. If the optional length N is given, `BINARY(N)` causes the cast to use no more than N bytes of the argument. Values shorter than N bytes are padded with `0x00`bytes to a length of N.

For a description of how casting to `BINARY` affects comparisons, see Section 11.3.3, “The BINARY and VARBINARY Types”.

```
- CHAR[(N)] [charset_info]
```

Produces a string with the `CHAR` data type. If the optional length N is given, `CHAR(N)` causes the cast to use no more than N characters of the argument. No padding occurs for values shorter than N characters.

With no `charset_info` clause, `CHAR` produces a string with the default character set. To specify the character set explicitly, these `charset_info` values are permitted:

- `CHARACTER SET charset_name`: Produces a string with the given character set.
- `ASCII`: Shorthand for `CHARACTER SET latin1`.
- `UNICODE`: Shorthand for `CHARACTER SET ucs2`.

In all cases, the string has the character set default collation.

```
- DATE
```

Produces a `DATE` value.

```
- DATETIME
```

Produces a `DATETIME` value.

```
- DECIMAL[(M[,D])]
```

Produces a `DECIMAL` value. If the optional M and D values are given, they specify the maximum number of digits (the precision) and the number of digits following the decimal point (the scale).

```
- NCHAR[(N)]
```

Like `CHAR`, but produces a string with the national character set. See Section 10.3.7, “The National Character Set”.

Unlike `CHAR`, `NCHAR` does not permit trailing character set information to be specified.

```
- SIGNED [INTEGER]
```

Produces a signed integer value.

```
- TIME
```

Character Set Conversions Produces a `TIME` value.

```
- UNSIGNED [INTEGER]
```

Produces an unsigned integer value.

```
- CONVERT(expr USING transcoding_name)
CONVERT(expr,type)
```

`CONVERT(expr USING transcoding_name)` is standard SQL syntax. The non-`USING` form of`CONVERT()` is ODBC syntax.

`CONVERT(expr USING transcoding_name)` converts data between different character sets. In MySQL, transcoding names are the same as the corresponding character set names. For example, this statement converts the string `'abc'` in the default character set to the corresponding string in the `utf8`character set:

```
SELECT CONVERT('abc' USING utf8);
```

`CONVERT(expr, type)` syntax (without `USING`) takes an expression and a `type` value specifying a result type, and produces a result value of the specified type. This operation may also be expressed as`CAST(expr AS type)`, which is equivalent. For more information, see the description of `CAST()`.

> Character Set Conversions

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

To convert strings between character sets, you can also use `CONVERT(expr, type)` syntax (without`USING`), or `CAST(expr AS type)`, which is equivalent:

```
CONVERT(string, CHAR[(N)] CHARACTER SET charset_name)
CAST(string AS CHAR[(N)] CHARACTER SET charset_name)
```

Examples:

```
SELECT CONVERT('test', CHAR CHARACTER SET utf8);
SELECT CAST('test' AS CHAR CHARACTER SET utf8);
```

If you specify `CHARACTER SET charset_name` as just shown, the character set and collation of the result are `charset_name` and the default collation of `charset_name`. If you omit`CHARACTER SET charset_name`, the character set and collation of the result are defined by the`character_set_connection` and `collation_connection` system variables that determine the default connection character set and collation (see Section 10.4, “Connection Character Sets and Collations”).

A `COLLATE` clause is not permitted within a `CONVERT()` or `CAST()` call, but you can apply it to the function result. For example, these are legal:Character Set Conversions for String Comparisons

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

For string literals, another way to specify the character set is to use a character set introducer. `_latin1`and `_latin2` in the preceding example are instances of introducers. Unlike conversion functions such as `CAST()`, or `CONVERT()`, which convert a string from one character set to another, an introducer designates a string literal as having a particular character set, with no conversion involved. For more information, see Section 10.3.8, “Character Set Introducers”.

> Character Set Conversions for String Comparisons

Normally, you cannot compare a `BLOB` value or other binary string in case-insensitive fashion because binary strings use the `binary` character set, which has no collation with the concept of lettercase. To perform a case-insensitive comparison, first use the `CONVERT()` or `CAST()` function to convert the value to a nonbinary string. Comparisons of the resulting string use its collation. For example, if the conversion result collation is not case-sensitive, a `LIKE` operation is not case-sensitive. That is true for the following operation because the default `latin1` collation (`latin1_swedish_ci`) is not case-sensitive:

```
SELECT 'A' LIKE CONVERT(blob_col USING latin1)
FROM tbl_name;
```

To specify a particular collation for the converted string, use a `COLLATE` clause following the `CONVERT()`call:

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

Character set conversion is also useful preceding lettercase conversion of binary strings. `LOWER()` and`UPPER()` are ineffective when applied directly to binary strings because the concept of lettercase does not apply. To perform lettercase conversion of a binary string, first convert it to a nonbinary string using a character set appropriate for the data stored in the string:Other Uses for Cast Operations

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

> Other Uses for Cast Operations

The cast functions are useful for creating a column with a specific type in a `CREATE TABLE ... SELECT`statement:

```
mysql> CREATE TABLE new_table SELECT CAST('2000-01-01' AS DATE) AS c1;
mysql> SHOW CREATE TABLE new_table\G
*************************** 1. row ***************************
Table: new_table
Create Table: CREATE TABLE `new_table` (
`c1` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

The cast functions are useful for sorting `ENUM` columns in lexical order. Normally, sorting of `ENUM` columns occurs using the internal numeric values. Casting the values to `CHAR` results in a lexical sort:

```
SELECT enum_col FROM tbl_name ORDER BY CAST(enum_col AS CHAR);
```

`CAST()` also changes the result if you use it as part of a more complex expression such as

```
CONCAT('Date: ',CAST(NOW() AS DATE)).
```

For temporal values, there is little need to use `CAST()` to extract data in different formats. Instead, use a function such as `EXTRACT()`, `DATE_FORMAT()`, or `TIME_FORMAT()`. See Section 12.7, “Date and Time Functions”.

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

For information about implicit conversion of numbers to strings, see Section 12.3, “Type Conversion in Expression Evaluation”.

MySQL supports arithmetic with both signed and unsigned 64-bit values. For numeric operators (such as + or -) where one of the operands is an unsigned integer, the result is unsigned by default (see XML Functions Section 12.6.1, “Arithmetic Operators”). To override this, use the `SIGNED` or `UNSIGNED` cast operator to cast a value to a signed or unsigned 64-bit integer, respectively.

```
mysql> SELECT 1 - 2;
-> -1
mysql> SELECT CAST(1 - 2 AS UNSIGNED);
-> 18446744073709551615
mysql> SELECT CAST(CAST(1 - 2 AS UNSIGNED) AS SIGNED);
-> -1
```

If either operand is a floating-point value, the result is a floating-point value and is not affected by the preceding rule. (In this context, `DECIMAL` column values are regarded as floating-point values.)

```
mysql> SELECT CAST(1 AS UNSIGNED) - 2.0;
-> -1.0
```

The SQL mode affects the result of conversion operations (see Section 5.1.10, “Server SQL Modes”).

Examples:

- For conversion of a “zero” date string to a date, `CONVERT()` and `CAST()` return `NULL` and produce a

warning when the `NO_ZERO_DATE` SQL mode is enabled.

- For integer subtraction, if the `NO_UNSIGNED_SUBTRACTION` SQL mode is enabled, the subtraction

result is signed even if any operand is unsigned.

## 12.12 XML Functions

Table 12.16 XML Functions Name Description`ExtractValue()` Extract a value from an XML string using XPath notation`UpdateXML()` Return replaced XML fragment This section discusses XML and related functionality in MySQL.

Note It is possible to obtain XML-formatted output from MySQL in the `mysql` and`mysqldump` clients by invoking them with the `--xml` option. See Section 4.5.1,“mysql — The MySQL Command-Line Client”, and Section 4.5.4, “mysqldump — A Database Backup Program”.

Two functions providing basic XPath 1.0 (XML Path Language, version 1.0) capabilities are available.

Some basic information about XPath syntax and usage is provided later in this section; however, an in-depth discussion of these topics is beyond the scope of this manual, and you should refer to the XML Path Language (XPath) 1.0 standard for definitive information. A useful resource for those new to XPath or who desire a refresher in the basics is the Zvon.org XPath Tutorial, which is available in several languages.

Note These functions remain under development. We continue to improve these and other aspects of XML and XPath functionality in MySQL 5.6 and onwards. You may discuss these, ask questions about them, and obtain help from other users with them in the MySQL XML User Forum.

XML Functions XPath expressions used with these functions support user variables and local stored program variables.

User variables are weakly checked; variables local to stored programs are strongly checked (see also Bug#26518):

- User variables (weak checking). Variables using the syntax `$@variable_name` (that is, user

variables) are not checked. No warnings or errors are issued by the server if a variable has the wrong type or has previously not been assigned a value. This also means the user is fully responsible for any typographical errors, since no warnings are given if (for example) `$@myvairable` is used where`$@myvariable` was intended.

Example:

```
mysql> SET @xml = '<a><b>X</b><b>Y</b></a>';
Query OK, 0 rows affected (0.00 sec)
mysql> SET @i =1, @j = 2;
Query OK, 0 rows affected (0.00 sec)
mysql> SELECT @i, ExtractValue(@xml, '//b[$@i]');
+------+--------------------------------+
| @i   | ExtractValue(@xml, '//b[$@i]') |
+------+--------------------------------+
|    1 | X                              |
+------+--------------------------------+
1 row in set (0.00 sec)
mysql> SELECT @j, ExtractValue(@xml, '//b[$@j]');
+------+--------------------------------+
| @j   | ExtractValue(@xml, '//b[$@j]') |
+------+--------------------------------+
|    2 | Y                              |
+------+--------------------------------+
1 row in set (0.00 sec)
mysql> SELECT @k, ExtractValue(@xml, '//b[$@k]');
+------+--------------------------------+
| @k   | ExtractValue(@xml, '//b[$@k]') |
+------+--------------------------------+
| NULL |                                |
+------+--------------------------------+
1 row in set (0.00 sec)
```

- Variables in stored programs (strong checking). Variables using the syntax `$variable_name`

can be declared and used with these functions when they are called inside stored programs. Such variables are local to the stored program in which they are defined, and are strongly checked for type and value.

Example:

```
mysql> DELIMITER |
mysql> CREATE PROCEDURE myproc ()
-> BEGIN
->   DECLARE i INT DEFAULT 1;
->   DECLARE xml VARCHAR(25) DEFAULT '<a>X</a><a>Y</a><a>Z</a>';
->
->   WHILE i < 4 DO
->     SELECT xml, i, ExtractValue(xml, '//a[$i]');
->     SET i = i+1;
->   END WHILE;
-> END |
Query OK, 0 rows affected (0.01 sec)
mysql> DELIMITER ;
```

XML Functions

```
mysql> CALL myproc();
+--------------------------+---+------------------------------+
| xml                      | i | ExtractValue(xml, '//a[$i]') |
+--------------------------+---+------------------------------+
| <a>X</a><a>Y</a><a>Z</a> | 1 | X                            |
+--------------------------+---+------------------------------+
1 row in set (0.00 sec)
+--------------------------+---+------------------------------+
| xml                      | i | ExtractValue(xml, '//a[$i]') |
+--------------------------+---+------------------------------+
| <a>X</a><a>Y</a><a>Z</a> | 2 | Y                            |
+--------------------------+---+------------------------------+
1 row in set (0.01 sec)
+--------------------------+---+------------------------------+
| xml                      | i | ExtractValue(xml, '//a[$i]') |
+--------------------------+---+------------------------------+
| <a>X</a><a>Y</a><a>Z</a> | 3 | Z                            |
+--------------------------+---+------------------------------+
1 row in set (0.01 sec)
```

Parameters. Variables used in XPath expressions inside stored routines that are passed in as parameters are also subject to strong checking.

Expressions containing user variables or variables local to stored programs must otherwise (except for notation) conform to the rules for XPath expressions containing variables as given in the XPath 1.0 specification.

Note A user variable used to store an XPath expression is treated as an empty string.

Because of this, it is not possible to store an XPath expression as a user variable.

(Bug #32911)

```
- ExtractValue(xml_frag, xpath_expr)
```

`ExtractValue()` takes two string arguments, a fragment of XML markup `xml_frag` and an XPath expression `xpath_expr` (also known as a locator); it returns the text (`CDATA`) of the first text node which is a child of the element or elements matched by the XPath expression.

Using this function is the equivalent of performing a match using the `xpath_expr` after appending`/text()`. In other words, `ExtractValue('<a><b>Sakila</b></a>', '/a/b')` and`ExtractValue('<a><b>Sakila</b></a>', '/a/b/text()')` produce the same result.

If multiple matches are found, the content of the first child text node of each matching element is returned (in the order matched) as a single, space-delimited string.

If no matching text node is found for the expression (including the implicit `/text()`)—for whatever reason, as long as `xpath_expr` is valid, and `xml_frag` consists of elements which are properly nested and closed—an empty string is returned. No distinction is made between a match on an empty element and no match at all. This is by design.

If you need to determine whether no matching element was found in `xml_frag` or such an element was found but contained no child text nodes, you should test the result of an expression that uses the XPath`count()` function. For example, both of these statements return an empty string, as shown here:

```
mysql> SELECT ExtractValue('<a><b/></a>', '/a/b');
+-------------------------------------+
| ExtractValue('<a><b/></a>', '/a/b') |
```

XML Functions

```
+-------------------------------------+
|                                     |
+-------------------------------------+
1 row in set (0.00 sec)
mysql> SELECT ExtractValue('<a><c/></a>', '/a/b');
+-------------------------------------+
| ExtractValue('<a><c/></a>', '/a/b') |
+-------------------------------------+
|                                     |
+-------------------------------------+
1 row in set (0.00 sec)
```

Note In MySQL 5.6.28 and MySQL 5.6.29, when `ExtractValue()` failed to find a match for the supplied expression, it returned `NULL`. This issue was resolved in MySQL 5.6.30. (Bug #22552615)However, you can determine whether there was actually a matching element using the following:

```
mysql> SELECT ExtractValue('<a><b/></a>', 'count(/a/b)');
+-------------------------------------+
| ExtractValue('<a><b/></a>', 'count(/a/b)') |
+-------------------------------------+
| 1                                   |
+-------------------------------------+
1 row in set (0.00 sec)
mysql> SELECT ExtractValue('<a><c/></a>', 'count(/a/b)');
+-------------------------------------+
| ExtractValue('<a><c/></a>', 'count(/a/b)') |
+-------------------------------------+
| 0                                   |
+-------------------------------------+
1 row in set (0.01 sec)
```

Important`ExtractValue()` returns only `CDATA`, and does not return any tags that might be contained within a matching tag, nor any of their content (see the result returned as `val1` in the following example).

```
mysql> SELECT
->   ExtractValue('<a>ccc<b>ddd</b></a>', '/a') AS val1,
->   ExtractValue('<a>ccc<b>ddd</b></a>', '/a/b') AS val2,
->   ExtractValue('<a>ccc<b>ddd</b></a>', '//b') AS val3,
->   ExtractValue('<a>ccc<b>ddd</b></a>', '/b') AS val4,
->   ExtractValue('<a>ccc<b>ddd</b><b>eee</b></a>', '//b') AS val5;
+------+------+------+------+---------+
| val1 | val2 | val3 | val4 | val5    |
+------+------+------+------+---------+
| ccc  | ddd  | ddd  |      | ddd eee |
+------+------+------+------+---------+
```

This function uses the current SQL collation for making comparisons with `contains()`, performing the same collation aggregation as other string functions (such as `CONCAT()`), in taking into account the XML Functions collation coercibility of their arguments; see Section 10.8.4, “Collation Coercibility in Expressions”, for an explanation of the rules governing this behavior.

(Previously, binary—that is, case-sensitive—comparison was always used.)`NULL` is returned if `xml_frag` contains elements which are not properly nested or closed, and a warning is generated, as shown in this example:

```
mysql> SELECT ExtractValue('<a>c</a><b', '//a');
+-----------------------------------+
| ExtractValue('<a>c</a><b', '//a') |
+-----------------------------------+
| NULL                              |
+-----------------------------------+
1 row in set, 1 warning (0.00 sec)
mysql> SHOW WARNINGS\G
*************************** 1. row ***************************
Level: Warning
Code: 1525
Message: Incorrect XML value: 'parse error at line 1 pos 11:
END-OF-INPUT unexpected ('>' wanted)'
1 row in set (0.00 sec)
mysql> SELECT ExtractValue('<a>c</a><b/>', '//a');
+-------------------------------------+
| ExtractValue('<a>c</a><b/>', '//a') |
+-------------------------------------+
| c                                   |
+-------------------------------------+
1 row in set (0.00 sec)
- UpdateXML(xml_target, xpath_expr, new_xml)
```

This function replaces a single portion of a given fragment of XML markup `xml_target` with a new XML fragment `new_xml`, and then returns the changed XML. The portion of `xml_target` that is replaced matches an XPath expression `xpath_expr` supplied by the user.

If no expression matching `xpath_expr` is found, or if multiple matches are found, the function returns the original `xml_target` XML fragment. All three arguments should be strings.

```
mysql> SELECT
->   UpdateXML('<a><b>ccc</b><d></d></a>', '/a', '<e>fff</e>') AS val1,
->   UpdateXML('<a><b>ccc</b><d></d></a>', '/b', '<e>fff</e>') AS val2,
->   UpdateXML('<a><b>ccc</b><d></d></a>', '//b', '<e>fff</e>') AS val3,
->   UpdateXML('<a><b>ccc</b><d></d></a>', '/a/d', '<e>fff</e>') AS val4,
->   UpdateXML('<a><d></d><b>ccc</b><d></d></a>', '/a/d', '<e>fff</e>') AS val5
-> \G
*************************** 1. row ***************************
val1: <e>fff</e>
val2: <a><b>ccc</b><d></d></a>
val3: <a><e>fff</e><d></d></a>
val4: <a><b>ccc</b><e>fff</e></a>
val5: <a><d></d><b>ccc</b><d></d></a>
```

Note A discussion in depth of XPath syntax and usage are beyond the scope of this manual. Please see the XML Path Language (XPath) 1.0 specification for definitive information. A useful resource for those new to XPath or who are wishing a refresher in the basics is the Zvon.org XPath Tutorial, which is available in several languages.

XML Functions Descriptions and examples of some basic XPath expressions follow:

```
- /tag
```

Matches `<tag/>` if and only if `<tag/>` is the root element.

Example: `/a` has a match in `<a><b/></a>` because it matches the outermost (root) tag. It does not match the inner a element in `<b><a/></b>` because in this instance it is the child of another element.

```
- /tag1/tag2
```

Matches `<tag2/>` if and only if it is a child of `<tag1/>`, and `<tag1/>` is the root element.

Example: `/a/b` matches the b element in the XML fragment `<a><b/></a>` because it is a child of the root element a. It does not have a match in `<b><a/></b>` because in this case, b is the root element(and hence the child of no other element). Nor does the XPath expression have a match in `<a><c><b/``></c></a>`; here, b is a descendant of a, but not actually a child of a.

This construct is extendable to three or more elements. For example, the XPath expression `/a/b/c`matches the c element in the fragment `<a><b><c/></b></a>`.

```
- //tag
```

Matches any instance of `<tag>`.

Example: `//a` matches the a element in any of the following: `<a><b><c/></b></a>`; `<c><a><b/></`

```
a></b>; <c><b><a/></b></c>.
```

`//` can be combined with /. For example, `//a/b` matches the b element in either of the fragments

```
<a><b/></a> or <c><a><b/></a></c>.
```

Note`//tag` is the equivalent of `/descendant-or-self::*/tag`. A common error is to confuse this with `/descendant-or-self::tag`, although the latter expression can actually lead to very different results, as can be seen here:

```
mysql> SET @xml = '<a><b><c>w</c><b>x</b><d>y</d>z</b></a>';
Query OK, 0 rows affected (0.00 sec)
mysql> SELECT @xml;
+-----------------------------------------+
| @xml                                    |
+-----------------------------------------+
| <a><b><c>w</c><b>x</b><d>y</d>z</b></a> |
+-----------------------------------------+
1 row in set (0.00 sec)
mysql> SELECT ExtractValue(@xml, '//b[1]');
+------------------------------+
| ExtractValue(@xml, '//b[1]') |
+------------------------------+
| x z                          |
+------------------------------+
1 row in set (0.00 sec)
mysql> SELECT ExtractValue(@xml, '//b[2]');
+------------------------------+
| ExtractValue(@xml, '//b[2]') |
+------------------------------+
|                              |
```

XML Functions

```
+------------------------------+
1 row in set (0.01 sec)
mysql> SELECT ExtractValue(@xml, '/descendant-or-self::*/b[1]');
+---------------------------------------------------+
| ExtractValue(@xml, '/descendant-or-self::*/b[1]') |
+---------------------------------------------------+
| x z                                               |
+---------------------------------------------------+
1 row in set (0.06 sec)
mysql> SELECT ExtractValue(@xml, '/descendant-or-self::*/b[2]');
+---------------------------------------------------+
| ExtractValue(@xml, '/descendant-or-self::*/b[2]') |
+---------------------------------------------------+
|                                                   |
+---------------------------------------------------+
1 row in set (0.00 sec)
mysql> SELECT ExtractValue(@xml, '/descendant-or-self::b[1]');
+-------------------------------------------------+
| ExtractValue(@xml, '/descendant-or-self::b[1]') |
+-------------------------------------------------+
| z                                               |
+-------------------------------------------------+
1 row in set (0.00 sec)
mysql> SELECT ExtractValue(@xml, '/descendant-or-self::b[2]');
+-------------------------------------------------+
| ExtractValue(@xml, '/descendant-or-self::b[2]') |
+-------------------------------------------------+
| x                                               |
+-------------------------------------------------+
1 row in set (0.00 sec)
```

- The * operator acts as a “wildcard” that matches any element. For example, the expression `/*/b`

matches the b element in either of the XML fragments `<a><b/></a>` or `<c><b/></c>`. However, the expression does not produce a match in the fragment `<b><a/></b>` because b must be a child of some other element. The wildcard may be used in any position: The expression `/*/b/*` matches any child of a b element that is itself not the root element.

- You can match any of several locators using the | (`UNION`) operator. For example, the expression `//`

`b|//c` matches all b and c elements in the XML target.

- It is also possible to match an element based on the value of one or more of its attributes. This done

using the syntax `tag[@attribute="value"]`. For example, the expression `//b[@id="idB"]`matches the second b element in the fragment `<a><b id="idA"/><c/><b id="idB"/></``a>`. To match against any element having `attribute="value"`, use the XPath expression `//`

```
*[attribute="value"].
```

To filter multiple attribute values, simply use multiple attribute-comparison clauses in succession. For example, the expression `//b[@c="x"][@d="y"]` matches the element `<b c="x" d="y"/>` occurring anywhere in a given XML fragment.

To find elements for which the same attribute matches any of several values, you can use multiple locators joined by the | operator. For example, to match all b elements whose c attributes have either of XML Functions the values 23 or 17, use the expression `//b[@c="23"]|//b[@c="17"]`. You can also use the logical`or` operator for this purpose: `//b[@c="23" or @c="17"]`.

Note The difference between `or` and | is that `or` joins conditions, while | joins result sets.

XPath Limitations. The XPath syntax supported by these functions is currently subject to the following limitations:

- Nodeset-to-nodeset comparison (such as `'/a/b[@c=@d]'`) is not supported.
- All of the standard XPath comparison operators are supported. (Bug #22823)
- Relative locator expressions are resolved in the context of the root node. For example, consider the

following query and result:

```
mysql> SELECT ExtractValue(
->   '<a><b c="1">X</b><b c="2">Y</b></a>',
->    'a/b'
-> ) AS result;
+--------+
| result |
+--------+
| X Y    |
+--------+
1 row in set (0.03 sec)
```

In this case, the locator `a/b` resolves to `/a/b`.

Relative locators are also supported within predicates. In the following example, `d[../@c="1"]` is resolved as `/a/b[@c="1"]/d`:

```
mysql> SELECT ExtractValue(
->      '<a>
->        <b c="1"><d>X</d></b>
->        <b c="2"><d>X</d></b>
->      </a>',
->      'a/b/d[../@c="1"]')
-> AS result;
+--------+
| result |
+--------+
| X      |
+--------+
1 row in set (0.00 sec)
```

- Locators prefixed with expressions that evaluate as scalar values—including variable references, literals,

numbers, and scalar function calls—are not permitted, and their use results in an error.

- The `::` operator is not supported in combination with node types such as the following:

```
- axis::comment()
- axis::text()
- axis::processing-instructions()
- axis::node()
```

However, name tests (such as `axis::name` and `axis::*`) are supported, as shown in these examples:XML Functions

```
mysql> SELECT ExtractValue('<a><b>x</b><c>y</c></a>','/a/child::b');
+-------------------------------------------------------+
| ExtractValue('<a><b>x</b><c>y</c></a>','/a/child::b') |
+-------------------------------------------------------+
| x                                                     |
+-------------------------------------------------------+
1 row in set (0.02 sec)
mysql> SELECT ExtractValue('<a><b>x</b><c>y</c></a>','/a/child::*');
+-------------------------------------------------------+
| ExtractValue('<a><b>x</b><c>y</c></a>','/a/child::*') |
+-------------------------------------------------------+
| x y                                                   |
+-------------------------------------------------------+
1 row in set (0.01 sec)
```

- “Up-and-down” navigation is not supported in cases where the path would lead “above” the root element.

That is, you cannot use expressions which match on descendants of ancestors of a given element,where one or more of the ancestors of the current element is also an ancestor of the root element (see Bug #16321).

- The following XPath functions are not supported, or have known issues as indicated:

```
- id()
- lang()
- local-name()
- name()
- namespace-uri()
- normalize-space()
- starts-with()
- string()
- substring-after()
- substring-before()
- translate()
```

- The following axes are not supported:

```
- following-sibling
- following
- preceding-sibling
- preceding
```

XPath expressions passed as arguments to `ExtractValue()` and `UpdateXML()` may contain the colon character (:) in element selectors, which enables their use with markup employing XML namespaces notation. For example:

```
mysql> SET @xml = '<a>111<b:c>222<d>333</d><e:f>444</e:f></b:c></a>';
```

XML Functions

```
Query OK, 0 rows affected (0.00 sec)
mysql> SELECT ExtractValue(@xml, '//e:f');
+-----------------------------+
| ExtractValue(@xml, '//e:f') |
+-----------------------------+
| 444                         |
+-----------------------------+
1 row in set (0.00 sec)
mysql> SELECT UpdateXML(@xml, '//b:c', '<g:h>555</g:h>');
+--------------------------------------------+
| UpdateXML(@xml, '//b:c', '<g:h>555</g:h>') |
+--------------------------------------------+
| <a>111<g:h>555</g:h></a>                   |
+--------------------------------------------+
1 row in set (0.00 sec)
```

This is similar in some respects to what is permitted by Apache Xalan and some other parsers, and is much simpler than requiring namespace declarations or the use of the `namespace-uri()` and `local-``name()` functions.

Error handling. For both `ExtractValue()` and `UpdateXML()`, the XPath locator used must be valid and the XML to be searched must consist of elements which are properly nested and closed. If the locator is invalid, an error is generated:

```
mysql> SELECT ExtractValue('<a>c</a><b/>', '/&a');
ERROR 1105 (HY000): XPATH syntax error: '&a'
```

If `xml_frag` does not consist of elements which are properly nested and closed, `NULL` is returned and a warning is generated, as shown in this example:

```
mysql> SELECT ExtractValue('<a>c</a><b', '//a');
+-----------------------------------+
| ExtractValue('<a>c</a><b', '//a') |
+-----------------------------------+
| NULL                              |
+-----------------------------------+
1 row in set, 1 warning (0.00 sec)
mysql> SHOW WARNINGS\G
*************************** 1. row ***************************
Level: Warning
Code: 1525
Message: Incorrect XML value: 'parse error at line 1 pos 11:
END-OF-INPUT unexpected ('>' wanted)'
1 row in set (0.00 sec)
mysql> SELECT ExtractValue('<a>c</a><b/>', '//a');
+-------------------------------------+
| ExtractValue('<a>c</a><b/>', '//a') |
+-------------------------------------+
| c                                   |
+-------------------------------------+
1 row in set (0.00 sec)
```

Important The replacement XML used as the third argument to `UpdateXML()` is not checked to determine whether it consists solely of elements which are properly nested and closed.

XML Functions XPath Injection. code injection occurs when malicious code is introduced into the system to gain unauthorized access to privileges and data. It is based on exploiting assumptions made by developers about the type and content of data input from users. XPath is no exception in this regard.

A common scenario in which this can happen is the case of application which handles authorization by matching the combination of a login name and password with those found in an XML file, using an XPath expression like this one:

```
//user[login/text()='neapolitan' and password/text()='1c3cr34m']/attribute::id
```

This is the XPath equivalent of an SQL statement like this one:

```
SELECT id FROM users WHERE login='neapolitan' AND password='1c3cr34m';
```

A PHP application employing XPath might handle the login process like this:

```
<?php
$file     =   "users.xml";
$login    =   $POST["login"];
$password =   $POST["password"];
$xpath = "//user[login/text()=$login and password/text()=$password]/attribute::id";
if( file_exists($file) )
{
$xml = simplexml_load_file($file);
if($result = $xml->xpath($xpath))
echo "You are now logged in as user $result[0].";
else
echo "Invalid login name or password.";
}
else
exit("Failed to open $file.");
?>
```

No checks are performed on the input. This means that a malevolent user can “short-circuit” the test by entering `' or 1=1` for both the login name and password, resulting in `$xpath` being evaluated as shown here:

```
//user[login/text()='' or 1=1 and password/text()='' or 1=1]/attribute::id
```

Since the expression inside the square brackets always evaluates as `true`, it is effectively the same as this one, which matches the `id` attribute of every `user` element in the XML document:

```
//user/attribute::id
```

One way in which this particular attack can be circumvented is simply by quoting the variable names to be interpolated in the definition of `$xpath`, forcing the values passed from a Web form to be converted to strings:

```
$xpath = "//user[login/text()='$login' and password/text()='$password']/attribute::id";
```

This is the same strategy that is often recommended for preventing SQL injection attacks. In general, the practices you should follow for preventing XPath injection attacks are the same as for preventing SQL injection:

- Never accepted untested data from users in your application.
- Check all user-submitted data for type; reject or convert data that is of the wrong type

Bit Functions and Operators

- Test numeric data for out of range values; truncate, round, or reject values that are out of range. Test

strings for illegal characters and either strip them out or reject input containing them.

- Do not output explicit error messages that might provide an unauthorized user with clues that could be

used to compromise the system; log these to a file or database table instead.

Just as SQL injection attacks can be used to obtain information about database schemas, so can XPath injection be used to traverse XML files to uncover their structure, as discussed in Amit Klein's paper Blind XPath Injection (PDF file, 46KB).

It is also important to check the output being sent back to the client. Consider what can happen when we use the MySQL `ExtractValue()` function:

```
mysql> SELECT ExtractValue(
->     LOAD_FILE('users.xml'),
->     '//user[login/text()="" or 1=1 and password/text()="" or 1=1]/attribute::id'
-> ) AS id;
+-------------------------------+
| id                            |
+-------------------------------+
| 00327 13579 02403 42354 28570 |
+-------------------------------+
1 row in set (0.01 sec)
```

Because `ExtractValue()` returns multiple matches as a single space-delimited string, this injection attack provides every valid ID contained within `users.xml` to the user as a single row of output. As an extra safeguard, you should also test output before returning it to the user. Here is a simple example:

```
mysql> SELECT @id = ExtractValue(
->     LOAD_FILE('users.xml'),
->     '//user[login/text()="" or 1=1 and password/text()="" or 1=1]/attribute::id'
-> );
Query OK, 0 rows affected (0.00 sec)
mysql> SELECT IF(
->     INSTR(@id, ' ') = 0,
->     @id,
->     'Unable to retrieve user ID')
-> AS singleID;
+----------------------------+
| singleID                   |
+----------------------------+
| Unable to retrieve user ID |
+----------------------------+
1 row in set (0.00 sec)
```

In general, the guidelines for returning data to users securely are the same as for accepting user input.

These can be summed up as:

- Always test outgoing data for type and permissible values.
- Never permit unauthorized users to view error messages that might provide information about the

application that could be used to exploit it.

## 12.13 Bit Functions and Operators

Table 12.17 Bit Functions and Operators Name Description& Bitwise AND Bit Functions and Operators Name Description`>>` Right shift`<<` Left shift^ Bitwise XOR`BIT_COUNT()` Return the number of bits that are set| Bitwise OR~ Bitwise inversion Bit functions and operators comprise `BIT_COUNT()`, `BIT_AND()`, `BIT_OR()`, `BIT_XOR()`, &, |, ^, ~, `<<`,and `>>`. (`BIT_AND()`, `BIT_OR()`, and `BIT_XOR()` are aggregate functions described at Section 12.19.1,“Aggregate Function Descriptions”.) Bit functions and operators require `BIGINT` (64-bit integer) arguments and return `BIGINT` values, so they have a maximum range of 64 bits. Arguments of other types (such as the `BINARY` and `VARBINARY` binary string types) are converted to `BIGINT` and truncation might occur.

The following list describes available bit functions and operators:

- |

Bitwise OR.

The result is an unsigned 64-bit integer.

```
mysql> SELECT 29 | 15;
-> 31
```

- &

Bitwise AND.

The result is an unsigned 64-bit integer.

```
mysql> SELECT 29 & 15;
-> 13
```

- ^

Bitwise XOR.

The result is an unsigned 64-bit integer.

```
mysql> SELECT 1 ^ 1;
-> 0
mysql> SELECT 1 ^ 0;
-> 1
mysql> SELECT 11 ^ 3;
-> 8
```

- `<<`

Shifts a longlong (`BIGINT`) number to the left.

The result is an unsigned 64-bit integer. The value is truncated to 64 bits. In particular, if the shift count is greater or equal to the width of an unsigned 64-bit number, the result is zero.

```
mysql> SELECT 1 << 2;
-> 4
```

- `>>`

Encryption and Compression Functions Shifts a longlong (`BIGINT`) number to the right.

The result is an unsigned 64-bit integer. The value is truncated to 64 bits. In particular, if the shift count is greater or equal to the width of an unsigned 64-bit number, the result is zero.

```
mysql> SELECT 4 >> 2;
-> 1
```

- ~

Invert all bits.

The result is an unsigned 64-bit integer.

```
mysql> SELECT 5 & ~1;
-> 4
- BIT_COUNT(N)
```

Returns the number of bits that are set in the argument N as an unsigned 64-bit integer, or `NULL` if the argument is `NULL`.

```
mysql> SELECT BIT_COUNT(29), BIT_COUNT(b'101010');
-> 4, 3
```

## 12.14 Encryption and Compression Functions

Table 12.18 Encryption Functions Name Description Introduced Deprecated`AES_DECRYPT()` Decrypt using AES`AES_ENCRYPT()` Encrypt using AES`COMPRESS()` Return result as a binary string`DECODE()` Decode a string encrypted using ENCODE()`DES_DECRYPT()` Decrypt a string`DES_ENCRYPT()` Encrypt a string`ENCODE()` Encode a string`ENCRYPT()` Encrypt a string`MD5()` Calculate MD5 checksum`OLD_PASSWORD()` Return the value of the Yes pre-4.1 implementation of PASSWORD`PASSWORD()` Calculate and return a password string`RANDOM_BYTES()` Return a random byte 5.6.17 vector`SHA1()`, `SHA()` Calculate an SHA-1 160-bit checksum Encryption and Compression Functions Name Description Introduced Deprecated`SHA2()` Calculate an SHA-2 checksum`UNCOMPRESS()` Uncompress a string compressed`UNCOMPRESSED_LENGTH()`Return the length of a string before compression`VALIDATE_PASSWORD_STRENGTH()`Determine strength of password Many encryption and compression functions return strings for which the result might contain arbitrary byte values. If you want to store these results, use a column with a `VARBINARY` or `BLOB` binary string data type.

This avoids potential problems with trailing space removal or character set conversion that would change data values, such as may occur if you use a nonbinary string data type (`CHAR`, `VARCHAR`, `TEXT`).

Some encryption functions return strings of ASCII characters: `MD5()`, `OLD_PASSWORD()`, `PASSWORD()`,`SHA()`, `SHA1()`, `SHA2()`. Their return value is a string that has a character set and collation determined by the `character_set_connection` and `collation_connection` system variables. This is a nonbinary string unless the character set is `binary`.

If an application stores values from a function such as `MD5()` or `SHA1()` that returns a string of hex digits, more efficient storage and comparisons can be obtained by converting the hex representation to binary using `UNHEX()` and storing the result in a `BINARY(N)` column. Each pair of hexadecimal digits requires one byte in binary form, so the value of N depends on the length of the hex string. N is 16 for an`MD5()` value and 20 for a `SHA1()` value. For `SHA2()`, N ranges from 28 to 32 depending on the argument specifying the desired bit length of the result.

The size penalty for storing the hex string in a `CHAR` column is at least two times, up to eight times if the value is stored in a column that uses the `utf8` character set (where each character uses 4 bytes). Storing the string also results in slower comparisons because of the larger values and the need to take character set collation rules into account.

Suppose that an application stores `MD5()` string values in a `CHAR(32)` column:

```
CREATE TABLE md5_tbl (md5_val CHAR(32), ...);
INSERT INTO md5_tbl (md5_val, ...) VALUES(MD5('abcdef'), ...);
```

To convert hex strings to more compact form, modify the application to use `UNHEX()` and `BINARY(16)`instead as follows:

```
CREATE TABLE md5_tbl (md5_val BINARY(16), ...);
INSERT INTO md5_tbl (md5_val, ...) VALUES(UNHEX(MD5('abcdef')), ...);
```

Applications should be prepared to handle the very rare case that a hashing function produces the same value for two different input values. One way to make collisions detectable is to make the hash column a primary key.

Note Exploits for the MD5 and SHA-1 algorithms have become known. You may wish to consider using another one-way encryption function described in this section instead, such as `SHA2()`.

Encryption and Compression Functions Caution Passwords or other sensitive values supplied as arguments to encryption functions are sent as cleartext to the MySQL server unless an SSL connection is used. Also,such values appear in any MySQL logs to which they are written. To avoid these types of exposure, applications can encrypt sensitive values on the client side before sending them to the server. The same considerations apply to encryption keys. To avoid exposing these, applications can use stored procedures to encrypt and decrypt values on the server side.

```
- AES_DECRYPT(crypt_str,key_str[,init_vector])
```

This function decrypts data using the official AES (Advanced Encryption Standard) algorithm. For more information, see the description of `AES_ENCRYPT()`.

The optional initialization vector argument, `init_vector`, is available as of MySQL 5.6.17. As of that version, statements that use `AES_DECRYPT()` are unsafe for statement-based replication and cannot be stored in the query cache.

```
- AES_ENCRYPT(str,key_str[,init_vector])
```

`AES_ENCRYPT()` and `AES_DECRYPT()` implement encryption and decryption of data using the official AES (Advanced Encryption Standard) algorithm, previously known as “Rijndael.” The AES standard permits various key lengths. By default these functions implement AES with a 128-bit key length. As of MySQL 5.6.17, key lengths of 196 or 256 bits can be used, as described later. The key length is a trade off between performance and security.

`AES_ENCRYPT()` encrypts the string `str` using the key string `key_str` and returns a binary string containing the encrypted output. `AES_DECRYPT()` decrypts the encrypted string `crypt_str` using the key string `key_str` and returns the original plaintext string. If either function argument is `NULL`, the function returns `NULL`.

The `str` and `crypt_str` arguments can be any length, and padding is automatically added to `str`so it is a multiple of a block as required by block-based algorithms such as AES. This padding is automatically removed by the `AES_DECRYPT()` function. The length of `crypt_str` can be calculated using this formula:

```
16 * (trunc(string_length / 16) + 1)
```

For a key length of 128 bits, the most secure way to pass a key to the `key_str` argument is to create a truly random 128-bit value and pass it as a binary value. For example:

```
INSERT INTO t
VALUES (1,AES_ENCRYPT('text',UNHEX('F3229A0B371ED2D9441B830D21A390C3')));
```

A passphrase can be used to generate an AES key by hashing the passphrase. For example:

```
INSERT INTO t
```

Encryption and Compression Functions

```
VALUES (1,AES_ENCRYPT('text', UNHEX(SHA2('My secret passphrase',512))));
```

Do not pass a password or passphrase directly to `crypt_str`, hash it first. Previous versions of this documentation suggested the former approach, but it is no longer recommended as the examples shown here are more secure.

If `AES_DECRYPT()` detects invalid data or incorrect padding, it returns `NULL`. However, it is possible for`AES_DECRYPT()` to return a non-`NULL` value (possibly garbage) if the input data or the key is invalid.

As of MySQL 5.6.17, `AES_ENCRYPT()` and `AES_DECRYPT()` permit control of the block encryption mode and take an optional `init_vector` initialization vector argument:

- The `block_encryption_mode` system variable controls the mode for block-based encryption

algorithms. Its default value is `aes-128-ecb`, which signifies encryption using a key length of 128 bits and ECB mode. For a description of the permitted values of this variable, see Section 5.1.7, “Server System Variables”.

- The optional `init_vector` argument provides an initialization vector for block encryption modes that

require it.

For modes that require the optional `init_vector` argument, it must be 16 bytes or longer (bytes in excess of 16 are ignored). An error occurs if `init_vector` is missing.

For modes that do not require `init_vector`, it is ignored and a warning is generated if it is specified.

A random string of bytes to use for the initialization vector can be produced by calling`RANDOM_BYTES(16)`. For encryption modes that require an initialization vector, the same vector must be used for encryption and decryption.

```
mysql> SET block_encryption_mode = 'aes-256-cbc';
mysql> SET @key_str = SHA2('My secret passphrase',512);
mysql> SET @init_vector = RANDOM_BYTES(16);
mysql> SET @crypt_str = AES_ENCRYPT('text',@key_str,@init_vector);
mysql> SELECT AES_DECRYPT(@crypt_str,@key_str,@init_vector);
+-----------------------------------------------+
| AES_DECRYPT(@crypt_str,@key_str,@init_vector) |
+-----------------------------------------------+
| text                                          |
+-----------------------------------------------+
```

The following table lists each permitted block encryption mode, the SSL libraries that support it, and whether the initialization vector argument is required.

Block Encryption Mode SSL Libraries that Support Initialization Vector Required Mode ECB OpenSSL, yaSSL No CBC OpenSSL, yaSSL Yes CFB1 OpenSSL Yes CFB8 OpenSSL Yes CFB128 OpenSSL Yes Encryption and Compression Functions Block Encryption Mode SSL Libraries that Support Initialization Vector Required Mode OFB OpenSSL Yes As of MySQL 5.6.17, statements that use `AES_ENCRYPT()` or `AES_DECRYPT()` are unsafe for statement-based replication and cannot be stored in the query cache.

If `AES_ENCRYPT()` is invoked from within the `mysql` client, binary strings display using hexadecimal notation, depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

```
- COMPRESS(string_to_compress)
```

Compresses a string and returns the result as a binary string. This function requires MySQL to have been compiled with a compression library such as `zlib`. Otherwise, the return value is always `NULL`.

The compressed string can be uncompressed with `UNCOMPRESS()`.

```
mysql> SELECT LENGTH(COMPRESS(REPEAT('a',1000)));
-> 21
mysql> SELECT LENGTH(COMPRESS(''));
-> 0
mysql> SELECT LENGTH(COMPRESS('a'));
-> 13
mysql> SELECT LENGTH(COMPRESS(REPEAT('a',16)));
-> 15
```

The compressed string contents are stored the following way:

- Empty strings are stored as empty strings.
- Nonempty strings are stored as a 4-byte length of the uncompressed string (low byte first), followed by

the compressed string. If the string ends with space, an extra . character is added to avoid problems with endspace trimming should the result be stored in a `CHAR` or `VARCHAR` column. (However,use of nonbinary string data types such as `CHAR` or `VARCHAR` to store compressed strings is not recommended anyway because character set conversion may occur. Use a `VARBINARY` or `BLOB`binary string column instead.)If `COMPRESS()` is invoked from within the `mysql` client, binary strings display using hexadecimal notation, depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

```
- DECODE(crypt_str,pass_str)
```

Decrypts the encrypted string `crypt_str` using `pass_str` as the password. `crypt_str` should be a string returned from `ENCODE()`.

```
- DES_DECRYPT(crypt_str[,key_str])
```

Decrypts a string encrypted with `DES_ENCRYPT()`. If an error occurs, this function returns `NULL`.

This function works only if MySQL has been configured with SSL support. See Section 6.3, “Using Encrypted Connections”.

If no `key_str` argument is given, `DES_DECRYPT()` examines the first byte of the encrypted string to determine the DES key number that was used to encrypt the original string, and then reads the key from Encryption and Compression Functions the DES key file to decrypt the message. For this to work, the user must have the `SUPER` privilege. The key file can be specified with the `--des-key-file` server option.

If you pass this function a `key_str` argument, that string is used as the key for decrypting the message.

If the `crypt_str` argument does not appear to be an encrypted string, MySQL returns the given

```
crypt_str.
- DES_ENCRYPT(str[,{key_num|key_str}])
```

Encrypts the string with the given key using the Triple-DES algorithm.

This function works only if MySQL has been configured with SSL support. See Section 6.3, “Using Encrypted Connections”.

The encryption key to use is chosen based on the second argument to `DES_ENCRYPT()`, if one was given. With no argument, the first key from the DES key file is used. With a `key_num` argument, the given key number (0 to 9) from the DES key file is used. With a `key_str` argument, the given key string is used to encrypt `str`.

The key file can be specified with the `--des-key-file` server option.

The return string is a binary string where the first character is `CHAR(128 | key_num)`. If an error occurs, `DES_ENCRYPT()` returns `NULL`.

The 128 is added to make it easier to recognize an encrypted key. If you use a string key, `key_num` is

127.

The string length for the result is given by this formula:

```
new_len = orig_len + (8 - (orig_len % 8)) + 1
```

Each line in the DES key file has the following format:

```
key_num des_key_str
```

Each `key_num` value must be a number in the range from 0 to 9. Lines in the file may be in any order.

`des_key_str` is the string that is used to encrypt the message. There should be at least one space between the number and the key. The first key is the default key that is used if you do not specify any key argument to `DES_ENCRYPT()`.

You can tell MySQL to read new key values from the key file with the `FLUSH DES_KEY_FILE`statement. This requires the `RELOAD` privilege.

One benefit of having a set of default keys is that it gives applications a way to check for the existence of encrypted column values, without giving the end user the right to decrypt those values.

```
mysql> SELECT customer_address FROM customer_table
-> WHERE crypted_credit_card = DES_ENCRYPT('credit_card_number');
```

If `DES_ENCRYPT()` is invoked from within the `mysql` client, binary strings display using hexadecimal notation, depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

Encryption and Compression Functions

```
- ENCODE(str,pass_str)
```

Encrypt `str` using `pass_str` as the password. The result is a binary string of the same length as `str`.

To decrypt the result, use `DECODE()`.

The `ENCODE()` function should no longer be used. If you still need to use `ENCODE()`, a salt value must be used with it to reduce risk. For example:

```
ENCODE('cleartext', CONCAT('my_random_salt','my_secret_password'))
```

A new random salt value must be used whenever a password is updated.

If `ENCODE()` is invoked from within the `mysql` client, binary strings display using hexadecimal notation,depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

```
- ENCRYPT(str[,salt])
```

Encrypts `str` using the Unix `crypt()` system call and returns a binary string. The `salt` argument must be a string with at least two characters or the result is `NULL`. If no `salt` argument is given, a random value is used.

```
mysql> SELECT ENCRYPT('hello');
-> 'VxuFAJXVARROc'
```

`ENCRYPT()` ignores all but the first eight characters of `str`, at least on some systems. This behavior is determined by the implementation of the underlying `crypt()` system call.

The use of `ENCRYPT()` with the `ucs2`, `utf16`, `utf16le`, or `utf32` multibyte character sets is not recommended because the system call expects a string terminated by a zero byte.

If `crypt()` is not available on your system (as is the case with Windows), `ENCRYPT()` always returns

```
NULL.
```

If `ENCRYPT()` is invoked from within the `mysql` client, binary strings display using hexadecimal notation,depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

```
- MD5(str)
```

Calculates an MD5 128-bit checksum for the string. The value is returned as a string of 32 hexadecimal digits, or `NULL` if the argument was `NULL`. The return value can, for example, be used as a hash key.

See the notes at the beginning of this section about storing hash values efficiently.

The return value is a string in the connection character set.

```
mysql> SELECT MD5('testing');
-> 'ae2b1fca515949e5d54fb22b8ed95575'
```

This is the “RSA Data Security, Inc. MD5 Message-Digest Algorithm.”See the note regarding the MD5 algorithm at the beginning this section.

```
- OLD_PASSWORD(str)
```

`OLD_PASSWORD()` was added when the implementation of `PASSWORD()` was changed in MySQL 4.1 to improve security. `OLD_PASSWORD()` returns the value of the pre-4.1 implementation of `PASSWORD()` as Encryption and Compression Functions a string, and is intended to permit you to reset passwords for any pre-4.1 clients that need to connect to your MySQL server without locking them out. See Section 6.1.2.4, “Password Hashing in MySQL”.

The return value is a string in the connection character set.

Note Passwords that use the pre-4.1 hashing method are less secure than passwords that use the native password hashing method and should be avoided. Pre-4.1 passwords are deprecated; expect support for them to be removed in a future MySQL release. Consequently, `OLD_PASSWORD()` is also deprecated.

```
- PASSWORD(str)
```

Returns a hashed password string calculated from the cleartext password `str`. The return value is a string in the connection character set, or `NULL` if the argument is `NULL`. This function is the SQL interface to the algorithm used by the server to encrypt MySQL passwords for storage in the `mysql.user` grant table.

The `old_passwords` system variable controls the password hashing method used by the `PASSWORD()`function. It also influences password hashing performed by `CREATE USER` and `GRANT` statements that specify a password using an `IDENTIFIED BY` clause.

The following table shows, for each password hashing method, the permitted value of `old_passwords`and which authentication plugins use the hashing method.

Password Hashing Method old_passwords Value Associated Authentication Plugin MySQL 4.1 native hashing 0 `mysql_native_password`Pre-4.1 (“old”) hashing 1 `mysql_old_password`SHA-256 hashing 2 `sha256_password`Note Passwords that use the pre-4.1 hashing method are less secure than passwords that use the native password hashing method and should be avoided. Pre-4.1 passwords are deprecated; expect support for them to be removed in a future MySQL release. Consequently, `old_passwords=1`, which causes `PASSWORD()`to generate pre-4.1 password hashes, is also deprecated. For account upgrade instructions, see Section 6.4.1.3, “Migrating Away from Pre-4.1 Password Hashing and the mysql_old_password Plugin”.

If `old_passwords=1`, `PASSWORD(str)` returns the same value as `OLD_PASSWORD(str)`. The latter function is not affected by the value of `old_passwords`.

```
mysql> SET old_passwords = 0;
mysql> SELECT PASSWORD('mypass'), OLD_PASSWORD('mypass');
+-------------------------------------------+------------------------+
| PASSWORD('mypass')                        | OLD_PASSWORD('mypass') |
+-------------------------------------------+------------------------+
| *6C8989366EAF75BB670AD8EA7A7FC1176A95CEF4 | 6f8c114b58f2ce9e       |
+-------------------------------------------+------------------------+
mysql> SET old_passwords = 1;
mysql> SELECT PASSWORD('mypass'), OLD_PASSWORD('mypass');
+--------------------+------------------------+
| PASSWORD('mypass') | OLD_PASSWORD('mypass') |
```

Encryption and Compression Functions

```
+--------------------+------------------------+
| 6f8c114b58f2ce9e   | 6f8c114b58f2ce9e       |
+--------------------+------------------------+
```

SHA-256 password hashing (`old_passwords=2`) uses a random salt value, which makes the result from `PASSWORD()` nondeterministic. Consequently, statements that use this function are not safe for statement-based replication and cannot be stored in the query cache.

Encryption performed by `PASSWORD()` is one-way (not reversible). It is not the same type of encryption as used for Unix passwords; for that, use `ENCRYPT()`.

Note`PASSWORD()` is used by the authentication system in MySQL Server; you should not use it in your own applications. For that purpose, consider a more secure function such as `AES_ENCRYPT()` or `SHA2()` instead. Also see RFC 2195,section 2 (Challenge-Response Authentication Mechanism (CRAM)), for more information about handling passwords and authentication securely in your applications.

Caution Under some circumstances, statements that invoke `PASSWORD()` may be recorded in server logs or on the client side in a history file such as`~/.mysql_history`, which means that cleartext passwords may be read by anyone having read access to that information. For information about the conditions under which this occurs for the server logs and how to control it, see Section 6.1.2.3, “Passwords and Logging”. For similar information about client-side logging, see Section 4.5.1.3, “mysql Client Logging”.

```
- RANDOM_BYTES(len)
```

This function returns a binary string of `len` random bytes generated using the random number generator of the SSL library. Permitted values of `len` range from 1 to 1024. For values outside that range, an error occurs.

`RANDOM_BYTES()` can be used to provide the initialization vector for the `AES_DECRYPT()` and`AES_ENCRYPT()` functions. For use in that context, `len` must be at least 16. Larger values are permitted, but bytes in excess of 16 are ignored.

`RANDOM_BYTES()` generates a random value, which makes its result nondeterministic. Consequently,statements that use this function are unsafe for statement-based replication and cannot be stored in the query cache.

If `RANDOM_BYTES()` is invoked from within the `mysql` client, binary strings display using hexadecimal notation, depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

This function is available as of MySQL 5.6.17.

```
- SHA1(str), SHA(str)
```

Calculates an SHA-1 160-bit checksum for the string, as described in RFC 3174 (Secure Hash Algorithm). The value is returned as a string of 40 hexadecimal digits, or `NULL` if the argument was Encryption and Compression Functions`NULL`. One of the possible uses for this function is as a hash key. See the notes at the beginning of this section about storing hash values efficiently. `SHA()` is synonymous with `SHA1()`.

The return value is a string in the connection character set.

```
mysql> SELECT SHA1('abc');
-> 'a9993e364706816aba3e25717850c26c9cd0d89d'
```

`SHA1()` can be considered a cryptographically more secure equivalent of `MD5()`. However, see the note regarding the MD5 and SHA-1 algorithms at the beginning this section.

```
- SHA2(str, hash_length)
```

Calculates the SHA-2 family of hash functions (SHA-224, SHA-256, SHA-384, and SHA-512). The first argument is the plaintext string to be hashed. The second argument indicates the desired bit length of the result, which must have a value of 224, 256, 384, 512, or 0 (which is equivalent to 256). If either argument is `NULL` or the hash length is not one of the permitted values, the return value is `NULL`.

Otherwise, the function result is a hash value containing the desired number of bits. See the notes at the beginning of this section about storing hash values efficiently.

The return value is a string in the connection character set.

```
mysql> SELECT SHA2('abc', 224);
-> '23097d223405d8228642a477bda255b32aadbce4bda0b3f7e36c9da7'
```

This function works only if MySQL has been configured with SSL support. See Section 6.3, “Using Encrypted Connections”.

`SHA2()` can be considered cryptographically more secure than `MD5()` or `SHA1()`.

```
- UNCOMPRESS(string_to_uncompress)
```

Uncompresses a string compressed by the `COMPRESS()` function. If the argument is not a compressed value, the result is `NULL`. This function requires MySQL to have been compiled with a compression library such as `zlib`. Otherwise, the return value is always `NULL`.

```
mysql> SELECT UNCOMPRESS(COMPRESS('any string'));
-> 'any string'
mysql> SELECT UNCOMPRESS('any string');
-> NULL
- UNCOMPRESSED_LENGTH(compressed_string)
```

Returns the length that the compressed string had before being compressed.

```
mysql> SELECT UNCOMPRESSED_LENGTH(COMPRESS(REPEAT('a',30)));
-> 30
- VALIDATE_PASSWORD_STRENGTH(str)
```

Given an argument representing a plaintext password, this function returns an integer to indicate how strong the password is. The return value ranges from 0 (weak) to 100 (strong).

Password assessment by `VALIDATE_PASSWORD_STRENGTH()` is done by the `validate_password`plugin. If that plugin is not installed, the function always returns 0. For information about installing`validate_password`, see Section 6.4.3, “The Password Validation Plugin”. To examine or configure Locking Functions the parameters that affect password testing, check or set the system variables implemented by`validate_password`. See Section 6.4.3.2, “Password Validation Plugin Options and Variables”.

The password is subjected to increasingly strict tests and the return value reflects which tests were satisfied, as shown in the following table.

Password Test Return Value Length < 4 0 Length ≥ 4 and < `validate_password_length` 25 Satisfies policy 1 (`LOW`) 50 Satisfies policy 2 (`MEDIUM`) 75 Satisfies policy 3 (`STRONG`) 100

## 12.15 Locking Functions

This section describes functions used to manipulate user-level locks.

Table 12.19 Locking Functions Name Description`GET_LOCK()` Get a named lock`IS_FREE_LOCK()` Whether the named lock is free`IS_USED_LOCK()` Whether the named lock is in use; return connection identifier if true`RELEASE_LOCK()` Release the named lock

```
- GET_LOCK(str,timeout)
```

Tries to obtain a lock with a name given by the string `str`, using a timeout of `timeout` seconds. A negative `timeout` value means infinite timeout. The lock is exclusive. While held by one session, other sessions cannot obtain a lock of the same name.

Returns 1 if the lock was obtained successfully, 0 if the attempt timed out (for example, because another client has previously locked the name), or `NULL` if an error occurred (such as running out of memory or the thread was killed with `mysqladmin kill`).

A lock obtained with `GET_LOCK()` is released explicitly by executing `RELEASE_LOCK()` or implicitly when your session terminates (either normally or abnormally). Locks obtained with `GET_LOCK()` are not released when transactions commit or roll back.

Important The behavior of `GET_LOCK()` changes in MySQL 5.7. In consideration of future upgrades, limit the `str` value to 64 characters or less and do not rely on subsequent calls to `GET_LOCK()` releasing previous locks.

`GET_LOCK()` can be used to implement application locks or to simulate record locks. Names are locked on a server-wide basis. If a name has been locked within one session, `GET_LOCK()` blocks any request by another session for a lock with the same name. This enables clients that agree on a given lock name to use the name to perform cooperative advisory locking. But be aware that it also enables a client that is not among the set of cooperating clients to lock a name, either inadvertently or deliberately, and thus Information Functions prevent any of the cooperating clients from locking that name. One way to reduce the likelihood of this is to use lock names that are database-specific or application-specific. For example, use lock names of the

```
form db_name.str or app_name.str.
mysql> SELECT GET_LOCK('lock1',10);
-> 1
mysql> SELECT IS_FREE_LOCK('lock2');
-> 1
mysql> SELECT GET_LOCK('lock2',10);
-> 1
mysql> SELECT RELEASE_LOCK('lock2');
-> 1
mysql> SELECT RELEASE_LOCK('lock1');
-> NULL
```

The second `RELEASE_LOCK()` call returns `NULL` because the lock `'lock1'` was automatically released by the second `GET_LOCK()` call.

If multiple clients are waiting for a lock, the order in which they acquire it is undefined. Applications should not assume that clients acquire the lock in the same order that they issued the lock requests.

`GET_LOCK()` is unsafe for statement-based replication. A warning is logged if you use this function when `binlog_format` is set to `STATEMENT`.

Since `GET_LOCK()` establishes a lock only on a single `mysqld`, it is not suitable for use with NDB Cluster, which has no way of enforcing an SQL lock across multiple MySQL servers. See Section 18.2.7.10, “Limitations Relating to Multiple NDB Cluster Nodes”, for more information.

```
- IS_FREE_LOCK(str)
```

Checks whether the lock named `str` is free to use (that is, not locked). Returns 1 if the lock is free (no one is using the lock), 0 if the lock is in use, and `NULL` if an error occurs (such as an incorrect argument).

This function is unsafe for statement-based replication. A warning is logged if you use this function when`binlog_format` is set to `STATEMENT`.

```
- IS_USED_LOCK(str)
```

Checks whether the lock named `str` is in use (that is, locked). If so, it returns the connection identifier of the client session that holds the lock. Otherwise, it returns `NULL`.

This function is unsafe for statement-based replication. A warning is logged if you use this function when`binlog_format` is set to `STATEMENT`.

```
- RELEASE_LOCK(str)
```

Releases the lock named by the string `str` that was obtained with `GET_LOCK()`. Returns 1 if the lock was released, 0 if the lock was not established by this thread (in which case the lock is not released),and `NULL` if the named lock did not exist. The lock does not exist if it was never obtained by a call to`GET_LOCK()` or if it has previously been released.

The `DO` statement is convenient to use with `RELEASE_LOCK()`. See Section 13.2.3, “DO Statement”.

This function is unsafe for statement-based replication. A warning is logged if you use this function when`binlog_format` is set to `STATEMENT`.

## 12.16 Information Functions

Information Functions Table 12.20 Information Functions Name Description`BENCHMARK()` Repeatedly execute an expression`CHARSET()` Return the character set of the argument`COERCIBILITY()` Return the collation coercibility value of the string argument`COLLATION()` Return the collation of the string argument`CONNECTION_ID()` Return the connection ID (thread ID) for the connection`CURRENT_USER()`, `CURRENT_USER` The authenticated user name and host name`DATABASE()` Return the default (current) database name`FOUND_ROWS()` For a SELECT with a LIMIT clause, the number of rows that would be returned were there no LIMIT clause`LAST_INSERT_ID()` Value of the AUTOINCREMENT column for the last INSERT`ROW_COUNT()` The number of rows updated`SCHEMA()` Synonym for DATABASE()`SESSION_USER()` Synonym for USER()`SYSTEM_USER()` Synonym for USER()`USER()` The user name and host name provided by the client`VERSION()` Return a string that indicates the MySQL server version

```
- BENCHMARK(count,expr)
```

The `BENCHMARK()` function executes the expression `expr` repeatedly `count` times. It may be used to time how quickly MySQL processes the expression. The result value is 0, or `NULL` for inappropriate arguments such as a `NULL` or negative repeat count.

The intended use is from within the `mysql` client, which reports query execution times:

```
mysql> SELECT BENCHMARK(1000000,AES_ENCRYPT('hello','goodbye'));
+---------------------------------------------------+
| BENCHMARK(1000000,AES_ENCRYPT('hello','goodbye')) |
+---------------------------------------------------+
|                                                 0 |
+---------------------------------------------------+
1 row in set (4.74 sec)
```

The time reported is elapsed time on the client end, not CPU time on the server end. It is advisable to execute `BENCHMARK()` several times, and to interpret the result with regard to how heavily loaded the server machine is.

`BENCHMARK()` is intended for measuring the runtime performance of scalar expressions, which has some significant implications for the way that you use it and interpret the results:Information Functions

- Only scalar expressions can be used. Although the expression can be a subquery, it must return a

single column and at most a single row. For example, `BENCHMARK(10, (SELECT * FROM t))` fails if the table t has more than one column or more than one row.

- Executing a `SELECT expr` statement N times differs from executing `SELECT BENCHMARK(N,`

`expr)` in terms of the amount of overhead involved. The two have very different execution profiles and you should not expect them to take the same amount of time. The former involves the parser,optimizer, table locking, and runtime evaluation N times each. The latter involves only runtime evaluation N times, and all the other components just once. Memory structures already allocated are reused, and runtime optimizations such as local caching of results already evaluated for aggregate functions can alter the results. Use of `BENCHMARK()` thus measures performance of the runtime component by giving more weight to that component and removing the “noise” introduced by the network, parser, optimizer, and so forth.

```
- CHARSET(str)
```

Returns the character set of the string argument.

```
mysql> SELECT CHARSET('abc');
-> 'latin1'
mysql> SELECT CHARSET(CONVERT('abc' USING utf8));
-> 'utf8'
mysql> SELECT CHARSET(USER());
-> 'utf8'
- COERCIBILITY(str)
```

Returns the collation coercibility value of the string argument.

```
mysql> SELECT COERCIBILITY('abc' COLLATE latin1_swedish_ci);
-> 0
mysql> SELECT COERCIBILITY(USER());
-> 3
mysql> SELECT COERCIBILITY('abc');
-> 4
mysql> SELECT COERCIBILITY(1000);
-> 5
```

The return values have the meanings shown in the following table. Lower values have higher precedence.

Coercibility Meaning Example 0 Explicit collation Value with `COLLATE` clause 1 No collation Concatenation of strings with different collations 2 Implicit collation Column value, stored routine parameter or local variable 3 System constant `USER()` return value 4 Coercible Literal string 5 Numeric Numeric or temporal value 6 Ignorable `NULL` or an expression derived from `NULL`For more information, see Section 10.8.4, “Collation Coercibility in Expressions”.

Information Functions

```
- COLLATION(str)
```

Returns the collation of the string argument.

```
mysql> SELECT COLLATION('abc');
-> 'latin1_swedish_ci'
mysql> SELECT COLLATION(_utf8'abc');
-> 'utf8_general_ci'
- CONNECTION_ID()
```

Returns the connection ID (thread ID) for the connection. Every connection has an ID that is unique among the set of currently connected clients.

The value returned by `CONNECTION_ID()` is the same type of value as displayed in the `ID` column of the Information Schema `PROCESSLIST` table, the `Id` column of `SHOW PROCESSLIST` output, and the`PROCESSLIST_ID` column of the Performance Schema `threads` table.

```
mysql> SELECT CONNECTION_ID();
-> 23786
```

Warning Changing the session value of the `pseudo_thread_id` system variable changes the value returned by the `CONNECTION_ID()` function.

```
- CURRENT_USER, CURRENT_USER()
```

Returns the user name and host name combination for the MySQL account that the server used to authenticate the current client. This account determines your access privileges. The return value is a string in the `utf8` character set.

The value of `CURRENT_USER()` can differ from the value of `USER()`.

```
mysql> SELECT USER();
-> 'davida@localhost'
mysql> SELECT * FROM mysql.user;
ERROR 1044: Access denied for user ''@'localhost' to
database 'mysql'
mysql> SELECT CURRENT_USER();
-> '@localhost'
```

The example illustrates that although the client specified a user name of `davida` (as indicated by the value of the `USER()` function), the server authenticated the client using an anonymous user account (as Information Functions seen by the empty user name part of the `CURRENT_USER()` value). One way this might occur is that there is no account listed in the grant tables for `davida`.

Within a stored program or view, `CURRENT_USER()` returns the account for the user who defined the object (as given by its `DEFINER` value) unless defined with the `SQL SECURITY INVOKER` characteristic.

In the latter case, `CURRENT_USER()` returns the object's invoker.

Triggers and events have no option to define the `SQL SECURITY` characteristic, so for these objects,`CURRENT_USER()` returns the account for the user who defined the object. To return the invoker, use

```
USER() or SESSION_USER().
```

The following statements support use of the `CURRENT_USER()` function to take the place of the name of(and, possibly, a host for) an affected user or a definer; in such cases, `CURRENT_USER()` is expanded where and as needed:

```
- DROP USER
- RENAME USER
- GRANT
- REVOKE
- CREATE FUNCTION
- CREATE PROCEDURE
- CREATE TRIGGER
- CREATE EVENT
- CREATE VIEW
- ALTER EVENT
- ALTER VIEW
- SET PASSWORD
```

For information about the implications that this expansion of `CURRENT_USER()` has for replication, see Section 17.4.1.8, “Replication of CURRENT_USER()”.

```
- DATABASE()
```

Returns the default (current) database name as a string in the `utf8` character set. If there is no default database, `DATABASE()` returns `NULL`. Within a stored routine, the default database is the database that the routine is associated with, which is not necessarily the same as the database that is the default in the calling context.

```
mysql> SELECT DATABASE();
-> 'test'
```

If there is no default database, `DATABASE()` returns `NULL`.

```
- FOUND_ROWS()
```

A `SELECT` statement may include a `LIMIT` clause to restrict the number of rows the server returns to the client. In some cases, it is desirable to know how many rows the statement would have returned Information Functions without the `LIMIT`, but without running the statement again. To obtain this row count, include an`SQL_CALC_FOUND_ROWS` option in the `SELECT` statement, and then invoke `FOUND_ROWS()` afterward:

```
mysql> SELECT SQL_CALC_FOUND_ROWS * FROM tbl_name
-> WHERE id > 100 LIMIT 10;
mysql> SELECT FOUND_ROWS();
```

The second `SELECT` returns a number indicating how many rows the first `SELECT` would have returned had it been written without the `LIMIT` clause.

In the absence of the `SQL_CALC_FOUND_ROWS` option in the most recent successful `SELECT` statement,`FOUND_ROWS()` returns the number of rows in the result set returned by that statement. If the statement includes a `LIMIT` clause, `FOUND_ROWS()` returns the number of rows up to the limit. For example,`FOUND_ROWS()` returns 10 or 60, respectively, if the statement includes `LIMIT 10` or `LIMIT 50, 10`.

The row count available through `FOUND_ROWS()` is transient and not intended to be available past the statement following the `SELECT SQL_CALC_FOUND_ROWS` statement. If you need to refer to the value later, save it:

```
mysql> SELECT SQL_CALC_FOUND_ROWS * FROM ... ;
mysql> SET @rows = FOUND_ROWS();
```

If you are using `SELECT SQL_CALC_FOUND_ROWS`, MySQL must calculate how many rows are in the full result set. However, this is faster than running the query again without `LIMIT`, because the result set need not be sent to the client.

`SQL_CALC_FOUND_ROWS` and `FOUND_ROWS()` can be useful in situations when you want to restrict the number of rows that a query returns, but also determine the number of rows in the full result set without running the query again. An example is a Web script that presents a paged display containing links to the pages that show other sections of a search result. Using `FOUND_ROWS()` enables you to determine how many other pages are needed for the rest of the result.

The use of `SQL_CALC_FOUND_ROWS` and `FOUND_ROWS()` is more complex for `UNION` statements than for simple `SELECT` statements, because `LIMIT` may occur at multiple places in a `UNION`. It may be applied to individual `SELECT` statements in the `UNION`, or global to the `UNION` result as a whole.

The intent of `SQL_CALC_FOUND_ROWS` for `UNION` is that it should return the row count that would be returned without a global `LIMIT`. The conditions for use of `SQL_CALC_FOUND_ROWS` with `UNION` are:

- The `SQL_CALC_FOUND_ROWS` keyword must appear in the first `SELECT` of the `UNION`.
- The value of `FOUND_ROWS()` is exact only if `UNION ALL` is used. If `UNION` without `ALL` is used,

duplicate removal occurs and the value of `FOUND_ROWS()` is only approximate.

- If no `LIMIT` is present in the `UNION`, `SQL_CALC_FOUND_ROWS` is ignored and returns the number of

rows in the temporary table that is created to process the `UNION`.

Beyond the cases described here, the behavior of `FOUND_ROWS()` is undefined (for example, its value following a `SELECT` statement that fails with an error).

Important`FOUND_ROWS()` is not replicated reliably using statement-based replication. This function is automatically replicated using row-based replication.

Information Functions

```
- LAST_INSERT_ID(), LAST_INSERT_ID(expr)
```

With no argument, `LAST_INSERT_ID()` returns a 64-bit value representing the first automatically generated value successfully inserted for an `AUTO_INCREMENT` column as a result of the most recently executed `INSERT` statement. The value of `LAST_INSERT_ID()` remains unchanged if no rows are successfully inserted.

With an argument, `LAST_INSERT_ID()` returns an unsigned integer.

For example, after inserting a row that generates an `AUTO_INCREMENT` value, you can get the value like this:

```
mysql> SELECT LAST_INSERT_ID();
-> 195
```

The currently executing statement does not affect the value of `LAST_INSERT_ID()`. Suppose that you generate an `AUTO_INCREMENT` value with one statement, and then refer to `LAST_INSERT_ID()`in a multiple-row `INSERT` statement that inserts rows into a table with its own `AUTO_INCREMENT`column. The value of `LAST_INSERT_ID()` remains stable in the second statement; its value for the second and later rows is not affected by the earlier row insertions. (However, if you mix references to`LAST_INSERT_ID()` and `LAST_INSERT_ID(expr)`, the effect is undefined.)If the previous statement returned an error, the value of `LAST_INSERT_ID()` is undefined. For transactional tables, if the statement is rolled back due to an error, the value of `LAST_INSERT_ID()` is left undefined. For manual `ROLLBACK`, the value of `LAST_INSERT_ID()` is not restored to that before the transaction; it remains as it was at the point of the `ROLLBACK`.

Prior to MySQL 5.6.15, this function was not replicated correctly if replication filtering rules were in use.

(Bug #17234370, Bug #69861)Within the body of a stored routine (procedure or function) or a trigger, the value of `LAST_INSERT_ID()`changes the same way as for statements executed outside the body of these kinds of objects. The effect of a stored routine or trigger upon the value of `LAST_INSERT_ID()` that is seen by following statements depends on the kind of routine:

- If a stored procedure executes statements that change the value of `LAST_INSERT_ID()`, the

changed value is seen by statements that follow the procedure call.

- For stored functions and triggers that change the value, the value is restored when the function or

trigger ends, so statements following it do not see a changed value.

The ID that was generated is maintained in the server on a per-connection basis. This means that the value returned by the function to a given client is the first `AUTO_INCREMENT` value generated for most recent statement affecting an `AUTO_INCREMENT` column by that client. This value cannot be affected by other clients, even if they generate `AUTO_INCREMENT` values of their own. This behavior ensures that each client can retrieve its own ID without concern for the activity of other clients, and without the need for locks or transactions.

The value of `LAST_INSERT_ID()` is not changed if you set the `AUTO_INCREMENT` column of a row to a non-“magic” value (that is, a value that is not `NULL` and not 0).

Important If you insert multiple rows using a single `INSERT` statement,`LAST_INSERT_ID()` returns the value generated for the first inserted row only.

Information Functions The reason for this is to make it possible to reproduce easily the same `INSERT`statement against some other server.

For example:

```
mysql> USE test;
mysql> CREATE TABLE t (
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(10) NOT NULL
);
mysql> INSERT INTO t VALUES (NULL, 'Bob');
mysql> SELECT * FROM t;
+----+------+
| id | name |
+----+------+
|  1 | Bob  |
+----+------+
mysql> SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|                1 |
+------------------+
mysql> INSERT INTO t VALUES
(NULL, 'Mary'), (NULL, 'Jane'), (NULL, 'Lisa');
mysql> SELECT * FROM t;
+----+------+
| id | name |
+----+------+
|  1 | Bob  |
|  2 | Mary |
|  3 | Jane |
|  4 | Lisa |
+----+------+
mysql> SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|                2 |
+------------------+
```

Although the second `INSERT` statement inserted three new rows into t, the ID generated for the first of these rows was 2, and it is this value that is returned by `LAST_INSERT_ID()` for the following `SELECT`statement.

If you use `INSERT IGNORE` and the row is ignored, the `LAST_INSERT_ID()` remains unchanged from the current value (or 0 is returned if the connection has not yet performed a successful `INSERT`) and,for non-transactional tables, the `AUTO_INCREMENT` counter is not incremented. For `InnoDB` tables,the `AUTO_INCREMENT` counter is incremented if `innodb_autoinc_lock_mode` is set to 1 or 2, as demonstrated in the following example:

```
mysql> USE test;
mysql> SELECT @@innodb_autoinc_lock_mode;
+----------------------------+
| @@innodb_autoinc_lock_mode |
+----------------------------+
```

Information Functions

```
|                          1 |
+----------------------------+
mysql> CREATE TABLE `t` (
`id` INT(11) NOT NULL AUTO_INCREMENT,
`val` INT(11) DEFAULT NULL,
PRIMARY KEY (`id`),
UNIQUE KEY `i1` (`val`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
# Insert two rows
mysql> INSERT INTO t (val) VALUES (1),(2);
# With auto_increment_offset=1, the inserted rows
# result in an AUTO_INCREMENT value of 3
mysql> SHOW CREATE TABLE t\G
*************************** 1. row ***************************
Table: t
Create Table: CREATE TABLE `t` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`val` int(11) DEFAULT NULL,
PRIMARY KEY (`id`),
UNIQUE KEY `i1` (`val`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1
# LAST_INSERT_ID() returns the first automatically generated
# value that is successfully inserted for the AUTO_INCREMENT column
mysql> SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|                1 |
+------------------+
# The attempted insertion of duplicate rows fail but errors are ignored
mysql> INSERT IGNORE INTO t (val) VALUES (1),(2);
Query OK, 0 rows affected (0.00 sec)
Records: 2  Duplicates: 2  Warnings: 0
# With innodb_autoinc_lock_mode=1, the AUTO_INCREMENT counter
# is incremented for the ignored rows
mysql> SHOW CREATE TABLE t\G
*************************** 1. row ***************************
Table: t
Create Table: CREATE TABLE `t` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`val` int(11) DEFAULT NULL,
PRIMARY KEY (`id`),
UNIQUE KEY `i1` (`val`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1
# The LAST_INSERT_ID is unchanged because the previous insert was unsuccessful
mysql> SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|                1 |
```

Information Functions

```
+------------------+
```

For more information, see Section 14.6.1.6, “AUTO_INCREMENT Handling in InnoDB”.

If `expr` is given as an argument to `LAST_INSERT_ID()`, the value of the argument is returned by the function and is remembered as the next value to be returned by `LAST_INSERT_ID()`. This can be used to simulate sequences:

1. Create a table to hold the sequence counter and initialize it:

```
mysql> CREATE TABLE sequence (id INT NOT NULL);
mysql> INSERT INTO sequence VALUES (0);
```

2. Use the table to generate sequence numbers like this:

```
mysql> UPDATE sequence SET id=LAST_INSERT_ID(id+1);
mysql> SELECT LAST_INSERT_ID();
```

The `UPDATE` statement increments the sequence counter and causes the next call to`LAST_INSERT_ID()` to return the updated value. The `SELECT` statement retrieves that value. The`mysql_insert_id()` C API function can also be used to get the value. See mysql_insert_id().

You can generate sequences without calling `LAST_INSERT_ID()`, but the utility of using the function this way is that the ID value is maintained in the server as the last automatically generated value. It is multi-user safe because multiple clients can issue the `UPDATE` statement and get their own sequence value with the `SELECT` statement (or `mysql_insert_id()`), without affecting or being affected by other clients that generate their own sequence values.

The `mysql_insert_id()` function is only updated after the `INSERT` and `UPDATE` statements, so you cannot use the C API function to retrieve the value for `LAST_INSERT_ID(expr)` after executing other SQL statements like `SELECT` or `SET`.

```
- ROW_COUNT()
```

`ROW_COUNT()` returns a value as follows:

- DDL statements: 0. This applies to statements such as `CREATE TABLE` or `DROP TABLE`.
- DML statements other than `SELECT`: The number of affected rows. This applies to statements such

as `UPDATE`, `INSERT`, or `DELETE` (as before), but now also to statements such as `ALTER TABLE` and

```
LOAD DATA.
```

- `SELECT`: -1 if the statement returns a result set, or the number of rows “affected” if it does not. For

example, for `SELECT * FROM t1`, `ROW_COUNT()` returns -1. For `SELECT * FROM t1 INTO``OUTFILE 'file_name'`, `ROW_COUNT()` returns the number of rows written to the file.

- `SIGNAL` statements: 0.

For `UPDATE` statements, the affected-rows value by default is the number of rows actually changed. If you specify the `CLIENT_FOUND_ROWS` flag to `mysql_real_connect()` when connecting to `mysqld`,the affected-rows value is the number of rows “found”; that is, matched by the `WHERE` clause.

For `REPLACE` statements, the affected-rows value is 2 if the new row replaced an old row, because in this case, one row was inserted after the duplicate was deleted.

For `INSERT ... ON DUPLICATE KEY UPDATE` statements, the affected-rows value per row is 1 if the row is inserted as a new row, 2 if an existing row is updated, and 0 if an existing row is set to its current Information Functions values. If you specify the `CLIENT_FOUND_ROWS` flag, the affected-rows value is 1 (not 0) if an existing row is set to its current values.

The `ROW_COUNT()` value is similar to the value from the `mysql_affected_rows()` C API function and the row count that the `mysql` client displays following statement execution.

```
mysql> INSERT INTO t VALUES(1),(2),(3);
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0
mysql> SELECT ROW_COUNT();
+-------------+
| ROW_COUNT() |
+-------------+
|           3 |
+-------------+
1 row in set (0.00 sec)
mysql> DELETE FROM t WHERE i IN(1,2);
Query OK, 2 rows affected (0.00 sec)
mysql> SELECT ROW_COUNT();
+-------------+
| ROW_COUNT() |
+-------------+
|           2 |
+-------------+
1 row in set (0.00 sec)
```

Important`ROW_COUNT()` is not replicated reliably using statement-based replication. This function is automatically replicated using row-based replication.

```
- SCHEMA()
```

This function is a synonym for `DATABASE()`.

```
- SESSION_USER()
```

`SESSION_USER()` is a synonym for `USER()`.

```
- SYSTEM_USER()
```

`SYSTEM_USER()` is a synonym for `USER()`.

```
- USER()
```

Returns the current MySQL user name and host name as a string in the `utf8` character set.

```
mysql> SELECT USER();
-> 'davida@localhost'
```

The value indicates the user name you specified when connecting to the server, and the client host from which you connected. The value can be different from that of `CURRENT_USER()`.

Spatial Analysis Functions

```
- VERSION()
```

Returns a string that indicates the MySQL server version. The string uses the `utf8` character set. The value might have a suffix in addition to the version number. See the description of the `version` system variable in Section 5.1.7, “Server System Variables”.

This function is unsafe for statement-based replication. A warning is logged if you use this function when`binlog_format` is set to `STATEMENT`.

```
mysql> SELECT VERSION();
-> '5.6.51-standard'
```

## 12.17 Spatial Analysis Functions

MySQL provides functions to perform various operations on spatial data. These functions can be grouped into several major categories according to the type of operation they perform:

- Functions that create geometries in various formats (WKT, WKB, internal)
- Functions that convert geometries between formats
- Functions that access qualitative or quantitative properties of a geometry
- Functions that describe relations between two geometries
- Functions that create new geometries from existing ones

For general background about MySQL support for using spatial data, see Section 11.4, “Spatial Data Types”.

### 12.17.1 Spatial Function Reference

The following table lists each spatial function and provides a short description of each one.

Table 12.21 Spatial Functions Name Description`Area()` Return Polygon or MultiPolygon area`AsBinary()`, `AsWKB()` Convert from internal geometry format to WKB`AsText()`, `AsWKT()` Convert from internal geometry format to WKT`Buffer()` Return geometry of points within given distance from geometry`Centroid()` Return centroid as a point`Contains()` Whether MBR of one geometry contains MBR of another`Crosses()` Whether one geometry crosses another`Dimension()` Dimension of geometry`Disjoint()` Whether MBRs of two geometries are disjoint`EndPoint()` End Point of LineString`Envelope()` Return MBR of geometry`Equals()` Whether MBRs of two geometries are equal`ExteriorRing()` Return exterior ring of Polygon Spatial Function Reference Name Description`GeomCollFromText()`, Return geometry collection from WKT

```
GeometryCollectionFromText()
```

`GeomCollFromWKB()`, Return geometry collection from WKB

```
GeometryCollectionFromWKB()
```

`GeometryCollection()` Construct geometry collection from geometries`GeometryN()` Return N-th geometry from geometry collection`GeometryType()` Return name of geometry type`GeomFromText()`, `GeometryFromText()` Return geometry from WKT`GeomFromWKB()`, `GeometryFromWKB()` Return geometry from WKB`GLength()` Return length of LineString`InteriorRingN()` Return N-th interior ring of Polygon`Intersects()` Whether MBRs of two geometries intersect`IsClosed()` Whether a geometry is closed and simple`IsEmpty()` Whether a geometry is empty`IsSimple()` Whether a geometry is simple`LineFromText()`, `LineStringFromText()` Construct LineString from WKT`LineFromWKB()`, `LineStringFromWKB()` Construct LineString from WKB`LineString()` Construct LineString from Point values`MBRContains()` Whether MBR of one geometry contains MBR of another`MBRDisjoint()` Whether MBRs of two geometries are disjoint`MBREqual()` Whether MBRs of two geometries are equal`MBRIntersects()` Whether MBRs of two geometries intersect`MBROverlaps()` Whether MBRs of two geometries overlap`MBRTouches()` Whether MBRs of two geometries touch`MBRWithin()` Whether MBR of one geometry is within MBR of another`MLineFromText()`, Construct MultiLineString from WKT

```
MultiLineStringFromText()
```

`MLineFromWKB()`, Construct MultiLineString from WKB

```
MultiLineStringFromWKB()
```

`MPointFromText()`, `MultiPointFromText()` Construct MultiPoint from WKT`MPointFromWKB()`, `MultiPointFromWKB()` Construct MultiPoint from WKB`MPolyFromText()`, `MultiPolygonFromText()` Construct MultiPolygon from WKT`MPolyFromWKB()`, `MultiPolygonFromWKB()` Construct MultiPolygon from WKB`MultiLineString()` Contruct MultiLineString from LineString values`MultiPoint()` Construct MultiPoint from Point values`MultiPolygon()` Construct MultiPolygon from Polygon values`NumGeometries()` Return number of geometries in geometry collection Spatial Function Reference Name Description`NumInteriorRings()` Return number of interior rings in Polygon`NumPoints()` Return number of points in LineString`Overlaps()` Whether MBRs of two geometries overlap`Point()` Construct Point from coordinates`PointFromText()` Construct Point from WKT`PointFromWKB()` Construct Point from WKB`PointN()` Return N-th point from LineString`PolyFromText()`, `PolygonFromText()` Construct Polygon from WKT`PolyFromWKB()`, `PolygonFromWKB()` Construct Polygon from WKB`Polygon()` Construct Polygon from LineString arguments`SRID()` Return spatial reference system ID for geometry`ST_Area()` Return Polygon or MultiPolygon area`ST_AsBinary()`, `ST_AsWKB()` Convert from internal geometry format to WKB`ST_AsText()`, `ST_AsWKT()` Convert from internal geometry format to WKT`ST_Buffer()` Return geometry of points within given distance from geometry`ST_Centroid()` Return centroid as a point`ST_Contains()` Whether one geometry contains another`ST_Crosses()` Whether one geometry crosses another`ST_Difference()` Return point set difference of two geometries`ST_Dimension()` Dimension of geometry`ST_Disjoint()` Whether one geometry is disjoint from another`ST_Distance()` The distance of one geometry from another`ST_EndPoint()` End Point of LineString`ST_Envelope()` Return MBR of geometry`ST_Equals()` Whether one geometry is equal to another`ST_ExteriorRing()` Return exterior ring of Polygon`ST_GeomCollFromText()`, Return geometry collection from WKT

```
ST_GeometryCollectionFromText(),
ST_GeomCollFromTxt()
```

`ST_GeomCollFromWKB()`, Return geometry collection from WKB

```
ST_GeometryCollectionFromWKB()
```

`ST_GeometryN()` Return N-th geometry from geometry collection`ST_GeometryType()` Return name of geometry type`ST_GeomFromText()`, Return geometry from WKT

```
ST_GeometryFromText()
```

`ST_GeomFromWKB()`, `ST_GeometryFromWKB()` Return geometry from WKB`ST_InteriorRingN()` Return N-th interior ring of Polygon`ST_Intersection()` Return point set intersection of two geometries Argument Handling by Spatial Functions Name Description`ST_Intersects()` Whether one geometry intersects another`ST_IsClosed()` Whether a geometry is closed and simple`ST_IsEmpty()` Whether a geometry is empty`ST_IsSimple()` Whether a geometry is simple`ST_LineFromText()`, Construct LineString from WKT

```
ST_LineStringFromText()
```

`ST_LineFromWKB()`, Construct LineString from WKB

```
ST_LineStringFromWKB()
```

`ST_NumGeometries()` Return number of geometries in geometry collection`ST_NumInteriorRing()`, Return number of interior rings in Polygon

```
ST_NumInteriorRings()
```

`ST_NumPoints()` Return number of points in LineString`ST_Overlaps()` Whether one geometry overlaps another`ST_PointFromText()` Construct Point from WKT`ST_PointFromWKB()` Construct Point from WKB`ST_PointN()` Return N-th point from LineString`ST_PolyFromText()`, `ST_PolygonFromText()` Construct Polygon from WKT`ST_PolyFromWKB()`, `ST_PolygonFromWKB()` Construct Polygon from WKB`ST_SRID()` Return spatial reference system ID for geometry`ST_StartPoint()` Start Point of LineString`ST_SymDifference()` Return point set symmetric difference of two geometries`ST_Touches()` Whether one geometry touches another`ST_Union()` Return point set union of two geometries`ST_Within()` Whether one geometry is within another`ST_X()` Return X coordinate of Point`ST_Y()` Return Y coordinate of Point`StartPoint()` Start Point of LineString`Touches()` Whether one geometry touches another`Within()` Whether MBR of one geometry is within MBR of another`X()` Return X coordinate of Point`Y()` Return Y coordinate of Point

### 12.17.2 Argument Handling by Spatial Functions

Spatial values, or geometries, have the properties described in Section 11.4.2.2, “Geometry Class”. The following discussion lists general spatial function argument-handling characteristics. Specific functions or groups of functions may have additional or different argument-handling characteristics, as discussed in the sections where those function descriptions occur. Where that is true, those descriptions take precedence over the general discussion here.

Functions That Create Geometry Values from WKT Values Spatial functions are defined only for valid geometry values. If an invalid geometry is passed to a spatial function, the result is undefined.

The spatial reference identifier (SRID) of a geometry identifies the coordinate space in which the geometry is defined. In MySQL, the SRID value is an integer associated with the geometry value. The maximum usable SRID value is 232−1. If a larger value is given, only the lower 32 bits are used.

Geometry values produced by any spatial function inherit the SRID of the geometry arguments.

### 12.17.3 Functions That Create Geometry Values from WKT Values

These functions take as arguments a Well-Known Text (WKT) representation and, optionally, a spatial reference system identifier (SRID). They return the corresponding geometry.

`GeomFromText()` and `ST_GeomFromText()` accept a WKT value of any geometry type as their first argument. Other functions provide type-specific construction functions for construction of geometry values of each geometry type.

For a description of WKT format, see Well-Known Text (WKT) Format.

```
- GeomCollFromText(wkt [, srid]), GeometryCollectionFromText(wkt [, srid])
ST_GeomCollFromText(), ST_GeometryCollectionFromText(), GeomCollFromText(),
```

and `GeometryCollectionFromText()` are synonyms. For more information, see the description of

```
ST_GeomCollFromText().
- GeomFromText(wkt [, srid]), GeometryFromText(wkt [, srid])
ST_GeomFromText(), ST_GeometryFromText(), GeomFromText(), and GeometryFromText()
```

are synonyms. For more information, see the description of `ST_GeomFromText()`.

```
- LineFromText(wkt [, srid]), LineStringFromText(wkt [, srid])
ST_LineFromText(), ST_LineStringFromText(), LineFromText(), and
```

`LineStringFromText()` are synonyms. For more information, see the description of

```
ST_LineFromText().
- MLineFromText(wkt [, srid]), MultiLineStringFromText(wkt [, srid])
```

Constructs a `MultiLineString` value using its WKT representation and SRID.

The result is `NULL` if the geometry argument is `NULL` or not a syntactically well-formed geometry.

```
- MPointFromText(wkt [, srid]), MultiPointFromText(wkt [, srid])
```

Constructs a `MultiPoint` value using its WKT representation and SRID.

The result is `NULL` if the geometry argument is `NULL` or not a syntactically well-formed geometry.

```
- MPolyFromText(wkt [, srid]), MultiPolygonFromText(wkt [, srid])
```

Constructs a `MultiPolygon` value using its WKT representation and SRID.

The result is `NULL` if the geometry argument is `NULL` or not a syntactically well-formed geometry.

```
- PointFromText(wkt [, srid])
```

`ST_PointFromText()` and `PointFromText()` are synonyms. For more information, see the description of `ST_PointFromText()`.

Functions That Create Geometry Values from WKT Values

```
- PolyFromText(wkt [, srid]), PolygonFromText(wkt [, srid])
ST_PolyFromText(), ST_PolygonFromText(), PolyFromText(), and PolygonFromText() are
```

synonyms. For more information, see the description of `ST_PolyFromText()`.

```
- ST_GeomCollFromText(wkt [, srid]), ST_GeometryCollectionFromText(wkt [, srid])
```

Constructs a `GeometryCollection` value using its WKT representation and SRID.

The result is `NULL` if the geometry argument is `NULL` or not a syntactically well-formed geometry.

```
mysql> SET @g = "MULTILINESTRING((10 10, 11 11), (9 9, 10 10))";
mysql> SELECT ST_AsText(ST_GeomCollFromText(@g));
+--------------------------------------------+
| ST_AsText(ST_GeomCollFromText(@g))         |
+--------------------------------------------+
| MULTILINESTRING((10 10,11 11),(9 9,10 10)) |
+--------------------------------------------+
ST_GeomCollFromText(), ST_GeometryCollectionFromText(), GeomCollFromText(), and
```

`GeometryCollectionFromText()` are synonyms.

```
- ST_GeomFromText(wkt [, srid]), ST_GeometryFromText(wkt [, srid])
```

Constructs a geometry value of any type using its WKT representation and SRID.

The result is `NULL` if the geometry argument is `NULL` or not a syntactically well-formed geometry.

```
ST_GeomFromText(), ST_GeometryFromText(), GeomFromText(), and GeometryFromText()
```

are synonyms.

```
- ST_LineFromText(wkt [, srid]), ST_LineStringFromText(wkt [, srid])
```

Constructs a `LineString` value using its WKT representation and SRID.

The result is `NULL` if the geometry argument is `NULL` or not a syntactically well-formed geometry.

```
ST_LineFromText(), ST_LineStringFromText(), LineFromText(), and
```

`LineStringFromText()` are synonyms.

```
- ST_PointFromText(wkt [, srid])
```

Constructs a `Point` value using its WKT representation and SRID.

The result is `NULL` if the geometry argument is `NULL` or not a syntactically well-formed geometry.

`ST_PointFromText()` and `PointFromText()` are synonyms.

```
- ST_PolyFromText(wkt [, srid]), ST_PolygonFromText(wkt [, srid])
```

Constructs a `Polygon` value using its WKT representation and SRID.

The result is `NULL` if the geometry argument is `NULL` or not a syntactically well-formed geometry.

```
ST_PolyFromText(), ST_PolygonFromText(), PolyFromText(), and PolygonFromText() are
```

synonyms.

Functions That Create Geometry Values from WKB Values

### 12.17.4 Functions That Create Geometry Values from WKB Values

These functions take as arguments a `BLOB` containing a Well-Known Binary (WKB) representation and,optionally, a spatial reference system identifier (SRID). They return the corresponding geometry.

`GeomFromWKB()` and `ST_GeomFromWKB()` accept a WKB value of any geometry type as their first argument. Other functions provide type-specific construction functions for construction of geometry values of each geometry type.

These functions also accept geometry objects as returned by the functions in Section 12.17.5, “MySQL-Specific Functions That Create Geometry Values”. Thus, those functions may be used to provide the first argument to the functions in this section.

For a description of WKB format, see Well-Known Binary (WKB) Format.

```
- GeomCollFromWKB(wkb [, srid]), GeometryCollectionFromWKB(wkb [, srid])
ST_GeomCollFromWKB(), ST_GeometryCollectionFromWKB(), GeomCollFromWKB(), and
```

`GeometryCollectionFromWKB()` are synonyms. For more information, see the description of

```
ST_GeomCollFromWKB().
- GeomFromWKB(wkb [, srid]), GeometryFromWKB(wkb [, srid])
ST_GeomFromWKB(), ST_GeometryFromWKB(), GeomFromWKB(), and GeometryFromWKB() are
```

synonyms. For more information, see the description of `ST_GeomFromWKB()`.

```
- LineFromWKB(wkb [, srid]), LineStringFromWKB(wkb [, srid])
ST_LineFromWKB(), ST_LineStringFromWKB(), LineFromWKB(), and LineStringFromWKB()
```

are synonyms. For more information, see the description of `ST_LineFromWKB()`.

```
- MLineFromWKB(wkb [, srid]), MultiLineStringFromWKB(wkb [, srid])
```

Constructs a `MultiLineString` value using its WKB representation and SRID.

The result is `NULL` if the WKB or SRID argument is `NULL`.

```
- MPointFromWKB(wkb [, srid]), MultiPointFromWKB(wkb [, srid])
```

Constructs a `MultiPoint` value using its WKB representation and SRID.

The result is `NULL` if the WKB or SRID argument is `NULL`.

```
- MPolyFromWKB(wkb [, srid]), MultiPolygonFromWKB(wkb [, srid])
```

Constructs a `MultiPolygon` value using its WKB representation and SRID.

The result is `NULL` if the WKB or SRID argument is `NULL`.

```
- PointFromWKB(wkb [, srid])
```

`ST_PointFromWKB()` and `PointFromWKB()` are synonyms. For more information, see the description

```
of ST_PointFromWKB().
- PolyFromWKB(wkb [, srid]), PolygonFromWKB(wkb [, srid])
ST_PolyFromWKB(), ST_PolygonFromWKB(), PolyFromWKB(), and PolygonFromWKB() are
```

synonyms. For more information, see the description of `ST_PolyFromWKB()`.

MySQL-Specific Functions That Create Geometry Values

```
- ST_GeomCollFromWKB(wkb [, srid]), ST_GeometryCollectionFromWKB(wkb [, srid])
```

Constructs a `GeometryCollection` value using its WKB representation and SRID.

The result is `NULL` if the WKB or SRID argument is `NULL`.

```
ST_GeomCollFromWKB(), ST_GeometryCollectionFromWKB(), GeomCollFromWKB(), and
```

`GeometryCollectionFromWKB()` are synonyms.

```
- ST_GeomFromWKB(wkb [, srid]), ST_GeometryFromWKB(wkb [, srid])
```

Constructs a geometry value of any type using its WKB representation and SRID.

The result is `NULL` if the WKB or SRID argument is `NULL`.

```
ST_GeomFromWKB(), ST_GeometryFromWKB(), GeomFromWKB(), and GeometryFromWKB() are
```

synonyms.

```
- ST_LineFromWKB(wkb [, srid]), ST_LineStringFromWKB(wkb [, srid])
```

Constructs a `LineString` value using its WKB representation and SRID.

The result is `NULL` if the WKB or SRID argument is `NULL`.

```
ST_LineFromWKB(), ST_LineStringFromWKB(), LineFromWKB(), and LineStringFromWKB()
```

are synonyms.

```
- ST_PointFromWKB(wkb [, srid])
```

Constructs a `Point` value using its WKB representation and SRID.

The result is `NULL` if the WKB or SRID argument is `NULL`.

`ST_PointFromWKB()` and `PointFromWKB()` are synonyms.

```
- ST_PolyFromWKB(wkb [, srid]), ST_PolygonFromWKB(wkb [, srid])
```

Constructs a `Polygon` value using its WKB representation and SRID.

The result is `NULL` if the WKB or SRID argument is `NULL`.

```
ST_PolyFromWKB(), ST_PolygonFromWKB(), PolyFromWKB(), and PolygonFromWKB() are
```

synonyms.

### 12.17.5 MySQL-Specific Functions That Create Geometry Values

MySQL provides a set of useful nonstandard functions for creating geometry values. The functions described in this section are MySQL extensions to the OpenGIS specification.

These functions produce geometry objects from either WKB values or geometry objects as arguments. If any argument is not a proper WKB or geometry representation of the proper object type, the return value is

```
NULL.
```

For example, you can insert the geometry return value from `Point()` directly into a `POINT` column:

```
INSERT INTO t1 (pt_col) VALUES(Point(1,2));
- GeometryCollection(g [, g] ...)
```

Geometry Format Conversion Functions Constructs a `GeometryCollection` value from the geometry arguments.

If an argument contains a nonsupported geometry, the return value is `NULL`.

```
- LineString(pt [, pt] ...)
```

Constructs a `LineString` value from a number of `Point` or WKB `Point` arguments. If the number of arguments is less than two, the return value is `NULL`.

```
- MultiLineString(ls [, ls] ...)
```

Constructs a `MultiLineString` value using `LineString` or WKB `LineString` arguments.

```
- MultiPoint(pt [, pt2] ...)
```

Constructs a `MultiPoint` value using `Point` or WKB `Point` arguments.

```
- MultiPolygon(poly [, poly] ...)
```

Constructs a `MultiPolygon` value from a set of `Polygon` or WKB `Polygon` arguments.

```
- Point(x, y)
```

Constructs a `Point` using its coordinates.

```
- Polygon(ls [, ls] ...)
```

Constructs a `Polygon` value from a number of `LineString` or WKB `LineString` arguments. If any argument does not represent a `LinearRing` (that is, not a closed and simple `LineString`), the return value is `NULL`.

### 12.17.6 Geometry Format Conversion Functions

MySQL supports the functions listed in this section for converting geometry values from internal geometry format to WKT or WKB format.

There are also functions to convert a string from WKT or WKB format to internal geometry format. See Section 12.17.3, “Functions That Create Geometry Values from WKT Values”, and Section 12.17.4,“Functions That Create Geometry Values from WKB Values”.

```
- AsBinary(g), AsWKB(g)
```

`ST_AsBinary()`, `ST_AsWKB()`, `AsBinary()`, and `AsWKB()` are synonyms. For more information, see the description of `ST_AsBinary()`.

```
- AsText(g), AsWKT(g)
```

`ST_AsText()`, `ST_AsWKT()`, `AsText()`, and `AsWKT()` are synonyms. For more information, see the description of `ST_AsText()`.

```
- ST_AsBinary(g), ST_AsWKB(g)
```

Converts a value in internal geometry format to its WKB representation and returns the binary result.

The result is `NULL` if the geometry argument is `NULL` or not a syntactically well-formed geometry.

```
SELECT ST_AsBinary(g) FROM geom;
```

`ST_AsBinary()`, `ST_AsWKB()`, `AsBinary()`, and `AsWKB()` are synonyms.

Geometry Property Functions

```
- ST_AsText(g), ST_AsWKT(g)
```

Converts a value in internal geometry format to its WKT representation and returns the string result.

The result is `NULL` if the geometry argument is `NULL` or not a syntactically well-formed geometry.

```
mysql> SET @g = 'LineString(1 1,2 2,3 3)';
mysql> SELECT ST_AsText(ST_GeomFromText(@g));
+--------------------------------+
| ST_AsText(ST_GeomFromText(@g)) |
+--------------------------------+
| LINESTRING(1 1,2 2,3 3)        |
+--------------------------------+
```

`ST_AsText()`, `ST_AsWKT()`, `AsText()`, and `AsWKT()` are synonyms.

### 12.17.7 Geometry Property Functions

Each function that belongs to this group takes a geometry value as its argument and returns some quantitative or qualitative property of the geometry. Some functions restrict their argument type. Such functions return `NULL` if the argument is of an incorrect geometry type. For example, the `ST_Area()`polygon function returns `NULL` if the object type is neither `Polygon` nor `MultiPolygon`.

#### 12.17.7.1 General Geometry Property Functions

The functions listed in this section do not restrict their argument and accept a geometry value of any type.

```
- Dimension(g)
```

`ST_Dimension()` and `Dimension()` are synonyms. For more information, see the description of

```
ST_Dimension().
- Envelope(g)
```

`ST_Envelope()` and `Envelope()` are synonyms. For more information, see the description of

```
ST_Envelope().
- GeometryType(g)
```

`ST_GeometryType()` and `GeometryType()` are synonyms. For more information, see the description

```
of ST_GeometryType().
- IsEmpty(g)
```

`ST_IsEmpty()` and `IsEmpty()` are synonyms. For more information, see the description of

```
ST_IsEmpty().
- IsSimple(g)
```

`ST_IsSimple()` and `IsSimple()` are synonyms. For more information, see the description of

```
ST_IsSimple().
- SRID(g)
```

`ST_SRID()` and `SRID()` are synonyms. For more information, see the description of `ST_SRID()`.

```
- ST_Dimension(g)
```

Geometry Property Functions Returns the inherent dimension of the geometry value g, or `NULL` if the argument is `NULL`. The dimension can be −1, 0, 1, or 2. The meaning of these values is given in Section 11.4.2.2, “Geometry Class”.

```
mysql> SELECT ST_Dimension(ST_GeomFromText('LineString(1 1,2 2)'));
+------------------------------------------------------+
| ST_Dimension(ST_GeomFromText('LineString(1 1,2 2)')) |
+------------------------------------------------------+
|                                                    1 |
+------------------------------------------------------+
```

`ST_Dimension()` and `Dimension()` are synonyms.

```
- ST_Envelope(g)
```

Returns the minimum bounding rectangle (MBR) for the geometry value g, or `NULL` if the argument is`NULL`. The result is returned as a `Polygon` value that is defined by the corner points of the bounding box:

```
POLYGON((MINX MINY, MAXX MINY, MAXX MAXY, MINX MAXY, MINX MINY))
mysql> SELECT ST_AsText(ST_Envelope(ST_GeomFromText('LineString(1 1,2 2)')));
+----------------------------------------------------------------+
| ST_AsText(ST_Envelope(ST_GeomFromText('LineString(1 1,2 2)'))) |
+----------------------------------------------------------------+
| POLYGON((1 1,2 1,2 2,1 2,1 1))                                 |
+----------------------------------------------------------------+
```

`ST_Envelope()` and `Envelope()` are synonyms.

```
- ST_GeometryType(g)
```

Returns a binary string indicating the name of the geometry type of which the geometry instance g is a member, or `NULL` if the argument is `NULL`. The name corresponds to one of the instantiable `Geometry`subclasses.

```
mysql> SELECT ST_GeometryType(ST_GeomFromText('POINT(1 1)'));
+------------------------------------------------+
| ST_GeometryType(ST_GeomFromText('POINT(1 1)')) |
+------------------------------------------------+
| POINT                                          |
+------------------------------------------------+
```

`ST_GeometryType()` and `GeometryType()` are synonyms.

```
- ST_IsEmpty(g)
```

This function is a placeholder that returns 0 for any valid geometry value, 1 for any invalid geometry value, or `NULL` if the argument is `NULL`.

MySQL does not support GIS `EMPTY` values such as `POINT EMPTY`.

`ST_IsEmpty()` and `IsEmpty()` are synonyms.

Geometry Property Functions

```
- ST_IsSimple(g)
```

Returns 1 if the geometry value g has no anomalous geometric points, such as self-intersection or self-tangency. `ST_IsSimple()` returns 0 if the argument is not simple, and `NULL` if the argument is `NULL`.

The descriptions of the instantiable geometric classes given under Section 11.4.2, “The OpenGIS Geometry Model” includes the specific conditions that cause class instances to be classified as not simple.

`ST_IsSimple()` and `IsSimple()` are synonyms.

```
- ST_SRID(g)
```

Returns an integer indicating the spatial reference system ID associated with the geometry value g, or`NULL` if the argument is `NULL`.

```
mysql> SELECT ST_SRID(ST_GeomFromText('LineString(1 1,2 2)',101));
+-----------------------------------------------------+
| ST_SRID(ST_GeomFromText('LineString(1 1,2 2)',101)) |
+-----------------------------------------------------+
|                                                 101 |
+-----------------------------------------------------+
```

`ST_SRID()` and `SRID()` are synonyms.

#### 12.17.7.2 Point Property Functions

A `Point` consists of X and Y coordinates, which may be obtained using the following functions:

```
- ST_X(p)
```

Returns the X-coordinate value for the `Point` object p as a double-precision number.

```
mysql> SELECT ST_X(Point(56.7, 53.34));
+--------------------------+
| ST_X(Point(56.7, 53.34)) |
+--------------------------+
|                     56.7 |
+--------------------------+
```

`ST_X()` and `X()` are synonyms.

```
- ST_Y(p)
```

Returns the Y-coordinate value for the `Point` object p as a double-precision number.

```
mysql> SELECT ST_Y(Point(56.7, 53.34));
+--------------------------+
| ST_Y(Point(56.7, 53.34)) |
+--------------------------+
|                    53.34 |
+--------------------------+
```

`ST_Y()` and `Y()` are synonyms.

```
- X(p)
```

`ST_X()` and `X()` are synonyms. For more information, see the description of `ST_X()`.

```
- Y(p)
```

`ST_Y()` and `Y()` are synonyms. For more information, see the description of `ST_Y()`.

Geometry Property Functions

#### 12.17.7.3 LineString and MultiLineString Property Functions

A `LineString` consists of `Point` values. You can extract particular points of a `LineString`, count the number of points that it contains, or obtain its length.

Some functions in this section also work for `MultiLineString` values.

```
- EndPoint(ls)
```

`ST_EndPoint()` and `EndPoint()` are synonyms. For more information, see the description of

```
ST_EndPoint().
- GLength(ls)
```

Returns a double-precision number indicating the length of the `LineString` or `MultiLineString`value `ls` in its associated spatial reference. The length of a `MultiLineString` value is equal to the sum of the lengths of its elements. If the argument is `NULL` or an empty geometry, the return value is

```
NULL.
mysql> SET @ls = 'LineString(1 1,2 2,3 3)';
mysql> SELECT GLength(GeomFromText(@ls));
+----------------------------+
| GLength(GeomFromText(@ls)) |
+----------------------------+
|         2.8284271247461903 |
+----------------------------+
mysql> SET @mls = 'MultiLineString((1 1,2 2,3 3),(4 4,5 5))';
mysql> SELECT GLength(GeomFromText(@mls));
+-----------------------------+
| GLength(GeomFromText(@mls)) |
+-----------------------------+
|           4.242640687119286 |
+-----------------------------+
```

`GLength()` is a nonstandard name. It corresponds to the OpenGIS `Length()` function. (There is an existing SQL function `Length()` that calculates the length of string values.)

```
- IsClosed(ls)
```

`ST_IsClosed()` and `IsClosed()` are synonyms. For more information, see the description of

```
ST_IsClosed().
- NumPoints(ls)
```

`ST_NumPoints()` and `NumPoints()` are synonyms. For more information, see the description of

```
ST_NumPoints().
- PointN(ls, N)
```

`ST_PointN()` and `PointN()` are synonyms. For more information, see the description of

```
ST_PointN().
- ST_EndPoint(ls)
```

Returns the `Point` that is the endpoint of the `LineString` value `ls`. If the argument is `NULL` or an empty geometry, the return value is `NULL`.

```
mysql> SET @ls = 'LineString(1 1,2 2,3 3)';
mysql> SELECT ST_AsText(ST_EndPoint(ST_GeomFromText(@ls)));
+----------------------------------------------+
```

Geometry Property Functions

```
| ST_AsText(ST_EndPoint(ST_GeomFromText(@ls))) |
+----------------------------------------------+
| POINT(3 3)                                   |
+----------------------------------------------+
```

`ST_EndPoint()` and `EndPoint()` are synonyms.

```
- ST_IsClosed(ls)
```

For a `LineString` value `ls`, `ST_IsClosed()` returns 1 if `ls` is closed (that is, its `ST_StartPoint()`and `ST_EndPoint()` values are the same). If the argument is `NULL` or an empty geometry, the return value is `NULL`.

For a `MultiLineString` value `ls`, `ST_IsClosed()` returns 1 if `ls` is closed (that is, the`ST_StartPoint()` and `ST_EndPoint()` values are the same for each `LineString` in `ls`).

`ST_IsClosed()` returns 0 if `ls` is not closed.

```
mysql> SET @ls1 = 'LineString(1 1,2 2,3 3,2 2)';
mysql> SET @ls2 = 'LineString(1 1,2 2,3 3,1 1)';
mysql> SELECT ST_IsClosed(ST_GeomFromText(@ls1));
+------------------------------------+
| ST_IsClosed(ST_GeomFromText(@ls1)) |
+------------------------------------+
|                                  0 |
+------------------------------------+
mysql> SELECT ST_IsClosed(ST_GeomFromText(@ls2));
+------------------------------------+
| ST_IsClosed(ST_GeomFromText(@ls2)) |
+------------------------------------+
|                                  1 |
+------------------------------------+
mysql> SET @ls3 = 'MultiLineString((1 1,2 2,3 3),(4 4,5 5))';
mysql> SELECT ST_IsClosed(ST_GeomFromText(@ls3));
+------------------------------------+
| ST_IsClosed(ST_GeomFromText(@ls3)) |
+------------------------------------+
|                                  0 |
+------------------------------------+
```

`ST_IsClosed()` and `IsClosed()` are synonyms.

```
- ST_NumPoints(ls)
```

Returns the number of `Point` objects in the `LineString` value `ls`. If the argument is `NULL` or an empty geometry, the return value is `NULL`.

```
mysql> SET @ls = 'LineString(1 1,2 2,3 3)';
mysql> SELECT ST_NumPoints(ST_GeomFromText(@ls));
+------------------------------------+
| ST_NumPoints(ST_GeomFromText(@ls)) |
+------------------------------------+
|                                  3 |
+------------------------------------+
```

`ST_NumPoints()` and `NumPoints()` are synonyms.

Geometry Property Functions

```
- ST_PointN(ls, N)
```

Returns the N-th `Point` in the `Linestring` value `ls`. Points are numbered beginning with 1. If any argument is `NULL` or the geometry argument is an empty geometry, the return value is `NULL`.

```
mysql> SET @ls = 'LineString(1 1,2 2,3 3)';
mysql> SELECT ST_AsText(ST_PointN(ST_GeomFromText(@ls),2));
+----------------------------------------------+
| ST_AsText(ST_PointN(ST_GeomFromText(@ls),2)) |
+----------------------------------------------+
| POINT(2 2)                                   |
+----------------------------------------------+
```

`ST_PointN()` and `PointN()` are synonyms.

```
- ST_StartPoint(ls)
```

Returns the `Point` that is the start point of the `LineString` value `ls`. If the argument is `NULL` or an empty geometry, the return value is `NULL`.

```
mysql> SET @ls = 'LineString(1 1,2 2,3 3)';
mysql> SELECT ST_AsText(ST_StartPoint(ST_GeomFromText(@ls)));
+------------------------------------------------+
| ST_AsText(ST_StartPoint(ST_GeomFromText(@ls))) |
+------------------------------------------------+
| POINT(1 1)                                     |
+------------------------------------------------+
```

`ST_StartPoint()` and `StartPoint()` are synonyms.

```
- StartPoint(ls)
```

`ST_StartPoint()` and `StartPoint()` are synonyms. For more information, see the description of

```
ST_StartPoint().
```

#### 12.17.7.4 Polygon and MultiPolygon Property Functions

Functions in this section return properties of `Polygon` or `MultiPolygon` values.

```
- Area({poly|mpoly})
```

`ST_Area()` and `Area()` are synonyms. For more information, see the description of `ST_Area()`.

```
- Centroid({poly|mpoly})
```

`ST_Centroid()` and `Centroid()` are synonyms. For more information, see the description of

```
ST_Centroid().
- ExteriorRing(poly)
```

`ST_ExteriorRing()` and `ExteriorRing()` are synonyms. For more information, see the description

```
of ST_ExteriorRing().
- InteriorRingN(poly, N)
```

`ST_InteriorRingN()` and `InteriorRingN()` are synonyms. For more information, see the description of `ST_InteriorRingN()`.

```
- NumInteriorRings(poly)
```

Geometry Property Functions`ST_NumInteriorRings()` and `NumInteriorRings()` are synonyms. For more information, see the description of `ST_NumInteriorRings()`.

```
- ST_Area({poly|mpoly})
```

Returns a double-precision number indicating the area of the `Polygon` or `MultiPolygon` argument,as measured in its spatial reference system. For arguments of dimension 0 or 1, the result is 0. If the argument is an empty geometry the return value is 0. If the argument is `NULL` the return value is `NULL`.

```
mysql> SET @poly =
'Polygon((0 0,0 3,3 0,0 0),(1 1,1 2,2 1,1 1))';
mysql> SELECT ST_Area(ST_GeomFromText(@poly));
+---------------------------------+
| ST_Area(ST_GeomFromText(@poly)) |
+---------------------------------+
|                               4 |
+---------------------------------+
mysql> SET @mpoly =
'MultiPolygon(((0 0,0 3,3 3,3 0,0 0),(1 1,1 2,2 2,2 1,1 1)))';
mysql> SELECT ST_Area(ST_GeomFromText(@mpoly));
+----------------------------------+
| ST_Area(ST_GeomFromText(@mpoly)) |
+----------------------------------+
|                                8 |
+----------------------------------+
```

`ST_Area()` and `Area()` are synonyms.

```
- ST_Centroid({poly|mpoly})
```

Returns the mathematical centroid for the `Polygon` or `MultiPolygon` argument as a `Point`. The result is not guaranteed to be on the `MultiPolygon`. If the argument is `NULL` or an empty geometry, the return value is `NULL`.

```
mysql> SET @poly =
ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0),(5 5,7 5,7 7,5 7,5 5))');
mysql> SELECT GeometryType(@poly),ST_AsText(ST_Centroid(@poly));
+---------------------+--------------------------------------------+
| GeometryType(@poly) | ST_AsText(ST_Centroid(@poly))              |
+---------------------+--------------------------------------------+
| POLYGON             | POINT(4.958333333333333 4.958333333333333) |
+---------------------+--------------------------------------------+
```

`ST_Centroid()` and `Centroid()` are synonyms.

```
- ST_ExteriorRing(poly)
```

Returns the exterior ring of the `Polygon` value `poly` as a `LineString`. If the argument is `NULL` or an empty geometry, the return value is `NULL`.

```
mysql> SET @poly =
'Polygon((0 0,0 3,3 3,3 0,0 0),(1 1,1 2,2 2,2 1,1 1))';
mysql> SELECT ST_AsText(ST_ExteriorRing(ST_GeomFromText(@poly)));
+----------------------------------------------------+
| ST_AsText(ST_ExteriorRing(ST_GeomFromText(@poly))) |
+----------------------------------------------------+
| LINESTRING(0 0,0 3,3 3,3 0,0 0)                    |
+----------------------------------------------------+
```

`ST_ExteriorRing()` and `ExteriorRing()` are synonyms.

Geometry Property Functions

```
- ST_InteriorRingN(poly, N)
```

Returns the N-th interior ring for the `Polygon` value `poly` as a `LineString`. Rings are numbered beginning with 1. If the argument is `NULL` or an empty geometry, the return value is `NULL`.

```
mysql> SET @poly =
'Polygon((0 0,0 3,3 3,3 0,0 0),(1 1,1 2,2 2,2 1,1 1))';
mysql> SELECT ST_AsText(ST_InteriorRingN(ST_GeomFromText(@poly),1));
+-------------------------------------------------------+
| ST_AsText(ST_InteriorRingN(ST_GeomFromText(@poly),1)) |
+-------------------------------------------------------+
| LINESTRING(1 1,1 2,2 2,2 1,1 1)                       |
+-------------------------------------------------------+
```

`ST_InteriorRingN()` and `InteriorRingN()` are synonyms.

```
- ST_NumInteriorRings(poly)
```

Returns the number of interior rings in the `Polygon` value `poly`. If the argument is `NULL` or an empty geometry, the return value is `NULL`.

```
mysql> SET @poly =
'Polygon((0 0,0 3,3 3,3 0,0 0),(1 1,1 2,2 2,2 1,1 1))';
mysql> SELECT ST_NumInteriorRings(ST_GeomFromText(@poly));
+---------------------------------------------+
| ST_NumInteriorRings(ST_GeomFromText(@poly)) |
+---------------------------------------------+
|                                           1 |
+---------------------------------------------+
```

`ST_NumInteriorRings()` and `NumInteriorRings()` are synonyms.

#### 12.17.7.5 GeometryCollection Property Functions

These functions return properties of `GeometryCollection` values.

```
- GeometryN(gc, N)
```

`ST_GeometryN()` and `GeometryN()` are synonyms. For more information, see the description of

```
ST_GeometryN().
- NumGeometries(gc)
```

`ST_NumGeometries()` and `NumGeometries()` are synonyms. For more information, see the description of `ST_NumGeometries()`.

```
- ST_GeometryN(gc, N)
```

Returns the N-th geometry in the `GeometryCollection` value `gc`. Geometries are numbered beginning with 1. If any argument is `NULL` or the geometry argument is an empty geometry, the return value is `NULL`.

```
mysql> SET @gc = 'GeometryCollection(Point(1 1),LineString(2 2, 3 3))';
mysql> SELECT ST_AsText(ST_GeometryN(ST_GeomFromText(@gc),1));
+-------------------------------------------------+
| ST_AsText(ST_GeometryN(ST_GeomFromText(@gc),1)) |
+-------------------------------------------------+
| POINT(1 1)                                      |
+-------------------------------------------------+
```

`ST_GeometryN()` and `GeometryN()` are synonyms.

Spatial Operator Functions

```
- ST_NumGeometries(gc)
```

Returns the number of geometries in the `GeometryCollection` value `gc`. If the argument is `NULL` or an empty geometry, the return value is `NULL`.

```
mysql> SET @gc = 'GeometryCollection(Point(1 1),LineString(2 2, 3 3))';
mysql> SELECT ST_NumGeometries(ST_GeomFromText(@gc));
+----------------------------------------+
| ST_NumGeometries(ST_GeomFromText(@gc)) |
+----------------------------------------+
|                                      2 |
+----------------------------------------+
```

`ST_NumGeometries()` and `NumGeometries()` are synonyms.

### 12.17.8 Spatial Operator Functions

OpenGIS proposes a number of functions that can produce geometries. They are designed to implement spatial operators.

In addition, Section 12.17.7, “Geometry Property Functions”, discusses several functions that construct new geometries from existing ones. See that section for descriptions of these functions:

```
- ST_Envelope(g)
- StartPoint(ls)
- ST_EndPoint(ls)
- ST_PointN(ls, N)
- ST_ExteriorRing(poly)
- ST_InteriorRingN(poly, N)
- ST_GeometryN(gc, N)
```

These spatial operator functions are available:

```
- Buffer(g, d)
```

`ST_Buffer()` and `Buffer()` are synonyms. For more information, see the description of

```
ST_Buffer().
- ST_Buffer(g, d)
```

Returns a geometry that represents all points whose distance from the geometry value g is less than or equal to a distance of d, or `NULL` if any argument is `NULL`.

`ST_Buffer()` supports negative distances for polygons, multipolygons, and geometry collections containing polygons or multipolygons. For point, multipoint, linestring, multilinestring, and geometry collections not containing any polygons or multipolygons, `ST_Buffer()` with a negative distance returns

```
NULL.
```

`ST_Buffer()` and `Buffer()` are synonyms.

```
- ST_Difference(g1, g2)
```

Returns a geometry that represents the point set difference of the geometry values `g1` and `g2`. If any argument is `NULL`, the return value is `NULL`.

Functions That Test Spatial Relations Between Geometry Objects

```
mysql> SET @g1 = Point(1,1), @g2 = Point(2,2);
mysql> SELECT ST_AsText(ST_Difference(@g1, @g2));
+------------------------------------+
| ST_AsText(ST_Difference(@g1, @g2)) |
+------------------------------------+
| POINT(1 1)                         |
+------------------------------------+
- ST_Intersection(g1, g2)
```

Returns a geometry that represents the point set intersection of the geometry values `g1` and `g2`. If any argument is `NULL`, the return value is `NULL`.

```
mysql> SET @g1 = ST_GeomFromText('LineString(1 1, 3 3)');
mysql> SET @g2 = ST_GeomFromText('LineString(1 3, 3 1)');
mysql> SELECT ST_AsText(ST_Intersection(@g1, @g2));
+--------------------------------------+
| ST_AsText(ST_Intersection(@g1, @g2)) |
+--------------------------------------+
| POINT(2 2)                           |
+--------------------------------------+
- ST_SymDifference(g1, g2)
```

Returns a geometry that represents the point set symmetric difference of the geometry values `g1` and`g2`, which is defined as:

```
g1 symdifference g2 := (g1 union g2) difference (g1 intersection g2)
```

Or, in function call notation:

```
ST_SymDifference(g1, g2) = ST_Difference(ST_Union(g1, g2), ST_Intersection(g1, g2))
```

If any argument is `NULL`, the return value is `NULL`.

```
mysql> SET @g1 = Point(1,1), @g2 = Point(2,2);
mysql> SELECT ST_AsText(ST_SymDifference(@g1, @g2));
+---------------------------------------+
| ST_AsText(ST_SymDifference(@g1, @g2)) |
+---------------------------------------+
| MULTIPOINT(1 1,2 2)                   |
+---------------------------------------+
- ST_Union(g1, g2)
```

Returns a geometry that represents the point set union of the geometry values `g1` and `g2`. If any argument is `NULL`, the return value is `NULL`.

```
mysql> SET @g1 = ST_GeomFromText('LineString(1 1, 3 3)');
mysql> SET @g2 = ST_GeomFromText('LineString(1 3, 3 1)');
mysql> SELECT ST_AsText(ST_Union(@g1, @g2));
+--------------------------------------+
| ST_AsText(ST_Union(@g1, @g2))        |
+--------------------------------------+
| MULTILINESTRING((1 1,3 3),(3 1,1 3)) |
+--------------------------------------+
```

### 12.17.9 Functions That Test Spatial Relations Between Geometry Objects

The functions described in this section take two geometries as arguments and return a qualitative or quantitative relation between them.

Functions That Test Spatial Relations Between Geometry Objects MySQL implements two sets of functions using function names defined by the OpenGIS specification. One set tests the relationship between two geometry values using precise object shapes, the other set uses object minimum bounding rectangles (MBRs).

There is also a MySQL-specific set of MBR-based functions available to test the relationship between two geometry values.

#### 12.17.9.1 Spatial Relation Functions That Use Object Shapes

The OpenGIS specification defines the following functions to test the relationship between two geometry values `g1` and `g2`, using precise object shapes. The return values 1 and 0 indicate true and false,respectively, except for `ST_Distance()`, which returns distance values.

```
- ST_Contains(g1, g2)
```

Returns 1 or 0 to indicate whether `g1` completely contains `g2`. This tests the opposite relationship as

```
ST_Within().
- Crosses(g1, g2)
```

`ST_Crosses()` and `Crosses()` are synonyms. For more information, see the description of

```
ST_Crosses().
- ST_Crosses(g1, g2)
```

The term spatially crosses denotes a spatial relation between two given geometries that has the following properties:

- The two geometries intersect.
- Their intersection results in a geometry that has a dimension that is one less than the maximum

dimension of the two given geometries.

- Their intersection is not equal to either of the two given geometries.

This function returns 1 or 0 to indicate whether `g1` spatially crosses `g2`. If `g1` is a `Polygon` or a`MultiPolygon`, or if `g2` is a `Point` or a `MultiPoint`, the return value is `NULL`.

`ST_Crosses()` and `Crosses()` are synonyms.

```
- ST_Disjoint(g1, g2)
```

Returns 1 or 0 to indicate whether `g1` is spatially disjoint from (does not intersect) `g2`.

```
- ST_Distance(g1, g2)
```

Returns the distance between `g1` and `g2`.

```
mysql> SET @g1 = Point(1,1);
mysql> SET @g2 = Point(2,2);
mysql> SELECT ST_Distance(@g1, @g2);
+-----------------------+
| ST_Distance(@g1, @g2) |
+-----------------------+
|    1.4142135623730951 |
+-----------------------+
- ST_Equals(g1, g2)
```

Returns 1 or 0 to indicate whether `g1` is spatially equal to `g2`.

Functions That Test Spatial Relations Between Geometry Objects

```
mysql> SET @g1 = Point(1,1), @g2 = Point(2,2);
mysql> SELECT ST_Equals(@g1, @g1), ST_Equals(@g1, @g2);
+---------------------+---------------------+
| ST_Equals(@g1, @g1) | ST_Equals(@g1, @g2) |
+---------------------+---------------------+
|                   1 |                   0 |
+---------------------+---------------------+
- ST_Intersects(g1, g2)
```

Returns 1 or 0 to indicate whether `g1` spatially intersects `g2`.

```
- ST_Overlaps(g1, g2)
```

Two geometries spatially overlap if they intersect and their intersection results in a geometry of the same dimension but not equal to either of the given geometries.

This function returns 1 or 0 to indicate whether `g1` spatially overlaps `g2`.

```
- ST_Touches(g1, g2)
```

Two geometries spatially touch if their interiors do not intersect, but the boundary of one of the geometries intersects either the boundary or the interior of the other.

This function returns 1 or 0 to indicate whether `g1` spatially touches `g2`.

`ST_Touches()` and `Touches()` are synonyms.

```
- ST_Within(g1, g2)
```

Returns 1 or 0 to indicate whether `g1` is spatially within `g2`. This tests the opposite relationship as

```
ST_Contains().
- Touches(g1, g2)
```

`ST_Touches()` and `Touches()` are synonyms. For more information, see the description of

```
ST_Touches().
```

#### 12.17.9.2 Spatial Relation Functions That Use Minimum Bounding Rectangles

MySQL provides several MySQL-specific functions that test the relationship between minimum bounding rectangles (MBRs) of two geometries `g1` and `g2`. The return values 1 and 0 indicate true and false,respectively.

A corresponding set of MBR functions defined according to the OpenGIS specification is described later in this section.

```
- MBRContains(g1, g2)
```

Returns 1 or 0 to indicate whether the minimum bounding rectangle of `g1` contains the minimum bounding rectangle of `g2`. This tests the opposite relationship as `MBRWithin()`.

```
mysql> SET @g1 = ST_GeomFromText('Polygon((0 0,0 3,3 3,3 0,0 0))');
mysql> SET @g2 = ST_GeomFromText('Point(1 1)');
mysql> SELECT MBRContains(@g1,@g2), MBRWithin(@g2,@g1);
+----------------------+--------------------+
| MBRContains(@g1,@g2) | MBRWithin(@g2,@g1) |
+----------------------+--------------------+
|                    1 |                  1 |
+----------------------+--------------------+
```

Functions That Test Spatial Relations Between Geometry Objects`MBRContains()` and `Contains()` are synonyms.

```
- MBRDisjoint(g1, g2)
```

Returns 1 or 0 to indicate whether the minimum bounding rectangles of the two geometries `g1` and `g2`are disjoint (do not intersect).

`MBRDisjoint()` and `Disjoint()` are synonyms.

```
- MBREqual(g1, g2)
```

Returns 1 or 0 to indicate whether the minimum bounding rectangles of the two geometries `g1` and `g2`are the same.

```
- MBRIntersects(g1, g2)
```

Returns 1 or 0 to indicate whether the minimum bounding rectangles of the two geometries `g1` and `g2`intersect.

`MBRIntersects()` and `Intersects()` are synonyms.

```
- MBROverlaps(g1, g2)
```

Two geometries spatially overlap if they intersect and their intersection results in a geometry of the same dimension but not equal to either of the given geometries.

This function returns 1 or 0 to indicate whether the minimum bounding rectangles of the two geometries`g1` and `g2` overlap.

`MBROverlaps()` and `Overlaps()` are synonyms.

```
- MBRTouches(g1, g2)
```

Two geometries spatially touch if their interiors do not intersect, but the boundary of one of the geometries intersects either the boundary or the interior of the other.

This function returns 1 or 0 to indicate whether the minimum bounding rectangles of the two geometries`g1` and `g2` touch.

```
- MBRWithin(g1, g2)
```

Returns 1 or 0 to indicate whether the minimum bounding rectangle of `g1` is within the minimum bounding rectangle of `g2`. This tests the opposite relationship as `MBRContains()`.

```
mysql> SET @g1 = ST_GeomFromText('Polygon((0 0,0 3,3 3,3 0,0 0))');
mysql> SET @g2 = ST_GeomFromText('Polygon((0 0,0 5,5 5,5 0,0 0))');
mysql> SELECT MBRWithin(@g1,@g2), MBRWithin(@g2,@g1);
+--------------------+--------------------+
| MBRWithin(@g1,@g2) | MBRWithin(@g2,@g1) |
+--------------------+--------------------+
|                  1 |                  0 |
+--------------------+--------------------+
```

`MBRWithin()` and `Within()` are synonyms.

The OpenGIS specification defines the following functions that test the relationship between two geometry values `g1` and `g2`. The MySQL implementation uses minimum bounding rectangles, so these functions return the same result as the corresponding MBR-based functions described earlier in this section. The return values 1 and 0 indicate true and false, respectively.

Functions Used with Global Transaction IDs

```
- Contains(g1, g2)
```

`MBRContains()` and `Contains()` are synonyms. For more information, see the description of

```
MBRContains().
- Disjoint(g1, g2)
```

`MBRDisjoint()` and `Disjoint()` are synonyms. For more information, see the description of

```
MBRDisjoint().
- Equals(g1, g2)
```

Returns 1 or 0 to indicate whether `g1` is spatially equal to `g2`.

```
- Intersects(g1, g2)
```

`MBRIntersects()` and `Intersects()` are synonyms. For more information, see the description of

```
MBRIntersects().
- Overlaps(g1, g2)
```

`MBROverlaps()` and `Overlaps()` are synonyms. For more information, see the description of

```
MBROverlaps().
- Within(g1, g2)
```

`MBRWithin()` and `Within()` are synonyms. For more information, see the description of

```
MBRWithin().
```

## 12.18 Functions Used with Global Transaction IDs

The functions described in this section are used with GTID-based replication. It is important to keep in mind that all of these functions take string representations of GTID sets as arguments—as such, the GTID sets must always be quoted when used with them.

The union of two GTID sets is simply their representations as strings, joined together with an interposed comma. In other words, you can define a very simple function for obtaining the union of two GTID sets,similar to that created here:

```
CREATE FUNCTION GTID_UNION(g1 TEXT, g2 TEXT)
RETURNS TEXT DETERMINISTIC
RETURN CONCAT(g1,',',g2);
```

For more information about GTIDs and how these GTID functions are used in practice, see Section 17.1.3,“Replication with Global Transaction Identifiers”.

Table 12.22 GTID Functions Name Description Deprecated`GTID_SUBSET()` Return true if all GTIDs in subset are also in set; otherwise false.

`GTID_SUBTRACT()` Return all GTIDs in set that are not in subset.

`SQL_THREAD_WAIT_AFTER_GTIDS()`Obsolete. Use Yes

```
WAIT_FOR_EXECUTED_GTID_SET().
WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS()Use
WAIT_FOR_EXECUTED_GTID_SET().
```

Functions Used with Global Transaction IDs

```
- GTID_SUBSET(subset,set)
```

Given two sets of global transaction IDs `subset` and `set`, returns true (1) if all GTIDs in `subset` are also in `set`. Returns false (0) otherwise.

The GTID sets used with this function are represented as strings, as shown in the following examples:

```
mysql> SELECT GTID_SUBSET('3E11FA47-71CA-11E1-9E33-C80AA9429562:23',
->     '3E11FA47-71CA-11E1-9E33-C80AA9429562:21-57')\G
*************************** 1. row ***************************
GTID_SUBSET('3E11FA47-71CA-11E1-9E33-C80AA9429562:23',
'3E11FA47-71CA-11E1-9E33-C80AA9429562:21-57'): 1
1 row in set (0.00 sec)
mysql> SELECT GTID_SUBSET('3E11FA47-71CA-11E1-9E33-C80AA9429562:23-25',
->     '3E11FA47-71CA-11E1-9E33-C80AA9429562:21-57')\G
*************************** 1. row ***************************
GTID_SUBSET('3E11FA47-71CA-11E1-9E33-C80AA9429562:23-25',
'3E11FA47-71CA-11E1-9E33-C80AA9429562:21-57'): 1
1 row in set (0.00 sec)
mysql> SELECT GTID_SUBSET('3E11FA47-71CA-11E1-9E33-C80AA9429562:20-25',
->     '3E11FA47-71CA-11E1-9E33-C80AA9429562:21-57')\G
*************************** 1. row ***************************
GTID_SUBSET('3E11FA47-71CA-11E1-9E33-C80AA9429562:20-25',
'3E11FA47-71CA-11E1-9E33-C80AA9429562:21-57'): 0
1 row in set (0.00 sec)
- GTID_SUBTRACT(set,subset)
```

Given two sets of global transaction IDs `subset` and `set`, returns only those GTIDs from `set` that are not in `subset`.

All GTID sets used with this function are represented as strings and must be quoted, as shown in these examples:

```
mysql> SELECT GTID_SUBTRACT('3E11FA47-71CA-11E1-9E33-C80AA9429562:21-57',
->     '3E11FA47-71CA-11E1-9E33-C80AA9429562:21')\G
*************************** 1. row ***************************
GTID_SUBTRACT('3E11FA47-71CA-11E1-9E33-C80AA9429562:21-57',
'3E11FA47-71CA-11E1-9E33-C80AA9429562:21'): 3e11fa47-71ca-11e1-9e33-c80aa9429562:22-57
1 row in set (0.00 sec)
mysql> SELECT GTID_SUBTRACT('3E11FA47-71CA-11E1-9E33-C80AA9429562:21-57',
->     '3E11FA47-71CA-11E1-9E33-C80AA9429562:20-25')\G
*************************** 1. row ***************************
GTID_SUBTRACT('3E11FA47-71CA-11E1-9E33-C80AA9429562:21-57',
'3E11FA47-71CA-11E1-9E33-C80AA9429562:20-25'): 3e11fa47-71ca-11e1-9e33-c80aa9429562:26-57
1 row in set (0.00 sec)
mysql> SELECT GTID_SUBTRACT('3E11FA47-71CA-11E1-9E33-C80AA9429562:21-57',
->     '3E11FA47-71CA-11E1-9E33-C80AA9429562:23-24')\G
*************************** 1. row ***************************
GTID_SUBTRACT('3E11FA47-71CA-11E1-9E33-C80AA9429562:21-57',
'3E11FA47-71CA-11E1-9E33-C80AA9429562:23-24'): 3e11fa47-71ca-11e1-9e33-c80aa9429562:21-22:25-57
1 row in set (0.01 sec)
- SQL_THREAD_WAIT_AFTER_GTIDS(gtid_set[, timeout])
```

`SQL_THREAD_WAIT_AFTER_GTIDS()` was added in MySQL 5.6.5, and replaced by`WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS()` in MySQL 5.6.9. (Bug #14775984)For more information, see Section 17.1.3, “Replication with Global Transaction Identifiers”.

Aggregate Functions

```
- WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS(gtid_set[, timeout])
```

Wait until the replica SQL thread has executed all of the transactions whose global transaction identifiers are contained in `gtid_set` (see Section 17.1.3.1, “GTID Concepts”, for a definition of “GTID sets”), or until `timeout` seconds have elapsed, whichever occurs first. `timeout` is optional; the default timeout is 0 seconds, in which case the source simply waits until all of the transactions in the GTID set have been executed.

Prior to MySQL 5.6.9, `WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS()` was named`SQL_THREAD_WAIT_AFTER_GTIDS()`. (Bug #14775984)For more information, see Section 17.1.3, “Replication with Global Transaction Identifiers”.

GTID sets used with this function are represented as strings and so must be quoted as shown in the following example:

```
mysql> SELECT WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS('3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5');
-> 5
```

The return value is the number of transactional events that were executed. Prior to MySQL 5.6.8, this function behaved unpredictably if no timeout was set and it was invoked while GTID-based replication was not active; in MySQL 5.6.8 and later, the function returns `NULL` whenever `gtid_mode` is `OFF`. (Bug#14640065)

## 12.19 Aggregate Functions

Aggregate functions operate on sets of values. They are often used with a `GROUP BY` clause to group values into subsets.

### 12.19.1 Aggregate Function Descriptions

This section describes aggregate functions that operate on sets of values. They are often used with a`GROUP BY` clause to group values into subsets.

Table 12.23 Aggregate Functions Name Description`AVG()` Return the average value of the argument`BIT_AND()` Return bitwise AND`BIT_OR()` Return bitwise OR`BIT_XOR()` Return bitwise XOR`COUNT()` Return a count of the number of rows returned`COUNT(DISTINCT)` Return the count of a number of different values`GROUP_CONCAT()` Return a concatenated string`MAX()` Return the maximum value`MIN()` Return the minimum value`STD()` Return the population standard deviation`STDDEV()` Return the population standard deviation`STDDEV_POP()` Return the population standard deviation`STDDEV_SAMP()` Return the sample standard deviation Aggregate Function Descriptions Name Description`SUM()` Return the sum`VAR_POP()` Return the population standard variance`VAR_SAMP()` Return the sample variance`VARIANCE()` Return the population standard variance Unless otherwise stated, aggregate functions ignore `NULL` values.

If you use an aggregate function in a statement containing no `GROUP BY` clause, it is equivalent to grouping on all rows. For more information, see Section 12.19.3, “MySQL Handling of GROUP BY”.

For numeric arguments, the variance and standard deviation functions return a `DOUBLE` value. The `SUM()`and `AVG()` functions return a `DECIMAL` value for exact-value arguments (integer or `DECIMAL`), and a`DOUBLE` value for approximate-value arguments (`FLOAT` or `DOUBLE`).

The `SUM()` and `AVG()` aggregate functions do not work with temporal values. (They convert the values to numbers, losing everything after the first nonnumeric character.) To work around this problem, convert to numeric units, perform the aggregate operation, and convert back to a temporal value. Examples:

```
SELECT SEC_TO_TIME(SUM(TIME_TO_SEC(time_col))) FROM tbl_name;
SELECT FROM_DAYS(SUM(TO_DAYS(date_col))) FROM tbl_name;
```

Functions such as `SUM()` or `AVG()` that expect a numeric argument cast the argument to a number if necessary. For `SET` or `ENUM` values, the cast operation causes the underlying numeric value to be used.

The `BIT_AND()`, `BIT_OR()`, and `BIT_XOR()` aggregate functions perform bit operations. They require`BIGINT` (64-bit integer) arguments and return `BIGINT` values. Arguments of other types are converted to`BIGINT` and truncation might occur.

```
- AVG([DISTINCT] expr)
```

Returns the average value of `expr`. The `DISTINCT` option can be used to return the average of the distinct values of `expr`.

If there are no matching rows, `AVG()` returns `NULL`.

```
mysql> SELECT student_name, AVG(test_score)
FROM student
GROUP BY student_name;
- BIT_AND(expr)
```

Returns the bitwise `AND` of all bits in `expr`. The calculation is performed with 64-bit (`BIGINT`) precision.

If there are no matching rows, `BIT_AND()` returns a neutral value (all bits set to 1).

```
- BIT_OR(expr)
```

Returns the bitwise `OR` of all bits in `expr`. The calculation is performed with 64-bit (`BIGINT`) precision.

If there are no matching rows, `BIT_OR()` returns a neutral value (all bits set to 0).

```
- BIT_XOR(expr)
```

Returns the bitwise `XOR` of all bits in `expr`. The calculation is performed with 64-bit (`BIGINT`) precision.

If there are no matching rows, `BIT_XOR()` returns a neutral value (all bits set to 0).

Aggregate Function Descriptions

```
- COUNT(expr)
```

Returns a count of the number of non-`NULL` values of `expr` in the rows retrieved by a `SELECT`statement. The result is a `BIGINT` value.

If there are no matching rows, `COUNT()` returns 0.

```
mysql> SELECT student.student_name,COUNT(*)
FROM student,course
WHERE student.student_id=course.student_id
GROUP BY student_name;
```

`COUNT(*)` is somewhat different in that it returns a count of the number of rows retrieved, whether or not they contain `NULL` values.

For transactional storage engines such as `InnoDB`, storing an exact row count is problematic. Multiple transactions may be occurring at the same time, each of which may affect the count.

`InnoDB` does not keep an internal count of rows in a table because concurrent transactions might “see”different numbers of rows at the same time. Consequently, `SELECT COUNT(*)` statements only count rows visible to the current transaction.

To process a `SELECT COUNT(*)` statement, `InnoDB` scans an index of the table, which takes some time if the index is not entirely in the buffer pool. For a faster count, create a counter table and let your application update it according to the inserts and deletes it does. However, this method may not scale well in situations where thousands of concurrent transactions are initiating updates to the same counter table. If an approximate row count is sufficient, use `SHOW TABLE STATUS`.

`InnoDB` handles `SELECT COUNT(*)` and `SELECT COUNT(1)` operations in the same way. There is no performance difference.

For `MyISAM` tables, `COUNT(*)` is optimized to return very quickly if the `SELECT` retrieves from one table,no other columns are retrieved, and there is no `WHERE` clause. For example:

```
mysql> SELECT COUNT(*) FROM student;
```

This optimization only applies to `MyISAM` tables, because an exact row count is stored for this storage engine and can be accessed very quickly. `COUNT(1)` is only subject to the same optimization if the first column is defined as `NOT NULL`.

```
- COUNT(DISTINCT expr,[expr...])
```

Returns a count of the number of rows with different non-`NULL` `expr` values.

If there are no matching rows, `COUNT(DISTINCT)` returns 0.

```
mysql> SELECT COUNT(DISTINCT results) FROM student;
```

In MySQL, you can obtain the number of distinct expression combinations that do not contain `NULL` by giving a list of expressions. In standard SQL, you would have to do a concatenation of all expressions inside `COUNT(DISTINCT ...)`.

```
- GROUP_CONCAT(expr)
```

This function returns a string result with the concatenated non-`NULL` values from a group. It returns `NULL`if there are no non-`NULL` values. The full syntax is as follows:

```
GROUP_CONCAT([DISTINCT] expr [,expr ...]
[ORDER BY {unsigned_integer | col_name | expr}
```

Aggregate Function Descriptions

```
[ASC | DESC] [,col_name ...]]
[SEPARATOR str_val])
mysql> SELECT student_name,
GROUP_CONCAT(test_score)
FROM student
GROUP BY student_name;
```

Or:

```
mysql> SELECT student_name,
GROUP_CONCAT(DISTINCT test_score
ORDER BY test_score DESC SEPARATOR ' ')
FROM student
GROUP BY student_name;
```

In MySQL, you can get the concatenated values of expression combinations. To eliminate duplicate values, use the `DISTINCT` clause. To sort values in the result, use the `ORDER BY` clause. To sort in reverse order, add the `DESC` (descending) keyword to the name of the column you are sorting by in the `ORDER BY` clause. The default is ascending order; this may be specified explicitly using the`ASC` keyword. The default separator between values in a group is comma (,). To specify a separator explicitly, use `SEPARATOR` followed by the string literal value that should be inserted between group values. To eliminate the separator altogether, specify `SEPARATOR ''`.

The result is truncated to the maximum length that is given by the `group_concat_max_len` system variable, which has a default value of 1024. The value can be set higher, although the effective maximum length of the return value is constrained by the value of `max_allowed_packet`. The syntax to change the value of `group_concat_max_len` at runtime is as follows, where `val` is an unsigned integer:

```
SET [GLOBAL | SESSION] group_concat_max_len = val;
```

The return value is a nonbinary or binary string, depending on whether the arguments are nonbinary or binary strings. The result type is `TEXT` or `BLOB` unless `group_concat_max_len` is less than or equal to 512, in which case the result type is `VARCHAR` or `VARBINARY`.

If `GROUP_CONCAT()` is invoked from within the `mysql` client, binary string results display using hexadecimal notation, depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

See also `CONCAT()` and `CONCAT_WS()`: Section 12.8, “String Functions and Operators”.

```
- MAX([DISTINCT] expr)
```

Returns the maximum value of `expr`. `MAX()` may take a string argument; in such cases, it returns the maximum string value. See Section 8.3.1, “How MySQL Uses Indexes”. The `DISTINCT` keyword can be used to find the maximum of the distinct values of `expr`, however, this produces the same result as omitting `DISTINCT`.

If there are no matching rows, `MAX()` returns `NULL`.

```
mysql> SELECT student_name, MIN(test_score), MAX(test_score)
FROM student
GROUP BY student_name;
```

For `MAX()`, MySQL currently compares `ENUM` and `SET` columns by their string value rather than by the string's relative position in the set. This differs from how `ORDER BY` compares them.

Aggregate Function Descriptions

```
- MIN([DISTINCT] expr)
```

Returns the minimum value of `expr`. `MIN()` may take a string argument; in such cases, it returns the minimum string value. See Section 8.3.1, “How MySQL Uses Indexes”. The `DISTINCT` keyword can be used to find the minimum of the distinct values of `expr`, however, this produces the same result as omitting `DISTINCT`.

If there are no matching rows, `MIN()` returns `NULL`.

```
mysql> SELECT student_name, MIN(test_score), MAX(test_score)
FROM student
GROUP BY student_name;
```

For `MIN()`, MySQL currently compares `ENUM` and `SET` columns by their string value rather than by the string's relative position in the set. This differs from how `ORDER BY` compares them.

```
- STD(expr)
```

Returns the population standard deviation of `expr`. `STD()` is a synonym for the standard SQL function`STDDEV_POP()`, provided as a MySQL extension.

If there are no matching rows, `STD()` returns `NULL`.

```
- STDDEV(expr)
```

Returns the population standard deviation of `expr`. `STDDEV()` is a synonym for the standard SQL function `STDDEV_POP()`, provided for compatibility with Oracle.

If there are no matching rows, `STDDEV()` returns `NULL`.

```
- STDDEV_POP(expr)
```

Returns the population standard deviation of `expr` (the square root of `VAR_POP()`). You can also use`STD()` or `STDDEV()`, which are equivalent but not standard SQL.

If there are no matching rows, `STDDEV_POP()` returns `NULL`.

```
- STDDEV_SAMP(expr)
```

Returns the sample standard deviation of `expr` (the square root of `VAR_SAMP()`.

If there are no matching rows, `STDDEV_SAMP()` returns `NULL`.

```
- SUM([DISTINCT] expr)
```

Returns the sum of `expr`. If the return set has no rows, `SUM()` returns `NULL`. The `DISTINCT` keyword can be used to sum only the distinct values of `expr`.

If there are no matching rows, `SUM()` returns `NULL`.

```
- VAR_POP(expr)
```

Returns the population standard variance of `expr`. It considers rows as the whole population, not as a sample, so it has the number of rows as the denominator. You can also use `VARIANCE()`, which is equivalent but is not standard SQL.

If there are no matching rows, `VAR_POP()` returns `NULL`.

```
- VAR_SAMP(expr)
```

GROUP BY Modifiers Returns the sample variance of `expr`. That is, the denominator is the number of rows minus one.

If there are no matching rows, `VAR_SAMP()` returns `NULL`.

```
- VARIANCE(expr)
```

Returns the population standard variance of `expr`. `VARIANCE()` is a synonym for the standard SQL function `VAR_POP()`, provided as a MySQL extension.

If there are no matching rows, `VARIANCE()` returns `NULL`.

### 12.19.2 GROUP BY Modifiers

The `GROUP BY` clause permits a `WITH ROLLUP` modifier that causes summary output to include extra rows that represent higher-level (that is, super-aggregate) summary operations. `ROLLUP` thus enables you to answer questions at multiple levels of analysis with a single query. For example, `ROLLUP` can be used to provide support for OLAP (Online Analytical Processing) operations.

Suppose that a `sales` table has `year`, `country`, `product`, and `profit` columns for recording sales profitability:

```
CREATE TABLE sales
(
year    INT,
country VARCHAR(20),
product VARCHAR(32),
profit  INT
);
```

To summarize table contents per year, use a simple `GROUP BY` like this:

```
mysql> SELECT year, SUM(profit) AS profit
FROM sales
GROUP BY year;
+------+--------+
| year | profit |
+------+--------+
| 2000 |   4525 |
| 2001 |   3010 |
+------+--------+
```

The output shows the total (aggregate) profit for each year. To also determine the total profit summed over all years, you must add up the individual values yourself or run an additional query. Or you can use`ROLLUP`, which provides both levels of analysis with a single query. Adding a `WITH ROLLUP` modifier to the`GROUP BY` clause causes the query to produce another (super-aggregate) row that shows the grand total over all year values:

```
mysql> SELECT year, SUM(profit) AS profit
FROM sales
GROUP BY year WITH ROLLUP;
+------+--------+
| year | profit |
+------+--------+
| 2000 |   4525 |
| 2001 |   3010 |
| NULL |   7535 |
+------+--------+
```

The `NULL` value in the `year` column identifies the grand total super-aggregate line.

GROUP BY Modifiers`ROLLUP` has a more complex effect when there are multiple `GROUP BY` columns. In this case, each time there is a change in value in any but the last grouping column, the query produces an extra super-aggregate summary row.

For example, without `ROLLUP`, a summary of the `sales` table based on `year`, `country`, and `product`might look like this, where the output indicates summary values only at the year/country/product level of analysis:

```
mysql> SELECT year, country, product, SUM(profit) AS profit
FROM sales
GROUP BY year, country, product;
+------+---------+------------+--------+
| year | country | product    | profit |
+------+---------+------------+--------+
| 2000 | Finland | Computer   |   1500 |
| 2000 | Finland | Phone      |    100 |
| 2000 | India   | Calculator |    150 |
| 2000 | India   | Computer   |   1200 |
| 2000 | USA     | Calculator |     75 |
| 2000 | USA     | Computer   |   1500 |
| 2001 | Finland | Phone      |     10 |
| 2001 | USA     | Calculator |     50 |
| 2001 | USA     | Computer   |   2700 |
| 2001 | USA     | TV         |    250 |
+------+---------+------------+--------+
```

With `ROLLUP` added, the query produces several extra rows:

```
mysql> SELECT year, country, product, SUM(profit) AS profit
FROM sales
GROUP BY year, country, product WITH ROLLUP;
+------+---------+------------+--------+
| year | country | product    | profit |
+------+---------+------------+--------+
| 2000 | Finland | Computer   |   1500 |
| 2000 | Finland | Phone      |    100 |
| 2000 | Finland | NULL       |   1600 |
| 2000 | India   | Calculator |    150 |
| 2000 | India   | Computer   |   1200 |
| 2000 | India   | NULL       |   1350 |
| 2000 | USA     | Calculator |     75 |
| 2000 | USA     | Computer   |   1500 |
| 2000 | USA     | NULL       |   1575 |
| 2000 | NULL    | NULL       |   4525 |
| 2001 | Finland | Phone      |     10 |
| 2001 | Finland | NULL       |     10 |
| 2001 | USA     | Calculator |     50 |
| 2001 | USA     | Computer   |   2700 |
| 2001 | USA     | TV         |    250 |
| 2001 | USA     | NULL       |   3000 |
| 2001 | NULL    | NULL       |   3010 |
| NULL | NULL    | NULL       |   7535 |
+------+---------+------------+--------+
```

Now the output includes summary information at four levels of analysis, not just one:

- Following each set of product rows for a given year and country, an extra super-aggregate summary row

appears showing the total for all products. These rows have the `product` column set to `NULL`.

- Following each set of rows for a given year, an extra super-aggregate summary row appears showing

the total for all countries and products. These rows have the `country` and `products` columns set to

```
NULL.
```

GROUP BY Modifiers

- Finally, following all other rows, an extra super-aggregate summary row appears showing the grand total

for all years, countries, and products. This row has the `year`, `country`, and `products` columns set to

```
NULL.
```

The `NULL` indicators in each super-aggregate row are produced when the row is sent to the client. The server looks at the columns named in the `GROUP BY` clause following the leftmost one that has changed value. For any column in the result set with a name that matches any of those names, its value is set to`NULL`. (If you specify grouping columns by column position, the server identifies which columns to set to`NULL` by position.)Because the `NULL` values in the super-aggregate rows are placed into the result set at such a late stage in query processing, you can test them as `NULL` values only in the select list or `HAVING` clause. You cannot test them as `NULL` values in join conditions or the `WHERE` clause to determine which rows to select. For example, you cannot add `WHERE product IS NULL` to the query to eliminate from the output all but the super-aggregate rows.

The `NULL` values do appear as `NULL` on the client side and can be tested as such using any MySQL client programming interface. However, at this point, you cannot distinguish whether a `NULL` represents a regular grouped value or a super-aggregate value.

> Other Considerations When using ROLLUP

The following discussion lists some behaviors specific to the MySQL implementation of `ROLLUP`.

When you use `ROLLUP`, you cannot also use an `ORDER BY` clause to sort the results. In other words,`ROLLUP` and `ORDER BY` are mutually exclusive in MySQL. However, you still have some control over sort order. `GROUP BY` in MySQL implicitly sorts results by default (in the absence of `ASC` or `DESC` designators).

However, implicit `GROUP BY` sorting in MySQL is deprecated. To achieve a specific sort order of grouped results:

- Use explicit `ASC` and `DESC` keywords with columns named in the `GROUP BY` list to specify sort order for

individual columns. In this case, the super-aggregate summary rows added by `ROLLUP` still appear after the rows from which they are calculated, regardless of the sort order.

- To work around the restriction that prevents using `ROLLUP` with `ORDER BY`, generate the grouped result

set as a derived table and apply `ORDER BY` to it. For example:

```
mysql> SELECT * FROM
(SELECT year, SUM(profit) AS profit
FROM sales GROUP BY year WITH ROLLUP) AS dt
ORDER BY year DESC;
+------+--------+
| year | profit |
+------+--------+
| 2001 |   3010 |
| 2000 |   4525 |
| NULL |   7535 |
+------+--------+
```

In this case, the super-aggregate summary rows sort with the rows from which they are calculated, and their placement depends on sort order (at the beginning for ascending sort, at the end for descending sort).

`LIMIT` can be used to restrict the number of rows returned to the client. `LIMIT` is applied after `ROLLUP`, so the limit applies against the extra rows added by `ROLLUP`. For example:

```
mysql> SELECT year, country, product, SUM(profit) AS profit
FROM sales
GROUP BY year, country, product WITH ROLLUP
LIMIT 5;
```

MySQL Handling of GROUP BY

```
+------+---------+------------+--------+
| year | country | product    | profit |
+------+---------+------------+--------+
| 2000 | Finland | Computer   |   1500 |
| 2000 | Finland | Phone      |    100 |
| 2000 | Finland | NULL       |   1600 |
| 2000 | India   | Calculator |    150 |
| 2000 | India   | Computer   |   1200 |
+------+---------+------------+--------+
```

Using `LIMIT` with `ROLLUP` may produce results that are more difficult to interpret, because there is less context for understanding the super-aggregate rows.

A MySQL extension permits a column that does not appear in the `GROUP BY` list to be named in the select list. (For information about nonaggregated columns and `GROUP BY`, see Section 12.19.3, “MySQL Handling of GROUP BY”.) In this case, the server is free to choose any value from this nonaggregated column in summary rows, and this includes the extra rows added by `WITH ROLLUP`. For example, in the following query, `country` is a nonaggregated column that does not appear in the `GROUP BY` list and values chosen for this column are nondeterministic:

```
mysql> SELECT year, country, SUM(profit) AS profit
FROM sales
GROUP BY year WITH ROLLUP;
+------+---------+--------+
| year | country | profit |
+------+---------+--------+
| 2000 | India   |   4525 |
| 2001 | USA     |   3010 |
| NULL | USA     |   7535 |
+------+---------+--------+
```

This behavior is permitted when the `ONLY_FULL_GROUP_BY` SQL mode is not enabled. If that mode is enabled, the server rejects the query as illegal because `country` is not listed in the `GROUP BY` clause.

### 12.19.3 MySQL Handling of GROUP BY

In standard SQL, a query that includes a `GROUP BY` clause cannot refer to nonaggregated columns in the select list that are not named in the `GROUP BY` clause. For example, this query is illegal in standard SQL because the nonaggregated `name` column in the select list does not appear in the `GROUP BY`:

```
SELECT o.custid, c.name, MAX(o.payment)
FROM orders AS o, customers AS c
WHERE o.custid = c.custid
GROUP BY o.custid;
```

For the query to be legal, the `name` column must be omitted from the select list or named in the `GROUP BY`clause.

MySQL extends the standard SQL use of `GROUP BY` so that the select list can refer to nonaggregated columns not named in the `GROUP BY` clause. This means that the preceding query is legal in MySQL.

You can use this feature to get better performance by avoiding unnecessary column sorting and grouping.

However, this is useful primarily when all values in each nonaggregated column not named in the `GROUP``BY` are the same for each group. The server is free to choose any value from each group, so unless they are the same, the values chosen are nondeterministic. Furthermore, the selection of values from each group cannot be influenced by adding an `ORDER BY` clause. Result set sorting occurs after values have been chosen, and `ORDER BY` does not affect which values within each group the server chooses.

A similar MySQL extension applies to the `HAVING` clause. In standard SQL, a query cannot refer to nonaggregated columns in the `HAVING` clause that are not named in the `GROUP BY` clause. To simplify calculations, a MySQL extension permits references to such columns. This extension assumes that the nongrouped columns have the same group-wise values. Otherwise, the result is nondeterministic.

Miscellaneous Functions To disable the MySQL `GROUP BY` extension and enable standard SQL behavior, enable the`ONLY_FULL_GROUP_BY` SQL mode. In this case, columns not named in the `GROUP BY` clause cannot be used in the select list or `HAVING` clause unless enclosed in an aggregate function.

The select list extension also applies to `ORDER BY`. That is, you can refer to nonaggregated columns in the`ORDER BY` clause that do not appear in the `GROUP BY` clause. (However, as mentioned previously, `ORDER``BY` does not affect which values are chosen from nonaggregated columns; it only sorts them after they have been chosen.) This extension does not apply if the `ONLY_FULL_GROUP_BY` SQL mode is enabled.

If a query has aggregate functions and no `GROUP BY` clause, it cannot have nonaggregated columns in the select list, `HAVING` condition, or `ORDER BY` list with `ONLY_FULL_GROUP_BY` enabled:

```
mysql> SELECT name, MAX(age) FROM t;
ERROR 1140 (42000): Mixing of GROUP columns (MIN(),MAX(),COUNT(),...)
with no GROUP columns is illegal if there is no GROUP BY clause
```

Without `GROUP BY`, there is a single group and it is nondeterministic which `name` value to choose for the group.

Another MySQL extension to standard SQL permits references in the `HAVING` clause to aliased expressions in the select list. Enabling `ONLY_FULL_GROUP_BY` prevents this. For example, the following query returns `name` values that occur only once in table `orders`; the query is accepted regardless of whether `ONLY_FULL_GROUP_BY` is enabled:

```
SELECT name, COUNT(name) FROM orders
GROUP BY name
HAVING COUNT(name) = 1;
```

The following query is accepted only if `ONLY_FULL_GROUP_BY` is disabled.

```
SELECT name, COUNT(name) AS c FROM orders
GROUP BY name
HAVING c = 1;
```

If you are trying to follow standard SQL, you can use only column expressions in `GROUP BY` clauses. As a workaround, use an alias for the expression:

```
SELECT id, FLOOR(value/100) AS val
FROM tbl_name
GROUP BY id, val;
```

MySQL permits noncolumn expressions in `GROUP BY` clauses, so the alias is unnecessary:

```
SELECT id, FLOOR(value/100)
FROM tbl_name
GROUP BY id, FLOOR(value/100);
```

## 12.20 Miscellaneous Functions

Table 12.24 Miscellaneous Functions Name Description`DEFAULT()` Return the default value for a table column`INET_ATON()` Return the numeric value of an IP address`INET_NTOA()` Return the IP address from a numeric value`INET6_ATON()` Return the numeric value of an IPv6 address`INET6_NTOA()` Return the IPv6 address from a numeric value Miscellaneous Functions Name Description`IS_IPV4()` Whether argument is an IPv4 address`IS_IPV4_COMPAT()` Whether argument is an IPv4-compatible address`IS_IPV4_MAPPED()` Whether argument is an IPv4-mapped address`IS_IPV6()` Whether argument is an IPv6 address`MASTER_POS_WAIT()` Block until the replica has read and applied all updates up to the specified position`NAME_CONST()` Cause the column to have the given name`SLEEP()` Sleep for a number of seconds`UUID()` Return a Universal Unique Identifier (UUID)`UUID_SHORT()` Return an integer-valued universal identifier`VALUES()` Define the values to be used during an INSERT

```
- DEFAULT(col_name)
```

Returns the default value for a table column. An error results if the column has no default value.

```
mysql> UPDATE t SET i = DEFAULT(i)+1 WHERE id < 100;
- FORMAT(X,D)
```

Formats the number X to a format like `'#,###,###.##'`, rounded to D decimal places, and returns the result as a string. For details, see Section 12.8, “String Functions and Operators”.

```
- INET_ATON(expr)
```

Given the dotted-quad representation of an IPv4 network address as a string, returns an integer that represents the numeric value of the address in network byte order (big endian). `INET_ATON()` returns`NULL` if it does not understand its argument.

```
mysql> SELECT INET_ATON('10.0.5.9');
-> 167773449
```

For this example, the return value is calculated as 10×2563 + 0×2562 + 5×256 + 9.

`INET_ATON()` may or may not return a non-`NULL` result for short-form IP addresses (such as `'127.1'`as a representation of `'127.0.0.1'`). Because of this, `INET_ATON()`a should not be used for such addresses.

Note To store values generated by `INET_ATON()`, use an `INT UNSIGNED`column rather than `INT`, which is signed. If you use a signed column, values corresponding to IP addresses for which the first octet is greater than 127 cannot be stored correctly. See Section 11.1.7, “Out-of-Range and Overflow Handling”.

```
- INET_NTOA(expr)
```

Given a numeric IPv4 network address in network byte order, returns the dotted-quad string representation of the address as a string in the connection character set. `INET_NTOA()` returns `NULL` if it does not understand its argument.

```
mysql> SELECT INET_NTOA(167773449);
-> '10.0.5.9'
```

Miscellaneous Functions

```
- INET6_ATON(expr)
```

Given an IPv6 or IPv4 network address as a string, returns a binary string that represents the numeric value of the address in network byte order (big endian). Because numeric-format IPv6 addresses require more bytes than the largest integer type, the representation returned by this function has the`VARBINARY` data type: `VARBINARY(16)` for IPv6 addresses and `VARBINARY(4)` for IPv4 addresses. If the argument is not a valid address, `INET6_ATON()` returns `NULL`.

The following examples use `HEX()` to display the `INET6_ATON()` result in printable form:

```
mysql> SELECT HEX(INET6_ATON('fdfe::5a55:caff:fefa:9089'));
-> 'FDFE0000000000005A55CAFFFEFA9089'
mysql> SELECT HEX(INET6_ATON('10.0.5.9'));
-> '0A000509'
```

`INET6_ATON()` observes several constraints on valid arguments. These are given in the following list along with examples.

- A trailing zone ID is not permitted, as in `fe80::3%1` or `fe80::3%eth0`.
- A trailing network mask is not permitted, as in `2001:45f:3:ba::/64` or `198.51.100.0/24`.
- For values representing IPv4 addresses, only classless addresses are supported. Classful addresses

such as `198.51.1` are rejected. A trailing port number is not permitted, as in `198.51.100.2:8080`.

Hexadecimal numbers in address components are not permitted, as in `198.0xa0.1.2`. Octal numbers are not supported: `198.51.010.1` is treated as `198.51.10.1`, not `198.51.8.1`. These IPv4 constraints also apply to IPv6 addresses that have IPv4 address parts, such as IPv4-compatible or IPv4-mapped addresses.

To convert an IPv4 address `expr` represented in numeric form as an `INT` value to an IPv6 address represented in numeric form as a `VARBINARY` value, use this expression:

```
INET6_ATON(INET_NTOA(expr))
```

For example:

```
mysql> SELECT HEX(INET6_ATON(INET_NTOA(167773449)));
-> '0A000509'
```

If `INET6_ATON()` is invoked from within the `mysql` client, binary strings display using hexadecimal notation, depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

Miscellaneous Functions

```
- INET6_NTOA(expr)
```

Given an IPv6 or IPv4 network address represented in numeric form as a binary string, returns the string representation of the address as a string in the connection character set. If the argument is not a valid address, `INET6_NTOA()` returns `NULL`.

`INET6_NTOA()` has these properties:

- It does not use operating system functions to perform conversions, thus the output string is platform

independent.

- The return string has a maximum length of 39 (4 x 8 + 7). Given this statement:

```
CREATE TABLE t AS SELECT INET6_NTOA(expr) AS c1;
```

The resulting table would have this definition:

```
CREATE TABLE t (c1 VARCHAR(39) CHARACTER SET utf8 DEFAULT NULL);
```

- The return string uses lowercase letters for IPv6 addresses.

```
mysql> SELECT INET6_NTOA(INET6_ATON('fdfe::5a55:caff:fefa:9089'));
-> 'fdfe::5a55:caff:fefa:9089'
mysql> SELECT INET6_NTOA(INET6_ATON('10.0.5.9'));
-> '10.0.5.9'
mysql> SELECT INET6_NTOA(UNHEX('FDFE0000000000005A55CAFFFEFA9089'));
-> 'fdfe::5a55:caff:fefa:9089'
mysql> SELECT INET6_NTOA(UNHEX('0A000509'));
-> '10.0.5.9'
```

If `INET6_NTOA()` is invoked from within the `mysql` client, binary strings display using hexadecimal notation, depending on the value of the `--binary-as-hex`. For more information about that option, see Section 4.5.1, “mysql — The MySQL Command-Line Client”.

```
- IS_IPV4(expr)
```

Returns 1 if the argument is a valid IPv4 address specified as a string, 0 otherwise.

```
mysql> SELECT IS_IPV4('10.0.5.9'), IS_IPV4('10.0.5.256');
-> 1, 0
```

For a given argument, if `IS_IPV4()` returns 1, `INET_ATON()` (and `INET6_ATON()`) returns a value that is not `NULL`. The converse statement is not true: In some cases, `INET_ATON()` returns a value other than `NULL` when `IS_IPV4()` returns 0.

As implied by the preceding remarks, `IS_IPV4()` is more strict than `INET_ATON()` about what constitutes a valid IPv4 address, so it may be useful for applications that need to perform strong checks against invalid values. Alternatively, use `INET6_ATON()` to convert IPv4 addresses to internal form and check for a `NULL` result (which indicates an invalid address). `INET6_ATON()` is equally strong as`IS_IPV4()` about checking IPv4 addresses.

```
- IS_IPV4_COMPAT(expr)
```

This function takes an IPv6 address represented in numeric form as a binary string, as returned by`INET6_ATON()`. It returns 1 if the argument is a valid IPv4-compatible IPv6 address, 0 otherwise. IPv4-compatible addresses have the form `::ipv4_address`.

```
mysql> SELECT IS_IPV4_COMPAT(INET6_ATON('::10.0.5.9'));
-> 1
```

Miscellaneous Functions

```
mysql> SELECT IS_IPV4_COMPAT(INET6_ATON('::ffff:10.0.5.9'));
-> 0
```

The IPv4 part of an IPv4-compatible address can also be represented using hexadecimal notation. For example, `198.51.100.1` has this raw hexadecimal value:

```
mysql> SELECT HEX(INET6_ATON('198.51.100.1'));
-> 'C6336401'
```

Expressed in IPv4-compatible form, `::198.51.100.1` is equivalent to `::c0a8:0001` or (without leading zeros) `::c0a8:1`

```
mysql> SELECT
->   IS_IPV4_COMPAT(INET6_ATON('::198.51.100.1')),
->   IS_IPV4_COMPAT(INET6_ATON('::c0a8:0001')),
->   IS_IPV4_COMPAT(INET6_ATON('::c0a8:1'));
-> 1, 1, 1
- IS_IPV4_MAPPED(expr)
```

This function takes an IPv6 address represented in numeric form as a binary string, as returned by`INET6_ATON()`. It returns 1 if the argument is a valid IPv4-mapped IPv6 address, 0 otherwise. IPv4-mapped addresses have the form `::ffff:ipv4_address`.

```
mysql> SELECT IS_IPV4_MAPPED(INET6_ATON('::10.0.5.9'));
-> 0
mysql> SELECT IS_IPV4_MAPPED(INET6_ATON('::ffff:10.0.5.9'));
-> 1
```

As with `IS_IPV4_COMPAT()` the IPv4 part of an IPv4-mapped address can also be represented using hexadecimal notation:

```
mysql> SELECT
->   IS_IPV4_MAPPED(INET6_ATON('::ffff:198.51.100.1')),
->   IS_IPV4_MAPPED(INET6_ATON('::ffff:c0a8:0001')),
->   IS_IPV4_MAPPED(INET6_ATON('::ffff:c0a8:1'));
-> 1, 1, 1
- IS_IPV6(expr)
```

Returns 1 if the argument is a valid IPv6 address specified as a string, 0 otherwise. This function does not consider IPv4 addresses to be valid IPv6 addresses.

```
mysql> SELECT IS_IPV6('10.0.5.9'), IS_IPV6('::1');
-> 0, 1
```

For a given argument, if `IS_IPV6()` returns 1, `INET6_ATON()` returns a value other than `NULL`.

```
- MASTER_POS_WAIT(log_name,log_pos[,timeout])
```

This function is useful for control of source/replica synchronization. It blocks until the replica has read and applied all updates up to the specified position in the source log. The return value is the number of log events the replica had to wait for to advance to the specified position. The function returns `NULL` if the replica SQL thread is not started, the replica's source information is not initialized, the arguments are incorrect, or an error occurs. It returns `-1` if the timeout has been exceeded. If the replica SQL thread stops while `MASTER_POS_WAIT()` is waiting, the function returns `NULL`. If the replica is past the specified position, the function returns immediately.

On a multithreaded replica, the function waits until expiry of the limit set by the`slave_checkpoint_group` or `slave_checkpoint_period` system variable, when the checkpoint Miscellaneous Functions operation is called to update the status of the replica. Depending on the setting for the system variables,the function might therefore return some time after the specified position was reached.

If a `timeout` value is specified, `MASTER_POS_WAIT()` stops waiting when `timeout` seconds have elapsed. `timeout` must be greater than 0; a zero or negative `timeout` means no timeout.

This function is unsafe for statement-based replication. A warning is logged if you use this function when`binlog_format` is set to `STATEMENT`.

```
- NAME_CONST(name,value)
```

Returns the given value. When used to produce a result set column, `NAME_CONST()` causes the column to have the given name. The arguments should be constants.

```
mysql> SELECT NAME_CONST('myname', 14);
+--------+
| myname |
+--------+
|     14 |
+--------+
```

This function is for internal use only. The server uses it when writing statements from stored programs that contain references to local program variables, as described in Section 20.7, “Stored Program Binary Logging”. You might see this function in the output from `mysqlbinlog`.

For your applications, you can obtain exactly the same result as in the example just shown by using simple aliasing, like this:

```
mysql> SELECT 14 AS myname;
+--------+
| myname |
+--------+
|     14 |
+--------+
1 row in set (0.00 sec)
```

See Section 13.2.9, “SELECT Statement”, for more information about column aliases.

```
- SLEEP(duration)
```

Sleeps (pauses) for the number of seconds given by the `duration` argument, then returns 0. If`SLEEP()` is interrupted, it returns 1. The duration may have a fractional part.

When sleep returns normally (without interruption), it returns 0:

```
mysql> SELECT SLEEP(1000);
+-------------+
| SLEEP(1000) |
+-------------+
|           0 |
+-------------+
```

When `SLEEP()` is the only thing invoked by a query that is interrupted, it returns 1 and the query itself returns no error. This statement is interrupted using `KILL QUERY` from another session:

```
mysql> SELECT SLEEP(1000);
+-------------+
| SLEEP(1000) |
+-------------+
|           1 |
```

Miscellaneous Functions

```
+-------------+
```

When `SLEEP()` is only part of a query that is interrupted, the query returns an error. This statement is interrupted using `KILL QUERY` from another session:

```
mysql> SELECT 1 FROM t1 WHERE SLEEP(1000);
ERROR 1317 (70100): Query execution was interrupted
```

This function is unsafe for statement-based replication. A warning is logged if you use this function when`binlog_format` is set to `STATEMENT`.

```
- UUID()
```

Returns a Universal Unique Identifier (UUID) generated according to RFC 4122, “A Universally Unique IDentifier (UUID) URN Namespace” (http://www.ietf.org/rfc/rfc4122.txt).

A UUID is designed as a number that is globally unique in space and time. Two calls to `UUID()` are expected to generate two different values, even if these calls are performed on two separate devices not connected to each other.

Warning Although `UUID()` values are intended to be unique, they are not necessarily unguessable or unpredictable. If unpredictability is required, UUID values should be generated some other way.

`UUID()` returns a value that conforms to UUID version 1 as described in RFC 4122. The value is a 128-bit number represented as a `utf8` string of five hexadecimal numbers in `aaaaaaaa-bbbb-cccc-``dddd-eeeeeeeeeeee` format:

- The first three numbers are generated from the low, middle, and high parts of a timestamp. The high

part also includes the UUID version number.

- The fourth number preserves temporal uniqueness in case the timestamp value loses monotonicity

(for example, due to daylight saving time).

- The fifth number is an IEEE 802 node number that provides spatial uniqueness. A random number is

substituted if the latter is not available (for example, because the host device has no Ethernet card,or it is unknown how to find the hardware address of an interface on the host operating system). In this case, spatial uniqueness cannot be guaranteed. Nevertheless, a collision should have very low probability.

The MAC address of an interface is taken into account only on FreeBSD, Linux, and Windows. On other operating systems, MySQL uses a randomly generated 48-bit number.

```
mysql> SELECT UUID();
-> '6ccd780c-baba-1026-9564-5b8c656024db'
```

This function is unsafe for statement-based replication. A warning is logged if you use this function when`binlog_format` is set to `STATEMENT`.

```
- UUID_SHORT()
```

Returns a “short” universal identifier as a 64-bit unsigned integer. Values returned by `UUID_SHORT()`differ from the string-format 128-bit identifiers returned by the `UUID()` function and have different Precision Math uniqueness properties. The value of `UUID_SHORT()` is guaranteed to be unique if the following conditions hold:

- The `server_id` value of the current server is between 0 and 255 and is unique among your set of

source and replica servers

- You do not set back the system time for your server host between `mysqld` restarts
- You invoke `UUID_SHORT()` on average fewer than 16 million times per second between `mysqld`

restarts The `UUID_SHORT()` return value is constructed this way:

```
(server_id & 255) << 56
+ (server_startup_time_in_seconds << 24)
+ incremented_variable++;
mysql> SELECT UUID_SHORT();
-> 92395783831158784
```

Note`UUID_SHORT()` does not work with statement-based replication.

```
- VALUES(col_name)
```

In an `INSERT ... ON DUPLICATE KEY UPDATE` statement, you can use the `VALUES(col_name)`function in the `UPDATE` clause to refer to column values from the `INSERT` portion of the statement. In other words, `VALUES(col_name)` in the `UPDATE` clause refers to the value of `col_name` that would be inserted, had no duplicate-key conflict occurred. This function is especially useful in multiple-row inserts. The `VALUES()` function is meaningful only in the `ON DUPLICATE KEY UPDATE` clause of`INSERT` statements and returns `NULL` otherwise. See Section 13.2.5.2, “INSERT ... ON DUPLICATE KEY UPDATE Statement”.

```
mysql> INSERT INTO table (a,b,c) VALUES (1,2,3),(4,5,6)
-> ON DUPLICATE KEY UPDATE c=VALUES(a)+VALUES(b);
```

## 12.21 Precision Math

MySQL provides support for precision math: numeric value handling that results in extremely accurate results and a high degree control over invalid values. Precision math is based on these two features:

- SQL modes that control how strict the server is about accepting or rejecting invalid data.
- The MySQL library for fixed-point arithmetic.

These features have several implications for numeric operations and provide a high degree of compliance with standard SQL:

- Precise calculations: For exact-value numbers, calculations do not introduce floating-point errors.

Instead, exact precision is used. For example, MySQL treats a number such as `.0001` as an exact value rather than as an approximation, and summing it 10,000 times produces a result of exactly 1, not a value that is merely “close” to 1.

- Well-defined rounding behavior: For exact-value numbers, the result of `ROUND()` depends on its

argument, not on environmental factors such as how the underlying C library works.

Types of Numeric Values

- Platform independence: Operations on exact numeric values are the same across different platforms

such as Windows and Unix.

- Control over handling of invalid values: Overflow and division by zero are detectable and can be

treated as errors. For example, you can treat a value that is too large for a column as an error rather than having the value truncated to lie within the range of the column's data type. Similarly, you can treat division by zero as an error rather than as an operation that produces a result of `NULL`. The choice of which approach to take is determined by the setting of the server SQL mode.

The following discussion covers several aspects of how precision math works, including possible incompatibilities with older applications. At the end, some examples are given that demonstrate how MySQL handles numeric operations precisely. For information about controlling the SQL mode, see Section 5.1.10, “Server SQL Modes”.

### 12.21.1 Types of Numeric Values

The scope of precision math for exact-value operations includes the exact-value data types (integer and`DECIMAL` types) and exact-value numeric literals. Approximate-value data types and numeric literals are handled as floating-point numbers.

Exact-value numeric literals have an integer part or fractional part, or both. They may be signed. Examples:

```
1, .2, 3.4, -5, -6.78, +9.10.
```

Approximate-value numeric literals are represented in scientific notation with a mantissa and exponent.

Either or both parts may be signed. Examples: `1.2E3`, `1.2E-3`, `-1.2E3`, `-1.2E-3`.

Two numbers that look similar may be treated differently. For example, `2.34` is an exact-value (fixed-point)number, whereas `2.34E0` is an approximate-value (floating-point) number.

The `DECIMAL` data type is a fixed-point type and calculations are exact. In MySQL, the `DECIMAL` type has several synonyms: `NUMERIC`, `DEC`, `FIXED`. The integer types also are exact-value types.

The `FLOAT` and `DOUBLE` data types are floating-point types and calculations are approximate. In MySQL,types that are synonymous with `FLOAT` or `DOUBLE` are `DOUBLE PRECISION` and `REAL`.

### 12.21.2 DECIMAL Data Type Characteristics

This section discusses the characteristics of the `DECIMAL` data type (and its synonyms), with particular regard to the following topics:

- Maximum number of digits
- Storage format
- Storage requirements
- The nonstandard MySQL extension to the upper range of `DECIMAL` columns

The declaration syntax for a `DECIMAL` column is `DECIMAL(M,D)`. The ranges of values for the arguments are as follows:

- M is the maximum number of digits (the precision). It has a range of 1 to 65.
- D is the number of digits to the right of the decimal point (the scale). It has a range of 0 to 30 and must

be no larger than M.

If D is omitted, the default is 0. If M is omitted, the default is 10.

Expression Handling The maximum value of 65 for M means that calculations on `DECIMAL` values are accurate up to 65 digits.

This limit of 65 digits of precision also applies to exact-value numeric literals, so the maximum range of such literals differs from before. (There is also a limit on how long the text of `DECIMAL` literals can be; see Section 12.21.3, “Expression Handling”.)Values for `DECIMAL` columns are stored using a binary format that packs nine decimal digits into 4 bytes.

The storage requirements for the integer and fractional parts of each value are determined separately.

Each multiple of nine digits requires 4 bytes, and any remaining digits left over require some fraction of 4 bytes. The storage required for remaining digits is given by the following table.

Leftover Digits Number of Bytes 0 0 1–2 1 3–4 2 5–6 3 7–9 4 For example, a `DECIMAL(18,9)` column has nine digits on either side of the decimal point, so the integer part and the fractional part each require 4 bytes. A `DECIMAL(20,6)` column has fourteen integer digits and six fractional digits. The integer digits require four bytes for nine of the digits and 3 bytes for the remaining five digits. The six fractional digits require 3 bytes.

`DECIMAL` columns do not store a leading + character or - character or leading 0 digits. If you insert`+0003.1` into a `DECIMAL(5,1)` column, it is stored as `3.1`. For negative numbers, a literal - character is not stored.

`DECIMAL` columns do not permit values larger than the range implied by the column definition. For example, a `DECIMAL(3,0)` column supports a range of `-999` to 999. A `DECIMAL(M,D)` column permits up to M - D digits to the left of the decimal point.

The SQL standard requires that the precision of `NUMERIC(M,D)` be exactly M digits. For `DECIMAL(M,D)`,the standard requires a precision of at least M digits but permits more. In MySQL, `DECIMAL(M,D)` and`NUMERIC(M,D)` are the same, and both have a precision of exactly M digits.

For a full explanation of the internal format of `DECIMAL` values, see the file `strings/decimal.c` in a MySQL source distribution. The format is explained (with an example) in the `decimal2bin()` function.

### 12.21.3 Expression Handling

With precision math, exact-value numbers are used as given whenever possible. For example, numbers in comparisons are used exactly as given without a change in value. In strict SQL mode, for `INSERT` into a column with an exact data type (`DECIMAL` or integer), a number is inserted with its exact value if it is within the column range. When retrieved, the value should be the same as what was inserted. (If strict SQL mode is not enabled, truncation for `INSERT` is permissible.)Handling of a numeric expression depends on what kind of values the expression contains:

- If any approximate values are present, the expression is approximate and is evaluated using floating-

point arithmetic.

- If no approximate values are present, the expression contains only exact values. If any exact value

contains a fractional part (a value following the decimal point), the expression is evaluated using Expression Handling`DECIMAL` exact arithmetic and has a precision of 65 digits. The term “exact” is subject to the limits of what can be represented in binary. For example, `1.0/3.0` can be approximated in decimal notation as`.333...`, but not written as an exact number, so `(1.0/3.0)*3.0` does not evaluate to exactly `1.0`.

- Otherwise, the expression contains only integer values. The expression is exact and is evaluated using

integer arithmetic and has a precision the same as `BIGINT` (64 bits).

If a numeric expression contains any strings, they are converted to double-precision floating-point values and the expression is approximate.

Inserts into numeric columns are affected by the SQL mode, which is controlled by the `sql_mode`system variable. (See Section 5.1.10, “Server SQL Modes”.) The following discussion mentions strict mode (selected by the `STRICT_ALL_TABLES` or `STRICT_TRANS_TABLES` mode values) and`ERROR_FOR_DIVISION_BY_ZERO`. To turn on all restrictions, you can simply use `TRADITIONAL` mode,which includes both strict mode values and `ERROR_FOR_DIVISION_BY_ZERO`:

```
SET sql_mode='TRADITIONAL';
```

If a number is inserted into an exact type column (`DECIMAL` or integer), it is inserted with its exact value if it is within the column range and precision.

If the value has too many digits in the fractional part, rounding occurs and a note is generated. Rounding is done as described in Section 12.21.4, “Rounding Behavior”. Truncation due to rounding of the fractional part is not an error, even in strict mode.

If the value has too many digits in the integer part, it is too large (out of range) and is handled as follows:

- If strict mode is not enabled, the value is truncated to the nearest legal value and a warning is generated.
- If strict mode is enabled, an overflow error occurs.

For `DECIMAL` literals, in addition to the precision limit of 65 digits, there is a limit on how long the text of the literal can be. If the value exceeds approximately 80 characters, unexpected results can occur. For example:

```
mysql> SELECT
CAST(0000000000000000000000000000000000000000000000000000000000000000000000000000000020.01 AS DECIMAL(1
+------------------+
| val              |
+------------------+
| 9999999999999.99 |
+------------------+
1 row in set, 2 warnings (0.00 sec)
mysql> SHOW WARNINGS;
+---------+------+----------------------------------------------+
| Level   | Code | Message                                      |
+---------+------+----------------------------------------------+
| Warning | 1292 | Truncated incorrect DECIMAL value: ''        |
| Warning | 1264 | Out of range value for column 'val' at row 1 |
+---------+------+----------------------------------------------+
2 rows in set (0.00 sec)
```

Underflow is not detected, so underflow handling is undefined.

For inserts of strings into numeric columns, conversion from string to number is handled as follows if the string has nonnumeric contents:

- A string that does not begin with a number cannot be used as a number and produces an error in strict

mode, or a warning otherwise. This includes the empty string.

Rounding Behavior

- A string that begins with a number can be converted, but the trailing nonnumeric portion is truncated.

If the truncated portion contains anything other than spaces, this produces an error in strict mode, or a warning otherwise.

By default, division by zero produces a result of `NULL` and no warning. By setting the SQL mode appropriately, division by zero can be restricted.

With the `ERROR_FOR_DIVISION_BY_ZERO` SQL mode enabled, MySQL handles division by zero differently:

- If strict mode is not enabled, a warning occurs.
- If strict mode is enabled, inserts and updates involving division by zero are prohibited, and an error

occurs.

In other words, inserts and updates involving expressions that perform division by zero can be treated as errors, but this requires `ERROR_FOR_DIVISION_BY_ZERO` in addition to strict mode.

Suppose that we have this statement:

```
INSERT INTO t SET i = 1/0;
```

This is what happens for combinations of strict and `ERROR_FOR_DIVISION_BY_ZERO` modes.

`sql_mode` Value Result`''` (Default) No warning, no error; i is set to `NULL`.

strict No warning, no error; i is set to `NULL`.

`ERROR_FOR_DIVISION_BY_ZERO` Warning, no error; i is set to `NULL`.

strict,`ERROR_FOR_DIVISION_BY_ZERO` Error condition; no row is inserted.

### 12.21.4 Rounding Behavior

This section discusses precision math rounding for the `ROUND()` function and for inserts into columns with exact-value types (`DECIMAL` and integer).

The `ROUND()` function rounds differently depending on whether its argument is exact or approximate:

- For exact-value numbers, `ROUND()` uses the “round half up” rule: A value with a fractional part of .5

or greater is rounded up to the next integer if positive or down to the next integer if negative. (In other words, it is rounded away from zero.) A value with a fractional part less than .5 is rounded down to the next integer if positive or up to the next integer if negative. (In other words, it is rounded toward zero.)

- For approximate-value numbers, the result depends on the C library. On many systems, this means that

`ROUND()` uses the “round to nearest even” rule: A value with a fractional part exactly half way between two integers is rounded to the nearest even integer.

The following example shows how rounding differs for exact and approximate values:

```
mysql> SELECT ROUND(2.5), ROUND(25E-1);
+------------+--------------+
| ROUND(2.5) | ROUND(25E-1) |
+------------+--------------+
| 3          |            2 |
+------------+--------------+
```

For inserts into a `DECIMAL` or integer column, the target is an exact data type, so rounding uses “round half away from zero,” regardless of whether the value to be inserted is exact or approximate:Precision Math Examples

```
mysql> CREATE TABLE t (d DECIMAL(10,0));
Query OK, 0 rows affected (0.00 sec)
mysql> INSERT INTO t VALUES(2.5),(2.5E0);
Query OK, 2 rows affected, 2 warnings (0.00 sec)
Records: 2  Duplicates: 0  Warnings: 2
mysql> SHOW WARNINGS;
+-------+------+----------------------------------------+
| Level | Code | Message                                |
+-------+------+----------------------------------------+
| Note  | 1265 | Data truncated for column 'd' at row 1 |
| Note  | 1265 | Data truncated for column 'd' at row 2 |
+-------+------+----------------------------------------+
2 rows in set (0.00 sec)
mysql> SELECT d FROM t;
+------+
| d    |
+------+
|    3 |
|    3 |
+------+
2 rows in set (0.00 sec)
```

The `SHOW WARNINGS` statement displays the notes that are generated by truncation due to rounding of the fractional part. Such truncation is not an error, even in strict SQL mode (see Section 12.21.3, “Expression Handling”).

### 12.21.5 Precision Math Examples

This section provides some examples that show precision math query results in MySQL. These examples demonstrate the principles described in Section 12.21.3, “Expression Handling”, and Section 12.21.4,“Rounding Behavior”.

> Example 1. Numbers are used with their exact value as given when possible:

```
mysql> SELECT (.1 + .2) = .3;
+----------------+
| (.1 + .2) = .3 |
+----------------+
|              1 |
+----------------+
```

For floating-point values, results are inexact:

```
mysql> SELECT (.1E0 + .2E0) = .3E0;
+----------------------+
| (.1E0 + .2E0) = .3E0 |
+----------------------+
|                    0 |
+----------------------+
```

Another way to see the difference in exact and approximate value handling is to add a small number to a sum many times. Consider the following stored procedure, which adds `.0001` to a variable 1,000 times.

```
CREATE PROCEDURE p ()
BEGIN
DECLARE i INT DEFAULT 0;
DECLARE d DECIMAL(10,4) DEFAULT 0;
DECLARE f FLOAT DEFAULT 0;
WHILE i < 10000 DO
SET d = d + .0001;
```

Precision Math Examples

```
SET f = f + .0001E0;
SET i = i + 1;
END WHILE;
SELECT d, f;
END;
```

The sum for both d and f logically should be 1, but that is true only for the decimal calculation. The floating-point calculation introduces small errors:

```
+--------+------------------+
| d      | f                |
+--------+------------------+
| 1.0000 | 0.99999999999991 |
+--------+------------------+
```

Example 2. Multiplication is performed with the scale required by standard SQL. That is, for two numbers`X1` and `X2` that have scale `S1` and `S2`, the scale of the result is `S1 + S2`:

```
mysql> SELECT .01 * .01;
+-----------+
| .01 * .01 |
+-----------+
| 0.0001    |
+-----------+
```

Example 3. Rounding behavior for exact-value numbers is well-defined:Rounding behavior (for example, with the `ROUND()` function) is independent of the implementation of the underlying C library, which means that results are consistent from platform to platform.

- Rounding for exact-value columns (`DECIMAL` and integer) and exact-valued numbers uses the “round

half away from zero” rule. A value with a fractional part of .5 or greater is rounded away from zero to the nearest integer, as shown here:

```
mysql> SELECT ROUND(2.5), ROUND(-2.5);
+------------+-------------+
| ROUND(2.5) | ROUND(-2.5) |
+------------+-------------+
| 3          | -3          |
+------------+-------------+
```

- Rounding for floating-point values uses the C library, which on many systems uses the “round to nearest

even” rule. A value with a fractional part exactly half way between two integers is rounded to the nearest even integer:

```
mysql> SELECT ROUND(2.5E0), ROUND(-2.5E0);
+--------------+---------------+
| ROUND(2.5E0) | ROUND(-2.5E0) |
+--------------+---------------+
|            2 |            -2 |
+--------------+---------------+
```

Example 4. In strict mode, inserting a value that is out of range for a column causes an error, rather than truncation to a legal value.

When MySQL is not running in strict mode, truncation to a legal value occurs:

```
mysql> SET sql_mode='';
Query OK, 0 rows affected (0.00 sec)
mysql> CREATE TABLE t (i TINYINT);
Query OK, 0 rows affected (0.01 sec)
```

Precision Math Examples

```
mysql> INSERT INTO t SET i = 128;
Query OK, 1 row affected, 1 warning (0.00 sec)
mysql> SELECT i FROM t;
+------+
| i    |
+------+
|  127 |
+------+
1 row in set (0.00 sec)
```

However, an error occurs if strict mode is in effect:

```
mysql> SET sql_mode='STRICT_ALL_TABLES';
Query OK, 0 rows affected (0.00 sec)
mysql> CREATE TABLE t (i TINYINT);
Query OK, 0 rows affected (0.00 sec)
mysql> INSERT INTO t SET i = 128;
ERROR 1264 (22003): Out of range value adjusted for column 'i' at row 1
mysql> SELECT i FROM t;
Empty set (0.00 sec)
```

Example 5: In strict mode and with `ERROR_FOR_DIVISION_BY_ZERO` set, division by zero causes an error, not a result of `NULL`.

In nonstrict mode, division by zero has a result of `NULL`:

```
mysql> SET sql_mode='';
Query OK, 0 rows affected (0.01 sec)
mysql> CREATE TABLE t (i TINYINT);
Query OK, 0 rows affected (0.00 sec)
mysql> INSERT INTO t SET i = 1 / 0;
Query OK, 1 row affected (0.00 sec)
mysql> SELECT i FROM t;
+------+
| i    |
+------+
| NULL |
+------+
1 row in set (0.03 sec)
```

However, division by zero is an error if the proper SQL modes are in effect:

```
mysql> SET sql_mode='STRICT_ALL_TABLES,ERROR_FOR_DIVISION_BY_ZERO';
Query OK, 0 rows affected (0.00 sec)
mysql> CREATE TABLE t (i TINYINT);
Query OK, 0 rows affected (0.00 sec)
mysql> INSERT INTO t SET i = 1 / 0;
ERROR 1365 (22012): Division by 0
mysql> SELECT i FROM t;
Empty set (0.01 sec)
```

> Example 6. Exact-value literals are evaluated as exact values.

Approximate-value literals are evaluated using floating point, but exact-value literals are handled as

```
DECIMAL:
```

Precision Math Examples

```
mysql> CREATE TABLE t SELECT 2.5 AS a, 25E-1 AS b;
Query OK, 1 row affected (0.01 sec)
Records: 1  Duplicates: 0  Warnings: 0
mysql> DESCRIBE t;
+-------+-----------------------+------+-----+---------+-------+
| Field | Type                  | Null | Key | Default | Extra |
+-------+-----------------------+------+-----+---------+-------+
| a     | decimal(2,1) unsigned | NO   |     | 0.0     |       |
| b     | double                | NO   |     | 0       |       |
+-------+-----------------------+------+-----+---------+-------+
2 rows in set (0.01 sec)
```

Example 7. If the argument to an aggregate function is an exact numeric type, the result is also an exact numeric type, with a scale at least that of the argument.

Consider these statements:

```
mysql> CREATE TABLE t (i INT, d DECIMAL, f FLOAT);
mysql> INSERT INTO t VALUES(1,1,1);
mysql> CREATE TABLE y SELECT AVG(i), AVG(d), AVG(f) FROM t;
```

The result is a double only for the floating-point argument. For exact type arguments, the result is also an exact type:

```
mysql> DESCRIBE y;
+--------+---------------+------+-----+---------+-------+
| Field  | Type          | Null | Key | Default | Extra |
+--------+---------------+------+-----+---------+-------+
| AVG(i) | decimal(14,4) | YES  |     | NULL    |       |
| AVG(d) | decimal(14,4) | YES  |     | NULL    |       |
| AVG(f) | double        | YES  |     | NULL    |       |
+--------+---------------+------+-----+---------+-------+
```

The result is a double only for the floating-point argument. For exact type arguments, the result is also an exact type.
