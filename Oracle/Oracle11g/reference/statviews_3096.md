---
title: DBA_BLOCKERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3096.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_BLOCKERS` displays a session if it is not waiting for a locked object but is holding a lock on an object for which another session is waiting. In an Oracle RAC environment, this only applies if the blocker is on the same instance.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HOLDING_SESSION` | `NUMBER` |  | Session holding a lock |