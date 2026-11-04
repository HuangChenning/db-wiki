---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: F31734-10
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/glossary.html
tags:
  - oracle
  - 21c
  - multitenant-administrators-guide
---

### application

Within an application root, an application is a named, versioned set of data and metadata created by a common user. An application might include an application common user, an application common object, or some multiple and combination of the preceding.

**Parent topic:** Glossary

### application common object

A shared database object created while connected to an application root. The metadata (for a metadata-linked object) or data (for a data-linked common object) is shared by application PDBs in the application container.

**Parent topic:** Glossary

### application common user

A common user created while connected to an application root. The metadata (for a metadata-linked common object) or data (for a data-linked common object) is shared by application PDBs in the application container.

**Parent topic:** Glossary

### application container

A named set of application PDBs plugged in to an application root. An application container may contain an application seed.

**Parent topic:** Glossary

### application patch

In an application container, a small change to an application. Typical examples of patching include bug fixes and security patches. An application upgrade begins and ends with an `ALTER PLUGGABLE DATABASE APPLICATION` statement.

**Parent topic:** Glossary

### application PDB

A PDB that is plugged in to an application container.

**Parent topic:** Glossary

### application root

The root container within an application container. Every application container has exactly one application root. An application root shares some characteristics with the CDB root, because it can contain common objects, and some characteristics with a PDB, because it is created with the `CREATE PLUGGABLE DATABASE` statement.

**Parent topic:** Glossary

### application seed

An optional application PDB that serves as a template for creating other PDBs within an application container. An application container includes 0 or 1 application seed.

**Parent topic:** Glossary

### application upgrade

In an application container, a major change to the physical architecture of an application. An application upgrade begins and ends with an `ALTER PLUGGABLE DATABASE APPLICATION` statement.

**Parent topic:** Glossary

### CDB

An Oracle Database installation that contains at least one PDB. Starting in Oracle Database 21c, every Oracle database is a CDB.

**Parent topic:** Glossary

### CDB administrator

A database administrator who manages a CDB. A PDB administrator manages individual PDBs within the CDB.

**Parent topic:** Glossary

### CDB fleet

A collection of different CDBs that can be managed as one logical CDB.

**Parent topic:** Glossary

### CDB restore point

In a CDB, a restore point that is created when connected to the root, and when the FOR PLUGGABLE DATABASE clause is not specified. Unlike a PDB restore point, a CDB restore point is usable by all PDBs.

**Parent topic:** Glossary

### CDB root

In a multitenant container database (CDB), a collection of schemas, schema objects, and nonschema objects to which all PDBs belong. Every CDB has exactly one root container, which stores the system metadata required to manage PDBs. All PDBs belong to the CDB root.

**Parent topic:** Glossary

### clean restore point

A PDB restore point that is created when the PDB is closed. A Flashback PDB to a clean restore point does not require restoring backups or creating a temporary instance.

**Parent topic:** Glossary

### common object

An object that resides either in the CDB root or an application root that shares either data (a data-linked common object) or metadata (a metadata-linked common object). All common objects in the CDB root are Oracle-supplied. A common object in an application root is called an application common object.

**Parent topic:** Glossary

### common user

In a multitenant container database (CDB), a database user that exists with the same identity in multiple containers. A common user created in the CDB root has the same identity in every existing and future PDB. A common user created in an application container has the same identity in every existing and future application PDB in this application container.

**Parent topic:** Glossary

### container

In a multitenant container database (CDB), either the root or a PDB.

**Parent topic:** Glossary

### container data object

In a CDB, a table or view containing data pertaining to multiple containers and possibly the CDB as a whole, along with mechanisms to restrict data visible to specific common users through such objects to one or more containers. Examples of container data objects are Oracle-supplied views whose names begin with `V$` and `CDB_`.

**Parent topic:** Glossary

### cross-container operation

In a CDB, a DDL statement that affects the CDB itself, multiple containers, multiple common users or roles, or a container other than the one to which the user is connected. Only a common user connected to the root can perform cross-container operations.

**Parent topic:** Glossary

### data link

In a PDB, an internal mechanism that points to data (not metadata) in the root. For example, AWR data resides in the root. Each PDB uses an object link to point to the AWR data in the root, thereby making views such as `DBA_HIST_ACTIVE_SESS_HISTORY` and `DBA_HIST_BASELINE` accessible in each separate container.

**Parent topic:** Glossary

### database consolidation

The general process of moving data from one or more non-CDBs into a multitenant container database (CDB).

**Parent topic:** Glossary

### data-linked common object

A common object that exists either in the CDB root or an application root. The data, rather than the metadata, is shared by any PDB that contains a data link that points to the common object.

**Parent topic:** Glossary

### extended data-linked common object

A hybrid of a data-linked common object and a metadata-linked common object. For an extended data-linked object, each application PDB can create its own PDB-specific data while sharing the common data in the application root.

**Parent topic:** Glossary

### Fast Application Notification (FAN)

Applications can use FAN to enable rapid failure detection, balancing of connection pools after failures, and re-balancing of connection pools when failed components are repaired. The FAN notification process uses system events that Oracle Database publishes when cluster servers become unreachable or if network interfaces fail.

**Parent topic:** Glossary

### hot cloning

Cloning a PDB while the source PDB is open in read/write mode.

**Parent topic:** Glossary

### lead CDB

In a CDB fleet, the central location for monitoring and managing several CDBs.

**Parent topic:** Glossary

### local undo mode

The use of a separate set of undo data files for each PDB in a CDB.

**Parent topic:** Glossary

### local user

In a multitenant container database (CDB), any user that is not a common user.

**Parent topic:** Glossary

### metadata link

In a PDB, an internal mechanism that points to a dictionary object definition stored in the root. For example, the `OBJ$` table in each PDB uses a metadata link to point to the definition of `OBJ$` stored in the root.

**Parent topic:** Glossary

### metadata-linked common object

A common object that exists either in the CDB root or an application root. The metadata, rather than the data, is shared by any PDB that contains a metadata link that points to the common object.

**Parent topic:** Glossary

### multitenant architecture

The architecture that enables an Oracle database to function as a multitenant container database (CDB), which means that it can contain PDB s and application container s.

**Parent topic:** Glossary

### multitenant container database (CDB)

See CDB.

**Parent topic:** Glossary

### non-CDB

An Oracle database that is not a multitenant container database (CDB). Before Oracle Database 12c, all databases were non-CDBs. Starting in Oracle Database 21c, every database must be a CDB.

**Parent topic:** Glossary

### Oracle Multitenant

A database option that enables you to create multiple PDBs in a CDB.

**Parent topic:** Glossary

### PDB

In a multitenant container database (CDB), a portable collection of schemas, schema objects, and nonschema objects that appears to an Oracle Net client as a separate database.

**Parent topic:** Glossary

### PDB administrator

A database administrator who manages one or more PDBs. A CDB administrator manages the whole CDB.

**Parent topic:** Glossary

### PDB archive file

A compressed file that contains both PDB data files and an XML metadata file. You can create a PDB by specifying the archive file, and thereby avoid copying the XML file and the data files separately.

**Parent topic:** Glossary

### PDB lockdown profile

A security mechanism to restrict operations that are available to local users connected to a specified PDB. A typical use is to limit the effect of a grant privilege. For example, you limit the grant of `ALTER SYSTEM` to only those options whose names begin with `PLSQL`.

**Parent topic:** Glossary

### PDB performance profile

A specified share of system resources, CPU, parallel execution servers, and memory for a PDB or set of PDBs.

**Parent topic:** Glossary

### PDB restore point

Within a CDB, a restore point that usable only for a specific PDB. In contrast, a CDB restore point is usable by all PDBs.

**Parent topic:** Glossary

### PDB snapshot

A named, point-in-time copy of a PDB created using the `ALTER PLUGGABLE DATABASE SNAPSHOT` command. At the file level, a PDB snapshot is an archive file containing the contents of the PDB copy.

If the underlying file system supports sparse files, then the first snapshot is full, and every subsequent snapshot is sparse.

**Parent topic:** Glossary

### PDB synchronization

The user-initiated update of the application in an application PDB to the latest version and patch in the application root.

**Parent topic:** Glossary

### pluggable database (PDB)

See PDB.

**Parent topic:** Glossary

### proxy PDB

A PDB that references a PDB in a remote CDB using a database link. The remote PDB is called a referenced PDB.

**Parent topic:** Glossary

### referenced PDB

The PDB that is referenced by a proxy PDB. A local PDB is in the same CDB as its referenced PDB, whereas a remote PDB is in a different CDB.

**Parent topic:** Glossary

### refreshable clone PDB

A read-only clone that can periodically synchronize with its source PDB. Depending on the value in the `REFRESH MODE` clause, the synchronization occurs either automatically or manually.

**Parent topic:** Glossary

### resource plan

A container for resource plan directives that specify how resources are allocated to resource consumer groups.

**Parent topic:** Glossary

### resource plan directive

A set of limits and controls for CPU, physical I/O, or logical I/O consumption for sessions in a consumer group.

**Parent topic:** Glossary

### seed PDB

In a multitenant container database (CDB), a default pluggable database (PDB) that the system uses as a template for user-created PDBs. A PDB seed is either the system-supplied `PDB$SEED` or an application seed.

**Parent topic:** Glossary

### shared undo mode

In a single-instance CDB, only one active undo tablespace exists. For an Oracle RAC CDB, one active undo tablespace exists for every instance.

**Parent topic:** Glossary

### snapshot copy PDB

A PDB that is created by running the `CREATE PLUGGABLE DATABASE ... FROM ... SNAPSHOT COPY` command. A storage-managed snapshot is a copy of the underlying storage that is only supported on specific file systems.

Note:

A storage-managed snapshot, which is used to make a snapshot copy PDB, is different from a PDB-managed snapshot, which can be specified in a `CREATE PLUGGABLE DATABASE ... USING SNAPSHOT` command. Storage-managed snapshots are not involved in clones from PDB snapshots.

**Parent topic:** Glossary

### split mirror clone PDB

A PDB that is created by splitting a mirror in Oracle ASM.

**Parent topic:** Glossary

### system container

The container that includes the CDB root and all PDBs in the CDB.

**Parent topic:** Glossary

### unplugged PDB

A self-contained set of PDB data files, and an XML metadata file that specifies the locations of the PDB files.

**Parent topic:** Glossary