---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/alter-pmem-filestore.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## ALTER PMEM FILESTORE

Purpose

Use this command to change the attributes of a PMEM file store.

Prerequisites

You cannot change the block size of a PMEM file store.

Syntax

alter\_pmem\_filestore  

![alter_pmem_fs](img/alter_pmem_fs.gif)

Description of alter\_pmem\_fs.eps follows

Semantics

MOUNT

Use this command to mount a PMEM file store. If you have already specified the mount point and backing file paths in the `init.ora` file you can issue the command like this:

```
ALTER PMEM FILESTORE 'filestore_name' MOUNT
```

You can also specify the mount point and backing file paths in the command line. In this case, you must ensure that there is no mismatch between the values in the `init.ora` file and the values you specify in the command line. The command fails when a mismatch occurs, unless you specify `FORCE` to override the values in the `init.ora` file. The paths on the command line become the new paths for the PMEM file store.

If you use a `spfile`, then the parameters are automatically updated with the new paths specified on the command line.

Use the mount PMEM file store command in cases when the PMEM file store was not already automatically mounted during database startup.

Specify the mount point path or the backing file path on the command line when:

- You have not specified either the mount point path or the backing file path in the `init.ora` file
- You want to specify new values for either the mount point path or the backing file path

Before you can change the mount point and the backing file, you must first dismount the file store.

DISMOUNT

Use this command to dismount a PMEM file store. You must ensure that the database instance is in `NOMOUNT` mode.

Examples

Example 1: Resize File Store Named cloud\_db\_1

```
ALTER PMEM FILESTORE cloud_db_1 RESIZE 5T
```

Example 2: Mount File Store Named cloud\_db\_1

```
ALTER  PMEM FILESTORE cloud_db_1 MOUNT  MOUNTPOINT ‘/corp/db/cloud_db_1’
    BACKINGFILE ‘/var/pmem/foo_1’
```

Example 3: Dismount File Store Named cloud\_db\_1

```
ALTER PMEM FILESTORE cloud_db_1 DISMOUNT
```