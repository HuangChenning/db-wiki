---
title: DBA_AUDIT_MGMT_CONFIG_PARAMS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3074.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_AUDIT_MGMT_CONFIG_PARAMS` displays information about the currently configured audit trail properties that are used by the `DBMS_AUDIT_MGMT` PL/SQL package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PARAMETER_NAME` | `VARCHAR2(1024)` | `NOT NULL` | Name of the property |
| `PARAMETER_VALUE` | `VARCHAR2(4000)` |  | Value of the property |
| `AUDIT_TRAIL` | `VARCHAR2(28)` |  | Audit trails for which the property is configured: |