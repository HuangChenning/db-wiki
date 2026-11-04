---
title: ALL_AWS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1023.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_AWS` describes the analytic workspaces accessible to the current user.

Related Views

- `DBA_AWS` describes all analytic workspaces in the database.
- `USER_AWS` describes the analytic workspaces owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the analytic workspace |
| `AW_NUMBER` | `NUMBER` |  | Number of the analytic workspace |
| `AW_NAME` | `VARCHAR2(30)` |  | Name of the analytic workspace |
| `AW_VERSION` | `VARCHAR2(4)` |  | Format version of the analytic workspace: |
| `PAGESPACES` | `NUMBER` |  | Number of pagespaces in the analytic workspace |
| `GENERATIONS` | `NUMBER` |  | Number of active generations in the analytic workspace |
| `FROZEN` | `VARCHAR2(6)` |  | Freeze state of the analytic workspace: |

See Also:

- ["DBA\_AWS"](statviews_3094.md)
- ["USER\_AWS"](statviews_5239.md)
- [Oracle OLAP User's Guide](https://docs.oracle.com/cd/E11882_01/olap.112/e17123/toc.htm) for more information about these views