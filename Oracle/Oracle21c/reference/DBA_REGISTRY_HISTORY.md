---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_REGISTRY_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.282 DBA\_REGISTRY\_HISTORY

`DBA_REGISTRY_HISTORY` provides information about upgrades, downgrades, and critical patch updates that have been performed on the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ACTION_TIME` | `TIMESTAMP(6)` |  | The time the upgrade, downgrade, or patch action was completed |
| `ACTION` | `VARCHAR2(30)` |  | The specific action (for example, UPGRADE or DOWNGRADE) |
| `NAMESPACE` | `VARCHAR2(30)` |  | The namespace of the components affected (for example, SERVER) |
| `VERSION` | `VARCHAR2(30)` |  | The version number of the server (for example, 10.2.0.1.0) |
| `ID` | `NUMBER` |  | Bundle ID |