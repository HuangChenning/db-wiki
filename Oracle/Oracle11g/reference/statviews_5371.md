---
title: USER_NETWORK_ACL_PRIVILEGES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5371.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_NETWORK_ACL_PRIVILEGES` describes the status of the network privileges for the current user to access network hosts.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HOST` | `VARCHAR2(1000)` |  | Network host |
| `LOWER_PORT` | `NUMBER(5)` |  | Lower bound of the port range |
| `UPPER_PORT` | `NUMBER(5)` |  | Upper bound of the port range |
| `PRIVILEGE` | `CHAR(7)` |  | Network privilege |
| `STATUS` | `VARCHAR2(7)` |  | Privilege status: |