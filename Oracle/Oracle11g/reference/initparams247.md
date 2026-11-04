---
title: SPFILE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams247.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `SPFILE =` `spfile_name` |
| Default value | `ORACLE_HOME` `/dbs/spfile.ora` |
| Modifiable | No |
| Range of values | Any valid `SPFILE` |
| Oracle RAC | Multiple instances should have the same value. |

The value of this parameter is the name of the current server parameter file (`SPFILE`) in use. This parameter can be defined in a client side PFILE to indicate the name of the server parameter file to use.

When the default server parameter file is used by the server, the value of `SPFILE` is internally set by the server.

The `SPFILE` resides in the `ORACLE_HOME` `/dbs` directory; however, users can place it anywhere on their machine as long as it is specified in an initialization parameter file.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about creating the server parameter file