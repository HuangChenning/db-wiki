---
title: LOG_ARCHIVE_LOCAL_FIRST
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams129.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `true \| false` |
| Basic | No |

Note:

The `LOG_ARCHIVE_LOCAL_FIRST` parameter is deprecated. It is retained for backward compatibility only.

`LOG_ARCHIVE_LOCAL_FIRST` specifies when the archiver processes (ARCn) transmit redo data to remote standby database destinations.

Values:

- `true`
	Directs the ARCn process to transmit redo data after the online redo log file has been completely and successfully archived to at least one local destination. This is the default value.
	Because the online redo log files are archived locally first, the LGWR process reuses the online redo log files much earlier than would be possible if the ARCn processes archived to the standby database concurrently with the local destination. This behavior is useful when archiving to remote destinations that use a slow network connection, such as a long-distance wide area network (WAN).
- `false`
	Directs the ARCn process to transmit redo data at the same time the online redo log file is archived to the local destinations. This results in redo data being promptly dispatched to the remote standby database destination.
	Setting `LOG_ARCHIVE_LOCAL_FIRST` to `false` is most useful for faster network connections, such as high-speed local area networks (LAN).

If `LOG_ARCHIVE_LOCAL_FIRST` is set to `true`, then it is not used on a physical standby database and any database for which the following attributes have been specified in the `LOG_ARCHIVE_DEST_` `n` initialization parameter:

- `MANDATORY`
- `LOCAL`

If `LOG_ARCHIVE_LOCAL_FIRST` is set to `true`, then it is ignored during certain operations, such as during a switchover, which requires synchronized archival operations. If the destination was explicitly configured to use the log writer process (by specifying the `LGWR` attribute in the `LOG_ARCHIVE_DEST_` `n` initialization parameter), but for some reason the log writer process becomes unable to archive to the destination, then Data Guard will revert to using the ARCn process to complete archival operations using the default behavior, even if `LOG_ARCHIVE_LOCAL_FIRST` is set to `false`.

For example, if a standby database problem or a network problem causes the LGWR process to fail, then the ARCn process will complete the archival. Data Guard minimizes the effect on the primary database as much as possible by archiving to the local destination first to ensure the online redo log files are available to the LGWR process as quickly as possible.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) for more information about the `LOG_ARCHIVE_LOCAL_FIRST` initialization parameter and its effect on ARCn behavior