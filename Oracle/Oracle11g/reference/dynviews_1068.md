---
title: "V$BGPROCESS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1068.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BGPROCESS` displays information about the background processes.

| Column | Datatype | Description |
| --- | --- | --- |
| `PADDR` | `RAW(4 \| 8)` | Address of the process state object |
| `PSERIAL#` | `NUMBER` | Process state object serial number |
| `NAME` | `VARCHAR2(5)` | Name of this background process |
| `DESCRIPTION` | `VARCHAR2(64)` | Description of the background process |
| `ERROR` | `NUMBER` | Error encountered |