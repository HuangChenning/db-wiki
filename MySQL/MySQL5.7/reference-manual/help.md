---
title: "13.8.3 HELP Statement"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/help.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.8.3 HELP Statement

```
HELP 'search_string'
```

The `HELP` statement returns online information from the MySQL Reference Manual. Its proper operation requires that the help tables in the `mysql` database be initialized with help topic information (see [Section 5.1.14, “Server-Side Help Support”](server-side-help-support.md)).

The `HELP` statement searches the help tables for the given search string and displays the result of the search. The search string is not case-sensitive.

The search string can contain the wildcard characters `%` and `_`. These have the same meaning as for pattern-matching operations performed with the [`LIKE`](string-comparison-functions.md) operator. For example, `HELP 'rep%'` returns a list of topics that begin with `rep`.

The `HELP` statement does not require a terminator such as `;` or `\G`.

The HELP statement understands several types of search strings:

- At the most general level, use `contents` to retrieve a list of the top-level help categories:
	```
	HELP 'contents'
	```
- For a list of topics in a given help category, such as `Data Types`, use the category name:
	```
	HELP 'data types'
	```
- For help on a specific help topic, such as the [`ASCII()`](string-functions.md) function or the [`CREATE TABLE`](create-table.md) statement, use the associated keyword or keywords:
	```
	HELP 'ascii'
	HELP 'create table'
	```

In other words, the search string matches a category, many topics, or a single topic. The following descriptions indicate the forms that the result set can take.

- Empty result
	No match could be found for the search string.
	Example: `HELP 'fake'`
	Yields:
	```
	Nothing found
	Please try to run 'help contents' for a list of all accessible topics
	```
- Result set containing a single row
	This means that the search string yielded a hit for the help topic. The result includes the following items:
	- `name`: The topic name.
	- `description`: Descriptive help text for the topic.
	- `example`: One or more usage examples. (May be empty.)
	Example: `HELP 'log'`
	Yields:
	```
	Name: 'LOG'
	Description:
	Syntax:
	LOG(X), LOG(B,X)
	If called with one parameter, this function returns the natural
	logarithm of X. If X is less than or equal to 0.0E0, the function
	returns NULL and a warning "Invalid argument for logarithm" is
	reported. Returns NULL if X or B is NULL.
	The inverse of this function (when called with a single argument) is
	the EXP() function.
	URL: https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mathematical-functions.html
	Examples:
	mysql> SELECT LOG(2);
	        -> 0.69314718055995
	mysql> SELECT LOG(-2);
	        -> NULL
	```
- List of topics.
	This means that the search string matched multiple help topics.
	Example: `HELP 'status'`
	Yields:
	```
	Many help items for your request exist.
	To make a more specific request, please type 'help <item>',
	where <item> is one of the following topics:
	   FLUSH
	   SHOW
	   SHOW ENGINE
	   SHOW FUNCTION STATUS
	   SHOW MASTER STATUS
	   SHOW PROCEDURE STATUS
	   SHOW SLAVE STATUS
	   SHOW STATUS
	   SHOW TABLE STATUS
	```
- List of topics.
	A list is also displayed if the search string matches a category.
	Example: `HELP 'functions'`
	Yields:
	```
	You asked for help about help category: "Functions"
	For more information, type 'help <item>', where <item> is one of the following
	categories:
	   Aggregate Functions and Modifiers
	   Bit Functions
	   Cast Functions and Operators
	   Comparison Operators
	   Date and Time Functions
	   Encryption Functions
	   Enterprise Encryption Functions
	   Flow Control Functions
	   GROUP BY Functions and Modifiers
	   GTID
	   Information Functions
	   Locking Functions
	   Logical Operators
	   Miscellaneous Functions
	   Numeric Functions
	   Spatial Functions
	   String Functions
	   XML
	```