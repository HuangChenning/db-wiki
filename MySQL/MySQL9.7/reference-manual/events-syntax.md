---
title: "27.5.3 Event Syntax"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/events-syntax.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 27.5.3 Event Syntax

MySQL provides several SQL statements for working with scheduled events:

- New events are defined using the [`CREATE           EVENT`](create-event.md) statement. See [Section 15.1.15, “CREATE EVENT Statement”](create-event.md).
- The definition of an existing event can be changed by means of the [`ALTER EVENT`](alter-event.md) statement. See [Section 15.1.3, “ALTER EVENT Statement”](alter-event.md).
- When a scheduled event is no longer wanted or needed, it can be deleted from the server by its definer using the [`DROP EVENT`](drop-event.md) statement. See [Section 15.1.29, “DROP EVENT Statement”](drop-event.md). Whether an event persists past the end of its schedule also depends on its `ON           COMPLETION` clause, if it has one. See [Section 15.1.15, “CREATE EVENT Statement”](create-event.md).
	An event can be dropped by any user having the [`EVENT`](privileges-provided.md) privilege for the database on which the event is defined. See [Section 27.5.6, “The Event Scheduler and MySQL Privileges”](events-privileges.md).