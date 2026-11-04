---
title: "SQL*Plus Commands"
book: SQL Language Quick Reference
doc_id: E41085-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41085/sqlqraa001.htm
tags:
  - oracle
  - 11g
  - sql-language-quick-reference
---

SQL\*Plus is a command-line tool that provides access to the Oracle RDBMS. SQL\*Plus enables you to:

- Enter SQL\*Plus commands to configure the SQL\*Plus environment
- Startup and shutdown an Oracle database
- Connect to an Oracle database
- Enter and execute SQL commands and PL/SQL blocks
- Format and print query results

SQL\*Plus is available on several platforms.

The commands shown in Table A-1 are SQL\*Plus commands available in the command-line interface. Not all commands or command parameters are shown.

See Also:

- [SQL\*Plus Quick Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16605/toc.htm)
- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/toc.htm)

Table A-1 Basic SQL\*Plus Commands

| Database Operation | SQL\*Plus Command |
| --- | --- |
| Log in to SQL\*Plus | ``` SQLPLUS [           [{username [/password ][@connect_identifier ] \| / }           [AS {SYSOPER \| SYSDBA \| SYSASM}][edition=value ]]         \| /NOLOG         ] ``` |
| List help topics available in SQL\*Plus | ``` HELP [ INDEX \| topic ] ``` |
| Execute host commands | ``` HOST [ command ] ``` |
| Show SQL\*Plus system variables or environment settings | ``` SHOW { ALL \| ERRORS \| USER \| system_variable [, system_variable] ...} ``` |
| Alter SQL\*Plus system variables or environment settings | ``` SET system_variable value ``` |
| Start up a database | ``` STARTUP [ PFILE = filename ]   [ MOUNT [ dbname ] \| NOMOUNT ] ``` |
| Connect to a database | ``` CONNECT [{username [/password ] [@connect_identifier ] \| /          \| proxy_user  [  username  ]  [/password ] [@connect_identifier ]}          [AS {SYSOPER \| SYSDBA \| SYSASM}] [edition=value ]         ] ```  Note: Brackets in boldface are part of the syntax and do not imply optionality. |
| List column definitions for a table, view, or synonym, or specifications for a function or procedure | ``` DESCRIBE [ schema. ] object ``` |
| Edit contents of the SQL buffer or a file | ``` EDIT [ filename [ .ext ] ] ``` |
| Get a file and load its contents into the SQL buffer | ``` GET filename [ .ext ] [ LIST \| NOLLIST ] ``` |
| Save contents of the SQL buffer to a file | ``` SAVE filename [ .ext ] [ CREATE \| REPLACE \| APPEND ] ``` |
| List contents of the SQL buffer | ``` LIST [ n \| n m \| n LAST ] ``` |
| Delete contents of the SQL buffer | ``` DEL [ n \| n m \| n LAST ] ``` |
| Add new lines following current line in the SQL buffer | ``` INPUT [ text ] ``` |
| Append text to end of current line in the SQL buffer | ``` APPEND text ``` |
| Find and replace first occurrence of a text string in current line of the SQL buffer | ``` CHANGE sepchar old [ sepchar [ new [ sepchar ] ] ] ```       can be any nonalphanumeric ASCII character such as "/" or "!" |
| Capture query results in a file and, optionally, send contents of file to default printer | ``` SPOOL [ filename [ .ext ]  [ CREATE \| REPLACE \| APPEND \| OFF \| OUT ] ``` |
| Run SQL\*Plus statements stored in a file | ``` @ { url \| filename [ .ext ] } [ arg ... ]START { url \| filename [ .ext ] } [ arg ... ] ```       can be omitted if the filename extension is.sql |
| Execute commands stored in the SQL buffer | ``` / ``` |
| List and execute commands stored in the SQL buffer | ``` RUN ``` |
| Execute a single PL/SQL statement or run a stored procedure | ``` EXECUTE statement ``` |
| Disconnect from a database | ``` DISCONNECT ``` |
| Shut down a database | ``` SHUTDOWN [ ABORT \| IMMEDIATE \| NORMAL ] ``` |
| Log out of SQL\*Plus | ``` { EXIT \| QUIT }   [ SUCCESS \| FAILURE \| WARNING ]   [ COMMIT \| ROLLBACK ] ``` |