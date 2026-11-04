---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/START.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
STA[RT] {url | file_name[.ext] } [arg...]
```

Runs the SQL\*Plus statements in the specified script. The script can be called from the local file system or from a web server.

Terms

```
url
```

Specifies the Uniform Resource Locator of a script to run on the specified web server. SQL\*Plus supports HTTP and FTP protocols, but not HTTPS. HTTP authentication in the form http://username:password@machine\_name.domain... is not supported in this release.

```
file_name[.ext]
```

The script you wish to execute. The file can contain any command that you can run interactively.

If you do not specify an extension, SQL\*Plus assumes the default command-file extension (normally SQL). See [SET SUF\[FIX\] {SQL | text}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-0DFB3D8C-0389-4F44-A68D-3FDBB9F962EA) for information on changing the default extension.

When you enter START file\_name.ext, SQL\*Plus searches for a file with the filename and extension you specify in the current default directory. If SQL\*Plus does not find such a file, SQL\*Plus will search a system-dependent path to find the file. Some operating systems may not support the path search. See the platform-specific Oracle documentation provided for your operating system for specific information related to your operating system environment.

```
arg ...
```

Data items you wish to pass to parameters in the script. If you enter one or more arguments, SQL\*Plus substitutes the values into the parameters (&1, &2, and so forth) in the script. The first argument replaces each occurrence of &1, the second replaces each occurrence of &2, and so on.

The START command defines the parameters with the values of the arguments; if you START the script again in this session, you can enter new arguments or omit the arguments to use the old values.

See [Defining Substitution Variables](using-substitution-variables-sqlplus.md) and [Using Substitution Variables](using-substitution-variables-sqlplus.md) for more information on using parameters.

Usage

All previous settings like COLUMN command settings stay in effect when the script starts. If the script changes any setting, then this new value stays in effect after the script has finished

The @ (at sign) and @@ (double at sign) commands function similarly to START. Disabling the START command in the Product User Profile also disables the @ and @@ commands. See [@ (at sign)](at-sign.md) and [@@ (double at sign)](double-at-sign.md) for further information on these commands. See [Disabling SQL\*Plus\_ SQL\_ and PL/SQL Commands](SQL-Plus-security.md) for more information.

The EXIT or QUIT command in a script terminates SQL\*Plus.

Examples

A file named PROMOTE with the extension SQL, used to promote employees, might contain the following command:

```
SELECT FIRST_NAME, LAST_NAME, JOB_ID, SALARYFROM EMP_DETAILS_VIEWWHERE JOB_ID='&1' AND SALARY>&2;
```

To run this script, enter

```
START PROMOTE ST_MAN 7000
```

or if it is located on a web server, enter a command in the form:

```
START HTTP://machine_name.domain:port/PROMOTE.SQL ST_MAN 7000
```

Where machine\_name.domain must be replaced by the host.domain name, and port by the port number used by the web server where the script is located.

The following command is executed:

```
SELECT LAST_NAME, LAST_NAME
FROM EMP_DETAILS_VIEW
WHERE JOB_ID='ST_MAN' AND SALARY>7000;
```

and the results displayed.