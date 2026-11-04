---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/COMPUTE.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
COMP[UTE] [function [LAB[EL] text] ...     OF {expr | column | alias} ...     ON {expr | column | alias | REPORT | ROW} ...]
```

In combination with the BREAK command, calculates and prints summary lines, using various standard computations on subsets of selected rows. It also lists all COMPUTE definitions. For details on how to create summaries, see [About Clarifying Your Report with Spacing and Summary Lines](formatting-SQL-Plus-reports.md).

Terms

```
function ...
```

Represents one of the functions listed in Table 13-2. If you specify more than one function, use spaces to separate the functions.

COMPUTE command functions are always executed in the sequence AVG, COUNT, MINIMUM, MAXIMUM, NUMBER, SUM, STD, VARIANCE, regardless of their order in the COMPUTE command.

Table 13-2 COMPUTE Functions

| Function | Computes | Applies to Datatypes |
| --- | --- | --- |
| ``` AVG ``` | Average of non-null values | NUMBER |
| ``` COU[NT] ``` | Count of non-null values | all types |
| ``` MIN[IMUM] ``` | Minimum value | NUMBER, CHAR, NCHAR, VARCHAR2 (VARCHAR), NVARCHAR2 (NCHAR VARYING) |
| ``` MAX[IMUM] ``` | Maximum value | NUMBER, CHAR, NCHAR, VARCHAR2 (VARCHAR), NVARCHAR2 (NCHAR VARYING) |
| ``` NUM[BER] ``` | Count of rows | all types |
| ``` SUM ``` | Sum of non-null values | NUMBER |
| ``` STD ``` | Standard deviation of non-null values | NUMBER |
| ``` VAR[IANCE] ``` | Variance of non-null values | NUMBER |

```
LAB[EL] text
```

Defines the label to be printed for the computed value. If no LABEL clause is used, text defaults to the unabbreviated function keyword. You must place single quotes around text containing spaces or punctuation. The label prints left justified and truncates to the column width or linesize, whichever is smaller. The maximum label length is 500 characters.

The label for the computed value appears in the break column specified. To suppress the label, use the NOPRINT option of the COLUMN command on the break column.

If you repeat a function in a COMPUTE command, SQL\*Plus issues a warning and uses the first occurrence of the function.

With ON REPORT and ON ROW computations, the label appears in the first column listed in the SELECT statement. The label can be suppressed by using a NOPRINT column first in the SELECT statement. When you compute a function of the first column in the SELECT statement ON REPORT or ON ROW, then the computed value appears in the first column and the label is not displayed. To see the label, select a dummy column first in the SELECT list.

```
OF {expr | column | alias} ...
```

In the OF clause, you can refer to an expression or function reference in the SELECT statement by placing the expression or function reference in double quotes. Column names and aliases do not need quotes.

```
ON {expr | column | alias | REPORT | ROW} ...
```

If multiple COMPUTE commands reference the same column in the ON clause, only the last COMPUTE command applies.

To reference a SQL SELECT expression or function reference in an ON clause, place the expression or function reference in quotes. Column names and aliases do not need quotes.

Enter COMPUTE without clauses to list all COMPUTE definitions.

Usage

In order for the computations to occur, the following conditions must all be true:

- One or more of the expressions, columns, or column aliases you reference in the OF clause must also be in the SELECT command.
- The expression, column, or column alias you reference in the ON clause must occur in the SELECT command and in the most recent BREAK command.
- If you reference either ROW or REPORT in the ON clause, also reference ROW or REPORT in the most recent BREAK command.

To remove all COMPUTE definitions, use the CLEAR COMPUTES command.

Note that if you use the NOPRINT option for the column on which the COMPUTE is being performed, the COMPUTE result is also suppressed.

Examples

To subtotal the salary for the "account manager", AC\_MGR, and "salesman", SA\_MAN, job classifications with a compute label of "TOTAL", enter

```
BREAK ON JOB_ID SKIP 1;
COMPUTE SUM LABEL 'TOTAL' OF SALARY ON JOB_ID;
SELECT JOB_ID, LAST_NAME, SALARY
FROM EMP_DETAILS_VIEW
WHERE JOB_ID IN ('AC_MGR', 'SA_MAN')
ORDER BY JOB_ID, SALARY;
```
```
JOB_ID     LAST_NAME                     SALARY
---------- ------------------------- ----------
AC_MGR     Higgins                        12000
**********                           ----------
TOTAL                                     12000
SA_MAN     Zlotkey                        10500
           Cambrault                      11000
           Errazuriz                      12000
           Partners                       13500
           Russell                        14000
**********                           ----------
TOTAL                                     61000

6 rows selected.
```

To calculate the total of salaries greater than 12,000 on a report, enter

```
COMPUTE SUM OF SALARY ON REPORT
BREAK ON REPORT
COLUMN DUMMY HEADING ''
SELECT '   ' DUMMY, SALARY, EMPLOYEE_ID
FROM EMP_DETAILS_VIEW
WHERE SALARY > 12000
ORDER BY SALARY;
```
```
SALARY EMPLOYEE_ID
--- ---------- -----------
         13000         201
         13500         146
         14000         145
         17000         101
         17000         102
         24000         100
    ----------
sum      98500

6 rows selected.
```

To calculate the average and maximum salary for the executive and accounting departments, enter

```
BREAK ON DEPARTMENT_NAME SKIP 1
COMPUTE AVG LABEL 'Dept Average' -
        MAX LABEL 'Dept Maximum' -
        OF SALARY ON DEPARTMENT_NAME
SELECT DEPARTMENT_NAME, LAST_NAME, SALARY
FROM EMP_DETAILS_VIEW
WHERE DEPARTMENT_NAME IN ('Executive', 'Accounting')
ORDER BY DEPARTMENT_NAME;
```
```
DEPARTMENT_NAME                LAST_NAME                     SALARY
------------------------------ ------------------------- ----------
Accounting                     Higgins                        12000
                               Gietz                           8300
******************************                           ----------
Dept Average                                                  10150
Dept Maximum                                                  12000

Executive                      King                           24000
                               Kochhar                        17000
                               De Haan                        17000
******************************                           ----------
Dept Average                                             19333.3333
Dept Maximum                                                  24000
```

To sum salaries for departments <= 20 without printing the compute label, enter

```
COLUMN DUMMY NOPRINT
COMPUTE SUM OF SALARY ON DUMMY
BREAK ON DUMMY SKIP 1
SELECT DEPARTMENT_ID DUMMY, DEPARTMENT_ID, LAST_NAME, SALARY
FROM EMP_DETAILS_VIEW
WHERE DEPARTMENT_ID <= 20
ORDER BY DEPARTMENT_ID;
```
```
DEPARTMENT_ID LAST_NAME                     SALARY
------------- ------------------------- ----------
           10 Whalen                          4400
                                        ----------
                                              4400

           20 Hartstein                      13000
           20 Fay                             6000
                                        ----------
                                             19000
```

To total the salary at the end of the report without printing the compute label, enter

```
COLUMN DUMMY NOPRINT
COMPUTE SUM OF SALARY ON DUMMY
BREAK ON DUMMY
SELECT NULL DUMMY, DEPARTMENT_ID, LAST_NAME, SALARY
FROM EMP_DETAILS_VIEW
WHERE DEPARTMENT_ID <= 30
ORDER BY DEPARTMENT_ID;
```
```
DEPARTMENT_ID LAST_NAME                     SALARY
------------- ------------------------- ----------
           10 Whalen                          4400
           20 Hartstein                      13000
           20 Fay                             6000
           30 Raphaely                       11000
           30 Khoo                            3100
           30 Baida                           2900
           30 Tobias                          2800
           30 Himuro                          2600
           30 Colmenares                      2500
                                        ----------
                                             48300

9 rows selected.
```