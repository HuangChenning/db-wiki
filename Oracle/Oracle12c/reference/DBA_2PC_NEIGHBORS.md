---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_2PC_NEIGHBORS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_2PC_NEIGHBORS` describes incoming and outgoing connections for pending transactions.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `LOCAL_TRAN_ID ` | `VARCHAR2(22)` |  | Local identifier of a transaction |
| `IN_OUT` | `VARCHAR2(3)` |  | `IN` for incoming connections, `OUT` for outgoing |
| `DATABASE` | `VARCHAR2(128)` |  | `IN ` for client database name, `OUT` for outgoing database link |
| `DBUSER_OWNER` | `VARCHAR2(128)` |  | `IN` for name of local user, `OUT` for owner of database link |
| `INTERFACE` | `VARCHAR2(1)` |  | `C` for request commit, otherwise `N` for prepare or request read only commit |
| `DBID` | `VARCHAR2(16)` |  | Database ID at the other end of the connection |
| `SESS#` | `NUMBER(38)` |  | Session number of the connection at this database |
| `BRANCH` | `VARCHAR2(128)` |  | Transaction branch ID of the connection at this database |