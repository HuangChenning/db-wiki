---
title: "20.13 Encryption Options"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/backup-encryption-options.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

These options are for creating encrypted single-file backups and for decrypting them. See [Chapter 10, *Encryption for Backups*](meb-encryption.md) for more details and usage examples for the encryption and decryption functions of MySQL Enterprise Backup.

- `--encrypt`
	Encrypt the data when creating a backup image by a [`backup-to-image`](backup-commands-backup.md) operation, or when packing a backup directory into a single file with the [`backup-dir-to-image`](backup-commands-single-file.md) command. It cannot be used with the [`backup`](backup-commands-backup.md) or [`backup-and-apply-log`](backup-commands-backup.md) command.
- `--decrypt`
	Decrypt an encrypted backup image when performing an [`extract`](backup-commands-single-file.md), [`image-to-backup-dir`](backup-commands-single-file.md), or [`copy-back-and-apply-log`](backup-commands-restore.md) operation. It is also used for performing a [`validate`](backup-commands-validate.md) or [`list-image`](backup-commands-single-file.md) operation on an encrypted backup image.
	The option cannot be used in a [`apply-log`](backup-commands-update.md), [`backup-and-apply-log`](backup-commands-backup.md), or [`copy-back`](backup-commands-restore.md) operation. For restoration using the [`copy-back`](backup-commands-restore.md) command, the encrypted backup image has to be unpacked and decrypted first using the [`image-to-backup-dir`](backup-commands-single-file.md) or [`extract`](backup-commands-single-file.md) command, together with the `--decrypt` option.
- `--key` = *`STRING`*
	| Command-Line Format | `--key=KEY` |
	| --- | --- |
	| Type | String |
	The symmetric key for encryption and decryption of a backup image. It should be a 256-bit key, encoded as a string of 64 hexadecimal digits. See [Chapter 10, *Encryption for Backups*](meb-encryption.md) on how to create a key. The option is incompatible with the `--key-file` option.
- `--key-file` = *`PATH`*
	| Command-Line Format | `--key-file=FILE` |
	| --- | --- |
	| Type | File name |
	The pathname to file that contains a 256-bit key, encoded as a string of 64 hexadecimal digits, for encryption and decryption of a backup image. The option is incompatible with the `--key` option.