---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/at-sign.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
@{url | file_name[.ext] } [arg...]
```

Runs the SQL\*Plus statements in the specified script. The script can be called from the local file system or from a web server.

The @ command functions similarly to @@ and START.

Terms

```
url
```

Specifies the Uniform Resource Locator of a script to run on the specified web server. SQL\*Plus supports HTTP and FTP protocols, but not HTTPS. HTTP authentication in the form http://username:password@machine\_name.domain... is not supported in this release.

```
file_name[.ext]
```

Represents the script you wish to run. If you omit ext, SQL\*Plus assumes the default command-file extension (normally SQL). For information on changing the default extension, see [SET SUF\[FIX\] {SQL | text}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-0DFB3D8C-0389-4F44-A68D-3FDBB9F962EA).

When you enter @file\_name.ext, SQL\*Plus searches for a file with that filename and extension in the current default directory. If SQL\*Plus does not find the file in the current directory, it searches a system-dependent path to find it. Some operating systems may not support the path search. See the platform-specific Oracle documentation provided for your operating system for specific information related to your operating system environment.

```
arg...
```

Represent data items you wish to pass to parameters in the script. If you enter one or more arguments, SQL\*Plus substitutes the values into the parameters (&1, &2, and so forth) in the script. The first argument replaces each occurrence of &1, the second replaces each occurrence of &2, and so forth.

The @ command defines the parameters with the values given by the arguments; if you run the script again in this session, you can enter new arguments or omit the arguments to use the current values. For more information on using parameters, see [Using Substitution Variables](using-substitution-variables-sqlplus.md).

Usage

All previous settings like COLUMN command settings stay in effect when the script starts. If the script changes any setting, this new value stays in effect after the script has finished.

You can include in a script any command you would normally enter interactively (typically, SQL, SQL\*Plus commands, or PL/SQL blocks).

If the START command is disabled (see [Disabling SQL\*Plus\_ SQL\_ and PL/SQL Commands](SQL-Plus-security.md)), this will also disable the @ command. See [START](START.md) for information on the START command.

SQL\*Plus removes the SQLTERMINATOR (a semicolon by default) before the @ command is issued. If you require a semicolon in your command, add a second SQLTERMINATOR. See [SET SQLT\[ERMINATOR\] {; | c | ON | OFF}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-5D91A9A9-13A2-4F62-B02A-AD2F3AFF8BB7) for more information.

Examples

To run a script named PRINTRPT with the extension SQL, enter

```
@PRINTRPT
```

To run a script named WKRPT with the extension QRY, enter

```
@WKRPT.QRY
```

You can run a script named YEAREND specified by a URL, and pass values to variables referenced in YEAREND in the usual way:

```
@HTTP://machine_name.domain:port/YEAREND.SQL VAL1 VAL2
@FTP://machine_name.domain:port/YEAREND.SQL  VAL1 VAL2
```

On a web server configured to serve SQL reports, you could request SQL\*Plus to execute a dynamic script with:

```
@HTTP://machine_name.domain:port/SCRIPTSERVER?ENDOFYEAR VAL1 VAL2
```