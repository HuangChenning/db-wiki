---
title: DBA_PRIV_AUDIT_OPTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4185.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_PRIV_AUDIT_OPTS` describes current system privileges being audited across the system and by user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USER_NAME` | `VARCHAR2(30)` |  | User name if by user auditing; `ANY CLIENT` if access by a proxy on behalf of a client is being audited; NULL for system-wide auditing |
| `PROXY_NAME` | `VARCHAR2(30)` |  | Name of the proxy user which is performing an operation for the client; NULL if the client is performing the operation directly |
| `PRIVILEGE` | `VARCHAR2(40)` | `NOT NULL` | Name of the system privilege being audited |
| `SUCCESS` | `VARCHAR2(10)` |  | Mode for `WHENEVER SUCCESSFUL` system auditing |
| `FAILURE` | `VARCHAR2(10)` |  | Mode for `WHENEVER NOT SUCCESSFUL` system auditing |