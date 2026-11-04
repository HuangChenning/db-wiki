---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PROCESSOR_GROUP_NAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.295 PROCESSOR\_GROUP\_NAME

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
- Starting with Oracle Database Appliance (ODA) release 19.9, you can use `PROCESSOR_GROUP_NAME` to specify the set of CPU cores on which the database on ODA will run. For more information, refer to [Oracle Database Appliance X8-2 Deployment and User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CMTXN-GUID-185A01BF-5A4B-4B38-8EFF-8FA635253DC1).

See Also:

" [USE\_DEDICATED\_BROKER](USE_DEDICATED_BROKER.md) "