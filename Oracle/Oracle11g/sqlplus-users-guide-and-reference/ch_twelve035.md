---
title: REPFOOTER
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve035.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

REPF\[OOTER\] \[PAGE\] \[printspec \[text | variable\]...\] | \[ON | OFF\]

where printspec represents one or more of the following clauses used to place and format the text:

COL nS\[KIP\] \[n\]TAB nLE\[FT\]CE\[NTER\]R\[IGHT\]BOLD FORMAT text

Places and formats a specified report footer at the bottom of each report, or lists the current REPFOOTER definition.

Enter REPFOOTER with no clauses to list the current REPFOOTER definition.

Terms

See the [REPHEADER](ch_twelve036.md) command for additional information on terms and clauses in the REPFOOTER command syntax.

Usage

If you do not enter a printspec clause before the text or variables, REPFOOTER left justifies the text or variables.

You can use any number of constants and variables in a printspec. SQL\*Plus displays the constants and variables in the order you specify them, positioning and formatting each constant or variable as specified by the printspec clauses that precede it.

Note:

If SET EMBEDDED is ON, the report footer is suppressed.

Examples

To define "END EMPLOYEE LISTING REPORT" as a report footer on a separate page and to center it, enter:

```
REPFOOTER PAGE CENTER 'END EMPLOYEE LISTING REPORT'
TTITLE RIGHT 'Page: ' FORMAT 999 SQL.PNO
SELECT LAST_NAME, SALARY
FROM EMP_DETAILS_VIEW
WHERE SALARY > 12000;
```

```
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

                                                                      Page:  2
                           END EMPLOYEE LISTING REPORT

6 rows selected.
```

To suppress the report footer without changing its definition, enter

```
REPFOOTER OFF
```