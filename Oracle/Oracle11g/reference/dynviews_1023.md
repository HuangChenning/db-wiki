---
title: "V$ASM_CLIENT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1023.htm
tags:
  - oracle
  - 11g
  - reference
---

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_CLIENT` identifies databases using disk groups managed by the Oracle ASM instance. In a database instance, `V$ASM_CLIENT` displays information about the Oracle ASM instance if the database has any open Oracle ASM files.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Number of the disk group being used by the client database instance (foreign key to the `V$ASM_DISKGROUP` view) |
| `INSTANCE_NAME` | `VARCHAR2(64)` | Identifier for the database instance client |
| `DB_NAME` | `VARCHAR2(8)` | Unique database name of the database client instance |
| `STATUS` | `VARCHAR2(12)` | Status of the client connection: - `CONNECTED` - Database instance client has an active connection to the Oracle ASM instance - `DISCONNECTED` - Database instance client normally ended its connection to the Oracle ASM instance - `BROKEN` - Connection with the database instance client terminated abnormally |
| `SOFTWARE_VERSION` | `VARCHAR2(60)` | Software version number of the database or Oracle ASM instance for the selected disk group connection |
| `COMPATIBLE_VERSION` | `VARCHAR2(60)` | Compatibility setting of the database or Oracle ASM instance for the selected disk group connection |