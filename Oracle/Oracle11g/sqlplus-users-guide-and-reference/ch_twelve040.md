---
title: SET System Variable Summary
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve040.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

| System Variable | Description |
| --- | --- |
| [SET APPI\[NFO\]{ON \| OFF \| text}](#i2698573) | Sets automatic registering of scripts through the DBMS\_APPLICATION\_INFO package. |
| [SET ARRAY\[SIZE\] {15 \| n}](#i2698625) | Sets the number of rows, called a batch, that SQL\*Plus will fetch from the database at one time. |
| [SET AUTO\[COMMIT\]{ON \| OFF \| IMM\[EDIATE\] \| n}](#i2698639) | Controls when Oracle Database commits pending changes to the database. |
| [SET AUTOP\[RINT\] {ON \| OFF}](#i2698656) | Sets the automatic printing of bind variables. |
| [SET AUTORECOVERY \[ON \| OFF\]](#i2698666) | ON sets the RECOVER command to automatically apply the default filenames of archived redo log files needed during recovery. |
| [SET AUTOT\[RACE\] {ON \| OFF \| TRACE\[ONLY\]} \[EXP\[LAIN\]\] \[STAT\[ISTICS\]\]](#i2698680) | Displays a report on the execution of successful SQL DML statements (SELECT, INSERT, UPDATE, DELETE or MERGE). |
| [SET BLO\[CKTERMINATOR\] {. \| c \| ON \| OFF}](#i2698691) | Sets the non-alphanumeric character used to end PL/SQL blocks to c. |
| [SET CMDS\[EP\] {; \| c \| ON \| OFF}](#i2698702) | Sets the non-alphanumeric character used to separate multiple SQL\*Plus commands entered on one line to c. |
| SET COLSEP { \| text} | Sets the text to be printed between selected columns. |
| [SET CON\[CAT\] {. \| c \| ON \| OFF}](#i2698818) | Sets the character you can use to terminate a substitution variable reference if you wish to immediately follow the variable with a character that SQL\*Plus would otherwise interpret as a part of the substitution variable name. |
| [SET COPYC\[OMMIT\] {0 \| n}](#i2698834) | Controls the number of batches after which the COPY command commits changes to the database. |
| SET COPYTYPECHECK {ON \| OFF} | Sets the suppression of the comparison of datatypes while inserting or appending to tables with the COPY command. |
| [SET DEF\[INE\] {& \| c \| ON \| OFF}](#i2698854) | Sets the character used to prefix variables to c. |
| [SET DESCRIBE \[DEPTH {1 \| n \| ALL}\] \[LINENUM {ON \| OFF}\] \[INDENT {ON \| OFF}\]](#i2698865) | Sets the depth of the level to which you can recursively describe an object. |
| SET ECHO {ON \| OFF} | Controls whether the START command lists each command in a script as the command is executed. |
| [SET EDITF\[ILE\] file\_name\[.ext\]](#i2678328) | Sets the default filename for the EDIT command. |
| [SET EMB\[EDDED\] {ON \| OFF}](#i2698935) | Controls where on a page each report begins. |
| [SET ERRORL\[OGGING\] {ON \| OFF} \[TABLE \[schema.\]tablename\] \[TRUNCATE\] \[IDENTIFIER identifier\]](#i2698945) | Enables recording of SQL, PL/SQL and SQL\*Plus errors to an error log table which you can query later. |
| [SET ESC\[APE\] {\\ \| c \| ON \| OFF}](#BGBFAHDB) | Defines the character you enter as the escape character. |
| SET ESCCHAR {@ \|? \| % \| $ \| OFF} | Specifies a special character to escape in a filename. Prevents character translation causing an error. |
| [SET EXITC\[OMMIT\] {ON \| OFF}](#BABEGEGC) | Specifies whether the default EXIT behavior is COMMIT or ROLLBACK. |
| [SET FEED\[BACK\] {6 \| n \| ON \| OFF}](#i2698970) | Displays the number of records returned by a query when a query selects at least n records. |
| [SET FLAGGER {OFF \| ENTRY \| INTERMED\[IATE\] \| FULL}](#i2698986) | Checks to make sure that SQL statements conform to the ANSI/ISO SQL92 standard. |
| [SET FLU\[SH\] {ON \| OFF}](#i2678409) | Controls when output is sent to the user's display device. |
| [SET HEA\[DING\] {ON \| OFF}](#i2699001) | Controls printing of column headings in reports. |
| [SET HEADS\[EP\] { \| c \| ON \| OFF}](#i2699036) | Defines the character you enter as the heading separator character. |
| [SET INSTANCE \[instance\_path \| LOCAL\]](#i2699050) | Changes the default instance for your session to the specified instance path. |
| [SET LIN\[ESIZE\] {80 \| n}](#i2678481) | Sets the total number of characters that SQL\*Plus displays on one line before beginning a new line. |
| [SET LOBOF\[FSET\] {1 \| n}](#i2699091) | Sets the starting position from which BLOB, BFILE, CLOB and NCLOB data is retrieved and displayed. |
| [SET LOGSOURCE \[pathname\]](#i2699109) | Specifies the location from which archive logs are retrieved during recovery. |
| SET LONG {80 \| n} | Sets maximum width (in bytes) for displaying LONG, BLOB, BFILE, CLOB, NCLOB and XMLType values; and for copying LONG values. |
| [SET LONGC\[HUNKSIZE\] {80 \| n}](#i2699146) | Sets the size (in bytes) of the increments in which SQL\*Plus retrieves a LONG, BLOB, BFILE, CLOB, NCLOB or XMLType value. |
| [SET MARK\[UP\] HTML \[ON \| OFF\] \[HEAD text\] \[BODY text\] \[TABLE text\] \[ENTMAP {ON \| OFF}\] \[SPOOL {ON \| OFF}\] \[PRE\[FORMAT\] {ON \| OFF}\]](#i2699173) | Outputs HTML marked up text. |
| [SET NEWP\[AGE\] {1 \| n \| NONE}](#i2678637) | Sets the number of blank lines to be printed from the top of each page to the top title. |
| SET NULL text | Sets the text that represents a null value in the result of a SQL SELECT command. |
| [SET NUMF\[ORMAT\] format](#i2699195) | Sets the default format for displaying numbers. |
| [SET NUM\[WIDTH\] {10 \| n}](#i2699209) | Sets the default width for displaying numbers. |
| [SET PAGES\[IZE\] {14 \| n}](#i2699247) | Sets the number of lines in each page. |
| [SET PAU\[SE\] {ON \| OFF \| text}](#i2699261) | Enables you to control scrolling of your terminal when running reports. |
| [SET RECSEP {WR\[APPED\] \| EA\[CH\] \| OFF}](#i2699269) | RECSEP tells SQL\*Plus where to make the record separation. |
| SET RECSEPCHAR { \| c} | Display or print record separators. |
| [SET SERVEROUT\[PUT\] {ON \| OFF} \[SIZE {n \| UNL\[IMITED\]}\] \[FOR\[MAT\] {WRA\[PPED\] \| WOR\[D\_WRAPPED\] \| TRU\[NCATED\]}\]](#i2699298) | Controls whether to display the output (that is, DBMS\_OUTPUT PUT\_LINE) of stored procedures or PL/SQL blocks in SQL\*Plus. |
| [SET SHIFT\[INOUT\] {VIS\[IBLE\] \| INV\[ISIBLE\]}](#i2678863) | Enables correct alignment for terminals that display shift characters. |
| [SET SHOW\[MODE\] {ON \| OFF}](#i2678887) | Controls whether SQL\*Plus lists the old and new settings of a SQL\*Plus system variable when you change the setting with SET. |
| [SET SQLBL\[ANKLINES\] {ON \| OFF}](#i2678904) | Controls whether SQL\*Plus puts blank lines within a SQL command or script. |
| [SET SQLC\[ASE\] {MIX\[ED\] \| LO\[WER\] \| UP\[PER\]}](#i2699335) | Converts the case of SQL commands and PL/SQL blocks just prior to execution. |
| [SET SQLCO\[NTINUE\] {> \| text}](#i2678950) | Sets the character sequence SQL\*Plus displays as a prompt after you continue a SQL\*Plus command on an additional line using a hyphen (–). |
| [SET SQLN\[UMBER\] {ON \| OFF}](#i2678981) | Sets the prompt for the second and subsequent lines of a SQL command or PL/SQL block. |
| [SET SQLPLUSCOMPAT\[IBILITY\] {x.y\[.z\]}](#i2699351) | Sets the behavior or output format of VARIABLE to that of the release or version specified by x.y\[.z\]. |
| [SET SQLPRE\[FIX\] {# \| c}](#i2679105) | Sets the SQL\*Plus prefix character. |
| [SET SQLP\[ROMPT\] {SQL> \| text}](#i2679128) | Sets the SQL\*Plus command prompt. |
| [SET SQLT\[ERMINATOR\] {; \| c \| ON \| OFF}](#i2498515) | Sets the character used to end and execute SQL commands to c. |
| [SET SUF\[FIX\] {SQL \| text}](#i2683419) | Sets the default file that SQL\*Plus uses in commands that refer to scripts. |
| SET TAB {ON \| OFF} | Determines how SQL\*Plus formats white space in terminal output. |
| [SET TERM\[OUT\] {ON \| OFF}](#i2683459) | Controls the display of output generated by commands executed from a script. |
| [SET TI\[ME\] {ON \| OFF}](#i2700163) | Controls the display of the current time. |
| [SET TIMI\[NG\] {ON \| OFF}](#i2699400) | Controls the display of timing statistics. |
| [SET TRIM\[OUT\] {ON \| OFF}](#i2683480) | Determines whether SQL\*Plus puts trailing blanks at the end of each displayed line. |
| [SET TRIMS\[POOL\] {ON \| OFF}](#i2683501) | Determines whether SQL\*Plus puts trailing blanks at the end of each spooled line. |
| [SET UND\[ERLINE\] {- \| c \| ON \| OFF}](#i2699420) | Sets the character used to underline column headings in SQL\*Plus reports to c. |
| [SET VER\[IFY\] {ON \| OFF}](#i2699432) | Controls whether SQL\*Plus lists the text of a SQL statement or PL/SQL command before and after SQL\*Plus replaces substitution variables with values. |
| [SET WRA\[P\] {ON \| OFF}](#i2699438) | Controls whether SQL\*Plus truncates the display of a SELECTed row if it is too long for the current line width. |
| [SET XMLOPT\[IMIZATIONCHECK\] \[ON\|OFF\]](#CACFBBCI) | Specifies that only fully optimized XML queries and DML operations are executed. Only to assist in developing and debugging, not for production. |
| SET XQUERY BASEURI {text} | Defines the base URI to use. This is useful to change the prefix of the file to access when writing generic XQuery expressions. |
| SET XQUERY ORDERING {UNORDERED \| ORDERED \| DEFAULT} | Controls the ordering of results from an XQuery. |
| SET XQUERY NODE {BYVALUE \| BYREFERENCE \| DEFAULT} | Sets the preservation mode for notes created or returned. |
| SET XQUERY CONTEXT {text} | Specifies an XQuery context item which can be either a node or a value. |

---

## SET APPI\[NFO\]{ON | OFF | text}

Sets automatic registering of scripts through the DBMS\_APPLICATION\_INFO package.

This enables the performance and resource usage of each script to be monitored by your DBA. The registered name appears in the MODULE column of the V$SESSION and V$SQLAREA virtual tables. You can also read the registered name using the DBMS\_APPLICATION\_INFO.READ\_MODULE procedure.

ON registers scripts invoked by the @, @@ or START commands. OFF disables registering of scripts. Instead, the current value of text is registered. text specifies the text to register when no script is being run or when APPINFO is OFF, which is the default. The default for text is "SQL\*Plus". If you enter multiple words for text, you must enclose them in quotes. The maximum length for text is limited by the DBMS\_APPLICATION\_INFO package.

The registered name has the format nn@xfilename where: nn is the depth level of script; x is '<' when the script name is truncated, otherwise, it is blank; and filename is the script name, possibly truncated to the length allowed by the DBMS\_APPLICATION\_INFO package interface.

For more information on the DBMS\_APPLICATION\_INFO package, see the [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm).

Example

To display the value of APPINFO, as it is SET OFF by default, enter

```
SET APPINFO ON
SHOW APPINFO
```

```
APPINFO is ON and set to "SQL*Plus"
```

To change the default text, enter

```
SET APPINFO 'This is SQL*Plus'
```

To make sure that registration has taken place, enter

```
VARIABLE MOD VARCHAR2(50)
VARIABLE ACT VARCHAR2(40)
EXECUTE DBMS_APPLICATION_INFO.READ_MODULE(:MOD, :ACT);
```

```
PL/SQL procedure successfully completed.
```

```
PRINT MOD
```

```
MOD
---------------------------------------------------
This is SQL*Plus
```

To change APPINFO back to its default setting, enter

```
SET APPINFO OFF
```

---

## SET ARRAY\[SIZE\] {15 | n}

Sets the number of rows that SQL\*Plus will fetch from the database at one time.

Valid values are 1 to 5000. A large value increases the efficiency of queries and subqueries that fetch many rows, but requires more memory. Values over approximately 100 provide little added performance. ARRAYSIZE has no effect on the results of SQL\*Plus operations other than increasing efficiency.

---

## SET AUTO\[COMMIT\]{ON | OFF | IMM\[EDIATE\] | n}

Controls when Oracle Database commits pending changes to the database after SQL or PL/SQL commands.

ON commits pending changes to the database after Oracle Database executes each successful INSERT, UPDATE, or DELETE, or PL/SQL block. OFF suppresses automatic committing so that you must commit changes manually (for example, with the SQL command COMMIT). IMMEDIATE functions in the same manner as ON. n commits pending changes to the database after Oracle Database executes n successful SQL INSERT, UPDATE, or DELETE commands, or PL/SQL blocks. n cannot be less than zero or greater than 2,000,000,000. The statement counter is reset to zero after successful completion of n INSERT, UPDATE or DELETE commands or PL/SQL blocks, a commit, a rollback, or a SET AUTOCOMMIT command.

SET AUTOCOMMIT does not alter the commit behavior when SQL\*Plus exits. Any uncommitted data is committed by default.

Note:

For this feature, a PL/SQL block is considered one transaction, regardless of the actual number of SQL commands contained within it.

---

## SET AUTOP\[RINT\] {ON | OFF}

Sets the automatic printing of bind variables.

ON or OFF controls whether SQL\*Plus automatically displays bind variables (referenced in a successful PL/SQL block or used in an EXECUTE command).

See [PRINT](ch_twelve031.md) for more information about displaying bind variables.

---

## SET AUTORECOVERY \[ON | OFF\]

ON sets the RECOVER command to automatically apply the default filenames of archived redo log files needed during recovery.

No interaction is needed, provided the necessary files are in the expected locations with the expected names. The filenames used are derived from the values of the initialization parameters LOG\_ARCHIVE\_DEST and LOG\_ARCHIVE\_FORMAT.

OFF, the default option, requires that you enter the filenames manually or accept the suggested default filename given. See [RECOVER](ch_twelve033.md) for more information about database recovery.

Example

To set the recovery mode to AUTOMATIC, enter

```
SET AUTORECOVERY ON
RECOVER DATABASE
```

---

## SET AUTOT\[RACE\] {ON | OFF | TRACE\[ONLY\]} \[EXP\[LAIN\]\] \[STAT\[ISTICS\]\]

Displays a report on the execution of successful SQL DML statements (such as SELECT, INSERT, UPDATE, DELETE or MERGE).

The report can include execution statistics and the query execution path.

SQL\*Plus report output may differ for DML if dynamic sampling is in effect.

OFF does not display a trace report. ON displays a trace report. TRACEONLY displays a trace report, but does not print query data, if any. EXPLAIN shows the query execution path by performing an EXPLAIN PLAN. STATISTICS displays SQL statement statistics. Information about EXPLAIN PLAN is documented in the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm).

Using ON or TRACEONLY with no explicit options defaults to EXPLAIN STATISTICS.

The TRACEONLY option may be useful to suppress the query data of large queries. If STATISTICS is specified, SQL\*Plus still fetches the query data from the server, however, the data is not displayed.

The AUTOTRACE report is printed after the statement has successfully completed.

Information about Execution Plans and the statistics is documented in the [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm).

When SQL\*Plus produces a STATISTICS report, a second connection to the database is automatically created. This connection is closed when the STATISTICS option is set to OFF, or you log out of SQL\*Plus.

The formatting of your AUTOTRACE report may vary depending on the version of the server to which you are connected and the configuration of the server. The additional information and tabular output of AUTOTRACE PLAN is supported when connecting to Oracle Database 10g (Release 10.1) or later. When you connect to an earlier database, the older form or AUTOTRACE reporting is used.

AUTOTRACE is not available when FIPS flagging is enabled.

See [Tracing Statements](ch_eight.md) for more information on AUTOTRACE.

---

## SET BLO\[CKTERMINATOR\] {. | c | ON | OFF}

Sets the character used to end PL/SQL blocks to c.

It cannot be an alphanumeric character or a whitespace. To execute the block, you must issue a RUN or / (slash) command.

OFF means that SQL\*Plus recognizes no PL/SQL block terminator. ON changes the value of c back to the default period (.), not the most recently used character.

---

## SET CMDS\[EP\] {; | c | ON | OFF}

Sets the non-alphanumeric character used to separate multiple SQL\*Plus commands entered on one line to c.

ON or OFF controls whether you can enter multiple commands on a line. ON automatically sets the command separator character to a semicolon (;).

Example

To specify a title with TTITLE and format a column with COLUMN, both on the same line, enter

```
SET CMDSEP +
TTITLE LEFT 'SALARIES' + COLUMN SALARY FORMAT $99,999
SELECT LAST_NAME, SALARY FROM EMP_DETAILS_VIEW
WHERE JOB_ID = 'SH_CLERK';
```

```
SALARIES
LAST_NAME                   SALARY
------------------------- --------
Taylor                      $3,200
Fleaur                      $3,100
Sullivan                    $2,500
Geoni                       $2,800
Sarchand                    $4,200
Bull                        $4,100
Dellinger                   $3,400
Cabrio                      $3,000
Chung                       $3,800
Dilly                       $3,600
Gates                       $2,900
Perkins                     $2,500
Bell                        $4,000
Everett                     $3,900
McCain                      $3,200
Jones                       $2,800

SALARIES
LAST_NAME                   SALARY
------------------------- --------
Walsh                       $3,100
Feeney                      $3,000
OConnell                    $2,600
Grant                       $2,600

20 rows selected.
```

---

## SET COLSEP { | text}

Sets the column separator character printed between columns in output.

If the COLSEP variable contains blanks or punctuation characters, you must enclose it with single quotes. The default value for text is a single space.

In multi-line rows, the column separator does not print between columns that begin on different lines. The column separator does not appear on blank lines produced by BREAK... SKIP n and does not overwrite the record separator. See [SET RECSEP {WR\[APPED\] | EA\[CH\] | OFF}](#i2699269) for more information.

Example

To set the column separator to "|" enter

```
SET MARKUP HTML PREFORMAT ON
SET COLSEP '|'
SELECT LAST_NAME, JOB_ID, DEPARTMENT_ID
FROM EMP_DETAILS_VIEW
WHERE DEPARTMENT_ID = 20;
```

```
LAST_NAME                |JOB_ID    |DEPARTMENT_ID
-------------------------|----------|-------------
Hartstein                |MK_MAN    |           20
Fay                      |MK_REP    |           20
```

---

## SET CON\[CAT\] {. | c | ON | OFF}

Sets the character used to terminate a substitution variable reference when SQL\*Plus would otherwise interpret the next character as a part of the variable name.

SQL\*Plus resets the value of CONCAT to a period when you switch CONCAT on.

---

## SET COPYC\[OMMIT\] {0 | n}

Controls the number of rows after which the COPY command commits changes to the database.

COPY commits rows to the destination database each time it copies n row batches. Valid values are zero to 5000. You can set the size of a batch with the ARRAYSIZE variable. If you set COPYCOMMIT to zero, COPY performs a commit only at the end of a copy operation.

---

## SET COPYTYPECHECK {ON | OFF}

Sets the suppression of the comparison of datatypes while inserting or appending to tables with the COPY command.

This is to facilitate copying to DB2, which requires that a CHAR be copied to a DB2 DATE.

---

## SET DEF\[INE\] {& | c | ON | OFF}

Sets the character used to prefix substitution variables to c.

ON or OFF controls whether SQL\*Plus will scan commands for substitution variables and replace them with their values. ON changes the value of c back to the default '&', not the most recently used character. The setting of DEFINE to OFF overrides the setting of the SCAN variable.

See [SET SCAN {ON|OFF} (obsolete)](apc.md) for more information on the SCAN variable.

---

## SET DESCRIBE \[DEPTH {1 | n | ALL}\] \[LINENUM {ON | OFF}\] \[INDENT {ON | OFF}\]

Sets the depth of the level to which you can recursively describe an object.

The valid range of the DEPTH clause is from 1 to 50. If you SET DESCRIBE DEPTH ALL, then the depth will be set to 50, which is the maximum level allowed. You can also display the line number and indentation of the attribute or column name when an object contains multiple object types. Use the SET LINESIZE command to control the width of the data displayed.

See [DESCRIBE](ch_twelve019.md) for more information about describing objects.

Example

To create an object type ADDRESS, enter

```
CREATE TYPE ADDRESS AS OBJECT
  ( STREET  VARCHAR2(20),
    CITY    VARCHAR2(20)
  );
/
```

```
Type created
```

To create the table EMPLOYEE that contains a nested object, EMPADDR, of type ADDRESS, enter

```
CREATE TABLE EMPLOYEE
  (LAST_NAME VARCHAR2(30),
   EMPADDR ADDRESS,
   JOB_ID VARCHAR2(20),
   SALARY NUMBER(7,2)
  );
/
```

```
Table created
```

To describe the table EMPLOYEE to a depth of two levels, and to indent the output and display line numbers, enter:

```
SET DESCRIBE DEPTH 2 LINENUM ON INDENT ON
DESCRIBE employee
```

```
Name                            Null?    Type
       ------------------------------- -------- --------------------------
1      LAST_NAME                                VARCHAR2(30)
2      EMPADDR                                  ADDRESS
3    2   STREET                                 VARCHAR2(20)
4    2   CITY                                   VARCHAR2(20)
5      JOB_ID                                   VARCHAR2(20)
6      SALARY                                   NUMBER(7,2)
```

---

## SET ECHO {ON | OFF}

Controls whether or not to echo commands in a script that is executed with @, @@ or START. ON displays the commands on screen. OFF suppresses the display. ECHO does not affect the display of commands you enter interactively or redirect to SQL\*Plus from the operating system.

---

## SET EDITF\[ILE\] file\_name\[.ext\]

Sets the default filename for the EDIT command. See [EDIT](ch_twelve021.md) for more information about the EDIT command. The default filename for the EDIT command is afiedt.buf which is the SQL buffer. The buffer has no command history list and does not record SQL\*Plus commands.

You can include a path and/or file extension. See [SET SUF\[FIX\] {SQL | text}](#i2683419) for information on changing the default extension. The default filename and maximum filename length are operating system specific.

---

## SET EMB\[EDDED\] {ON | OFF}

Controls where on a page each report begins.

OFF forces each report to start at the top of a new page. ON enables a report to begin anywhere on a page. Set EMBEDDED to ON when you want a report to begin printing immediately following the end of the previously run report.

---

## SET ERRORL\[OGGING\] {ON | OFF} \[TABLE \[schema.\]tablename\] \[TRUNCATE\] \[IDENTIFIER identifier\]

Turns SQL\*Plus error logging ON or OFF. Error logging records SQL, PL/SQL and SQL\*Plus errors and associated parameters in an error log table. You can then query the log table to review errors resulting from a query. When error logging is ON, errors are recorded whether the query is run interactively or from a script. This is particularly useful for capturing errors generated from long running queries and avoids capturing all output using the SPOOL command, or having to remain present during the run.

By default, errors are written to a the table SPERRORLOG in your schema. If this table does not exist, it is created automatically. You can also use the TABLE schema.tablename option to specify other tables to use. When using a table other than SPERRORLOG, it must already exist, and you must have access to it. See Creating a User Defined Error Log Table.

If an internal error occurs, to avoid recursion errors caused by the errorlog calling itself, errorlogging is automatically set OFF.

Error logging is set OFF by default.

ON

Writes ORA, PLS and SP2 errors to the default table, SPERRORLOG.

OFF

Disables error.

TABLE \[schema.\]tablename

Specifies a user defined table to use instead of the default, SPERRORLOG. If you omit schema. the table is created in the current schema. The table you specify must exist, and you must have access permissions.

If the table specified does not exist, or you do not have access, an error message is displayed and the default table, SPERRORLOG, is used.

TRUNCATE

Clears all existing rows in the error log table and begins recording errors from the current session.

IDENTIFIER identifier

A user defined string to identify errors. You can use it to identify errors from a particular session or from a particular version of a query.

Creating a User Defined Error Log Table

You can create one or more error log tables to use other than the default. Before specifying a user defined error log table with the TABLE schema.tablename option, you must create it and ensure that you have permissions to access it. The error log table has the following column definitions:

Table 12-4 SQL\*Plus Error Log Column Definitions

| Column | Type | Description |
| --- | --- | --- |
| username | VARCHAR(256) | Oracle account name. |
| timestamp | TIMESTAMP | Time when the error occurred. |
| script | VARCHAR(1024) | Name of the originating script if applicable. |
| identifier | VARCHAR(256) | User defined identifier string. |
| message | CLOB | ORA, PLA or SP2 error message. No feed back messages are included. For example, "PL/SQL Block Created" is not recorded. |
| statement | CLOB | The statement causing the error. |

Using User Defined Error Log Tables

To use a user defined log table, you must have permission to access the table, and you must issue the SET ERRORLOGGING command with the TABLE schema.tablename option to identify the error log table and the schema if applicable.

Querying Error Log Tables

To view the records recorded in an error log table, you query the columns you want to view as for any table. The columns available are shown in Table 12-4, "SQL\*Plus Error Log Column Definitions".

Example

To use the default error log table to record query errors from a script, myfile.sql, which contains the following:

```
VARIABLE U REFCURSOR
BEGIN
  OPEN :U FOR SELECT * FROM DEPT;
END;
/

SHOW ERRORS PROCEDURE 'SSS'

SET GARBAGE

SELECT * 
FROM
GARBAGE
;
```

Enter the following:

```
SET ERRORLOGGING ON
@myfile
```

which produces the following output:

```
open :u for select * from dept;
                          *
ERROR at line 2:
ORA-6550: line 2, column 29:
PLS-00201: ORA-00942: table or view does not exist
ORA-6550: line 2, column 16:
PL/SQL: SQL Statement ignored

ERROR:
ORA-00907: missing right parenthesis

SP2-0158: unknown SET option "garbage"

garbage
*
ERROR at line 3:
ORA-00942: table or view does not exist
```

To view the errror log written to the default error log table, SPERRORLOG, enter:

```
SELECT TIMESTAMP, USERNAME, SCRIPT, IDENTIFIER, STATEMENT, MESSAGE
FROM SPERRORLOG;
```

which produces the following output:

| TIMESTAMP | USERNAME | SCRIPT | IDENTIFIER | STATEMENT | MESSAGE |
| --- | --- | --- | --- | --- | --- |
| Mon May 08 21:30:03 2006 | SYSTEM | d:\\myfile.sql |  | open:u for select \* from dept; | ORA-06550: line 2, column 27: |
| Mon May 08 21:30:05 2006 | SYSTEM | d:\\myfile.sql |  | open:u for select \* from dept; | PL/SQL: ORA-00942: table or view does not exist |
| Mon May 08 21:30:05 2006 | SYSTEM | d:\\myfile.sql |  | open:u for select \* from dept; | ORA-06550: line 2, column 13: |
| Mon May 08 21:30:05 2006 | SYSTEM | d:\\myfile.sql |  | open:u for select \* from dept; | PL/SQL: SQL Statement ignored |
| Mon May 08 21:30:06 2006 | SYSTEM | d:\\myfile.sql |  | show errors procedure "sss" | ORA-00907: missing right parenthesis |
| Mon May 08 21:30:09 2006 | SYSTEM | d:\\myfile.sql |  | set garbage | SP2-0158: unknown SET option "garbage" |
| Mon May 08 21:30:10 2006 | SYSTEM | d:\\myfile.sql |  | garbage | ORA-00942: table or view does not exist |

Example 2

To use a user defined error log table to record query errors from a script, myfile.sql, which contains the following:

```
VARIABLE U REFCURSOR
BEGIN
  OPEN :U FOR SELECT * FROM DEPT;
END;
/

SHOW ERRORS PROCEDURE 'SSS'

SET GARBAGE

SELECT * 
FROM
GARBAGE
;
```

Enter the following:

```
SET ERRORLOGGING ON
@MYFILE
```

which produces the following output:

```
open :u for select * from dept;
                          *
ERROR at line 2:
ORA-6550: line 2, column 29:
PLS-00201: ORA-00942: table or view does not exist
ORA-6550: line 2, column 16:
PL/SQL: SQL Statement ignored

ERROR:
ORA-00907: missing right parenthesis

SP2-0158: unknown SET option "garbage"

garbage
*
ERROR at line 3:
ORA-00942: table or view does not exist
```

To view the errror log written to the default error log table, SPERRORLOG, enter:

```
SELECT TIMESTAMP, USERNAME, SCRIPT, IDENTIFIER, STATEMENT, MESSAGE
FROM SPERRORLOG;
```

which produces the following output:

| TIMESTAMP | USERNAME | SCRIPT | IDENTIFIER | STATEMENT | MESSAGE |
| --- | --- | --- | --- | --- | --- |
| Mon May 08 21:30:03 2006 | SYSTEM | d:\\myfile.sql |  | open:u for select \* from dept; | ORA-06550: line 2, column 27: |
| Mon May 08 21:30:05 2006 | SYSTEM | d:\\myfile.sql |  | open:u for select \* from dept; | PL/SQL: ORA-00942: table or view does not exist |
| Mon May 08 21:30:05 2006 | SYSTEM | d:\\myfile.sql |  | open:u for select \* from dept; | ORA-06550: line 2, column 13: |
| Mon May 08 21:30:05 2006 | SYSTEM | d:\\myfile.sql |  | open:u for select \* from dept; | PL/SQL: SQL Statement ignored |
| Mon May 08 21:30:06 2006 | SYSTEM | d:\\myfile.sql |  | show errors procedure "sss" | ORA-00907: missing right parenthesis |
| Mon May 08 21:30:09 2006 | SYSTEM | d:\\myfile.sql |  | set garbage | SP2-0158: unknown SET option "garbage" |
| Mon May 08 21:30:10 2006 | SYSTEM | d:\\myfile.sql |  | garbage | ORA-00942: table or view does not exist |

Example 3

To use an error log table other than the default:

- Create the error log table you want to use
- Specify the table you want to use with the TABLE option of the SET ERRORLOGGING ON command.

The error log table must have the column definitions defined in Table 12-4, "SQL\*Plus Error Log Column Definitions".

John wants to use an error log table named john\_sperrorlog. John would run the following SQL statements to create the new error log table:

```
DROP TABLE john_sperrorlog;   
CREATE TABLE john_sperrorlog(username   VARCHAR(256), 
timestamp  TIMESTAMP,
script     VARCHAR(1024),
identifier VARCHAR(256),
message    CLOB,
statement  CLOB);
```

John then issues the following SET command to enable error logging using the newly created error log table

```
SET ERRORLOGGING ON TABLE john_sperrorlog
```

All error logging for John is now recorded to john\_sperrorlog, and not to the default error log table, SPERRORLOG.

Access privileges for the error log table are handled in the same way as for any user table. See the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for more information about granting access to tables.

---

## SET ESC\[APE\] {\\ | c | ON | OFF}

Defines the character used as the escape character.

OFF undefines the escape character. ON enables the escape character. ON changes the value of c back to the default "\\".

You can use the escape character before the substitution character (set through SET DEFINE) to indicate that SQL\*Plus should treat the substitution character as an ordinary character rather than as a request for variable substitution.

Example

If you define the escape character as an exclamation point (!), then

```
SET ESCAPE !
ACCEPT v1 PROMPT 'Enter !&1:'
```

displays this prompt:

```
Enter &1:
```

To set the escape character back to the default value of \\ (backslash), enter

```
SET ESCAPE ON
```

---

## SET ESCCHAR {@ |? | % | $ | OFF}

Specifies a character to be escaped and not interpreted when used in a file name for the SPOOL, START, @, RUN and EDIT commands. These special characters are translated to the following:

While it is not recommended that these characters are used in filenames, if you have legacy files that do use them, it might be useful to include a SET ESCCHAR command in your GLogin file to implement it across your site.

Example

If you include the character '$' in your filename, then

```
SET ESCCHAR $
RUN MYFILE$
```

behaves normally.

---

## SET EXITC\[OMMIT\] {ON | OFF}

Specifies whether the default EXIT behavior is COMMIT or ROLLBACK.

The default setting is ON, which means that work is committed on exit, whether you expected it to be committed or not. Set EXITCOMMIT OFF to rollback work on exit.

Table 12-5 shows the exit action associated with combinations of SET commands (AUTOCOMMIT & EXITCOMMIT) and the EXIT command.

Table 12-5 Exit Behavior: AUTOCOMMIT, EXITCOMMIT, EXIT

| AUTOCOMMIT | EXITCOMMIT | EXIT | Exit Behavior |
| --- | --- | --- | --- |
| ON | ON | \- | COMMIT |
| ON | OFF | \- | COMMIT |
| OFF | ON | \- | COMMIT |
| OFF | OFF | \- | ROLLBACK |
| ON | ON | COMMIT | COMMIT |
| ON | ON | ROLLBACK | COMMIT |
| ON | OFF | COMMIT | COMMIT |
| ON | OFF | ROLLBACK | COMMIT |
| OFF | ON | COMMIT | COMMIT |
| OFF | ON | ROLLBACK | ROLLBACK |
| OFF | OFF | COMMIT | COMMIT |
| OFF | OFF | ROLLBACK | ROLLBACK |

---

## SET FEED\[BACK\] {6 | n | ON | OFF}

Displays the number of records returned by a script when a script selects at least n records.

ON or OFF turns this display on or off. Turning feedback ON sets n to 1. Setting feedback to zero is equivalent to turning it OFF.

SET FEEDBACK OFF also turns off the statement confirmation messages such as 'Table created' and 'PL/SQL procedure successfully completed' that are displayed after successful SQL or PL/SQL statements.

---

## SET FLAGGER {OFF | ENTRY | INTERMED\[IATE\] | FULL}

Checks to make sure that SQL statements conform to the ANSI/ISO SQL92 standard.

If any non-standard constructs are found, the Oracle Database Server flags them as errors and displays the violating syntax. This is the equivalent of the SQL language ALTER SESSION SET FLAGGER command.

You may execute SET FLAGGER even if you are not connected to a database. FIPS flagging will remain in effect across SQL\*Plus sessions until a SET FLAGGER OFF (or ALTER SESSION SET FLAGGER = OFF) command is successful or you exit SQL\*Plus.

When FIPS flagging is enabled, SQL\*Plus displays a warning for the CONNECT, DISCONNECT, and ALTER SESSION SET FLAGGER commands, even if they are successful.

---

## SET FLU\[SH\] {ON | OFF}

Controls when output is sent to the user's display device. OFF enables the operating system to buffer output. ON disables buffering. FLUSH only affects display output, it does not affect spooled output.

Use OFF only when you run a script non-interactively (that is, when you do not need to see output and/or prompts until the script finishes running). The use of FLUSH OFF may improve performance by reducing the amount of program I/O.

---

## SET HEA\[DING\] {ON | OFF}

Controls printing of column headings in reports.

ON prints column headings in reports; OFF suppresses column headings.

The SET HEADING OFF command does not affect the column width displayed, it only suppresses the printing of the column header itself.

Example

To suppress the display of column headings in a report, enter

```
SET HEADING OFF
```

If you then run a SQL SELECT command

```
SELECT LAST_NAME, SALARY
FROM EMP_DETAILS_VIEW
WHERE JOB_ID = 'AC_MGR';
```

the following output results:

```
Higgins 12000
```

To turn the display of column headings back on, enter

```
SET HEADING ON
```

---

## SET HEADS\[EP\] { | c | ON | OFF}

Defines the character used as a line break in column headings.

The heading separator character cannot be alphanumeric or white space. You can use the heading separator character in the COLUMN command and in the old forms of BTITLE and TTITLE to divide a column heading or title onto more than one line. ON or OFF turns heading separation on or off. When heading separation is OFF, SQL\*Plus prints a heading separator character like any other character. ON changes the value of c back to the default "|".

---

## SET INSTANCE \[instance\_path | LOCAL\]

Changes the default instance for your session to the specified instance path.

Using the SET INSTANCE command does not connect to a database. The default instance is used for commands when no instance is specified. Any commands preceding the first use of SET INSTANCE communicate with the default instance.

To reset the instance to the default value for your operating system, you can either enter SET INSTANCE with no instance\_path or SET INSTANCE LOCAL.

Note, you can only change the instance when you are not currently connected to any instance. That is, you must first make sure that you have disconnected from the current instance, then set or change the instance, and reconnect to an instance in order for the new setting to be enabled.

This command may only be issued when Oracle Net is running. You can use any valid Oracle Net connect identifier as the specified instance path. See your operating system-specific Oracle Database documentation for a complete description of how your operating system specifies Oracle Net connect identifiers. The maximum length of the instance path is 64 characters.

Example

To set the default instance to "PROD1" enter

```
DISCONNECT
SET INSTANCE PROD1
```

To set the instance back to the default of local, enter

```
SET INSTANCE local
```

You must disconnect from any connected instances to change the instance.

---

## SET LIN\[ESIZE\] {80 | n}

Sets the total number of characters that SQL\*Plus displays on one line before beginning a new line.

It also controls the position of centered and right-aligned text in TTITLE, BTITLE, REPHEADER and REPFOOTER. Changing the linesize setting can affect text wrapping in output from the DESCRIBE command. DESCRIBE output columns are typically allocated a proportion of the linesize. Decreasing or increasing the linesize may give unexpected text wrapping in your display. You can define LINESIZE as a value from 1 to a maximum that is system dependent.

---

## SET LOBOF\[FSET\] {1 | n}

Sets the starting position from which BLOB, BFILE, CLOB and NCLOB data is retrieved and displayed.

Example

To set the starting position from which a CLOB column's data is retrieved to the 22nd position, enter

```
SET LOBOFFSET 22
```

The CLOB data will wrap on your screen; SQL\*Plus will not truncate until the 23rd character.

---

## SET LOGSOURCE \[pathname\]

Specifies the location from which archive logs are retrieved during recovery.

The default value is set by the LOG\_ARCHIVE\_DEST initialization parameter in the Oracle Database initialization file, init.ora. Using the SET LOGSOURCE command without a pathname restores the default location.

Example

To set the default location of log files for recovery to the directory "/usr/oracle10/dbs/arch" enter

```
SET LOGSOURCE "/usr/oracle10/dbs/arch"
RECOVER DATABASE
```

---

## SET LONG {80 | n}

Sets maximum width (in bytes) for displaying BLOB, BFILE, CLOB, LONG, NCLOB and XMLType values; and for copying LONG values.

Querying LONG columns requires enough local memory to store the amount of data specified by SET LONG, irrespective of the value of the SET LONGCHUNKSIZE command. This requirement does not apply when querying LOBs.

It is recommended that you do not create tables with LONG columns. LONG columns are supported only for backward compatibility. Use LOB columns (BLOB, BFILE, CLOB, NCLOB) instead. LOB columns have fewer restrictions than LONG columns and are still being enhanced.

The maximum value of n is 2,000,000,000 bytes. It is important to check that the memory required by your SET LONG command is available on your machine, for example:

```
SET LONG 2000000000
```

assumes that available RAM (random access memory) on the machine exceeds 2 gigabytes.

Example

To set the maximum number of bytes to fetch for displaying and copying LONG values, to 500, enter

```
SET LONG 500
```

The LONG data will wrap on your screen; SQL\*Plus will not truncate until the 501st byte. The default for LONG is 80 bytes.

---

## SET LONGC\[HUNKSIZE\] {80 | n}

Sets the size (in bytes) of the increments SQL\*Plus uses to retrieve a BLOB, BFILE, CLOB, LONG, NCLOB or XMLType value.

LONGCHUNKSIZE is not used for object relational queries such as CLOB, or NCLOB.

Example

To set the size of the increments in which SQL\*Plus retrieves LONG values to 100 bytes, enter

```
SET LONGCHUNKSIZE 100
```

The LONG data will be retrieved in increments of 100 bytes until the entire value is retrieved or the value of SET LONG is reached, whichever is the smaller.

---

## SET MARK\[UP\] HTML \[ON | OFF\] \[HEAD text\] \[BODY text\] \[TABLE text\] \[ENTMAP {ON | OFF}\] \[SPOOL {ON | OFF}\] \[PRE\[FORMAT\] {ON | OFF}\]

Outputs HTML marked up text.

To be effective, SET MARKUP commands that change values in dynamic report output must occur before statements that produce query output. The first statement that produces query output triggers the output of information affected by SET MARKUP such as HEAD and TABLE settings. Subsequent SET MARKUP commands have no effect on the information already sent to the report.

SET MARKUP only specifies that SQL\*Plus output will be HTML encoded. You must use SET MARKUP HTML ON SPOOL ON and the SQL\*Plus SPOOL command to create and name a spool file, and to begin writing HMTL output to it. SET MARKUP has the same options and behavior as SQLPLUS -MARKUP.

See [MARKUP Options](ch_three.md) for detailed information. For examples of usage, see [SET MARK\[UP\] HTML \[ON | OFF\] \[HEAD text\] \[BODY text\] \[TABLE text\] \[ENTMAP {ON | OFF}\] \[SPOOL {ON | OFF}\] \[PRE\[FORMAT\] {ON | OFF}\]](#i2699173), and [Generating HTML Reports from SQL\*Plus](ch_seven.md).

Use the SHOW MARKUP command to view the status of MARKUP options.

Example

The following is a script which uses the SET MARKUP HTML command to enable HTML marked up text to be spooled to a specified file:

Note:

The SET MARKUP example command is laid out for readability using line continuation characters "–" and spacing. Command options are concatenated in normal entry.

Use your favorite text editor to enter the commands necessary to set up the HTML options and the query you want for your report.

```
SET MARKUP HTML ON SPOOL ON HEAD "<TITLE>SQL*Plus Report</title> -
<STYLE TYPE='TEXT/CSS'><!--BODY {background: ffffc6} --></STYLE>"
SET ECHO OFF
SPOOL employee.htm
SELECT FIRST_NAME, LAST_NAME, SALARY
FROM EMP_DETAILS_VIEW
WHERE SALARY>12000;
SPOOL OFF
SET MARKUP HTML OFF
SET ECHO ON
```

As this script contains SQL\*Plus commands, do not attempt to run it with / (slash) from the buffer because it will fail. Save the script in your text editor and use START to execute it:

```
START employee.sql
```

As well as writing the HTML spool file, employee.htm, the output is also displayed on screen because SET TERMOUT defaults to ON. You can view the spool file, employee.htm, in your web browser. It should appear something like the following:

![markup](img/markup.gif)

> The markup.gif image shows the employee.html spool file displayed in a web browser. Employee.html is the output file resulting from the example of a Markup interactive session. It is described in the text prior to this image The heading row of the three column HTML table contains the labels:
>
> - FIRST\_NAME
> - LAST\_NAME
> - SALARY
>
> There are 6 more rows containing the query results. The HTML table is followed by the SQL\*Plus statement, 6 rows selected.
  
  

---

## SET NEWP\[AGE\] {1 | n | NONE}

Sets the number of blank lines to be printed from the top of each page to the top title. A value of zero places a formfeed at the beginning of each page (including the first page) and clears the screen on most terminals. If you set NEWPAGE to NONE, SQL\*Plus does not print a blank line or formfeed between the report pages.

---

## SET NULL text

Sets the text displayed whenever a null value occurs in the result of a SQL SELECT command.

Use the NULL clause of the COLUMN command to override the setting of the NULL variable for a given column. The default output for a null is blank ("").

---

## SET NUMF\[ORMAT\] format

Sets the default format for displaying numbers. See the FORMAT clause of the [COLUMN](ch_twelve013.md) command for number format descriptions. Enter a number format for format. To use the default field width and formatting model specified by SET NUMWIDTH, enter

```
SET NUMFORMAT ""
```

---

## SET NUM\[WIDTH\] {10 | n}

Sets the default width for displaying numbers. See the FORMAT clause of the [COLUMN](ch_twelve013.md) command for number format descriptions.

COLUMN FORMAT settings take precedence over SET NUMFORMAT settings, which take precedence over SET NUMWIDTH settings.

---

## SET PAGES\[IZE\] {14 | n}

Sets the number of lines on each page of output. You can set PAGESIZE to zero to suppress all headings, page breaks, titles, the initial blank line, and other formatting information.

---

## SET PAU\[SE\] {ON | OFF | text}

Enables you to control scrolling of your terminal when running reports. You need to first, SET PAUSE text, and then SET PAUSE ON if you want text to appear each time SQL\*Plus pauses.

SET PAUSE ON pauses output at the beginning of each PAGESIZE number of lines of report output. Press Return to view more output. SET PAUSE text specifies the text to be displayed each time SQL\*Plus pauses. Multiple words in text must be enclosed in single quotes.

You can embed terminal-dependent escape sequences in the PAUSE command. These sequences allow you to create inverse video messages or other effects on terminals that support such characteristics.

---

## SET RECSEP {WR\[APPED\] | EA\[CH\] | OFF}

RECSEP tells SQL\*Plus where to make the record separation.

For example, if you set RECSEP to WRAPPED, SQL\*Plus prints a record separator only after wrapped lines. If you set RECSEP to EACH, SQL\*Plus prints a record separator following every row. If you set RECSEP to OFF, SQL\*Plus does not print a record separator.

---

## SET RECSEPCHAR { | c}

Defines the character to display or print to separate records.

A record separator consists of a single line of the RECSEPCHAR (record separating character) repeated LINESIZE times. The default is a single space.

---

## SET SERVEROUT\[PUT\] {ON | OFF} \[SIZE {n | UNL\[IMITED\]}\] \[FOR\[MAT\] {WRA\[PPED\] | WOR\[D\_WRAPPED\] | TRU\[NCATED\]}\]

Controls whether to display output (that is, DBMS\_OUTPUT.PUT\_LINE) of stored procedures or PL/SQL blocks in SQL\*Plus. The DBMS\_OUTPUT line length limit is 32767 bytes.

OFF suppresses the output of DBMS\_OUTPUT.PUT\_LINE. ON displays the output.

ON uses the SIZE and FORMAT of the previous SET SERVEROUTPUT ON SIZE n FORMAT f, or uses default values if no SET SERVEROUTPUT command was previously issued in the current connection.

SIZE sets the number of bytes of the output that can be buffered within the Oracle Database server. The default is UNLIMITED. n cannot be less than 2000 or greater than 1,000,000.

Resources are not pre-allocated when SERVEROUTPUT is set. As there is no performance penalty, use UNLIMITED unless you want to conserve physical memory.

Every server output line begins on a new output line.

When WRAPPED is enabled SQL\*Plus wraps the server output within the line size specified by SET LINESIZE, beginning new lines when required.

When WORD\_WRAPPED is enabled, each line of server output is wrapped within the line size specified by SET LINESIZE. Lines are broken on word boundaries. SQL\*Plus left justifies each line, skipping all leading whitespace.

When TRUNCATED is enabled, each line of server output is truncated to the line size specified by SET LINESIZE.

For detailed information about using UTL\_FILE and associated utilities, see the [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm).

For more information on DBMS\_OUTPUT.PUT\_LINE, see your [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm).

Example

To enable text display in a PL/SQL block using DBMS\_OUTPUT.PUT\_LINE, enter

```
SET SERVEROUTPUT ON
```

The following example shows what happens when you execute an anonymous procedure with SET SERVEROUTPUT ON:

```
BEGIN
  DBMS_OUTPUT.PUT_LINE('Task is complete');
END;
/
```

```
Task is complete.
PL/SQL procedure successfully completed.
```

The following example shows what happens when you create a trigger with SET SERVEROUTPUT ON:

```
CREATE TABLE SERVER_TAB (Letter CHAR);
CREATE TRIGGER SERVER_TRIG BEFORE INSERT OR UPDATE -
OR DELETE
ON SERVER_TAB
BEGIN
DBMS_OUTPUT.PUT_LINE('Task is complete.');
END;
/
```

```
Trigger Created.
```

```
INSERT INTO SERVER_TAB VALUES ('M');
DROP TABLE SERVER_TAB; 
/* Remove SERVER_TAB from database */
```

```
Task is complete.
1 row created.
```

To set the output to WORD\_WRAPPED, enter

```
SET SERVEROUTPUT ON FORMAT WORD_WRAPPED
SET LINESIZE 20
BEGIN
  DBMS_OUTPUT.PUT_LINE('If there is nothing left to do');
  DBMS_OUTPUT.PUT_LINE('shall we continue with plan B?');
END;
/
```

```
If there is nothing
left to do
shall we continue
with plan B?
```

To set the output to TRUNCATED, enter

```
SET SERVEROUTPUT ON FORMAT TRUNCATED
SET LINESIZE 20
BEGIN
  DBMS_OUTPUT.PUT_LINE('If there is nothing left to do');
  DBMS_OUTPUT.PUT_LINE('shall we continue with plan B?');
END;
/
```

```
If there is nothing
shall we continue wi
```

---

## SET SHIFT\[INOUT\] {VIS\[IBLE\] | INV\[ISIBLE\]}

Enables correct alignment for terminals that display shift characters. The SET SHIFTINOUT command is useful for terminals which display shift characters together with data (for example, IBM 3270 terminals). You can only use this command with shift sensitive character sets (for example, JA16DBCS).

Use VISIBLE for terminals that display shift characters as a visible character (for example, a space or a colon). INVISIBLE is the opposite and does not display any shift characters.

Example

To enable the display of shift characters on a terminal that supports them, enter

```
SET SHIFTINOUT VISIBLE
SELECT LAST_NAME, JOB_ID FROM EMP_DETAILS_VIEW
WHERE SALARY > 12000;
```

```
LAST_NAME      JOB_ID
---------- ----------
:JJOO:       :AABBCC:
:AA:abc       :DDEE:e
```

where ":" = visible shift character uppercase represents multibyte characters

lowercase represents singlebyte characters

---

## SET SHOW\[MODE\] {ON | OFF}

Controls whether SQL\*Plus lists the old and new settings of a SQL\*Plus system variable when you change the setting with SET. ON lists the settings; OFF suppresses the listing. SHOWMODE ON has the same behavior as the obsolete SHOWMODE BOTH.

---

## SET SQLBL\[ANKLINES\] {ON | OFF}

Controls whether SQL\*Plus puts blank lines within a SQL command or script. ON interprets blank lines and new lines as part of a SQL command or script. OFF, the default value, does not allow blank lines or new lines in a SQL command or script or script.

Enter the BLOCKTERMINATOR to stop SQL command entry without running the SQL command. Enter the SQLTERMINATOR character to stop SQL command entry and run the SQL statement.

Example

To allow blank lines in a SQL statement, enter

```
SET SQLBLANKLINES ON
REM Using the SQLTERMINATOR (default is ";") 
REM Could have used the BLOCKTERMINATOR (default is ".")
SELECT *

FROM

DUAL

;
```

The following output results:

```
D
-
X
```

---

## SET SQLC\[ASE\] {MIX\[ED\] | LO\[WER\] | UP\[PER\]}

Converts the case of SQL commands and PL/SQL blocks just prior to execution.

SQL\*Plus converts all text within the command, including quoted literals and identifiers, to uppercase if SQLCASE equals UPPER, to lowercase if SQLCASE equals LOWER, and makes no changes if SQLCASE equals MIXED.

SQLCASE does not change the SQL buffer itself.

---

## SET SQLCO\[NTINUE\] {> | text}

Sets the character sequence SQL\*Plus displays as a prompt after you continue a SQL\*Plus command on an additional line using a hyphen (–).

Example

To set the SQL\*Plus command continuation prompt to an exclamation point followed by a space, enter

```
SET SQLCONTINUE '! '
```

SQL\*Plus will prompt for continuation as follows:

```
TTITLE 'MONTHLY INCOME' -
! RIGHT SQL.PNO SKIP 2 -
! CENTER 'PC DIVISION'
```

The default continuation prompt is "> ".

---

## SET SQLN\[UMBER\] {ON | OFF}

Sets the prompt for the second and subsequent lines of a SQL command or PL/SQL block. ON sets the prompt to be the line number. OFF sets the prompt to the value of SQLPROMPT.

---

## SET SQLPLUSCOMPAT\[IBILITY\] {x.y\[.z\]}

Sets the behavior to that of the release or version specified by x.y\[.z\].

Where x is the version number, y is the release number, and z is the update number. For example, 8.1.7, 9.0.1 or 10.2. The features affected by SQLPLUSCOMPATIBILITY are tabulated in the SQL\*Plus Compatibility Matrix shown. You can also set the value of SQLPLUSCOMPATIBILITY using the -C\[OMPATIBILITY\] argument of the SQLPLUS command when starting SQL\*Plus from the command line.

The default setting for SQLPLUSCOMPATIBILITY is the value of the SQL\*Plus client.

It is recommended that you add SET SQLPLUSCOMPATIBILITY 11.2 to your scripts to maximize their compatibility with future versions of SQL\*Plus.

### SQL\*Plus Compatibility Matrix

The SQL\*Plus Compatibility Matrix tabulates behavior affected by each SQL\*Plus compatibility setting. SQL\*Plus compatibility modes can be set in three ways:

- You can include a SET SQLPLUSCOMPATIBILITY command in your site or user profile. On installation, there is no SET SQLPLUSCOMPATIBILITY setting in glogin.sql. Therefore the default compatibility is 11.2.
- You can use the SQLPLUS -C\[OMPATIBILITY\] {x.y\[.z\]} command argument at startup to set the compatibility mode of that session.
- You can use the SET SQLPLUSCOMPATIBILITY {x.y\[.z\]} command during a session to set the SQL\*Plus behavior you want for that session.

The following table shows the release of SQL\*Plus which introduced the behavior change, and hence the minimum value of SQLPLUSCOMPATIBILITY to obtain that behavior. For example, to obtain the earlier behavior of the VARIABLE command, you must either use a version of SQL\*Plus earlier than 9.0.1, or you must use a SQLPLUSCOMPATIBILITY value of less than 9.0.1. The lowest value that can be set for SQLPLUSCOMPATIBILITY is 7.3.4

Table 12-6 Compatibility Matrix

| Value | Consequence | When available |
| --- | --- | --- |
| \>=10.1 | SHOW ERRORS sorts PL/SQL error messages using new columns only available in Oracle Database 10g. | 10.1 |
| \>=10.1 | SPOOL Options CREATE, REPLACE, SAVE were added which may affect filename parsing on some platforms. | 10.1 |
| \>=10.1 | SET SQLPROMPT | 10.1 |
| \>=10.1 | Whitespace characters are allowed in Windows file names that are enclosed in quotes. Some other special punctuation characters are now disallowed in Windows. | 10.1 |
| \>=10.1 | Glogin/login files are called for each reconnect. | 10.1 |
| <10.1 | Uses the obsolete DOC> prompt when echoing /\* comments. | 10.1 |
| \>= 9.2 | A wide column defined FOLD\_AFTER may be displayed at the start of a new line. Otherwise it is incorrectly put at the end of the preceding line with a smaller width than expected. | 9.2. |
| \>= 9.0 | Whitespace before a slash ("/") in a SQL statement is ignored and the slash is taken to mean execute the statement. Otherwise the slash is treated as part of the statement, for example, as a division sign. | 9.0.1.4. |
| \>= 9.0 | The length specified for NCHAR and NVARCHAR2 types is characters. Otherwise the length may represent bytes or characters depending on the character set. | 9.0.1 |

---

## SET SQLPRE\[FIX\] {# | c}

Sets the SQL\*Plus prefix character. While you are entering a SQL command or PL/SQL block, you can enter a SQL\*Plus command on a separate line, prefixed by the SQL\*Plus prefix character. SQL\*Plus will execute the command immediately without affecting the SQL command or PL/SQL block that you are entering. The prefix character must be a non-alphanumeric character.

---

## SET SQLP\[ROMPT\] {SQL> | text}

Sets the SQL\*Plus command prompt. SET SQLPROMPT substitute variables dynamically. This enables the inclusion of runtime variables such as the current connection identifier. Substitution variables used in SQLPROMPT do not have to be prefixed with '&', and they can be used and accessed like any other substitution variable. Variable substitution is not attempted for the default prompt, "SQL> ".

Variable substitution occurs each time SQLPROMPT is SET. If SQLPROMPT is included in glogin.sql, then substitution variables in SQLPROMPT are refreshed with each login or connect.

Example

To change your SQL\*Plus prompt to display your connection identifier, enter:

```
SET SQLPROMPT "_CONNECT_IDENTIFIER > "
```

To set the SQL\*Plus command prompt to show the current user, enter

```
SET SQLPROMPT "_USER > "
```

To change your SQL\*Plus prompt to display your the current date, the current user and the users privilege level, enter:

```
SET SQLPROMPT "_DATE _USER _PRIVILEGE> "
```

To change your SQL\*Plus prompt to display a variable you have defined, enter:

```
DEFINE mycon = Prod1
SET SQLPROMPT "mycon> "
```

```
Prod1>
```

Text in nested quotes is not parsed for substitution. To have a SQL\*Plus prompt of your username, followed by "@", and then your connection identifier, enter:

```
SET SQLPROMPT "_USER'@'_CONNECT_IDENTIFIER > "
```

---

## SET SQLT\[ERMINATOR\] {; | c | ON | OFF}

Sets the character used to end script or data entry for PL/SQL blocks or SQL statements, to execute the script, and to load it into the buffer.

It cannot be an alphanumeric character or a whitespace. OFF means that SQL\*Plus recognizes no command terminator; you terminate a SQL command by entering an empty line or a slash (/). If SQLBLANKLINES is set ON, you must use the BLOCKTERMINATOR to terminate a SQL command. ON resets the terminator to the default semicolon (;).

---

## SET SUF\[FIX\] {SQL | text}

Sets the default file extension that SQL\*Plus uses in commands that refer to scripts. SUFFIX does not control extensions for spool files.

Example

To change the default command-file extension from the default,.SQL to.TXT, enter

```
SET SUFFIX TXT
```

If you then enter

```
GET EXAMPLE
```

SQL\*Plus will look for a file named EXAMPLE.TXT instead of EXAMPLE.SQL.

---

## SET TAB {ON | OFF}

Determines how SQL\*Plus formats white space in terminal output. OFF uses spaces to format white space in the output. ON uses the TAB character. TAB settings are every eight characters. The default value for TAB is system dependent.

---

## SET TERM\[OUT\] {ON | OFF}

Controls the display of output generated by commands in a script that is executed with @, @@ or START. OFF suppresses the display so that you can spool output to a file without displaying the output on screen. ON displays the output on screen. TERMOUT OFF does not affect output from commands you enter interactively or redirect to SQL\*Plus from the operating system.

---

## SET TI\[ME\] {ON | OFF}

Controls the display of the current time. ON displays the current time before each command prompt. OFF suppresses the time display.

---

## SET TIMI\[NG\] {ON | OFF}

Controls the display of timing statistics.

ON displays timing statistics on each SQL command or PL/SQL block run. OFF suppresses timing of each command.

See [TIMING](ch_twelve047.md) for information on timing multiple commands.

Example

The format of timing statistics is dependent on the operating system. In Linux and Windows, the timing statistics are in 24 hour format displaying hours, minutes, seconds and hundredths of seconds

```
SET SUFFIX TXT
```

If you enter

```
GET EXAMPLE
```

SQL\*Plus displays output like

```
GET EXAMPLE
```

---

## SET TRIM\[OUT\] {ON | OFF}

Determines whether SQL\*Plus puts trailing blanks at the end of each displayed line. ON removes blanks at the end of each line, improving performance especially when you access SQL\*Plus from a slow communications device. OFF enables SQL\*Plus to display trailing blanks. TRIMOUT ON does not affect spooled output.

---

## SET TRIMS\[POOL\] {ON | OFF}

Determines whether SQL\*Plus puts trailing blanks at the end of each spooled line. ON removes blanks at the end of each line. OFF enables SQL\*Plus to include trailing blanks. TRIMSPOOL ON does not affect terminal output.

---

## SET UND\[ERLINE\] {- | c | ON | OFF}

Sets the character used to underline column headings in reports. The underline character cannot be an alphanumeric character or a white space. ON or OFF turns underlining on or off. ON changes the value of c back to the default "-".

---

## SET VER\[IFY\] {ON | OFF}

Controls whether to list the text of a SQL statement or PL/SQL command before and after replacing substitution variables with values. ON lists the text; OFF suppresses the listing.

---

## SET WRA\[P\] {ON | OFF}

Controls whether to truncate the display of a selected row if it is too long for the current line width. OFF truncates the selected row; ON enables the selected row to wrap to the next line.

Use the WRAPPED and TRUNCATED clauses of the COLUMN command to override the setting of WRAP for specific columns.

---

## SET XMLOPT\[IMIZATIONCHECK\] \[ON|OFF\]

Controls whether only XML queries and DML operations that are fully optimized are executed. ON prevents the execution of any XML query or DML operation that cannot be fully optimized and writes the reason in the trace file. OFF does not prevent the execution of such queries and operations. OFF is the default.

SET XMLOPT\[IMIZATIONCHECK\] ON is only to assist during development and debugging an XML query or DML operation.

---

## SET XQUERY BASEURI {text}

Specifies the base URI used to resolve relative URIs in functions. It enables the prefix of the file accessed by an XQuery to be changed.

To unset the BASEURI, set an empty string, for example:

```
SET XQUERY BASEURI ''
```

Take care to enter valid values as values are checked only when an XQUERY command is issued.

Example

```
SET XQUERY BASEURI '/public/scott'
XQUERY for $i in doc("foo.xml") return $i
/
```

This is equivalent to:

```
XQuery declare base-uri "/public/hr"; 
for $i in doc("foo.xml") return $i
```

---

## SET XQUERY ORDERING {UNORDERED | ORDERED | DEFAULT}

Sets the ordering of output from an XQuery. There are three values:

UNORDERED specifies that results are sorted in the order they are retrieved from the database.

ORDERED specifies that results are sorted as defined by the XQuery.

DEFAULT specifies the database default. In Oracle Database 10g the default is UNORDERED.

When SET XQUERY ORDERING is not set, the default is DEFAULT (UNORDERED).

Example

```
SET XQUERY ORDERING ORDERED
XQUERY for $i in doc("foo.xml") return $i
/
```

This is equivalent to:

```
XQuery declare ordering ordered; 
for $i in doc("foo.xml") return $i
/
```

---

## SET XQUERY NODE {BYVALUE | BYREFERENCE | DEFAULT}

Sets the node identity preservation mode. The preservation mode applies to all expressions that either create a new node (such as element constructors) or return an item or sequence containing nodes (such as path expressions). There are three values:

BYVALUE specifies that the node identity need not be preserved. This means that any node operation such as creation, or that is returned as a result of an expression is deep copied and loses its context from the original tree. Subsequent operations on this node that test for node identity, parent or sibling axes or ordering will be undefined.

BYREFERENCE specifies that node identities are to be preserved. Subsequent operations on this node preserve the node's context and definition.

DEFAULT specifies the database default. In Oracle Database 10g the default is BYVALUE.

When SET XQUERY NODE is not set, the default is DEFAULT (BYVALUE).

Example

```
SET XQUERY NODE BYREFERENCE
XQUERY for $i in doc("foo.xml") return $i
/
```

This is equivalent to:

```
XQuery declare node byreference; 
for $i in doc("foo.xml") return $i
/
```

---

## SET XQUERY CONTEXT {text}

Specifies an XQuery context item expression. A context item expression evaluates to the context item, which may be either a node (as in the expression fn:doc("bib.xml")//book\[fn:count(./author)>1\]), or an atomic value (as in the expression (1 to 100)\[. mod 5 eq 0\]).

To unset the XQUERY CONTEXT, set an empty string, for example:

```
SET XQUERY CONTEXT ''
```

Take care to enter valid values as values are checked only when an XQUERY command is issued.

Example

```
SET XQUERY CONTEXT 'doc("foo.xml")'
XQUERY for $i in /a return $i
/
```

This is equivalent to:

```
XQuery for $i in /a return $i 
passing XMLQuery("doc('foo.xml')")
/
```