---
title: REMOTE_OS_AUTHENT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams213.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Range of values | `true \| false` |

`REMOTE_OS_AUTHENT` specifies whether remote clients will be authenticated with the value of the `OS_AUTHENT_PREFIX` parameter.

Note:

The `REMOTE_OS_AUTHENT` parameter is deprecated. It is retained for backward compatibility only.

See Also:

- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm) for more information on setting this parameter
- ["OS\_AUTHENT\_PREFIX"](initparams176.md)