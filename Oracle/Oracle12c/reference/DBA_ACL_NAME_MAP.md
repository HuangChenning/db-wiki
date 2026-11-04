---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_ACL_NAME_MAP.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_ACL_NAME_MAP` maps new names of the access control lists for PL/SQL network utility packages from old XDB names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `XDB_NAME` | `VARCHAR2(4000)` | `NOT NULL` | The old XDB name of the access control list |
| `ACL` | `VARCHAR2(128)` |  | The new name of the access control list |
| `ACL_OWNER` | `VARCHAR2(128)` |  | The owner of the access control list |