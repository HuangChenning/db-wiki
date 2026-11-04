---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SQL-Plus-security.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

This chapter describes the available methods for controlling access to database tables, and SQL\*Plus commands. It covers the following topics:

### 10.1 Disabling SQL\*Plus, SQL, and PL/SQL Commands

Note:

Starting with Oracle Database 19c, the SQL\*Plus table PRODUCT\_USER\_PROFILE (PUP table) is desupported. Oracle recommends that you protect data by using Oracle Database settings, so that you ensure consistent security across all client applications.

To disable a SQL or SQL\*Plus command for a given user, insert a row containing the user's username in the Userid column, the command name in the Attribute column, and DISABLED in the Char\_Value column. The Scope, Numeric\_Value, and Date\_Value columns should contain NULL. For example:

```
PRODUCT    USERID  ATTRIBUTE  SCOPE   NUMBERIC    CHAR       DATE    LONG
                                      VALUE       VALUE      VALUE   VALUE
-------    ------  ---------  -----   --------    ------     -----   -----
SQL*Plus   HR      HOST                           DISABLED
SQL*Plus   %       INSERT                         DISABLED
SQL*Plus   %       UPDATE                         DISABLED
SQL*Plus   %       DELETE                         DISABLED
```

To re-enable commands, delete the row containing the restriction.

SQL\*Plus commands that can be disabled:

- ACCEPT
- DEFINE
- PASSWORD
- SHUTDOWN
- APPEND
- DEL
- PAUSE
- SPOOL
- ARCHIVE LOG
- DESCRIBE
- PRINT
- START (@, @@)
- ATTRIBUTE
- DISCONNECT
- PROMPT
- STARTUP
- BREAK
- EDIT
- RECOVER
- STORE
- BTITLE
- EXECUTE
- REMARK
- TIMING
- CHANGE
- EXIT/QUIT
- REPFOOTER
- TTITLE
- CLEAR
- GET
- REPHEADER
- UNDEFINE
- COLUMN
- HELP (?)
- RUN
- VARIABLE
- COMPUTE
- HOST
- SAVE
- WHENEVER OSERROR
- CONNECT
- INPUT
- SET
- WHENEVER SQLERROR
- COPY
- LIST (;)
- SHOW
- XQUERY

SQL commands that can be disabled:

- ALTER
- ANALYZE
- ASSOCIATE
- AUDIT
- CALL