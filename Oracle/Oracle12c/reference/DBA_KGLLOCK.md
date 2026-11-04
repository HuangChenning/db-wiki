---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_KGLLOCK.html
tags:
  - oracle
  - 12c
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