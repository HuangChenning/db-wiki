---
title: "SQL*Plus Security"
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_nine.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

## 9 SQL\*Plus Security

This chapter describes the available methods for controlling access to database tables, and SQL\*Plus commands. It covers the following topics:

## PRODUCT\_USER\_PROFILE Table

SQL\*Plus uses the PRODUCT\_USER\_PROFILE (PUP) table, a table in the SYSTEM account, to provide product-level security that supplements the user-level security provided by the SQL GRANT and REVOKE commands and user roles.

DBAs can use the PUP table to disable certain SQL and SQL\*Plus commands in the SQL\*Plus environment on a per-user basis. SQL\*Plus—not Oracle Database—enforces this security. DBAs can even restrict access to the GRANT, REVOKE, and SET ROLE commands to control users' ability to change their database privileges.

SQL\*Plus reads restrictions from the PUP table when a user logs in to SQL\*Plus and maintains those restrictions for the duration of the session. Changes to the PUP table will only take effect the next time the affected users log in to SQL\*Plus.

When SYSTEM, SYS, or a user authenticating with SYSDBA or SYSOPER privileges connects or logs in, SQL\*Plus does not read the PUP table. Therefore, no restrictions apply to these users.

The PUP table applies only to the local database. If accessing objects on a remote database through a database link, the PUP table for the remote database does not apply. The remote database cannot extract the username and password from the database link in order to determine that user's profile and privileges.

### Creating the PUP Table

You can create the PUP table by running the script named PUPBLD with the extension SQL as SYSTEM. The exact format of the file extension and the location of the file are system dependent. See your DBA for more information.

Note:

If the table is created incorrectly, all users other than privileged users will see a warning when connecting to Oracle Database that the PUP table information is not loaded.

### PUP Table Structure

The PUP table has the following columns:

```
PRODUCT                 NOT NULL VARCHAR2 (30)
USERID                  VARCHAR2(30)
ATTRIBUTE               VARCHAR2(240)
SCOPE                   VARCHAR2(240)
NUMERIC_VALUE           NUMBER(15,2)
CHAR_VALUE              VARCHAR2(240)
DATE_VALUE              DATE
LONG_VALUE              LONG
```

### Description and Use of PUP Columns

The following list describes each column in the PUP table:

| PUP Column | Description |
| --- | --- |
| PRODUCT | Must contain the product name (in this case "SQL\*Plus"). You cannot enter wildcards or NULL in this column. |
| USERID | Must contain the username (uppercase) of the user for whom you wish to disable the command. To disable the command for more than one user, use SQL wild cards (%) or make multiple entries. Thus, all of the following entries are valid: - HR - CLASS1 - CLASS% (all users whose names start with CLASS) - % (all users) |
| ATTRIBUTE | Must contain the name (in uppercase) of the SQL, SQL\*Plus, or PL/SQL command to disable (for example, RUN). If you are disabling a role, it must contain the character string "ROLES". You cannot enter a wildcard. See PUP Table Administration for a list of SQL and SQL\*Plus commands you can disable. See Creating and Controlling Roles for information on how to disable a role. |
| SCOPE | Not used, it is recommended that you enter NULL. Other products may store specific file restrictions or other data in this column. |
| NUMERIC\_VALUE | Not used, it is recommended that you enter NULL. Other products may store numeric values in this column. |
| CHAR\_VALUE | Must contain the character string "DISABLED" to disable a SQL, SQL\*Plus, or PL/SQL command. If you are disabling a role, it must contain the name of the role you wish to disable. You cannot use a wildcard. See Disabling Commands with SQLPLUS -RESTRICT for information on disabling a role. |
| DATE\_VALUE | Not used, it is recommended that you enter NULL. Other products may store DATE values in this column. |
| LONG\_VALUE | Not used, it is recommended that you enter NULL. Other products may store LONG values in this column. |

### PUP Table Administration

The DBA username SYSTEM owns and has all privileges on the PUP table. Other Oracle Database usernames should have only SELECT access to this table, which enables a view of restrictions for that username and those restrictions assigned to PUBLIC. The script PUPBLD.SQL, when run, grants SELECT access on the PUP table to PUBLIC.

## Disabling SQL\*Plus, SQL, and PL/SQL Commands

To disable a SQL or SQL\*Plus command for a given user, insert a row containing the user's username in the Userid column, the command name in the Attribute column, and DISABLED in the Char\_Value column. The Scope, Numeric\_Value, and Date\_Value columns should contain NULL. For example:

```
PRODUCT    USERID  ATTRIBUTE  SCOPE   NUMBERIC    CHAR       DATE    LONG
                                      VALUE       VALUE      VALUE   VALUE
-------    ------  ---------  -----   --------    ------     -----   -----
SQL*Plus   HR      HOST                           DISABLED
SQL*Plus   %       INSERT                         DISABLED
SQL*Plus   %       UPDATE                         DISABLED
SQL*Plus   %       DELETE                         DISABLED
```

To re-enable commands, delete the row containing the restriction.

<table><thead><tr><th colspan="4">SQL*Plus Commands That Can Be Disabled</th></tr></thead><tbody><tr><td headers="r1c1-t4">ACCEPT</td><td headers="r2c1-t4 r1c1-t4">DEFINE</td><td headers="r2c1-t4 r1c1-t4">PASSWORD</td><td headers="r2c1-t4 r1c1-t4">SHUTDOWN</td></tr><tr><td headers="r1c1-t4">APPEND</td><td headers="r3c1-t4 r1c1-t4">DEL</td><td headers="r3c1-t4 r1c1-t4">PAUSE</td><td headers="r3c1-t4 r1c1-t4">SPOOL</td></tr><tr><td headers="r1c1-t4">ARCHIVE LOG</td><td headers="r4c1-t4 r1c1-t4">DESCRIBE</td><td headers="r4c1-t4 r1c1-t4">PRINT</td><td headers="r4c1-t4 r1c1-t4">START (@, @@)</td></tr><tr><td headers="r1c1-t4">ATTRIBUTE</td><td headers="r5c1-t4 r1c1-t4">DISCONNECT</td><td headers="r5c1-t4 r1c1-t4">PROMPT</td><td headers="r5c1-t4 r1c1-t4">STARTUP</td></tr><tr><td headers="r1c1-t4">BREAK</td><td headers="r6c1-t4 r1c1-t4">EDIT</td><td headers="r6c1-t4 r1c1-t4">RECOVER</td><td headers="r6c1-t4 r1c1-t4">STORE</td></tr><tr><td headers="r1c1-t4">BTITLE</td><td headers="r7c1-t4 r1c1-t4">EXECUTE</td><td headers="r7c1-t4 r1c1-t4">REMARK</td><td headers="r7c1-t4 r1c1-t4">TIMING</td></tr><tr><td headers="r1c1-t4">CHANGE</td><td headers="r8c1-t4 r1c1-t4">EXIT/QUIT</td><td headers="r8c1-t4 r1c1-t4">REPFOOTER</td><td headers="r8c1-t4 r1c1-t4">TTITLE</td></tr><tr><td headers="r1c1-t4">CLEAR</td><td headers="r9c1-t4 r1c1-t4">GET</td><td headers="r9c1-t4 r1c1-t4">REPHEADER</td><td headers="r9c1-t4 r1c1-t4">UNDEFINE</td></tr><tr><td headers="r1c1-t4">COLUMN</td><td headers="r10c1-t4 r1c1-t4">HELP (?)</td><td headers="r10c1-t4 r1c1-t4">RUN</td><td headers="r10c1-t4 r1c1-t4">VARIABLE</td></tr><tr><td headers="r1c1-t4">COMPUTE</td><td headers="r11c1-t4 r1c1-t4">HOST</td><td headers="r11c1-t4 r1c1-t4">SAVE</td><td headers="r11c1-t4 r1c1-t4">WHENEVER OSERROR</td></tr><tr><td headers="r1c1-t4">CONNECT</td><td headers="r12c1-t4 r1c1-t4">INPUT</td><td headers="r12c1-t4 r1c1-t4">SET</td><td headers="r12c1-t4 r1c1-t4">WHENEVER SQLERROR</td></tr><tr><td headers="r1c1-t4">COPY</td><td headers="r13c1-t4 r1c1-t4">LIST (;)</td><td headers="r13c1-t4 r1c1-t4">SHOW</td><td headers="r13c1-t4 r1c1-t4">XQUERY</td></tr></tbody></table>

<table><thead><tr><th colspan="4">SQL Commands That Can Be Disabled</th></tr></thead><tbody><tr><td headers="r1c1-t5">ALTER</td><td headers="r2c1-t5 r1c1-t5">DELETE</td><td headers="r2c1-t5 r1c1-t5">MERGE</td><td headers="r2c1-t5 r1c1-t5">SET CONSTRAINTS</td></tr><tr><td headers="r1c1-t5">ANALYZE</td><td headers="r3c1-t5 r1c1-t5">DISASSOCIATE</td><td headers="r3c1-t5 r1c1-t5">NOAUDIT</td><td headers="r3c1-t5 r1c1-t5">SET ROLE</td></tr><tr><td headers="r1c1-t5">ASSOCIATE</td><td headers="r4c1-t5 r1c1-t5">DROP</td><td headers="r4c1-t5 r1c1-t5">PURGE</td><td headers="r4c1-t5 r1c1-t5">SET TRANSACTION</td></tr><tr><td headers="r1c1-t5">AUDIT</td><td headers="r5c1-t5 r1c1-t5">EXPLAIN</td><td headers="r5c1-t5 r1c1-t5">RENAME</td><td headers="r5c1-t5 r1c1-t5">TRUNCATE</td></tr><tr><td headers="r1c1-t5">CALL</td><td headers="r6c1-t5 r1c1-t5">FLASHBACK</td><td headers="r6c1-t5 r1c1-t5">REVOKE</td><td headers="r6c1-t5 r1c1-t5">UPDATE</td></tr><tr><td headers="r1c1-t5">COMMENT</td><td headers="r7c1-t5 r1c1-t5">GRANT</td><td headers="r7c1-t5 r1c1-t5">ROLLBACK</td><td headers="r7c1-t5 r1c1-t5">VALIDATE</td></tr><tr><td headers="r1c1-t5">COMMIT</td><td headers="r8c1-t5 r1c1-t5">INSERT</td><td headers="r8c1-t5 r1c1-t5">SAVEPOINT</td><td headers="r8c1-t5 r1c1-t5">na</td></tr><tr><td headers="r1c1-t5">CREATE</td><td headers="r9c1-t5 r1c1-t5">LOCK</td><td headers="r9c1-t5 r1c1-t5">SELECT</td><td headers="r9c1-t5 r1c1-t5">na</td></tr></tbody></table>

You can disable the following PL/SQL commands:

<table><thead><tr><th colspan="4">PL/SQL Commands That Can Be Disabled</th></tr></thead><tbody><tr><td headers="r1c1-t6">BEGIN</td><td headers="r2c1-t6 r1c1-t6">DECLARE</td><td headers="r2c1-t6 r1c1-t6">na</td><td headers="r2c1-t6 r1c1-t6">na</td></tr></tbody></table>

Note:

- Disabling HOST disables the operating system alias for HOST, such as $ on Windows, and! on UNIX.
- Disabling LIST disables; and numbers (numbers entered to go to that line in a script).
- You must disable HELP and? separately to disable access to command-line help.
- Disabling the SQL\*Plus SET command also disables SQL SET CONSTRAINTS, SET ROLE and SET TRANSACTION.
- Disabling SQL\*Plus START also disables @ and @@.
- Disabling BEGIN and DECLARE does not prevent the use of SQL\*Plus EXECUTE to run PL/SQL. EXECUTE must be disabled separately.
- Disabling EXIT/QUIT is not recommended. If disabled, terminate a command-line session by sending an EOF character such as Ctrl+D in UNIX or Ctrl+Z in Windows. Otherwise, terminate a session by terminating the SQL\*Plus process. If disabled, the EXIT operation in WHENEVER OSERROR and WHENEVER SQLERROR is also disabled.

Example 9-1 Setting Restrictions in the PUP Table

This is an example of how to insert a row into the PUP table to restrict the user HR from using the SELECT statement:

1. Log in as SYSTEM with the command
	```
	SQLPLUS SYSTEM
	```
2. Insert a row into the PUP table with the command:
	```
	INSERT INTO PRODUCT_USER_PROFILE
	VALUES ('SQL*Plus', 'HR', 'SELECT', NULL, NULL, 'DISABLED', NULL, NULL);
	```
3. Connect as HR and try to SELECT something:
	```
	CONNECT HR 
	SELECT * FROM EMP_DETAILS_VIEW;
	```
	This command causes the following error message:
	```
	SP2-0544: Command SELECT disabled in Product User Profile
	```
4. To delete this row and remove the restriction from the user HR, CONNECT again as SYSTEM and enter:
	```
	DELETE FROM PRODUCT_USER_PROFILE WHERE USERID = 'HR';
	```

## Creating and Controlling Roles

You can use SQL commands to create and control access to roles to provide security for your database tables. By creating a role and then controlling who has access to it, you can ensure that only certain users have access to particular database privileges.

Roles are created and used with the SQL CREATE, GRANT, and SET commands:

- To create a role, you use the CREATE command. You can create roles with or without passwords.
- To grant access to roles, you use the GRANT command. In this way, you can control who has access to the privileges associated with the role.
- To access roles, you use the SET ROLE command. If you created the role with a password, the user must know the password in order to access the role.

For more information about roles, see your [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm), your [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm), and your [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) manual.

### Disabling SET ROLE

From SQL\*Plus, users can submit any SQL command. In certain situations, this can cause security problems. Unless you take proper precautions, a user could use SET ROLE to access privileges obtained through an application role. With these privileges, they might issue SQL statements from SQL\*Plus that could wrongly change database tables.

To prevent application users from accessing application roles in SQL\*Plus, you can use the PUP table to disable the SET ROLE command. You also need to disable the BEGIN and SQL\*Plus EXECUTE commands to prevent application users setting application roles through a PL/SQL block. This gives a SQL\*Plus user only those privileges associated with the roles enabled when they started SQL\*Plus. For more information about the creation and usage of user roles, see your [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm).

### Disabling User Roles

To disable a role for a given user, insert a row in the PUP table containing the user's username in the Userid column, "ROLES" in the Attribute column, and the role name in the Char\_Value column.

Note:

When you enter "PUBLIC" or "%" for the Userid column, you disable the role for all users. You should only use "%" or "PUBLIC" for roles which are granted to "PUBLIC". If you try to disable a role that has not been granted to a user, none of the roles for that user are disabled.

The Scope, Numeric\_Value, and Date\_Value columns should contain NULL. For example:

```
PRODUCT    USERID  ATTRIBUTE  SCOPE   NUMERIC     CHAR      DATE     LONG
                                      VALUE       VALUE     VALUE    VALUE
-------    ------  ---------  -----   --------    ------    -----    -----
SQL*Plus   HR      ROLES                          ROLE1
SQL*Plus   PUBLIC  ROLES                          ROLE2
```

During login, these table rows are translated into the command

```
SET ROLE ALL EXCEPT ROLE1, ROLE2
```

To ensure that the user does not use the SET ROLE command to change their roles after login, you can disable the SET ROLE command.

To re-enable roles, delete the row containing the restriction.

See Disabling SET ROLE for more information.

## Disabling Commands with SQLPLUS -RESTRICT

Like the Product User Profile table, the RESTRICT option enables you to disable certain commands that interact with the operating system. However, commands disabled with the -RESTRICT option are disabled even when no connection to a server exists, and remain disabled until SQL\*Plus terminates.

The following table shows which commands are disabled in each restriction level.

| Command | Level 1 | Level 2 | Level 3 |
| --- | --- | --- | --- |
| EDIT | disabled | disabled | disabled |
| GET |  |  | disabled |
| HOST | disabled | disabled | disabled |
| SAVE |  | disabled | disabled |
| SPOOL |  | disabled | disabled |
| START |  |  | disabled |
| STORE |  | disabled | disabled |

Note:

- Disabling HOST also disables your operating system's alias for HOST, such as $ on Windows, and! on UNIX.
- Disabling the SQL\*Plus START command will also disable the SQL\*Plus @ and @@ commands.

For more information about the RESTRICT option, see the SQLPLUS [RESTRICT Option](ch_three.md).

## Program Argument Security

Some operating systems allow any user to see what programs are being run. If the display also shows command-line arguments, it may be possible to view the usernames and passwords of other SQL\*Plus users.

For example, on many UNIX or Linux systems the ps command shows program arguments. To stop passwords being displayed depends on how you use SQL\*Plus.

- To run SQL\*Plus interactively, always wait for SQL\*Plus to prompt for connection information, particularly your password.
- To run a batch SQL script from a UNIX shell script, set environment variables MYUSERNAME and MYPASSWORD to the appropriate values. Run a shell script containing:
	```
	sqlplus /nolog <<EOF
	connect $MYUSERNAME/$MYPASSWORD
	select ...
	EOF
	```
- To run a batch SQL script, hard code the username and password as the first line of the SQL script. Then call the script with:
	```
	sqlplus @myscript.sql
	```

When SQL\*Plus is started like this, it uses the first line of the script as the username/password@connection\_identifier string.

Avoid storing your username and password in files or scripts. If you do store your username and password in a file or script, ensure that the file or script is secured from non-authorized access.