---
title: "10.14.9 Event Scheduler Thread States"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/event-scheduler-thread-states.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 10.14.9 Event Scheduler Thread States

These states occur for the Event Scheduler thread, threads that are created to execute scheduled events, or threads that terminate the scheduler.

- `Clearing`
	The scheduler thread or a thread that was executing an event is terminating and is about to end.
- `Initialized`
	The scheduler thread or a thread that executes an event has been initialized.
- `Waiting for next activation`
	The scheduler has a nonempty event queue but the next activation is in the future.
- `Waiting for scheduler to stop`
	The thread issued `SET GLOBAL             event_scheduler=OFF` and is waiting for the scheduler to stop.
- `Waiting on empty queue`
	The scheduler's event queue is empty and it is sleeping.