---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_NETWORK_ACLS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_NETWORK_ACLS` describes the access control list assignments to network hosts.

Note:

This `DBA_NETWORK_ACLS` view is deprecated in Oracle Database 12c Release 1 (12.1). Oracle recommends that you use the `DBA_HOST_ACLS` view, instead.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HOST` | `VARCHAR2(1000)` | `NOT NULL` | Network host |
| `LOWER_PORT` | `NUMBER(5)` |  | Lower bound of the port range |
| `UPPER_PORT` | `NUMBER(5)` |  | Upper bound of the port range |
| `ACL` | `VARCHAR2(4000)` |  | Path of the access control list |
| `ACLID` | `RAW(8)` |  | Object ID of the access control list |
| `ACL_OWNER` | `VARCHAR2(128)` |  | Owner of the access control list |

See Also:

" [DBA\_HOST\_ACLS](DBA_HOST_ACLS.md) "