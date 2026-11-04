---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/FILEIO_NETWORK_ADAPTERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.135 FILEIO\_NETWORK\_ADAPTERS

`FILEIO_NETWORK_ADAPTERS` specifies a list of network adapters that can be used to access the disk storage.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `FILEIO_NETWORK_ADAPTERS = ` `adapter_name` `  [,  ``adapter_name` ` ] ...` |
| Default value | There is no default value. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | One or more network adapter names, separated by commas |
| Basic | No |

On platforms where the database files reside in network attached storage, this parameter provides the storage access library the list of network adapters that can be used to access the storage.

The network adapter name is a fully qualified address name of the network card that can be accessed through the host name database or using the Network Information Service. The components of the adapter name are separated by periods. For example, the following is a fully qualified adapter name:

```
ib1.oracle.com
```