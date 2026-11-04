---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/UNIFIED_AUDIT_SYSTEMLOG.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.375 UNIFIED\_AUDIT\_SYSTEMLOG

`UNIFIED_AUDIT_SYSTEMLOG` specifies whether key fields of unified audit records will be written to the SYSLOG utility (on UNIX platforms) or to the Windows Event Viewer (on Windows). In a CDB, this parameter is a per-PDB static initialization parameter.

| Property | Description |
| --- | --- |
| Parameter type | String for UNIX platforms, Boolean for Windows |
| Syntax | On UNIX:  `UNIFIED_AUDIT_SYSTEMLOG = 'facility_clause.priority_clause'`  `facility_clause::=`  `{ USER \| LOCAL[ 0 \| 1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 7 ] }`  `priority_clause::=`  `{ NOTICE \| INFO \| DEBUG \| WARNING \| ERR \| CRIT \| ALERT \| EMERG }`  On Windows:  `UNIFIED_AUDIT_SYSTEMLOG = { FALSE \| TRUE }` |
| Default value | No default on UNIX platforms  `FALSE` on Windows |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

When this parameter is set on UNIX, key fields of unified audit records are written to SYSLOG. When this parameter is set on Windows, key fields of unified audit records are written to the Windows Event Viewer.

Do not set this parameter (or set it to `FALSE` on Windows) if you do not want key fields of unified audit records written to SYSLOG or the Windows Event Viewer.

When `UNIFIED_AUDIT_SYSTEMLOG` is enabled, the key fields of the unified audit records that are written to SYSLOG or Windows Event Viewer uniquely identify the detailed unified audit records in the `UNIFIED_AUDIT_TRAIL` view. Only a subset of the unified audit record fields are written to ensure that the audit record entries do not exceed the maximum allowed size for a SYSLOG entry (typically 1024 bytes).

This parameter differs from the `UNIFIED_AUDIT_COMMON_SYSTEMLOG` parameter in that it is set at the PDB level and enables the logging of unified audit records on a per-PDB basis, whereas `UNIFIED_AUDIT_COMMON_SYSTEMLOG` is set at the CDB level and enables all unified audit records from common unified audit policies to be consolidated into a single destination.

See Also:

- " [UNIFIED\_AUDIT\_COMMON\_SYSTEMLOG](UNIFIED_AUDIT_COMMON_SYSTEMLOG.md) "
- " [UNIFIED\_AUDIT\_TRAIL](UNIFIED_AUDIT_TRAIL.md) "
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG-GUID-9A2B93A7-4166-4F29-B406-4AE6C6141ADD) for a table that maps the names given to the unified audit records fields that are written to SYSLOG and the Windows Event Viewer to the corresponding column names in the `UNIFIED_AUDIT_TRAIL` view