---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_FLASHBACK_ARCHIVE.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.476 USER\_FLASHBACK\_ARCHIVE

`USER_FLASHBACK_ARCHIVE` describes flashback data archives, which consist of multiple tablespaces and historic data from all transactions against tracked tables.

The content of this view depends on the privileges of the user who queries it, as follows:

- If the user has the `FLASHBACK ARCHIVE ADMINISTER` system privilege, then `USER_FLASHBACK_ARCHIVE` describes the flashback archives for all users who have been granted the `FLASHBACK ARCHIVE` object privilege.
- If the user does not have the `FLASHBACK ARCHIVE ADMINISTER` system privilege, then `USER_FLASHBACK_ARCHIVE` describes flashback archives for which the current user has been granted the `FLASHBACK ARCHIVE` object privilege.

The columns of the `USER_FLASHBACK_ARCHIVE` view are the same as those in `DBA_FLASHBACK_ARCHIVE`.

See Also:

" [DBA\_FLASHBACK\_ARCHIVE](DBA_FLASHBACK_ARCHIVE.md) "