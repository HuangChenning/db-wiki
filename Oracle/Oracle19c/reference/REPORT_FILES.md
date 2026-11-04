---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/REPORT_FILES.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.229 REPORT\_FILES

`REPORT_FILES` displays data for all of the XML schema and XSLT files associated with reports for a given component.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILENAME` | `VARCHAR2(500)` | `NOT NULL` | Name of the XSLT/XML schema file |
| `DATA` | `XMLTYPE` |  | XSLT/XML schema data |