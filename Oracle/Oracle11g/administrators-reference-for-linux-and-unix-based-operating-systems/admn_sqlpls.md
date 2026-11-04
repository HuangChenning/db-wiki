---
title: "Administering SQL*Plus"
book: "Administrator's Reference for Linux and UNIX-Based Operating Systems"
doc_id: E10839-25
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10839/admn_sqlpls.htm
tags:
  - oracle
  - 11g
  - administrators-reference-for-linux-and-unix-based-operating-systems
---

## 4 Administering SQL\*Plus

This chapter describes how to administer SQL\*Plus. It contains the following sections:

- Administering Command-Line SQL\*Plus
- Using Command-Line SQL\*Plus
- SQL\*Plus Restrictions
	See Also:
	[SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/toc.htm) for more information about SQL\*Plus

## 4.1 Administering Command-Line SQL\*Plus

This section describes how to administer command-line SQL\*Plus. In the examples, SQL\*Plus replaces the question mark (?) with the value of the `ORACLE_HOME` environment variable.

### 4.1.1 Using Setup Files

When you start SQL\*Plus, it runs the `glogin.sql` site profile setup file and then runs the `login.sql` user profile setup file.

Using the Site Profile File

The global site profile file is `$ORACLE_HOME/sqlplus/admin/glogin.sql`. If a site profile exists at this location, then it is overwritten when you install SQL\*Plus. If SQL\*Plus is removed, then the site profile file is also removed.

Using the User Profile File

The user profile file is `login.sql`. SQL\*Plus looks for this file in the current directory, and then in the directories specified by the `SQLPATH` environment variable. The value of this environment variable is a colon-separated list of directories. SQL\*Plus searches these directories for the `login.sql` file in the order that they are listed in the `SQLPATH` environment variable.

The options set in the `login.sql` file override those set in the `glogin.sql` file.

See Also:

[SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/toc.htm) for more information about profile files

### 4.1.2 Using the PRODUCT\_USER\_PROFILE Table

Oracle Database provides the PRODUCT\_USER\_PROFILE table that you can use to disable the specified SQL and SQL\*Plus commands. This table is automatically created when you choose an installation type that installs a preconfigured database.

See Also:

[Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more information about installation options

To re-create the PRODUCT\_USER\_PROFILE table, run the `$ORACLE_HOME/sqlplus/admin/pupbld.sql` script in the SYSTEM schema. For example, run the following commands, where `SYSTEM_PASSWORD` is the password of the SYSTEM user:

```
$ sqlplus 
SQL> CONNECT SYSTEM
Enter password: system_password
SQL> @?/sqlplus/admin/pupbld.sql
```

You can also re-create the PRODUCT\_USER\_PROFILE table manually in the SYSTEM schema by using the `$ORACLE_HOME/bin/pupbld` shell script. This script prompts for the SYSTEM password. To run the `pupbld` script without interaction, then set the `SYSTEM_PASS` environment variable to the SYSTEM user name and password.

### 4.1.3 Using Oracle Database Sample Schemas

When you install Oracle Database or use Oracle Database Configuration Assistant to create a database, you can choose to install Oracle Database Sample Schemas.

See Also:

[Oracle Database Sample Schemas](https://docs.oracle.com/cd/E11882_01/server.112/e10831/toc.htm) for information about installing and using Oracle Database Sample Schemas

### 4.1.4 Installing and Removing SQL\*Plus Command-Line Help

This section describes how to install and remove the SQL\*Plus command-line Help.

- Installing SQL\*Plus Command-Line Help
- Removing SQL\*Plus Command-Line Help

See Also:

[SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/toc.htm) for more information about the SQL\*Plus command-line Help

#### 4.1.4.1 Installing SQL\*Plus Command-Line Help

There are three ways to install the SQL\*Plus command-line Help:

- Complete an installation that installs a preconfigured database.
	When you install a preconfigured database as part of an installation, SQL\*Plus automatically installs the SQL\*Plus command-line Help in the SYSTEM schema.
- Install the command-line Help manually in the SYSTEM schema by using the `$ORACLE_HOME/bin/helpins` shell script.
	The `helpins` script prompts for the SYSTEM password. To run this script without interaction, set the `SYSTEM_PASS` environment variable to the SYSTEM user name and password. For example:
	- Bourne, Bash, or Korn shell:
		```
		$ SYSTEM_PASS=SYSTEM/system_password; export SYSTEM_PASS
		```
		- C shell:
		```
		% setenv SYSTEM_PASS SYSTEM/system_password
		```
- Install the command-line Help manually in the SYSTEM schema by using the `$ORACLE_HOME/sqlplus/admin/help/helpbld.sql` script.
	For example, run the following commands, where `system_password` is the password of the SYSTEM user:
	```
	$ sqlplus 
	SQL> CONNECT SYSTEM
	Enter password: system_password
	SQL> @?/sqlplus/admin/help/helpbld.sql ?/sqlplus/admin/help helpus.sql
	```
	Note:
	Both the `helpins` shell script and the `helpbld.sql` script drop existing command-line Help tables before creating new tables.

#### 4.1.4.2 Removing SQL\*Plus Command-Line Help

To manually drop the SQL\*Plus command-line Help tables from the SYSTEM schema, run the `$ORACLE_HOME/sqlplus/admin/help/helpdrop.sql` script. To do this, run the following commands, where `system_password` is the password of the SYSTEM user:

```
$ sqlplus 
SQL> CONNECT SYSTEM
Enter password: system_password
SQL> @?/sqlplus/admin/help/helpdrop.sql
```

## 4.2 Using Command-Line SQL\*Plus

This section describes how to use command-line SQL\*Plus. It contains the following topics:

- Using a System Editor from SQL\*Plus
- Running Operating System Commands from SQL\*Plus
- Interrupting SQL\*Plus
- Using the SPOOL Command

### 4.2.1 Using a System Editor from SQL\*Plus

If you run an `ED` or `EDIT` command at the SQL\*Plus prompt, then the system starts an operating system editor, such as `ed`, `emacs`, `ned`, or `vi`. However, the `PATH` environment variable must include the directory where the editor executable is located.

When you start the editor, the current SQL buffer is placed in the editor. When you exit the editor, the changed SQL buffer is returned to SQL\*Plus.

You can specify which editor should start by defining the SQL\*Plus `_EDITOR` variable. You can define this variable in the `glogin.sql` site profile or the `login.sql` user profile. Alternatively, you can define it during the SQL\*Plus session. For example, to set the default editor to `vi`, run the following command:

```
SQL> DEFINE _EDITOR=vi
```

If you do not set the `_EDITOR` variable, then the value of either the `EDITOR` or the `VISUAL` environment variable is used. If both environment variables are set, then the value of the `EDITOR` variable is used. If `_EDITOR`, `EDITOR`, and `VISUAL` are not specified, then the default editor is `ed`.

When you start the editor, SQL\*Plus uses the `afiedt.buf` temporary file to pass text to the editor. You can use the `SET EDITFILE` command to specify a different file name. For example:

```
SQL> SET EDITFILE /tmp/myfile.sql
```

SQL\*Plus does not delete the temporary file.

### 4.2.2 Running Operating System Commands from SQL\*Plus

Using the HOST command or an exclamation point (!) as the first character after the SQL\*Plus prompt causes subsequent characters to be passed to a subshell. The `SHELL` environment variable sets the shell used to run operating system commands. The default shell is the Bourne shell. If the shell cannot be run, then SQL\*Plus displays an error message.

To return to SQL\*Plus, run the `exit` command or press Ctrl+D.

For example, to run a single command, use the following command syntax:

```
SQL> ! command
```

In this example, `command` represents the operating system command that you want to run.

To run multiple operating system commands from SQL\*Plus, run the HOST or! command. Press Enter to return to the operating system prompt.

### 4.2.3 Interrupting SQL\*Plus

While running SQL\*Plus, you can stop the scrolling record display and terminate a SQL statement by pressing Ctrl+C.

### 4.2.4 Using the SPOOL Command

The default file name extension of files generated by the SPOOL command is `.lst`. To change this extension, specify a spool file containing a period (.). For example:

```
SQL> SPOOL query.txt
```

## 4.3 SQL\*Plus Restrictions

This section describes the following SQL\*Plus restrictions:

- Resizing Windows
- Return Codes
- Hiding the Password

### 4.3.1 Resizing Windows

The default values for the SQL\*Plus `LINESIZE` and `PAGESIZE` system variables do not automatically adjust for window size.

### 4.3.2 Return Codes

Operating system return codes use only one byte, which is not enough space to return an Oracle error code. The range for a return code is 0 to 255.

### 4.3.3 Hiding the Password

If you set the `SYSTEM_PASS` environment variable to the user name and password of the SYSTEM user, then the output of the `ps` command may display this information. To prevent unauthorized access, enter the `SYSTEM` password only when prompted by SQL\*Plus.

To automatically run a script, consider using an authentication method that does not require you to store a password. For example, externally authenticated logins to Oracle Database. If you have a low-security environment, then you should consider using operating system pipes in script files to pass a password to SQL\*Plus. For example:

```
$ echo system_password | sqlplus SYSTEM @MYSCRIPT
```

Alternatively, run the following commands:

```
$ sqlplus <<EOF
SYSTEM/system_password
SELECT ...
EXIT
EOF
```

In the preceding examples, `system_password` is the password of the SYSTEM user.