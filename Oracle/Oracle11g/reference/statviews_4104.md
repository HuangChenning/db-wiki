---
title: DBA_KGLLOCK
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4104.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_KGLLOCK` lists all the locks and pins held on KGL objects (objects in the Kernel Generic Library cache).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `kgllkuse` | `RAW(4)` |  | Address of the user session that holds the lock or pin |
| `kgllkhdl` | `RAW(4)` |  | Address of the handle for the KGL object |
| `kgllkmod` | `NUMBER` |  | Current mode of the lock or pin |
| `kgllkreq` | `NUMBER` |  | Mode in which the lock or pin was requested |
| `kgllktype` | `VARCHAR2(4)` |  | Whether this is a lock or a pin |