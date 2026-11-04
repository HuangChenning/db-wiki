---
title: "V$EXECUTION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1132.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$EXECUTION` displays information on parallel execution.

| Column | Datatype | Description |
| --- | --- | --- |
| `PID` | `NUMBER` | Session ID |
| `DEPTH` | `NUMBER` | The depth |
| `FUNCTION` | `VARCHAR2(10)` | Session serial number |
| `TYPE` | `VARCHAR2(7)` | Name of the `OBJECT_NODE` in plan table |
| `NVALS` | `NUMBER` | Elapsed time for `OBJECT_NODE` |
| `VAL1` | `NUMBER` | The value for number 1 |
| `VAL2` | `NUMBER` | The value for number 2 |
| `SEQH` | `NUMBER` | A sequence |
| `SEQL` | `NUMBER` | A sequence |