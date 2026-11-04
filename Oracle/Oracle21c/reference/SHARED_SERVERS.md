---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SHARED_SERVERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.339 SHARED\_SERVERS

`SHARED_SERVERS` specifies the number of server processes that you want to create when an instance is started. If system load decreases, then this minimum number of servers is maintained. Therefore, you should take care not to set `SHARED_SERVERS` too high at system startup.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0`, meaning that shared server is not on.  If you are using shared server architecture or if the `DISPATCHERS` parameter is set such that the total number of dispatchers is more than 0, then the default value is `1`. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | The value of this parameter should be less than `MAX_SHARED_SERVERS`. If it is greater than or equal to `MAX_SHARED_SERVERS`, then the number of servers will not be self-tuned but will remain constant, as specified by `SHARED_SERVERS`. |
| Basic | Yes |

Starting with Oracle Database 12c Release 1 (12.1.0.2), the `SHARED_SERVERS` parameter can be set on PDBs. However, unlike most other parameters that can be set on a PDB, this parameter can only be used within a PDB to enable or disable use of shared servers for that PDB. Therefore, in a PDB, the DBA can either set `SHARED_SERVERS` to 0 to disable use of shared servers for that PDB or use `ALTER SYSTEM RESET SHARED_SERVERS` to re-enable shared servers for the PDB. The configuration of shared servers for the CDB can only be done in the root.

See Also:

- " [DISPATCHERS](DISPATCHERS.md) "
- " [MAX\_SHARED\_SERVERS](MAX_SHARED_SERVERS.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11171) for more information on setting this parameter