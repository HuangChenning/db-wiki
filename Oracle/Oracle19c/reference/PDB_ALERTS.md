---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/PDB_ALERTS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.213 PDB\_ALERTS

`PDB_ALERTS` contains descriptions of reasons for PDB alerts.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TIME` | `TIMESTAMP(6)` | `NOT NULL` | Time when the violation happened |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | A name of a PDB or non-CDB to which this record applies |
| `CAUSE_NO` | `NUMBER` | `NOT NULL` | Number identifying a specific reason for a PDB alert |
| `TYPE_NO` | `NUMBER` | `NOT NULL` | Type of the violation |
| `ERROR` | `NUMBER` |  | Oracle error, if any, for this violation |
| `LINE` | `NUMBER` | `NOT NULL` | Line number for the violation message |
| `MESSAGE` | `VARCHAR2(4000)` | `NOT NULL` | Description of the violation |
| `STATUS` | `NUMBER` |  | Status of the violation |
| `ACTION` | `VARCHAR2(4000)` |  | Actions to take to resolve the violations |