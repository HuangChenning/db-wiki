---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/FILESYSTEMIO_OPTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.136 FILESYSTEMIO\_OPTIONS

`FILESYSTEMIO_OPTIONS` specifies I/O operations for file system files. This parameter is platform-specific and has a default value that is suitable for a particular platform.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `FILESYSTEMIO_OPTIONS = { ASYNCH \| DIRECTIO \| SETALL \| NONE }` |
| Default value | Varies by database version and operating system. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |

Values:

- `ASYNCH` - Enable asynchronous I/O on file system files, which has no timing requirement for transmission.
- `DIRECTIO` - Enable direct I/O on file system files, which bypasses the buffer cache.
- `SETALL` - Enable both asynchronous and direct I/O on file system files.
- `NONE` - Disable both asynchronous and direct I/O on file system files.

See Also:

- Your platform-specific documentation for more details
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-08ED4172-9398-402E-B0C4-4CE88DE87603) for information about setting this parameter before running I/O calibration