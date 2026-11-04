---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/FORWARD_LISTENER.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.138 FORWARD\_LISTENER

`FORWARD_LISTENER` specifies the name of a listener to which a connection must be forwarded by an existing set of remote listeners.

Examples

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `FORWARD_LISTENER = listener-name` |
| Default value | NULL |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | A different value can be set on different instances. |

The parameter is useful when it is difficult to change an existing client connect string, for example, after an offsite database has been moved into the Oracle Cloud. With the `FORWARD_LISTENER` parameter, clients can continue to connect to their offsite listener, and the offsite listener forwards the connection to the Oracle Cloud listener.

Once a forward listener has been configured through the `FORWARD_LISTENER` parameter, the `LOCAL_LISTENER` parameter can be cleared by setting its value to `-oracle-none-` so that all the connections coming to an existing set of remote listeners configured through the `REMOTE_LISTENER` parameter are forwarded only to listeners configured through `FORWARD_LISTENER`.

The `FORWARD_LISTENER` parameter can also be specified in the `LISTENER_NETWORKS` parameter.

The following setup can be used to forward all the database connections coming to an existing customer SCAN listener to the Oracle Cloud SCAN listener.

```
REMOTE_LISTENER=customer-scan
FORWARD_LISTENER=oracle-cloud-scan
LOCAL_LISTENER=oracle-none-
```