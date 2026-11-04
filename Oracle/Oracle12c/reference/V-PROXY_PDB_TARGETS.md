---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-PROXY_PDB_TARGETS.html
tags:
  - oracle
  - 12c
  - reference
---

`V$PROXY_PDB_TARGETS` provides information about the target of a proxy PDB.

| Column | Datatype | Description |
| --- | --- | --- |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  n: Where n is the container ID of a proxy PDB |
| `TARGET_PORT` | `NUMBER` | Port number that the target of the proxy PDB has registered with the listener, and which will be used by the proxy PDB to connect to the target |
| `TARGET_HOST` | `VARCHAR2(128)` | Host name where the target of the proxy PDB is running, and which will be used by the proxy PDB to connect to the target |
| `TARGET_SERVICE` | `VARCHAR2(128)` | Service name that the target of the proxy PDB has registered with the listener, and which will be used by the proxy PDB to connect to the target |
| `TARGET_USER` | `VARCHAR2(128)` | User name used by the proxy PDB to connect to the target of the proxy PDB. If null, the name of the connected user will be used. |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN-GUID-7C23D560-5AD5-4AF2-93B4-F4FDC6DE768C) for information about creating proxy PDBs