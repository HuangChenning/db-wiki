---
title: DBA_AQ_AGENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3066.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_AQ_AGENTS` displays information about all registered AQ agents in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `AGENT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the AQ agent |
| `HTTP_ENABLED` | `VARCHAR2(4)` |  | Indicates whether the agent is allowed to access AQ through HTTP (`YES`) or not (`NO`) |
| `SMTP_ENABLED` | `VARCHAR2(4)` |  | Indicates whether the agent is allowed to access AQ through SMTP (`YES`) or not (`NO`) |