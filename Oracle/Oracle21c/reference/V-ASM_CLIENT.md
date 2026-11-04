---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_CLIENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.54 V$ASM\_CLIENT

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_CLIENT` identifies databases using disk groups managed by the Oracle ASM instance.

In a database instance, `V$ASM_CLIENT` displays information about the Oracle ASM instance if the database has any open Oracle ASM files.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Number of the disk group being used by the database instance (foreign key to the `V$ASM_DISKGROUP` view). When a client is connected to an Oracle ASM instance, but is not currently using any disk groups, `V$ASM_CLIENT.GROUP_NUMBER` contains `0`.  When the Cluster Ready Services Daemon (CRSD) or Cluster Synchronization Services (OCSSD) connects to the Oracle ASM instance, this will represent the number of the disk group used for their OCR and voting files respectively. |
| `INSTANCE_NAME` | `VARCHAR2(64)` | Identifier for the database instance client  When CRSD or OCSSD has opened its files in the disk group mounted by the Oracle ASM instance, this will contain the node name where CRSD or OCSSD is running. |
| `DB_NAME` | `VARCHAR2(8)` | Unique database name of the database client instance  When CRSD has opened the Oracle Cluster Registry (OCR) file in the disk group mounted by the Oracle ASM instance, `DB_NAME` will contain `_OCR`.  When OCSSD has opened the voting file in the disk group mounted by the Oracle ASM instance, `DB_NAME` will contain `_CSS`. |
| `CLUSTER_NAME` | `VARCHAR2(31)` | Name of the cluster |
| `STATUS` | `VARCHAR2(12)` | Status of the client connection:  - `CONNECTED` - Database instance client has an active connection to the Oracle ASM instance - `DISCONNECTED` - Database instance client normally ended its connection to the Oracle ASM instance - `BROKEN` - Connection with the database instance client terminated in a nonstandard way  When CRSD or OCSSD has opened its files in the disk group mounted by the Oracle ASM instance, it will report `Connected` as status. |
| `SOFTWARE_VERSION` | `VARCHAR2(60)` | Software version number of the database or Oracle ASM instance for the selected disk group connection |
| `COMPATIBLE_VERSION` | `VARCHAR2(60)` | Compatibility setting of the database or Oracle ASM instance for the selected disk group connection  The value will be `-` when CRSD or OCSSD has opened its files in the disk group mounted by the Oracle ASM instance. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

Note:

In an Oracle Database instance, this view returns 0 rows when queried from a PDB.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information