---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/OFS_THREADS.html
tags:
  - oracle
  - 12c
  - reference
---

`OFS_THREADS` sets the maximum number of Oracle file system (OFS) threads that can be started to service Oracle file system requests.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `4` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `2` to `128` |
| Basic | No |
| Oracle RAC | The same value should be specified on all instances. |

Note:

This initialization parameter is supported only on the Linux operating system.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN-GUID-CDE9CC7F-237D-4699-A0D9-C7ED698D70E3) for more information about the Oracle Database NFS server feature