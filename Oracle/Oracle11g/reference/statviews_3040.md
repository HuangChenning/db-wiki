---
title: DBA_ADVISOR_SQLW_TEMPLATES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3040.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_SQLW_TEMPLATES` displays an aggregated picture of all SQLWkld template objects in the database.

Related View

`USER_ADVISOR_SQLW_TEMPLATES` displays an aggregated picture of the SQLWkld template objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the workload object |
| `WORKLOAD_ID` | `NUMBER` | `NOT NULL` | Unique identifier number of the workload object |
| `WORKLOAD_NAME` | `VARCHAR2(30)` |  | Unique name of the workload |
| `DESCRIPTION` | `VARCHAR2(256)` |  | User-specified description of the workload |
| `CREATE_DATE` | `DATE` | `NOT NULL` | Date on which the workload object was created |
| `MODIFY_DATE` | `DATE` | `NOT NULL` | Date of last update to the current workload |
| `SOURCE` | `VARCHAR2(30)` |  | Optional object or template on which the object was based |
| `READ_ONLY` | `VARCHAR2(5)` |  | Indicates whether the workload template can be modified or deleted (`TRUE`) or not (`FALSE`) |

See Also:

["USER\_ADVISOR\_SQLW\_TEMPLATES"](statviews_5222.md)