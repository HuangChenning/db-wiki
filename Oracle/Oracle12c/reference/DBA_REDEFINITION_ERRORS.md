---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_REDEFINITION_ERRORS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_REDEFINITION_ERRORS` is an online redefinition view. It displays the dependent objects for which errors were raised while attempting to create similar objects on the interim table of the redefinition.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_TYPE` | `VARCHAR2(12)` |  | Type of the redefinition object:  - `TABLE` - `INDEX` - `CONSTRAINT` - `TRIGGER` - `NESTED TABLE` - `PARTITION` - `MV LOG` |
| `OBJECT_OWNER` | `VARCHAR2(4000)` |  | Owner of the redefinition object |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the redefinition object |
| `BASE_TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the base table of the redefinition object |
| `BASE_TABLE_NAME` | `VARCHAR2(128)` |  | Name of the base table of the redefinition object |
| `DDL_TXT` | `CLOB` |  | DDL used to create the corresponding interim redefinition object |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Reserved for future use |
| `ERR_NO` | `NUMBER(38)` |  | Oracle error number corresponding to this error |
| `ERR_TXT` | `VARCHAR2(1000)` |  | Oracle error text corresponding to this error |

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN11668) for more information about online redefinition