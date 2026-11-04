---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PROCESSOR_GROUP_NAME.html
tags:
  - oracle
  - 12c
  - reference
---

`PROCESSOR_GROUP_NAME` specifies the name of the processor group that this instance should run in.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PROCESSOR_GROUP_NAME =` `string` |
| Default value | There is no default value |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | For Oracle RAC databases, it is recommended that the operating system processor groups for each database instance are all named the same, so that the same `PROCESSOR_GROUP_NAME` value can be used. However, you can choose to use different names. In this case, you would set the `PROCESSOR_GROUP_NAME` explicitly for each database instance. |

This initialization parameter is supported on the Linux and Solaris operating systems.

`PROCESSOR_GROUP_NAME` instructs the database instance to run itself within the specified operating system processor group. All Oracle processes will be bound to the CPUs in this group and will only run on these CPUs.

Notes:

- Oracle recommends that this parameter be set only for databases on which the `USE_DEDICATED_BROKER` initialization parameter is also set to `TRUE`.
- For NUMA systems, all SGA and PGA memory allocated by the database instance will be allocated from NUMA nodes within the group.

See Also:

- " [USE\_DEDICATED\_BROKER](USE_DEDICATED_BROKER.md) "
- [Oracle Database Administrator's Reference for Linux and UNIX-Based Operating Systems](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=UNXAR407) for more information about using the `PROCESSOR_GROUP_NAME` initialization parameter