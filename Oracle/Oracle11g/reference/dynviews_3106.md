---
title: "V$TEMPORARY_LOBS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3106.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TEMPORARY_LOBS` displays temporary LOBs.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID |
| `CACHE_LOBS` | `NUMBER` | Number of cache temp LOBs |
| `NOCACHE_LOBS` | `NUMBER` | Number of nocache temp LOBs |
| `ABSTRACT_LOBS` | `NUMBER` | Number of abstract LOBs |