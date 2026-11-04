---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_APP_VERSIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.110 DBA\_APP\_VERSIONS

`DBA_APP_VERSIONS` displays information about all application versions installed in an application container.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APP_NAME` | `VARCHAR2(128)` |  | Name of the application |
| `APP_VERSION` | `VARCHAR2(30)` |  | Version of the application |
| `APP_VERSION_COMMENT` | `VARCHAR2(4000)` |  | Comment associated with the application version |
| `APP_VERSION_CHECKSUM` | `NUMBER` |  | Checksum for the application version |
| `APP_ROOT_CLONE_NAME` | `VARCHAR2(64)` |  | Name of the application root clone that corresponds to the application |

See Also:

[Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=MULTI-GUID-B964031E-8ACE-4603-8F1E-DD173BE5BA01) for more information about application containers