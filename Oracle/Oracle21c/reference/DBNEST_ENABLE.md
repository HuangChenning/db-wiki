---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBNEST_ENABLE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.101 DBNEST\_ENABLE

`DBNEST_ENABLE` allows you to enable or disable dbNest.

Note:

This parameter is applicable only on Linux systems.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DBNEST_ENABLE = { NONE \| CDB_RESOURCE_PDB_ALL }` |
| Default value | `NONE` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | All instances should use the same value. |

DbNest provides operating system resource isolation and management, file system isolation, and secure computing for PDBs. The infrastructure is implemented as a Linux-specific package that provides hierarchical containers, called nests. A CDB resides within a single parent nest, while PDBs reside within the individual child nests created within the parent. The isolation and resource management properties of a nest are separate. A full nest includes both isolation and resource management. Alternatively, you can configure a partial nest that includes only resource management.

You can set the following values for this parameter:

- `NONE`: Disables dbNest. This is the default value.
- `CDB_RESOURCE_PDB_ALL`: Enables a resource management-only nest for the CDB and a full nest for each PDB.

Note:

This parameter is available starting with Oracle Database 21c.

See Also:

[Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=MULTI-GUID-BEE0A670-F46F-49DC-819B-6191361A6C8E) for information on securing and isolating resources using dbNest