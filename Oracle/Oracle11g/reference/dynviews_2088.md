---
title: "V$PARAMETER_VALID_VALUES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2088.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PARAMETER_VALID_VALUES` displays a list of valid values for list parameters.

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM` | `NUMBER` | Parameter number |
| `NAME` | `VARCHAR2(64)` | Parameter name |
| `ORDINAL` | `NUMBER` | Ordinal number in the list (1-based) |
| `VALUE` | `VARCHAR2(255)` | Parameter value at ordinal |
| `ISDEFAULT` | `VARCHAR2(64)` | Indicates whether the given ordinal value is the default value for the parameter |