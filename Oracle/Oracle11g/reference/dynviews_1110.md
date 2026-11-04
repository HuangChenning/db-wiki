---
title: "V$DBFILE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1110.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DBFILE` displays all datafiles making up the database. This view is retained for historical compatibility. Use of `V$DATAFILE` is recommended instead.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | File identifier |
| `NAME` | `VARCHAR2(513)` | Name of the file |

See Also:

["V$DATAFILE"](dynviews_1100.md)