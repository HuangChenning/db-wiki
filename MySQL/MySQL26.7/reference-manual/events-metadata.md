---
title: "MySQL :: MySQL 26.7 Reference Manual :: 27.5.4 Event Metadata"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/events-metadata.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 27.5.4 Event Metadata

To obtain metadata about events:

- Query the [`EVENTS`](information-schema-events-table.md) table of the `INFORMATION_SCHEMA` database. See [Section 28.3.14, “The INFORMATION\_SCHEMA EVENTS Table”](information-schema-events-table.md).
- Use the [`SHOW CREATE EVENT`](show-create-event.md) statement. See [Section 15.7.7.8, “SHOW CREATE EVENT Statement”](show-create-event.md).
- Use the [`SHOW EVENTS`](show-events.md) statement. See [Section 15.7.7.21, “SHOW EVENTS Statement”](show-events.md).

**Event Scheduler Time Representation**

Each session in MySQL has a session time zone (STZ). This is the session [`time_zone`](server-system-variables.md) value that is initialized from the server's global [`time_zone`](server-system-variables.md) value when the session begins but may be changed during the session.

The session time zone that is current when a [`CREATE EVENT`](create-event.md) or [`ALTER EVENT`](alter-event.md) statement executes is used to interpret times specified in the event definition. This becomes the event time zone (ETZ); that is, the time zone that is used for event scheduling and is in effect within the event as it executes.

For representation of event information in the data dictionary, the `execute_at`, `starts`, and `ends` times are converted to UTC and stored along with the event time zone. This enables event execution to proceed as defined regardless of any subsequent changes to the server time zone or daylight saving time effects. The `last_executed` time is also stored in UTC.

Event times can be obtained by selecting from the Information Schema [`EVENTS`](information-schema-events-table.md) table or from [`SHOW EVENTS`](show-events.md), but they are reported as ETZ or STZ values. The following table summarizes representation of event times.

| Value | [`EVENTS`](information-schema-events-table.md) Table | [`SHOW EVENTS`](show-events.md) |
| --- | --- | --- |
| Execute at | ETZ | ETZ |
| Starts | ETZ | ETZ |
| Ends | ETZ | ETZ |
| Last executed | ETZ | n/a |
| Created | STZ | n/a |
| Last altered | STZ | n/a |