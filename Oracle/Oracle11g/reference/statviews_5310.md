---
title: USER_FLASHBACK_ARCHIVE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5310.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_FLASHBACK_ARCHIVE` describes flashback data archives, which consist of multiple tablespaces and historic data from all transactions against tracked tables. The content of this view depends on the privileges of the user who queries it, as follows:

- If the user has the `FLASHBACK ARCHIVE ADMINISTER` system privilege, then `USER_FLASHBACK_ARCHIVE` describes the flashback archives for all users who have been granted the `FLASHBACK ARCHIVE` object privilege.
- If the user does not have the `FLASHBACK ARCHIVE ADMINISTER` system privilege, then `USER_FLASHBACK_ARCHIVE` describes flashback archives for which the current user has been granted the `FLASHBACK ARCHIVE` object privilege.

The columns of the `USER_FLASHBACK_ARCHIVE` view are the same as those in `DBA_FLASHBACK_ARCHIVE`.

See Also:

["DBA\_FLASHBACK\_ARCHIVE"](statviews_3189.md)