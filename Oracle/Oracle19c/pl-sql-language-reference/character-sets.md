---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/character-sets.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Character Sets

Any character data to be processed by PL/SQL or stored in a database must be represented as a sequence of bytes. The byte representation of a single character is called a character code. A set of character codes is called a character set.

Every Oracle database supports a database character set and a national character set. PL/SQL also supports these character sets. This document explains how PL/SQL uses the database character set and national character set.

Topics

### Database Character Set

PL/SQL uses the database character set to represent:

- Stored source text of PL/SQL units
	For information about PL/SQL units, see " [PL/SQL Units and Compilation Parameters](architecture-pl-sql.md) ".
- Character values of data types `CHAR`, `VARCHAR2`, `CLOB`, and `LONG`
	For information about these data types, see " [SQL Data Types](sql-data-types.md) ".

The database character set can be either single-byte, mapping each supported character to one particular byte, or multibyte-varying-width, mapping each supported character to a sequence of one, two, three, or four bytes. The maximum number of bytes in a character code depends on the particular character set.

Every database character set includes these basic characters:

- Latin letters: A through Z and a through z
- Decimal digits: 0 through 9
- Punctuation characters in Table 2-1
- Whitespace characters: space, tab, new line, and carriage return

PL/SQL source text that uses only the basic characters can be stored and compiled in any database. PL/SQL source text that uses nonbasic characters can be stored and compiled only in databases whose database character sets support those nonbasic characters.

Table 2-1 Punctuation Characters in Every Database Character Set

| Symbol | Name |
| --- | --- |
| `(` | Left parenthesis |
| `)` | Right parenthesis |
| `<` | Left angle bracket |
| `>` | Right angle bracket |
| `+` | Plus sign |
| `-` | Hyphen or minus sign |
| `*` | Asterisk |
| `/` | Slash |
| `=` | Equal sign |
| `,` | Comma |
| `;` | Semicolon |
| `:` | Colon |
| `.` | Period |
| `!` | Exclamation point |
| `?` | Question mark |
| `'` | Apostrophe or single quotation mark |
| " | Quotation mark or double quotation mark |
| `@` | At sign |
| `%` | Percent sign |
| `#` | Number sign |
| `$` | Dollar sign |
| `_` | Underscore |
| `\|` | Vertical bar |

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=NLSPG171) for more information about the database character set

### National Character Set

PL/SQL uses the national character set to represent character values of data types `NCHAR`, `NVARCHAR2` and `NCLOB`.

See Also:

- " [SQL Data Types](sql-data-types.md) " for information about these data types
- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=NLSPG180) for more information about the national character set

### About Data-Bound Collation

Collation (also called sort ordering) is a set of rules that determines if a character string equals, precedes, or follows another string when the two strings are compared and sorted.

Different collations correspond to rules of different spoken languages. Collation-sensitive operations are operations that compare text and need a collation to control the comparison rules. The equality operator and the built-in function `INSTR` are examples of collation-sensitive operations.

Starting with Oracle Database 12c release 2 (12.2), a new architecture provides control of the collation to be applied to operations on character data. In the new architecture, collation becomes an attribute of character data, analogous to a data type. You can now declare collation for a column and this collation is automatically applied by all collation-sensitive SQL operations referencing the column. The data-bound collation feature uses syntax and semantics compatible with the ISO/IEC SQL standard.

The PL/SQL language has limited support for the data-bound collation architecture. All data processed in PL/SQL expressions is assumed to have the compatibility collation `USING_NLS_COMP`. This pseudo-collation instructs collation-sensitive operators to behave in the same way as in previous Oracle Database releases. That is, the values of the session parameters `NLS_COMP` and `NLS_SORT` determine the collation to use. However, all SQL statements embedded or constructed dynamically in PL/SQL fully support the new architecture.

A new property called default collation has been added to tables, views, materialized views, packages, stored procedures, stored functions, triggers, and types. The default collation of a unit determines the collation for data containers, such as columns, variables, parameters, literals, and return values, that do not have their own explicit collation declaration in that unit. The default collation for packages, stored procedures, stored functions, triggers, and types must be `USING_NLS_COMP`.

For syntax and semantics, see the [DEFAULT COLLATION Clause](DEFAULT-COLLATION-clause.md).

To facilitate the creation of PL/SQL units in a schema that has a schema default collation other than `USING_NLS_COMP`, the syntax and semantics for the following statements enable an explicit declaration of the object's default collation to be ` USING_NLS_COMP`:
- [CREATE FUNCTION Statement](CREATE-FUNCTION-statement.md)
- [CREATE PACKAGE Statement](CREATE-PACKAGE-statement.md)
- [CREATE PROCEDURE Statement](CREATE-PROCEDURE-statement.md)
- [CREATE TRIGGER Statement](CREATE-TRIGGER-statement.md)
- [CREATE TYPE Statement](CREATE-TYPE-statement.md)

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=NLSPG-GUID-D67BA73B-805F-429D-BA08-BC7DBF524F64) for more information about specifying data-bound collation for PL/SQL units
- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=NLSPG-GUID-F1F6A1EC-7ABF-45DF-9901-40576313A2EF) for more information about effective schema default collation