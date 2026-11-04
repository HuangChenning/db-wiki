---
title: "V$NLS_PARAMETERS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2075.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$NLS_PARAMETERS` contains current values of NLS parameters.

| Column | Datatype | Description |
| --- | --- | --- |
| `PARAMETER` | `VARCHAR2(64)` | Parameter names are as follows: `NLS_CALENDAR, NLS_CHARACTERSET, NLS_COMP, NLS_CURRENCY, NLS_DATE_FORMAT, NLS_DATE_LANGUAGE, NLS_DUAL_CURRENCY, NLS_ISO_CURRENCY, NLS_LANGUAGE, NLS_LENGTH_SEMANTICS, NLS_NCHAR_CHARACTERSET, NLS_NCHAR_CONV_EXCP, NLS_NUMERIC_CHARACTERS, NLS_SORT, NLS_TERRITORY, NLS_TIMESTAMP_FORMAT, NLS_TIMESTAMP_TZ_FORMAT`  Two additional parameters, NLS\_TIME\_FORMAT and NLS\_TIME\_TZ\_FORMAT, are currently used for internal purposes only. |
| `VALUE` | `VARCHAR2(64)` | NLS parameter value |