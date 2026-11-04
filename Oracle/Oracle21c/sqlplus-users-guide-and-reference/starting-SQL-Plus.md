---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/starting-SQL-Plus.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

This chapter describes how to start, login, and connect to a database, how to get help, and how to exit SQL\*Plus.

Specific topics discussed are:

### 3.1 Login Username and Password

When you start SQL\*Plus, you need a username and password to login to an Oracle Database schema. Your username and password identify you as an authorized user of the Oracle Database schema.

The database administrator (DBA) is responsible for creating your database account with the necessary privileges and giving you the username and password that enables you to access your account.

Default logins are created and you are prompted for associated passwords during Oracle Database installation. Some of the default login usernames created are:

- SYS
- SYSTEM
- HR

Logins are created and displayed in messages during Oracle Database installation.

For further information about the default logins, see [Types of Oracle Database Users](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN-GUID-C7B90809-E930-44BF-B836-F760B0989BB0).

Once you have logged in, you can connect under a different username using the CONNECT command. The username and password must be valid for the database. For example, to connect the username TODD to the default database using the password FOX, you could enter

```
CONNECT TODD
```

You are prompted to enter the password, FOX.

In the command-line interface, if you omit the username and password, SQL\*Plus prompts you for them. Because CONNECT first disconnects you from your current database, you will be left unconnected to any database if you use an invalid username and password in your CONNECT command.

If you log on or connect as a user whose account has expired, you are prompted to change your password before you can connect.

If an account is locked, a message is displayed and connection as this user is not permitted until the account is unlocked by your DBA.

You can use the DISCONNECT command to disconnect from a database without leaving SQL\*Plus.

#### 3.1.1 Secure External Password Store

As a command-line alternative for large-scale deployments where applications use password credentials to connect to databases, it is possible to store such credentials in a client-side Oracle wallet. An Oracle wallet is a secure software container that is used to store authentication and signing credentials.

Storing database password credentials in a client-side Oracle wallet eliminates the need to embed usernames and passwords in application code, batch jobs, or scripts. This reduces the risk of exposing passwords in the clear in scripts and application code, and simplifies maintenance because you need not change your code each time usernames and passwords change. In addition, not having to change application code also makes it easier to enforce password management policies for these user accounts.

When you configure a client to use the external password store, applications can use the following syntax to connect to databases that use password authentication:

```
CONNECT /@database_alias
```

Note that you need not specify database login credentials in this `CONNECT` statement. Instead your system looks for database login credentials in the client wallet.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN11133) for information about configuring your client to use secure external password store and for information about managing credentials in it.

#### 3.1.2 Expired Password

In the command-line interface, if your password has expired, SQL\*Plus prompts you to change it when you attempt to log in. You are logged in once you successfully change your password.

#### 3.1.3 About Changing your Password

In the command-line interface, you can change your password with the PASSWORD command. See [PASSWORD](PASSWORD.md).

### 3.2 About Connecting to a Database

You must connect to an Oracle Database (instance) before you can query or modify data in that database. You can connect to the default database and to other databases accessible through your network. To connect to another database over a network, both databases must have Oracle Net configured, and have compatible network drivers. You must enter either a connection identifier or a net service name to connect to a database other than the default.

The connection identifier or net service name is entered:

- as an argument to the SQLPLUS Program Syntax when starting a command-line session.
- as an argument to the [CONNECT](CONNECT.md) command from a current session. For detailed usage, see [Accessing a Container in a CDB](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN13607) in the Oracle Database Administrator's Guide.

#### 3.2.1 Net Service Name

Your DBA is responsible for creating the databases you use and defining net service names for them in the tnsnames.ora file.

A net service name definition in the tnsnames.ora file has the syntax:

```
net_service_name= 
(DESCRIPTION= 
(ADDRESS=(PROTOCOL=tcp)(HOST=host)(PORT=port) )
(CONNECT_DATA= 
(SERVICE_NAME=service_name) ) )
```

To use a net service name (alias), it must have an entry in the tnsnames.ora file on the machine running SQL\*Plus. An entry in tnsnames.ora is not required if you use a connection identifier.

Example 3-1 The tnsnames.ora entry for the sales database

```
SALES1 =
(DESCRIPTION =
(ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521) )
(CONNECT_DATA=
(SERVICE_NAME=sales.us.acme.com) ) )
```

Example 3-2 Start a command-line session to the sales database using the net service name

```
SQLPLUS hr@SALES1
```

See [Configuration Parameters](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=NETRF-GUID-16D92508-C526-4AB1-A54D-CF23466624D6) and [Configuration and Administration of Oracle Net Services](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=NETAG-GUID-18C53DE7-28A6-4D01-AEA4-56A5F42B1B2A) for more information about database connections and net service name definitions.

#### 3.2.2 Full Connection Identifier

Depending on your configuration, use the full connection identifier syntax like:

```
(DESCRIPTION=
(ADDRESS=(PROTOCOL=tcp)(HOST=host)(PORT=port) )
(CONNECT_DATA=
(SERVICE_NAME=service_name) ) )
```

The `SERVICE_NAME` is the global database name entered during database creation. It combines a database name with a domain name. For example, the `SERVICE_NAME` `sales.us.acme.com` has a database name of `sales` and a domain of `us.acme.com`.

An `INSTANCE_NAME` is the name you give to the database instance during creation. It defaults to the SID you entered during database creation.

An Oracle System Identifier (`SID`) identifies a specific Oracle release 8.0 database instance.

You can optionally use an `INSTANCE_NAME` in place of the `SERVICE_NAME` phrase.

Use a `SID` in place of the `SERVICE_NAME` when connecting to an Oracle release 8.0 or earlier database.

Example 3-3 Full connection identifier for SALES1

```
SQLPLUS hr@\"(DESCRIPTION=
(ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521) )
(CONNECT_DATA=
(SERVICE_NAME=sales.us.acme.com) ) )\"
```

#### 3.2.3 Easy Connection Identifier

The easy or abbreviated connection identifier has the syntax:

```
[//]host[:port][/service_name]
```

Example 3-4 Start a command-line session to the sales database using the easy connection identifier

```
sqlplus hr@\"sales-server:1521/sales.us.acme.com\"
```

Example 3-5 CONNECT to the sales database using the easy connection identifier

When the password is omitted, the connect string needs to be quoted.

```
connect hr@"sales-server:1521/sales.us.acme.com"
```

The easy connection identifier can be used wherever you can use a full connection identifier, or a net service name. The easy syntax is less complex, and no tnsnames.ora entry is required.

Note:

Starting with Oracle Database release 19c, the easy connect syntax has improved functionality and is called Easy Connect Plus. For more information, see [About Easy Connect Plus](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=NETAG-GUID-8C85D289-6AF3-41BC-848B-BF39D32648BA).

#### 3.2.4 Connectionless Session with /NOLOG

In the command-line interface, it is possible to start SQL\*Plus without connecting to a database. This is useful for performing some database administration tasks, writing transportable scripts, or to use SQL\*Plus editing commands to write or edit scripts.

You use the /NOLOG argument to the SQLPLUS command to start a connectionless command-line session. After SQL\*Plus has started you can connect to a database with the CONNECT command.

Example 3-6 Start a connectionless SQL\*Plus session with /NOLOG

```
SQLPLUS /NOLOG
```

### 3.3 About Starting SQL\*Plus

If you are connecting to a remote Oracle database, make sure your Oracle Net software is installed and working properly. For more information, see [Testing and Troubleshooting Oracle Net Services](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=NETAG-GUID-E8B29E61-3236-486B-AB89-665215E86CFA).

When you start a SQL\*Plus command-line session, and after a CONNECT command in that session, the site profile, glogin.sql, and the user profile file, login.sql, are processed:

- After SQL\*Plus starts and connects, and prior to displaying the first prompt.
- After SQL\*Plus starts and connects, and prior to running a script specified on the command line.
- Prior to the first prompt when /NOLOG is specified on the command line and no connection is made.

The site profile file, glogin.sql is processed first, then the user profile file, login.sql.

#### 3.3.1 About Starting Command-line SQL\*Plus

To begin using SQL\*Plus, you must first understand how to start and stop SQL\*Plus.

1. Make sure that SQL\*Plus has been installed on your computer.
2. Log on to the operating system (if required).
3. Enter the command, SQLPLUS, and press Return.
	Note:
	Some operating systems expect you to enter commands in lowercase letters. If your system expects lowercase, enter the SQLPLUS command in lowercase.
	```
	SQLPLUS
	```
	SQL\*Plus displays its version number, the current date, and copyright information, and prompts you for your username (the text displayed on your system may differ slightly):
	```
	SQL*Plus: Release 21.0.0.0.0 Production on Fri Nov 13 22:12:47 2020
	Version 21.1.0.0.0
	Copyright (c) 1982, 2020, Oracle. All rights reserved.
	```
4. Enter your username and press Return. SQL\*Plus displays the prompt "Enter password:".
5. Enter your password and press Return again. For your protection, your password does not appear on the screen.
	The process of entering your username and password is called logging in. SQL\*Plus displays the version of Oracle Database to which you connected and the versions of available tools such as PL/SQL, and the local time of the last time you logged on.
	```
	SQL*Plus: Release 21.0.0.0.0 Production on Fri Nov 13 22:12:47 2020
	Version 21.1.0.0.0
	Copyright (c) 1982, 2020, Oracle. All rights reserved.
	Last Successful login time: Fri Nov 06 2020 23:35:38 -07:00
	Connected to:
	Oracle Database 21c Enterprise Edition Release 21.0.0.0.0 - 64bit Production
	```
	Next, SQL\*Plus displays the SQL\*Plus command prompt:
	```
	SQL>
	```
	The SQL\*Plus command prompt indicates that SQL\*Plus is ready to accept your commands.

If SQL\*Plus does not start, you should see a message to help you correct the problem.

Example 3-7 Starting SQL\*Plus

This example shows you how to start SQL\*Plus:

#### 3.3.2 About Getting Command-line Help

To access command-line help for SQL\*Plus commands, type HELP or? followed by the command name at the SQL command prompt or in the iSQL\*Plus Workspace Input area. See the [HELP](HELP.md) command for more information. For example:

```
HELP ACCEPT
```

To display a list of SQL\*Plus commands, type HELP followed by either TOPICS or INDEX. HELP TOPICS displays a single column list of SQL\*Plus commands. HELP INDEX displays a four column list of SQL\*Plus commands which fits in a standard screen. For example:

```
HELP INDEX
```

### 3.4 About Exiting SQL\*Plus Command-line

If you cannot log in to SQL\*Plus because your username or password is invalid or for some other reason, SQL\*Plus returns an error status equivalent to an EXIT FAILURE command. See the [EXIT](EXIT.md) command for further information.

When you are done working with SQL\*Plus and wish to return to the operating system, enter EXIT or QUIT at the SQL\*Plus prompt, or enter the end of file character, Ctrl+D on UNIX or Ctrl+Z on Windows.

SQL\*Plus displays the version of Oracle Database from which you disconnected and the versions of tools available through SQL\*Plus before you return to the operating system prompt.

### 3.5 SQL\*Plus Program Syntax

You use the SQLPLUS command at the operating system prompt to start command-line SQL\*Plus:

```
SQLPLUS [ [Options] [Logon|/NOLOG] [Start] ]
```

where: Options has the following syntax:

```
-H[ELP]|-V[ERSION]
|[[-C[OMPATIBILITY] {x.y[.z]] [–F[ast]] [-M[ARKUP] markup_option] [-L[OGON]] 
 [-NOLOGINTIME] [-R[ESTRICT] {1|2|3}] [-S[ILENT]]]
```

and markup\_option consists of:

- ```
	csv_option
	```
- ```
	html_option
	```

csv\_option has the following syntax:

```
CSV {ON|OFF} [DELIMI[TER] character] [QUOTE {ON|OFF}]
```

html\_option has the following syntax:

```
HTML [ON|OFF] [HEAD text] [BODY text] [TABLE text] [ENTMAP {ON|OFF}] [SPOOL {ON|OFF}] [PRE[FORMAT] {ON|OFF}]
```

where Logon has the following syntax:

```
{username[/password][@connect_identifier]| / } 
[AS {SYSASM|SYSBACKUP|SYSDBA|SYSDG|SYSOPER|SYSRAC|SYSKM}][edition=value]
```

where Start has the following syntax:

```
@{url|file_name[.ext]} [arg ...]
```

WARNING:

Including your password in plain text is a security risk. You can avoid this risk by omitting the password, and entering it only when the system prompts for it.

You have the option of entering logon. If you do not specify logon but do specify start, SQL\*Plus assumes that the first line of the script contains a valid logon. If neither start nor logon are specified, SQL\*Plus prompts for logon information.

#### 3.5.1 Options

The following sections contain descriptions of SQLPLUS command options:

##### 3.5.1.1 HELP Option

```
-H[ELP]
```

Displays the usage and syntax for the SQLPLUS command, and then returns control to the operating system.

##### 3.5.1.2 VERSION Option

```
-V[ERSION]
```

Displays the current version and level number for SQL\*Plus, and then returns control to the operating system.

##### 3.5.1.3 COMPATIBILITY Option

```
-C[OMPATIBILITY] {x.y[.z]
```

Sets the value of the SQLPLUSCOMPATIBILITY system variable to the SQL\*Plus release specified by x.y\[.z\]. Where x is the version number, y is the release number, and z is the update number. For example, 9.0.1 or 10.2. For more information, see the [SET SQLPLUSCOMPAT\[IBILITY\] {x.y\[.z\]}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-B78B8F90-AD6C-48CA-B0A8-D657F6FBFC38) system variable.

##### 3.5.1.4 LOGON Option

```
-L[OGON]
```

Specifies not to reprompt for username or password if the initial connection does not succeed. This can be useful in operating system scripts that must either succeed or fail and you don't want to be reprompted for connection details if the database server is not running.

##### 3.5.1.5 FAST Option

```
–F[ast]
```

The FAST option improves general performance. This command line option changes the values of the following default settings:

- ARRAYSIZE = 100
- LOBPREFETCH = 16384
- PAGESIZE = 50000
- ROWPREFETCH = 2
- STATEMENTCACHE = 20

##### 3.5.1.6 MARKUP Options

```
-M[ARKUP]
```

You can use the MARKUP options to generate output in HTML or CSV (Character Separated Values) format, through a query or script.

MARKUP currently supports HTML 4.0 transitional, and the CSV format.

Use SQLPLUS -MARKUP to produce output in HTML or CSV format.

Note:

Depending on your operating system, the complete markup\_option clause for the SQL\*PLUS command may need to be contained in quotes.

For HTML output, use SQLPLUS -MARKUP HTML ON or SQLPLUS -MARKUP HTML ON SPOOL ON to produce standalone web pages. SQL\*Plus will generate complete HTML pages automatically encapsulated with \<HTML> and \<BODY> tags. The HTML tags in a spool file are closed when SPOOL OFF is executed or SQL\*Plus exits.

The -SILENT and -RESTRICT command-line options may be useful when used in conjunction with -MARKUP.

You can use MARKUP HTML ON to produce HTML output in either the \<PRE> tag or in an HTML table. Output to a table uses standard HTML \<TABLE>, \<TR> and \<TD> tags to automatically encode the rows and columns resulting from a query. Output to an HTML table is the default behavior when the HTML option is set ON. You can generate output using HTML \<PRE> tags by setting PREFORMAT ON.

For CSV output, use SQLPLUS -MARKUP CSV ON to produce output in CSV format. You can specify the delimiter character by using the DELIMITER option. You can also output text without quotes by using QUOTE OFF.

Use the SHOW MARKUP command to view the status of MARKUP options.

The SQLPLUS -MARKUP command has the same functionality as the SET MARKUP command. These options are described in this section. For other information on the SET MARKUP command, see the [SET](SET.md) command.

```
CSV {ON|OFF}
```

CSV is a mandatory MARKUP argument which specifies that the type of output to be generated is CSV. The optional CSV arguments, ON and OFF, specify whether or not to generate CSV output. The default is OFF. You can turn CSV output ON and OFF as required during a session.

```
HTML {ON|OFF}
```

HTML is a mandatory MARKUP argument which specifies that the type of output to be generated is HTML. The optional HTML arguments, ON and OFF, specify whether or not to generate HTML output. The default is OFF.

MARKUP HTML ON generates HTML output using the specified MARKUP options.

You can turn HTML output ON and OFF as required during a session.

```
HEAD text
```

The HEAD text option enables you to specify content for the \<HEAD> tag. By default, text includes a default in-line cascading style sheet and title.

If text includes spaces, it must be enclosed in quotes. SQL\*Plus does not test this free text entry for HTML validity. You must ensure that the text you enter is valid for the HTML \<HEAD> tag. This gives you the flexibility to customize output for your browser or special needs.

```
BODY text
```

The BODY text option enables you to specify attributes for the \<BODY> tag. By default, there are no attributes. If text includes spaces, it must be enclosed in quotes. SQL\*Plus does not test this free text entry for HTML validity. You must ensure that the text you enter is valid for the HTML \<BODY> tag. This gives you the flexibility to customize output for your browser or special needs.

```
TABLE text
```

The TABLE text option enables you to enter attributes for the \<TABLE> tag. You can use TABLE text to set HTML \<TABLE> tag attributes such as BORDER, CELLPADDING, CELLSPACING and WIDTH. By default, the \<TABLE> WIDTH attribute is set to 90% and the BORDER attribute is set to 1.

If text includes spaces, it must be enclosed in quotes. SQL\*Plus does not test this free text entry for HTML validity. You must ensure that the text you enter is valid for the HTML \<TABLE> tag. This gives you the flexibility to customize output for your browser or special needs.

```
ENTMAP {ON|OFF}
```

ENTMAP ON or OFF specifies whether or not SQL\*Plus replaces special characters <, >, " and & with the HTML entities &lt;, &gt;, &quot; and &amp; respectively. ENTMAP is set ON by default.

You can turn ENTMAP ON and OFF as required during a session. For example, with ENTMAP OFF, SQL\*Plus screen output is:

```
SQL>PROMPT A > B
A > B
```

With ENTMAP ON, SQL\*Plus screen output is:

```
SQL&gt; PROMPT A > B
A &gt; B
```

As entities in the \<HEAD> and \<BODY> tags are not mapped, you must ensure that valid entities are used in the MARKUP HEAD and BODY options.

If entities are not mapped, web browsers may treat data as invalid HTML and all subsequent output may display incorrectly. ENTMAP OFF enables users to write their own HTML tags to customize output.

Note:

ENTMAP only takes effect when the HTML option is set ON. For more information about using entities in your output, see the [COLUMN](COLUMN.md) command.

```
SPOOL {ON|OFF}
```

SPOOL ON or OFF specifies whether or not SQL\*Plus writes the HTML opening tags, \<HTML> and \<BODY>, and the closing tags, \</BODY> and \</HTML>, to the start and end of each file created by the SQL\*Plus SPOOL filename command. The default is OFF.

You can turn SPOOL ON and OFF as required during a session.

Note:

It is important to distinguish between the SET MARKUP HTML SPOOL option, and the SQLPLUS SPOOL filename command.

The SET MARKUP HTML SPOOL ON option enables the writing of the \<HTML> tag to the spool file. The spool file is not created, and the header and footer tags enabled by the SET MARKUP HTML SPOOL ON option are not written to the spool file until you issue the SQLPLUS SPOOL filename command. See the [SPOOL](SPOOL.md) command for more information.

SQL\*Plus writes several HTML tags to the spool file when you issue the SPOOL filename command.

When you issue any of the SQL\*Plus commands: EXIT, SPOOL OFF or SPOOL filename, SQL\*Plus appends the following end tags and closes the file:

```
</BODY>
</HTML>
```

You can specify \<HEAD> tag contents and \<BODY> attributes using the HEAD and BODY options

```
PRE[FORMAT] {ON|OFF}
```

PREFORMAT ON or OFF specifies whether or not SQL\*Plus writes output to the \<PRE> tag or to an HTML table. The default is OFF, so output is written to a HTML table by default. You can turn PREFORMAT ON and OFF as required during a session.

Note:

To produce report output using the HTML \<PRE> tag, you must set PREFORMAT ON. For example:

`SQLPLUS -M "HTML ON PREFORMAT ON"`

or

`SET MARKUP HTML ON PREFORMAT ON`

##### 3.5.1.7 MARKUP Usage Notes

MARKUP HTML ON

When MARKUP HTML ON PREFORMAT OFF is used, commands originally intended to format paper reports have different meaning for reports intended for web tables:

- PAGESIZE is the number of rows in an HTML table, not the number of lines. Each row may contain multiple lines. The TTITLE, BTITLE and column headings are repeated every PAGESIZE rows.
- LINESIZE may have an effect on data if wrapping is on, or for very long data. Depending on data size, output may be generated on separate lines, which a browser may interpret as a space character.
- TTITLE and BTITLE content is output to three line positions: left, center and right, and the maximum line width is preset to 90% of the browser window. These elements may not align with the main output as expected due to the way they are handled for web output. Entity mapping in TTITLE and BTITLE is the same as the general ENTMAP setting specified in the MARKUP command.
- If you use a title in your output, then SQL\*Plus starts a new HTML table for output rows that appear after the title. Your browser may format column widths of each table differently, depending on the width of data in each column.
- SET COLSEP, RECSEP and UNDERLINE only produce output in HTML reports when PREFORMAT is ON.

MARKUP CSV ON

When MARKUP CSV ON is used, output from a query will be displayed in CSV format.

You can enable CSV markup while logging into a user session, by using the -M\[ARKUP\] CSV ON option at the SQL\*Plus command line. For more information, see SQL\*Plus Program Syntax. While logged in to a user session, you can enable CSV markup by using the SET MARKUP CSV ON command.

You can specify the delimiter character by using the DELIMITER option. You can also output text without quotes by using QUOTE OFF.

##### 3.5.1.8 No Login Time Option

```
-nologintime
```

The last login time for non-SYS users is displayed when you log on. This feature is on by default. The last login time is displayed in local time format. You can use the `-nologintime` option to disable this security feature. After you login, the last login information is displayed

```
SQL*Plus: Release 21.0.0.0.0 Production on Fri Nov 13 22:12:47 2020
Version 21.1.0.0.0

Copyright (c) 1982, 2020, Oracle. All rights reserved.

Last Successful login time: Fri Nov 06 2020 23:35:38 -07:00

Connected to:
Oracle Database 21c Enterprise Edition Release 21.0.0.0.0 - Production
Version 21.1.0.0.0
With the Partitioning, Oracle Label Security, Data Mining and Real Application
```

Last login time does not show when making a connection with the CONNECT command.

##### 3.5.1.9 RESTRICT Option

```
-R[ESTRICT] {1|2|3}
```

Enables you to disable certain commands that interact with the operating system. This is similar to disabling the same commands in the Product User Profile (PUP) table. However, commands disabled with the -RESTRICT option are disabled even if there is no connection to a server, and remain disabled until SQL\*Plus terminates.

If no -RESTRICT option is active, than all commands can be used, unless disabled in the PUP table.

If -RESTRICT 3 is used, then LOGIN.SQL is not read. GLOGIN.SQL is read but restricted commands used will fail.

Table 3-1 Commands Disabled by Restriction Level

| Command | Level 1 | Level 2 | Level 3 |
| --- | --- | --- | --- |
| EDIT | disabled | disabled | disabled |
| GET |  |  | disabled |
| HOST | disabled | disabled | disabled |
| SAVE |  | disabled | disabled |
| SPOOL |  | disabled | disabled |
| START, @, @@ |  |  | disabled |
| STORE |  | disabled | disabled |

##### 3.5.1.10 SILENT Option

```
-S[ILENT]
```

Suppresses all SQL\*Plus information and prompt messages, including the command prompt, the echoing of commands, and the banner normally displayed when you start SQL\*Plus. If you omit username or password, SQL\*Plus prompts for them, but the prompts are not visible! Use SILENT to invoke SQL\*Plus within another program so that the use of SQL\*Plus is invisible to the user.

SILENT is a useful mode for creating reports for the web using the SQLPLUS -MARKUP command inside a CGI script or operating system script. The SQL\*Plus banner and prompts are suppressed and do not appear in reports created using the SILENT option.

#### 3.5.2 Logon

```
username[/password]
```

Represent the username and password with which you wish to start SQL\*Plus and connect to Oracle Database.

WARNING:

Including your password in plain text is a security risk. You can avoid this risk by omitting the password, and entering it only when the system prompts for it.

If you omit username and password, SQL\*Plus prompts you for them. If you omit only password, SQL\*Plus prompts for it. In silent mode, username and password prompts are not visible! Your username appears when you type it, but not your password.

```
@connect_identifier
```

Consists of an Oracle Net connect identifier. The exact syntax depends upon the Oracle Net configuration. For more information, refer to the Oracle Net manual or contact your DBA.

```
edition=value
```

The value for the Oracle Edition. An edition enables two or more versions of an object in a database. It provides a staging area where changed objects can be loaded into the database, compiled, and executed during uptime. This is particularly useful to reduce downtime associated with patching an application. edition=value overrides any edition value specified in the ORA\_EDITION environment variable. For more detailed information, see [Using Edition-Based Redefinition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADFNS-GUID-58DE05A0-5DEF-4791-8FA8-F04D11964906).

```
/
```

Represents a default logon using operating system authentication. You cannot enter a connect identifier if you use a default logon. In a default logon, SQL\*Plus typically attempts to log you in using the username OPS$name, where name is your operating system username. Note that the prefix "OPS$" can be set to any other string of text. For example, you may wish to change the settings in your INIT.ORA parameters file to LOGONname or USERIDname. See [Using Operating System Authentication](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN-GUID-BB22E256-CC25-405F-A887-E3FA92CC37D4) for information about operating system authentication.

```
AS {SYSASM |SYSBACKUP |SYSDBA |SYSDG |SYSOPER |SYSRAC |SYSKM}
```

The AS clause enables privileged connections by users who have been granted SYSASM, SYSBACKUP, SYSDBA, SYSDG, SYSOPER, SYSRAC or SYSKM system privileges.

```
/NOLOG
```

Establishes no initial connection to Oracle Database. Before issuing any SQL commands, you must issue a CONNECT command to establish a valid logon. Use /NOLOG when you want to have a SQL\*Plus script prompt for the username, password, or database specification. The first line of this script is not assumed to contain a logon.

#### 3.5.3 Start

```
@{url|file_name[.ext]} [arg ...]
```

Specifies the name of a script and arguments to run. The script can be called from the local file system or from a web server.

SQL\*Plus passes the arguments to the script as if executing the file using the SQL\*Plus START command. If no file suffix (file extension) is specified, the suffix defined by the SET SUFFIX command is used. The default suffix is.sql.

See the [START](START.md) command for more information.