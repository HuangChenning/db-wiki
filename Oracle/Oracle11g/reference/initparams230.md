---
title: SERIAL_REUSE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams230.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `SERIAL_REUSE = { disable \| all \| select \| dml \| plsql \| force }` |
| Default value | `disable` |
| Modifiable | No |
| Basic | No |

Note:

The `SERIAL_REUSE` parameter is deprecated. It is retained for backward compatibility only.

`SERIAL_REUSE` specifies which types of cursors make use of the serial-reusable memory feature. This feature allocates private cursor memory in the SGA so that it can be reused (serially, not concurrently) by sessions executing the same cursor.

Values:

- `disable`
	Disables the option for all SQL statement types. This value overrides any other values included in the list.
- `all`
	Enables the option for both DML and `SELECT` statements. Equivalent to setting `select`, `dml`, and `plsql`.
- `select`
	Enables the option for `SELECT` statements.
- `dml`
	Enables the option for DML statements.
- `plsql`
	Currently has no effect (although PLSQL packages do support the serial-reuse memory option using PLSQL pragmas).

Note:

If `CURSOR_SPACE_FOR_TIME` is set to `true`, then the value of `SERIAL_REUSE` is ignored and treated as if it were set to `disable`.

See Also:

["CURSOR\_SPACE\_FOR\_TIME"](initparams045.md)