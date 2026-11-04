---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_ADDM_FINDINGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.267 USER\_ADDM\_FINDINGS

`USER_ADDM_FINDINGS` displays the ADDM findings discovered by the advisors owned by the current user.

Each row for ADDM tasks in the related `USER_ADVISOR_FINDINGS` view has a corresponding row in this view. Its columns (except for `OWNER`) are the same as those in `DBA_ADDM_FINDINGS`.

See Also:

" [DBA\_ADDM\_FINDINGS](DBA_ADDM_FINDINGS.md) "