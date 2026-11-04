---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/COLUMN.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
COL[UMN] [{column | expr} [option ...]]
```

where option represents one of the following clauses:

```
ALI[AS] alias CLE[AR] ENTMAP {ON | OFF} FOLD_A[FTER] FOLD_B[EFORE] FOR[MAT] format HEA[DING] text JUS[TIFY] {L[EFT] | C[ENTER] | R[IGHT]} LIKE {expr | alias} NEWL[INE] NEW_V[ALUE] variable NOPRI[NT] | PRI[NT]
 NUL[L] text OLD_V[ALUE] variable ON | OFF WRA[PPED]
 | WOR[D_WRAPPED] | TRU[NCATED]
```

Specifies display attributes for a given column, such as

- text for the column heading
- alignment of the column heading
- format for NUMBER data
- wrapping of column data

Also lists the current display attributes for a single column or all columns.

Enter COLUMN followed by column or expr and no other clauses to list the current display attributes for only the specified column or expression. Enter COLUMN with no clauses to list all current column display attributes.

Terms

```
{column | expr}
```

Identifies the data item (typically, the name of a column) in a SQL SELECT command to which the column command refers. If you use an expression in a COLUMN command, you must enter expr exactly as it appears in the SELECT command. If the expression in the SELECT command is a+b, for example, you cannot use b+a or (a+b) in a COLUMN command to refer to the expression in the SELECT command.

If you select columns with the same name from different tables, a COLUMN command for that column name will apply to both columns. That is, a COLUMN command for the column LAST\_NAME applies to all columns named LAST\_NAME that you reference in this session. COLUMN ignores table name prefixes in SELECT commands. Also, spaces are ignored unless the name is placed in double quotes.

To format the columns differently, assign a unique alias to each column within the SELECT command itself (do not use the ALIAS clause of the COLUMN command) and enter a COLUMN command for each column's alias.

```
ALI[AS] alias
```

Assigns a specified alias to a column, which can be used to refer to the column in BREAK, COMPUTE, and other COLUMN commands.

```
CLE[AR]
```

Resets the display attributes for the column to default values.

To reset the attributes for all columns, use the CLEAR COLUMNS command. CLEAR COLUMNS also clears the ATTRIBUTEs for that column.

```
ENTMAP {ON | OFF}
```

Enables entity mapping to be turned on or off for selected columns in HTML output. This feature enables you to include, for example, HTML hyperlinks in a column of data, while still mapping entities in other columns of the same report. By turning entity mapping off for a column containing HTML hyperlinks, the HTML anchor tag delimiters, <, >, " and &, are correctly interpreted in the report. Otherwise they would be replaced with their respective entities, &lt;, &gt;, &quot; and &amp;, preventing web browsers from correctly interpreting the HTML.

Entities in the column heading and any COMPUTE labels or output appearing in the column are mapped or not mapped according to the value of ENTMAP for the column.

The default setting for COLUMN ENTMAP is the current setting of the MARKUP HTML ENTMAP option.

For more information about the MARKUP HTML ENTMAP option, see SET [MARKUP Options](starting-SQL-Plus.md).

```
FOLD_A[FTER]
```

Inserts a carriage return after the column heading and after each row in the column. SQL\*Plus does not insert an extra carriage return after the last column in the SELECT list. FOLD\_A\[FTER\] does not work in SET MARKUP HTML ON mode unless PREFORMAT is set ON.

```
FOLD_B[EFORE]
```

Inserts a carriage return before the column heading and before each row of the column. SQL\*Plus does not insert an extra carriage return before the first column in the SELECT list. FOLD\_A\[FTER\] does not work in SET MARKUP HTML ON mode unless PREFORMAT is set ON.

```
FOR[MAT] format
```

Specifies the display format of the column. The format specification must be a text constant such as A10 or $9,999.

Character Columns

The default width of CHAR, NCHAR, VARCHAR2 (VARCHAR) and NVARCHAR2 (NCHAR VARYING) columns is the width of the column in the database. SQL\*Plus formats these datatypes left-justified. If a value does not fit within the column width, SQL\*Plus wraps or truncates the character string depending on the setting of SET WRAP.

A LONG, BLOB, BFILE, CLOB, NCLOB XMLType or JSON column's width defaults to the value of SET LONGCHUNKSIZE or SET LONG, whichever one is smaller.

To change the width of a datatype to n, use FORMAT An. (A stands for alphabetic.) If you specify a width shorter than the column heading, SQL\*Plus truncates the heading.

SQL\*Plus truncates or wraps XMLType columns after 2000 bytes. To avoid this you need to set an explicit COLUMN format for the XMLType column. A COLUMN format can be up to a maximum of 60000 per row.

DATE Columns

The default width and format of unformatted DATE columns in SQL\*Plus is derived from the NLS\_DATE\_FORMAT parameter. The NLS\_DATE\_FORMAT setting is determined by the NLS territory parameter. For example, the default format for the NLS territory, America, is DD-Mon-RR, and the default width is A9. The NLS parameters may be set in your database parameter file, in environment variables or an equivalent platform-specific mechanism. They may also be specified for each session with the ALTER SESSION command. For more information about DATE formats, and about NLS parameters, see the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=SQLRF).

You can change the format of any DATE column using the SQL function TO\_CHAR in your SQL SELECT statement. You may also wish to use an explicit COLUMN FORMAT command to adjust the column width.

When you use SQL functions like TO\_CHAR, Oracle Database automatically enables a very wide column. The default column width may also depend on the character sets in use in SQL\*Plus and in the database. To maximize script portability if multiple characters sets are used, Oracle Database recommends using COLUMN FORMAT for each column selected.

To change the width of a DATE column to n, use the COLUMN command with FORMAT An. If you specify a width shorter than the column heading, the heading is truncated.

NUMBER Columns

For numeric columns, COLUMN FORMAT settings take precedence over SET NUMFORMAT settings, which take precedence over SET NUMWIDTH settings.

See [SET NUMF\[ORMAT\] format](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-729CE19A-7022-4381-A209-DE92CD5F7C6F) and [SET NUM\[WIDTH\] {10 | n}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-BEC116D1-AEF3-499F-BDAB-4EAC4A149655).

To change a NUMBER column's width, use FORMAT followed by an element as specified in Table 13-1.

Table 13-1 Number Formats

| Element | Examples | Description |
| --- | --- | --- |
| , (comma) | ``` 9,999 ``` | Displays a comma in the specified position. |
| . (period) | ``` 99.99 ``` | Displays a period (decimal point) to separate the integral and fractional parts of a number. |
| $ | ``` $9999 ``` | Displays a leading dollar sign. |
| 0 | ``` 0999 9990 ``` | Displays leading zeros Displays trailing zeros. |
| 9 | ``` 9999 ``` | Displays a value with the number of digits specified by the number of 9s. Value has a leading space if positive, a leading minus sign if negative. Blanks are displayed for leading zeroes. A zero (0) is displayed for a value of zero. |
| B | ``` B9999 ``` | Displays blanks for the integer part of a fixed-point number when the integer part is zero, regardless of zeros in the format model. |
| C | ``` C999 ``` | Displays the ISO currency symbol in the specified position. |
| D | ``` 99D99 ``` | Displays the decimal character to separate the integral and fractional parts of a number. |
| EEEE | ``` 9.999EEEE ``` | Displays value in scientific notation (format must contain exactly four "E"s). |
| G | ``` 9G999 ``` | Displays the group separator in the specified positions in the integral part of a number. |
| L | ``` L999 ``` | Displays the local currency symbol in the specified position. |
| MI | ``` 9999MI ``` | Displays a trailing minus sign after a negative value. Display a trailing space after a positive value. |
| PR | ``` 9999PR ``` | Displays a negative value in \<angle brackets>. Displays a positive value with a leading and trailing space. |
| RN rn | ``` RN rn ``` | Displays uppercase Roman numerals. Displays lowercase Roman numerals. Value can be an integer between 1 and 3999. |
| S | ``` S9999 9999S ``` | Displays a leading minus or plus sign. Displays a trailing minus or plus sign. |
| TM | ``` TM ``` | Displays the smallest number of decimal characters possible. The default is TM9. Fixed notation is used for output up to 64 characters, scientific notation for more than 64 characters. Cannot precede TM with any other element. TM can only be followed by a single 9 or E |
| U | ``` U9999 ``` | Displays the dual currency symbol in the specified position. |
| V | ``` 999V99 ``` | Displays value multiplied by 10n, where n is the number of 9's after the V. |
| X | ``` XXXX xxxx ``` | Displays the hexadecimal value for the rounded value of the specified number of digits. |

The MI and PR format elements can only appear in the last position of a number format model. The S format element can only appear in the first or last position.

If a number format model does not contain the MI, S or PR format elements, negative return values automatically contain a leading negative sign and positive values automatically contain a leading space.

A number format model can contain only a single decimal character (D) or period (.), but it can contain multiple group separators (G) or commas (,). A group separator or comma cannot appear to the right of a decimal character or period in a number format model.

SQL\*Plus formats NUMBER data right-justified. A NUMBER column's width equals the width of the heading or the width of the FORMAT plus one space for the sign, whichever is greater. If you do not explicitly use COLUMN FORMAT or SET NUMFORMAT, then the column's width will always be at least the value of SET NUMWIDTH.

SQL\*Plus may round your NUMBER data to fit your format or field width.

If a value cannot fit in the column, SQL\*Plus displays pound signs (#) instead of the number.

If a positive value is extremely large and a numeric overflow occurs when rounding a number, then the infinity sign (~) replaces the value. Likewise, if a negative value is extremely small and a numeric overflow occurs when rounding a number, then the negative infinity sign replaces the value (-~).

```
HEA[DING] text
```

Defines a column heading. If you do not use a HEADING clause, the column's heading defaults to column or expr. If text contains blanks or punctuation characters, you must enclose it with single or double quotes. Each occurrence of the HEADSEP character (by default, "|") begins a new line.

For example,

```
COLUMN LAST_NAME HEADING 'Employee |Name'
```

would produce a two-line column heading.

See [SET HEADS\[EP\] { | c | ON | OFF}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-6E015894-FF93-4F48-A679-A452FAD87BCC) for information on changing the HEADSEP character.

```
JUS[TIFY] {L[EFT] | C[ENTER] | R[IGHT]}
```

Aligns the heading. If you do not use a JUSTIFY clause, headings for NUMBER columns default to RIGHT and headings for other column types default to LEFT.

```
LIKE {expr | alias}
```

Copies the display attributes of another column or expression (whose attributes you have already defined with another COLUMN command). LIKE copies only attributes not defined by another clause in the current COLUMN command.

```
NEWL[INE]
```

Starts a new line before displaying the column's value. NEWLINE has the same effect as FOLD\_BEFORE. NEWL\[INE\] does not work in SET MARKUP HTML ON mode unless PREFORMAT is SET ON.

```
NEW_V[ALUE] variable
```

Specifies a variable to hold a column value. You can reference the variable in TTITLE commands. Use NEW\_VALUE to display column values or the date in the top title. You must include the column in a BREAK command with the SKIP PAGE action. The variable name cannot contain a pound sign (#).

NEW\_VALUE is useful for master/detail reports in which there is a new master record for each page. For master/detail reporting, you must also include the column in the ORDER BY clause. See the example at the end of this command description.

Variables specified with NEW\_V\[ALUE\] are expanded before TTITLE is executed. The resulting string is stored as the TTITLE text. During subsequent execution for each page of the report, the expanded value of a variable may itself be interpreted as a variable with unexpected results.

You can avoid this double substitution in a TTITLE command by not using the & prefix for NEW\_V\[ALUE\] variables that are to be substituted on each page of the report. If you want to use a substitution variable to insert unchanging text in a TTITLE, enclose it in quotes so that it is only substituted once.

For information on displaying a column value in the bottom title, see OLD\_V\[ALUE\] variable below. For more information on referencing variables in titles, see the [TTITLE](TTITLE.md) command. For information on formatting and valid format models, see FOR\[MAT\] format above.

```
NOPRI[NT] | PRI[NT]
```

Controls the printing of the column (the column heading and all the selected values). NOPRINT turns off the screen output and printing of the column. PRINT turns the printing of the column ON.

```
NUL[L] text
```

Controls the text SQL\*Plus displays for null values in the given column. The default is a white space. SET NULL controls the text displayed for all null values for all columns, unless overridden for a specific column by the NULL clause of the COLUMN command. When a NULL value is selected, a variable's type always becomes CHAR so the SET NULL text can be stored in it.

```
OLD_V[ALUE] variable
```

Specifies a variable to hold a column value. You can reference the variable in BTITLE commands. Use OLD\_VALUE to display column values in the bottom title. You must include the column in a BREAK command with the SKIP PAGE action.

OLD\_VALUE is useful for master/detail reports in which there is a new master record for each page. For master/detail reporting, you must also include the column in the ORDER BY clause.

Variables specified with OLD\_V\[ALUE\] are expanded before BTITLE is executed. The resulting string is stored as the BTITLE text. During subsequent execution for each page of the report, the expanded value of a variable may itself be interpreted as a variable with unexpected results.

You can avoid this double substitution in a BTITLE command by not using the & prefix for OLD\_V\[ALUE\] variables that are to be substituted on each page of the report. If you want to use a substitution variable to insert unchanging text in a BTITLE, enclose it in quotes so that it is only substituted once.

For information on displaying a column value in the top title, see NEW\_V\[ALUE\] variable. For more information on referencing variables in titles, see the [TTITLE](TTITLE.md) command.

```
ON | OFF
```

Controls the status of display attributes for a column. OFF disables the attributes for a column without affecting the attributes' definition. ON reinstates the attributes.

```
WRA[PPED] | WOR[D_WRAPPED] | TRU[NCATED]
```

Specifies how SQL\*Plus will treat a datatype or DATE string that is too wide for a column. WRAPPED wraps the string within the column bounds, beginning new lines when required. When WORD\_WRAP is enabled, SQL\*Plus left justifies each new line, skipping all leading whitespace (for example, returns, newline characters, tabs and spaces), including embedded newline characters. Embedded whitespace not on a line boundary is not skipped. TRUNCATED truncates the string at the end of the first line of display.

NCLOB, BLOB, BFILE or multibyte CLOB columns cannot be formatted with the WORD\_WRAPPED option. If you format an NCLOB, BLOB, BFILE or multibyte CLOB column with COLUMN WORD\_WRAPPED, the column data behaves as though COLUMN WRAPPED was applied instead.

Usage

The COLUMN commands you enter can control a column's display attributes for multiple SQL SELECT commands.

You can enter any number of COLUMN commands for one or more columns. All column attributes set for each column remain in effect for the remainder of the session, until you turn the column OFF, or until you use the CLEAR COLUMN command.

When you enter multiple COLUMN commands for the same column, SQL\*Plus applies their clauses collectively. If several COLUMN commands apply the same clause to the same column, the last one entered will control the output.

Examples

To make the LAST\_NAME column 20 characters wide and display EMPLOYEE NAME on two lines as the column heading, enter

```
COLUMN LAST_NAME FORMAT A20 HEADING 'EMPLOYEE|NAME'
```

To format the SALARY column so that it shows millions of dollars, rounds to cents, uses commas to separate thousands, and displays $0.00 when a value is zero, enter

```
COLUMN SALARY FORMAT $9,999,990.99
```

To assign the alias NET to a column containing a long expression, to display the result in a dollar format, and to display \<NULL> for null values, you might enter

```
COLUMN SALARY+COMMISSION_PCT+BONUS-EXPENSES-INS-TAX ALIAS NET
COLUMN NET FORMAT $9,999,999.99 NULL '<NULL>'
```

Note that the example divides this column specification into two commands. The first defines the alias NET, and the second uses NET to define the format.

Also note that in the first command you must enter the expression exactly as you enter it in the SELECT command. Otherwise, SQL\*Plus cannot match the COLUMN command to the appropriate column.

To wrap long values in a column named REMARKS, you can enter

```
COLUMN REMARKS FORMAT A20 WRAP
```
```
CUSTOMER     DATE        QUANTITY REMARKS
----------   ---------   -------- --------------------
123          25-AUG-2001 144      This order must be s
                                  hipped by air freigh
                                  t to ORD
```

If you replace WRAP with WORD\_WRAP, REMARKS looks like this:

```
CUSTOMER     DATE        QUANTITY   REMARKS
----------   ---------   --------   ---------------------
123          25-AUG-2001 144        This order must be
                                    shipped by air freight
                                    to ORD
```

If you specify TRUNCATE, REMARKS looks like this:

```
CUSTOMER     DATE        QUANTITY   REMARKS
----------   ---------   --------   --------------------
123          25-AUG-2001 144        This order must be s
```

To print the current date and the name of each job in the top title, enter the following. Use the EMPLOYEES table of the HR schema instead of EMP\_DETAILS\_VIEW.

For details on creating a date variable, see [About Displaying the Current Date in Titles](formatting-SQL-Plus-reports.md).

Your two page report would look similar to the following report, with "Job Report" centered within your current linesize:

```
COLUMN JOB_ID NOPRINT NEW_VALUE JOBVAR
COLUMN TODAY  NOPRINT NEW_VALUE DATEVAR
BREAK ON JOB_ID SKIP PAGE ON TODAY
TTITLE CENTER 'Job Report' RIGHT DATEVAR  SKIP 2 -
LEFT 'Job:     ' JOBVAR SKIP 2
SELECT TO_CHAR(SYSDATE, 'MM/DD/YYYY') TODAY,
LAST_NAME, JOB_ID, MANAGER_ID, HIRE_DATE, SALARY, DEPARTMENT_ID
FROM EMPLOYEES WHERE JOB_ID IN ('MK_MAN', 'SA_MAN')
ORDER BY JOB_ID, LAST_NAME;
```

To change the default format of DATE columns to 'YYYY-MM-DD', you can enter

```
ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD';
```
```
Session altered.
```

To display the change, enter a SELECT statement, such as:

```
SELECT HIRE_DATEFROM EMPLOYEESWHERE EMPLOYEE_ID = 206;
```
```
Job Report                         04/19/01

Job:     SA_MAN

HIRE_DATE
----------
1994-06-07
```

See [ALTER SESSION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=SQLRF-GUID-27186B28-7EFC-4998-B1ED-2B905CC0211B) for information on the ALTER SESSION command.