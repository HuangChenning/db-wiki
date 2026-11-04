---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SHOW.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
SHO[W] option
```

where option represents one of the following terms or clauses:

```
system_variable  ALL BTI[TLE]  CON_ID  CON_NAME EDITION  ERR[ORS] [ {ANALYTIC VIEW | ATTRIBUTE DIMENSION | HIERARCHY | FUNCTION | PROCEDURE | PACKAGE | PACKAGE BODY | TRIGGER | VIEW | TYPE | TYPE BODY | DIMENSION | JAVA CLASS } [schema.]name]HISTORY  LNO  LOBPREF[ETCH]  PARAMETER[S] [parameter_name]  PDBS PNO  RECYC[LEBIN] [original_name]  REL[EASE]  REPF[OOTER]  REPH[EADER]  ROWPREF[ETCH] SGA SPOO[L]  SPPARAMETER[S] [parameter_name]  SQLCODE STATEMENTC[ACHE] TTI[TLE] USER XQUERY
```

Shows the value of a SQL\*Plus system variable or the current SQL\*Plus environment. SHOW SGA requires a DBA privileged login.

Terms

```
system_variable
```

Represents any system variable set by the SET command.

```
ALL
```

Lists the settings of all SHOW options, except ERRORS and SGA, in alphabetical order.

```
CON_ID
```

Displays the id of the Container to which you are connected when connected to a Consolidated Database.

```
CON_NAME
```

Displays the name of the Container to which you are connected when connected to a Consolidated Database.

```
EDITION
```

Shows the edition attribute of the existing database.

```
BTI[TLE]
```

Shows the current BTITLE definition.

```
ERR[ORS] [{ANALYTIC VIEW | ATTRIBUTE DIMENSION | HIERARCHY | FUNCTION | PROCEDURE | PACKAGE | PACKAGE BODY | TRIGGER  | VIEW | TYPE | TYPE BODY | DIMENSION | JAVA CLASS} [schema.]name]
```

Shows the compilation errors of a stored procedure (includes stored functions, procedures, and packages). After you use the CREATE command to create a stored procedure, a message is displayed if the stored procedure has any compilation errors. To see the errors, you use SHOW ERRORS.

When you specify SHOW ERRORS with no arguments, SQL\*Plus shows compilation errors for the most recently created or altered stored procedure. When you specify the type (analytic view, attribute dimension, hierarchy, function, procedure, package, package body, trigger, view, type, type body, dimension, or java class) and the name of the PL/SQL stored procedure, SQL\*Plus shows errors for that stored procedure. For more information on compilation errors, see your PL/SQL User's Guide and Reference.

schema contains the named object. If you omit schema, SHOW ERRORS assumes the object is located in your current schema.

SHOW ERRORS output displays the line and column number of the error (LINE/COL) as well as the error itself (ERROR). LINE/COL and ERROR have default widths of 8 and 65, respectively. You can use the COLUMN command to alter the default widths.

```
HISTORY
```

Shows the current command history status that is set by using the [SET HISTORY](SET-system-variable-summary.md) command.

```
LNO
```

Shows the current line number (the position in the current page of the display and/or spooled output).

```
LOBPREFETCH
```

Shows the current setting for the amount of LOB data that SQL\*Plus will prefetch from the database at one time. For more information about setting the amount of LOB data that SQL\*Plus will prefetch from the database at one time, see [SET LOBPREFETCH](SET-system-variable-summary.md).

```
PARAMETERS [parameter_name]
```

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
```
PDBS
```

Display the names, ids, mode and restriction status of Pluggable Databases in the Consolidated Database to which you are connected.

The PDBS option is only available when you are logged in as SYSDBA and have the SYSDBA privilege. For non-DBA users, attempting to use the PDBS option returns the error SP2-0382: The SHOW PDBS command is not available.

```
PNO
```

Shows the current page number.

```
RECYC[LEBIN] [original_name]
```

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

```
REL[EASE]
```

Shows the release number of Oracle Database that SQL\*Plus is accessing.

```
REPF[OOTER]
```

Shows the current REPFOOTER definition.

```
REPH[EADER]
```

Shows the current REPHEADER definition.

```
ROWPREFETCH
```

Shows the current setting for the number of rows that SQL\*Plus will prefetch from the database at one time. For more information about setting the number of rows that SQL\*Plus will prefetch from the database at one time, see [SET ROWPREFETCH](SET-system-variable-summary.md).

```
SPOO[L]
```

Shows whether output is being spooled.

```
SGA
```

Displays information about the current instance's System Global Area. You need SELECT ON V\_$SGA object privileges otherwise you will receive a message

```
ORA-00942: table or view does not exist
```
```
SPPARAMETERS [parameter_name]
```

As for SHOW PARAMETERS except that SHOW SPPARAMETERS displays current values for initialization parameters for all instances. You can use a string after the command to see a subset of parameters whose names include that string.

The SHOW SPPARAMETERS command, without any string following the command, displays all initialization parameters for all instances.

Your output may vary depending on the version and configuration of the Oracle Database server to which you are connected. You need SELECT ON V\_$PARAMETER object privileges to use the SPPARAMETERS clause.

```
SQLCODE
```

Shows the value of SQL.SQLCODE (the SQL return code of the most recent operation).

```
STATEMENTCACHE
```

Shows the current setting for the statement cache size. For more information about setting the statement cache size, see [SET STATEMENTCACHE](SET-system-variable-summary.md).

```
TTI[TLE]
```

Shows the current TTITLE definition.

```
USER
```

Shows the username you are currently using to access SQL\*Plus. If you connect as "/ AS SYSDBA", then the SHOW USER command displays

```
USER is "SYS"
```
```
XQUERY
```

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

To display the id of the container to which you are connected, enter

```
SHOW CON_ID
```
```
CON_ID
------------------------------
1
```

To display the name of the container to which you are connected, enter

```
SHOW CON_NAME
```
```
CON_NAME
------------------------------
CDB$ROOT
```

To display the current command history status that is set by issuing the [SET HIST\[ORY\] {ON | OFF | n}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-45BC9BAA-83C0-4AD8-A912-ECC836A83AA2) command, enter

```
SHOW HISTORY
```
```
SQL> set history on
SQL> show history
History is ON and set to "100"
SQL> set history off
SQL> show history
History is OFF
SQL> set history 1000
SQL> show history
History is ON and set to "1000"
```

To display the names, ids, and modes of Pluggable Databases in the Consolidated Database to which you are connected, enter

```
SHOW PDBS
```
```
CON_ID CON_NAME   OPEN MODE    RESTRICTED
------ ---------- ------------ -----------
2      PDB$SEED   READ ONLY    NO
3      CDB1_PDB1  READ WRITE   NO
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