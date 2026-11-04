---
title: CLONEDB
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams027.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | The same value should be set for all instances. |

`CLONEDB` should be set on Direct NFS Client CloneDB databases. When this parameter is set, the CloneDB database uses the database backup as the backing store for the data files.

Note:

The `CLONEDB` initialization parameter is available starting with Oracle Database 11g Release 2 (11.2.0.3).

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN14023) for more information about cloning a database with CloneDB