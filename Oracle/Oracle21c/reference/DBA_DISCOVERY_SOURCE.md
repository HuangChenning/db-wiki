---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_DISCOVERY_SOURCE.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.292 DBA\_DISCOVERY\_SOURCE

`DBA_DISCOVERY_SOURCE` describes sensitive data discovery import information.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_NAME` | `VARCHAR2(128)` |  | The name of the discovery source. In the case of Application Data Model (ADM), this is the ADM instance name. |
| `SOURCE_TYPE` | `VARCHAR2(6)` |  | The type of the source:  - `ADM`: import from ADM - `CUSTOM`: custom import - `DB`: discovered within the database |
| `CTIME` | `TIMESTAMP(6)` |  | The last time sensitive data was imported from this source |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG856) for more information about transparent sensitive data protection