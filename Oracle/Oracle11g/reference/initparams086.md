---
title: ENABLE_GOLDENGATE_REPLICATION
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams086.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | false |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | All instances must have the same setting |

`ENABLE_GOLDENGATE_REPLICATION` controls services provided by the RDBMS for Oracle GoldenGate (both capture and apply services). Set this to `true` to enable RDBMS services used by Oracle GoldenGate.

This parameter primarily controls supplemental logging required to support logical replication of new data types and operations. The redo log file is designed to be applied physically to a database, therefore the default contents of the redo log file often do not contain sufficient information to allow logged changes to be converted into SQL statements. Supplemental logging adds extra information into the redo log files so that replication can convert logged changes into SQL statements without having to access the database for each change. Previously these extra changes were controlled by the supplemental logging DDL. Now the `ENABLE_GOLDENGATE_REPLICATION` parameter must also be set to enable the required supplemental logging for any new data types or operations.

All enhancements to supplemental logging required to support logical replication are also controlled by this parameter.

The RDBMS services controlled by this parameter also include (but are not limited to):

- Transparent Data Encryption (including Tablespace Encryption) utilities used by GoldenGate Extract
- Service to read redo logs used by GoldenGate Extract
- Service to suppress triggers used by GoldenGate Replicat
- Service to handle transient duplicate handling used by GoldenGate Replicat
- Service to bypass referential integrity checking used by GoldenGate Replicat
- Services required to run Oracle GoldenGate in Integrated Extract and Integrated Replicat

See Also:

[Oracle GoldenGate Installing and Configuring Oracle GoldenGate for Oracle Database](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GIORA983) for more information about the `ENABLE_GOLDENGATE_REPLICATION` initialization parameter