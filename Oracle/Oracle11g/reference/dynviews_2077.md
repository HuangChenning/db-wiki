---
title: "V$OBJECT_DEPENDENCY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2077.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$OBJECT_DEPENDENCY` displays the objects depended on by a package, procedure, or cursor that is currently loaded in the shared pool. For example, together with `V$SESSION` and `V$SQL`, this view can be used to determine which tables are used in the SQL statement that a user is currently executing.

See Also:

["V$SESSION"](dynviews_3016.md) and ["V$SQL"](dynviews_3043.md)

| Column | Datatype | Description |
| --- | --- | --- |
| `FROM_ADDRESS` | `RAW(4 \| 8)` | Address of a procedure, package, or cursor that is currently loaded in the shared pool |
| `FROM_HASH` | `NUMBER` | Hash value of a procedure, package, or cursor that is currently loaded in the shared pool |
| `TO_OWNER` | `VARCHAR2(64)` | Owner of the object that is depended on |
| `TO_NAME` | `VARCHAR2(1000)` | Name of the object that is depended on |
| `TO_ADDRESS` | `RAW(4 \| 8)` | Address of the object that is depended on. These can be used to look up more information on the object in `V$DB_OBJECT_CACHE`. |
| `TO_HASH` | `NUMBER` | Hash value of the object that is depended on. These can be used to look up more information on the object in `V$DB_OBJECT_CACHE`. |
| `TO_TYPE` | `NUMBER` | Type of the object that is depended on |