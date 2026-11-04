---
title: BTITLE
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve010.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

BTI\[TLE\] \[printspec \[text | variable\]...\] | \[ON | OFF\]

where printspec represents one or more of the following clauses used to place and format the text:

BOLD

CE\[NTER\]

COL n

FORMAT text

LE\[FT\]

R\[IGHT\]

S\[KIP\] \[n\]

TAB n

Places and formats a specified title at the bottom of each report page, or lists the current BTITLE definition.

Enter BTITLE with no clauses to list the current BTITLE definition. For a description of the old form of BTITLE, see [BTI\[TLE\] text (obsolete old form)](https://docs.oracle.com/cd/E11882_01/server.112/e16604/apc.htm#i656733).

Terms

See the [TTITLE](ch_twelve048.md) command for information on terms and clauses in the BTITLE command syntax.

Usage

If you do not enter a printspec clause before the first occurrence of text, BTITLE left justifies the text. SQL\*Plus interprets BTITLE in the new form if a valid printspec clause (LEFT, SKIP, COL, and so on) immediately follows the command name.

SQL\*Plus substitution variables (& variables) are expanded before BTITLE is executed. The resulting string is stored as the BTITLE text. During subsequent execution for each page of results, the expanded value of a variable may itself be interpreted as a variable with unexpected results.

You can avoid this double substitution in a BTITLE command by not using the & prefix for variables that are to be substituted on each page of results. If you want to use a substitution variable to insert unchanging text in a BTITLE, enclose it in quotes so that it is only substituted once.

Examples

To set a bottom title with CORPORATE PLANNING DEPARTMENT on the left and a date on the right, enter

```
BTITLE LEFT 'CORPORATE PLANNING DEPARTMENT' -
RIGHT '1 JAN 2001'
```

To set a bottom title with CONFIDENTIAL in column 50, followed by six spaces and a date, enter

```
BTITLE COL 50 'CONFIDENTIAL' 
TAB 6 
'1 JAN 2001'
```