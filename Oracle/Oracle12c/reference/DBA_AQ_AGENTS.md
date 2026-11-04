---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_AQ_AGENTS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_AQ_AGENTS` displays information about all registered AQ agents in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `AGENT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the AQ agent |
| `HTTP_ENABLED` | `VARCHAR2(4)` |  | Indicates whether the agent is allowed to access AQ through HTTP (`YES`) or not (`NO`) |
| `SMTP_ENABLED` | `VARCHAR2(4)` |  | Indicates whether the agent is allowed to access AQ through SMTP (`YES`) or not (`NO`) |