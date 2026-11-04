---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WALLET_ACES.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.105 DBA\_WALLET\_ACES

`DBA_WALLET_ACES` describes access control entries defined in wallet access control lists.

Related View

`USER_WALLET_ACES` describes the status of access control entries for the current user to access wallets through PL/SQL network utility packages. This view does not display the `ACE_ORDER`, `START_DATE`, `END_DATE`, `GRANT_TYPE`, `INVERTED_PRINCIPAL`, `PRINCIPAL`, or `PRINCIPAL_TYPE` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WALLET_PATH` | `VARCHAR2(1000)` | `NOT NULL` | Wallet path |
| `ACE_ORDER` | `NUMBER` | `NOT NULL` | Order number of the access control entry |
| `START_DATE` | `TIMESTAMP(6)` |  | Start date of the access control entry |
| `END_DATE` | `TIMESTAMP(6)` |  | End date of the access control entry |
| `GRANT_TYPE` | `VARCHAR2(5)` |  | Indicates whether the access control entry grants or denies the privilege |
| `INVERTED_PRINCIPAL` | `VARCHAR2(3)` |  | Indicates whether the principal is inverted or not |
| `PRINCIPAL` | `VARCHAR2(128)` |  | Principal the privilege is applied to |
| `PRINCIPAL_TYPE` | `VARCHAR2(16)` |  | Type of the principal |
| `PRIVILEGE` | `VARCHAR2(128)` |  | Privilege |

See Also:

" [USER\_WALLET\_ACES](USER_WALLET_ACES.md) "