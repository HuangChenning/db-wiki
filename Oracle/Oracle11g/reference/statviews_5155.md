---
title: PROXY_USERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5155.htm
tags:
  - oracle
  - 11g
  - reference
---

`PROXY_USERS` describes the list of proxy users and the clients on whose behalf they can act.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROXY` | `VARCHAR2(30)` | `NOT NULL` | Name of a proxy user |
| `CLIENT` | `VARCHAR2(30)` | `NOT NULL` | Name of the client user who the proxy user can act as |
| `AUTHENTICATION` | `VARCHAR2(3)` |  | Indicates whether the proxy is required to supply the client's authentication credentials (`YES`) or not (`NO`) |
| `FLAGS` | `VARCHAR2(35)` |  | Flags associated with the proxy/client pair: |