---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/LOCAL_LISTENER.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.177 LOCAL\_LISTENER

`LOCAL_LISTENER` specifies a network name that resolves to an address or address list of Oracle Net local listeners (that is, listeners that run on the same system as this instance). The address or address list is specified in the `TNSNAMES.ORA` file or other address repository as configured for your system.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LOCAL_LISTENER = ` `network_name` |
| Default value | `(ADDRESS = (PROTOCOL=TCP)(HOST=` `hostname``)(PORT=1521))` where `hostname` is the network name of the local host. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=CNCPT904) for more information about listener processes and dispatcher processes
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=NETAG295) and your operating system-specific Oracle documentation for more information about specifying network addresses for the protocols on your system