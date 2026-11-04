---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/double-at-sign.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
@@{url | file_name[.ext] } [arg...]
```

Runs a script. This command is almost identical to the @ (at sign) command. When running nested scripts it looks for nested scripts in the same path or url as the calling script. The @@ command functions similarly to @ and START.

Terms

```
url
```

Specifies the Uniform Resource Locator of a script to run on the specified web server. SQL\*Plus supports HTTP and FTP protocols, but not HTTPS. HTTP authentication in the form http://username:password@machine\_name.domain... is not supported in this release.

```
file_name[.ext]
```

Represents the nested script you wish to run. If you omit ext, SQL\*Plus assumes the default command-file extension (normally SQL). For information on changing the default extension, see [SET SUF\[FIX\] {SQL | text}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-0DFB3D8C-0389-4F44-A68D-3FDBB9F962EA).

When you enter @@file\_name.ext from within a script, SQL\*Plus runs file\_name.ext from the same directory as the script.

When you enter @@file\_name.ext interactively, SQL\*Plus runs file\_name.ext from the current working directory or from the same url as the script from which it was called. If SQL\*Plus does not find the file, it searches a system-dependent path to find the file. Some operating systems may not support the path search. See the platform-specific Oracle documentation provided for your operating system for specific information related to your operating system environment.

```
arg...
```

Represent data items you wish to pass to parameters in the script. If you enter one or more arguments, SQL\*Plus substitutes the values into the parameters (&1, &2, and so forth) in the script. The first argument replaces each occurrence of &1, the second replaces each occurrence of &2, and so forth.

The @@ command defines the parameters with the values given by the arguments. If you run the script again in this session, you can enter new arguments or omit the arguments to use the current values. For more information on using parameters, see [Using Substitution Variables](using-substitution-variables-sqlplus.md).

Usage

All previous settings like COLUMN command settings stay in effect when the script starts. If the script changes any setting, the new value stays in effect after the script has finished.

You can include in a script any command you would normally enter interactively (typically, SQL or SQL\*Plus commands).

If the START command is disabled (see [Disabling SQL\*Plus\_ SQL\_ and PL/SQL Commands](SQL-Plus-security.md)), this will also disable the @@ command. For more information, see the [SPOOL](SPOOL.md) command.

SQL\*Plus removes the SQLTERMINATOR (a semicolon by default) before the @@ command is issued. A workaround for this is to add another SQLTERMINATOR. See [SET SQLT\[ERMINATOR\] {; | c | ON | OFF}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-5D91A9A9-13A2-4F62-B02A-AD2F3AFF8BB7) for more information.

Examples

Suppose that you have the following script named PRINTRPT:

```
SELECT DEPARTMENT_ID, CITY FROM EMP_DETAILS_VIEW WHERE SALARY>12000;
@EMPRPT.SQL
@@ WKRPT.SQL
```

When you START PRINTRPT and it reaches the @ command, it looks for the script named EMPRPT in the current working directory and runs it. When PRINTRPT reaches the @@ command, it looks for the script named WKRPT in the same path as PRINTRPT and runs it.

Suppose that the same script PRINTRPT was located on a web server and you ran it with START HTTP://machine\_name.domain:port/PRINTRPT. When it reaches the @ command, it looks for the script named EMPRPT in the current working directory and runs it. When PRINTRPT reaches the @@ command, it looks for the script named WKRPT in the same url as PRINTRPT, HTTP://machine\_name.domain:port/WKRPT.SQL and runs it.