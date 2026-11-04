---
title: FILEIO_NETWORK_ADAPTERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams093.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `FILEIO_NETWORK_ADAPTERS =` `adapter_name` `[,` `adapter_name` `] ...` |
| Default value | There is no default value. |
| Modifiable | No |
| Range of values | One or more network adapter names, separated by commas |
| Basic | No |

`FILEIO_NETWORK_ADAPTERS` specifies a list of network adapters that can be used to access the disk storage. On platforms where the database files reside in network attached storage, this parameter provides the storage access library the list of network adapters that can be used to access the storage.

The network adapter name is a fully qualified address name of the network card that can be accessed through the host name database or using the Network Information Service. The components of the adapter name are separated by periods. For example, the following is a fully qualified adapter name:

```
ib1.oracle.com
```