---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/ARCHIVE-LOG.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
ARCHIVE LOG LIST
```

Displays information about redo log files.

Terms

```
LIST
```

Requests a display that shows the range of redo log files to be archived, the current log file group's sequence number, and the current archive destination (specified by either the optional command text or by the initialization parameter LOG\_ARCHIVE\_DEST).

If you are using both ARCHIVELOG mode and automatic archiving, the display might appear like:

```
ARCHIVE LOG LIST

Database log mode              Archive Mode
Automatic archival             Enabled
Archive destination            /vobs/oracle/dbs/arch
Oldest online log sequence     221
Next log sequence to archive   222
Current log sequence           222
```

Since the log sequence number of the current log group and the next log group to archive are the same, automatic archival has archived all log groups up to the current one.

If you are using ARCHIVELOG but have disabled automatic archiving, the last three lines might look like:

```
Oldest online log sequence            222
Next log sequence to archive          222
Current log sequence                  225
```

If you are using NOARCHIVELOG mode, the "next log sequence to archive" line is suppressed.

The log sequence increments every time the Log Writer begins to write to another redo log file group; it does not indicate the number of logs being used. Every time an online redo log file group is reused, the contents are assigned a new log sequence number.

Usage

You must be connected to an open Oracle database as SYSOPER, or SYSDBA. For information about connecting to the database, see the [CONNECT](CONNECT.md) command.

For information about specifying archive destinations, see your platform-specific Oracle Database documentation.

Note:

ARCHIVE LOG LIST only applies to the current instance. To START and STOP archiving, use the SQL command ALTER SYSTEM. For more information about using SQL commands, see the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=SQLRF).