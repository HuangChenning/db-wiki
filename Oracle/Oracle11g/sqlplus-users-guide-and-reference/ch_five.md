---
title: "Using Scripts in SQL*Plus"
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_five.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

## 5 Using Scripts in SQL\*Plus

This chapter helps you learn to write and edit scripts containing SQL\*Plus commands, SQL commands, and PL/SQL blocks. It covers the following topics:

Read this chapter while sitting at your computer and try out the examples shown. Before beginning, make sure you have access to the sample schema described in [SQL\*Plus Overview](qstart.md).

## Editing Scripts

In SQL\*Plus command-line, the use of an external editor in combination with the @, @@ or START commands is an effective method of creating and executing generic scripts. You can write scripts which contain SQL\*Plus, SQL and PL/SQL commands, which you can retrieve and edit. This is especially useful for storing complex commands or frequently used reports.

### Writing Scripts with a System Editor

Your operating system may have one or more text editors that you can use to write scripts. You can run your operating system's default text editor without leaving the SQL\*Plus command-line by entering the EDIT command.

You can use the SQL\*Plus DEFINE command to define the variable, \_EDITOR, to hold the name of your preferred text editor. For example, to define the editor used by EDIT to be vi, enter the following command:

```
DEFINE _EDITOR = vi
```

You can include an editor definition in your user or site profile so that it is always enabled when you start SQL\*Plus. See [SQL\*Plus Configuration](ch_two.md), and the [DEFINE](ch_twelve017.md) and [EDIT](ch_twelve021.md) commands for more information.

To create a script with a text editor, enter EDIT followed by the name of the file to edit or create, for example:

```
EDIT SALES
```

EDIT adds the filename extension.SQL to the name unless you specify the file extension. When you save the script with the text editor, it is saved back into the same file. EDIT lets you create or modify scripts.

You must include a semicolon at the end of each SQL command and a slash (/) on a line by itself after each PL/SQL block in the file. You can include multiple SQL commands and PL/SQL blocks in a script.

Example 5-1 Using a System Editor to Write a SQL Script

Suppose you have composed a query to display a list of salespeople and their commissions. You plan to run it once a month to keep track of how well each employee is doing.

To compose and save the query using your system editor, invoke your editor and create a file to hold your script:

```
EDIT SALES
```

Enter each of the following lines in your editor. Do not forget to include the semicolon at the end of the SQL statement:

```
COLUMN LAST_NAME HEADING 'LAST NAME'
COLUMN SALARY HEADING 'MONTHLY SALARY' FORMAT $99,999
COLUMN COMMISSION_PCT HEADING 'COMMISSION %' FORMAT 90.90
SELECT LAST_NAME, SALARY, COMMISSION_PCT
FROM EMP_DETAILS_VIEW
WHERE JOB_ID='SA_MAN';
```

The format model for the column COMMISSION\_PCT tells SQL\*Plus to display an initial zero for decimal values, and a zero instead of a blank when the value of COMMISSION\_PCT is zero for a given row. Format models and the COLUMN command are described in more detail in the [COLUMN](ch_twelve013.md) command and in the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm).

Now use your editor's save command to store your query in a file called SALES.SQL.

## Editing Scripts in SQL\*Plus Command-Line

You can use a number of SQL\*Plus commands to edit the SQL command or PL/SQL block currently stored in the buffer.

Table 5-1, "SQL\*Plus Editing Commands" lists the SQL\*Plus commands that allow you to examine or change the command in the buffer without re-entering the command.

Table 5-1 SQL\*Plus Editing Commands

| Command | Abbreviation | Purpose |
| --- | --- | --- |
| ``` APPEND text ``` | ``` A text ``` | adds text at the end of the current line |
| ``` CHANGE/old/new ``` | ``` C/old/new ``` | changes old to new in the current line |
| ``` CHANGE/text ``` | ``` C/text ``` | deletes text from the current line |
| ``` CLEAR BUFFER ``` | ``` CL BUFF ``` | deletes all lines |
| ``` DEL ``` | (none) | deletes the current line |
| ``` DEL n ``` | (none) | deletes line n |
| ``` DEL * ``` | (none) | deletes the current line |
| ``` DEL n * ``` | (none) | deletes line n through the current line |
| ``` DEL LAST ``` | (none) | deletes the last line |
| ``` DEL m n ``` | (none) | deletes a range of lines (m to n) |
| ``` DEL * n ``` | (none) | deletes the current line through line n |
| ``` INPUT ``` | ``` I ``` | adds one or more lines |
| ``` INPUT text ``` | ``` I text ``` | adds a line consisting of text |
| ``` LIST ``` | ``` ; or L ``` | lists all lines in the SQL buffer |
| ``` LIST n ``` | ``` L n or n ``` | lists line n |
| ``` LIST * ``` | ``` L * ``` | lists the current line |
| ``` LIST n * ``` | ``` L n * ``` | lists line n through the current line |
| ``` LIST LAST ``` | ``` L LAST ``` | lists the last line |
| ``` LIST m n ``` | ``` L m n ``` | lists a range of lines (m to n) |
| ``` LIST * n ``` | ``` L * n ``` | lists the current line through line n |

These are useful if you want to correct or modify a command you have entered.

### Listing the Buffer Contents

The SQL buffer contains the last SQL or PL/SQL command. Any editing command other than LIST and DEL affects only a single line in the buffer. This line is called the current line. It is marked with an asterisk when you list the current command or block.

Example 5-2 Listing the Buffer Contents

Suppose you want to list the current command. Use the LIST command as shown. (If you have exited SQL\*Plus or entered another SQL command or PL/SQL block since following the steps in [Example 4-3, "Entering a SQL Command"](ch_four.md), perform the steps in that example again before continuing.)

```
LIST
```

```
SELECT EMPLOYEE_ID, LAST_NAME, JOB_ID, SALARY
  2  FROM EMP_DETAILS_VIEW
  3* WHERE SALARY>12000
```

Notice that the semicolon you entered at the end of the SELECT command is not listed. This semicolon is necessary to indicate the end of the command when you enter it, but it is not part of the SQL command and SQL\*Plus does not store it in the SQL buffer.

### Editing the Current Line

The SQL\*Plus CHANGE command enables you to edit the current line. Various actions determine which line is the current line:

- LIST a given line to make it the current line.
- When you LIST or RUN the command in the buffer, the last line of the command becomes the current line. (Note, that using the slash (/) command to run the command in the buffer does not affect the current line.)
- If you get an error, the error line automatically becomes the current line.

Example 5-3 Making an Error in Command Entry

Suppose you try to select the JOB\_ID column but mistakenly enter it as JO\_ID. Enter the following command, purposely misspelling JOB\_ID in the first line:

```
SELECT EMPLOYEE_ID, LAST_NAME, JO_ID, SALARY
FROM EMP_DETAILS_VIEW
WHERE JOB_ID='SA_MAN';
```

You see this message on your screen:

```
SELECT EMPLOYEE_ID, LAST_NAME, JO_ID, SALARY
                               *
ERROR at line 1:
ORA-00904: invalid column name
```

Examine the error message; it indicates an invalid column name in line 1 of the query. The asterisk shows the point of error—the mis-typed column JOB\_ID.

Instead of re-entering the entire command, you can correct the mistake by editing the command in the buffer. The line containing the error is now the current line. Use the CHANGE command to correct the mistake. This command has three parts, separated by slashes or any other non-alphanumeric character:

- the word CHANGE or the letter C
- the sequence of characters you want to change
- the replacement sequence of characters

The CHANGE command finds the first occurrence in the current line of the character sequence to be changed and changes it to the new sequence. You do not need to use the CHANGE command to re-enter an entire line.

Example 5-4 Correcting the Error

To change JO\_ID to JOB\_ID, change the line with the CHANGE command:

```
CHANGE /JO_ID/JOB_ID
```

The corrected line appears on your screen:

```
1* SELECT EMPLOYEE_ID, FIRST_NAME, JOB_ID, SALARY
```

Now that you have corrected the error, you can use the RUN command to run the command again:

```
RUN
```

SQL\*Plus correctly displays the query and its result:

```
1  SELECT EMPLOYEE_ID, LAST_NAME, JOB_ID, SALARY
  2  FROM EMP_DETAILS_VIEW
  3* WHERE JOB_ID='SA_MAN'

EMPLOYEE_ID LAST_NAME                 JOB_ID     MONTHLY SALARY
----------- ------------------------- ---------- --------------
        145 Russell                   SA_MAN            $14,000
        146 Partners                  SA_MAN            $13,500
        147 Errazuriz                 SA_MAN            $12,000
        148 Cambrault                 SA_MAN            $11,000
        149 Zlotkey                   SA_MAN            $10,500
```

Note that the column SALARY retains the format you gave it in [Example 4-4, "Entering a SQL\*Plus Command"](ch_four.md). (If you have left SQL\*Plus and started again since performing [Example 4-4, "Entering a SQL\*Plus Command"](ch_four.md) the column has reverted to its original format.)

See [CHANGE](ch_twelve011.md) for information about the significance of case in a CHANGE command and on using wildcards to specify blocks of text in a CHANGE command.

### Appending Text to a Line

To add text to the end of a line in the buffer, use the APPEND command.

1. Use the LIST command (or the line number) to list the line you want to change.
2. Enter APPEND followed by the text you want to add. If the text you want to add begins with a blank, separate the word APPEND from the first character of the text by two blanks: one to separate APPEND from the text, and one to go into the buffer with the text.

Example 5-5 Appending Text to a Line

To append a space and the clause DESC to line 4 of the current query, first list line 4:

```
LIST 4
```

```
4* ORDER BY SALARY
```

Next, enter the following command (be sure to type two spaces between APPEND and DESC):

```
APPEND  DESC
```

```
4* ORDER BY SALARY DESC
```

Type RUN to verify the query:

```
1  SELECT EMPLOYEE_ID, LAST_NAME, JOB_ID, SALARY
  2  FROM EMP_DETAILS_VIEW
  3  WHERE JOB_ID='SA_MAN'
  4* ORDER BY SALARY DESC

EMPLOYEE_ID LAST_NAME                 JOB_ID     MONTHLY SALARY
----------- ------------------------- ---------- --------------
        145 Russell                   SA_MAN            $14,000
        146 Partners                  SA_MAN            $13,500
        147 Errazuriz                 SA_MAN            $12,000
        148 Cambrault                 SA_MAN            $11,000
        149 Zlotkey                   SA_MAN            $10,500
```

### Adding a New Line

To insert a new line after the current line, use the INPUT command.

To insert a line before line 1, enter a zero ("0") and follow the zero with text. SQL\*Plus inserts the line at the beginning of the buffer and all lines are renumbered starting at 1.

```
0 SELECT EMPLOYEE_ID
```

Example 5-6 Adding a Line

Suppose you want to add a fourth line to the SQL command you modified in Example 5-4, "Correcting the Error". Since line 3 is already the current line, enter INPUT and press Return.

```
INPUT
```

SQL\*Plus prompts you for the new line:

```
4
```

Enter the new line. Then press Return.

```
4 ORDER BY SALARY
```

SQL\*Plus prompts you again for a new line:

```
5
```

Press Return again to indicate that you will not enter any more lines, and then use RUN to verify and re-run the query.

```
1  SELECT EMPLOYEE_ID, LAST_NAME, JOB_ID, SALARY
  2  FROM EMP_DETAILS_VIEW
  3  WHERE JOB_ID='SA_MAN'
  4* ORDER BY SALARY

EMPLOYEE_ID LAST_NAME                 JOB_ID     MONTHLY SALARY
----------- ------------------------- ---------- --------------
        149 Zlotkey                   SA_MAN            $10,500
        148 Cambrault                 SA_MAN            $11,000
        147 Errazuriz                 SA_MAN            $12,000
        146 Partners                  SA_MAN            $13,500
        145 Russell                   SA_MAN            $14,000
```

### Deleting Lines

Use the DEL command to delete lines in the buffer. Enter DEL specifying the line numbers you want to delete.

Suppose you want to delete the current line to the last line inclusive. Use the DEL command as shown.

```
DEL * LAST
```

DEL makes the following line of the buffer (if any) the current line.

See [DEL](ch_twelve018.md) for more information.

## Placing Comments in Scripts

You can enter comments in a script in three ways:

- using the SQL\*Plus REMARK command for single line comments.
- using the SQL comment delimiters /\*... \*/ for single or multi line comments.
- using ANSI/ISO (American National Standards Institute/International Standards Organization) comments - - for single line comments.
	Comments entered at the command-line are not stored in the SQL buffer.

### Using the REMARK Command

Use the REMARK command on a line by itself in a script, followed by comments on the same line. To continue the comments on additional lines, enter additional REMARK commands. Do not place a REMARK command between different lines of a single SQL command.

```
REMARK Commission Report;
REMARK to be run monthly.;
COLUMN LAST_NAME HEADING 'LAST_NAME';
COLUMN SALARY HEADING 'MONTHLY SALARY' FORMAT $99,999;
COLUMN COMMISSION_PCT HEADING 'COMMISSION %' FORMAT 90.90;
REMARK Includes only salesmen;
SELECT LAST_NAME, SALARY, COMMISSION_PCT
FROM EMP_DETAILS_VIEW
WHERE JOB_ID='SA_MAN';
```

### Using /\*...\*/

Enter the SQL comment delimiters, /\*...\*/, on separate lines in your script, on the same line as a SQL command, or on a line in a PL/SQL block.

You must enter a space after the slash-asterisk(/\*) beginning a comment.

The comments can span multiple lines, but cannot be nested within one another:

```
/* Commission Report
 to be run monthly. */
COLUMN LAST_NAME HEADING 'LAST_NAME';
COLUMN SALARY HEADING 'MONTHLY SALARY' FORMAT $99,999;
COLUMN COMMISSION_PCT HEADING 'COMMISSION %' FORMAT 90.90;
REMARK Includes only salesmen;
SELECT LAST_NAME, SALARY, COMMISSION_PCT
FROM EMP_DETAILS_VIEW
/* Include only salesmen.*/
WHERE JOB_ID='SA_MAN';
```

### Using - -

You can use ANSI/ISO "- -" style comments within SQL statements, PL/SQL blocks, or SQL\*Plus commands. Since there is no ending delimiter, the comment cannot span multiple lines.

For PL/SQL and SQL, enter the comment after a command on a line, or on a line by itself:

```
-- Commissions report to be run monthly
DECLARE --block for reporting monthly sales
```

For SQL\*Plus commands, you can only include "- -" style comments if they are on a line by themselves. For example, these comments are legal:

```
-- set maximum width for LONG to 777
SET LONG 777
```

This comment is illegal:

```
SET LONG 777 -- set maximum width for LONG to 777
```

If you enter the following SQL\*Plus command, SQL\*Plus interprets it as a comment and does not execute the command:

```
-- SET LONG 777
```

### Notes on Placing Comments

SQL\*Plus does not have a SQL or PL/SQL command parser. It scans the first few keywords of each new statement to determine the command type, SQL, PL/SQL or SQL\*Plus. Comments in some locations can prevent SQL\*Plus from correctly identifying the command type, giving unexpected results. The following usage notes may help you to use SQL\*Plus comments more effectively:

1. Do not put comments within the first few keywords of a statement. For example:
	```
	CREATE OR REPLACE
	  2  /* HELLO */
	  3  PROCEDURE HELLO AS
	  4  BEGIN
	  5  DBMS_OUTPUT.PUT_LINE('HELLO');
	  6  END;
	  7  /
	Warning: Procedure created with compilation errors.
	```
	The location of the comment prevents SQL\*Plus from recognizing the command as a command. SQL\*Plus submits the PL/SQL block to the server when it sees the slash "/" at the beginning of the comment, which it interprets as the "/" statement terminator. Move the comment to avoid this error. For example:
	```
	CREATE OR REPLACE PROCEDURE
	  2  /* HELLO */
	  3  HELLO AS
	  4  BEGIN
	  5  DBMS_OUTPUT.PUT_LINE('HELLO');
	  6  END;
	  7  /
	Procedure created.
	```
2. Do not put comments after statement terminators (period, semicolon or slash). For example, if you enter:
	```
	SELECT 'Y' FROM DUAL; -- TESTING
	```
	You get the following error:
	```
	SELECT 'Y' FROM DUAL; -- TESTING
	                    *
	ERROR at line 1:
	ORA-00911: invalid character
	```
	SQL\*Plus expects no text after a statement terminator and is unable to process the command.
3. Do not put statement termination characters at the end of a comment line or after comments in a SQL statement or a PL/SQL block. For example, if you enter:
	```
	SELECT *
	-- COMMENT;
	```
	You get the following error:
	```
	-- COMMENT
	         *
	ERROR at line 2:
	ORA-00923: FROM keyword not found where expected
	```
	The semicolon is interpreted as a statement terminator and SQL\*Plus submits the partially formed SQL command to the server for processing, resulting in an error.
4. Do not use ampersand characters '&' in comments in a SQL statement or PL/SQL block. For example, if you enter a script such as:
	```
	SELECT REGION_NAME, CITY
	/* THIS & THAT */
	FROM EMP_DETAILS_VIEW
	WHERE SALARY>12000;
	```
	SQL\*Plus interprets text after the ampersand character "&" as a substitution variable and prompts for the value of the variable, &that:
	```
	Enter value for that: 
	old   2: /* THIS & THAT */
	new   2: /* THIS  */
	REGION_NAME               CITY
	------------------------- ------------------------------
	Americas                  Seattle
	Americas                  Seattle
	Americas                  Seattle
	Europe                    Oxford
	Europe                    Oxford
	Americas                  Toronto
	6 rows selected.
	```
	You can SET DEFINE OFF to prevent scanning for the substitution character.

For more information on substitution and termination characters, see DEFINE, SQLTERMINATOR and SQLBLANKLINES in the [SET](ch_twelve039.md) command.

## Running Scripts

The START command retrieves a script and runs the commands it contains. Use START to run a script containing SQL commands, PL/SQL blocks, and SQL\*Plus commands. You can have many commands in the file. Follow the START command with the name of the file:

```
START file_name
```

SQL\*Plus assumes the file has a.SQL extension by default.

Example 5-7 Running a Script

To retrieve and run the command stored in SALES.SQL, enter

```
START SALES
```

SQL\*Plus runs the commands in the file SALES and displays the results of the commands on your screen, formatting the query results according to the SQL\*Plus commands in the file:

```
LAST NAME                 MONTHLY SALARY COMMISSION %
------------------------- -------------- ------------
Russell                          $14,000         0.40
Partners                         $13,500         0.30
Errazuriz                        $12,000         0.30
Cambrault                        $11,000         0.30
Zlotkey                          $10,500         0.20
```

You can also use the @ (at sign) command to run a script:

```
@SALES
```

The @ and @@ commands list and run the commands in the specified script in the same manner as START. SET ECHO affects the @ and @@ commands in the same way as it affects the START command.

To see the commands as SQL\*Plus "enters" them, you can SET ECHO ON. The ECHO system variable controls the listing of the commands in scripts run with the START, @ and @@ commands. Setting the ECHO variable OFF suppresses the listing.

START, @ and @@ leave the last SQL command or PL/SQL block of the script in the buffer.

### Running a Script as You Start SQL\*Plus

To run a script as you start SQL\*Plus, use one of the following options:

- Follow the SQLPLUS command with your username, a slash, a space, @, and the name of the file:
	```
	SQLPLUS HR @SALES
	```
	SQL\*Plus starts, prompts for your password and runs the script.
- Include your username as the first line of the file. Follow the SQLPLUS command with @ and the filename. SQL\*Plus starts, prompts for your password and runs the file.

## Nesting Scripts

To run a series of scripts in sequence, first create a script containing several START commands, each followed by the name of a script in the sequence. Then run the script containing the START commands. For example, you could include the following START commands in a script named SALESRPT:

```
START Q1SALES
START Q2SALES
START Q3SALES
START Q4SALES
START YRENDSLS
```

Note:

The @@ command may be useful in this example. See the [@@ (double at sign)](ch_twelve003.md) command for more information.

## Exiting from a Script with a Return Code

You can include an EXIT command in a script to return a value when the script finishes. See the [EXIT](ch_twelve023.md) command for more information.

You can include a WHENEVER SQLERROR command in a script to automatically exit SQL\*Plus with a return code should your script generate a SQL error. Similarly, you can include a WHENEVER OSERROR command to automatically exit should an operating system error occur. In iSQL\*Plus, the script is stopped and focus is returned to the Workspace. See the [WHENEVER SQLERROR](ch_twelve052.md) command, and the [WHENEVER OSERROR](ch_twelve051.md) command for more information.

## Defining Substitution Variables

You can define variables, called substitution variables, for repeated use in a single script by using the SQL\*Plus DEFINE command. Note that you can also define substitution variables to use in titles and to save your keystrokes (by defining a long string as the value for a variable with a short name).

Example 5-8 Defining a Substitution Variable

To define a substitution variable L\_NAME and give it the value "SMITH", enter the following command:

```
DEFINE L_NAME = SMITH
```

To confirm the variable definition, enter DEFINE followed by the variable name:

```
DEFINE L_NAME
```

```
DEFINE L_NAME = "SMITH" (CHAR)
```

To list all substitution variable definitions, enter DEFINE by itself. Note that any substitution variable you define explicitly through DEFINE takes only CHAR values (that is, the value you assign to the variable is always treated as a CHAR datatype). You can define a substitution variable of datatype NUMBER implicitly through the ACCEPT command. You will learn more about the ACCEPT command.

To delete a substitution variable, use the SQL\*Plus command UNDEFINE followed by the variable name.

## Using Predefined Variables

There are eight variables containing SQL\*Plus information that are defined during SQL\*Plus installation. These variables can be redefined, referenced or removed the same as any other variable. They are always available from session to session unless you explicitly remove or redefine them.

See Also:

[Predefined Variables](ch_twelve017.md) for a list of the predefined variables and examples of their use.

## Using Substitution Variables

Suppose you want to write a query like the one in SALES (see Example 5-1, "Using a System Editor to Write a SQL Script") to list the employees with various jobs, not just those whose job is SA\_MAN. You could do that by editing a different value into the WHERE clause each time you run the command, but there is an easier way.

By using a substitution variable in place of the text, SA\_MAN, in the WHERE clause, you can get the same results you would get if you had written the values into the command itself.

A substitution variable is preceded by one or two ampersands (&). When SQL\*Plus encounters a substitution variable in a command, SQL\*Plus executes the command as though it contained the value of the substitution variable, rather than the variable itself.

For example, if the variable SORTCOL has the value JOB\_ID and the variable MYTABLE has the value EMP\_DETAILS\_VIEW, SQL\*Plus executes the commands

```
SELECT &SORTCOL, SALARY
FROM &MYTABLE
WHERE SALARY>12000;
```

as if they were

```
SELECT JOB_ID, SALARY
FROM EMP_DETAILS_VIEW
WHERE SALARY>12000;
```

### Where and How to Use Substitution Variables

You can use substitution variables anywhere in SQL and SQL\*Plus commands, except as the first word entered. When SQL\*Plus encounters an undefined substitution variable in a command, SQL\*Plus prompts you for the value.

You can enter any string at the prompt, even one containing blanks and punctuation. If the SQL command containing the reference should have quote marks around the variable and you do not include them there, the user must include the quotes when prompted.

SQL\*Plus reads your response from the keyboard, even if you have redirected terminal input or output to a file. If a terminal is not available (if, for example, you run the script in batch mode), SQL\*Plus uses the redirected file.

After you enter a value at the prompt, SQL\*Plus lists the line containing the substitution variable twice: once before substituting the value you enter and once after substitution. You can suppress this listing by setting the SET command variable VERIFY to OFF.

Example 5-9 Using Substitution Variables

Create a script named STATS, to be used to calculate a subgroup statistic (the maximum value) on a numeric column:

```
SELECT &GROUP_COL, MAX(&NUMBER_COL) MAXIMUM
FROM &TABLE
GROUP BY &GROUP_COL
.
SAVE STATS
```

```
Created file STATS
```

Now run the script STATS:

```
@STATS
```

And respond to the prompts for values as shown:

```
Enter value for group_col: JOB_ID
old   1: SELECT   &GROUP_COL,
new   1: SELECT   JOB_ID,
Enter value for number_col: SALARY
old   2:          MAX(&NUMBER_COL) MAXIMUM
new   2:          MAX(SALARY) MAXIMUM
Enter value for table: EMP_DETAILS_VIEW
old   3: FROM     &TABLE
new   3: FROM     EMP_DETAILS_VIEW
Enter value for group_col: JOB_ID
old   4: GROUP BY &GROUP_COL
new   4: GROUP BY JOB_ID
```

SQL\*Plus displays the following output:

```
JOB_ID        MAXIMUM
---------- ----------
AC_ACCOUNT       8300
AC_MGR          12000
AD_ASST          4400
AD_PRES         24000
AD_VP           17000
FI_ACCOUNT       9000
FI_MGR          12000
HR_REP           6500
IT_PROG          9000
MK_MAN          13000
MK_REP           6000

JOB_ID        MAXIMUM
---------- ----------
PR_REP          10000
PU_CLERK         3100
PU_MAN          11000
SA_MAN          14000
SA_REP          11500
SH_CLERK         4200
ST_CLERK         3600
ST_MAN           8200

19 rows selected.
```

If you wish to append characters immediately after a substitution variable, use a period to separate the variable from the character. For example:

```
SELECT SALARY FROM EMP_DETAILS_VIEW WHERE EMPLOYEE_ID='&X.5';
Enter value for X:  20
```

is interpreted as

```
SELECT SALARY FROM EMP_DETAILS_VIEW WHERE EMPLOYEE_ID='205';
```

### Avoiding Unnecessary Prompts for Values

Suppose you wanted to expand the file STATS to include the minimum, sum, and average of the "number" column. You may have noticed that SQL\*Plus prompted you twice for the value of GROUP\_COL and once for the value of NUMBER\_COL in Example 5-9, "Using Substitution Variables", and that each GROUP\_COL or NUMBER\_COL had a single ampersand in front of it. If you were to add three more functions—using a single ampersand before each—to the script, SQL\*Plus would prompt you a total of four times for the value of the number column.

You can avoid being re-prompted for the group and number columns by adding a second ampersand in front of each GROUP\_COL and NUMBER\_COL in STATS. SQL\*Plus automatically DEFINEs any substitution variable preceded by two ampersands, but does not DEFINE those preceded by only one ampersand. When you have defined a variable, SQL\*Plus will not prompt for its value in the current session.

Example 5-10 Using Double Ampersands

To expand the script STATS using double ampersands and then run the file, first suppress the display of each line before and after substitution:

```
SET VERIFY OFF
```

Now retrieve and edit STATS by entering the following commands:

```
GET STATS
```

```
SELECT   &GROUP_COL,
MAX(&NUMBER_COL) MAXIMUM
FROM     &TABLE
GROUP BY &GROUP_COL
```

```
2
```

```
2* MAX(&NUMBER_COL) MAXIMUM
```

```
APPEND ,
```

```
2* MAX(&NUMBER_COL) MAXIMUM,
```

```
CHANGE/&/&&
```

```
2* MAX(&&NUMBER_COL) MAXIMUM,
```

```
I
```

```
3i
```

```
MIN (&&NUMBER_COL) MINIMUM,
```

```
4i
```

```
SUM(&&NUMBER_COL)  TOTAL,
```

```
5i
```

```
AVG(&&NUMBER_COL)  AVERAGE
```

```
6i
```

```
1
```

```
1* SELECT   &GROUP_COL,
```

```
CHANGE/&/&&
```

```
1* SELECT   &&GROUP_COL,
```

```
7
```

```
7* GROUP BY &GROUP_COL
```

```
CHANGE/&/&&/
```

```
7* GROUP BY &&GROUP_COL
```

```
SAVE STATS2
```

```
Created file STATS2
```

Finally, run the script STATS2 and respond to the prompts as follows:

```
START STATS2
Enter value for group_col: JOB_ID
Enter value for number_col: SALARY
Enter value for table: EMP_DETAILS_VIEW
```

SQL\*Plus displays the following output:

```
JOB_ID        MAXIMUM    MINIMUM      TOTAL    AVERAGE
---------- ---------- ---------- ---------- ----------
AC_ACCOUNT       8300       8300       8300       8300
AC_MGR          12000      12000      12000      12000
AD_ASST          4400       4400       4400       4400
AD_PRES         24000      24000      24000      24000
AD_VP           17000      17000      34000      17000
FI_ACCOUNT       9000       6900      39600       7920
FI_MGR          12000      12000      12000      12000
HR_REP           6500       6500       6500       6500
IT_PROG          9000       4200      28800       5760
MK_MAN          13000      13000      13000      13000
MK_REP           6000       6000       6000       6000

JOB_ID        MAXIMUM    MINIMUM      TOTAL    AVERAGE
---------- ---------- ---------- ---------- ----------
PR_REP          10000      10000      10000      10000
PU_CLERK         3100       2500      13900       2780
PU_MAN          11000      11000      11000      11000
SA_MAN          14000      10500      61000      12200
SA_REP          11500       6100     250500       8350
SH_CLERK         4200       2500      64300       3215
ST_CLERK         3600       2100      55700       2785
ST_MAN           8200       5800      36400       7280

19 rows selected.
```

Note that you were prompted for the values of NUMBER\_COL and GROUP\_COL only once. If you were to run STATS2 again during the current session, you would be prompted for TABLE (because its name has a single ampersand and the variable is therefore not DEFINEd) but not for GROUP\_COL or NUMBER\_COL (because their names have double ampersands and the variables are therefore DEFINEd).

Before continuing, set the system variable VERIFY back to ON:

```
SET VERIFY ON
```

### Restrictions

You cannot use substitution variables in the buffer editing commands, APPEND, CHANGE, DEL, and INPUT, nor in other commands where substitution would be meaningless. The buffer editing commands, APPEND, CHANGE, and INPUT, treat text beginning with "&" or "&&" literally, like any other text string.

### System Variables

The following system variables, specified with the SQL\*Plus SET command, affect substitution variables:

| System Variable | Affect on Substitution Variables |
| --- | --- |
| ``` SET CONCAT ``` | Defines the character that separates the name of a substitution variable or parameter from characters that immediately follow the variable or parameter—by default the period (.). |
| ``` SET DEFINE ``` | Defines the substitution character (by default the ampersand "&") and turns substitution on and off. |
| ``` SET ESCAPE ``` | Defines an escape character you can use before the substitution character. The escape character instructs SQL\*Plus to treat the substitution character as an ordinary character rather than as a request for variable substitution. The default escape character is a backslash (\\). |
| ``` SET NUMFORMAT ``` | Sets the default format for displaying numbers, including numeric substitution variables. |
| ``` SET NUMWIDTH ``` | Sets the default width for displaying numbers, including numeric substitution variables. |
| ``` SET VERIFY ON ``` | Lists each line of the script before and after substitution. |

See [SET](ch_twelve039.md) for more information about system variables.

## Passing Parameters through the START Command

You can bypass the prompts for values associated with substitution variables by passing values to parameters in a script through the START command.

You do this by placing an ampersand (&) followed by a numeral in the script in place of a substitution variable. Each time you run this script, START replaces each &1 in the file with the first value (called an argument) after START filename, then replaces each &2 with the second value, and so forth.

For example, you could include the following commands in a script called MYFILE:

```
SELECT * FROM EMP_DETAILS_VIEW
WHERE JOB_ID='&1'
AND SALARY='&2';
```

In the following START command, SQL\*Plus would substitute PU\_CLERK for &1 and 3100 for &2 in the script MYFILE:

```
START MYFILE PU_CLERK 3100
```

When you use arguments with the START command, SQL\*Plus DEFINEs each parameter in the script with the value of the appropriate argument.

Example 5-11 Passing Parameters through START

To create a new script based on SALES that takes a parameter specifying the job to be displayed, enter

```
GET SALES
```

```
1  COLUMN LAST_NAME HEADING 'LAST NAME'
2  COLUMN SALARY  HEADING 'MONTHLY SALARY' FORMAT $99,999
3  COLUMN COMMISSION_PCT HEADING 'COMMISSION %' FORMAT 90.90
4  SELECT LAST_NAME, SALARY, COMMISSION_PCT
5  FROM EMP_DETAILS_VIEW
6* WHERE JOB_ID='SA_MAN'
```

```
6
```

```
6* WHERE JOB_ID='SA_MAN'
```

```
CHANGE /SA_MAN/&1
```

```
6* WHERE JOB_ID='&1'
```

```
SAVE ONEJOB
```

```
Created file ONEJOB
```

Now run the command with the parameter SA\_MAN:

```
START ONEJOB SA_MAN
```

SQL\*Plus lists the line of the SQL command that contains the parameter, before and after replacing the parameter with its value, and then displays the output:

```
old   3: WHERE JOB_ID='&1'
new   3: WHERE JOB_ID='SA_MAN'

LAST NAME                 MONTHLY SALARY COMMISSION %
------------------------- -------------- ------------
Russell                          $14,000         0.40
Partners                         $13,500         0.30
Errazuriz                        $12,000         0.30
Cambrault                        $11,000         0.30
Zlotkey                          $10,500         0.20
```

You can use many parameters in a script. Within a script, you can refer to each parameter many times, and you can include the parameters in any order.

While you cannot use parameters when you run a command with RUN or slash (/), you could use substitution variables instead.

Before continuing, return the columns to their original heading by entering the following command:

```
CLEAR COLUMN
```

## Communicating with the User

Three SQL\*Plus commands—PROMPT, ACCEPT, and PAUSE—help you communicate with the end user. These commands enable you to send messages to the screen and receive input from the user, including a simple Return. You can also use PROMPT and ACCEPT to customize the prompts for values SQL\*Plus automatically generates for substitution variables.

### Receiving a Substitution Variable Value

Through PROMPT and ACCEPT, you can send messages to the end user and receive values from end-user input. PROMPT displays a message you specify on-screen to give directions or information to the user. ACCEPT prompts the user for a value and stores it in the substitution variable you specify. Use PROMPT in conjunction with ACCEPT when a prompt spans more than one line.

Example 5-12 Prompting for and Accepting Input

To direct the user to supply a report title and to store the input in the variable MYTITLE for use in a subsequent query, first clear the buffer:

```
CLEAR BUFFER
```

Next, set up a script as shown and save this file as PROMPT1:

```
PROMPT Enter a title of up to 30 characters
ACCEPT MYTITLE PROMPT 'Title: '
TTITLE LEFT MYTITLE SKIP 2
SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, SALARY
FROM EMP_DETAILS_VIEW
WHERE JOB_ID='SA_MAN'
  
SAVE PROMPT1
```

```
Created file PROMPT1.sql
```

The TTITLE command sets the top title for your report. See [Defining Page and Report Titles and Dimensions](ch_six.md) for more information about the TTITILE command.

Finally, run the script, responding to the prompt for the title as shown:

```
START PROMPT1
```

```
Enter a title of up to 30 characters
Title: Department Report
Department ReportEMPLOYEE_ID FIRST_NAME           LAST_NAME                     SALARY
----------- -------------------- ------------------------- ----------
        145 John                 Russell                        14000
        146 Karen                Partners                       13500
        147 Alberto              Errazuriz                      12000
        148 Gerald               Cambrault                      11000
        149 Eleni                Zlotkey                        10500
```

Before continuing, turn the TTITLE command off:

```
TTITLE OFF
```

### Customizing Prompts for Substitution Variable

If you want to customize the prompt for a substitution variable value, use PROMPT and ACCEPT in conjunction with the substitution variable, as shown in the following example.

Example 5-13 Using PROMPT and ACCEPT in Conjunction with Substitution Variables

As you have seen in Example 5-12, "Prompting for and Accepting Input", SQL\*Plus automatically generates a prompt for a value when you use a substitution variable. You can replace this prompt by including PROMPT and ACCEPT in the script with the query that references the substitution variable. First clear the buffer with:

```
CLEAR BUFFER
```

To create such a file, enter the following:

```
INPUT
PROMPT Enter a valid employee ID
PROMPT For Example 145, 206
ACCEPT ENUMBER NUMBER PROMPT 'Employee ID. :'
SELECT FIRST_NAME, LAST_NAME, SALARY
FROM EMP_DETAILS_VIEW
WHERE EMPLOYEE_ID=&ENUMBER;
```

Save this file as PROMPT2. Next, run this script. SQL\*Plus prompts for the value of ENUMBER using the text you specified with PROMPT and ACCEPT:

```
START PROMPT2
```

SQL\*Plus prompts you to enter an Employee ID:

```
Enter a valid employee ID
For Example 145, 206

Employee ID. :
```

```
205
```

```
old   3: WHERE EMPLOYEE_ID=&ENUMBER
new   3: WHERE EMPLOYEE_ID=       205

Department Report

FIRST_NAME           LAST_NAME                     SALARY
-------------------- ------------------------- ----------
Shelley              Higgins                        12000
```

What would happen if you typed characters instead of numbers? Since you specified NUMBER after the variable name in the ACCEPT command, SQL\*Plus will not accept a non-numeric value:

Try entering characters instead of numbers to the prompt for "Employee ID.", SQL\*Plus will respond with an error message and prompt you again to re-enter the correct number:

```
START PROMPT2
```

When SQL\*Plus prompts you to enter an Employee ID, enter the word "one" instead of a number:

```
Enter a valid employee ID
For Example 145, 206

Employee ID. :
```

```
one
```

```
SP2-0425: "one" is not a valid number
```

### Sending a Message and Accepting Return as Input

If you want to display a message on the user's screen and then have the user press Return after reading the message, use the SQL\*Plus command PAUSE. For example, you might include the following lines in a script:

```
PROMPT Before continuing, make sure you have your account card.
PAUSE Press RETURN to continue.
```

### Clearing the Screen

If you want to clear the screen before displaying a report (or at any other time), include the SQL\*Plus CLEAR command with its SCREEN clause at the appropriate point in your script, using the following format:

```
CLEAR SCREEN
```

Before continuing to the next section, reset all columns to their original formats and headings by entering the following command:

```
CLEAR COLUMNS
```

## Using Bind Variables

Bind variables are variables you create in SQL\*Plus and then reference in PL/SQL or SQL. If you create a bind variable in SQL\*Plus, you can use the variable as you would a declared variable in your PL/SQL subprogram and then access the variable from SQL\*Plus. You can use bind variables for such things as storing return codes or debugging your PL/SQL subprograms.

Because bind variables are recognized by SQL\*Plus, you can display their values in SQL\*Plus or reference them in PL/SQL subprograms that you run in SQL\*Plus.

### Creating Bind Variables

You create bind variables in SQL\*Plus with the VARIABLE command. For example

```
VARIABLE ret_val NUMBER
```

This command creates a bind variable named ret\_val with a datatype of NUMBER. See the [VARIABLE](ch_twelve050.md) command for more information. (To list all bind variables created in a session, type VARIABLE without any arguments.)

### Referencing Bind Variables

You reference bind variables in PL/SQL by typing a colon (:) followed immediately by the name of the variable. For example

```
:ret_val := 1;
```

To change this bind variable in SQL\*Plus, you must enter a PL/SQL block. For example:

```
BEGIN
 :ret_val:=4;
END;
/
```

```
PL/SQL procedure successfully completed.
```

This command assigns a value to the bind variable named ret\_val.

### Displaying Bind Variables

To display the value of a bind variable in SQL\*Plus, you use the SQL\*Plus PRINT command. For example:

```
PRINT RET_VAL
```

```
RET_VAL
----------
         4
```

This command displays a bind variable named ret\_val. See [PRINT](ch_twelve031.md) for more information about displaying bind variables.

## Using REFCURSOR Bind Variables

SQL\*Plus REFCURSOR bind variables allow SQL\*Plus to fetch and format the results of a SELECT statement contained in a PL/SQL block.

REFCURSOR bind variables can also be used to reference PL/SQL cursor variables in stored procedures. This enables you to store SELECT statements in the database and reference them from SQL\*Plus.

A REFCURSOR bind variable can also be returned from a stored function.

Example 5-14 Creating, Referencing, and Displaying REFCURSOR Bind Variables

To create, reference and display a REFCURSOR bind variable, first declare a local bind variable of the REFCURSOR datatype

```
VARIABLE employee_info REFCURSOR
```

Next, enter a PL/SQL block that uses the bind variable in an OPEN... FOR SELECT statement. This statement opens a cursor variable and executes a query. See the [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm) for information on the OPEN command and cursor variables.

In this example we are binding the SQL\*Plus employee\_info bind variable to the cursor variable.

```
BEGIN
OPEN :employee_info FOR SELECT EMPLOYEE_ID, SALARY
FROM                                            EMP_DETAILS_VIEW WHERE JOB_ID='SA_MAN' ;
END;
 /
```

```
PL/SQL procedure successfully completed.
```

The results from the SELECT statement can now be displayed in SQL\*Plus with the PRINT command.

```
PRINT employee_info
```

```
EMPLOYEE_ID     SALARY
----------- ----------
        145      14000
        146      13500
        147      12000
        148      11000
        149      10500
```

The PRINT statement also closes the cursor. To reprint the results, the PL/SQL block must be executed again before using PRINT.

Example 5-15 Using REFCURSOR Variables in Stored Procedures

A REFCURSOR bind variable is passed as a parameter to a procedure. The parameter has a REF CURSOR type. First, define the type.

```
CREATE OR REPLACE PACKAGE EmpPack AS
  TYPE EmpInfoTyp IS REF CURSOR;
  PROCEDURE EmpInfoRpt (emp_cv IN OUT EmpInfoTyp);
END EmpPack;
/
```

```
Package created.
```

Next, create the stored procedure containing an OPEN... FOR SELECT statement.

```
CREATE OR REPLACE PACKAGE BODY EmpPack AS
  PROCEDURE EmpInfoRpt (emp_cv IN OUT EmpInfoTyp) AS
  BEGIN
    OPEN emp_cv FOR SELECT EMPLOYEE_ID, SALARY
    FROM EMP_DETAILS_VIEW
    WHERE JOB_ID='SA_MAN' ;
  END;
END;
 /
```

```
Procedure created.
```

Execute the procedure with a SQL\*Plus bind variable as the parameter.

```
VARIABLE cv REFCURSOR
EXECUTE EmpPack.EmpInfoRpt(:cv)
```

```
PL/SQL procedure successfully completed.
```

Now print the bind variable.

```
PRINT cv
```

```
EMPLOYEE_ID     SALARY
----------- ----------
        145      14000
        146      13500
        147      12000
        148      11000
        149      10500
```

The procedure can be executed multiple times using the same or a different REFCURSOR bind variable.

```
VARIABLE pcv REFCURSOR
EXECUTE EmpInfo_rpt(:pcv)
```

```
PL/SQL procedure successfully completed.
```

```
PRINT pcv
```

```
EMPLOYEE_ID     SALARY
----------- ----------
        145      14000
        146      13500
        147      12000
        148      11000
        149      10500
```

Example 5-16 Using REFCURSOR Variables in Stored Functions

Create a stored function containing an OPEN... FOR SELECT statement:

```
CREATE OR REPLACE FUNCTION EmpInfo_fn RETURN -
cv_types.EmpInfo IS
resultset cv_types.EmpInfoTyp;
BEGIN
OPEN resultset FOR SELECT EMPLOYEE_ID, SALARY
FROM EMP_DETAILS_VIEW
WHERE JOB_ID='SA_MAN';
RETURN(resultset);
END;
/
```

```
Function created.
```

Execute the function.

```
VARIABLE rc REFCURSOR
EXECUTE :rc := EmpInfo_fn
```

```
PL/SQL procedure successfully completed.
```

Now print the bind variable.

```
PRINT rc
```

```
EMPLOYEE_ID     SALARY
----------- ----------
        145      14000
        146      13500
        147      12000
        148      11000
        149      10500
```

The function can be executed multiple times using the same or a different REFCURSOR bind variable.

```
EXECUTE :rc := EmpInfo_fn
```

```
PL/SQL procedure successfully completed.
```