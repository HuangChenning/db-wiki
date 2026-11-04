---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/using-scripts-in-SQL-Plus.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

This chapter helps you learn to write and edit scripts containing SQL\*Plus commands, SQL commands, and PL/SQL blocks. It covers the following topics:

Read this chapter while sitting at your computer and try out the examples shown. Before beginning, make sure you have access to the sample schema described in [SQL\*Plus Overview](SQL-Plus-quick-start.md).

### 5.1 About Editing Scripts

In SQL\*Plus command-line, the use of an external editor in combination with the @, @@ or START commands is an effective method of creating and executing generic scripts. You can write scripts which contain SQL\*Plus, SQL and PL/SQL commands, which you can retrieve and edit. This is especially useful for storing complex commands or frequently used reports.

#### 5.1.1 Writing Scripts with a System Editor

Your operating system may have one or more text editors that you can use to write scripts. You can run your operating system's default text editor without leaving the SQL\*Plus command-line by entering the EDIT command.

You can use the SQL\*Plus DEFINE command to define the variable, \_EDITOR, to hold the name of your preferred text editor. For example, to define the editor used by EDIT to be vi, enter the following command:

```
DEFINE _EDITOR = vi
```

You can include an editor definition in your user or site profile so that it is always enabled when you start SQL\*Plus. See [SQL\*Plus Configuration](configuring-SQL-Plus.md), and the [DEFINE](DEFINE.md) and [EDIT](EDIT.md) commands for more information.

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

The format model for the column COMMISSION\_PCT tells SQL\*Plus to display an initial zero for decimal values, and a zero instead of a blank when the value of COMMISSION\_PCT is zero for a given row. Format models and the COLUMN command are described in more detail in the [COLUMN](COLUMN.md) command and in [Format Models](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=SQLRF-GUID-DFB23985-2943-4C6A-96DF-DF0F664CED96).

Now use your editor's save command to store your query in a file called SALES.SQL.

### 5.2 About Editing Scripts in SQL\*Plus Command-Line

You can use a number of SQL\*Plus commands to edit the SQL command or PL/SQL block currently stored in the buffer.

Table 5-1 lists the SQL\*Plus commands that allow you to examine or change the command in the buffer without re-entering the command.

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

#### 5.2.1 Listing the Buffer Contents

The SQL buffer contains the last SQL or PL/SQL command. Any editing command other than LIST and DEL affects only a single line in the buffer. This line is called the current line. It is marked with an asterisk when you list the current command or block.

```
SELECT EMPLOYEE_ID, LAST_NAME, JOB_ID, SALARY
  2  FROM EMP_DETAILS_VIEW
  3* WHERE SALARY>12000
```

Notice that the semicolon you entered at the end of the SELECT command is not listed. This semicolon is necessary to indicate the end of the command when you enter it, but it is not part of the SQL command and SQL\*Plus does not store it in the SQL buffer.

Example 5-2 Listing the Buffer Contents

Suppose you want to list the current command. Use the LIST command as shown. (If you have exited SQL\*Plus or entered another SQL command or PL/SQL block since following the steps in [Example 4-3](SQL-Plus-basics.md), perform the steps in that example again before continuing.)

```
LIST
```

#### 5.2.2 Editing the Current Line

The SQL\*Plus CHANGE command enables you to edit the current line. Various actions determine which line is the current line:

- LIST a given line to make it the current line.
- When you LIST or RUN the command in the buffer, the last line of the command becomes the current line. (Note, that using the slash (/) command to run the command in the buffer does not affect the current line.)
- If you get an error, the error line automatically becomes the current line.
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

Note that the column SALARY retains the format you gave it in [Example 4-4](SQL-Plus-basics.md). (If you have left SQL\*Plus and started again since performing [Example 4-4](SQL-Plus-basics.md) the column has reverted to its original format.)

See [CHANGE](CHANGE.md) for information about the significance of case in a CHANGE command and on using wildcards to specify blocks of text in a CHANGE command.

Example 5-3 Making an Error in Command Entry

Suppose you try to select the JOB\_ID column but mistakenly enter it as JO\_ID. Enter the following command, purposely misspelling JOB\_ID in the first line:

```
SELECT EMPLOYEE_ID, LAST_NAME, JO_ID, SALARY
FROM EMP_DETAILS_VIEW
WHERE JOB_ID='SA_MAN';
```

You see this message on your screen:

Example 5-4 Correcting the Error

To change JO\_ID to JOB\_ID, change the line with the CHANGE command:

```
CHANGE /JO_ID/JOB_ID
```

The corrected line appears on your screen:

#### 5.2.3 Appending Text to a Line

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

#### 5.2.4 Adding a New Line

To insert a new line after the current line, use the INPUT command.

To insert a line before line 1, enter a zero ("0") and follow the zero with text. SQL\*Plus inserts the line at the beginning of the buffer and all lines are renumbered starting at 1.

```
0 SELECT EMPLOYEE_ID
```
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

Example 5-6 Adding a Line

Suppose you want to add a fourth line to the SQL command you modified in Example 5-4. Since line 3 is already the current line, enter INPUT and press Return.

```
INPUT
```

SQL\*Plus prompts you for the new line:

#### 5.2.5 Deleting Lines

Use the DEL command to delete lines in the buffer. Enter DEL specifying the line numbers you want to delete.

Suppose you want to delete the current line to the last line inclusive. Use the DEL command as shown.

```
DEL * LAST
```

DEL makes the following line of the buffer (if any) the current line.

See [DEL](DEL.md) for more information.

### 5.3 About Placing Comments in Scripts

You can enter comments in a script in three ways:

- using the SQL\*Plus REMARK command for single line comments.
- using the SQL comment delimiters /\*... \*/ for single or multi line comments.
- using ANSI/ISO (American National Standards Institute/International Standards Organization) comments - - for single line comments.
	Comments entered at the command-line are not stored in the SQL buffer.

#### 5.3.1 Using the REMARK Command

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

#### 5.3.2 Using /\*...\*/

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

#### 5.3.3 Using - -

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

#### 5.3.4 Notes on Placing Comments

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

For more information on substitution and termination characters, see DEFINE, SQLTERMINATOR and SQLBLANKLINES in the [SET](SET.md) command.

### 5.4 Running Scripts

The START command retrieves a script and runs the commands it contains. Use START to run a script containing SQL commands, PL/SQL blocks, and SQL\*Plus commands. You can have many commands in the file. Follow the START command with the name of the file:

```
START file_name
```

SQL\*Plus assumes the file has a.SQL extension by default.

Note:

Starting from Oracle Database release 19c, version 19.3, executing a script that contains a $ (dollar) symbol results in an error on Windows because the $ symbol denotes an environment variable in Linux and Unix.

For example:

```
SQL>@C:\User\my$script.sql
```

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

Example 5-7 Running a Script

To retrieve and run the command stored in SALES.SQL, enter

```
START SALES
```

SQL\*Plus runs the commands in the file SALES and displays the results of the commands on your screen, formatting the query results according to the SQL\*Plus commands in the file:

#### 5.4.1 Running a Script as You Start SQL\*Plus

To run a script as you start SQL\*Plus, use one of the following options:

- Follow the SQLPLUS command with your username, a slash, a space, @, and the name of the file:
	```
	SQLPLUS HR @SALES
	```
	SQL\*Plus starts, prompts for your password and runs the script.
- Include your username as the first line of the file. Follow the SQLPLUS command with @ and the filename. SQL\*Plus starts, prompts for your password and runs the file.

### 5.5 Nesting Scripts

To run a series of scripts in sequence, first create a script containing several START commands, each followed by the name of a script in the sequence. Then run the script containing the START commands. For example, you could include the following START commands in a script named SALESRPT:

```
START Q1SALES
START Q2SALES
START Q3SALES
START Q4SALES
START YRENDSLS
```

Note:

The @@ command may be useful in this example. See the [@@ (double at sign)](double-at-sign.md) command for more information.

### 5.6 About Exiting from a Script with a Return Code

You can include an EXIT command in a script to return a value when the script finishes. See the [EXIT](EXIT.md) command for more information.

You can include a WHENEVER SQLERROR command in a script to automatically exit SQL\*Plus with a return code should your script generate a SQL error. Similarly, you can include a WHENEVER OSERROR command to automatically exit should an operating system error occur. See the [WHENEVER SQLERROR](WHENEVER-SQLERROR.md) command, and the [WHENEVER OSERROR](WHENEVER-OSERROR.md) command for more information.