---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_APP_VERSIONS.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.97 DBA\_APP\_VERSIONS

`DBA_APP_VERSIONS` displays information about all application versions installed in an application container.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APP_NAME` | `VARCHAR2(128)` |  | Name of the application |
| `APP_VERSION` | `VARCHAR2(30)` |  | Version of the application |
| `APP_VERSION_COMMENT` | `VARCHAR2(4000)` |  | Comment associated with the application version |
| `APP_VERSION_CHECKSUM` | `NUMBER` |  | Checksum for the application version |
| `APP_ROOT_CLONE_NAME` <sup>Foot 1</sup> | `VARCHAR2(64)` |  | Name of the application root clone that corresponds to the application |
| `APP_VERSION_BEGIN_TIME` <sup>Foot 2</sup> | `DATE` |  | Begin time of the most recent sync of the application |
| `APP_VERSION_END_TIME` <sup>Foot 2</sup> | `DATE` |  | End time of the most recent sync of the application |
| `APP_VERSION_NUMBER` <sup>Foot 2</sup> | `NUMBER` |  | Version number of the application version |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 19c, Release Update 19.7.

<sup>Footnote 2</sup> This column is available only on Oracle Autonomous Database Serverless.

See Also:

[Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=MULTI-GUID-B964031E-8ACE-4603-8F1E-DD173BE5BA01) for more information about application containers