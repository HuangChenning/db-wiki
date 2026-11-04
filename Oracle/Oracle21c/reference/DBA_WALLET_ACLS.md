---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WALLET_ACLS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.106 DBA\_WALLET\_ACLS

`DBA_WALLET_ACLS` displays the access control lists assigned to restrict access to wallets through PL/SQL network utility packages.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WALLET_PATH` | `VARCHAR2(1000)` | `NOT NULL` | Wallet path |
| `ACL` | `VARCHAR2(4000)` |  | Path of the access control list |
| `ACLID` | `RAW(8)` |  | Object ID of the access control list |
| `ACL_OWNER` | `VARCHAR2(128)` |  | Owner of the access control list |