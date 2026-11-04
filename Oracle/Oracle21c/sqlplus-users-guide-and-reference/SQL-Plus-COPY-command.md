---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SQL-Plus-COPY-command.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

This appendix discusses the following topics:

Read this chapter while sitting at your computer and try out the example shown. Before beginning, make sure you have access to the sample tables described in [SQL\*Plus Quick Start](SQL-Plus-quick-start.md) .

The COPY command will be deprecated in future releases of SQL\*Plus. After Oracle 9i, no new datatypes are supported by COPY.

### B.1 COPY Command Syntax

```
COPY {FROM database | TO database | FROM database TO database}            {APPEND|CREATE|INSERT|REPLACE} destination_table [(column, column, column, ...)]  USING query
```

where database has the following syntax:

```
username[/password]@connect_identifier
```

Copies data from a query to a table in the same or another database. COPY supports the following datatypes:

- CHAR
- DATE
- LONG
- NUMBER
- VARCHAR2

WARNING:

Including your password in plain text is a security risk. You can avoid this risk by omitting the password, and entering it only when the system prompts for it.

#### B.1.1 Terms

See the following list for a description of each term or clause:

```
FROM database
```

The database that contains the data to be copied. If you omit the FROM clause, the source defaults to the database to which SQL\*Plus is connected (that is, the database that other commands address). You must use a FROM clause to specify a source database other than the default. The COPY command FROM clause does not support SYSDBA or SYSOPER privileged connections.

```
TO database
```

The database containing the destination table. If you omit the TO clause, the destination defaults to the database to which SQL\*Plus is connected (that is, the database that other commands address). You must use a TO clause to specify a destination database other than the default. The COPY command TO clause does not support SYSDBA or SYSOPER privileged connections.

```
database
```

Specifies username\[/password\] @connect\_identifier of the Oracle Database source or destination database you wish to COPY FROM or COPY TO. The COPY command does not support SYSDBA or SYSOPER privileged connections. You must include a username. SQL\*Plus prompts you for the password associated with the username specified in the COPY FROM or COPY TO clauses. SQL\*Plus suppresses the display of your password response.

You must include the connect\_identifier clause to specify the source or destination database. The exact syntax depends on the Oracle Net configuration. For more information, refer to the Oracle Net manual or contact your DBA.

```
APPEND
```

Inserts the rows from query into destination\_table if the table exists. If destination\_table does not exist, COPY creates it.

```
CREATE
```

Inserts the rows from query into destination\_table after first creating the table. If destination\_table already exists, COPY returns an error.

```
INSERT
```

Inserts the rows from query into destination\_table. If destination\_table does not exist, COPY returns an error. When using INSERT, the USING query must select one column for each column in destination\_table.

```
REPLACE
```

Replaces destination\_table and its contents with the rows from query. If destination\_table does not exist, COPY creates it. Otherwise, COPY drops the existing table and replaces it with a table containing the copied data.

```
destination_table
```

Represents the table you wish to create or to which you wish to add data.

```
(column, column, column, ...)
```

Specifies the names of the columns in destination\_table. You must enclose a name in double quotes if it contains lowercase letters or blanks.

If you specify columns, the number of columns must equal the number of columns selected by the query. If you do not specify any columns, the copied columns will have the same names in the destination table as they had in the source if COPY creates destination\_table.

```
USING query
```

Specifies a SQL query (SELECT command) determining which rows and columns COPY copies.

#### B.1.2 Usage

To enable the copying of data between Oracle and non-Oracle databases, NUMBER columns are changed to DECIMAL columns in the destination table. Hence, if you are copying between Oracle databases, a NUMBER column with no precision will be changed to a DECIMAL(38) column. When copying between Oracle databases, you should use SQL commands (CREATE TABLE AS and INSERT) or you should ensure that your columns have a precision specified.

The SQL\*Plus SET LONG variable limits the length of LONG columns that you copy. If any LONG columns contain data longer than the value of LONG, COPY truncates the data.

SQL\*Plus performs a commit at the end of each successful COPY. If you set the SQL\*Plus SET COPYCOMMIT variable to a positive value n, SQL\*Plus performs a commit after copying every n batches of records. The SQL\*Plus SET ARRAYSIZE variable determines the size of a batch.

Some operating environments require that service names be placed in double quotes.

#### B.1.3 Examples

The following command copies the entire EMPLOYEES table to a table named WESTEMPLOYEES. Note that the tables are located in two different databases. If WESTEMPLOYEES already exists, SQL\*Plus replaces the table and its contents. The columns in WESTEMPLOYEES have the same names as the columns in the source table, EMPLOYEES.

```
COPY FROM HR@HQ TO JOHN@WEST -
REPLACE WESTEMPLOYEES -
USING SELECT * FROM EMPLOYEES
```

The following command copies selected records from EMPLOYEES to the database to which SQL\*Plus is connected. SQL\*Plus creates SALESMEN through the copy. SQL\*Plus copies only the columns EMPLOYEE\_ID and LAST\_NAME, and at the destination names them EMPLOYEE\_ID and SA\_MAN.

```
COPY FROM HR@ORACLE01 -
CREATE SALESMEN (EMPLOYEE_ID, SA_MAN) -
USING SELECT EMPLOYEE_ID, LAST_NAME FROM EMPLOYEES -
WHERE JOB_ID='SA_MAN';
```

### B.2 Copying Data from One Database to Another

Use the SQL\*Plus COPY command to copy CHAR, DATE, LONG, NUMBER or VARCHAR2 data between databases and between tables on the same database. With the COPY command, you can copy data between databases in the following ways:

- Copy data from a remote database to your local database.
- Copy data from your local (default) database to a remote database (most systems).
- Copy data from one remote database to another remote database (most systems).
	Note:
	In general, the COPY command was designed to be used for copying data between Oracle and non-Oracle databases. You should use SQL commands (CREATE TABLE AS and INSERT) to copy data between Oracle databases.

#### B.2.1 Understanding COPY Command Syntax

You enter the COPY command in the following form:

```
COPY FROM database TO database action -
destination_table (column_name, column_name, -
column_name ...) USING query
```

Here is a sample COPY command:

```
COPY FROM HR@BOSTONDB -
TO TODD@CHICAGODB -
CREATE NEWDEPT (DEPARTMENT_ID, DEPARTMENT_NAME, CITY) -
USING SELECT * FROM EMP_DETAILS_VIEW
```

To specify a database in the FROM or TO clause, you must have a valid username and password for the local and remote databases and know the appropriate Oracle Net service names. COPY obeys Oracle Database security, so the username you specify must have been granted access to tables for you to have access to tables. For information on what databases are available to you, contact your DBA.

When you copy to your local database from a remote database, you can omit the TO clause. When you copy to a remote database from your local database, you can omit the FROM clause. When you copy between remote databases, you must include both clauses. However, including both clauses increases the readability of your scripts.

The COPY command behaves differently based on whether the destination table already exists and on the action clause you enter (CREATE in the example). See About Controlling Treatment of the Destination Table for more information.

By default, the copied columns have the same names in the destination table that they have in the source table. If you want to give new names to the columns in the destination table, enter the new names in parentheses after the destination table name. If you enter any column names, you must enter a name for every column you are copying.

Note:

To enable the copying of data between Oracle and non-Oracle databases, NUMBER columns are changed to DECIMAL columns in the destination table. Hence, if you are copying between Oracle databases, a NUMBER column with no precision will be changed to a DECIMAL(38) column. When copying between Oracle databases, you should use SQL commands (CREATE TABLE AS and INSERT) or you should ensure that your columns have a precision specified.

The USING clause specifies a query that names the source table and specifies the data that COPY copies to the destination table. You can use any form of the SQL SELECT command to select the data that the COPY command copies.

Here is an example of a COPY command that copies only two columns from the source table, and copies only those rows in which the value of DEPARTMENT\_ID is 30:

```
COPY FROM HR@BOSTONDB -
REPLACE EMPCOPY2 -
USING SELECT LAST_NAME, SALARY -
FROM EMP_DETAILS_VIEW -
WHERE DEPARTMENT_ID = 30
```

You may find it easier to enter and edit long COPY commands in scripts rather than trying to enter them directly at the command prompt.

#### B.2.2 About Controlling Treatment of the Destination Table

You control the treatment of the destination table by entering one of four control clauses—REPLACE, CREATE, INSERT, or APPEND.

The REPLACE clause names the table to be created in the destination database and specifies the following actions:

- If the destination table already exists, COPY drops the existing table and replaces it with a table containing the copied data.
- If the destination table does not already exist, COPY creates it using the copied data.

You can use the CREATE clause to avoid accidentally writing over an existing table. CREATE specifies the following actions:

- If the destination table already exists, COPY reports an error and stops.
- If the destination table does not already exist, COPY creates the table using the copied data.

Use INSERT to insert data into an existing table. INSERT specifies the following actions:

- If the destination table already exists, COPY inserts the copied data in the destination table.
- If the destination table does not already exist, COPY reports an error and stops.

Use APPEND when you want to insert data in an existing table, or create a new table if the destination table does not exist. APPEND specifies the following actions:

- If the destination table already exists, COPY inserts the copied data in the destination table.
- If the table does not already exist, COPY creates the table and then inserts the copied data in it.

Note:

See your DBA for an appropriate username, password, and service name for a remote computer that contains a copy of EMPLOYEE\_COPY.

```
COPY FROM HR@BOSTONDB -
CREATE EMPCOPY -
USING SELECT * FROM HR
```
```
Array fetch/bind size is 15. (arraysize is 15)
Will commit when done. (copycommit is 0)
Maximum long size is 80. (long is 80)
```

SQL\*Plus then creates the table EMPLOYEE\_COPY and copies the rows:

```
Table SALESMAN created.

   5 rows selected from HR@BOSTONDB.
   5 rows inserted into SALESMAN.
   5 rows committed into SALESMAN at DEFAULT HOST connection.
```

In this COPY command, the FROM clause directs COPY to connect you to the database with the specification BOSTONDB as HR.

Notice that you do not need a semicolon at the end of the command; COPY is a SQL\*Plus command, not a SQL command, even though it contains a query. Since most COPY commands are longer than one line, you must use a line continuation hyphen (-), optionally preceded by a space, at the end of each line except the last.

Example B-1 Copying from a Remote Database to Your Local Database Using CREATE

To copy HR from a remote database into a table called EMPLOYEE\_COPY on your own database, enter the following command:

#### B.2.3 About Interpreting the Messages that COPY Displays

The first three messages displayed by COPY show the values of SET command variables that affect the COPY operation. The most important one is LONG, which limits the length of a LONG column's value. (LONG is a datatype, similar to CHAR.) If the source table contains a LONG column, COPY truncates values in that column to the length specified by the system variable LONG.

The variable ARRAYSIZE limits the number of rows that SQL\*Plus fetches from the database at one time. This number of rows makes up a batch. The variable COPYCOMMIT sets the number of batches after which COPY commits changes to the database. (If you set COPYCOMMIT to zero, COPY commits changes only after all batches are copied.) For more information on SET variables, including how to change their settings, see the [SET](SET.md) command.

After listing the three system variables and their values, COPY tells you if a table was dropped, created, or updated during the copy. Then COPY lists the number of rows selected, inserted, and committed.

#### B.2.4 Specifying Another User's Table

You can refer to another user's table in a COPY command by qualifying the table name with the username, just as you would in your local database, or in a query with a database link.

For example, to make a local copy of a table named DEPARTMENT owned by the username ADAMS on the database associated with the Oracle Net connect identifier BOSTONDB, you would enter

```
COPY FROM HR@BOSTONDB -
CREATE EMPLOYEE_COPY2 -
USING SELECT * FROM ADAMS.DEPARTMENT
```

Of course, you could get the same result by instructing COPY to log in to the remote database as ADAMS. You cannot do that, however, unless you know the password associated with the username ADAMS.

### B.3 About Copying Data between Tables on One Database

You can copy data from one table to another in a single database (local or remote). To copy between tables in your local database, specify your own username and the service name for your local database in either a FROM or a TO clause (omit the other clause):

```
COPY FROM HR@MYDATABASE -
INSERT EMPLOYEE_COPY2 -
USING SELECT * FROM EMPLOYEE_COPY
```

To copy between tables on a remote database, include the same username and service name in the FROM and TO clauses:

```
COPY FROM HR@BOSTONDB -
TO HR@BOSTONDB -
INSERT EMPLOYEE_COPY2 -
USING SELECT * FROM EMPLOYEE_COPY
```