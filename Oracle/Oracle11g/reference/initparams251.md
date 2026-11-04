---
title: STANDBY_ARCHIVE_DEST
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams251.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `STANDBY_ARCHIVE_DEST =` `filespec` |
| Default value | Operating system-specific |
| Modifiable | `ALTER SYSTEM` |
| Range of values | A valid path or device name other than `RAW` |

Note:

The `STANDBY_ARCHIVE_DEST` parameter is deprecated. It is retained for backward compatibility only.

`STANDBY_ARCHIVE_DEST` can be used to specify where archived logs received from a primary database are stored on a standby database. It is no longer necessary to set this parameter, because an appropriate location is automatically chosen.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) for more information