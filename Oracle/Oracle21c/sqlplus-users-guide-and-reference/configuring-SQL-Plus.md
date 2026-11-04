---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/configuring-SQL-Plus.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

This chapter explains how to configure your SQL\*Plus command-line environment. It has the following topics:

- SQL\*Plus Environment Variables
- SQL\*Plus Configuration

### 2.1 SQL\*Plus Environment Variables

These environment variables specify the location or path of files used by SQL\*Plus. For other environment variables that influence the behavior of SQL\*Plus, see the Oracle Database Administrator's Reference.

Table 2-1 Parameters or Environment Variables influencing SQL\*Plus

| Parameter or Variable | Description |
| --- | --- |
| LD\_LIBRARY\_PATH | Environment variable to specify the path used to search for libraries on UNIX and Linux. The environment variable may have a different name on some operating systems, such as DYLD\_LIBRARY\_PATH on Apple Mac OS, LIBPATH on IBM/AIX-5L, and SHLIB\_PATH on HP-UX. Not applicable to Windows operating systems.  Example  ``` $ORACLE_HOME/lib ``` |
| LOCAL | Windows environment variable to specify a connection string. Performs the same function as TWO\_TASK on UNIX. |
| NLS\_LANG | Environment variable to specify globalization behavior.  Example  ``` american_america.utf8 ``` |
| ORACLE\_HOME | Environment variable to specify where SQL\*Plus is installed. It is also used by SQL\*Plus to specify where message files are located.  Examples:  ``` d:\oracle\10g /u01/app/oracle/product/v10g ``` |
| ORA\_EDITION | Environment variable to specify the database edition to use. If you specify the edition with the CONNECT or SQLPLUS command option, edition=value, it is used instead of ORA\_EDITION. If no edition is specified in either the CONNECT or SQLPLUS command option, or in ORA\_EDITION, SQL\*Plus connects to the default edition.  When ORA\_EDITION is set, a subsequent STARTUP command in the session results in an ORA-38802 error. To correct this, you must unset ORA\_EDITION, then reconnect and shutdown the database, then start the database again. |
| ORA\_NLS10 | Environment variable to specify the locations of the NLS data and the user boot file in SQL\*Plus 10.2. The default location is $ORACLE\_HOME/nls/data. In a system with both Oracle9i and 10g, or a system under version upgrade, you should set ORA\_NLS10 for Oracle 10g and set ORA\_NLS33 for 9i. The default NLS location in 9i was $ORACLE\_HOME/common/nls/admin/data. |
| ORACLE\_PATH | Environment variable to specify the location of SQL scripts. If SQL\*Plus cannot find the file in ORACLE\_PATH, or if ORACLE\_PATH is not set, it searches for the file in the current working directory.  Not applicable to Windows |
| ORACLE\_SID | Environment variable to specify the database instance, optional |
| PATH | Environment variable to specify the path to search for executables, and DLLs in Windows. Typically includes ORACLE\_HOME/bin |
| SQLPATH | Environment variable or Windows registry entry to specify the location of SQL scripts. SQL\*Plus searches for SQL scripts, including login.sql, in the directories specified by SQLPATH. SQLPATH is a colon-separated list of directories. There is no default value set in UNIX installations.  In Windows, SQLPATH is defined in a registry entry during installation. For more information about the SQLPATH registry entry, see SQLPATH Registry Entry. |
| TNS\_ADMIN | Environment variable to specify the location of the tnsnames.ora file. If not specified, $ORACLE\_HOME/network/admin is used  Example  ``` h:\network  /var/opt/oracle ``` |
| TWO\_TASK | UNIX environment variable to specify a connection string. Connections that do not specify a database will connect to the database specified in TWO\_TASK.  Example  ``` TWO_TASK=MYDB export TWO_TASK sqlplus hr ```  is the same as:  ``` sqlplus hr@MYDB ``` |

#### 2.1.1 SQLPATH Registry Entry

The SQLPATH registry entry specifies the location of SQL scripts. SQL\*Plus searches for SQL scripts in the current directory and then in the directories specified by the SQLPATH registry entry, and in the subdirectories of SQLPATH directories.

The HKEY\_LOCAL\_MACHINE\\SOFTWARE\\ORACLE\\HOME0 registry subkey (or the HOMEn directory for the associated ORACLE\_HOME) contains the SQLPATH registry entry. SQLPATH is created with a default value of ORACLE\_HOME\\DBS. You can specify any directories on any drive as valid values for SQLPATH.

When setting the SQLPATH registry entry, you can concatenate directories with a semicolon (;). For example:

`c:\oracle\ora12\database;c:\oracle\ora12\dbs`

See the Registry Editor's help system for instructions on how to edit the SQLPATH registry entry.

### 2.2 SQL\*Plus Configuration

You can set up your SQL\*Plus environment to use the same settings with each session.

There are two operating system files to do this:

- The Site Profile file, glogin.sql, for site wide settings.
- Additionally, the User Profile, login.sql, sets user specific settings.

The exact names of these files is system dependent.

Note:

The Site Profile and User Profile files are run after a successful Oracle Database connection from a `SQLPLUS` or `CONNECT` command, or where `/NOLOG` is specified.The Site Profile and User Profile files are not run when you switch to another PDB using `ALTER SESSION SET CONTAINER`.

Some privileged connections may generate errors if SET SERVEROUTPUT or SET APPINFO commands are put in the Site Profile or User Profile.

The following tables show the profile scripts, and some commands and settings that affect the Command-line user interface.

Table 2-2 Profile Scripts affecting SQL\*Plus User Interface Settings

| This script... | is run in the Command-line... |
| --- | --- |
| Site Profile (glogin.sql)  Can contain any content that can be included in a SQL\*Plus script, such as system variable settings or other global settings the DBA wants to implement. | After successful Oracle Database connection from a SQLPLUS or CONNECT command.  Where /NOLOG is specified. |
| User Profile (login.sql)  Can contain any content that can be included in a SQL\*Plus script, but the settings are only applicable to the user's sessions. | Immediately after the Site Profile. |

Table 2-3 Commands in Profile scripts affecting SQL\*Plus User Interface Settings

| In a profile script, this command... | affects the Command-line by... |
| --- | --- |
| [SET SQLPLUSCOMPAT\[IBILITY\] {x.y\[.z\]}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-B78B8F90-AD6C-48CA-B0A8-D657F6FBFC38)  Also see the [SQL\*Plus Compatibility Matrix](SET-system-variable-summary.md). | Setting the SQL\*Plus compatibility mode to obtain the behavior the DBA wants for this site. |
| SQLPLUS command [COMPATIBILITY Option](starting-SQL-Plus.md) | As for SET SQLPLUSCOMPATIBILITY but set with the SQLPLUS command COMPATIBILITY option. |
| SQLPLUS command [RESTRICT Option](starting-SQL-Plus.md) | Starting SQL\*Plus with the RESTRICT option set to 3 prevents the User Profile script from being read. |

#### 2.2.1 Site Profile

A Site Profile script is created during installation. It is used by the database administrator to configure site-wide behavior for SQL\*Plus Command-line connections. The Site Profile script installed during installation is an empty script.

The Site Profile script is generally named glogin.sql. SQL\*Plus executes this script whenever a user starts a SQL\*Plus session and successfully establishes the Oracle Database connection.

The Site Profile enables the DBA to set up site wide SQL\*Plus environment defaults for all users of a particular SQL\*Plus installation

Users cannot directly access the Site Profile.

##### 2.2.1.1 Default Site Profile Script

The Site Profile script is $ORACLE\_HOME/sqlplus/admin/glogin.sql in UNIX, and ORACLE\_HOME\\sqlplus\\admin\\glogin.sql in Windows. If a Site Profile already exists at this location, it is overwritten when you install SQL\*Plus. If SQL\*Plus is removed, the Site Profile script is deleted.

#### 2.2.2 User Profile

For SQL\*Plus command-line connections, SQL\*Plus also supports a User Profile script. The User Profile is executed after the Site Profile and is intended to allow users to specifically customize their session. The User Profile script is generally named login.sql. SQL\*Plus searches for the directories you specify with the ORACLE\_PATH environment variable. SQL\*Plus searches this colon-separated list of directories and their subdirectories in the order they are listed.

Note:

SQL\*Plus will no longer search for login.sql in the current directory.

You can add any SQL commands, PL/SQL blocks, or SQL\*Plus commands to your user profile. When you start SQL\*Plus, it automatically searches for your user profile and runs the commands it contains.

##### 2.2.2.1 Modifying Your LOGIN File

You can modify your LOGIN file just as you would any other script. The following sample User Profile script shows some modifications that you could include:

```
--   login.sql
--   SQL*Plus user login startup file.
--
--   This script is automatically run after glogin.sql
--
-- To change the SQL*Plus prompt to display the current user,
-- connection identifier and current time.
-- First set the database date format to show the time.
ALTER SESSION SET nls_date_format = 'HH:MI:SS';

-- SET the SQLPROMPT to include the _USER, _CONNECT_IDENTIFIER
-- and _DATE variables.
SET SQLPROMPT "_USER'@'_CONNECT_IDENTIFIER _DATE> "

-- To set the number of lines to display in a report page to 24.
SET PAGESIZE 24

-- To set the number of characters to display on each report line to 78.
SET LINESIZE 78

-- To set the number format used in a report to $99,999.
SET NUMFORMAT $99,999
```

See Also:

- [SET](SET.md) command for more information on these and other SET command variables you may wish to set in your SQL\*Plus LOGIN file.
- [About Using Predefined Variables](using-substitution-variables-sqlplus.md) for more information about predefined variables.

#### 2.2.3 Storing and Restoring SQL\*Plus System Variables

From the Command-line you can store the current SQL\*Plus system variables in a script with the STORE command. If you alter any variables, this script can be run to restore the original values. This is useful if you want to reset system variables after running a report that alters them. You could also include the script in your User Profile script so that these system variables are set each time you start SQL\*Plus.

To store the current setting of all system variables, enter

```
STORE SET file_name
```

Enter a file name and file extension, or enter only the file name to use the default extension.SQL. You can use the [SET SUF\[FIX\] {SQL | text}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-0DFB3D8C-0389-4F44-A68D-3FDBB9F962EA) command to change the default file extension.

##### 2.2.3.1 Restoring the System Variables

To restore the stored system variables, enter

```
START file_name
```

If the file has the default extension (as specified by the [SET SUF\[FIX\] {SQL | text}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-0DFB3D8C-0389-4F44-A68D-3FDBB9F962EA) command), you do not need to add the period and extension to the file name.

You can also use the @ (at sign) or the @@ (double at sign) commands to run the script.

```
Created file plusenv
```

Now the value of any system variable can be changed:

```
SHOW PAGESIZE
```
```
PAGESIZE 24
```
```
SET PAGESIZE 60
SHOW PAGESIZE
```
```
PAGESIZE 60
```

The original values of system variables can then be restored from the script:

```
START plusenv
SHOW PAGESIZE
```
```
PAGESIZE 24
```

Example 2-1 Storing and Restoring SQL\*Plus System Variables

To store the current values of the SQL\*Plus system variables in a new script "plusenv.sql":

```
STORE SET plusenv
```

#### 2.2.4 About Installing Command-line Help

Command-line help is usually installed during Oracle Database installation. If not, the database administrator can create the SQL\*Plus command-line help tables and populate them with SQL\*Plus help data by running a supplied SQL script from SQL\*Plus.

The database administrator can also remove the SQL\*Plus command-line help tables by running a SQL script from SQL\*Plus.

Before you can install or remove SQL\*Plus help, ensure that:

- SQL\*Plus is installed.
- The ORACLE\_HOME environment variable is set.
- The SQL\*Plus help script files exist:
	- HLPBLD.SQL - to drop and create new help tables.
		- HELPDROP.SQL - to drop existing help tables.
		- HELPUS.SQL - to populate the help tables with the help data.

##### 2.2.4.1 Running the hlpbld.sql Script to Install Command-line Help

Run the provided SQL script, HLPBLD.SQL, to load command-line help.

1. Log in to SQL\*Plus as the SYSTEM user with:
	```
	SQLPLUS SYSTEM
	```
	You are prompted to enter the password you have defined for the SYSTEM user.
2. In UNIX run the SQL script, HLPBLD.SQL, from SQL\*Plus with:
	```
	@$ORACLE_HOME/sqlplus/admin/help/hlpbld.sql helpus.sql
	```
	In Windows run the SQL script, HLPBLD.SQL, from SQL\*Plus with:
	```
	@%ORACLE_HOME%\SQLPLUS\ADMIN\HELP\HLPBLD.SQL HELPUS.SQL
	```
	The HLPBLD.SQL script creates and loads the help tables.

##### 2.2.4.2 Running the helpdrop.sql Script to Remove Command-line Help

Run the provided SQL script, HELPDROP.SQL, to remove the command-line help.

1. Log in to SQL\*Plus as the SYSTEM user with:
	```
	SQLPLUS SYSTEM
	```
	You are prompted to enter the password you have defined for the SYSTEM user.
2. In UNIX run the SQL script, HELPDROP.SQL, from SQL\*Plus with:
	```
	@$ORACLE_HOME/sqlplus/admin/help/helpdrop.sql
	```
	In Windows run the SQL script, HELPDROP.SQL, from SQL\*Plus with:
	```
	@%ORACLE_HOME\SQLPLUS\ADMIN\HELP\HELPDROP.SQL
	```
	The HELPDROP.SQL script drops the help tables, and then disconnects.

#### 2.2.5 About Configuring Oracle Net Services

If you plan to connect to a database other than the default, whether on the same computer or another computer, you need to ensure that Oracle Net is installed, and the database listener is configured and running. Oracle Net services are used by SQL\*Plus.

Oracle Net services and the database listener are installed by default during Oracle Database installation. For further information about installing and configuring Oracle Net, see the Oracle Database documentation at [`http://www.oracle.com/technology/documentation`](http://www.oracle.com/technology/documentation).