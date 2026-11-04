---
title: PL/SQL Language Fundamentals
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/fundamentals.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

## 2 PL/SQL Language Fundamentals

This chapter explains these aspects of the PL/SQL language:

## Character Sets

Any character data to be processed by PL/SQL or stored in a database must be represented as a sequence of bytes. The byte representation of a single character is called a character code. A set of character codes is called a character set.

Every Oracle database supports a database character set and a national character set. PL/SQL also supports these character sets. This document explains how PL/SQL uses the database character set and national character set.

Topics

- Database Character Set
- National Character Set

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch2charset.htm#NLSPG002) for general information about character sets

### Database Character Set

PL/SQL uses the database character set to represent:

- Stored source text of PL/SQL units
	For information about PL/SQL units, see ["PL/SQL Units and Compilation Parameters"](overview.md).
- Character values of data types `CHAR`, `VARCHAR2`, `CLOB`, and `LONG`
	For information about these data types, see ["SQL Data Types"](datatypes.md).

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

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch2charset.htm#NLSPG171) for more information about the database character set

### National Character Set

PL/SQL uses the national character set to represent character values of data types `NCHAR`, `NVARCHAR2` and `NCLOB`. For information about these data types, see ["SQL Data Types"](datatypes.md).

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch2charset.htm#NLSPG180) for more information about the national character set

## Lexical Units

The lexical units of PL/SQL are its smallest individual components—delimiters, identifiers, literals, and comments.

Topics

- Delimiters
- Identifiers
- Literals