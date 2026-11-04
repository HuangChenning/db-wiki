---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/REPORT_COMPONENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.231 REPORT\_COMPONENTS

`REPORT_COMPONENTS` displays metadata about different database components offering reports in XML, HTML, or Text formats.

Reports are first generated in XML and can then be translated into HTML or Text formats, for supported report types. Each component generates one or more reports containing different types of content. You can request reports using the component's own PL/SQL interface (for example, `DBMS_SQLTUNE` for SQL Tuning Advisor).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPONENT_ID` | `NUMBER` | `NOT NULL` | ID number of the database component building the report |
| `COMPONENT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the database component building the report (for example, `sqltune` for SQL Tuning Advisor) |
| `COMPONENT_DESCRIPTION` | `VARCHAR2(256)` |  | Component description |
| `REPORT_ID` | `NUMBER` | `NOT NULL` | ID number of the report type |
| `REPORT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the report type |
| `REPORT_DESCRIPTION` | `VARCHAR2(256)` |  | Description of the report type |
| `SCHEMA_FILENAME` | `VARCHAR2(500)` |  | Filename of the XML schema for the report (optional) |
| `SCHEMA_DATA` | `XMLTYPE` |  | XML schema for this report (optional) |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS220) for more information about the `DBMS_SQLTUNE` package