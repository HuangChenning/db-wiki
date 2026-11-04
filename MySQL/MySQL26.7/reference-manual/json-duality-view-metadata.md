---
title: "MySQL :: MySQL 26.7 Reference Manual :: 27.7.3 JSON Duality View Metadata"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/json-duality-view-metadata.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 27.7.3 JSON Duality View Metadata

You can obtain information about existing JSON duality views from the following Information Schema tables which have been implemented in this release:

- [`JSON_DUALITY_VIEWS`](information-schema-json-duality-views-table.md): Provides per-view information about JSON duality views.
- [`JSON_DUALITY_VIEW_COLUMNS`](information-schema-json-duality-view-columns-table.md): Provides information about columns defined in JSON duality views.
- [`JSON_DUALITY_VIEW_LINKS`](information-schema-json-duality-view-links-table.md): Describes parent-child relationships between JSON duality views and their base tables.
- [`JSON_DUALITY_VIEW_TABLES`](information-schema-json-duality-view-tables-table.md): Provides information about tables referenced by JSON duality views.

See the descriptions of the individual tables for more information.

JSON duality views are also supported as a feature by the Option Tracker component, which exposes a status variable [`option_tracker_usage:JSON Duality       View`](option-tracker-component-status-variables.md); this variable stores the number of times that any JSON duality views have been opened by the server.