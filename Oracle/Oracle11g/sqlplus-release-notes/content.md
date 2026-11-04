---
title: "SQL*Plus® Release Notes"
book: "SQL*Plus Release Notes"
doc_id: E16608-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/relnotes.112/e16608/toc.htm
tags:
  - oracle
  - 11g
  - sqlplus-release-notes
---

## SQL\*Plus®

Release Notes

Release 11.2.0.4

E16608-03

## About these Release Notes

This document summarizes requirements, differences between SQL\*Plus and its documented functionality, new features in this release and support information.

It contains the following topics:

## Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility Program website at `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc`.

Access to Oracle Support

Oracle customers have access to electronic support through My Oracle Support. For information, visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info` or visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs` if you are hearing impaired.

## Certification

SQL\*Plus is certified against the operating systems set out in the operating-system specific Oracle Database documentation.

SQL\*Plus is certified against Oracle Database 11g Release 2 (11.2) and all supported versions of the Oracle Server.

## New Features in SQL\*Plus

SQL\*Plus Release 11.2.0.4 is a superset of SQL\*Plus Release 11.2.

This section describes new features introduced in this release of SQL\*Plus. Some features may be affected by the SQLPLUSCOMPATIBILITY setting. See the SET SQLPLUSCOMPATIBILITY Matrix in chapter 12, "SQL\*Plus Command Reference" in the [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/toc.htm).

### SET XMLOPTIMIZATIONCHECK

SET XMLOPTIMIZATIONCHECK specifies that only fully optimized XML queries and DML operations are executed. It is only to assist during code development and debugging.

## New Features in Previous Releases

This section lists new features introduced to SQL\*Plus in previous releases.

### New Features in SQL\*Plus 11.2 Production

- Editions Option
- SET EXITCOMMIT
- FAILOVER Option removed. FAN Events in a RAC Database are now permanently enabled on UNIX/Linux.

### New Features in SQL\*Plus 11.1 Production

- SET ERRORLOGGING command enables error logging of SQL, PL/SQL and SQL\*Plus errors.
- SQL\*Plus supports standard querying of tables and objects containing BLOB and BFILE datatypes.
- SET ESCCHAR command enables specific characters in file names to be escaped.
- The SQLPLUS command -F argument enables SQL\*Plus to receive FAN events from a RAC database.

## Bugs Fixed

The following section lists bugs fixed in SQL\*Plus. Numbers in parentheses following the problem description refer to bug numbers in the Oracle Bug Database.

### Bugs Fixed in SQL\*Plus Release 11.2.0.4

- SQL\*PLUS no longer raises SP2-0575 during CONNECT when ADG STANDBY SLA is violated (10143882)WHENEVER SQLERROR no longer exits SQLPLUS when an error occurs (13068233)
- SPERRORLOG now logs SQL statements greater than 4,000 characters (13078263)
- PS in AIX now shows arguments for SQLPLUS (13452339)
- Output of HELP SHO\[W\] option fixed (14115987)
- SP2-1503 starting SQLPLUS with "ORAACCESS.XML" (14257546)
- SQL\*PLUS now throws 28000: ACCOUNT LOCKED ERROR (15921394)
- SQL\*PLUS SELECT on OS X now behaves normally (16371259)
- SET ERRORLOGGING now supports exotic error log table names (16735202)
- SPERRORLOG ENTRIES now correctly handle single/double quotes (16734585)
- ERRORLOGGING now handles long strings (16823442)
- Internal changes: (10177235, 12728137, 4431998, 16734434, 16734526)

## Support

For SQL\*Plus support, please contact your local Oracle Support Services Center.

## Desupport Notices

This section gives advance notice of the desupport of SQL\*Plus commands and interfaces. It is not official notice of desupport dates, nor is it intended to replace the Oracle obsolescence process. This information provides you with advance warning that Oracle Corporation intends to desupport these features/interfaces in upcoming releases.

### Windows Graphical User Interface

The SQL\*Plus for Windows graphical user interface (GUI) was desupported in SQL\*Plus Release 11.1. In Oracle Database 11g Release 1 (11.1) or later, Oracle recommends using one of the following:

- SQL\*Plus command line
- Oracle Application Express
- Oracle SQL Developer

### iSQL\*Plus User Interface

The iSQL\*Plus user interface was desupported in SQL\*Plus Release 11.1. In Oracle Database 11g Release 1 (11.1) or later, Oracle recommends using one of the following:

- SQL\*Plus command line
- Oracle Application Express
- Oracle SQL Developer

---

SQL\*Plus Release Notes, Release 11.2.0.4

E16608-03

Copyright © 1996, 2013, Oracle and/or its affiliates. All rights reserved.

This software and related documentation are provided under a license agreement containing restrictions on use and disclosure and are protected by intellectual property laws. Except as expressly permitted in your license agreement or allowed by law, you may not use, copy, reproduce, translate, broadcast, modify, license, transmit, distribute, exhibit, perform, publish, or display any part, in any form, or by any means. Reverse engineering, disassembly, or decompilation of this software, unless required by law for interoperability, is prohibited.

The information contained herein is subject to change without notice and is not warranted to be error-free. If you find any errors, please report them to us in writing.

If this is software or related documentation that is delivered to the U.S. Government or anyone licensing it on behalf of the U.S. Government, the following notice is applicable:

U.S. GOVERNMENT END USERS: Oracle programs, including any operating system, integrated software, any programs installed on the hardware, and/or documentation, delivered to U.S. Government end users are "commercial computer software" pursuant to the applicable Federal Acquisition Regulation and agency-specific supplemental regulations. As such, use, duplication, disclosure, modification, and adaptation of the programs, including any operating system, integrated software, any programs installed on the hardware, and/or documentation, shall be subject to license terms and license restrictions applicable to the programs. No other rights are granted to the U.S. Government.

This software or hardware is developed for general use in a variety of information management applications. It is not developed or intended for use in any inherently dangerous applications, including applications that may create a risk of personal injury. If you use this software or hardware in dangerous applications, then you shall be responsible to take all appropriate fail-safe, backup, redundancy, and other measures to ensure its safe use. Oracle Corporation and its affiliates disclaim any liability for any damages caused by use of this software or hardware in dangerous applications.

Oracle and Java are registered trademarks of Oracle and/or its affiliates. Other names may be trademarks of their respective owners.

Intel and Intel Xeon are trademarks or registered trademarks of Intel Corporation. All SPARC trademarks are used under license and are trademarks or registered trademarks of SPARC International, Inc. AMD, Opteron, the AMD logo, and the AMD Opteron logo are trademarks or registered trademarks of Advanced Micro Devices. UNIX is a registered trademark of The Open Group.

This software or hardware and documentation may provide access to or information on content, products, and services from third parties. Oracle Corporation and its affiliates are not responsible for and expressly disclaim all warranties of any kind with respect to third-party content, products, and services. Oracle Corporation and its affiliates will not be responsible for any loss, costs, or damages incurred due to your access to or use of third-party content, products, or services.