---
title: REPORT_FILES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5165.htm
tags:
  - oracle
  - 11g
  - reference
---

`REPORT_FILES` displays data for all of the XML schema and XSLT files associated with reports for a given component.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPONENT_ID` | `NUMBER` |  | ID number of the database component building the report |
| `COMPONENT_NAME` | `VARCHAR2(30)` |  | Name of the database component building the report (for example, `sqltune` for SQL Tuning Advisor) |
| `FILENAME` | `VARCHAR2(500)` | `NOT NULL` | Name of the XSLT/XML schema file |
| `DATA` | `XMLTYPE` |  | XSLT/XML schema data |