---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/different-releases-asm-db-instances.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

Oracle Automatic Storage Management (Oracle ASM) 18c supports Oracle Database 18c or older software versions, including Oracle Database 10g Release 1 (10.1).

Note:

- An Oracle ASM instance must be at Oracle ASM 18c to support Oracle Database 18c.
- Refer to Oracle Exadata documentation for information about the Oracle Database versions that Oracle ASM supports when Oracle Exadata storage is present.
- There are additional compatibility considerations when using disk groups with different releases of Oracle ASM and database instances.

When using different software versions, the database instance supports Oracle ASM functionality of the earliest release in use. For example, an Oracle Database 10g Release 1 (10.1) database instance operating with an Oracle ASM 18c instance only supports Oracle ASM 10g Release 1 (10.1) features.

The `V$ASM_CLIENT` view contains the `SOFTWARE_VERSION` and `COMPATIBLE_VERSION` columns with information about the software version number and instance compatibility level.

- The `SOFTWARE_VERSION` column of `V$ASM_CLIENT` contains the software version number of the database or Oracle ASM instance for the selected disk group connection.
- The `COMPATIBLE_VERSION` column contains the setting of the `COMPATIBLE` parameter of the database or Oracle ASM instance for the selected disk group connection.

You can query the `V$ASM_CLIENT` view on both Oracle ASM and database instances.

See Also:

- [Disk Group Compatibility](diskgroup-compatibility.md) for information about disk group compatibility attributes settings
- [Example 6-5](views-asm-info.md) for an example showing a query on the `V$ASM_CLIENT` view
- [Views Containing Oracle ASM Information](views-asm-info.md) for more information about the `V$ASM_CLIENT` and `V$ASM_*` views