---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/REPORT_FILES.html
tags:
  - oracle
  - 12c
  - reference
---

`REPORT_FILES` displays data for all of the XML schema and XSLT files associated with reports for a given component.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILENAME` | `VARCHAR2(500)` | `NOT NULL` | Name of the XSLT/XML schema file |
| `DATA` | `XMLTYPE` |  | XSLT/XML schema data |