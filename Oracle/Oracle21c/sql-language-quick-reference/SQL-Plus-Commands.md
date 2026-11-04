---
title: SQL Language Quick Reference
book: SQL Language Quick Reference
doc_id: F31302-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlqr/SQL-Plus-Commands.html
tags:
  - oracle
  - 21c
  - sql-language-quick-reference
---

This appendix presents many of the SQL\*Plus commands.

This appendix includes the following section:

- SQL\*Plus Commands

### SQL\*Plus Commands

SQL\*Plus is a command-line tool that provides access to the Oracle RDBMS. SQL\*Plus enables you to:

- Enter SQL\*Plus commands to configure the SQL\*Plus environment
- Startup and shutdown an Oracle database
- Connect to an Oracle database
- Enter and execute SQL commands and PL/SQL blocks
- Format and print query results

SQL\*Plus is available on several platforms.

The commands shown in Table A-1 are SQL\*Plus commands available in the command-line interface. Not all commands or command parameters are shown.

See Also:

- [SQL\*Plus Quick Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQPQR)
- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQPUG)

Table A-1 Basic SQL\*Plus Commands

| Database Operation | SQL\*Plus Command |
| --- | --- |
| Log in to SQL\*Plus | ``` SQLPLUS [   [{username[/password][@connect_identifier] \| / }   [AS {SYSASM\|SYSBACKUP\|SYSDBA\|SYSDG\|SYSOPER\|SYSKM}]   [edition=value]]         \| /NOLOG         ] ``` |
| List help topics available in SQL\*Plus | ``` HELP [ INDEX \| topic ] ``` |
| Execute host commands | ``` HOST [ command ] ``` |
| Show SQL\*Plus system variables or environment settings | ``` SHOW { ALL \| ERRORS \| USER \| system_variable   [, system_variable] ...} ``` |
| Alter SQL\*Plus system variables or environment settings | ``` SET system_variable value ``` |
| Start up a database | ``` STARTUP { db_options \| cdb_options \| upgrade_options } ```  Where `db_options` has the following syntax:  ``` [FORCE] [RESTRICT] [PFILE=filename] [QUIET] [ MOUNT [dbname] \| [ OPEN [open_db_options] [dbname] ] \| NOMOUNT ] ```  Where `open_db_options` has the following syntax:  ``` READ {ONLY \| WRITE [RECOVER]} \| RECOVER ```  Where `cdb_options` has the following syntax:  ``` root_connection_options \| pdb_connection_options ```  Where `root_connection_options` has the following syntax:  ``` PLUGGABLE DATABASE pdbname [FORCE] \| [RESTRICT] [ OPEN {open_pdb_options} ] ```  Where `pdb_connection_options` has the following syntax:  ``` [FORCE] \| [RESTRICT] [ OPEN {open_pdb_options} ] ```  Where `open_pdb_options` has the following syntax:  ``` READ WRITE \| READ ONLY ```  Where `upgrade_options` has the following syntax:  ``` [PFILE=filename] {UPGRADE \| DOWNGRADE} [QUIET] ``` |
| Connect to a database | ``` CONNECT [{username[/password] [@connect_identifier]          \| /          \| proxy_user [ username ] [/password]          [@connect_identifier]}          [AS {SYSASM\|SYSBACKUP\|SYSDBA\|SYSDG\|SYSOPER              \|SYSKM}]          [edition=value]         ] ```  Note: The square brackets shown in boldface type are part of the syntax and do not imply optionality. |
| List column definitions for a table, view, or synonym, or specifications for a function or procedure | ``` DESCRIBE [ schema. ] object ``` |
| Edit contents of the SQL buffer or a file | ``` EDIT [ filename [ .ext ] ] ``` |
| Get a file and load its contents into the SQL buffer | ``` GET filename [ .ext ] [ LIST \| NOLLIST ] ``` |
| Save contents of the SQL buffer to a file | ``` SAVE filename [ .ext ] [ CREATE \| REPLACE \| APPEND ] ``` |
| List contents of the SQL buffer | ``` LIST [ n \| n m \| n LAST ] ``` |
| Delete contents of the SQL buffer | ``` DEL [ n \| n m \| n LAST ] ``` |
| Add new lines following current line in the SQL buffer | ``` INPUT [ text ] ``` |
| Append text to end of current line in the SQL buffer | ``` APPEND text ``` |
| Find and replace first occurrence of a text string in current line of the SQL buffer | ``` CHANGE sepchar old [ sepchar [ new [ sepchar ] ] ] ```  sepchar can be any nonalphanumeric ASCII character such as "/" or "!" |
| Capture query results in a file and, optionally, send contents of file to default printer | ``` SPOOL [ filename[ .ext ]         [ CREATE \| REPLACE \| APPEND ] \| OFF \| OUT ] ``` |
| Run SQL\*Plus statements stored in a file | ``` @ { url \| filename [ .ext ] } [ arg ... ]START { url \| filename [ .ext ] } [ arg ... ] ```  ext can be omitted if the filename extension is.sql |
| Execute commands stored in the SQL buffer | ``` / ``` |
| List and execute commands stored in the SQL buffer | ``` RUN ``` |
| Execute a single PL/SQL statement or run a stored procedure | ``` EXECUTE statement ``` |
| Disconnect from a database | ``` DISCONNECT ``` |
| Shut down a database | ``` SHUTDOWN   [ ABORT \| IMMEDIATE \| NORMAL \| TRANSACTIONAL [LOCAL] ] ``` |
| Log out of SQL\*Plus | ``` { EXIT \| QUIT }  [ SUCCESS \| FAILURE \| WARNING \| n \| variable \| :BindVariable ]  [ COMMIT \| ROLLBACK ] ``` |