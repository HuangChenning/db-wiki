---
title: LOCAL_LISTENER
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams120.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LOCAL_LISTENER =` `network_name` |
| Default value | `(ADDRESS = (PROTOCOL=TCP)(HOST=` `hostname``)(PORT=1521))` where `hostname` is the network name of the local host. |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |

`LOCAL_LISTENER` specifies a network name that resolves to an address or address list of Oracle Net local listeners (that is, listeners that are running on the same machine as this instance). The address or address list is specified in the `TNSNAMES.ORA` file or other address repository as configured for your system.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for more information about instances, listener processes, and dispatcher processes
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) and your operating system-specific Oracle documentation for more information about specifying network addresses for the protocols on your system