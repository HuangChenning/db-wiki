---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/THREADED_EXECUTION.html
tags:
  - oracle
  - 12c
  - reference
---

`THREADED_EXECUTION` specifies whether to enable the multithreaded Oracle model.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | If specified, all instances must use the same value |

Starting in Oracle Database 12c, the multithreaded Oracle model enables Oracle processes on UNIX and Linux to run as operating system threads in separate address spaces.

By default, some background processes on UNIX and Linux always use threaded execution; the remaining Oracle processes run as operating system processes. Thus, an "Oracle process" is not always equivalent to an "operating system process."

Note:

When this initialization parameter is set to `TRUE`, which enables the multithreaded Oracle model, operating system authentication is not supported. Attempts to connect to the database using operating system authentication (for example, `CONNECT / AS SYSDBA` or `CONNECT /` ) when this initialization parameter is set to `TRUE` receive an `ORA-01031 "insufficient privileges"` error.

The solution to this error is to always use the password when connecting to the database.

Also, when this initialization parameter is set to `TRUE`, the `DEDICATED_THROUGH_BROKER_listener-name` `=ON` parameter should be added to the listener.ora file, where `listener-name` is the name of the Oracle Net listener and the `LOCAL_LISTENER` initialization parameter should be set to a TNS name entry corresponding to your instance service. This enables the server to spawn threads when connections to the database are requested through the listener.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT901) for more information about multithreaded Oracle
- [Table F-1](background-processes.md) for more information about background processes that run as threads instead of as operating system processes when multithreaded Oracle is enabled
- [Oracle Database Net Services Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=NETRF2101) for more information about the `DEDICATED_THROUGH_BROKER_` listener-name parameter in the listener.ora file
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=NETAG-GUID-A3263EB4-C3F2-4529-ABC2-ADE749114D33) for an overview of Oracle Net listener