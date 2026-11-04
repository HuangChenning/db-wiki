---
title: Oracle Wait Events
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/waitevents.htm
tags:
  - oracle
  - 11g
  - reference
---

## C Oracle Wait Events

This appendix contains the following topics:

- [Classes of Wait Events](waitevents001.md)
- [Descriptions of Common Wait Event Parameters](waitevents002.md)
- [Descriptions of Wait Events](waitevents003.md)

Information about wait events is displayed in three dynamic performance views:

- `V$SESSION_WAIT` displays the events for which sessions have just completed waiting or are currently waiting.
- `V$SYSTEM_EVENT` displays the total number of times all the sessions have waited for the events in that view.
- `V$SESSION_EVENT` is similar to `V$SYSTEM_EVENT`, but displays all waits for each session.

See Also:

["V$SESSION\_EVENT"](dynviews_3020.md), ["V$SESSION\_WAIT"](dynviews_3024.md), and ["V$SYSTEM\_EVENT"](dynviews_3095.md)

Many of these wait events are tied to the internal implementation of Oracle and therefore are subject to change or deletion without notice. Application developers should be aware of this and write their code to tolerate missing or extra wait events.

The following SQL statement displays an alphabetical list of all Oracle wait events and the wait class to which they belong:

```
SQL> SELECT name, wait_class FROM V$EVENT_NAME ORDER BY name;
```