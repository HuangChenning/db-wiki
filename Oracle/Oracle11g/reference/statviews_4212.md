---
title: DBA_REGISTRY_HISTORY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4212.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_REGISTRY_HISTORY` provides information about upgrades, downgrades, and critical patch updates that have been performed on the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ACTION_TIME` | `TIMESTAMP(6)` |  | The time the upgrade, downgrade, or patch action was completed |
| `ACTION` | `VARCHAR2(30)` |  | The specific action (for example, UPGRADE or DOWNGRADE) |
| `NAMESPACE` | `VARCHAR2(30)` |  | The namespace of the components affected (for example, SERVER) |
| `VERSION` | `VARCHAR2(30)` |  | The version number of the server (for example, 10.2.0.1.0) |
| `ID` | `NUMBER` |  | Bundle ID |
| `BUNDLE_SERIES` <sup>Foot 1</sup> | `VARCHAR2(30)` |  | Name of the bundle series (for example, CPU, PSU, or WINBUNDLE) |
| `COMMENTS` | `VARCHAR2(255)` |  | Additional comments about the action taken |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).