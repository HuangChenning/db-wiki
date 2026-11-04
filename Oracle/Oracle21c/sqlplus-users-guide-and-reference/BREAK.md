---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/BREAK.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
BRE[AK] [ON report_element [action [action]]] ...
```

where report\_element has the syntax {column|expr|ROW|REPORT}

and action has the syntax \[SKI\[P\] n|\[SKI\[P\]\] PAGE\] \[NODUP\[LICATES\]|DUP\[LICATES\]\]

Specifies where changes occur in a report and the formatting action to perform, such as:

- suppressing display of duplicate values for a given column
- skipping a line each time a given column value changes
- printing computed figures each time a given column value changes or at the end of the report.
	See the [COMPUTE](COMPUTE.md) command.

Enter BREAK with no clauses to list the current BREAK definition.

Terms

```
ON column [action [action]]
```

When you include actions, specifies actions for SQL\*Plus to take whenever a break occurs in the specified column (called the break column). (column cannot have a table or view appended to it. To achieve this, you can alias the column in the SQL statement.) A break is one of three events, a change in the value of a column or expression, the output of a row, or the end of a report

When you omit actions, BREAK ON column suppresses printing of duplicate values in column and marks a place in the report where SQL\*Plus will perform the computation you specify in a corresponding COMPUTE command.

You can specify ON column one or more times. If you specify multiple ON clauses, as in

```
BREAK ON DEPARTMENT_ID SKIP PAGE ON JOB_ID - 
SKIP 1 ON SALARY SKIP 1
```

the first ON clause represents the outermost break (in this case, ON DEPARTMENT\_ID) and the last ON clause represents the innermost break (in this case, ON SALARY). SQL\*Plus searches each row of output for the specified breaks, starting with the outermost break and proceeding—in the order you enter the clauses—to the innermost. In the example, SQL\*Plus searches for a change in the value of DEPARTMENT\_ID, then JOB\_ID, then SALARY.

Next, SQL\*Plus executes actions beginning with the action specified for the innermost break and proceeding in reverse order toward the outermost break (in this case, from SKIP 1 for ON SALARY toward SKIP PAGE for ON DEPARTMENT\_ID). SQL\*Plus executes each action up to and including the action specified for the first break encountered in the initial search.

If, for example, in a given row the value of JOB\_ID changes—but the values of DEPARTMENT\_ID and SALARY remain the same—SQL\*Plus skips two lines before printing the row (one as a result of SKIP 1 ON SALARY and one as a result of SKIP 1 ON JOB\_ID).

Whenever you use ON column, you should also use an ORDER BY clause in the SQL SELECT command. Typically, the columns used in the BREAK command should appear in the same order in the ORDER BY clause (although all columns specified in the ORDER BY clause need not appear in the BREAK command). This prevents breaks from occurring at meaningless points in the report.

If the BREAK command specified earlier in this section is used, the following SELECT command produces meaningful results:

```
SELECT DEPARTMENT_ID, JOB_ID, SALARY, LAST_NAME
FROM EMP_DETAILS_VIEW
WHERE SALARY > 12000
ORDER BY DEPARTMENT_ID, JOB_ID, SALARY, LAST_NAME;
```

All rows with the same DEPARTMENT\_ID print together on one page, and within that page all rows with the same JOB\_ID print in groups. Within each group of jobs, those jobs with the same SALARY print in groups. Breaks in LAST\_NAME cause no action because LAST\_NAME does not appear in the BREAK command.

In BREAK commands, nulls are considered equal to each other, but not equal to anything else. This is different to the treatment of nulls in WHERE clauses.

```
ON expr [action [action]]
```

When you include actions, specifies actions for SQL\*Plus to take when the value of the expression changes.

When you omit actions, BREAK ON expr suppresses printing of duplicate values of expr and marks where SQL\*Plus will perform the computation you specify in a corresponding COMPUTE command.

You can use an expression involving one or more table columns or an alias assigned to a report column in a SQL SELECT or SQL\*Plus COLUMN command. If you use an expression in a BREAK command, you must enter expr exactly as it appears in the SELECT command. If the expression in the SELECT command is a+b, for example, you cannot use b+a or (a+b) in a BREAK command to refer to the expression in the SELECT command.

The information given for ON column also applies to ON expr.

```
ON ROW [action [action]]
```

When you include actions, specifies actions for SQL\*Plus to take when a SQL SELECT command returns a row. The ROW break becomes the innermost break regardless of where you specify it in the BREAK command. You should always specify an action when you BREAK on a row.

```
ON REPORT [action]
```

Marks a place in the report where SQL\*Plus will perform the computation you specify in a corresponding COMPUTE command. Use BREAK ON REPORT in conjunction with COMPUTE to print grand totals or other "grand" computed values.

The REPORT break becomes the outermost break regardless of where you specify it in the BREAK command.

Note that SQL\*Plus will not skip a page at the end of a report, so you cannot use BREAK ON REPORT SKIP PAGE.

```
SKI[P] n
```

Skips n lines before printing the row where the break occurred. BREAK SKIP n does not work in SET MARKUP HTML ON mode unless PREFORMAT is SET ON.

```
[SKI[P]] PAGE
```

Skips the number of lines that are defined to be a page before printing the row where the break occurred. The number of lines per page can be set with the PAGESIZE clause of the SET command. Note that PAGESIZE only changes the number of lines that SQL\*Plus considers to be a page. Therefore, SKIP PAGE may not always cause a physical page break, unless you have also specified NEWPAGE 0. Note also that if there is a break after the last row of data to be printed in a report, SQL\*Plus will not skip the page.

```
NODUP[LICATES]
```

Prints blanks rather than the value of a break column when the value is a duplicate of the column's value in the preceding row.

```
DUP[LICATES]
```

Prints the value of a break column in every selected row.

Enter BREAK with no clauses to list the current break definition.

Usage

Each new BREAK command you enter replaces the preceding one.

To remove the BREAK command, use CLEAR BREAKS.

Examples

To produce a report that prints duplicate job values, prints the average of SALARY, and additionally prints the sum of SALARY, you could enter the following commands. (The example selects departments 50 and 80 and the jobs of clerk and salesman only.)

```
BREAK ON DEPARTMENT_ID ON JOB_ID DUPLICATES
COMPUTE SUM OF SALARY ON DEPARTMENT_ID
COMPUTE AVG OF SALARY ON JOB_ID
SELECT DEPARTMENT_ID, JOB_ID, LAST_NAME, SALARY
FROM EMP_DETAILS_VIEW
WHERE JOB_ID IN ('SH_CLERK', 'SA_MAN')
AND DEPARTMENT_ID IN (50, 80)
ORDER BY DEPARTMENT_ID, JOB_ID;
```
```
DEPARTMENT_ID JOB_ID     LAST_NAME                     SALARY
------------- ---------- ------------------------- ----------
           50 SH_CLERK   Taylor                          3200
              SH_CLERK   Fleaur                          3100
                 .
                 .
                 .
              SH_CLERK   Gates                           2900

DEPARTMENT_ID JOB_ID     LAST_NAME                     SALARY
------------- ---------- ------------------------- ----------
           50 SH_CLERK   Perkins                         2500
              SH_CLERK   Bell                            4000
                 .
                 .
                 .
              SH_CLERK   Grant                           2600
              **********                           ----------
              avg                                        3215

DEPARTMENT_ID JOB_ID     LAST_NAME                     SALARY
------------- ---------- ------------------------- ----------

*************                                      ----------
sum                                                     64300

           80 SA_MAN     Russell                        14000
              SA_MAN     Partners                       13500
              SA_MAN     Errazuriz                      12000
              SA_MAN     Cambrault                      11000
              SA_MAN     Zlotkey                        10500
              **********                           ----------
              avg                                       12200

DEPARTMENT_ID JOB_ID     LAST_NAME                     SALARY
------------- ---------- ------------------------- ----------

*************                                      ----------
sum                                                     61000

25 rows selected.
```