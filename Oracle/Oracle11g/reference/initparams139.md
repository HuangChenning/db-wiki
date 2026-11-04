---
title: MAX_DUMP_FILE_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams139.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `MAX_DUMP_FILE_SIZE = {` `integer` `[K \| M \| G] \| UNLIMITED }` |
| Default value | `UNLIMITED` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Range of values | 0 to unlimited, or `UNLIMITED` |
| Basic | No |

`MAX_DUMP_FILE_SIZE` specifies the maximum size of trace files (excluding the alert file). Change this limit if you are concerned that trace files may use too much space.

- A numerical value for `MAX_DUMP_FILE_SIZE` specifies the maximum size in operating system blocks.
- A number followed by a `K` or `M` suffix specifies the file size in kilobytes or megabytes.
- The special value string `UNLIMITED` means that there is no upper limit on trace file size. Thus, dump files can be as large as the operating system permits.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) and [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information on setting this parameter