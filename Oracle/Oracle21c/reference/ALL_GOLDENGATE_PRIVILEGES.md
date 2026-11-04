---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_GOLDENGATE_PRIVILEGES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.202 ALL\_GOLDENGATE\_PRIVILEGES

Oracle GoldenGate privileges are granted using the `DBMS_GOLDENGATE_AUTH` package.

Related Views

- `DBA_GOLDENGATE_PRIVILEGES` displays details about Oracle GoldenGate privileges for all users who have been granted Oracle GoldenGate privileges.
- `USER_GOLDENGATE_PRIVILEGES` displays details about Oracle GoldenGate privileges. This view does not display the `USERNAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the user that is granted the privilege |
| `PRIVILEGE_TYPE` | `VARCHAR2(7)` |  | Type of privilege granted:  - `APPLY` - `CAPTURE` - \*: Both `APPLY` and `CAPTURE` |
| `GRANT_SELECT_PRIVILEGES` | `VARCHAR2(3)` |  | Shows whether the set of privileges granted to the administrator make the administrator a full privilege administrator or a minimum privilege administrator:  - `YES`: The administrator has the `SELECT_CATALOG_ROLE` role and other privileges, is considered a full privilege administrator, and can manage any Oracle GoldenGate configuration. - `NO`: The administrator is considered a minimum privilege administrator, and can only manage Oracle GoldenGate configurations where the apply\_user or capture\_user (based on the `PRIVILEGE_TYPE` column) matches the username. |
| `CREATE_TIME` | `TIMESTAMP(6)` |  | Time at which the privilege was granted |
| `LAST_MODIFIED` | `TIMESTAMP(6)` |  | Time at which the privilege was last modified |