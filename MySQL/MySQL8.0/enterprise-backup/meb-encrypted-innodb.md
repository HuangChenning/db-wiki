---
title: "Chapter 6 Working with Encrypted InnoDB Tablespaces"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/meb-encrypted-innodb.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

MySQL Enterprise Backup supports encrypted InnoDB tablespaces. For details on how the MySQL server encrypts and decrypts InnoDB tablespaces, see [InnoDB Data-at-Rest Encryption](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-data-encryption.html) —it explains concepts like master key and tablespace keys, which are important for understanding how MySQL Enterprise Backup works with encrypted InnoDB tablespaces.

When InnoDB tablespace encryption uses a centralized key management solution, the feature is referred to as “MySQL Enterprise Transparent Data Encryption (TDE).”

The following is a brief description on how encrypted InnoDB tablespaces are handled by MySQL Enterprise Backup in backup, restore, and apply-log operations.

Note

- [Encrypted InnoDB undo logs](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-data-encryption.html#innodb-data-encryption-undo-log) are supported by MySQL Enterprise Backup *only for release 8.0.16 and later*. The encrypted undo tablespaces are handled the same way as the encrypted tablespaces for InnoDB tables.
- [Encrypted InnoDB redo logs](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-data-encryption.html#innodb-data-encryption-redo-log) are supported by MySQL Enterprise Backup *only for release 8.0.17 and later*. The encrypted redo tablespaces are handled the same way as the encrypted tablespaces for InnoDB tables.
- Backing up and restoring encrypted InnoDB tables created using the [keyring components](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/keyring-component-plugin-comparison.html) are supported by MySQL Enterprise Backup *only for release 8.0.26 and later*.

**Backing up a database server with encrypted InnoDB tablespaces.**

Important

For MySQL Enterprise Backup to backup encrypted InnoDB tablespaces, the operating system user that runs MySQL Enterprise Backup must have write permission for the keyring file on the server if the `keyring_file` or `keyring_aws` plugin is used on it.

When the database server uses encrypted InnoDB tablespaces, MySQL Enterprise Backup always stores the master key for encryption in an encrypted file inside the backup, irrespective of the kind of keyring plugin or component the server uses. The following is a typical command for backing up a database server containing encrypted InnoDB tablespaces:

```
$ mysqlbackup --defaults-file=/home/dbadmin/my.cnf --backup-image=/home/admin/backups/my.mbi \
  --backup-dir=/home/admin/backup-tmp --encrypt-password="password" backup-to-image
```

During the backup operation, **mysqlbackup** copies the encrypted InnoDB tablespace files into the backup, and also performs the following actions:

- **mysqlbackup** contacts the MySQL server to determine the keyring plugin or component the server is using.
- If the server is using the `keyring_encrypted_file` plugin or the `component_keyring_encrypted_file` component, the user must use the option [`--encrypt-password`](backup-encrypted-innodb-options.md) to supply to **mysqlbackup** the keyring file encryption password that has been set on the server either with the [`--keyring_encrypted_file_password`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/keyring-system-variables.html#sysvar_keyring_encrypted_file_password) option (if the plugin is used) or with the `component_keyring_encrypted_file.cnf` file (if the component is used). **mysqlbackup** then copies over from the server the encrypted keyring data file, which contains the master key used to encrypt all the tablespace keys, into the `meta` folder in the backup; the file is encrypted with the user password supplied with the option [`--encrypt-password`](backup-encrypted-innodb-options.md). The encrypted tablespace files are also copied into the backup.
- If the server uses a keyring plugin other than `keyring_encrypted_file` or a keyring component other than `component_keyring_encrypted_file`, **mysqlbackup** accesses the keyring to obtain the master key and uses it to decrypt the encrypted tablespace keys, which were used to encrypt the InnoDB tablespaces on the server. The master key is then put into a keyring data file named `keyring_kef` and saved in the `meta` folder in the backup; the file is encrypted with the user password supplied with the option [`--encrypt-password`](backup-encrypted-innodb-options.md).
	Notes
	- Backing up a server that uses a keyring plugin other than `keyring_encrypted_file` or a keyring component other than `component_keyring_encrypted_file` is only supported for servers that allow socket connections or TCP/IP connections using TLS; it is, therefore, not supported when, for example, the server is running on a Windows platform and only allows shared memory connections.
	- Users who do not want to supply the password on the command line or in a defaults file may use the [`--encrypt-password`](backup-encrypted-innodb-options.md) option without specifying any value; **mysqlbackup** then asks the user to type in the password before the operation starts. This applies to all commands that use the [`--encrypt-password`](backup-encrypted-innodb-options.md) option.
	- If the server uses the `keyring_hashicorp` plugin, use the [`--encrypt-password`](backup-encrypted-innodb-options.md) to supply the HashiCorp Vault AppRole authentication secret ID, which was the value of [`keyring_hashicorp_secret_id`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/keyring-system-variables.html#sysvar_keyring_hashicorp_secret_id) on the server to be backed up.

An [`extract`](backup-commands-single-file.md) or [`image-to-backup-dir`](backup-commands-single-file.md) command for an image backup containing encrypted InnoDB tablespaces does not require the [`--encrypt-password`](backup-encrypted-innodb-options.md) option.

**Restoring a backup with encrypted InnoDB tablespaces.** The following is a typical command for restoring a single-file backup containing encrypted InnoDB tablespaces:

```
$ mysqlbackup  --defaults-file=/usr/local/mysql/my.cnf  --backup-image=/home/admin/backups/my.mbi \
    --backup-dir=/home/admin/restore-tmp --encrypt-password="password" copy-back-and-apply-log
```

The same password used for backing up the database server must be supplied with the [`--encrypt-password`](backup-encrypted-innodb-options.md) option for a restore operation. During a restore, **mysqlbackup** copies the encrypted InnoDB tablespace files onto the server. It also performs the following actions:

- *When any keyring plugin other than `keyring_file` was used on the backed-up server,* **mysqlbackup** restores the encrypted keyring data file to its proper location on the server. The restored server has to be started with `keyring_encrypted_file` plugin and with the options [`keyring_encrypted_file_data`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/keyring-system-variables.html#sysvar_keyring_encrypted_file_data) and [`--keyring_encrypted_file_password`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/keyring-system-variables.html#sysvar_keyring_encrypted_file_password) (which should supply the server with the same password used with the [`--encrypt-password`](backup-encrypted-innodb-options.md) option during the restore). After the server is up and running, if another keyring plugin or component is needed (for example, the backed-up user was using `keyring_aws` and the restored server is supposed to use it too), a [keyring migration](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/keyring-key-migration.html) can be performed.
- *When the `keyring_file` keyring plugin was used on the backed-up server,* **mysqlbackup** uses the password supplied with the [`--encrypt-password`](backup-encrypted-innodb-options.md) option to decrypt the keyring data file and then restores it under the data directory with the file name `keyring_kuf` for the `keyring_file` plugin to use.
- *When the `component_keyring_encrypted_file.cnf` keyring component was used on the backed-up server,* **mysqlbackup** restores the encrypted keyring data file to its proper location on the server, and also creates a `manifest` file and the configuration file `component_keyring_encrypted_file.cnf` (which contains the password used with the [`--encrypt-password`](backup-encrypted-innodb-options.md) option during the restore) on the restored server, so that the server will load the `component_keyring_encrypted_file` component when it restarts.
- *When the `component_keyring_file` keyring component was used on the backed-up server,* **mysqlbackup** uses the password supplied with the [`--encrypt-password`](backup-encrypted-innodb-options.md) option to decrypt the keyring data file and then restores it to the proper location on the server. It also creates a `manifest` file and the configuration file `component_keyring_file.cnf` on the restored server, so that the server will load the `component_keyring_file` component when it restarts.

If a keyring component is used on the restored server, take these additional steps:

- *To use global manifest and configuration file for starting the keyring component:*
	- Copy the `manifest` file from restored data directory to the folder where the `mysqld` binary resides.
	- Copy the configuration file `component_keyring_file.cnf` from the restore data directory to the folder where the component binary resides.
- *To use local manifest and configuration file for starting the keyring component:*
	- Create a new `manifest` file with following contents in the folder where the `mysqld` binary resides
		```
		{ "read_local_manifest": true }
		```
	- Create a new configuration file `component_keyring_file.cnf` with following contents in the folder where the component binary resides:
		```
		{ "read_local_config": true }
		```

**For Incremental Backups.** For a series of incremental backups, if a keyring plugin other than `keyring_encrypted_file` or a component other than `component_keyring_encrypted_file` is being used on the server, users can provide a different value for [`--encrypt-password`](backup-encrypted-innodb-options.md) for any of the full or incremental backup in the backup sequence. However, the password used to make the specific full or incremental backup must be provided to restore that backup, and, if a keyring plug-in is used, when starting the server after restoring a series of incremental backups, the password used for the restore of the *last* incremental backup should be supplied to the server (except when the `keyring_file plugin` is used, which does not require the [`--keyring_encrypted_file_password`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/keyring-system-variables.html#sysvar_keyring_encrypted_file_password) option to start).

**Advanced: Creating and Restoring a directory backup with encrypted InnoDB tablespaces.** The following is a typical command for creating a directory backup containing encrypted InnoDB tablespaces:

```
$ mysqlbackup --defaults-file=/home/dbadmin/my.cnf --backup-dir=/home/admin/backup \
    --encrypt-password="password" backup
```

The following is a typical command for preparing the backup with the [`apply-log`](backup-commands-update.md) command:

```
$ mysqlbackup --backup-dir=/home/admin/backup  --encrypt-password="password" apply-log
```

Notice that the user password supplied during the backup must be supplied with the [`--encrypt-password`](backup-encrypted-innodb-options.md) option, as the tablespace keys and then the tablespaces must be decrypted before the log can be applied. The same requirement applies when you try to update an encrypted backup with an encrypted incremental backup using the [`apply-incremental-backup`](backup-commands-update.md) command:

```
$ mysqlbackup  --backup-dir=/home/admin/backup --incremental-backup-dir=/home/admin/backup-in \
    --encrypt-password="password" apply-incremental-backup
```

If you used different values for [`--encrypt-password`](backup-encrypted-innodb-options.md) for the full or incremental backups in the backup sequence, make sure you supply the very password you used to create the individual backup when you perform an [`apply-log`](backup-commands-update.md) or [`apply-incremental-backup`](backup-commands-update.md) operation with it.

Next, a [`copy-back`](backup-commands-restore.md) command restores the prepared backup onto the server:

```
$ mysqlbackup  --defaults-file=/usr/local/mysql/my.cnf  --backup-dir=/home/admin/backup copy-back
```

Notice that the [`--encrypt-password`](backup-encrypted-innodb-options.md) option is not required for this step.

You can combine the two steps of [`apply-log`](backup-commands-update.md) and [`copy-back`](backup-commands-restore.md) into one by running the [`copy-back-and-apply-log`](backup-commands-restore.md) command, for which the [`--encrypt-password`](backup-encrypted-innodb-options.md) option is required:

```
$ mysqlbackup  --defaults-file=/usr/local/mysql/my.cnf  --backup-dir=/home/admin/backup \ 
  --encrypt-password="password" copy-back-and-apply-log
```

**Limitations.** Certain limitations apply when MySQL Enterprise Backup works with encrypted InnoDB tablespaces:

- *For MySQL Enterprise Backup 8.0.20 and earlier:* During a [`validate`](backup-commands-validate.md) operation, if **mysqlbackup** encounters any encrypted InnoDB tablespaces, it issues a warning and then skips over them.
- *For MySQL Enterprise Backup 8.0.20 and earlier:* For partial backups using transportable table spaces (that is, when the [`--use-tts`](backup-partial-options.md) option is used), encrypted InnoDB tables are never included in a backup. A warning is issued in the log file whenever an encrypted InnoDB table that matches the table selection criteria has been skipped over.
- The [`--skip-unused-pages`](backup-capacity-options.md) option has no effect on encrypted InnoDB tables during a backup (that is, empty pages for those tables are not skipped).
- If the server performs a [master key rotation](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-data-encryption.html#innodb-data-encryption-master-key-rotation) when a backup is running, the resulting backup might become corrupted.