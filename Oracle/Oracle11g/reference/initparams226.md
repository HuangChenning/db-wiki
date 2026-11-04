---
title: SEC_MAX_FAILED_LOGIN_ATTEMPTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams226.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `10` |
| Modifiable | No |
| Range of values | `1` or higher. In this context, "higher" means any integer value higher than 1, not the string "higher." |
| Basic | No |

`SEC_MAX_FAILED_LOGIN_ATTEMPTS` specifies the number of authentication attempts that can be made by a client on a connection to the server process. After the specified number of failure attempts, the connection will be automatically dropped by the server process.