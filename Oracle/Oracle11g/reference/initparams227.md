---
title: SEC_PROTOCOL_ERROR_FURTHER_ACTION
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams227.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `SEC_PROTOCOL_ERROR_FURTHER_ACTION = { CONTINUE \| (DELAY,``integer``) \| (DROP,``integer``) }` |
| Default value | `CONTINUE` |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |

`SEC_PROTOCOL_ERROR_FURTHER_ACTION` specifies the further execution of a server process when receiving bad packets from a possibly malicious client.

Values:

- `CONTINUE`
	The server process continues execution. The database server may be subject to a Denial of Service (DoS) if bad packets continue to be sent by a malicious client.
- `(DELAY,``integer``)`
	The client experiences a delay of integer seconds before the server process accepts the next request from the same client connection. Malicious clients are prevented from excessive consumption of server resources while legitimate clients experience a degradation in performance but can continue to function.
- `(DROP,``integer``)`
	The server forcefully terminates the client connection after integer cumulative bad packets. The server protects itself at the expense of the client (for example, a client transaction may be lost). The client may reconnect and attempt the same operation.