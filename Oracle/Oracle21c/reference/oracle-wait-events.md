---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/oracle-wait-events.html
tags:
  - oracle
  - 21c
  - reference
---

## C Oracle Wait Events

It includes these topics:

- [Classes of Wait Events](classes-of-wait-events.md)
- [Descriptions of Common Wait Event Parameters](descriptions-of-common-wait-event-parameters.md)
- [Descriptions of Wait Events](descriptions-of-wait-events.md)

Information about wait events is displayed in three dynamic performance views:

- `V$SESSION_WAIT` displays the events for which sessions have just completed waiting or are currently waiting.
- `V$SYSTEM_EVENT` displays the total number of times all the sessions have waited for the events in that view.
- `V$SESSION_EVENT` is similar to `V$SYSTEM_EVENT`, but displays all waits for each session.

See Also:

" [V$SESSION\_WAIT](V-SESSION_WAIT.md) ", " [V$SYSTEM\_EVENT](V-SYSTEM_EVENT.md) ", and " [V$SESSION\_EVENT](V-SESSION_EVENT.md) "

Many of these wait events are tied to the internal implementation of Oracle and therefore are subject to change or deletion without notice. Application developers should be aware of this and write their code to tolerate missing or extra wait events.

The following SQL statement displays an alphabetical list of all Oracle wait events and the wait class to which they belong:

```
SQL> SELECT name, wait_class FROM V$EVENT_NAME ORDER BY name;
```