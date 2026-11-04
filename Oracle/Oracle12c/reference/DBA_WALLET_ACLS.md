---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_WALLET_ACLS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_WALLET_ACLS` displays the access control lists assigned to restrict access to wallets through PL/SQL network utility packages.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WALLET_PATH` | `VARCHAR2(1000)` | `NOT NULL` | Wallet path |
| `ACL` | `VARCHAR2(4000)` |  | Path of the access control list |
| `ACLID` | `RAW(8)` |  | Object ID of the access control list |
| `ACL_OWNER` | `VARCHAR2(128)` |  | Owner of the access control list |