---
title: "V$TIMEZONE_NAMES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3112.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TIMEZONE_NAMES` displays valid time zone names.

| Column | Datatype | Description |
| --- | --- | --- |
| `TZNAME` | `VARCHAR2(64)` | Time zone region (for example, `US/Pacific`) |
| `TZABBREV` | `VARCHAR2(64)` | Corresponding daylight abbreviation (for example, `PDT`) |