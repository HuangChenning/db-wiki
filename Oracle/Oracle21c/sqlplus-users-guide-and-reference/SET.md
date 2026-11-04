---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Sets a system variable to alter the SQL\*Plus environment settings for your current session, for example, to:

- customize HTML formatting
- enable or disable the printing of column headings
- set the number of lines per page
- set the display width for data

Syntax

```
SET system_variable value
```

where system\_variable and value represent one of the clauses shown in the [SET System Variable Summary](SET-system-variable-summary.md) table following.

Usage

SQL\*Plus maintains system variables (also called SET command variables) to enable you to set up a particular environment for a SQL\*Plus session. You can change these system variables with the SET command and list them with the SHOW command. The default value for each system variable is underlined in the following sections.

SET ROLE and SET TRANSACTION are SQL commands (see [SQL Statements: MERGE to UPDATE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=SQLRF-GUID-07BBB875-6272-441A-893F-35E2F9CA58ED) for more information). When not followed by the keywords TRANSACTION or ROLE, SET is assumed to be a SQL\*Plus command.