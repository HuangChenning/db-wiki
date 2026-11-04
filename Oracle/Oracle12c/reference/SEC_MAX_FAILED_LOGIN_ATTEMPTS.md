---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/SEC_MAX_FAILED_LOGIN_ATTEMPTS.html
tags:
  - oracle
  - 12c
  - reference
---

`SEC_MAX_FAILED_LOGIN_ATTEMPTS` specifies the number of authentication attempts that can be made by a client on a connection to the server process.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `3` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | An integer greater than or equal to `1`. |
| Basic | No |

These login attempts can be for multiple user accounts in the same connection. After the specified number of failure attempts, the connection will be automatically dropped by the server process, and the server process is terminated.

See Also:

[Oracle Database 2 Day + Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TDPSG94351) for more information about this parameter