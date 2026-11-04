---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_TAB_PRIVS_RECD.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_TAB_PRIVS_RECD` describes the following types of grants:

- Object grants for which the current user is the grantee
- Object grants for which an enabled role or `PUBLIC` is the grantee

Related View

`USER_TAB_PRIVS_RECD` describes the object grants for which the current user is the grantee. This view does not display the `GRANTEE` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(128)` |  | Name of the user or role to whom access was granted |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the object |
| `GRANTOR` | `VARCHAR2(128)` |  | Name of the user who performed the grant |
| `PRIVILEGE` | `VARCHAR2(40)` |  | Privilege on the object |
| `GRANTABLE` | `VARCHAR2(3)` |  | Indicates whether the privilege was granted with the `GRANT OPTION` (`YES`) or not (`NO`) |
| `HIERARCHY` | `VARCHAR2(3)` |  | Indicates whether the privilege was granted with the `HIERARCHY OPTION` (`YES`) or not (`NO`) |
| `COMMON` | `VARCHAR2(3)` |  | Indicates how the grant was made. Possible values:  - `YES` if the privilege was granted commonly (`CONTAINER=ALL` was used) - `NO` if the privilege was granted locally (`CONTAINER=ALL` was not used) |
| `TYPE` | `VARCHAR2(24)` |  | Type of the object |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the privilege grant was inherited from another container (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |