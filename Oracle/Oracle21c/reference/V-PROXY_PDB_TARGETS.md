---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PROXY_PDB_TARGETS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.141 V$PROXY\_PDB\_TARGETS

`V$PROXY_PDB_TARGETS` provides information about the target of a proxy PDB.

| Column | Datatype | Description |
| --- | --- | --- |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  n: Where n is the container ID of a proxy PDB |
| `TARGET_PORT` | `NUMBER` | Port number that the target of the proxy PDB has registered with the listener, and which will be used by the proxy PDB to connect to the target |
| `TARGET_HOST` | `VARCHAR2(128)` | Host name where the target of the proxy PDB is running, and which will be used by the proxy PDB to connect to the target |
| `TARGET_SERVICE` | `VARCHAR2(128)` | Service name that the target of the proxy PDB has registered with the listener, and which will be used by the proxy PDB to connect to the target |
| `TARGET_USER` | `VARCHAR2(128)` | User name used by the proxy PDB to connect to the target of the proxy PDB. If null, the name of the connected user will be used. |

See Also:

[Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=MULTI-GUID-7C23D560-5AD5-4AF2-93B4-F4FDC6DE768C) for information about creating proxy PDBs