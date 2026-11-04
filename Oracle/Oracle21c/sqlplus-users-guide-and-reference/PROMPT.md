---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/PROMPT.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
PRO[MPT] [text]
```

where text represents the text of the message you want to display.

Sends the specified message or a blank line to the user's screen. If you omit text, PROMPT displays a blank line on the user's screen.

Usage

You can use this command in scripts to give information to the user.

Examples

The following example shows the use of PROMPT in conjunction with ACCEPT in a script called ASKFORDEPT.SQL. ASKFORDEPT.SQL contains the following SQL\*Plus and SQL commands:

```
PROMPTPROMPT Please enter a valid departmentPROMPT For example:  10SELECT DEPARTMENT_NAME FROM EMP_DETAILS_VIEWWHERE DEPARTMENT_ID = &NEWDEPT
```

Assume you run the file using START or @:

```
@ASKFORDEPT.SQL VAL1
@HTTP://machine_name.domain:port/ASKFORDEPT.SQL VAL1
```
```
Please enter a valid department
For example: 10
Department ID?>
```

You can enter a department number at the prompt Department ID?>. By default, SQL\*Plus lists the line containing &NEWDEPT before and after substitution, and then displays the department name corresponding to the number entered at the Department ID?> prompt. You can use SET VERIFY OFF to prevent this behavior.