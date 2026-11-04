---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_APP_VERSIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_APP_VERSIONS` displays information about all application versions installed in an application container.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APP_NAME` | `VARCHAR2(128)` |  | Name of the application |
| `APP_VERSION` | `VARCHAR2(30)` |  | Version of the application |
| `APP_VERSION_COMMENT` | `VARCHAR2(4000)` |  | Comment associated with the application version |

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN-GUID-127F2E91-351D-49CE-8254-380C4E33813D) for more information about application containers