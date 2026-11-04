---
title: "V$HM_INFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1176.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$HM_INFO` displays information about Health Monitor runs, findings, and recommendations. The information for a run/finding/recommendation is organized as a name, value pair.

If the type of information is `RUN`, then the data represents the input parameters for that run. If the type of information is `FINDING` or `RECOMMENDATION`, then the data represents the information about that particular finding/recommendation.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Unique identifier of the information |
| `TYPE` | `VARCHAR2(14)` | Type of the information: |
| `NAME` | `VARCHAR2(32)` | Information parameter name |
| `VALUE` | `VARCHAR2(513)` | Information parameter value |