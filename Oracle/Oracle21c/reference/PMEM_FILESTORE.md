---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PMEM_FILESTORE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.291 PMEM\_FILESTORE

`PMEM_FILESTORE` specifies the Persistent Memory Filestores (PMEM Filestores) that the database automatically mounts during instance startup.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PMEM_FILESTORE = ( 'mount_point', 'backing_file' [, 'mount_point', 'backing_file' ]... )` |
| Default value | None |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |

You can specify one or more PMEM Filestores to be mounted during instance startup.

Specify the following pair of values for each PMEM Filestore:

- `mount_point`: The operating system directory path for the mount point of the PMEM Filestore
- `backing_file`: The operating system file path for the backing file of the PMEM Filestore

For example:

```
PMEM_FILESTORE=('/var/db/db_1', '/var/db_storage/db1.f')

PMEM_FILESTORE=('/var/db/db_1', '/var/db_storage/db1.f', '/var/db/db_2', '/var/db_storage/db2.f')
```

Note:

This parameter is available starting with Oracle Database 21c.