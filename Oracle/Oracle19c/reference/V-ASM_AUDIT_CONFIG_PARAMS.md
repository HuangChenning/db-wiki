---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-ASM_AUDIT_CONFIG_PARAMS.html
tags:
  - oracle
  - 19c
  - reference
---

## 7.60 V$ASM\_AUDIT\_CONFIG\_PARAMS

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_AUDIT_CONFIG_PARAMS` displays information about the currently configured audit trail properties that are used by the `DBMS_AUDIT_MGMT` package.

In a database instance, `V$ASM_AUDIT_CONFIG_PARAMS` displays no rows.

| Column | Datatype | Description |
| --- | --- | --- |
| `PARAMETER_NAME` | `VARCHAR2(64)` | Name of the property |
| `PARAMETER_VALUE` | `VARCHAR2(64)` | Value of the property |
| `AUDIT_TRAIL` | `VARCHAR2(64)` | Audit trails for which the property is configured: `OS AUDIT TRAIL` and `UNIFIED AUDIT TRAIL` |
| `PARAMETER_UNIT` <sup>Foot 1</sup> | `VARCHAR2(64)` | Provides description of units of audit properties (file size in KB and file age in day(s)) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 19c.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ARPLS241) for more information about the `DBMS_AUDIT_MGMT` package
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information