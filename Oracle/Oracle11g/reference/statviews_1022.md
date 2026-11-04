---
title: ALL_AW_PS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1022.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_AW_PS` describes the page spaces in the analytic workspaces accessible to the current user.

Related Views

- `DBA_AW_PS` describes the page spaces in all analytic workspaces in the database.
- `USER_AW_PS` describes the page spaces in the analytic workspaces owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the analytic workspace |
| `AW_NUMBER` | `NUMBER` | `NOT NULL` | Number of the analytic workspace |
| `AW_NAME` | `VARCHAR2(30)` |  | Name of the analytic workspace |
| `PSNUMBER` | `NUMBER(10)` |  | Number of the page space |
| `GENERATIONS` | `NUMBER` |  | Number of active generations in the page space |
| `MAXPAGES` | `NUMBER` |  | Maximum pages allocated in the page space |

See Also:

- ["DBA\_AW\_PS"](statviews_3093.md)
- ["USER\_AW\_PS"](statviews_5238.md)
- [Oracle OLAP User's Guide](https://docs.oracle.com/cd/E11882_01/olap.112/e17123/toc.htm) for more information about these views