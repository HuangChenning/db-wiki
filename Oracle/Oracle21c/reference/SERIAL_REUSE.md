---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SERIAL_REUSE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.326 SERIAL\_REUSE

This feature allocates private cursor memory in the SGA so that it can be reused (serially, not concurrently) by sessions executing the same cursor.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `SERIAL_REUSE = { disable \| all \| select \| dml \| plsql \| force }` |
| Default value | `disable` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |

Note:

The `SERIAL_REUSE` parameter is deprecated. It is retained for backward compatibility only.

Values

- `disable`
	Disables the option for all SQL statement types. This value overrides any other values included in the list.
- `all`
	Enables the option for both DML and `SELECT` statements. Equivalent to setting `select`, `dml`, and `plsql`.
- `select`
	Enables the option for `SELECT` statements.
- `dml`
	Enables the option for DML statements.
- `plsql`
	Currently has no effect (although PL/SQL packages do support the serial-reuse memory option using PL/SQL pragmas).

Note:

If `CURSOR_SPACE_FOR_TIME` is set to `true`, then the value of `SERIAL_REUSE` is ignored and treated as if it were set to `disable`.

See Also:

" [CURSOR\_SPACE\_FOR\_TIME](CURSOR_SPACE_FOR_TIME.md) "