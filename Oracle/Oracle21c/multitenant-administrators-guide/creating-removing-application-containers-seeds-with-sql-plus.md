---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: F31734-10
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/creating-removing-application-containers-seeds-with-sql-plus.html
tags:
  - oracle
  - 21c
  - multitenant-administrators-guide
---

You can create application containers and application seeds in several different ways. You can also remove application containers from a CDB, and you can remove application seeds from application containers.

- [About Application Containers](application-containers2.md)  
	An **application container** is an optional, user-created CDB component that stores data and metadata for one or more application back ends. A CDB includes zero or more application containers.
- [Creating Application Containers](creating-application-containers1.md)  
	You can create application containers in several different ways, including using the PDB seed, cloning an existing PDB, and plugging in an unplugged PDB by using the `CREATE PLUGGABLE DATABASE` statement.
- [Unplugging an Application Container from a CDB](unplugging-application-container-cdb.md)  
	You can unplug an application container from a CDB.
- [Dropping an Application Container](dropping-application-container.md)  
	You can drop an application container when you want to move the application container from one CDB to another or when you no longer need the application container.
- [Creating Application Seeds](creating-application-seeds.md)  
	You can create application seeds in several different ways, including using the PDB seed, cloning an existing PDB, and plugging in an unplugged PDB by using the `CREATE PLUGGABLE DATABASE` statement.
- [Unplugging an Application Seed from an Application Container](unplugging-application-seed-application-container.md)  
	You can unplug an application seed from an application container.
- [Dropping an Application Seed](dropping-application-seed.md)  
	You can use the `DROP` `PLUGGABLE` `DATABASE` statement to drop an application seed. You can drop an application seed when you no longer need it.
- [Creating an Application PDB](creating-application-pdb.md)  
	You create an application PDB by running the `CREATE PLUGGABLE DATABASE` statement with an application root as the current container.

See Also:

- " [About Application Containers](application-containers2.md) "
- " [Administering an Application Container](administering-application-containers-with-sql-plus.md) "

**Parent topic:** [Creating PDBs and Application Containers](creating-pdbs.md)