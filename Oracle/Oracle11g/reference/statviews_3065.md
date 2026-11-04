---
title: DBA_AQ_AGENT_PRIVS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3065.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_AQ_AGENT_PRIVS` displays information about the registered AQ agents that are mapped to all users in the database.

Related View

`USER_AQ_AGENT_PRIVS` displays information about the registered AQ agents that are mapped to the current user. This view does not display the `DB_USERNAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `AGENT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the AQ agent |
| `DB_USERNAME` | `VARCHAR2(30)` |  | Name of the database user that the agent maps to |
| `HTTP_ENABLED` | `VARCHAR2(4)` |  | Indicates whether the agent is allowed to access AQ through HTTP (`YES`) or not (`NO`) |
| `SMTP_ENABLED` | `VARCHAR2(4)` |  | Indicates whether the agent is allowed to access AQ through SMTP (`YES`) or not (`NO`) |

See Also:

["USER\_AQ\_AGENT\_PRIVS"](statviews_5227.md)