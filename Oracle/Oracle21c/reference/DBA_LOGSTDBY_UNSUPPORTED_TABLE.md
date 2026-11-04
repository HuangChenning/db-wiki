---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_LOGSTDBY_UNSUPPORTED_TABLE.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.172 DBA\_LOGSTDBY\_UNSUPPORTED\_TABLE

`DBA_LOGSTDBY_UNSUPPORTED_TABLE` displays the data tables that are unsupported by logical standby.

The query results for this view depend on whether the database is currently undergoing a manual rolling upgrade performed using transient logical standby databases. If the database is undergoing such an upgrade, then this view displays information about tables in the database that are unsupported for transient logical standby. If the database is not undergoing such an upgrade, then this view displays information about tables in the database are unsupported for logical standby.

The data displayed pertains to the container in which the view is queried.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the unsupported table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the unsupported table |
| `EXPLANATION` <sup>Foot 1</sup> | `VARCHAR2(4000)` |  | If the database is currently undergoing a manual rolling upgrade performed using transient logical standby databases, then this column displays the reason the table is unsupported for transient logical standby. Otherwise, this column displays the reason the table is unsupported for logical standby.  This column is populated only when the value of the `COMPATIBLE` initialization parameter is `20.0` or higher. |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.