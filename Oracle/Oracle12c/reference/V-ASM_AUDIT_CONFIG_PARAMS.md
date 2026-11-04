---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-ASM_AUDIT_CONFIG_PARAMS.html
tags:
  - oracle
  - 12c
  - reference
---

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_AUDIT_CONFIG_PARAMS` displays information about the currently configured audit trail properties that are used by the `DBMS_AUDIT_MGMT` package.

In a database instance, `V$ASM_AUDIT_CONFIG_PARAMS` displays no rows.

| Column | Datatype | Description |
| --- | --- | --- |
| `PARAMETER_NAME` | `VARCHAR2(64)` | Name of the property |
| `PARAMETER_VALUE` | `VARCHAR2(64)` | Value of the property |
| `AUDIT_TRAIL` | `VARCHAR2(64)` | Audit trails for which the property is configured: `OS AUDIT TRAIL` and `UNIFIED AUDIT TRAIL` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS241) for more information about the `DBMS_AUDIT_MGMT` package
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information