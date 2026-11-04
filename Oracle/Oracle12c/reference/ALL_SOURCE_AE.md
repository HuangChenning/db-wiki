---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_SOURCE_AE.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_SOURCE_AE` describes the text source of the stored objects (across all editions) accessible to the current user.

Related Views

- `DBA_SOURCE_AE` describes the text source of all stored objects (across all editions) in the database.
- `USER_SOURCE_AE` describes the text source of the stored objects (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the object |
| `NAME` | `VARCHAR2(128)` |  | Name of the object |
| `TYPE` | `VARCHAR2(12)` |  | Type of the object:  - `TYPE` - `TYPE BODY` - `PROCEDURE` - `FUNCTION` - `PACKAGE` - `PACKAGE BODY` - `LIBRARY` - `JAVA SOURCE` |
| `LINE` | `NUMBER` |  | Line number of this line of source |
| `TEXT` | `VARCHAR2(4000)` |  | Source text |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the Edition |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |

See Also:

- " [DBA\_SOURCE\_AE](DBA_SOURCE_AE.md) "
- " [USER\_SOURCE\_AE](USER_SOURCE_AE.md) "