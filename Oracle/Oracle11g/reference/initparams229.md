---
title: SEC_RETURN_SERVER_RELEASE_BANNER
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams229.htm
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
| Basic | No |

`SEC_RETURN_SERVER_RELEASE_BANNER` specifies whether or not the server returns complete database software information to unauthenticated clients.

Values:

- `true`
	Returns complete database version information to the client.
- `false`
	Returns a generic version string to the client.

See Also:

[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/oci08sca.htm#LNOCI16581) and [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/app_devs.htm#DBSEG162) for more information on controlling the display of the database version banner.