---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ENABLE_GOLDENGATE_REPLICATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.122 ENABLE\_GOLDENGATE\_REPLICATION

`ENABLE_GOLDENGATE_REPLICATION` controls services provided by the RDBMS for Oracle GoldenGate (both capture and apply services).

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | All instances must have the same setting |

Set this parameter to `true` to enable RDBMS services used by Oracle GoldenGate.

This parameter primarily controls supplemental logging required to support logical replication of new data types and operations. The redo log file is designed to be applied physically to a database, therefore the default contents of the redo log file often do not contain sufficient information to allow logged changes to be converted into SQL statements. Supplemental logging adds extra information into the redo log files so that replication can convert logged changes into SQL statements without having to access the database for each change. Previously these extra changes were controlled by the supplemental logging DDL. Now the `ENABLE_GOLDENGATE_REPLICATION` parameter must also be set to enable the required supplemental logging for any new data types or operations.

All enhancements to supplemental logging required to support logical replication are also controlled by this parameter.

The RDBMS services controlled by this parameter also include (but are not limited to):

- Transparent Data Encryption (including Tablespace Encryption) utilities used by GoldenGate Extract
- Service to read redo logs used by GoldenGate Extract
- Service to suppress triggers used by GoldenGate Replicat
- Service to handle transient duplicate handling used by GoldenGate Replicat
- Service to bypass referential integrity checking used by GoldenGate Replicat
- Services required to run Oracle GoldenGate in Integrated Extract and Integrated Replicat

Note:

When this database parameter is set to `true`, you must have a valid Oracle GoldenGate license or an authorized managed cloud client to use the enabled features. GoldenGate licenses or authorized managed cloud clients are required for all 3rd party or end-user tools that are used with this feature. Refer to [Oracle GoldenGate Licensing Information](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OGGLC) and ensure that you have obtained the appropriate licensing before setting this parameter to `true`.