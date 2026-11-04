---
title: "MySQL :: MySQL 26.10 Reference Manual :: SQL Modes Index"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/dynindex-sqlmode.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

[Documentation Home](https://dev.mysql.com/doc/)

---

MySQL 26.10 Reference Manual

Related Documentation

[MySQL 26.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.10/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.10-en.pdf) - 42.3Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.10-en.a4.pdf) - 42.4Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.tar.gz) - 272.9Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.zip) - 379.1Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.10.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.10.info.zip) - 4.2Mb

version 26.10

[26.7](https://dev.mysql.com/doc/refman/26.7/en/dynindex-sqlmode.html)  
[9.7 current](https://dev.mysql.com/doc/refman/9.7/en/dynindex-sqlmode.html)  
[8.4](https://dev.mysql.com/doc/refman/8.4/en/dynindex-sqlmode.html)  
[8.0](https://dev.mysql.com/doc/refman/8.0/en/dynindex-sqlmode.html)  

[8.0 Japanese](https://dev.mysql.com/doc/refman/8.0/ja/)

[MySQL 26.10 Reference Manual](https://dev.mysql.com/doc/refman/26.10/en/) / [Indexes](indexes.md) / Modes Index

## SQL Modes Index

A | E | H | I | N | O | P | R | S | T

### A

\[index top\]

### ALLOW\_INVALID\_DATES

[Section 13.2, “Date and Time Data Types”](date-and-time-types.md)

[Section 14.7, “Date and Time Functions”](date-and-time-functions.md)

[Section B.3.4.2, “Problems Using DATE Columns”](using-date.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

[Section 13.2.2, “The DATE, DATETIME, and TIMESTAMP Types”](datetime.md)

### ANSI

[Section 11.2.5, “Function Name Parsing and Resolution”](function-resolution.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

[Section 15.7.7.16, “SHOW CREATE VIEW Statement”](show-create-view.md)

[Section 28.3.53, “The INFORMATION\_SCHEMA VIEWS Table”](information-schema-views-table.md)

### ANSI\_QUOTES

[Section 15.1.19, “CREATE LIBRARY Statement”](create-library.md)

[Section 15.1.25.5, “FOREIGN KEY Constraints”](create-table-foreign-keys.md)

[Section 6.5.1.6, “mysql Client Tips”](mysql-tips.md)

[Section 1.7.1, “MySQL Extensions to Standard SQL”](extensions-to-ansi.md)

[Section 6.5.4, “mysqldump — A Database Backup Program”](mysqldump.md)

[Section 10.9.3, “Optimizer Hints”](optimizer-hints.md)

[Section 11.2, “Schema Object Names”](identifiers.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

[Section 11.1.1, “String Literals”](string-literals.md)

### E

\[index top\]

### ERROR\_FOR\_DIVISION\_BY\_ZERO

[Section 14.26.3, “Expression Handling”](precision-math-expressions.md)

[Section A.3, “MySQL 26.10 FAQ: Server SQL Mode”](faqs-sql-modes.md)

[Section 14.26.5, “Precision Math Examples”](precision-math-examples.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

### H

\[index top\]

### HIGH\_NOT\_PRECEDENCE

[Section 11.5, “Expressions”](expressions.md)

[Section 14.4.1, “Operator Precedence”](operator-precedence.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

### I

\[index top\]

### IGNORE\_SPACE

[Section 15.1.22, “CREATE PROCEDURE and CREATE FUNCTION Statements”](create-procedure.md)

[Section 11.2.5, “Function Name Parsing and Resolution”](function-resolution.md)

[Section 6.5.1.1, “mysql Client Options”](mysql-command-options.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

### INTERPRET\_UTF8\_AS\_UTF8MB4

[Section 12.15, “Character Set Configuration”](charset-configuration.md)

[Section 12.3.8, “Character Set Introducers”](charset-introducer.md)

[Section 15.1.22, “CREATE PROCEDURE and CREATE FUNCTION Statements”](create-procedure.md)

[Section 19.5.1.31, “Replication and Server SQL Mode”](replication-features-sql-mode.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

[Section 12.9.3, “The utf8 Character Set (Deprecated alias)”](charset-unicode-utf8.md)

[Section 27.4.1, “Trigger Syntax and Examples”](trigger-syntax.md)

### N

\[index top\]

### NO\_AUTO\_VALUE\_ON\_ZERO

[Section 15.1.25, “CREATE TABLE Statement”](create-table.md)

[Section 13.1.6, “Numeric Type Attributes”](numeric-type-attributes.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

[Section 5.6.9, “Using AUTO\_INCREMENT”](example-auto-increment.md)

### NO\_BACKSLASH\_ESCAPES

[Section 14.17.4, “Functions That Modify JSON Values”](json-modification-functions.md)

[Section 14.8.2, “Regular Expressions”](regexp.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

[Section 14.8.1, “String Comparison Functions and Operators”](string-comparison-functions.md)

[Section 11.1.1, “String Literals”](string-literals.md)

[Section 13.5, “The JSON Data Type”](json.md)

### NO\_DIR\_IN\_CREATE

[Section 15.1.25, “CREATE TABLE Statement”](create-table.md)

[Section 19.5.1.10, “Replication and DIRECTORY Table Options”](replication-features-directory.md)

[Section 19.5.1.41, “Replication and Variables”](replication-features-variables.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

[Section 7.4.4, “The Binary Log”](binary-log.md)

### NO\_ENGINE\_SUBSTITUTION

[Section 15.1.11, “ALTER TABLE Statement”](alter-table.md)

[Section 15.1.25, “CREATE TABLE Statement”](create-table.md)

[Section 7.6.1, “Installing and Uninstalling Plugins”](plugin-loading.md)

[Section A.3, “MySQL 26.10 FAQ: Server SQL Mode”](faqs-sql-modes.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

[Section 18.1, “Setting the Storage Engine”](storage-engine-setting.md)

[Section 19.4.4, “Using Replication with Different Source and Replica Storage Engines”](replication-solutions-diffengines.md)

### NO\_UNSIGNED\_SUBTRACTION

[Section 14.6.1, “Arithmetic Operators”](arithmetic-functions.md)

[Section 14.10, “Cast Functions and Operators”](cast-functions.md)

[Section 13.1.1, “Numeric Data Type Syntax”](numeric-type-syntax.md)

[Section 13.1.7, “Out-of-Range and Overflow Handling”](out-of-range-and-overflow.md)

[Section 26.6, “Restrictions and Limitations on Partitioning”](partitioning-limitations.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

### NO\_ZERO\_DATE

[Section 13.2.5, “Automatic Initialization and Updating for TIMESTAMP and DATETIME”](timestamp-initialization.md)

[Section 14.10, “Cast Functions and Operators”](cast-functions.md)

[Section 15.1.25, “CREATE TABLE Statement”](create-table.md)

[Section 13.2, “Date and Time Data Types”](date-and-time-types.md)

[Section 14.7, “Date and Time Functions”](date-and-time-functions.md)

[Section 15.2.9, “LOAD DATA Statement”](load-data.md)

[Section A.3, “MySQL 26.10 FAQ: Server SQL Mode”](faqs-sql-modes.md)

[Section B.3.4.2, “Problems Using DATE Columns”](using-date.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

[Section 7.1.8, “Server System Variables”](server-system-variables.md)

[Section 13.2.2, “The DATE, DATETIME, and TIMESTAMP Types”](datetime.md)

### NO\_ZERO\_IN\_DATE

[Section 15.1.25, “CREATE TABLE Statement”](create-table.md)

[Section 13.2, “Date and Time Data Types”](date-and-time-types.md)

[Section 15.2.9, “LOAD DATA Statement”](load-data.md)

[Section A.3, “MySQL 26.10 FAQ: Server SQL Mode”](faqs-sql-modes.md)

[Section B.3.4.2, “Problems Using DATE Columns”](using-date.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

### O

\[index top\]

### ONLY\_FULL\_GROUP\_BY

[Section 5.3.4.8, “Counting Rows”](counting-rows.md)

[Section 14.19.2, “GROUP BY Modifiers”](group-by-modifiers.md)

[Section 14.25, “Miscellaneous Functions”](miscellaneous-functions.md)

[Section A.3, “MySQL 26.10 FAQ: Server SQL Mode”](faqs-sql-modes.md)

[Section 14.19.3, “MySQL Handling of GROUP BY”](group-by-handling.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

### P

\[index top\]

### PAD\_CHAR\_TO\_FULL\_LENGTH

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

[Section 13.3.1, “String Data Type Syntax”](string-type-syntax.md)

[Section 13.3.2, “The CHAR and VARCHAR Types”](char.md)

### PIPES\_AS\_CONCAT

[Section 11.5, “Expressions”](expressions.md)

[Section 14.4.3, “Logical Operators”](logical-operators.md)

[Section 14.4.1, “Operator Precedence”](operator-precedence.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

### R

\[index top\]

### REAL\_AS\_FLOAT

[Section 14.10, “Cast Functions and Operators”](cast-functions.md)

[Section 13.1.1, “Numeric Data Type Syntax”](numeric-type-syntax.md)

[Section 13.1, “Numeric Data Types”](numeric-types.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

### S

\[index top\]

### STRICT\_ALL\_TABLES

[Section 14.26.3, “Expression Handling”](precision-math-expressions.md)

[Section A.3, “MySQL 26.10 FAQ: Server SQL Mode”](faqs-sql-modes.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

### STRICT\_TRANS\_TABLES

[Section 14.26.3, “Expression Handling”](precision-math-expressions.md)

[Section A.3, “MySQL 26.10 FAQ: Server SQL Mode”](faqs-sql-modes.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

### T

\[index top\]

### TIME\_TRUNCATE\_FRACTIONAL

[Section 13.2.6, “Fractional Seconds in Time Values”](fractional-seconds.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

### TRADITIONAL

[Section 13.2.5, “Automatic Initialization and Updating for TIMESTAMP and DATETIME”](timestamp-initialization.md)

[Section 14.26.3, “Expression Handling”](precision-math-expressions.md)

[Section A.3, “MySQL 26.10 FAQ: Server SQL Mode”](faqs-sql-modes.md)

[Section 7.1.11, “Server SQL Modes”](sql-mode.md)

[Section 7.1.8, “Server System Variables”](server-system-variables.md)

[PREV](dynindex-priv.md) [HOME](index.md) [UP](indexes.md) [NEXT](dynindex-statement.md)

Related Documentation

[MySQL 26.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.10/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.10-en.pdf) - 42.3Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.10-en.a4.pdf) - 42.4Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.tar.gz) - 272.9Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.zip) - 379.1Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.10.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.10.info.zip) - 4.2Mb