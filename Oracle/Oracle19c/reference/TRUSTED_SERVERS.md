---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/TRUSTED_SERVERS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.257 TRUSTED\_SERVERS

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

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ARPLS66236)
- [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=DBIMI110)