---
title: Database Concepts
book: Database Concepts
doc_id: E96138-11
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/release-changes.html
tags:
  - oracle
  - 19c
  - concepts
---

## Changes in This Release for Oracle Database Concepts

This preface contains:

- Changes in Oracle Database Release 19c, Version 19.1
- Changes in Oracle Database Release 18c, Version 18.1

- Changes in Oracle Database Release 19c, Version 19.1  
	Oracle Database Concepts for Oracle Database release 19c, version 19.1 has the following changes.
- Changes in Oracle Database Release 18c, Version 18.1  
	Oracle Database Concepts for Oracle Database release 18c, version 18.1 has the following changes.

### Changes in Oracle Database Release 19c, Version 19.1

Oracle Database Concepts for Oracle Database release 19c, version 19.1 has the following changes.

- New Features  
	The following major features are new in this release:
- Desupported Features  
	The following features are desupported in this release.

**Parent topic:** Changes in This Release for Oracle Database Concepts

#### New Features

The following major features are new in this release:

- Deferred inserts
	Applications can stream single-row inserts into special buffers stored in the large pool. The inserts are “deferred” because the database writes these buffers to data files asynchronously. The inserts are committed automatically and cannot be rolled back.
	See " [Large Pool Buffers for Deferred Inserts](memory-architecture.md) ".
- Hybrid partitioned tables
	A table can contain internal and external partitions. Internal partitions consume space inside the database (segments). External partitions are stored outside the database using external table functionality. For example, a sales table might contain two partitions stored in data files and three partitions stored in text files.
	See " [Segments for Partitioned Tables](partitions-views-and-other-schema-objects.md) ".

**Parent topic:** Changes in Oracle Database Release 19c, Version 19.1

#### Desupported Features

The following features are desupported in this release.

- Oracle Multimedia
	Starting in Oracle Database 19c, Oracle Multimedia is desupported. Unless deselected, the Oracle Multimedia component (ORDIM) in dba\_registry displays as VALID in upgraded and newly created databases. Oracle Locator (installed with Oracle Multimedia if Spatial and Graph is not installed) continues to be installed and supported. Oracle recommends that you store multimedia content in SecureFiles LOBs, and use third-party products for image processing and conversion.
	See " [SecureFiles](concepts-for-database-developers.md) ".
- Oracle Streams
	Starting in Oracle Database 19c, Oracle Streams is desupported.
	See " [Oracle GoldenGate](topics-for-database-administrators-and-developers.md) ".

**Parent topic:** Changes in Oracle Database Release 19c, Version 19.1

### Changes in Oracle Database Release 18c, Version 18.1

Oracle Database Concepts for Oracle Database release 18c, version 18.1 has the following changes.

- New Features  
	The following major features are new in this release:
- Deprecated Features  
	The following features are deprecated in this release, and may be desupported in a future release:

**Parent topic:** Changes in This Release for Oracle Database Concepts

#### New Features

The following major features are new in this release:

- Memoptimize pool
	Oracle Database supports high-performance reads for tables specified with the `MEMOPTIMIZE FOR READ` clause. The buffers are cached in a new area in the SGA called the [memoptimize pool](Chunk806120860.md).
	See " [Memoptimize Pool](memory-architecture.md) ".
- Private temporary tables
	Private temporary tables are temporary database objects that are automatically dropped at the end of a transaction or a session. A private temporary table is stored in memory and is visible only to the session that created it. A private temporary table confines the scope of a temporary table to a session or a transaction, thus providing more flexibility in application coding, leading to easier code maintenance and better ready-to-use functionality.
	See " [Overview of Temporary Tables](tables-and-table-clusters.md) ".
- Shadow lost write protection
	A lost write occurs when the database thinks it has written a block to storage, but the write did not occur. A shadow tablespace enables the database to catch the majority of lost writes without requiring the use of a standby database and without the possibility of cascading errors.
	See " [Shadow Tablespaces](logical-storage-structures.md) ".

**Parent topic:** Changes in Oracle Database Release 18c, Version 18.1

#### Deprecated Features

The following features are deprecated in this release, and may be desupported in a future release:

- Oracle Multimedia
	Starting in Oracle Database 18c, Oracle Multimedia is deprecated. Oracle recommends that you store multimedia content in SecureFiles LOBs, and use third-party products for image processing and conversion.
	See " [SecureFiles](concepts-for-database-developers.md) ".

**Parent topic:** Changes in Oracle Database Release 18c, Version 18.1