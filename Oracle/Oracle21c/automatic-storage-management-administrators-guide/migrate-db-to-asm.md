---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/migrate-db-to-asm.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

With a new installation of Oracle Database and Oracle ASM, you can initially create your database and select the Oracle ASM storage option. If you have an existing Oracle Database that stores database files in the operating system file system, then you can migrate some or all of your data files to Oracle ASM storage.

Oracle provides several methods for migrating your database to Oracle ASM. Using Oracle ASM enables you to realize the benefits of automation and simplicity in managing your database storage. To migrate to Oracle ASM, you can use the methods described in the following sections:

- About Using Oracle Recovery Manager to Migrate Databases to Oracle ASM
- Best Practices Technical Briefs on Migrating to Oracle ASM

Note:

You must upgrade to at least Oracle Database 10g before migrating your database to Oracle ASM.

### About Using Oracle Recovery Manager to Migrate Databases to Oracle ASM

You can use Oracle Recovery Manager (RMAN) to manually migrate to Oracle ASM. You can also use RMAN to migrate a single tablespace or data file to Oracle ASM.

For more information, see [Performing Oracle ASM Data Migration with RMAN](asm-migration-rman.md).

### Best Practices Technical Briefs on Migrating to Oracle ASM

The Oracle Maximum Availability Architecture (MAA) website provides excellent best practices technical technical briefs based on different scenarios, such as:

- Minimal Downtime Migration to Oracle ASM
- Platform Migration using Transportable Tablespaces
- Platform Migration using Transportable Database

See Also:

- Information about best practices for migrating to Oracle ASM on the Oracle Maximum Availability Architecture (MAA) website at [`https://www.oracle.com/database/technologies/high-availability/maa.html`](https://www.oracle.com/database/technologies/high-availability/maa.html)
- Additional information on the Oracle ASM website at [`https://www.oracle.com/database/technologies/rac/asm.html`](https://www.oracle.com/database/technologies/rac/asm.html)