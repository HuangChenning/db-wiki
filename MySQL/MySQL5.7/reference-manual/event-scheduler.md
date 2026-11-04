---
title: "23.4 Using the Event Scheduler"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/event-scheduler.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

The MySQL Event Scheduler manages the scheduling and execution of events, that is, tasks that run according to a schedule. The following discussion covers the Event Scheduler and is divided into the following sections:

- [Section 23.4.1, “Event Scheduler Overview”](events-overview.md), provides an introduction to and conceptual overview of MySQL Events.
- [Section 23.4.3, “Event Syntax”](events-syntax.md), discusses the SQL statements for creating, altering, and dropping MySQL Events.
- [Section 23.4.4, “Event Metadata”](events-metadata.md), shows how to obtain information about events and how this information is stored by the MySQL Server.
- [Section 23.4.6, “The Event Scheduler and MySQL Privileges”](events-privileges.md), discusses the privileges required to work with events and the ramifications that events have with regard to privileges when executing.

Stored routines require the `event` table in the `mysql` database. This table is created during the MySQL 5.7 installation procedure. If you are upgrading to MySQL 5.7 from an earlier version, be sure to update your grant tables to make sure that the `event` table exists. See [Section 2.10, “Upgrading MySQL”](upgrading.md).

### Additional Resources

- There are some restrictions on the use of events; see [Section 23.8, “Restrictions on Stored Programs”](stored-program-restrictions.md).
- Binary logging for events takes place as described in [Section 23.7, “Stored Program Binary Logging”](stored-programs-logging.md).
- You may also find the [MySQL User Forums](https://forums.mysql.com/list.php?20) to be helpful.