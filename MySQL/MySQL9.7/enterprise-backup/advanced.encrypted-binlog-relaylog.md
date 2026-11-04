---
title: "8.4 Working with Encrypted Binary and Relay Logs"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/advanced.encrypted-binlog-relaylog.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

MySQL Enterprise Backup supports [encrypted binary and relay logs](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/replication-binlog-encryption.html), which are handled in a similar way as the encrypted InnoDB tables are (see [Chapter 6, *Working with Encrypted InnoDB Tablespaces*](meb-encrypted-innodb.md) for details).

When backing up encrypted binary or relay logs, the option [`--encrypt-password`](backup-encrypted-innodb-options.md) is required for the following purposes:

- If the server is using the `component_keyring_encrypted_file` keyring component, the user must use the option [`--encrypt-password`](backup-encrypted-innodb-options.md) to supply to **mysqlbackup** the keyring file encryption password that has been set on the server with the `component_keyring_encrypted_file.cnf` file. **mysqlbackup** then copies over from the server the encrypted keyring data file, which contains the replication master key used to encrypt all the passwords for the individual log files, into the `meta` folder in the backup and names the file `keyring_kef`.
- If the server uses a keyring plugin or component other than `component_keyring_encrypted_file`, **mysqlbackup** accesses the keyring to obtain the replication master key and uses it to decrypt the individual log files' passwords. The replication master key is then put into a keyring data file, which is encrypted with the user password supplied with the option [`--encrypt-password`](backup-encrypted-innodb-options.md), and then saved under the `meta` folder in the backup with the name `keyring_kef`.

When restoring encrypted binary or relay logs, the same password used for backing up the database must be supplied with the [`--encrypt-password`](backup-encrypted-innodb-options.md) option. **mysqlbackup** restores the encrypted keyring data file to its proper location on the server. If the backed up server used the `component_keyring_file` keyring component. **mysqlbackup** creates a `manifest` file and the configuration file `component_keyring_file.cnf` (which contains the password used with the [`--encrypt-password`](backup-encrypted-innodb-options.md) option during the restore) on the restored server, so that the server will load `component_keyring_file` when it restarts. Otherwise, **mysqlbackup** creates a `manifest` file and the configuration file `component_keyring_encrypted_file.cnf` (which contains the password used with the [`--encrypt-password`](backup-encrypted-innodb-options.md) option during the restore) on the restored server, so that the server will load `component_keyring_encrypted_file` when it restarts.

If you want to use another keyring plugin or component (for example, the backed-up server was using `keyring_aws` and you want the restored server to use it too, or you simply want to switch to a new component or plugin), a [keyring migration](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/keyring-key-migration.html) can be performed.

**For Incremental Backups.** For a series of incremental backups, if a keyring plugin or component other than `component_keyring_encrypted_file` is being used on the server, users can provide a different value for [`--encrypt-password`](backup-encrypted-innodb-options.md) for any of the full or incremental backup in the backup sequence. However, the password used to make the specific full or incremental backup must be provided to restore that backup. When starting the server after restoring a series of incremental backups, the password used for the restore of the last incremental backup should be supplied to the server.