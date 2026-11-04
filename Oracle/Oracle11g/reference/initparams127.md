---
title: LOG_ARCHIVE_DUPLEX_DEST
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams127.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LOG_ARCHIVE_DUPLEX_DEST =` `filespec` |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Range of values | Either a null string or any valid path or device name, except raw partitions |
| Basic | No |

Note:

If you are using Oracle Enterprise Edition, this parameter is deprecated in favor of the `LOG_ARCHIVE_DEST_` `n` parameters. If Oracle Enterprise Edition is not installed or it is installed but you have not specified any `LOG_ARCHIVE_DEST_` `n` parameters, this parameter is valid.

`LOG_ARCHIVE_DUPLEX_DEST` is similar to the initialization parameter `LOG_ARCHIVE_DEST`. This parameter specifies a second archive destination: the duplex archive destination. This duplex archive destination can be either a must-succeed or a best-effort archive destination, depending on how many archive destinations must succeed (as specified in the `LOG_ARCHIVE_MIN_SUCCEED_DEST` parameter).

The default setting of a null string ("") or (' ') indicates that a duplex archive destination does not exist.