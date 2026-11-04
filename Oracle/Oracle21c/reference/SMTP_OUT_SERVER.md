---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SMTP_OUT_SERVER.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.342 SMTP\_OUT\_SERVER

`SMTP_OUT_SERVER` specifies the SMTP host and port to which `UTL_MAIL` delivers out-bound E-mail.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `SMTP_OUT_SERVER = ` `server_clause` `  [,  ``server_clause` ` ] ...` |
| Syntax | server\_clause::=  `host_name` `[:``port``]` |
| Default value | There is no default value. |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

Multiple servers may be specified, separated by commas.

If the first server in the list is unavailable, then `UTL_MAIL` tries the second server, and so on.

If `SMTP_OUT_SERVER` is not specified, then the SMTP server name defaults to the value of `DB_DOMAIN`, the port number defaults to `25`, and the SMTP domain defaults to the suffix of `DB_DOMAIN`.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS384) for information on the `UTL_MAIL` package