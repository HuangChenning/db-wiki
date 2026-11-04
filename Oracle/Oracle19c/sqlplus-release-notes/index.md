---
title: Release Notes
book: "SQL*Plus Release Notes"
doc_id: E96455-02
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqprn/index.html
tags:
  - oracle
  - 19c
  - sqlplus-release-notes
---

Release Notes

19c

E96455-02

### About these Release Notes

This document summarizes requirements, differences between SQL\*Plus and its documented functionality, new features in this release and support information.

It contains the following topics:

### Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility Program website at [`http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc`](http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc).

Access to Oracle Support

Oracle customers have access to electronic support through My Oracle Support. For information, visit [`http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info`](http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info) or visit [`http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs`](http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs) if you are hearing impaired.

### Certification

SQL\*Plus is certified against the operating systems set out in the operating-system specific Oracle Database documentation.

SQL\*Plus is certified against Oracle Database 18c and all supported versions of the Oracle Server.

### New Features in SQL\*Plus Release 19c

This section describes new features introduced in SQL\*Plus in 19c.

New Features

- The Easy Connect syntax, used by applications to connect to Oracle Database, has been enhanced and is called Easy Connect Plus.

Desupported Features

- Desupport of `PRODUCT_USER_PROFILE` Table
	Starting in Oracle Database 19c, the SQL\*Plus table PRODUCT\_USER\_PROFILE (PUP table) is desupported.
	The SQL\*Plus product-level security feature is unavailable in Oracle Database 19c. Oracle recommends that you protect data by using Oracle Database settings, so that you ensure consistent security across all client applications.

### New Features in SQL\*Plus Release 18c, Version 18.3

There are no new features for this release.

Deprecated Features

- Deprecation of `PRODUCT_USER_PROFILE` Table
	Starting in Oracle Database 18c, the SQL\*Plus table ` PRODUCT_USER_PROFILE` (PUP) table is deprecated.
	The only use for the `PRODUCT_USER_PROFILE` (PUP) table is to provide a mechanism to control product-level security for SQL\*Plus. Starting with Oracle Database 18c, this mechanism is no longer relevant. This SQL\*Plus product-level security feature will be unavailable in Oracle Database 19c. Oracle recommends that you protect data by using Oracle Database settings, so that you ensure consistent security across all client applications.

### New Features in SQL\*Plus Release 18c, Version 18.1

This section describes new features introduced in SQL\*Plus in 18c.

- Display the sql\_id for a query
	Support for SET FEEDBACK command to display the sql\_id for a query. A new SQL\_ID option for the SET FEEDBACK command displays the sql\_id for the currently executed SQL or PL/SQL statements. The sql\_id will be assigned to the predefined variable \_SQL\_ID.
- Set the number of rows displayed for a query
	The SET ROWLIMIT command enables users to set a limit for the number of rows displayed for a query.
- Dynamically change the output display to fit the screen size
	The SET LINESIZE command has a WINDOW option to automatically change the linesize and pagesize for the formatted output according to the width and height of the screen.

### New Features in Previous Releases

This section lists new features introduced in SQL\*Plus in previous releases.

#### New Features in SQL\*Plus 12.2.0.1.0 Production

SQL\*Plus Release 12.2.0.1 is a superset of SQL\*Plus Release 12.1.

This section describes new features introduced in this release of SQL\*Plus. Some features may be affected by the SQLPLUSCOMPATIBILITY setting. See the SET SQLPLUSCOMPATIBILITY Matrix in chapter 12, "SQL\*Plus Command Reference" in the [SQL\*Plus User's Guide and Reference.](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqprn&id=SQPUG)

- Support for Command History
	The command history feature enables users to run, edit, or delete previously used SQL\*Plus, SQL, or PL/SQL commands from the history list in the current session.
- Support for long Identifiers
	SQL\*Plus supports object lengths of 128 bytes. In previous releases, the object length limit was 30 bytes.
- Commands to improve performance
	SET LOBPREF\[ETCH\], SET ROWPREF\[ETCH\], and SET STATEMENTC\[ACHE\] are new commands that enable users to control row and LOB prefetching, as well as statement caching.
- New Administrative Privilege
	The SQLPLUS and CONNECT commands support the new user privilege SYSRAC as well as the existing SYSBACKUP |SYSDG |SYSKM |SYSASM |SYSDBA |SYSOPER privileges.
- Support for Input Binding
	The VARIABLE command supports input binding which can be used in SQL and PL/SQL statements.
- Support for Extracting Data in CSV Format
	The SET MARKUP command supports the display of data in CSV format.
- Support for Suppressing Data Returned by a Query
	The ONLY option for the SET FEEDBACK command suppresses display of data returned by the query. The number of rows selected and returned by the query is displayed.
- Support for Application Continuity
	The SQL\*Plus command-line option –AC enables Application Continuity in a session. For more information about Application Continuity, see the Oracle Call Interface Programmer's Guide.
- General Performance Improvement
	SQL\*Plus command-line option –F\[ast\] improves general performance.

#### New Features in SQL\*Plus 12.1 Production

### Known Problem

Bug 24602051 - STARTUP OPEN RESTRICTED should return a syntax error when connecting to the Application container root. Instead it results in the PDB opening in normal mode.

Work Around: Use STARTUP OPEN RESTRICT or ALTER PLUGGABLE DATABASE \<pdb name> OPEN RESTRICTED.

### Bugs Fixed

The following section lists bugs fixed in SQL\*Plus. Numbers in parentheses following the problem description refer to bug numbers in the Oracle Bug Database.

#### Bugs Fixed in SQL\*Plus Release 18c, Version 18.1

- Using the invalid option RESTRICTED in the STARTUP command will now return an error when connecting to the Application container root (24602051).
- SET FEEDBACK ONLY will now have the same setting as the -F\[ast\] command-line option (24642116).
- SQL\*Plus no longer crashes when describing DBMS packages (25097640).
- Querying the long data column in a Multibyte character set now displays the correct error message when incomplete data is returned (25668186).
- SQL\*Plus now handles leading comments correctly (17419163).
- SQL\*Plus Instant Client no longer leaks memory (25127228).
- Passing the directory path as an argument to a file works now(25699321).
- SQL\*Plus now observes SQLPATH in the registry or as an environment variable for login.sql on Windows (25804573).
- The SQLPATH environment variable can now hold more than 256 characters (25997107).
- DBMS\_OUTPUT.PUT\_LINE now returns the value correctly (26163790).
- Internal fixes (25361890, 25390622, 25475326, 25475334)

#### Bugs Fixed in SQL\*Plus 12.2.0.1.0 Production

- SQL\*Plus no longer throws ORA-1005 error when a user name that contains double quotes (") is specified while using the Password command (17613757)
- SQL\*Plus no longer crashes when compiling a package body with errors if the name of the "object" specified in the command line is greater than 46 characters (18389912)
- Long column names are no longer displayed as junk characters in the table description (20453052)
- Using the "force" option to create views after altering the session's NLS\_SORT parameter no longer causes a crash (20592522)
- Internal fixes (17830524, 17847776, 18925904, 19655924, 19674161, 19953173, 21609521)

#### Bugs Fixed in SQL\*Plus Release 12.1

- SQL\*Plus now correctly executes a sql script that contains a WHENEVER SQLERROR EXIT clause (10375866)
- SPERRORLOG now displays entire statement (9559937)
- SQL\*Plus commands now display correctly in PRODUCT\_USER\_PROFILE (9298298)
- SHUTDOWN IMMEDIATE no longer hangs after session becomes defunct (8299200)
- INSERT now correctly reports all rows inserted (7047565)
- Internal fixes (9587813, 9575131, 8832471, 8670263, 8244438, 7629280, 6862613)

### Support

For SQL\*Plus support, contact your local Oracle Support Services Center.

---

SQL\*Plus Release Notes, 19c

E96455-02

Copyright © 1996, 2019, Oracle and/or its affiliates. All rights reserved.

This software and related documentation are provided under a license agreement containing restrictions on use and disclosure and are protected by intellectual property laws. Except as expressly permitted in your license agreement or allowed by law, you may not use, copy, reproduce, translate, broadcast, modify, license, transmit, distribute, exhibit, perform, publish, or display any part, in any form, or by any means. Reverse engineering, disassembly, or decompilation of this software, unless required by law for interoperability, is prohibited.

The information contained herein is subject to change without notice and is not warranted to be error-free. If you find any errors, please report them to us in writing.

If this is software or related documentation that is delivered to the U.S. Government or anyone licensing it on behalf of the U.S. Government, then the following notice is applicable:

U.S. GOVERNMENT END USERS: Oracle programs, including any operating system, integrated software, any programs installed on the hardware, and/or documentation, delivered to U.S. Government end users are "commercial computer software" pursuant to the applicable Federal Acquisition Regulation and agency-specific supplemental regulations. As such, use, duplication, disclosure, modification, and adaptation of the programs, including any operating system, integrated software, any programs installed on the hardware, and/or documentation, shall be subject to license terms and license restrictions applicable to the programs. No other rights are granted to the U.S. Government.

This software or hardware is developed for general use in a variety of information management applications. It is not developed or intended for use in any inherently dangerous applications, including applications that may create a risk of personal injury. If you use this software or hardware in dangerous applications, then you shall be responsible to take all appropriate fail-safe, backup, redundancy, and other measures to ensure its safe use. Oracle Corporation and its affiliates disclaim any liability for any damages caused by use of this software or hardware in dangerous applications.

Oracle and Java are registered trademarks of Oracle and/or its affiliates. Other names may be trademarks of their respective owners.

Intel and Intel Xeon are trademarks or registered trademarks of Intel Corporation. All SPARC trademarks are used under license and are trademarks or registered trademarks of SPARC International, Inc. AMD, Opteron, the AMD logo, and the AMD Opteron logo are trademarks or registered trademarks of Advanced Micro Devices. UNIX is a registered trademark of The Open Group.

This software or hardware and documentation may provide access to or information about content, products, and services from third parties. Oracle Corporation and its affiliates are not responsible for and expressly disclaim all warranties of any kind with respect to third-party content, products, and services unless otherwise set forth in an applicable agreement between you and Oracle. Oracle Corporation and its affiliates will not be responsible for any loss, costs, or damages incurred due to your access to or use of third-party content, products, or services, except as set forth in an applicable agreement between you and Oracle.