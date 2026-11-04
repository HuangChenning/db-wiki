---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ASM_PREFERRED_READ_FAILURE_GROUPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.22 ASM\_PREFERRED\_READ\_FAILURE\_GROUPS

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `ASM_PREFERRED_READ_FAILURE_GROUPS = ‘<diskgroup_name>.<failure_group_name>, ...’` |
| Default value | NULL |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | The value is different on different nodes |

Note:

The `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter is deprecated in Oracle Database 12c Release 2 (12.2.0.1) and may be desupported in a future release. It is replaced by the `PREFERRED_READ.ENABLED` disk group attribute.

See [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG-GUID-F3E0FDDE-125D-4D7B-B3F5-8EE81DC1D3FB) for more information about the `PREFERRED_READ.ENABLED` disk group attribute.

To reset the parameter value to null, issue the following statement, which updates the server parameter file (SP file), then reboot Oracle ASM so that the change takes effect:

```
alter system reset asm_preferred_read_failure_groups;
```

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10145) for more information about this parameter