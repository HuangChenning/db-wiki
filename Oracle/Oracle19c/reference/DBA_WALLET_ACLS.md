---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_WALLET_ACLS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.105 DBA\_WALLET\_ACLS

`DBA_WALLET_ACLS` displays the access control lists assigned to restrict access to wallets through PL/SQL network utility packages.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WALLET_PATH` | `VARCHAR2(1000)` | `NOT NULL` | Wallet path |
| `ACL` | `VARCHAR2(4000)` |  | Path of the access control list |
| `ACLID` | `RAW(8)` |  | Object ID of the access control list |
| `ACL_OWNER` | `VARCHAR2(128)` |  | Owner of the access control list |