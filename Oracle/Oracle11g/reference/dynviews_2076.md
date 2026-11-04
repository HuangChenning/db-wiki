---
title: "V$NLS_VALID_VALUES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2076.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$NLS_VALID_VALUES` lists all valid values for NLS parameters.

| Column | Datatype | Description |
| --- | --- | --- |
| `PARAMETER` | `VARCHAR2(64)` | Parameter name (`LANGUAGE` \| `SORT` \| `TERRITORY` \| `CHARACTERSET`) |
| `VALUE` | `VARCHAR2(64)` | NLS parameter value |
| `ISDEPRECATED` | `VARCHAR2(5)` | Indicates whether the parameter has been deprecated (`TRUE`) or not (`FALSE`) |