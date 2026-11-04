---
title: LISTENER_NETWORKS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams119.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LISTENER_NETWORKS =` ``` '((NAME=network_name)  (LOCAL_LISTENER=["]listener_address[,...]["])  [(REMOTE_LISTENER=["]listener_address[,...]["])])' [,...] ``` |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |

`LISTENER_NETWORKS` specifies one or more sets of local & remote listeners for cross-registration. All listeners within the same network\_name will cross-register.

If a network\_name is specified multiple times, then the resulting listener set is the union of each specification. This can be used to specify sets that require more than 255 characters, which is the per element limit.

The listener\_address specifies a string that is an address, address list, or an alias that resolves to an address or address list of Oracle Net listeners. If an alias, the address or address list is specified in the TNSNAMES.ORA file or another address repository as configured for your system.

If a comma is used to specify a listener\_address list, then the set of addresses must be surrounded by double quotes.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/listenercfg.htm#NETAG1470) for more information on setting this parameter