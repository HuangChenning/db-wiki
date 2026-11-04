---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_HOST_ACLS.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.96 DBA\_HOST\_ACLS

`DBA_HOST_ACLS` describes access control lists assigned to restrict access to network hosts through PL/SQL network utility packages.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HOST` | `VARCHAR2(1000)` | `NOT NULL` | Network host |
| `LOWER_PORT` | `NUMBER(5)` |  | Lower bound of the port range |
| `UPPER_PORT` | `NUMBER(5)` |  | Upper bound of the port range |
| `ACL` | `VARCHAR2(4000)` |  | The name of the access control list |
| `ACLID` | `RAW(8)` |  | The object ID of the access control list |
| `ACL_OWNER` | `VARCHAR2(128)` |  | The owner of the access control list |