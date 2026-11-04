---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HOST_ACES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.94 DBA\_HOST\_ACES

`DBA_HOST_ACES` describes access control entries defined in host access control lists.

Related View

`USER_HOST_ACES` describes the status of access control entries for the current user to access network hosts through PL/SQL network utility packages. This view does not display the `ACE_ORDER`, `START_DATE`, `END_DATE`, `GRANT_TYPE`, `INVERTED_PRINCIPAL`, `PRINCIPAL`, or `PRINCIPAL_TYPE` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HOST` | `VARCHAR2(1000)` | `NOT NULL` | Network host |
| `LOWER_PORT` | `NUMBER(5)` |  | Lower bound of the port range |
| `UPPER_PORT` | `NUMBER(5)` |  | Upper bound of the port range |
| `ACE_ORDER` | `NUMBER` | `NOT NULL` | Order number of the access control entry |
| `START_DATE` | `TIMESTAMP(6)` |  | Start date of the access control entry |
| `END_DATE` | `TIMESTAMP(6)` |  | End date of the access control entry |
| `GRANT_TYPE` | `VARCHAR2(5)` |  | Indicates whether the access control entry grants or denies the privilege |
| `INVERTED_PRINCIPAL` | `VARCHAR2(3)` |  | Indicates whether the principal is inverted or not |
| `PRINCIPAL` | `VARCHAR2(128)` |  | Principal the privilege is applied to |
| `PRINCIPAL_TYPE` | `VARCHAR2(16)` |  | Type of the principal |
| `PRIVILEGE` | `VARCHAR2(128)` |  | Privilege |

See Also:

" [USER\_HOST\_ACES](USER_HOST_ACES.md) "