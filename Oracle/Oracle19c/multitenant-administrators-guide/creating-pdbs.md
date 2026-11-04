---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: E96136-19
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/creating-pdbs.html
tags:
  - oracle
  - 19c
  - multitenant-administrators-guide
---

## Part III Creating and Removing PDBs and Application Containers

You can create PDBs, application containers, and application seeds using a variety of techniques.

For example, you can create a PDB from scratch, cloning an existing PDB or non-CDB, or plug in an unplugged PDB. You can also remove PDBs from a CDB.

Note:

You can complete the tasks in this part using SQL\*Plus or Oracle SQL Developer.

- [Overview of PDB Creation](overview-of-pdb-creation.md)  
	A CDB supports multiple techniques for creating PDBs.
- [Creating a PDB from Scratch](creating-a-pdb-from-scratch.md)  
	Use the `CREATE PLUGGABLE DATABASE` statement to create a PDB in a CDB using the files of the PDB seed (`PDB$SEED`).
- [Cloning a PDB or Non-CDB](cloning-a-pdb.md)  
	You can create a PDB by cloning a local PDB, a remote PDB, or a non-CDB.
- [Relocating a PDB](relocating-a-pdb.md)  
	You can move a PDB to a different CDB or application container.
- [Plugging In an Unplugged PDB](plugging-in-a-pdb.md)  
	You can create a PDB by plugging an unplugged PDB into a CDB.
- [Creating a PDB as a Proxy PDB](creating-a-proxy-pdb.md)  
	You can create a PDB as a proxy PDB by referencing it in a remote CDB.
- [Removing a PDB](removing-a-pdb.md)  
	You can remove a plugged-in PDB from a CDB by unplugging it, dropping it, or relocating it.
- [Creating and Removing Application Containers and Seeds](creating-removing-application-containers-seeds-with-sql-plus.md)  
	You can create application containers and application seeds in several different ways. You can also remove application containers from a CDB, and you can remove application seeds from application containers.