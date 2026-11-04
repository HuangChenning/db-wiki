---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SQL-Plus-command-summary.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

| Command | Description |
| --- | --- |
| ``` @ (at sign) ``` | Runs SQL\*Plus statements in the specified script. The script can be called from the local file system or from a web server. |
| ``` @@ (double at sign) ``` | Runs a script. This command is similar to the @ (at sign) command It is useful for running nested scripts because it looks for the specified script in the same path as the calling script. |
| ``` / (slash) ``` | Executes the SQL command or PL/SQL block. |
| ``` ACCEPT ``` | Reads a line of input and stores it in a given substitution variable. |
| ``` APPEND ``` | Adds specified text to the end of the current line in the buffer. |
| ``` ARCHIVE LOG ``` | Displays information about redo log files. |
| ``` ATTRIBUTE ``` | Specifies display characteristics for a given attribute of an Object Type column, and lists the current display characteristics for a single attribute or all attributes. |
| ``` BREAK ``` | Specifies where and how formatting will change in a report, or lists the current break definition. |
| ``` BTITLE ``` | Places and formats a specified title at the bottom of each report page, or lists the current BTITLE definition. |
| ``` CHANGE ``` | Changes text on the current line in the buffer. |
| ``` CLEAR ``` | Resets or erases the current clause or setting for the specified option, such as BREAKS or COLUMNS. |
| ``` COLUMN ``` | Specifies display characteristics for a given column, or lists the current display characteristics for a single column or for all columns. |
| ``` COMPUTE ``` | Calculates and prints summary lines, using various standard computations, on subsets of selected rows, or lists all COMPUTE definitions. |
| ``` CONNECT ``` | Connects a given user to Oracle Database. |
| ``` COPY ``` | Copies results from a query to a table in the same or another database. |
| ``` DEFINE ``` | Specifies a substitution variable and assigns it a CHAR value, or lists the value and variable type of a single variable or all variables. |
| ``` DEL ``` | Deletes one more lines of the buffer. |
| ``` DESCRIBE ``` | Lists the column definitions for the specified table, view, or synonym or the specifications for the specified function procedure. |
| ``` DISCONNECT ``` | Commits pending changes to the database and logs the current user off Oracle Database, but does not exit SQL\*Plus. |
| ``` EDIT ``` | Invokes an operating system text editor on the contents of the specified file or on the contents of the buffer. |
| ``` EXECUTE ``` | Executes a single PL/SQL statement. |
| ``` EXIT ``` | Terminates SQL\*Plus and returns control to the operating system. |
| ``` GET ``` | Loads an operating system file into the buffer. |
| ``` HELP ``` | Accesses the SQL\*Plus command-line help system. |
| ``` HISTORY ``` | Recalls the history of commands, SQL\*Plus commands, and SQL or PL/SQL statements issued in the current SQL\*Plus session. |
| ``` HOST ``` | Executes an operating system command without leaving SQL\*Plus. |
| ``` INPUT ``` | Adds one or more new lines after the current line in the buffer. |
| ``` LIST ``` | Lists one or more lines of the buffer. |
| ``` PASSWORD ``` | Enables a password to be changed without echoing the password on an input device. |
| ``` PAUSE ``` | Displays the specified text, then waits for the user to press Return. |
| ``` PRINT ``` | Displays the current value of a bind variable. |
| ``` PROMPT ``` | Sends the specified message to the user's screen. |
| ``` EXIT ``` | Terminates SQL\*Plus and returns control to the operating system QUIT is identical to EXIT. |
| ``` RECOVER ``` | Performs media recovery on one or more tablespaces, one or more datafiles, or the entire database. |
| ``` REMARK ``` | Begins a comment in a script. |
| ``` REPFOOTER ``` | Places and formats a specified report footer at the bottom of each report, or lists the current REPFOOTER definition. |
| ``` REPHEADER ``` | Places and formats a specified report header at the top of each report, or lists the current REPHEADER definition. |
| ``` RUN ``` | Lists and runs the SQL command or PL/SQL block currently stored in the SQL buffer. |
| ``` SAVE ``` | Saves the contents of the buffer in an operating system file (a script). |
| ``` SET ``` | Sets a system variable to alter the SQL\*Plus environment for your current session. |
| ``` SHOW ``` | Shows the value of a SQL\*Plus system variable or the current SQL\*Plus environment. |
| ``` SHUTDOWN ``` | Shuts down a currently running Oracle Database instance. |
| ``` SPOOL ``` | Stores query results in an operating system file and, optionally, sends the file to a printer. |
| ``` START ``` | Runs the SQL statements in the specified script. The script can be called from a local file system or a web server in SQL\*Plus command-line. |
| ``` STARTUP ``` | Starts an Oracle Database instance and optionally mounts and opens a database. |
| ``` STORE ``` | Saves attributes of the current SQL\*Plus environment in an operating system script. |
| ``` TIMING ``` | Records timing data for an elapsed period of time, lists the current timer's title and timing data, or lists the number of active timers. |
| ``` TTITLE ``` | Places and formats a specified title at the top of each report page, or lists the current TTITLE definition. |
| ``` UNDEFINE ``` | Deletes one or more substitution variables that you defined either explicitly (with the DEFINE command) or implicitly (with an argument to the START command). |
| ``` VARIABLE ``` | Declares a bind variable that can be referenced in PL/SQL, or lists the current display characteristics for a single variable or all variables. |
| ``` WHENEVER OSERROR ``` | Exits SQL\*Plus if an operating system command generates an error. |
| ``` WHENEVER SQLERROR ``` | Exits SQL\*Plus if a SQL command or PL/SQL block generates an error. |
| ``` XQUERY ``` | Runs an XQuery 1.0 statement. |