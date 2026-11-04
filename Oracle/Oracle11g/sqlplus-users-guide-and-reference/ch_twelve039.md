---
title: SET
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve039.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Sets a system variable to alter the SQL\*Plus environment settings for your current session, for example, to:

- customize HTML formatting
- enable or disable the printing of column headings
- set the number of lines per page
- set the display width for data

Syntax

SET system\_variable value

where system\_variable and value represent one of the clauses shown in the [SET System Variable Summary](ch_twelve040.md) table following.

Usage

SQL\*Plus maintains system variables (also called SET command variables) to enable you to set up a particular environment for a SQL\*Plus session. You can change these system variables with the SET command and list them with the SHOW command.

SET ROLE and SET TRANSACTION are SQL commands (see the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for more information). When not followed by the keywords TRANSACTION or ROLE, SET is assumed to be a SQL\*Plus command.