---
title: PERMIT_92_WRAP_FORMAT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams192.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Multiple instances should use the same value |

`PERMIT_92_WRAP_FORMAT` allows Oracle Database release 9.2 wrapped versions of PL/SQL source text to be used in Oracle Database releases 10.2 and 11.2 when this parameter is set to `true` (the default).

Oracle recommends that wrapped files be created using the PL/SQL Wrapper utility from Oracle Database release 10 or later.

See Also:

[Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/wrap.htm#LNPLS016) for more information about PL/SQL source text wrapping