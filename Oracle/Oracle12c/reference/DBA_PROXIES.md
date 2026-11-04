---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_PROXIES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_PROXIES` displays Information about all proxy connections in the database.

Related View

`USER_PROXIES` displays information about connections the current user is allowed to proxy. This view does not display the `PROXY` or `PROXY_AUTHORITY` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROXY` | `VARCHAR2(128)` |  | Name of the proxy user |
| `CLIENT` | `VARCHAR2(128)` | `NOT NULL` | Name of the client user who the proxy user can act on behalf of |
| `AUTHENTICATION` | `VARCHAR2(3)` |  | Indicates whether the proxy is required to supply the client's authentication credentials (`YES`) or not (`NO`) |
| `AUTHORIZATION_CONSTRAINT` | `VARCHAR2(35)` |  | Indicates the proxy's authority to exercise roles on the client's behalf:  - `NO CLIENT ROLES MAY BE ACTIVATED` - `PROXY MAY ACTIVATE ROLE` - `PROXY MAY ACTIVATE ALL CLIENT ROLES` - `PROXY MAY NOT ACTIVATE ROLE` |
| `ROLE` | `VARCHAR2(128)` |  | Name of the role referenced in `AUTHORIZATION_CONSTRAINT` |
| `PROXY_AUTHORITY` | `VARCHAR2(9)` |  | Value is either:  - DIRECTORY if EUS proxy is enabled for that database user - DATABASE if this row describes a local proxy permission |

See Also:

" [USER\_PROXIES](USER_PROXIES.md) "