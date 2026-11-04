---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_AUDIT_LAST_ARCH_TS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.53 V$ASM\_AUDIT\_LAST\_ARCH\_TS

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_AUDIT_LAST_ARCH_TS` displays information about the last archive timestamps set for audit trail cleanup or purges.

In a database instance, `V$ASM_AUDIT_LAST_ARCH_TS` displays no rows.

| Column | Datatype | Description |
| --- | --- | --- |
| `AUDIT_TRAIL` | `VARCHAR2(64)` | Audit trail for which the last archive timestamp applies: `OS AUDIT TRAIL` and `UNIFIED AUDIT TRAIL` |
| `LAST_ARCHIVE_TS` | `TIMESTAMP(6) WITH TIME ZONE` | Timestamp of the last audit file that has been archived |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information