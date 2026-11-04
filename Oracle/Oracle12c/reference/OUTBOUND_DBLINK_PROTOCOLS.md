---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/OUTBOUND_DBLINK_PROTOCOLS.html
tags:
  - oracle
  - 12c
  - reference
---

`OUTBOUND_DBLINK_PROTOCOLS` specifies the network protocols allowed for communicating for outbound database links in the database.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `OUTBOUND_DBLINK_PROTOCOLS = { ALL \| NONE \| [ TCP \| [, ] \| TCPS \| [, ] \| IPC ] }` |
| Default value | `ALL` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

Specify a value of `ALL` to allow all network protocols, and a value of `NONE` to disallow all network communication protocols for database link communication. Specify a single value or a list of comma separated network communication protocols to allow only certain network protocols for outbound database link communication.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).