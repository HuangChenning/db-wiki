---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PROXY_USERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.221 PROXY\_USERS

`PROXY_USERS` describes the list of proxy users and the clients on whose behalf they can act.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROXY` | `VARCHAR2(128)` | `NOT NULL` | Name of a proxy user |
| `CLIENT` | `VARCHAR2(128)` | `NOT NULL` | Name of the client user who the proxy user can act as |
| `AUTHENTICATION` | `VARCHAR2(3)` |  | Indicates whether the proxy is required to supply the client's authentication credentials (`YES`) or not (`NO`) |
| `FLAGS` | `VARCHAR2(35)` |  | Flags associated with the proxy/client pair:  - `PROXY MAY ACTIVATE ALL CLIENT ROLES` - `NO CLIENT ROLES MAY BE ACTIVATED` - `PROXY MAY ACTIVATE ROLE` - `PROXY MAY ACTIVATE ALL CLIENT ROLES` - `PROXY MAY NOT ACTIVATE ROLE` |

See Also:

" [DBA\_PROXIES](DBA_PROXIES.md) " for information about all proxy connections in the database