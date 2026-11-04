---
title: DBA_WALLET_ACLS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5088.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_WALLET_ACLS` displays the access control lists assigned to restrict access to wallets through PL/SQL network utility packages.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WALLET_PATH` | `VARCHAR2(1000)` | `NOT NULL` | Wallet path |
| `ACL` | `VARCHAR2(4000)` |  | Path of the access control list |
| `ACLID` | `RAW(16)` | `NOT NULL` | Object ID of the access control list |