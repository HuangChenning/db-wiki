---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_NETWORK_ACL_PRIVILEGES.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_NETWORK_ACL_PRIVILEGES` describes the status of the network privileges for the current user to access network hosts.

Note:

This `USER_NETWORK_ACL_PRIVILEGES` view is deprecated in Oracle Database 12c Release 1 (12.1). Oracle recommends that you use the `USER_HOST_ACES` view, instead.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HOST` | `VARCHAR2(1000)` | `NOT NULL` | Network host |
| `LOWER_PORT` | `NUMBER(5)` |  | Lower bound of the port range |
| `UPPER_PORT` | `NUMBER(5)` |  | Upper bound of the port range |
| `PRIVILEGE` | `CHAR(128)` |  | Network privilege |
| `STATUS` | `VARCHAR2(7)` |  | Privilege status:  - `DENIED` - `GRANTED` |

See Also:

" [USER\_HOST\_ACES](USER_HOST_ACES.md) "