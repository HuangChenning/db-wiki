---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XSTREAM_ADMINISTRATOR.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.158 ALL\_XSTREAM\_ADMINISTRATOR

`ALL_XSTREAM_ADMINISTRATOR` displays information about the current users's granted privileges to be an XStream administrator by procedures in the `DBMS_XSTREAM_AUTH` package.

Related View

`DBA_XSTREAM_ADMINISTRATOR` displays information about the users who have been granted privileges to be XStream administrators by procedures in the `DBMS_XSTREAM_AUTH` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the user who has been granted privileges to be an XStream administrator |
| `PRIVILEGE_TYPE` | `VARCHAR2(7)` |  | Type of privilege granted:  - `APPLY` - `CAPTURE` - `*` - Both `APPLY` and `CAPTURE` |
| `GRANT_SELECT_PRIVILEGES` | `VARCHAR2(3)` |  | Shows whether set of privileges granted to the user (grantee) includes the `SELECT_CATALOG_ROLE` role, which enables the user to manage other XStream servers that belong to other XStream users.  Possible values:  - `YES`: The administrator has the `SELECT_CATALOG_ROLE` role and other privileges, is considered a full privilege administrator, and can manage other users' XStream configuration - `NO`: The administrator is considered a minimum privilege administrator, and can only manage XStream configurations where the apply\_user or capture\_user (based on the `PRIVILEGE_TYPE` column) matches the username. |
| `CREATE_TIME` | `TIMESTAMP(6)` |  | Time at which the privilege was granted |
| `LAST_MODIFIED` | `TIMESTAMP(6)` |  | Time at which the privilege was last modified |

See Also:

- " [DBA\_XSTREAM\_ADMINISTRATOR](DBA_XSTREAM_ADMINISTRATOR.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS73647) for more information about the `DBMS_XSTREAM_AUTH` package