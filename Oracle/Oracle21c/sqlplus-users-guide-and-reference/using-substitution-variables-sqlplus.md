---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/using-substitution-variables-sqlplus.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

This chapter explains how SQL\*Plus substitution variables work and where they can be used. It shows the relationship between the three types of variables (substitution, bind, and system) used in SQL\*Plus.

This topics covered are:

### 6.1 Defining Substitution Variables

You can define variables, called substitution variables, for repeated use in a single script by using the SQL\*Plus DEFINE command. Note that you can also define substitution variables to use in titles and to save your keystrokes (by defining a long string as the value for a variable with a short name).

```
DEFINE L_NAME = "SMITH" (CHAR)
```

To list all substitution variable definitions, enter DEFINE by itself. Note that any substitution variable you define explicitly through DEFINE takes only CHAR values (that is, the value you assign to the variable is always treated as a CHAR datatype). You can define a substitution variable of datatype NUMBER implicitly through the ACCEPT command. You will learn more about the ACCEPT command.

To delete a substitution variable, use the SQL\*Plus command UNDEFINE followed by the variable name.

Example 6-1 Defining a Substitution Variable

To define a substitution variable L\_NAME and give it the value "SMITH", enter the following command:

```
DEFINE L_NAME = SMITH
```

To confirm the variable definition, enter DEFINE followed by the variable name:

```
DEFINE L_NAME
```

### 6.2 About Using Predefined Variables

There are nine variables containing SQL\*Plus information that are defined during SQL\*Plus installation. These variables can be redefined, referenced or removed the same as any other variable. They are always available from session to session unless you explicitly remove or redefine them.

See Also:

[Predefined Variables](DEFINE.md) for a list of the predefined variables and examples of their use.

### 6.3 Referencing Substitution Variables

Suppose you want to write a query like the one in SALES to list the employees with various jobs, not just those whose job is SA\_MAN. You could do that by editing a different value into the WHERE clause each time you run the command, but there is an easier way.

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

#### 6.3.1 Where and How to Use Substitution Variables

You can use substitution variables anywhere in SQL and SQL\*Plus commands, except as the first word entered. When SQL\*Plus encounters an undefined substitution variable in a command, SQL\*Plus prompts you for the value.

You can enter any string at the prompt, even one containing blanks and punctuation. If the SQL command containing the reference should have quote marks around the variable and you do not include them there, the user must include the quotes when prompted.

SQL\*Plus reads your response from the keyboard or standard input.

After you enter a value at the prompt, SQL\*Plus lists the line containing the substitution variable twice: once before substituting the value you enter and once after substitution. You can suppress this listing by setting the SET command variable VERIFY to OFF.

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

A more practical use of substitution variables is to prompt for a value before referencing the variable:

```
SQL> accept myv char prompt 'Enter a last name: ' 
SQL> select employee_id from employees where last_name = '&myv';
```

If these two commands are stored in a SQL\*Plus script, a different last name can be entered each time the script is run.

If you wish to append characters immediately after a substitution variable, use a period to separate the variable from the character. For example:

```
SELECT SALARY FROM EMP_DETAILS_VIEW WHERE EMPLOYEE_ID='&X.5';
Enter value for X:  20
```

is interpreted as

```
SELECT SALARY FROM EMP_DETAILS_VIEW WHERE EMPLOYEE_ID='205';
```

If you want to append a period immediately after a substitution variable name, then use two periods together. For example, if "myfile" is defined as "reports" then the command:

```
SQL> spool &myfile..log
```

is the same as:

```
SQL> spool reports.log
```

Text in ANSI "/\* \*/" or "--" comments that looks like a substitution variable may be treated as one. For example:

```
SQL> select department_id, location_id /* get dept & loc */ from departments;
Enter value for loc: _
```

Here the text "& loc" in the comment is interpreted as a variable reference. SQL\*Plus prompts you for a value for the variable "loc".

Example 6-2 Using Substitution Variables

Create a script named STATS, to be used to calculate a subgroup statistic (the maximum value) on a numeric column:

```
SELECT &GROUP_COL, MAX(&NUMBER_COL) MAXIMUM
FROM &TABLE
GROUP BY &GROUP_COL
.
SAVE STATS
```

#### 6.3.2 Difference Between "&" and "&&" Prefixes

Both single ampersand (&) and double ampersand (&&) can prefix a substitution variable name in a statement. SQL\*Plus pre-processes the statement and substitutes the variable's value. The statement is then executed. If the variable was not previously defined then SQL\*Plus prompts you for a value before doing the substitution.

If a single ampersand prefix is used with an undefined variable, the value you enter at the prompt is not stored. Immediately after the value is substituted in the statement the variable is discarded and remains undefined. If the variable is referenced twice, even in the same statement, then you are prompted twice. Different values can be entered at each prompt:

```
SQL> prompt Querying table &mytable
Enter value for mytable: employees
Querying table employees
SQL> select employee_id from &mytable where last_name = 'Jones';
Enter value for mytable: employees

EMPLOYEE_ID
-----------
        195
```

If a double ampersand reference causes SQL\*Plus to prompt you for a value, then SQL\*Plus defines the variable as that value (that is, the value is stored until you exit). Any subsequent reference to the variable (even in the same command) using either "&" or "&&" substitutes the newly defined value. SQL\*Plus will not prompt you again:

```
SQL> prompt Querying table &&mytable
Enter value for mytable: employees
Querying table employees
SQL> select employee_id from &mytable where last_name = 'Jones';

EMPLOYEE_ID
-----------
        195
```

#### 6.3.3 Storing a Query Column Value in a Substitution Variable

Data stored in the database can be put into substitution variables:

```
SQL> column last_name new_value mynv
SQL> select last_name from employees where employee_id = 100;
```

The `NEW_VALUE` option in the `COLUMN` command implicitly creates a substitution variable called `mynv`. The variable is not physically created until a query references the column `LAST_NAME`. When the query finishes, the variable `mynv` holds the last retrieved value from the column `LAST_NAME`:

```
SQL> define mynv
DEFINE mynv      = "King" (CHAR)
```

#### 6.3.4 Restrictions

You cannot use substitution variables in the buffer editing commands, APPEND, CHANGE, DEL, and INPUT, nor in other commands where substitution would be meaningless. The buffer editing commands, APPEND, CHANGE, and INPUT, treat text beginning with "&" or "&&" literally, like any other text string.

#### 6.3.5 How Substitution Variables are Handled in SQL\*Plus

Substitution variable references are pre-processed and substituted before the command is parsed and executed. For each statement, SQL\*Plus will do the following:

```
1. Loop for each "&" and "&&" variable reference:
    If the variable already has a value defined (i.e. stored)
        Replace the variable reference with the value
    else
        Prompt for a value
        Replace the variable reference with the value
        If the variable is prefixed with "&&" then
            define (i.e. store) the variable for future use

2. Execute the statement
```

Step 1 happens inside the SQL\*Plus client tool. SQL\*Plus then sends the final statement to the database engine where step 2 occurs.

It is not possible to repeatedly prompt in a PL/SQL loop. This example prompts once and the entered value is substituted in the script text. The resulting script is then sent to the database engine for execution. The same entered value is stored five times in the table:

```
begin
  for i in 1 .. 5 loop
    insert into mytable values (&myv);
  end loop;
end;
/
```

Substitution variables are not recursively expanded. If the value of a referenced variable contains an ampersand, then the ampersand is used literally and is not treated as a second variable prefix:

```
SQL> set escape \
SQL> define myv = \&mytext
SQL> prompt &myv
&mytext
```

You cannot use a substitution variable as the first token of a command. Each command name must be hard-coded text else an error is displayed. For example:

```
SQL> &myv * from dual;
SP2-0734: unknown command beginning "&myv * fro..." - rest of line ignored.
```

#### 6.3.6 Substitution Variable Commands

Substitution variables can be used to replace options and values in almost all SQL\*Plus commands. Several of the commands have special significance for substitution variables.

| Command | Description |
| --- | --- |
| `ACCEPT` | Reads a line of input and stores it in a given substitution variable. |
| `COLUMN` | Specifies display attributes for a given column. |
| `DEFINE` | Specifies a user or predefined variable and assigns a CHAR value to it, or lists the value and variable type of a single variable or all variables. |
| `EDIT` | Invokes an operating system text editor on the contents of the specified file or on the contents of the buffer. |
| `EXIT` | Commits or rolls back all pending changes, logs out of Oracle Database, terminates SQL\*Plus and returns control to the operating system. |
| `HOST` | Executes an operating system command without leaving SQL\*Plus. |
| `TTITLE`, `BTITLE`, `REPHEADER`, `REPFOOTER` | `TTITLE` places and formats a specified title at the top of each report page.  `BTITLE` places and formats a specified title at the bottom of each report page.  `REPHEADER` places and formats a specified report header at the top of each report.  `REPFOOTER` places and formats a specified report footer at the bottom of each report. |
| `UNDEFINE` | Deletes one or more substitution variables that you defined either explicitly (with the `DEFINE` command) or implicitly (with an argument to the `START` command). |
| `WHENEVER` | `WHENEVER OSERROR` performs the specified action (exits SQL\*Plus by default) if an operating system error occurs (such as a file writing error).  `WHENEVER SQLERROR` performs the specified action (exits SQL\*Plus by default) if a SQL command or PL/SQL block generates an error. |

See [SQL\*Plus Command Summary](SQL-Plus-command-summary.md) for more information about these substitution variable commands.

##### 6.3.6.1 Using "&" Prefixes With Title Variables

The title commands (TTITLE, BTITLE, REPHEADER and REPFOOTER) substitute variables differently to most other commands. (The exceptions are the EXIT and SET SQLPROMPT commands, which are similar to the title commands).

The guidelines for variables in titles are:
- If you want the same value for a variable to be printed on every page then use an "&" prefix and put the variable inside a quoted string:
	```
	accept mycustomer char prompt 'Enter your company name: '
	ttitle left 'Report generated for company &mycustomer'
	select last_name, job_id from employees order by job_id;
	```
- If you want each title to have data from the query that is unique to each report page then do not use an "&" prefix for the variable and do not put the variable inside quotes.
	```
	column job_id new_value ji_nv noprint
	break on job_id skip page
	ttitle left 'Employees in job: ' ji_nv
	select last_name, job_id from employees order by job_id;
	```

SQL\*Plus substitution variables are expanded before each command is executed. After this happens in a title command, the resulting string is stored as the title text. What makes variables in titles special is that they need to be re-substituted for each page of query results. This is so the current COLUMN NEW\_VALUE and OLD\_VALUE substitution variable values are displayed on each page, customizing each title for the results displayed on its page. If "&" is used inadvertently or incorrectly to prefix title variables, it is possible to get double substitution. This is dependent on the variable's value and is easily overlooked when you write scripts.

Any non-quoted, non-keyword in a title is checked when the page is printed to see if it is a variable. If it is, its value is printed. If not, then the word is printed verbatim. This means that if you use "&myvar" in a title command, and the text substituted for it can itself be interpreted as another variable name then you get double variable substitution. For example, the script:

```
define myvar = scottsvar
ttitle left &myvar
define scottsvar = Hello
select * from dual;
```

causes the text "left scottsvar" to be stored as the title. When the title is printed on each page of the query this string is re-evaluated. The word "scottsvar" in the title is itself treated as a variable reference and substituted. The query output is:

```
Hello
D
-
deX
```

Using "&" in titles most commonly causes a problem with the numeric variable names of the SQL\*Plus script parameters. If the value of an arbitrary "&"-prefixed title variable is the same as a script parameter variable name, then double substitution will occur.

To display an "&" in a title, prefix it with the SET ESCAPE character. The ampersand (&) is stored as the title text and is not substituted when page titles are printed.

##### 6.3.6.2 Variables and Text Spacing in Titles

Unquoted whitespace in titles is removed. Use whitespace instead of the SET CONCAT character to separate variables from text that should appear immediately adjacent. Use whitespace inside quotes to display a space. For example, the script:

```
define myvar = 'ABC'
ttitle left myvar myvar Text ' Other words'
select ...;
```

gives a title of:

```
ABCABCText Other words
```

#### 6.3.7 Substitution Variable Namespace, Types, Formats and Limits

Substitution Variable Namespace

In a SQL\*Plus session there is just one global name space for substitution variables. If you reconnect using CONNECT, or run subscripts using "@", all variables ever defined are available for use and may be overridden or undefined.

When a child script finishes, all substitution variables it defined or changed are visible to the calling script. This is particularly noticeable when a subscript executed with "@" or START is given script parameters. The parameters "&1" etc. get redefined and the parent script sees the new values.

To minimize problems, and for general readability, use symbolic variable names for command parameters. All other references should use the new variable name instead of "&1". For example:
```
define myuser = '&1'
@myscript.sql King
select first_name from employees where last_name = '&myuser';
```

The call to myscript.sql changes the value of "&1" to "King". By saving the original value of "&1" in "myuser" and using "&myuser" instead of "&1" in the SELECT, the query executes correctly.

Substitution Variable Types

The substitution variable types stored by SQL\*Plus are:

- CHAR
- NUMBER
- BINARY\_FLOAT
- BINARY\_DOUBLE

The CHAR type is a generic text format similar to the database table VARCHAR2 column type. All variables created from the following are of type CHAR:

- with DEFINE
- from prompts for "&" variables
- from script parameters

This ensures that values entered are substituted verbatim with no conversion loss.

Variables created by COLUMN NEW\_VALUE or OLD\_VALUE for the columns in Oracle number format will have the type NUMBER. These substitution variables are stored in Oracle's internal number representation as they are in the database. This allows display formats to be altered without any internal value loss. Substitution variables of BINARY\_FLOAT and BINARY\_DOUBLE types are similarly created for Oracle BINARY\_FLOAT and BINARY\_DOUBLE columns. These variables are stored in native machine representation. The CHAR type is used for NEW\_VALUE and OLD\_VALUE variables with all other column types.

There is no explicit DATE type. The DATE keyword in the ACCEPT command is used solely to allow correct format validation against a date format. Substitution variables created by ACCEPT... DATE, or by COLUMN NEW\_VALUE on a date column, are stored as type CHAR. For example:

```
SQL> accept mydvar date format 'DD-MON-YYYY'
prompt 'Enter a date: '
Enter a date: 03-APR-2003
SQL> define mydvar
DEFINE MYDVAR              = "03-APR-2003" (CHAR)
```

If a variable already exists and is redefined, its old type is discarded and the new type used.

The type of a substitution variable is generally transparent. Substitution variables are weakly typed. For example, a COLUMN NEW\_VALUE variable takes on the particular type of the named column in each new query. It may also change type during a query. For example, the type of a substitution variable used on a NUMBER column changes from NUMBER to CHAR when a NULL value is fetched. It changes back to NUMBER when the next numeric value is fetched.

No type comparison semantics are defined for any type since there is no direct comparison of variables. All variables are textually substituted before any SQL or PL/SQL statement that could do a comparison is executed.

Substitution Variable Formats

When a variable is substituted, or its value is shown by a DEFINE command, it is formatted as text before the command referencing the variable is finally executed.

CHAR variables are substituted verbatim.

NUMBER variables are formatted according to SET NUMWIDTH (by default) or SET NUMFORMAT (if you have explicitly set one):

The display format of a number can be changed even after the variable is created. To show this, first create a NUMBER variable. You cannot use DEFINE to do this because it makes the type of all new variables CHAR. Instead use a COLUMN NEW\_VALUE command which inherits the NUMBER type from a NUMBER column:

```
SQL> column c2 new_val m
SQL> select 1.1 c2 from dual C2;
----------
1.1
SQL> define m
DEFINE M               =        1.1 (NUMBER)
```

Changing the format affects the display of the number but not the stored value:

```
SQL> set numformat 99.990
SQL> define m
DEFINE M               =   1.100 (NUMBER)
```

Substitution Variable Limits

The maximum number of substitution variables allowed is 2048. SQL\*Plus gives an error an attempt is made to create more. The limit includes the predefined variables, however these can be undefined if necessary. Leaving a large number of unnecessarily defined variables can reduce the performance of SQL\*Plus because variable lookups are slower.

A character substitution variable can be up to 240 bytes long.

A numeric substitution variable holds the full range of Oracle numbers.

When a command line undergoes variable substitution, the resulting line length can be no more than:

- 3000 bytes if it is a line of SQL (like SELECT or INSERT) or PL/SQL text (like BEGIN or CREATE PROCEDURE)
- 2499 bytes if it a line of a SQL\*Plus command (like TTITLE or COLUMN)

Otherwise an error is displayed.

These limits may be lower in old versions of SQL\*Plus.

#### 6.3.8 Assigning Substitution Variables to Bind Variables

You can assign a substitution variable to a bind variable:

```
SQL> define mysubv = 123 
SQL> variable mybndv number 
SQL> execute :mybndv := &mysubv;
```

SQL\*Plus executes the PL/SQL assignment statement after it substitutes the value of "mysubv". If "mysubv" was not already defined, you would be prompted for a value.

The bind variable can be used in subsequent SQL or PL/SQL commands.

#### 6.3.9 Assigning Bind Variables to Substitution Variables

Sometimes it is useful to make the value of a bind variable available to SQL\*Plus commands like TTITLE or SPOOL. For example, you might want to call a PL/SQL function that returns a string and use the value for a SQL\*Plus spool file name. The SPOOL command does not understand bind variable syntax so the bind variable value needs to be assigned to a substitution variable first.

This is done using COLUMN NEW\_VALUE and SELECT commands. For example, declare a bind variable in SQL\*Plus and instantiate it in a PL/SQL block. Its value can be returned from a PL/SQL function, or like here, set by a direct assignment:

```
SQL> variable mybv varchar2(14)
SQL> begin
  2    /* ... */
  3    :mybv := 'report.log';
  4  end;
  5  /
```

Pass the bind variable's value to a new substitution variable "nv" by using a query:

```
SQL> column mybvcol new_value nv noprint
SQL> select :mybv mybvcol from dual;
```

Now you can use the substitution variable in a SPOOL command:

```
SQL> spool &nv
```

The SPOOL command executes as if you had typed

```
SQL> spool report.log
```

#### 6.3.10 Substitution Variable Examples

The following examples demonstrate how to use substitution variables.

- Setting a Substitution Variable's Value
- Using a Substitution Variable
- Finding All Defined Substitution Variables
- Inserting Data Containing "&" Without Being Prompted
- Putting the Current Date in a Spool File Name
- Appending Alphanumeric Characters Immediately After a Substitution Variable
- Putting a Period After a Substitution Variable
- Using a Fixed Value Variable in a TTITLE, BTITLE, REPHEADER or REPFOOTER
- Using a Changing Value Variable in a TTITLE, BTITLE, REPHEADER or REPFOOTER
- Using the Value of a Bind Variable in a SQL\*Plus Command Like SPOOL
- Passing Parameters to SQL\*Plus Substitution Variables
- Passing Operating System Variables to SQL\*Plus
- Passing a Value to a PL/SQL Procedure From the Command Line
- Allowing Script Parameters to be Optional and Have a Default Value
- Using a Variable for the SQL\*Plus Return Status
- Putting the Username and Database in the Prompt

##### 6.3.10.1 Setting a Substitution Variable's Value

A substitution variable can be set in several ways. The common ways are as follows:

- The DEFINE command sets an explicit value:
	```
	define myv = 'King'
	```
- The ACCEPT command:
	```
	accept myv char prompt 'Enter a last name: '
	```
	prompts you for a value and creates a character variable "myv" set to the text you enter.
- Using "&&" before an undefined variable prompts you for a value and uses that value in the statement:
	```
	select first_name from employees where last_name = '&&myuser';
	```
	If the substitution variable "myuser" is not already defined, then this statement creates "myuser" and sets it to the value you enter.
- Using COLUMN NEW\_VALUE to set a substitution variable to a value stored in the database:
	```
	column last_name new_value mynv     select last_name from employees where employee_id = 100;
	```
	This creates a substitution variable "mynv" set to the value in the "last\_name" column.

##### 6.3.10.2 Using a Substitution Variable

Once a substitution variable has a value, it can be referenced by prefixing the variable name with an ampersand (&).

If the variable "myv" is already defined, it can be used as:

```
select employee_id from employees where last_name = '&myv';
```

##### 6.3.10.3 Finding All Defined Substitution Variables

The DEFINE command with no parameters shows all defined substitution variables, their values, and their types. For example:

```
define
```

might give:

```
DEFINE MYV             = "King" (CHAR)
...
```

##### 6.3.10.4 Inserting Data Containing "&" Without Being Prompted

There are two ways to make an "&" be treated as text and not cause a prompt. The first turns all variable substitution off:

```
set define off
create table mytable (c1 varchar2(20));
insert into mytable (c1) values ('thick & thin');
```

The INSERT statement stores the text "thick & thin" in the table.

The second method is useful for ignoring individual occurrences of "&" while allowing others to prefix substitution variables:

```
set escape \
create table mytable (c1 varchar2(20));
insert into mytable (c1) values ('thick \& thin');
insert into mytable (c1) values ('&mysubvar');
```

The first INSERT statement in this method stores the text "thick & thin" in the table. The second INSERT causes SQL\*Plus to prompt you for a value, which is then stored.

##### 6.3.10.5 Putting the Current Date in a Spool File Name

Using SYSDATE you can query the current date and put it in a substitution variable. The substitution variable can then be used in a SPOOL command:

```
column dcol new_value mydate noprint
select to_char(sysdate,'YYYYMMDD') dcol from dual;
spool &mydate.report.txt

-- my report goes here
select last_name from employees;

spool off
```

In this example, the first query puts the date in the substitution variable "mydate". There is no visible output from this query because of the NOPRINT option in the COLUMN command. In the SPOOL command, the first period (.) indicates the end of the variable name and is not included in the resulting string. If "mydate" contained "20030120" from the first query, then the spool file name would be "20030120report.txt".

You can use this technique to build up any string for the file name.

The period is the default value of SET CONCAT. If you have assigned another character, use it instead of a period to end the substitution variable name.

##### 6.3.10.6 Appending Alphanumeric Characters Immediately After a Substitution Variable

If you wish to append alphanumeric characters immediately after a substitution variable, use the value of SET CONCAT to separate the variable name from the following text. The default value of SET CONCAT is a single period (.). For example:

```
define mycity = Melbourne 
spool &mycity.Australia.txt
```

creates a file with the name "MelbourneAustralia.txt".

##### 6.3.10.7 Putting a Period After a Substitution Variable

If SET CONCAT is a period (.) and you want to append a period immediately after a substitution variable, use two periods together. For example:

```
define mycity = Melbourne
spool &mycity..log
```

is the same as:

```
spool Melbourne.log
```

##### 6.3.10.8 Using a Fixed Value Variable in a TTITLE, BTITLE, REPHEADER or REPFOOTER

This example makes every page of a report have exactly the same heading. It can be used for TTITLE, BTITLE, REPHEADER or REPFOOTER commands. In a TTITLE command, prefix the variable name "dept" with "&" and place it inside a quoted string:

```
define dept = '60'
ttitle left 'Salaries for department &dept'
select last_name, salary from employees where department_id = &dept;
```

##### 6.3.10.9 Using a Changing Value Variable in a TTITLE, BTITLE, REPHEADER or REPFOOTER

This example uses a different title on every page of a report. Each title contains a value derived from query results shown on that particular page. In a TTITLE command, do not put an "&" before the variable name "dv". Put the variable name outside a quoted string:

```
column department_id new_value dv noprint
ttitle left 'Members of department ' dv
break on department_id skip page
select department_id, last_name from employees order by department_id, last_name;
```

In a BTITLE or REPFOOTER command, use a COLUMN OLD\_VALUE variable instead of a COLUMN NEW\_VALUE variable.

##### 6.3.10.10 Using the Value of a Bind Variable in a SQL\*Plus Command Like SPOOL

If you want to use the value of a bind variable in a SQL\*Plus command, it must first be copied to a substitution variable.

SQL\*Plus commands such as SPOOL, SET and TTITLE are executed in the SQL\*Plus program and are not passed to the database for execution. Because of this, these commands do not understand bind variables.

To use a bind variable's value as the name of a spool file:

```
-- Set a bind variable to a text string
variable mybindvar varchar2(20)
begin
  :mybindvar := 'myspoolfilename';
end;

-- Transfer the value from the bind variable to the substitution variable
column mc new_value mysubvar noprint
select :mybindvar mc from dual;

-- Use the substitution variable
spool &mysubvar..txt
select * from employees;

spool off
```

##### 6.3.10.11 Passing Parameters to SQL\*Plus Substitution Variables

You can pass parameters on the command line to a SQL\*Plus script:

```
sqlplus hr/my_password @myscript.html employees "De Haan"
```

They can be referenced in the script using "&1" and "&2". For example, myscript.sql could be:

```
set verify off
select employee_id from &1 where last_name = '&2';
```

Here the "SET VERIFY OFF" command stops SQL\*Plus from echoing the SQL statement before and after the variables are substituted. The query returns the employee identifier for the employee "De Haan" from the "employees" table.

Parameters can also be passed to scripts called within SQL\*Plus:

```
SQL> @myscript.sql employees "De Haan"
```

##### 6.3.10.12 Passing Operating System Variables to SQL\*Plus

You can pass an operating system variable to a SQL\*Plus script as a command line parameter. For example, on UNIX:

```
sqlplus hr/my_password @myscript.sql $USER
```

or in a Windows command window:

```
sqlplus hr/my_password @myscript.sql %USERNAME%
```

The script myscript.sql could reference the substitution variable "&1" to see the passed name.

##### 6.3.10.13 Passing a Value to a PL/SQL Procedure From the Command Line

If you create a procedure "myproc":

```
create or replace procedure myproc (p1 in number) as
begin
  dbms_output.put_line('The number is '||p1);
end;
/
```

and myscript.sql contains:

```
begin
  myproc(&1);
end;
/
```

then calling:

```
sqlplus hr/my_password @myscript.sql 88
```

executes the script as if it is:

```
begin
  myproc(88);
end;
/
```

This method does not work if the parameter "p1" to "myproc" is "IN OUT". The variable reference is pre-processed and is effectively a hardcoded value which cannot contain an OUT value. To get around this, you can assign the substitution variable to a bind variable. The script myscript.sql becomes:

```
variable mybindvar number
begin
  :mybindvar := &1;
  myproc(:mybindvar);
end;
/
```

##### 6.3.10.14 Allowing Script Parameters to be Optional and Have a Default Value

The goal is to create a script that accepts an optional parameter. If a parameter is passed from the command line, then its value should be used. However, if there is no parameter, then SQL\*Plus should ask for a value with a customized prompt. Perhaps the closest solution is with a PROMPT/DEFINE sequence. If myscript.sql is:

```
-- Name: myscript.sql
prompt Enter a value for PAGESIZE
set termout off
define mypar = &1
set termout on
prompt Setting PAGESIZE to &mypar
set pagesize &mypar
select last_name from employees where rownum < 20;
exit
```

you can call the script with or without a parameter. If you enter "12" at the prompt your screen looks like:

```
$ sqlplus hr/my_password @myscript.sql
SQL*Plus: Release 9.2.0.3.0 - Production on Wed Mar 5 15:19:40 2003
. . .
Enter a value for PAGESIZE     12
Setting PAGESIZE to 12

LAST_NAME
-------------------------
King
Kochhar
De Haan
. . .
```

or if you call it with a parameter "8":

```
$ sqlplus hr/my_password @myscript.sql 8
SQL*Plus: Release 9.2.0.3.0 - Production on Wed Mar 5 15:20:38 2003
. . .
Enter a value for PAGESIZE
Setting PAGESIZE to 8

LAST_NAME
-------------------------
King
Kochhar
De Haan
. . .
```

Note when you pass a parameter, the PROMPT text is still displayed, but you do not enter a value. The PROMPT command is the SQL\*Plus "echo" or "print" statement. (It does not read input). The only occurrence of "&1" should be where "mypar" is defined. All other references to the parameter should use "&mypar" or "&&mypar".

##### 6.3.10.15 Using a Variable for the SQL\*Plus Return Status

To use the value of a substitution variable called "myv" as the SQL\*Plus return status, use:

```
EXIT myv
```

No ampersand (&) prefix is required before the substitution variable name.

A numeric bind variable requires a colon (:) prefix:

```
EXIT :mybv
```

##### 6.3.10.16 Putting the Username and Database in the Prompt

In SQL\*Plus 10g, add the following to your glogin.sql or login.sql:

```
set sqlprompt "_user'@'_connect_identifier:SQL> "
```

For customized prompts that query the database, ensure that you explicitly DEFINE any referenced substitution variables. Glogin.sql and login.sql can get run when there is no database connection. Defining variables prevents the user being prompted for values when the query fails and the variables do not get defined by it:

```
set termout off
define myv = 'Not connected'
column myc new_value myv
select user||'@'||global_name myc from global_name;
set sqlprompt '&myv:SQL> '
set termout on
```

SQL\*Plus 9.2 and earlier do not re-execute glogin.sql and login.sql after CONNECT commands. Also, variables in the SQLPROMPT are not dynamically substituted. It is possible to use the query script given above, but note that the prompt will only be valid for the original connection.

### 6.4 System Variables Influencing Substitution Variables

The following system variables, specified with the SQL\*Plus SET command, affect substitution variables:

| System Variable | Affect on Substitution Variables |
| --- | --- |
| ``` SET CONCAT ``` | Defines the character that separates the name of a substitution variable or parameter from characters that immediately follow the variable or parameter—by default the period (.). |
| ``` SET DEFINE ``` | Defines the substitution character (by default the ampersand "&") and turns substitution on and off. |
| ``` SET ESCAPE ``` | Defines an escape character you can use before the substitution character. The escape character instructs SQL\*Plus to treat the substitution character as an ordinary character rather than as a request for variable substitution. The default escape character is a backslash (\\). |
| ``` SET NUMFORMAT ``` | Sets the default format for displaying numbers, including numeric substitution variables. |
| ``` SET NUMWIDTH ``` | Sets the default width for displaying numbers, including numeric substitution variables. |
| ``` SET SQLPROMPT ``` | Sets the SQL\*Plus command prompt. |
| ``` SET VERIFY ON ``` | Lists each line of the script before and after substitution. |

See [SET](SET.md) for more information about system variables.

#### 6.4.1 System Variables in Titles and EXIT

There is a special syntax to reference system variables in TTITLE, BTITLE, REPHEADER, REPFOOTER, and EXIT commands. The name of each special variable is the same as the SHOW option prefixed with "SQL.".

The special variables that can be referenced include:

- SQL.PNO - page number
- SQL.LNO - line number
- SQL.USER - current username
- SQL.RELEASE - SQL\*Plus version
- SQL.SQLCODE - last Oracle "ORA" error number

For example:

```
SQL> ttitle left 'Salary Report. Page: ' sql.pno
SQL> select salary from employees;
SQL> exit sql.sqlcode
```

System variables of numeric type, such as SQL.SQLCODE, are formatted using the same rules as numeric substitution variables.

The variables cannot be prefixed with an "&".

These variables are not substitution variables. The DEFINE command does not show them. They cannot be referenced in general commands. The system variables are not affected if you create substitution variables with the same name. For example, SQL.USER is not affected if you create a substitution variable called USER. The system variable SQL.RELEASE is not affected if the predefined substitution variable \_O\_RELEASE is changed.

### 6.5 Passing Parameters through the START Command

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

Example 6-3 Passing Parameters through START

To create a new script based on SALES that takes a parameter specifying the job to be displayed, enter

```
GET SALES
```

#### 6.5.1 Script Parameters

Parameters can be passed to SQL\*Plus scripts. For example, from the command line:

```
sqlplus hr/my_password @myscript.sql King
```

You can also pass parameters when calling a SQL\*Plus script from within a SQL\*Plus session, for example:

```
SQL> @myscript.sql King
```

Script parameters become defined substitution variables. The variable name for the first parameter is "1", the second is "2", etc. The effect is the same as starting SQL\*Plus and typing:

```
SQL> define 1 = King
SQL> @myscript.sql
```

Commands in myscript.sql can reference "&1" to get the value "King". A DEFINE command shows the parameter variable:

```
SQL> define 1
DEFINE 1      = "King" (CHAR)
```

Script parameter variables have type CHAR, similar to variables explicitly created with DEFINE.

Quoting parameters with single or double quotes is allowed. This lets whitespace be used within parameters. Operating systems and scripting languages that call SQL\*Plus handle quotes in different ways. They may or may not pass quotes to the SQL\*Plus executable. For example, in a standard Bourne shell on UNIX, quotes around parameters are stripped before the parameters are passed to SQL\*Plus, and SQL\*Plus never sees the quotes.

It is recommended to check how quoted parameters are handled on your operating system with your patch level of SQL\*Plus. For portability between UNIX and Windows environments use double quotes around parameters containing whitespace.

SQL\*Plus Releases 8.1.7, 9.2.0.3 (and other 9.x versions patched for bug 2471872) and 10.1 onwards remove an outer set of single or double quotes from parameters passed on the SQL\*Plus command line. This makes SQL\*Plus behave the same way on operating systems that do not themselves strip quotes as it does when the operating system strips the quotes before calling SQL\*Plus.

As an example of passing parameters, when SQL\*Plus 10.1 is called in the UNIX shell script:

```
#! /bin/sh
sqlplus hr/<i>my_password</i> @myscript.sql "Jack and Jill"
```

only one program parameter is defined. References in myscript.sql to "&1" are replaced with "Jack and Jill" (without quotes - because the shell script does not pass quotes to SQL\*Plus).

### 6.6 About Communicating with the User

Three SQL\*Plus commands—PROMPT, ACCEPT, and PAUSE—help you communicate with the end user. These commands enable you to send messages to the screen and receive input from the user, including a simple Return. You can also use PROMPT and ACCEPT to customize the prompts for values SQL\*Plus automatically generates for substitution variables.

#### 6.6.1 Receiving a Substitution Variable Value

Through PROMPT and ACCEPT, you can send messages to the end user and receive values from end-user input. PROMPT displays a message you specify on-screen to give directions or information to the user. ACCEPT prompts the user for a value and stores it in the substitution variable you specify. Use PROMPT in conjunction with ACCEPT when a prompt spans more than one line.

```
Created file PROMPT1.sql
```

The TTITLE command sets the top title for your report. See [About Defining Page and Report Titles and Dimensions](formatting-SQL-Plus-reports.md) for more information about the TTITILE command.

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

Example 6-4 Prompting for and Accepting Input

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

#### 6.6.2 Customizing Prompts for Substitution Variable

If you want to customize the prompt for a substitution variable value, use PROMPT and ACCEPT in conjunction with the substitution variable, as shown in the following example.

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

Example 6-5 Using PROMPT and ACCEPT in Conjunction with Substitution Variables

As you have seen in Example 6-4, SQL\*Plus automatically generates a prompt for a value when you use a substitution variable. You can replace this prompt by including PROMPT and ACCEPT in the script with the query that references the substitution variable. First clear the buffer with:

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

#### 6.6.3 Sending a Message and Accepting Return as Input

If you want to display a message on the user's screen and then have the user press Return after reading the message, use the SQL\*Plus command PAUSE. For example, you might include the following lines in a script:

```
PROMPT Before continuing, make sure you have your account card.
PAUSE Press RETURN to continue.
```

#### 6.6.4 Clearing the Screen

If you want to clear the screen before displaying a report (or at any other time), include the SQL\*Plus CLEAR command with its SCREEN clause at the appropriate point in your script, using the following format:

```
CLEAR SCREEN
```

Before continuing to the next section, reset all columns to their original formats and headings by entering the following command:

```
CLEAR COLUMNS
```

### 6.7 About Using Bind Variables

Bind variables are variables you create in SQL\*Plus and then reference in PL/SQL or SQL. If you create a bind variable in SQL\*Plus, you can use the variable as you would a declared variable in your PL/SQL subprogram and then access the variable from SQL\*Plus. You can use a bind variable as an input bind variable to hold data which can then be used in PL/SQL or SQL statements to insert data into the database. You can assign a value to a newly defined variable. The value assigned in this variable can then be used in a statement.

Because bind variables are recognized by SQL\*Plus, you can display their values in SQL\*Plus or reference them in PL/SQL subprograms that you run in SQL\*Plus.

#### 6.7.1 Creating Bind Variables

You create bind variables in SQL\*Plus with the VARIABLE command. For example

```
VARIABLE ret_val NUMBER
```

This command creates a bind variable named ret\_val with a datatype of NUMBER. See the [VARIABLE](VARIABLE.md) command for more information. (To list all bind variables created in a session, type VARIABLE without any arguments.)

#### 6.7.2 Referencing Bind Variables

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

#### 6.7.3 Displaying Bind Variables

To display the value of a bind variable in SQL\*Plus, you use the SQL\*Plus PRINT command. For example:

```
PRINT RET_VAL
```
```
RET_VAL
----------
         4
```

This command displays a bind variable named ret\_val. See [PRINT](PRINT.md) for more information about displaying bind variables.

#### 6.7.4 Executing an Input Bind

You can assign a value to a variable for input binding.

```
SQL> variable abc number=123 
SQL> select :abc from dual;

        :ABC 
----------  
         123

SQL>
```
```
SQL> create table mytab (col1 number, col2 varchar2(10));  

Table created.  

SQL> var abc number=123 
SQL> var xyz varchar2(10)='test' 
SQL> insert into mytab values(:abc,:xyz);  

1 row created.  

SQL> select * from mytab;        

       COL1 COL2 
---------- ----------
        123 test 

SQL>
```

See the [VARIABLE](VARIABLE.md) command for more information.

### 6.8 Using REFCURSOR Bind Variables

SQL\*Plus REFCURSOR bind variables allow SQL\*Plus to fetch and format the results of a SELECT statement contained in a PL/SQL block.

REFCURSOR bind variables can also be used to reference PL/SQL cursor variables in stored procedures. This enables you to store SELECT statements in the database and reference them from SQL\*Plus.

A REFCURSOR bind variable can also be returned from a stored function.

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

Example 6-6 Creating, Referencing, and Displaying REFCURSOR Bind Variables

To create, reference and display a REFCURSOR bind variable, first declare a local bind variable of the REFCURSOR datatype

```
create procedure p4 as
  c1 sys_refcursor;
  c2 sys_refcursor;
begin
  open c1 for SELECT * FROM DEPT;
  dbms_sql.return_result(c1);
  open c2 for SELECT * FROM EMP;
  dbms_sql.return_result(c2);
end;
/
```

Next, enter a PL/SQL block that uses the bind variable in an OPEN... FOR SELECT statement. This statement opens a cursor variable and executes a query. See [OPEN Statement](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=LNPLS-GUID-FB5A9CC3-655F-4AF4-8105-14CB39F2FEA8) for information on the OPEN command and cursor variables.

In this example we are binding the SQL\*Plus employee\_info bind variable to the cursor variable.

```
BEGIN
OPEN :employee_info FOR SELECT EMPLOYEE_ID, SALARY
FROM     EMP_DETAILS_VIEW WHERE JOB_ID='SA_MAN' ;
END;
 /
```

Example 6-7 Using REFCURSOR Variables in Stored Procedures

A REFCURSOR bind variable is passed as a parameter to a procedure. The parameter has a REF CURSOR type. First, define the type.

```
CREATE OR REPLACE PACKAGE EmpPack AS
  TYPE EmpInfoTyp IS REF CURSOR;
  PROCEDURE EmpInfoRpt (emp_cv IN OUT EmpInfoTyp);
END EmpPack;
/
```

Example 6-8 Using REFCURSOR Variables in Stored Functions

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

### 6.9 Fetching Iterative Results from a SELECT inside a PL/SQL Block

SQL\*Plus can iteratively fetch and format the results of a SELECT statement contained in a PL/SQL block or stored procedure. You do not need to define local REFCURSOR variables.

The results from the SELECT statements are displayed.

```
ResultSet #1
```
```
DEPTNO DNAME       LOC
------ ----------  ---------
10     ACCOUNTING  NEW YORK
20     RESEARCH    DALLAS
30     SALES       CHICAGO
40     OPERATIONS  BOSTON

4 rows selected
```
```
ResultSet #2
```
```
EMPNO ENAME  JOB       MGR  HIREDATE  SAL  COMM DEPTNO
----- ------ --------- ---- --------- ---- ---- --
7369  SMITH  CLERK     7902 17-DEC-80  800      20
7499  ALLEN  SALESMAN  7698 20-FEB-81 1600  300 30
7521  WARD   SALESMAN  7698 22-FEB-81 1250  500 30
7566  JONES  MANAGER   7839 02-APR-81 2975      20
7654  MARTIN SALESMAN  7698 28-SEP-81 1250 1400 30
7698  BLAKE  MANAGER   7839 01-MAY-81 2850      30
7782  CLARK  MANAGER   7839 09-JUN-81 2450      10
7788  SCOTT  ANALYST   7566 05-APR-11 3000      20
7839  KING   PRESIDENT      17-NOV-81 5000      10
7844  TURNER SALESMAN  7698 08-SEP-81 1500    0 30
7876  ADAMS  CLERK     7788 09-MAY-11 1100

14 rows selected
```

Example 6-9 Creating a PL/SQL Procedure

Create a PL/SQL procedure P4 which calls two statements.

```
create procedure p4 as
    c1 sys_refcursor;
    c2 sys_refcursor;
begin
    open c1 for SELECT * FROM DEBT;
    dbms_sql.return_result(c1);
    open c2 for SELECT * FROM EMP;
    dbms_sql.return_result(c2);
end;
/
Procedure created.
```

Next, run the procedure to retrieve results iteratively from the SELECT statements in the procedure.

```
exec p4
PL/SQL procedure successfully completed.
```