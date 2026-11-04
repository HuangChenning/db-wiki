---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SEC_PROTOCOL_ERROR_FURTHER_ACTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.323 SEC\_PROTOCOL\_ERROR\_FURTHER\_ACTION

`SEC_PROTOCOL_ERROR_FURTHER_ACTION` specifies the further execution of a server process when receiving bad packets from a possibly malicious client.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `SEC_PROTOCOL_ERROR_FURTHER_ACTION = { CONTINUE \| (DELAY,``integer``) \| (DROP,``integer``) }` |
| Default value | `(DROP,3)` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

Values

- `CONTINUE`
	The server process continues execution. The database server may be subject to a Denial of Service (DoS) if bad packets continue to be sent by a malicious client.
- `(DELAY,``integer``)`
	The client experiences a delay of integer seconds before the server process accepts the next request from the same client connection. Malicious clients are prevented from excessive consumption of server resources while legitimate clients experience a degradation in performance but can continue to function.
- `(DROP,``integer``)`
	The server forcefully terminates the client connection after integer cumulative bad packets. The server protects itself at the expense of the client (for example, a client transaction may be lost). The client may reconnect and attempt the same operation.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG160) for examples of using this parameter