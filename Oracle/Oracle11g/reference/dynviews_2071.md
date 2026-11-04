---
title: "V$MYSTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2071.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MYSTAT` contains statistics on the current session.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | ID of the current session |
| `STATISTIC#` | `NUMBER` | Number of the statistic |
| `VALUE` | `NUMBER` | Value of the statistic |