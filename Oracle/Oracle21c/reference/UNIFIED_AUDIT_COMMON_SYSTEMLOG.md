---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/UNIFIED_AUDIT_COMMON_SYSTEMLOG.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.374 UNIFIED\_AUDIT\_COMMON\_SYSTEMLOG

`UNIFIED_AUDIT_COMMON_SYSTEMLOG` specifies whether key fields of unified audit records generated due to common audit policies will be written to the SYSLOG utility.

Note:

This initialization parameter is supported only on UNIX platforms.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `UNIFIED_AUDIT_COMMON_SYSTEMLOG = 'facility_clause.priority_clause'`  `facility_clause::=`  `{ USER \| LOCAL[ 0 \| 1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 7 ] }`  `priority_clause::=`  `{ NOTICE \| INFO \| DEBUG \| WARNING \| ERR \| CRIT \| ALERT \| EMERG }` |
| Default value | None |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

When this parameter is set, key fields of unified audit records generated due to common audit policies are written to SYSLOG. These fields uniquely identify the detailed unified audit records in the `UNIFIED_AUDIT_TRAIL` view. Only a subset of unified audit record fields are written to ensure that the audit record entries do not exceed the maximum allowed size for a SYSLOG entry (typically 1024 bytes).

Do not set this parameter if you do not want key fields of unified audit records generated due to common audit policies written to SYSLOG.

This parameter differs from the `UNIFIED_AUDIT_SYSTEMLOG` parameter in that it is set at the CDB level and enables all unified audit records from common unified audit policies to be consolidated into a single destination, whereas `UNIFIED_AUDIT_SYSTEMLOG` is set at the PDB level and enables the logging of unified audit records on a per-PDB basis.

See Also:

- " [UNIFIED\_AUDIT\_SYSTEMLOG](UNIFIED_AUDIT_SYSTEMLOG.md) "
- " [UNIFIED\_AUDIT\_TRAIL](UNIFIED_AUDIT_TRAIL.md) "
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG-GUID-9A2B93A7-4166-4F29-B406-4AE6C6141ADD) for a table that maps the names given to the unified audit records fields that are written to SYSLOG to the corresponding column names in the `UNIFIED_AUDIT_TRAIL` view