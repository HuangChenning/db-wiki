---
title: "12.17.2 Functions That Create JSON Values"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/json-creation-functions.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 12.17.2 Functions That Create JSON Values

The functions listed in this section compose JSON values from component elements.

- [``JSON_ARRAY([*`val`*[,           *`val`*] ...])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/json-creation-functions.html#function_json-array)
	Evaluates a (possibly empty) list of values and returns a JSON array containing those values.
	```
	mysql> SELECT JSON_ARRAY(1, "abc", NULL, TRUE, CURTIME());
	+---------------------------------------------+
	| JSON_ARRAY(1, "abc", NULL, TRUE, CURTIME()) |
	+---------------------------------------------+
	| [1, "abc", null, true, "11:30:24.000000"]   |
	+---------------------------------------------+
	```
- [``JSON_OBJECT([*`key`*,           *`val`*[,           *`key`*,           *`val`*] ...])``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/json-creation-functions.html#function_json-object)
	Evaluates a (possibly empty) list of key-value pairs and returns a JSON object containing those pairs. An error occurs if any key name is `NULL` or the number of arguments is odd.
	```
	mysql> SELECT JSON_OBJECT('id', 87, 'name', 'carrot');
	+-----------------------------------------+
	| JSON_OBJECT('id', 87, 'name', 'carrot') |
	+-----------------------------------------+
	| {"id": 87, "name": "carrot"}            |
	+-----------------------------------------+
	```
- ``JSON_QUOTE(*`string`*)``
	Quotes a string as a JSON value by wrapping it with double quote characters and escaping interior quote and other characters, then returning the result as a `utf8mb4` string. Returns `NULL` if the argument is `NULL`.
	This function is typically used to produce a valid JSON string literal for inclusion within a JSON document.
	Certain special characters are escaped with backslashes per the escape sequences shown in [Table 12.23, “JSON\_UNQUOTE() Special Character Escape Sequences”](json-modification-functions.md).
	```
	mysql> SELECT JSON_QUOTE('null'), JSON_QUOTE('"null"');
	+--------------------+----------------------+
	| JSON_QUOTE('null') | JSON_QUOTE('"null"') |
	+--------------------+----------------------+
	| "null"             | "\"null\""           |
	+--------------------+----------------------+
	mysql> SELECT JSON_QUOTE('[1, 2, 3]');
	+-------------------------+
	| JSON_QUOTE('[1, 2, 3]') |
	+-------------------------+
	| "[1, 2, 3]"             |
	+-------------------------+
	```

You can also obtain JSON values by casting values of other types to the `JSON` type using [``CAST(*`value`* AS       JSON)``](cast-functions.md); see [Converting between JSON and non-JSON values](json.md), for more information.

Two aggregate functions generating JSON values are available (MySQL 5.7.22 and later). [`JSON_ARRAYAGG()`](aggregate-functions.md) returns a result set as a single JSON array, and [`JSON_OBJECTAGG()`](aggregate-functions.md) returns a result set as a single JSON object. For more information, see [Section 12.19, “Aggregate Functions”](aggregate-functions-and-modifiers.md).