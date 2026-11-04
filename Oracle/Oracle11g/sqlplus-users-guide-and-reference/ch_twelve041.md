---
title: SHOW
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve041.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

SHO\[W\] option

where option represents one of the following terms or clauses:

system\_variable ALL BTI\[TLE\]ERR\[ORS\] \[ { FUNCTION | PROCEDURE | PACKAGE | PACKAGE BODY | TRIGGER | VIEW | TYPE | TYPE BODY | DIMENSION | JAVA CLASS } \[schema.\]name\] LNO PARAMETERS \[parameter\_name\] PNO RECYC\[LEBIN\] \[original\_name\] REL\[EASE\] REPF\[OOTER\] REPH\[EADER\] SGA SPOO\[L\] SPPARAMETERS \[parameter\_name SQLCODE TTI\[TLE\] USER XQUERY

Shows the value of a SQL\*Plus system variable or the current SQL\*Plus environment. SHOW SGA requires a DBA privileged login.

Terms

system\_variable

Represents any system variable set by the SET command.

ALL

Lists the settings of all SHOW options, except ERRORS and SGA, in alphabetical order.

BTI\[TLE\]

Shows the current BTITLE definition.

ERR\[ORS\] \[{FUNCTION | PROCEDURE | PACKAGE | PACKAGE BODY | TRIGGER | VIEW | TYPE | TYPE BODY | DIMENSION | JAVA CLASS} \[schema.\]name\]

Shows the compilation errors of a stored procedure (includes stored functions, procedures, and packages). After you use the CREATE command to create a stored procedure, a message is displayed if the stored procedure has any compilation errors. To see the errors, you use SHOW ERRORS.

When you specify SHOW ERRORS with no arguments, SQL\*Plus shows compilation errors for the most recently created or altered stored procedure. When you specify the type (function, procedure, package, package body, trigger, view, type, type body, dimension, or java class) and the name of the PL/SQL stored procedure, SQL\*Plus shows errors for that stored procedure. For more information on compilation errors, see your PL/SQL User's Guide and Reference.

schema contains the named object. If you omit schema, SHOW ERRORS assumes the object is located in your current schema.

SHOW ERRORS output displays the line and column number of the error (LINE/COL) as well as the error itself (ERROR). LINE/COL and ERROR have default widths of 8 and 65, respectively. You can use the COLUMN command to alter the default widths.

LNO

Shows the current line number (the position in the current page of the display and/or spooled output).

PARAMETERS \[parameter\_name\]

Displays the current values for one or more initialization parameters. You can use a string after the command to see a subset of parameters whose names include that string. For example, if you enter:

```
SHOW PARAMETERS COUNT
```

```
NAME                              TYPE     VALUE  
------------------------------    -----    -----  
db_file_multiblock_read_count     integer  12
spin_count                        integer  0
```

The SHOW PARAMETERS command, without any string following the command, displays all initialization parameters.

Your output may vary depending on the version and configuration of the Oracle Database server to which you are connected. You need SELECT ON V\_$PARAMETER object privileges to use the PARAMETERS clause, otherwise you will receive a message

```
ORA-00942: table or view does not exist
```

PNO

Shows the current page number.

RECYC\[LEBIN\] \[original\_name\]

Shows objects in the recycle bin that can be reverted with the FLASHBACK BEFORE DROP command. You do not need to remember column names, or interpret the less readable output from the query:

```
SELECT * FROM USER_RECYCLEBIN
```

The query returns four columns displayed in the following order:

| Column Name | Description |
| --- | --- |
| `ORIGINAL NAME` | Shows the original name used when creating the object. |
| `RECYCLEBIN NAME` | Shows the name used to identify the object in the recyclebin. |
| `OBJECT TYPE` | Shows the type of the object. |
| `DROP TIME` | Shows the time when the object was dropped. |

The output columns can be formatted with the COLUMN command.

For DBAs, the command lists their own objects as they have their own user\_recyclebin view.

REL\[EASE\]

Shows the release number of Oracle Database that SQL\*Plus is accessing.

REPF\[OOTER\]

Shows the current REPFOOTER definition.

REPH\[EADER\]

Shows the current REPHEADER definition.

SPOO\[L\]

Shows whether output is being spooled.

SGA

Displays information about the current instance's System Global Area. You need SELECT ON V\_$SGA object privileges otherwise you will receive a message

```
ORA-00942: table or view does not exist
```

SPPARAMETERS \[parameter\_name\]

As for SHOW PARAMETERS except that SHOW SPPARAMETERS displays current values for initialization parameters for all instances. You can use a string after the command to see a subset of parameters whose names include that string.

The SHOW SPPARAMETERS command, without any string following the command, displays all initialization parameters for all instances.

Your output may vary depending on the version and configuration of the Oracle Database server to which you are connected. You need SELECT ON V\_$PARAMETER object privileges to use the SPPARAMETERS clause.

SQLCODE

Shows the value of SQL.SQLCODE (the SQL return code of the most recent operation).

TTI\[TLE\]

Shows the current TTITLE definition.

USER

Shows the username you are currently using to access SQL\*Plus. If you connect as "/ AS SYSDBA", then the SHOW USER command displays

```
USER is "SYS"
```

XQUERY

Shows the current values of the XQUERY settings, BASEURI, CONTEXT, NODE and ORDERING.

```
xquery BASEURI "public/scott" CONTEXT "doc("test.xml")" NODE byreference ORDERING ordered
```

The following output is displayed when no values are set:

```
xquery BASEURI "" CONTEXT "" NODE default ORDERING default
```

Examples

To display information about the SGA, enter

```
SHOW SGA
```

```
Total System Global Area                            7629732 bytes 
Fixed Size                                            60324 bytes 
Variable Size                                       6627328 bytes 
Database Buffers                                     409600 bytes 
Redo Buffers                                         532480 bytes
```

The following example illustrates how to create a stored procedure and then show its compilation errors:

```
CONNECT SYSTEM/MANAGER
CREATE PROCEDURE HR.PROC1 AS
BEGIN
:P1 := 1;
END;
/
```

```
Warning: Procedure created with compilation errors.
```

```
SHOW ERRORS PROCEDURE PROC1
```

```
NO ERRORS.
```

```
SHOW ERRORS PROCEDURE HR.PROC1
```

```
Errors for PROCEDURE HR PROC1:
LINE/COL ERROR
--------------------------------------------------------
3/3      PLS-00049: bad bind variable 'P1'
```

To show whether AUTORECOVERY is enabled, enter

```
SHOW AUTORECOVERY
```

```
AUTORECOVERY ON
```

To display the connect identifier for the default instance, enter

```
SHOW INSTANCE
```

```
INSTANCE "LOCAL"
```

To display the location for archive logs, enter

```
SHOW LOGSOURCE
```

```
LOGSOURCE "/usr/oracle90/dbs/arch"
```

To display objects that can be reverted with the FLASHBACK commands where CJ1 and ABC were objects dropped, enter:

```
SHOW RECYCLEBIN
```

```
ORIGINAL NAME     RECYCLEBIN NAME       OBJECT TYPE     DROP TIME
--------------    ------------------    ------------    --------------------
CJ1               RB$$29458$TABLE$0     TABLE           2003-01-22:14:54:07
ABC               RB$$29453$TABLE$0     TABLE           2003-01-20:18:50:29
```

To restore CJ1, enter

```
FLASHBACK TABLE CJ1 TO BEFORE DROP;
```