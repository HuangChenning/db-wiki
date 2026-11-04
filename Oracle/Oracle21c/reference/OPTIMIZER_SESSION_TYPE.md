---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_SESSION_TYPE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.256 OPTIMIZER\_SESSION\_TYPE

`OPTIMIZER_SESSION_TYPE` controls how the database performs automatic indexing for SQL statements in the session.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `OPTIMIZER_SESSION_TYPE = { NORMAL \| CRITICAL \| ADHOC }` |
| Default value | `NORMAL` |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | No |
| Basic | No |

Values:

- `NORMAL`
	Automatic indexing is performed normally for SQL statements in the session. The automatic indexing process identifies auto index candidates, creates auto indexes, and verifies them against SQL statements.
- `CRITICAL`
	Automatic indexing is performed for SQL statements in the session, with a higher priority given to long-running statements. The automatic indexing process identifies auto index candidates and creates auto indexes. However, auto indexes are verified against SQL statements in descending order of elapsed execution time for each statement.
- `ADHOC`
	Automatic indexing is suspended for SQL statements in the session. The automatic indexing process does not identify auto index candidates, create auto indexes, or verify auto indexes against SQL statements. This setting is useful when running ad hoc queries or testing new functionality.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN-GUID-082972AD-1866-411A-8250-9B23D4088582) for more information about how automatic indexing works