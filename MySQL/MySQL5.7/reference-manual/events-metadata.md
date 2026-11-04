---
title: "23.4.4 Event Metadata"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/events-metadata.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 23.4.4 Event Metadata

To obtain metadata about events:

- Query the `event` table of the `mysql` database.
- Query the [`EVENTS`](information-schema-events-table.md) table of the `INFORMATION_SCHEMA` database. See [Section 24.3.8, “The INFORMATION\_SCHEMA EVENTS Table”](information-schema-events-table.md).
- Use the [`SHOW CREATE EVENT`](show-create-event.md) statement. See [Section 13.7.5.7, “SHOW CREATE EVENT Statement”](show-create-event.md).
- Use the [`SHOW EVENTS`](show-events.md) statement. See [Section 13.7.5.18, “SHOW EVENTS Statement”](show-events.md).

**Event Scheduler Time Representation**

Each session in MySQL has a session time zone (STZ). This is the session [`time_zone`](server-system-variables.md) value that is initialized from the server's global [`time_zone`](server-system-variables.md) value when the session begins but may be changed during the session.

The session time zone that is current when a [`CREATE EVENT`](create-event.md) or [`ALTER EVENT`](alter-event.md) statement executes is used to interpret times specified in the event definition. This becomes the event time zone (ETZ); that is, the time zone that is used for event scheduling and is in effect within the event as it executes.

For representation of event information in the `mysql.event` table, the `execute_at`, `starts`, and `ends` times are converted to UTC and stored along with the event time zone. This enables event execution to proceed as defined regardless of any subsequent changes to the server time zone or daylight saving time effects. The `last_executed` time is also stored in UTC.

If you select information from `mysql.event`, the times just mentioned are retrieved as UTC values. These times can also be obtained by selecting from the Information Schema [`EVENTS`](information-schema-events-table.md) table or from [`SHOW EVENTS`](show-events.md), but they are reported as ETZ values. Other times available from these sources indicate when an event was created or last altered; these are displayed as STZ values. The following table summarizes representation of event times.

| Value | `mysql.event` | [`EVENTS`](information-schema-events-table.md) Table | [`SHOW EVENTS`](show-events.md) |
| --- | --- | --- | --- |
| Execute at | UTC | ETZ | ETZ |
| Starts | UTC | ETZ | ETZ |
| Ends | UTC | ETZ | ETZ |
| Last executed | UTC | ETZ | n/a |
| Created | STZ | STZ | n/a |
| Last altered | STZ | STZ | n/a |