---
title: TRUSTED_SERVERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5191.htm
tags:
  - oracle
  - 11g
  - reference
---

`TRUSTED_SERVERS` displays whether a server is trusted or untrusted.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TRUST` | `VARCHAR2(9)` |  | Trustedness of the server listed. Values can be `TRUSTED` or `UNTRUSTED` servers which are not listed in the `NAME` column have opposite trustedness. |
| `NAME` | `VARCHAR2(128)` |  | Server name. Can be a specific server name or ALL for all servers. |

Table 6-1 shows examples of the values returned depending on the status of the servers.

Table 6-1 TRUSTED\_SERVERS Values

| Condition (If... ) | TRUSTED column | NAME column |
| --- | --- | --- |
| ... all servers are trusted | `Trusted` | `ALL` |
| ... no servers are trusted | `Untrusted` | `ALL` |
| ... all servers except DB1 are trusted | `Untrusted` | `DB1` |
| ... all servers except DB1 are untrusted | `Trusted` | `DB1` |