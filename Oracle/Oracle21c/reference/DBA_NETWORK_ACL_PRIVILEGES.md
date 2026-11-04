---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_NETWORK_ACL_PRIVILEGES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.206 DBA\_NETWORK\_ACL\_PRIVILEGES

`DBA_NETWORK_ACL_PRIVILEGES` describes the network privileges defined in all access control lists that are currently assigned to network hosts.

Note:

This `DBA_NETWORK_ACL_PRIVILEGES` view is deprecated in Oracle Database 12c Release 1 (12.1). Oracle recommends that you use the `DBA_HOST_ACES` view, instead.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ACL` | `VARCHAR2(4000)` |  | Path of the access control list |
| `ACLID` | `RAW(8)` | `NOT NULL` | Object ID of the access control list |
| `PRINCIPAL` | `VARCHAR2(128)` |  | Principal (database user or role) whom the privilege is granted to or denied from |
| `PRIVILEGE` | `VARCHAR2(128)` |  | Network privilege |
| `IS_GRANT` | `VARCHAR2(5)` |  | Indicates whether the privilege is granted (`true`) or denied (`false`) |
| `INVERT` | `VARCHAR2(5)` |  | Indicates whether the access control entry contains invert principal (`true`) or not (`false`) |
| `START_DATE` | `TIMESTAMP(6)` |  | Start date of the access control entry |
| `END_DATE` | `TIMESTAMP(6)` |  | End date of the access control entry |
| `ACL_OWNER` | `VARCHAR2(128)` |  | Owner of the access control list |

See Also:

" [DBA\_HOST\_ACES](DBA_HOST_ACES.md) "