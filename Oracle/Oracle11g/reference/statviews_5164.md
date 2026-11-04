---
title: REPORT_COMPONENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5164.htm
tags:
  - oracle
  - 11g
  - reference
---

`REPORT_COMPONENTS` displays metadata about different database components offering reports in XML, HTML, or Text formats. Reports are first generated in XML and can then be translated into HTML or Text formats, for supported report types. Each component generates one or more reports containing different types of content. You can request reports using the component's own PL/SQL interfaces (for example, `DBMS_SQLTUNE` for SQL Tuning Advisor) or using the `DBMS_REPORT` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPONENT_ID` | `NUMBER` | `NOT NULL` | ID number of the database component building the report |
| `COMPONENT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the database component building the report (for example, `sqltune` for SQL Tuning Advisor) |
| `COMPONENT_DESCRIPTION` | `VARCHAR2(256)` |  | Component description |
| `REPORT_ID` | `NUMBER` | `NOT NULL` | ID number of the report type |
| `REPORT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the report type |
| `REPORT_DESCRIPTION` | `VARCHAR2(256)` |  | Description of the report type |
| `SCHEMA_FILENAME` | `VARCHAR2(500)` |  | Filename of the XML schema for the report (optional) |
| `SCHEMA_DATA` | `XMLTYPE` |  | XML schema for this report (optional) |