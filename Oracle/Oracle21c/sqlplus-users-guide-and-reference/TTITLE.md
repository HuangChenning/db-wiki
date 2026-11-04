---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/TTITLE.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
TTI[TLE] [printspec [text | variable] ...] [ON | OFF
]
```

where printspec represents one or more of the following clauses used to place and format the text:

```
BOLD CE[NTER] COL n FORMAT text LE[FT] R[IGHT] S[KIP] [n] TAB n
```

Places and formats a specified title at the top of each report page. Enter TTITLE with no clauses to list its current definition. The old form of TTITLE is used if only a single word or string in quotes follows the TTITLE command.

See [TTI\[TLE\] text (obsolete old form)](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/obsolete-SQL-Plus-commands.html#GUID-865E4EF3-21ED-4C12-AFF0-3DA3EC2C4EE3) for a description of the old form of TTITLE.

Terms

These terms and clauses also apply to the BTITLE command.

```
text
```

The title text. Enter text in single quotes if you want to place more than one word on a single line.

```
variable
```

A substitution variable or any of the following system-maintained values, SQL.LNO (the current line number), SQL.PNO (the current page number), SQL.RELEASE (the current Oracle Database release number), SQL.SQLCODE (the current error code), or SQL.USER (the current username).

To print one of these values, reference the appropriate variable in the title. You can format variable with the FORMAT clause.

SQL\*Plus substitution variables (& variables) are expanded before TTITLE is executed. The resulting string is stored as the TTITLE text. During subsequent execution for each page of results, the expanded value of a variable may itself be interpreted as a substitution variable with unexpected results.

You can avoid this double substitution in a TTITLE command by not using the & prefix for variables that are to be substituted on each page of results. If you want to use a substitution variable to insert unchanging text in a TTITLE, enclose it in quotes so that it is only substituted once.

```
OFF
```

Turns the title off (suppresses its display) without affecting its definition.

```
ON
```

Turns the title on (restores its display). When you define a top title, SQL\*Plus automatically sets TTITLE to ON.

```
COL n
```

Indents to column n of the current line (backward if column n has been passed). Here "column" means print position, not table column.

```
S[KIP] [n]
```

Skips to the start of a new line n times; if you omit n, one time; if you enter zero for n, backward to the start of the current line.

```
TAB n
```

Skips forward n columns (backward if you enter a negative value for n). "Column" in this context means print position, not table column.

```
LE[FT] | CE[NTER] | R[IGHT]
```

Left-align, center, and right-align data on the current line respectively. SQL\*Plus aligns following data items as a group, up to the end of the printspec or the next LEFT, CENTER, RIGHT, or COL command. CENTER and RIGHT use the SET LINESIZE value to calculate the position of the data item that follows.

```
BOLD
```

Prints data in bold print. SQL\*Plus represents bold print on your terminal by repeating the data on three consecutive lines. On some operating systems, SQL\*Plus may instruct your printer to print bold text on three consecutive lines, instead of bold.

```
FORMAT text
```

Specifies a format model that determines the format of following data items, up to the next FORMAT clause or the end of the command. The format model must be a text constant such as A10 or $999. See the [COLUMN](COLUMN.md) command for more information on formatting and valid format models.

If the datatype of the format model does not match the datatype of a given data item, the FORMAT clause has no effect on that item.

If no appropriate FORMAT model precedes a given data item, SQL\*Plus prints NUMBER values using the format specified by SET NUMFORMAT or, if you have not used SET NUMFORMAT, the default format. SQL\*Plus prints DATE values according to the default format.

Enter TTITLE with no clauses to list the current TTITLE definition.

Usage

If you do not enter a printspec clause before the first occurrence of text, TTITLE left justifies the text. SQL\*Plus interprets TTITLE in the new form if a valid printspec clause (LEFT, SKIP, COL, and so on) immediately follows the command name.

See [COLUMN](COLUMN.md) for information on printing column and DATE values in the top title.

You can use any number of constants and variables in a printspec. SQL\*Plus displays them in the order you specify them, positioning and formatting each constant or variable as specified by the printspec clauses that precede it.

The length of the title you specify with TTITLE cannot exceed 2400 characters.

The continuation character (a hyphen) will not be recognized inside a single-quoted title text string. To be recognized, the continuation character must appear outside the quotes, as follows:

```
TTITLE CENTER 'Summary Report for' -
> 'the Month of May'
```

Examples

To define "Monthly Analysis" as the top title and to left-align it, to center the date, to right-align the page number with a three-digit format, and to display "Data in Thousands" in the center of the next line, enter

```
TTITLE LEFT 'Monthly Analysis' CENTER '01 Jan 2003' -
RIGHT 'Page:' FORMAT 999 SQL.PNO SKIP CENTER -
'Data in Thousands'
```
```
Monthly Analysis                01 Jan 2003                      Page: 1
                              Data in Thousands
```

To suppress the top title display without changing its definition, enter

```
TTITLE OFF
```