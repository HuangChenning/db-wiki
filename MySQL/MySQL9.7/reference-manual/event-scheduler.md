---
title: "27.5 Using the Event Scheduler"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/event-scheduler.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

The MySQL Event Scheduler manages the scheduling and execution of events, that is, tasks that run according to a schedule. The following discussion covers the Event Scheduler and is divided into the following sections:

- [Section 27.5.1, “Event Scheduler Overview”](events-overview.md), provides an introduction to and conceptual overview of MySQL Events.
- [Section 27.5.3, “Event Syntax”](events-syntax.md), discusses the SQL statements for creating, altering, and dropping MySQL Events.
- [Section 27.5.4, “Event Metadata”](events-metadata.md), shows how to obtain information about events and how this information is stored by the MySQL Server.
- [Section 27.5.6, “The Event Scheduler and MySQL Privileges”](events-privileges.md), discusses the privileges required to work with events and the ramifications that events have with regard to privileges when executing.

Stored routines require the `events` data dictionary table in the `mysql` system database. This table is created during the MySQL 9.7 installation procedure. If you are upgrading to MySQL 9.7 from an earlier version, be sure to perform the upgrade procedure to make sure that your system database is up to date. See [Chapter 3, *Upgrading MySQL*](upgrading.md).

### Additional Resources

- There are some restrictions on the use of events; see [Section 27.10, “Restrictions on Stored Programs”](stored-program-restrictions.md).
- Binary logging for events takes place as described in [Section 27.9, “Stored Program Binary Logging”](stored-programs-logging.md).
- You may also find the [MySQL User Forums](https://forums.mysql.com/list.php?20) to be helpful.