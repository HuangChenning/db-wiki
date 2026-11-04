---
title: "MySQL :: MySQL 26.10 Reference Manual :: 27.5.3 Event Syntax"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/events-syntax.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 27.5.3 Event Syntax

MySQL provides several SQL statements for working with scheduled events:

- New events are defined using the [`CREATE           EVENT`](create-event.md) statement. See [Section 15.1.15, “CREATE EVENT Statement”](create-event.md).
- The definition of an existing event can be changed by means of the [`ALTER EVENT`](alter-event.md) statement. See [Section 15.1.3, “ALTER EVENT Statement”](alter-event.md).
- When a scheduled event is no longer wanted or needed, it can be deleted from the server by its definer using the [`DROP EVENT`](drop-event.md) statement. See [Section 15.1.30, “DROP EVENT Statement”](drop-event.md). Whether an event persists past the end of its schedule also depends on its `ON           COMPLETION` clause, if it has one. See [Section 15.1.15, “CREATE EVENT Statement”](create-event.md).
	An event can be dropped by any user having the [`EVENT`](privileges-provided.md) privilege for the database on which the event is defined. See [Section 27.5.6, “The Event Scheduler and MySQL Privileges”](events-privileges.md).