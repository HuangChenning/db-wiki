---
title: "20.14 Options for Working with Encrypted InnoDB Tablespaces and Encrypted Binary/Relay Logs"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/backup-encrypted-innodb-options.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

MySQL Enterprise Backup supports encrypted InnoDB tablespaces and, for release 8.0.14 and later, encrypted binary/relay logs. For details on how MySQL Server encrypts and decrypts these items, see [InnoDB Data-at-Rest Encryption](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-data-encryption.html) and [Encrypting Binary Log Files and Relay Log Files](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/replication-binlog-encryption.html). See [Chapter 6, *Working with Encrypted InnoDB Tablespaces*](meb-encrypted-innodb.md) and [Section 8.4, “Working with Encrypted Binary and Relay Logs”](advanced.encrypted-binlog-relaylog.md) on how **mysqlbackup** commands handle these encrypted items.

The following is the command-line option for working with encrypted InnoDB tables and binary/relay logs:

- `--encrypt-password` \[= *`STRING`*\]
	| Command-Line Format | `--encrypt-password=STRING` |
	| --- | --- |
	| Type | String |
	The user-supplied password by which **mysqlbackup** encrypts the master encryption key, which is used to encrypt the encryption keys for the InnoDB tablespaces or binary/relay log files.
	The option must be used when backing up a server that has a keyring plugin enabled for InnoDB table or binary/relay log encryption and for restoring a backup containing encrypted InnoDB tables or binary/relay log. If the server is using the `keyring_encrypted_file` plugin, the password supplied with the option must match the value of the system variable [`keyring_encrypted_file_password`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/keyring-system-variables.html#sysvar_keyring_encrypted_file_password) on the server. If the server uses the `keyring_hashicorp` plugin, use the option to supply the HashiCorp Vault AppRole authentication secret ID, which was the value of [`keyring_hashicorp_secret_id`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/keyring-system-variables.html#sysvar_keyring_hashicorp_secret_id) on the server to be backed up.
	The same password supplied during backup must be supplied again during a [`copy-back-and-apply-log`](backup-commands-restore.md), [`apply-log`](backup-commands-update.md), or an [`apply-incremental-backup`](backup-commands-update.md) operation for the backup, or **mysqlbackup** will error out when it encounters encrypted InnoDB tables or binary/relay logs during the operation. If different passwords were used for different backups in a sequence of full and incremental backups, make sure the very password used to create an individual backup is supplied when performing an [`apply-log`](backup-commands-update.md), [`apply-incremental-backup`](backup-commands-update.md), or [`copy-back-and-apply-log`](backup-commands-restore.md) operation on it.
	Users who do not want to supply the password on the command line or in a default file may use the option without specifying any value; **mysqlbackup** then asks the user to type in the password before the operation starts.