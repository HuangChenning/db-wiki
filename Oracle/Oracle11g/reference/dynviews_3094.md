---
title: "V$SYSTEM_CURSOR_CACHE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3094.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SYSTEM_CURSOR_CACHE` displays system wide information on cursor usage.

See Also:

["V$SESSION\_CURSOR\_CACHE"](dynviews_3019.md)

| Column | Datatype | Description |
| --- | --- | --- |
| `OPENS` | `NUMBER` | Cumulative total of cursor opens |
| `HITS` | `NUMBER` | Cumulative total of cursor open hits |
| `HIT_RATIO` | `NUMBER` | Ratio of the number of times an open cursor was found divided by the number of times a cursor was sought |