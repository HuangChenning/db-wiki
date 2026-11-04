---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_USERS_WITH_DEFPWD.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.99 DBA\_USERS\_WITH\_DEFPWD

`DBA_USERS_WITH_DEFPWD` displays all users in the database that are still using their default passwords.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the user |
| `PRODUCT` | `VARCHAR2(4000)` |  | Name of the product the user belongs to |

Note:

In a CDB, when `DBA_USERS_WITH_DEFPWD` is queried from a PDB, information about local users who are using their default passwords is displayed. To display information about common users, query `DBA_USERS_WITH_DEFPWD` from the CDB root.

See Also:

[Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT89257) for an introduction to local and common users in a CDB