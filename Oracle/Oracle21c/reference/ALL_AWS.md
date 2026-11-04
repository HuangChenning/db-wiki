---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_AWS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.114 ALL\_AWS

`ALL_AWS` describes the analytic workspaces accessible to the current user.

Related Views

- `DBA_AWS` describes all analytic workspaces in the database.
- `USER_AWS` describes the analytic workspaces owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the analytic workspace |
| `AW_NUMBER` | `NUMBER` | `NOT NULL` | Number of the analytic workspace |
| `AW_NAME` | `VARCHAR2(128)` |  | Name of the analytic workspace |
| `AW_VERSION` | `VARCHAR2(4)` |  | Format version of the analytic workspace:  - `9.1` - `10.1` - `10.2` - `11.1` |
| `PAGESPACES` | `NUMBER` |  | Number of pagespaces in the analytic workspace |
| `GENERATIONS` | `NUMBER` |  | Number of active generations in the analytic workspace |
| `FROZEN` | `VARCHAR2(6)` |  | Freeze state of the analytic workspace:  - `Frozen` - `NoThaw` |

See Also:

- " [DBA\_AWS](DBA_AWS.md) "
- " [USER\_AWS](USER_AWS.md) "
- [Oracle OLAP User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OLAUG100) for more information about the OLAP option for Oracle Database