---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/THREADED_EXECUTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.363 THREADED\_EXECUTION

`THREADED_EXECUTION` specifies whether to enable the multithreaded Oracle model.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | On UNIX and Linux: `false`  On Windows: `true` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | If specified, all instances must use the same value |

THREADED\_EXECUTION on UNIX and Linux

Oracle Database 12c introduced the `THREADED_EXECUTION` initialization parameter for databases running on UNIX and Linux systems. On such databases, the default value for `THREADED_EXECUTION` is `false`. Setting this parameter to `true` enables the multithreaded Oracle model, which allows Oracle processes on UNIX and Linux to run as operating system threads in separate address spaces.

By default, some background processes on UNIX and Linux always use threaded execution; the remaining Oracle processes run as operating system processes. Thus, an "Oracle process" is not always equivalent to an "operating system process."

Note:

When `THREADED_EXECUTION` is set to `true` on databases running on UNIX and Linux systems, which enables the multithreaded Oracle model, operating system authentication is not supported. Attempts to connect to the database using operating system authentication (for example, `CONNECT / AS SYSDBA` or `CONNECT /` ) when this initialization parameter is set to `true` receive an `ORA-01031 "insufficient privileges"` error.

The solution to this error is to always use the password when connecting to the database.

Also, when this initialization parameter is set to `true` on databases running on UNIX and Linux systems, the `DEDICATED_THROUGH_BROKER_listener-name=ON` parameter should be added to the listener.ora file, where `listener-name` is the name of the Oracle Net listener and the `LOCAL_LISTENER` initialization parameter should be set to a TNS name entry corresponding to your instance service. This enables the server to spawn threads when connections to the database are requested through the listener.

THREADED\_EXECUTION on Windows

Starting with Oracle Database 21c, the `THREADED_EXECUTION` initialization parameter is supported for databases running on Microsoft Windows. On such databases, this parameter must remain set to its default value of `true`; setting this parameter to `false` on databases running on Windows is not supported. The introduction of this parameter does not change the threading model for Oracle database on Windows. As in previous releases, an Oracle Database server instance on Windows is a service with a single multi-threaded operating system process. However, starting with Oracle Database 21c, you will observe changes to the `V$PROCESS` view, the dedicated connection broker, and the naming of trace files. For details about these changes, refer to [Oracle Database Administrator’s Reference for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NTQRF-GUID-6BA9D2DC-F8FF-47A1-A56F-C8491A68E481).

Note:

Unlike on UNIX and Linux systems, when `THREADED_EXECUTION` is set to `true` on Windows, operating system authentication is supported.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT901) for more information about multithreaded Oracle
- [Table F-1](background-processes.md) for more information about background processes that run as threads instead of as operating system processes when multithreaded Oracle is enabled
- [Oracle Database Net Services Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NETRF-GUID-C09A2180-5DB2-4226-96A4-3313539E12EF) for more information about the `DEDICATED_THROUGH_BROKER_` listener-name parameter in the listener.ora file
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NETAG-GUID-A3263EB4-C3F2-4529-ABC2-ADE749114D33) for an overview of Oracle Net listener