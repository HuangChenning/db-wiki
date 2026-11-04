---
title: "V$SQL_CS_SELECTIVITY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3048.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQL_CS_SELECTIVITY` exposes the valid selectivity ranges for a child cursor in extended cursor sharing mode. A valid range consists of a low and high value for each predicate containing binds. Each predicate's selectivity (with the current bind value) must fall between the corresponding low and high values in order for the child cursor to be shared.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4)` | Address of the handle to the parent for this cursor |
| `HASH_VALUE` | `NUMBER` | Hash value of the parent statement in the library cache |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the parent cursor in the library cache |
| `CHILD_NUMBER` | `NUMBER` | Number of the child cursor |
| `PREDICATE` | `VARCHAR2(40)` | Predicate whose selectivity must fall between low and high values |
| `RANGE_ID` | `NUMBER` | Identifier for the range used to match up the low and high values for multiple predicates |
| `LOW` | `VARCHAR2(10)` | Lower bound for allowable selectivity |
| `HIGH` | `VARCHAR2(10)` | Upper bound for allowable selectivity |