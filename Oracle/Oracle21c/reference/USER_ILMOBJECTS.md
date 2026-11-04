---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_ILMOBJECTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.510 USER\_ILMOBJECTS

`USER_ILMOBJECTS` displays all the Automatic Data Optimization policies and objects for a user.

Many objects inherit policies via their parent objects or because they were created in a particular tablespace. This view provides a mapping between the policies and objects and indicates whether a policy is inherited by an object or is directly specified on it. Its columns are the same as those in `DBA_ILMOBJECTS`.

Note:

Automatic Data Optimization is supported in Oracle Database 12c Release 2 multitenant environments.

See Also:

" [DBA\_ILMOBJECTS](DBA_ILMOBJECTS.md) "