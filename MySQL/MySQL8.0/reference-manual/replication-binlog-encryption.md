---
title: "19.3.2 Encrypting Binary Log Files and Relay Log Files"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/replication-binlog-encryption.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 19.3.2 Encrypting Binary Log Files and Relay Log Files

From MySQL 8.0.14, binary log files and relay log files can be encrypted, helping to protect these files and the potentially sensitive data contained in them from being misused by outside attackers, and also from unauthorized viewing by users of the operating system where they are stored. The encryption algorithm used for the files, the AES (Advanced Encryption Standard) cipher algorithm, is built in to MySQL Server and cannot be configured.

You enable this encryption on a MySQL server by setting the [`binlog_encryption`](replication-options-binary-log.md) system variable to `ON`. `OFF` is the default. The system variable sets encryption on for binary log files and relay log files. Binary logging does not need to be enabled on the server to enable encryption, so you can encrypt the relay log files on a replica that has no binary log. To use encryption, a keyring component or plugin must be installed and configured to supply MySQL Server's keyring service. For instructions to do this, see [Section 8.4.4, “The MySQL Keyring”](keyring.md). Any supported keyring component or plugin can be used to store binary log encryption keys.

When you first start the server with encryption enabled, a new binary log encryption key is generated before the binary log and relay logs are initialized. This key is used to encrypt a file password for each binary log file (if the server has binary logging enabled) and relay log file (if the server has replication channels), and further keys generated from the file passwords are used to encrypt the data in the files. The binary log encryption key that is currently in use on the server is called the binary log master key. The two tier encryption key architecture means that the binary log master key can be rotated (replaced by a new master key) as required, and only the file password for each file needs to be re-encrypted with the new master key, not the whole file. Relay log files are encrypted for all channels, including new channels that are created after encryption is activated. The binary log index file and relay log index file are never encrypted.

If you activate encryption while the server is running, a new binary log encryption key is generated at that time. The exception is if encryption was active previously on the server and was then disabled, in which case the binary log encryption key that was in use before is used again. The binary log file and relay log files are rotated immediately, and file passwords for the new files and all subsequent binary log files and relay log files are encrypted using this binary log encryption key. Existing binary log files and relay log files still present on the server are not encrypted, but you can purge them if they are no longer needed.

If you deactivate encryption by changing the [`binlog_encryption`](replication-options-binary-log.md) system variable to `OFF`, the binary log file and relay log files are rotated immediately and all subsequent logging is unencrypted. Previously encrypted files are not automatically decrypted, but the server is still able to read them. The [`BINLOG_ENCRYPTION_ADMIN`](privileges-provided.md) privilege is required to activate or deactivate encryption while the server is running.

Encrypted and unencrypted binary log files can be distinguished using the magic number at the start of the file header for encrypted log files (`0xFD62696E`), which differs from that used for unencrypted log files (`0xFE62696E`). The [`SHOW       BINARY LOGS`](show-binary-logs.md) statement shows whether each binary log file is encrypted or unencrypted.

When binary log files have been encrypted, [**mysqlbinlog**](mysqlbinlog.md) cannot read them directly, but can read them from the server using the [`--read-from-remote-server`](mysqlbinlog.md) option. From MySQL 8.0.14, [**mysqlbinlog**](mysqlbinlog.md) returns a suitable error if you attempt to read an encrypted binary log file directly, but older versions of [**mysqlbinlog**](mysqlbinlog.md) do not recognize the file as a binary log file at all. If you back up encrypted binary log files using [**mysqlbinlog**](mysqlbinlog.md), note that the copies of the files that are generated using [**mysqlbinlog**](mysqlbinlog.md) are stored in an unencrypted format.

Binary log encryption can be combined with binary log transaction compression (available as of MySQL 8.0.20). For more information on binary log transaction compression, see [Section 7.4.4.5, “Binary Log Transaction Compression”](binary-log-transaction-compression.md).