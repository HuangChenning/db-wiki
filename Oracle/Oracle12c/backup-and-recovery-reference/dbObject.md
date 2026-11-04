---
title: Database Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: E85640-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/rcmrf/dbObject.html
tags:
  - oracle
  - 12c
  - backup-and-recovery-reference
---

Purpose

Use the `dbObject` subclause to identify a database or a subset of a database.

Syntax

dbObject::=

![dbobject](img/dbobject.gif)

> {DATABASE \[ROOT\] | PLUGGABLE DATABASE pdb\_name \[, pdb\_name\]...} | DATAFILE datafileSpec \[, datafileSpec\]... | TABLESPACE \[pdb\_name:\] \['\] tablespace\_name \['\] \[, \[pdb\_name:\] \['\] tablespace\_name \['\]\]...


([datafileSpec::=](datafileSpec.md))

Semantics

| Syntax Element | Description |
| --- | --- |
| `DATABASE` | Specifies the entire database. In a multitenant container database (CDB), specifies the whole CDB. |
| `DATABASE ROOT` | Specifies only the root in a CDB. |
| `PLUGGABLE DATABASE` `pdb_name` | Specifies one or more pluggable databases (PDBs) in a CDB. Use a comma-delimited list to specify multiple PDBs. |
| `DATAFILE` `datafileSpec` | Specifies a list of one or more data files by either file name or absolute data file number.  See Also: `datafileSpec` |
| `TABLESPACE` `tablespace_name` | Specifies one or more tablespaces. |
| `TABLESPACE ` `pdb_name``:``tablespace_name` | Specifies the name of a tablespace in a PDB. Use a comma-delimited list to specify multiple tablespaces. Multiple PDBs can have tablespaces with the same name. A qualifier before the name uniquely identifies the tablespace. `pdb-name` is the name of the PDB that contains `tablespace_name`. If `pdb_name` is omitted, root is used as the default container. |