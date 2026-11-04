---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/REPHEADER.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
REPH[EADER] [PAGE] [printspec [text | variable] ...]  | [ON | OFF
]
```

where printspec represents one or more of the following clauses used to place and format the text:

```
COL n S[KIP] [n] TAB n LE[FT] CE[NTER] R[IGHT] BOLD FORMAT text
```

Places and formats a specified report header at the top of each report, or lists the current REPHEADER definition.

Enter REPHEADER with no clauses to list the current REPHEADER definition.

Terms

These terms and clauses also apply to the REPFOOTER command.

```
PAGE
```

Begins a new page after printing the specified report header or before printing the specified report footer.

```
text
```

The report header or footer text. Enter text in single quotes if you want to place more than one word on a single line. The default is NULL.

```
variable
```

A substitution variable or any of the following system-maintained values. SQL.LNO is the current line number, SQL.PNO is the current page number, SQL.CODE is the current error code, SQL.RELEASE is the current Oracle Database release number, and SQL.USER is the current username.

To print one of these values, reference the appropriate variable in the report header or footer. You can use the FORMAT clause to format variable.

```
OFF
```

Turns the report header or footer off (suppresses its display) without affecting its definition.

```
COL n
```

Indents to column n of the current line (backward if column n has been passed). Column in this context means print position, not table column.

```
S[KIP] [n]
```

Skips to the start of a new line n times; if you omit n, one time; if you enter zero for n, backward to the start of the current line.

```
TAB n
```

Skips forward n columns (backward if you enter a negative value for n). Column in this context means print position, not table column.

```
LE[FT] CE[NTER] R[IGHT]
```

Left-align, center, and right-align data on the current line respectively. SQL\*Plus aligns following data items as a group, up to the end of the printspec or the next LEFT, CENTER, RIGHT, or COL command. CENTER and RIGHT use the SET LINESIZE value to calculate the position of the data item that follows.

```
BOLD
```

Prints data in bold print. SQL\*Plus represents bold print on your terminal by repeating the data on three consecutive lines. On some operating systems, SQL\*Plus may instruct your printer to print bold text on three consecutive lines, instead of bold.

```
FORMAT text
```

Specifies a format model that determines the format of data items up to the next FORMAT clause or the end of the command. The format model must be a text constant such as A10 or $999. See [COLUMN](COLUMN.md) for more information on formatting and valid format models.

If the datatype of the format model does not match the datatype of a given data item, the FORMAT clause has no effect on that item.

If no appropriate FORMAT model precedes a given data item, SQL\*Plus prints NUMBER values according to the format specified by SET NUMFORMAT or, if you have not used SET NUMFORMAT, the default format. SQL\*Plus prints DATE values using the default format.

Usage

If you do not enter a printspec clause before the text or variables, REPHEADER left justifies the text or variables.

You can use any number of constants and variables in a printspec. SQL\*Plus displays the constants and variables in the order you specify, positioning and formatting each constant or variable as specified by the printspec clauses that precede it.

Examples

To define "EMPLOYEE LISTING REPORT" as a report header on a separate page, and to center it, enter:

```
REPHEADER PAGE CENTER 'EMPLOYEE LISTING REPORT'
TTITLE RIGHT 'Page: ' FORMAT 999 SQL.PNO
SELECT LAST_NAME, SALARY
FROM EMP_DETAILS_VIEW
WHERE SALARY > 12000;
```
```
Page:   1
                             EMPLOYEE LISTING REPORT
                                                                 Page:   2
LAST_NAME                     SALARY
------------------------- ----------
King                           24000
Kochhar                        17000
De Haan                        17000
Russell                        14000
Partners                       13500
Hartstein                      13000
                          ----------
sum                            98500

6 rows selected.
```

To suppress the report header without changing its definition, enter:

```
REPHEADER OFF
```