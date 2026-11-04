---
title: XQUERY
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve053.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

XQUERY xquery\_statement

The SQL\*Plus XQUERY command enables you to perform an XQuery 1.0 query on a specified database. XQUERY is supported on Oracle Database 10g (Release 2) and later versions. Attempting to use XQUERY on an earlier version of the Oracle Database gives the error:

```
SP2-614 Server version too low
```

Terms

xquery\_statement

Specifies the XQuery statement you want to run. The statement is entered with standard XQuery syntax. The XQUERY statement is terminated with a forward slash, '/'.

Usage

Prefix your XQuery statement with the SQL\*Plus command, XQUERY, and terminate the XQUERY command with a slash (/). XQUERY is a SQL\*Plus keyword. If XQueries are executed in other tools, the keyword may not be needed.

XML output from the XQUERY command is displayed as native XML according to the active SET command options. SET LONG typically needs to be set. It may be useful to consider the following settings:

- Linesize for rows longer than the default 80 characters (SET LINESIZE).
- LOB, LONG and XML Type Size for rows longer than the default 80 characters (SET LONG).
- Output Page Setup to match output (SET PAGESIZE).
- Display Headings to repress the "Result Sequence" column heading (SET HEADING OFF).

The XQUERY command requires an active database connection. The command will not work with SQLPLUS /NOLOG.

Bind variables are not supported in the XQUERY command.

There are four SET commands specific to the XQUERY command. The SHOW XQUERY command gives the status of these settings. They are:

Table 12-7 XQUERY SET commands

| SET Command |
| --- |
| SET XQUERY BASEURI |
| SET XQUERY ORDERING |
| SET XQUERY NODE |
| SET XQUERY CONTEXT |

For more information about the SET XQUERY commands, see:

- [SET XQUERY BASEURI {text}](ch_twelve040.md)
- [SET XQUERY ORDERING {UNORDERED | ORDERED | DEFAULT}](ch_twelve040.md)
- [SET XQUERY NODE {BYVALUE | BYREFERENCE | DEFAULT}](ch_twelve040.md)
- [SET XQUERY CONTEXT {text}](ch_twelve040.md)

Examples

The XQuery statement in the following script queries the EMP\_DETAILS\_VIEW view of the HR schema:

```
set long 160
set linesize 160
xquery for $i in ora:view("EMP_DETAILS_VIEW") return $i
/
```

```
Result Sequence
-------------------------------------------------------------------------------------------
<ROW><EMPNO>7369</EMPNO><ENAME>SMITH</ENAME><JOB>CLERK</JOB><MGR>7902</MGR><HIREDATE>17-
DEC-80</HIREDATE><SAL>800</SAL><DEPTNO>20</DEPTNO></ROW>

14 item(s) selected.
```