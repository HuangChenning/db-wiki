---
title: "SQL*Plus Command Summary"
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve001.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

| Command | Description |
| --- | --- |
| [@ (at sign)](ch_twelve002.md) | Runs SQL\*Plus statements in the specified script. The script can be called from the local file system or from a web server. |
| [@@ (double at sign)](ch_twelve003.md) | Runs a script. This command is similar to the @ (at sign) command It is useful for running nested scripts because it looks for the specified script in the same path as the calling script. |
| [/ (slash)](ch_twelve004.md) | Executes the SQL command or PL/SQL block. |
| [ACCEPT](ch_twelve005.md) | Reads a line of input and stores it in a given substitution variable. |
| [APPEND](ch_twelve006.md) | Adds specified text to the end of the current line in the buffer. |
| [ARCHIVE LOG](ch_twelve007.md) | Displays information about redo log files. |
| [ATTRIBUTE](ch_twelve008.md) | Specifies display characteristics for a given attribute of an Object Type column, and lists the current display characteristics for a single attribute or all attributes. |
| [BREAK](ch_twelve009.md) | Specifies where and how formatting will change in a report, or lists the current break definition. |
| [BTITLE](ch_twelve010.md) | Places and formats a specified title at the bottom of each report page, or lists the current BTITLE definition. |
| [CHANGE](ch_twelve011.md) | Changes text on the current line in the buffer. |
| [CLEAR](ch_twelve012.md) | Resets or erases the current clause or setting for the specified option, such as BREAKS or COLUMNS. |
| [COLUMN](ch_twelve013.md) | Specifies display characteristics for a given column, or lists the current display characteristics for a single column or for all columns. |
| [COMPUTE](ch_twelve014.md) | Calculates and prints summary lines, using various standard computations, on subsets of selected rows, or lists all COMPUTE definitions. |
| [CONNECT](ch_twelve015.md) | Connects a given user to Oracle Database. |
| [COPY](ch_twelve016.md) | Copies results from a query to a table in the same or another database. |
| [DEFINE](ch_twelve017.md) | Specifies a substitution variable and assigns it a CHAR value, or lists the value and variable type of a single variable or all variables. |
| [DEL](ch_twelve018.md) | Deletes one more lines of the buffer. |
| [DESCRIBE](ch_twelve019.md) | Lists the column definitions for the specified table, view, or synonym or the specifications for the specified function procedure. |
| [DISCONNECT](ch_twelve020.md) | Commits pending changes to the database and logs the current user off Oracle Database, but does not exit SQL\*Plus. |
| [EDIT](ch_twelve021.md) | Invokes an operating system text editor on the contents of the specified file or on the contents of the buffer. |
| [EXECUTE](ch_twelve022.md) | Executes a single PL/SQL statement. |
| [EXIT](ch_twelve023.md) | Terminates SQL\*Plus and returns control to the operating system. |
| [GET](ch_twelve024.md) | Loads an operating system file into the buffer. |
| [HELP](ch_twelve025.md) | Accesses the SQL\*Plus command-line help system. |
| [HOST](ch_twelve026.md) | Executes an operating system command without leaving SQL\*Plus. |
| [INPUT](ch_twelve027.md) | Adds one or more new lines after the current line in the buffer. |
| [LIST](ch_twelve028.md) | Lists one or more lines of the buffer. |
| [PASSWORD](ch_twelve029.md) | Enables a password to be changed without echoing the password on an input device. |
| [PAUSE](ch_twelve030.md) | Displays the specified text, then waits for the user to press Return. |
| [PRINT](ch_twelve031.md) | Displays the current value of a bind variable. |
| [PROMPT](ch_twelve032.md) | Sends the specified message to the user's screen. |
| [EXIT](ch_twelve023.md) | Terminates SQL\*Plus and returns control to the operating system QUIT is identical to EXIT. |
| [RECOVER](ch_twelve033.md) | Performs media recovery on one or more tablespaces, one or more datafiles, or the entire database. |
| [REMARK](ch_twelve034.md) | Begins a comment in a script. |
| [REPFOOTER](ch_twelve035.md) | Places and formats a specified report footer at the bottom of each report, or lists the current REPFOOTER definition. |
| [REPHEADER](ch_twelve036.md) | Places and formats a specified report header at the top of each report, or lists the current REPHEADER definition. |
| [RUN](ch_twelve037.md) | Lists and runs the SQL command or PL/SQL block currently stored in the SQL buffer. |
| [SAVE](ch_twelve038.md) | Saves the contents of the buffer in an operating system file (a script). |
| [SET](ch_twelve039.md) | Sets a system variable to alter the SQL\*Plus environment for your current session. |
| [SHOW](ch_twelve041.md) | Shows the value of a SQL\*Plus system variable or the current SQL\*Plus environment. |
| [SHUTDOWN](ch_twelve042.md) | Shuts down a currently running Oracle Database instance. |
| [SPOOL](ch_twelve043.md) | Stores query results in an operating system file and, optionally, sends the file to a printer. |
| [START](ch_twelve044.md) | Runs the SQL statements in the specified script. The script can be called from a local file system or a web server in SQL\*Plus command-line. |
| [STARTUP](ch_twelve045.md) | Starts an Oracle Database instance and optionally mounts and opens a database. |
| [STORE](ch_twelve046.md) | Saves attributes of the current SQL\*Plus environment in an operating system script. |
| [TIMING](ch_twelve047.md) | Records timing data for an elapsed period of time, lists the current timer's title and timing data, or lists the number of active timers. |
| [TTITLE](ch_twelve048.md) | Places and formats a specified title at the top of each report page, or lists the current TTITLE definition. |
| [UNDEFINE](ch_twelve049.md) | Deletes one or more substitution variables that you defined either explicitly (with the DEFINE command) or implicitly (with an argument to the START command). |
| [VARIABLE](ch_twelve050.md) | Declares a bind variable that can be referenced in PL/SQL. |
| [WHENEVER OSERROR](ch_twelve051.md) | Exits SQL\*Plus if an operating system command generates an error. |
| [WHENEVER SQLERROR](ch_twelve052.md) | Exits SQL\*Plus if a SQL command or PL/SQL block generates an error. |
| [XQUERY](ch_twelve053.md) | Runs an XQuery 1.0 statement. |