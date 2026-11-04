---
title: DBA_NETWORK_ACL_PRIVILEGES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4152.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_NETWORK_ACL_PRIVILEGES` describes the network privileges defined in all access control lists that are currently assigned to network hosts.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ACL` | `VARCHAR2(4000)` |  | Path of the access control list |
| `ACLID` | `RAW(16)` | `NOT NULL` | Object ID of the access control list |
| `PRINCIPAL` | `VARCHAR2(4000)` |  | Principal (database user or role) whom the privilege is granted to or denied from |
| `PRIVILEGE` | `VARCHAR2(7)` |  | Network privilege |
| `IS_GRANT` | `VARCHAR2(5)` |  | Indicates whether the privilege is granted (`true`) or denied (`false`) |
| `INVERT` | `VARCHAR2(5)` |  | Indicates whether the access control entry contains invert principal (`true`) or not (`false`) |
| `START_DATE` | `TIMESTAMP(9) WITH TIME ZONE` |  | Start date of the access control entry |
| `END_DATE` | `TIMESTAMP(9) WITH TIME ZONE` |  | End date of the access control entry |