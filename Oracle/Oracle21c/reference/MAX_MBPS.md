---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MAX_MBPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.207 MAX\_MBPS

`MAX_MBPS` enables you to set the maximum number of megabytes (MB) of I/Os issued per second on a per pluggable database (PDB) basis. This parameter is used to throttle PDB I/Os.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | 0 |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to the maximum `Integer` value. A very low value (for example, under 25 MB per second) is not recommended. |
| Basic | No |
| Oracle RAC | Different values can be set on different instances. |

DBWR I/Os, control file I/Os, password file I/Os and other critical I/Os are exempted from the throughput limit set by this parameter, but their I/Os are accounted for while throttling. Because of these exemptions, the PDB's actual I/O rate may sometimes exceed the limit.

This feature is enabled for multitenant container database (CDB) only. The feature is not supported on Oracle Exadata.

This parameter can be set from inside a PDB. If the parameter is set in CDB$ROOT, all the PDBs in that CDB will inherit the parameter value from CDB$ROOT. This parameter cannot be set in a non-CDB environment.

The default value of `0` means that no limits are set on the maximum number of megabytes (MB) of I/Os that can be issued per second in a PDB.

If Oracle processes need to wait because of this IO rate limit, the wait event is resmgr: I/O rate limit.

See Also:

- " [MAX\_IOPS](MAX_IOPS.md) "
- " [resmgr: I/O rate limit](descriptions-of-wait-events.md) "

Examples

This example shows how to use SQL statements to set a maximum of 200 megabytes per second on a PDB named CDB1\_PDB1:

```
alter session set container = cdb1_pdb1;
alter system set max_mbps = 200;
```