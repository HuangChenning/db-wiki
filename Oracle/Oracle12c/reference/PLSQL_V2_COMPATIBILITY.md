---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PLSQL_V2_COMPATIBILITY.html
tags:
  - oracle
  - 12c
  - reference
---

`PLSQL_V2_COMPATIBILITY` is used to specify whether abnormal behavior that PL/SQL Version 2 allows will be allowed in PL/SQL Version 8.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |

Note:

The `PLSQL_V2_COMPATIBILITY` parameter is deprecated. It is retained for backward compatibility only.

PL/SQL Version 2 allows some abnormal behavior that Version 8 disallows. If you want to retain that behavior for backward compatibility, set `PLSQL_V2_COMPATIBILITY` to `true`. If you set it to `false`, then PL/SQL Version 8 behavior is enforced and Version 2 behavior is not allowed.

See Also:

[Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=LNPLS006) for a description of the differences between PL/SQL Version 2 and Version 8, and for more information on setting this parameter