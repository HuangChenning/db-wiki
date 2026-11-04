---
title: "MySQL :: MySQL 26.7 Reference Manual :: 15.1.30 DROP EVENT Statement"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/drop-event.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 15.1.30 DROP EVENT Statement

```sql
DROP EVENT [IF EXISTS] event_name
```

This statement drops the event named *`event_name`*. The event immediately ceases being active, and is deleted completely from the server.

If the event does not exist, the error ERROR 1517 (HY000): Unknown event ' *`event_name`* ' results. You can override this and cause the statement to generate a warning for nonexistent events instead using `IF EXISTS`.

This statement requires the [`EVENT`](privileges-provided.md) privilege for the schema to which the event to be dropped belongs.