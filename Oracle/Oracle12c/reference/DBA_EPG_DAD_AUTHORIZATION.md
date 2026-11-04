---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_EPG_DAD_AUTHORIZATION.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_EPG_DAD_AUTHORIZATION` describes the DADs that are authorized to use different user's privileges.

Related View

`USER_EPG_DAD_AUTHORIZATION` describes the DADs that are authorized to use the user's privileges. This view does not display the `USERNAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DAD_NAME` | `VARCHAR2(64)` | NOT NULL | Name of DAD |
| `USERNAME` | `VARCHAR2(128)` | NOT NULL | Name of the user whose privileges the DAD is authorized to use |

See Also:

" [USER\_EPG\_DAD\_AUTHORIZATION](USER_EPG_DAD_AUTHORIZATION.md) "