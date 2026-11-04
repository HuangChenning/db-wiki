---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_AW_PS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.113 ALL\_AW\_PS

`ALL_AW_PS` describes the page spaces in the analytic workspaces accessible to the current user.

Related Views

- `DBA_AW_PS` describes the page spaces in all analytic workspaces in the database.
- `USER_AW_PS` describes the page spaces in the analytic workspaces owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the analytic workspace |
| `AW_NUMBER` | `NUMBER` | `NOT NULL` | Number of the analytic workspace |
| `AW_NAME` | `VARCHAR2(128)` |  | Name of the analytic workspace |
| `PSNUMBER` | `NUMBER(10)` |  | Number of the page space |
| `GENERATIONS` | `NUMBER` |  | Number of active generations in the page space |
| `MAXPAGES` | `NUMBER` |  | Maximum pages allocated in the page space |

See Also:

- " [DBA\_AW\_PS](DBA_AW_PS.md) "
- " [USER\_AW\_PS](USER_AW_PS.md) "
- [Oracle OLAP User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OLAUG100) for more information about the OLAP option for Oracle Database