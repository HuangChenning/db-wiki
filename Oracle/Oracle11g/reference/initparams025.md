---
title: CLIENT_RESULT_CACHE_LAG
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams025.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `CLIENT_RESULT_CACHE_LAG =` `integer` |
| Default value | `3000` |
| Modifiable | No |
| Range of values | `0` to operating system-dependent |
| Basic | No |

`CLIENT_RESULT_CACHE_LAG` specifies the maximum time (in milliseconds) since the last round trip to the server, before which the OCI client query execute makes a round trip to get any database changes related to the queries cached on the client.

See Also:

[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/oci10new.htm#LNOCI10103) for more information about the client query cache feature