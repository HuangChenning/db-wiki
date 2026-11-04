---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_USERS_WITH_DEFPWD.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.98 DBA\_USERS\_WITH\_DEFPWD

`DBA_USERS_WITH_DEFPWD` displays all users in the database that are still using their default passwords.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the user |
| `PRODUCT` | `VARCHAR2(4000)` |  | Name of the product the user belongs to |

Note:

In a CDB, when `DBA_USERS_WITH_DEFPWD` is queried from a PDB, information about local users who are using their default passwords is displayed. To display information about common users, query `DBA_USERS_WITH_DEFPWD` from the CDB root.

Note:

Starting with Oracle Database 19c, Release Update 19.32, this view displays additional default password account findings and associated product labels for `SYS`, `SYSTEM`, and `ADMIN` account combinations. This feature gives administrators a more complete view of default password risks and the related product context for remediation.

See Also:

[Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=CNCPT89257) for an introduction to local and common users in a CDB