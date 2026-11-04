---
title: "27.4.3 Event Syntax"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/events-syntax.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 27.4.3 Event Syntax

MySQL provides several SQL statements for working with scheduled events:

- New events are defined using the [`CREATE           EVENT`](create-event.md) statement. See [Section 15.1.13, “CREATE EVENT Statement”](create-event.md).
- The definition of an existing event can be changed by means of the [`ALTER EVENT`](alter-event.md) statement. See [Section 15.1.3, “ALTER EVENT Statement”](alter-event.md).
- When a scheduled event is no longer wanted or needed, it can be deleted from the server by its definer using the [`DROP EVENT`](drop-event.md) statement. See [Section 15.1.25, “DROP EVENT Statement”](drop-event.md). Whether an event persists past the end of its schedule also depends on its `ON           COMPLETION` clause, if it has one. See [Section 15.1.13, “CREATE EVENT Statement”](create-event.md).
	An event can be dropped by any user having the [`EVENT`](privileges-provided.md) privilege for the database on which the event is defined. See [Section 27.4.6, “The Event Scheduler and MySQL Privileges”](events-privileges.md).