---
title: "V$HS_PARAMETER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1180.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$HS_PARAMETER` describes the initialization parameters in use by the server and agent.

| Column | Datatype | Description |
| --- | --- | --- |
| `HS_SESSION_ID` | `NUMBER` | Unique HS session identifier (maps to the `HS_SESSION_ID` column of `V$HS_SESSION`) |
| `PARAMETER` | `VARCHAR2(30)` | Name of the parameter |
| `VALUE` | `VARCHAR2(64)` | Value of the parameter |
| `SOURCE` | `VARCHAR2(1)` | Indicates whether the parameter was defined in the agent (`A`) or server (`S`) |
| `ENV` | `VARCHAR2(1)` | Indicates whether the parameter was set as an environment variable in the agent (`T`) or elsewhere (`F`) |