---
title: "Chapter 20 mysqlbackup Command-Line Options"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/mysqlbackup.usage.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

The following sections describe the command-line options for the different modes of operation of **mysqlbackup**.

The table below list all the command options for **mysqlbackup**. Use the hyperlinks at the option names to jump to the detailed descriptions for the options.

Note

The command options can also be specified in configuration files; see explanations in [Chapter 21, *Configuration Files and Parameters*](config-file-parameters.md). **mysqlbackup** follows the MySQL standard practice for handling duplicate options, whether specified in a configuration file, on the command line, or both. Options are processed first from configuration files, then from the command line. If an option is specified more than once, the last instance takes precedence.

**Table 20.1 List of All Options**

| Option Name | Description |
| --- | --- |
| [\--backup-dir](backup-repository-options.md) | The directory to store the backup data. |
| [\--backup-image](backup-repository-options.md) | Specifies the path name of the backup image. |
| [\--backup\_innodb\_data\_file\_path](backup-repository-options.md) | Specifies Innodb system tablespace files' path and size in backup. |
| [\--backup\_innodb\_data\_home\_dir](backup-repository-options.md) | Backup base directory for all InnoDB data files in the system tablespace. |
| [\--backup\_innodb\_log\_group\_home\_dir](backup-repository-options.md) | Backup directory for InnoDB log files. |
| [\--backup\_innodb\_undo\_directory](backup-repository-options.md) | The relative or absolute directory path where InnoDB creates separate tablespaces for the undo logs. |
| [\--character-sets-dir](connection-options.md) | Directory for character set files. |
| [\--cloud-access-key-id](backup-cloud-options.md) | AWS access key ID for logging onto Amazon S3. |
| [\--cloud-aws-region](backup-cloud-options.md) | Region for Amazon Web Services that mysqlbackup access for S3. |
| [\--cloud-basicauth-url](backup-cloud-options.md) | The URL for HTTP Basic Authentication for accessing Swift. |
| [\--cloud-bucket](backup-cloud-options.md) | The storage bucket for the backup image. |
| [\--cloud-buffer-size](backup-cloud-options.md) | Size of buffer for cloud operations. |
| [\--cloud-chunked-transfer](backup-cloud-options.md) | Use chunked transfer with cloud storage service. |
| [\--cloud-container](backup-cloud-options.md) | The Swift container for the backup image. |
| [\--cloud-host](backup-cloud-options.md) | The hostname for a storage service. |
| [\--cloud-identity-url](backup-cloud-options.md) | The URL of the Keystone identity service. |
| [\--cloud-object](backup-cloud-options.md) | The storage object for the backup image. |
| [\--cloud-object-key](backup-cloud-options.md) | The Amazon S3 object key for the backup image. |
| [\--cloud-password](backup-cloud-options.md) | Password for user specified by --cloud-user-id. |
| [\--cloud-proxy](backup-cloud-options.md) | Proxy address and port number for overriding the environment's default proxy settings for accessing cloud service. |
| [\--cloud-region](backup-cloud-options.md) | The Keystone region for the user specified by --cloud-user-id. |
| [\--cloud-secret-access-key](backup-cloud-options.md) | AWS secret access key. |
| [\--cloud-service](backup-cloud-options.md) | Cloud service for data backup or restoration. |
| [\--cloud-tempauth-url](backup-cloud-options.md) | The URL of the identity service for authenticating user credentials with Swift's TempAuth authentication system. |
| [\--cloud-tenant](backup-cloud-options.md) | The Keystone tenant for the user specified by --cloud-user-id. |
| [\--cloud-trace](backup-cloud-options.md) | Print trace information for cloud operations. |
| [\--cloud-user-id](backup-cloud-options.md) | User ID for accessing Swift. |
| [\--comments](backup-metadata-options.md) | Specifies comments string. |
| [\--comments-file](backup-metadata-options.md) | Specifies path to comments file. |
| [\--compress](backup-compression-options.md) | Create backup in compressed format. |
| [\--compress-level](backup-compression-options.md) | Specifies the level of compression. |
| [\--compress-method](backup-compression-options.md) | Specifies the compression algorithm. |
| [\--connect\_timeout](connection-options.md) | Connection timeout in seconds. |
| [\--datadir](server-repository-options.md) | Path to mysql server data directory. |
| [\--debug](standard-options.md) | Print debug information. |
| [\--decrypt](backup-encryption-options.md) | Decrypt backup image written in an MEB Secure File. |
| [\--default-character-set](connection-options.md) | Set the default character set. |
| [\--defaults-extra-file](standard-options.md) | Read this file after the global files are read. |
| [\--defaults-file](standard-options.md) | Only read default options from the given file. |
| [\--defaults-group-suffix](standard-options.md) | Also read option groups with the usual names and a suffix of str. |
| [\--disable-manifest](backup-single-file-options.md) | Disable generation of manifest files for a backup operation. |
| [\--dst-entry](backup-single-file-options.md) | Used with single-file backups to extract a single file or directory to a user-specified path. |
| [\--enable-cleartext-plugin](standard-options.md) | Enables the cleartext authentication plugin. |
| [\--encrypt](backup-encryption-options.md) | Encrypt backup image and write it in an MEB Secure File. |
| [\--encrypt-password](backup-encrypted-innodb-options.md) | The user-supplied password by which mysqlbackup encrypts the encryption keys for encrypted InnoDB tablespaces. |
| [\--error-code](standard-options.md) | The exit code for which the print-message command prints the corresponding exit message. |
| [\--exclude-tables](backup-partial-options.md) | Exclude in a backup or restore tables whose names match the regular expression REGEXP. |
| [\--exec-when-locked](backup-special-options.md) | Execute the specified utility in the lock phase near the end of the backup operation. |
| [\--help](standard-options.md) | Display help. |
| [\--host](connection-options.md) | Host name to connect. |
| [\--include-tables](backup-partial-options.md) | Include in a backup or a restore tables whose names match the regular expression REGEXP. |
| [\--incremental](backup-incremental-options.md) | Specifies that the associated backup or backup-to-image operation is incremental. |
| [\--incremental-backup-dir](backup-incremental-options.md) | Specifies the location for an incremental directory backup. |
| [\--incremental-base](backup-incremental-options.md) | The specification of base backup for --incremental option. |
| [\--incremental-with-redo-log-only](backup-incremental-options.md) | Specifies the incremental backup of InnoDB tables to be based on copying redo log to the backup, without including any InnoDB data files in the backup. |
| [\--innodb\_data\_home\_dir](server-repository-options.md) | Specifies base directory for all InnoDB data files in the shared system tablespace. |
| [\--innodb\_log\_group\_home\_dir](server-repository-options.md) | The directory path to InnoDB log files. |
| [\--key](backup-encryption-options.md) | The symmetric key used for encryption and decryption. |
| [\--key-file](backup-encryption-options.md) | The pathname of a file that contains the symmetric key used for encryption and decryption. |
| [\--limit-memory](backup-capacity-options.md) | The memory in MB available for the MEB operation. |
| [\--log-bin-index](server-repository-options.md) | Specifies the absolute path of the index file that lists all the binary log files. |
| [\--login-path](connection-options.md) | Read options from the named login path in the.mylogin.cnf login file. |
| [\--messages-logdir](backup-message-logging-options.md) | Specifies the path name of an existing directory for storing the message log. |
| [\--no-defaults](standard-options.md) | Do not read default options from any given file. |
| [\--no-history-logging](backup-metadata-options.md) | Disable history logging even if connection is available. |
| [\--no-locking](backup-capacity-options.md) | Disable all locking of tables during backups. |
| [\--no-redo-log-archive](backup-capacity-options.md) | Skip using redo log archiving during backups. |
| [\--number-of-buffers](backup-capacity-options.md) | Specifies the exact number of memory buffers to be used for the backup operation. |
| [\--on-disk-full](backup-capacity-options.md) | Specifies the behavior when a backup process encounters a disk-full condition. |
| [\--only-innodb](backup-partial-options.md) | Back up only InnoDB data and log files. |
| [\--only-known-file-types](backup-partial-options.md) | Includes only files of a list of known types in the backup. |
| [\--optimistic-busy-tables](backup-capacity-options.md) | Perform an optimistic backup, using the regular expression specified with the option to select tables that will be skipped in the first phase of an optimistic backup. |
| [\--optimistic-time](backup-capacity-options.md) | Perform an optimistic backup with the value specified with the option as the optimistic time—a time after which tables that have not been modified are believed to be inactive tables. |
| [\--page-reread-count](backup-capacity-options.md) | Maximum number of page re-reads. |
| [\--page-reread-time](backup-capacity-options.md) | Wait time before a page re-read. |
| [\--password](connection-options.md) | Connection password. |
| [\--pipe](connection-options.md) | alias for –protocol=pipe. |
| [\--plugin-dir](standard-options.md) | Specifies the directory for client-side plugins. |
| [\--port](connection-options.md) | TCP portnumber to connect to. |
| [\--print-defaults](standard-options.md) | Print a list of option values supplied by defaults files and exit. |
| [\--process-threads](backup-capacity-options.md) | Specifies the number of process-threads for the backup operation. |
| [\--progress-interval](backup-progress-report-options.md) | Interval between progress reports in seconds. |
| [\--protocol](connection-options.md) | Connection protocol. |
| [\--read-threads](backup-capacity-options.md) | Specifies the number of read-threads for the backup operation. |
| [\--relay-log-index](server-repository-options.md) | Specifies the absolute path of the index file that lists all the relay log files. |
| [\--rename](backup-partial-options.md) | Rename a single table when it is selected by the --include-tables option to be restored |
| [\--sbt-database-name](backup-single-file-options.md) | Used as a hint to the Media Management Software (MMS) for the selection of media and policies for tape backup. |
| [\--sbt-environment](backup-single-file-options.md) | Comma separated list of environment variable assignments to be given to the SBT library. |
| [\--sbt-lib-path](backup-single-file-options.md) | Path name of the SBT library used by software that manages tape backups. |
| [\--shared-memory-base-name](connection-options.md) | It designates the shared-memory name used by a Windows server to permit clients to connect using shared memory (Windows only). |
| [\--show-progress](backup-progress-report-options.md) | Instructs mysqlbackup to periodically output short progress reports known as progress indicators on its operation. |
| [\--skip-binlog](backup-capacity-options.md) | Do not include binary log files during backup, or do not restore binary log files during restore. |
| [\--skip-final-rescan](backup-capacity-options.md) | Skip the final rescan for InnoDB tables that are modified by DDL operations. |
| [\--skip-messages-logdir](backup-message-logging-options.md) | Disable logging to teelog file. |
| [\--skip-relaylog](backup-capacity-options.md) | Do not include relay log files during backup, or do not restore relay log files during a restore. |
| [\--skip-unused-pages](backup-capacity-options.md) | Skip unused pages in tablespaces when backing up InnoDB tables. |
| [\--sleep](backup-capacity-options.md) | Time to sleep in milliseconds after copying each 1MB of data. |
| [\--socket](connection-options.md) | Socket file to use to connect. |
| [\--src-entry](backup-single-file-options.md) | Identifies a file or directory to extract from a single-file backup. |
| [\--ssl-ca](connection-options.md) | CA file in PEM format (implies –ssl). |
| [\--ssl-capath](connection-options.md) | CA directory (check OpenSSL docs,implies --ssl). |
| [\--ssl-cert](connection-options.md) | X509 cert in PEM format (implies --ssl). |
| [\--ssl-cipher](connection-options.md) | SSL cipher to use (implies --ssl). |
| [\--ssl-key](connection-options.md) | X509 key in PEM format (implies --ssl). |
| [\--start-lsn](backup-incremental-options.md) | Specifies the highest LSN value included in a previous backup. |
| [\--suspend-at-end](backup-special-options.md) | Pauses the mysqlbackup command when the backup procedure is close to ending. |
| [\--trace](standard-options.md) | Trace level of messages by mysqlbackup. |
| [\--uncompress](backup-compression-options.md) | Uncompress a backup during an operation. |
| [\--use-tts](backup-partial-options.md) | Enable selective backup of InnoDB tables using transportable tablespaces (TTS). |
| [\--user](connection-options.md) | Database server user name to connect. |
| [\--verbose](standard-options.md) | Print more verbose information. |
| [\--version](standard-options.md) | Display version information. |
| [\--with-timestamp](backup-repository-options.md) | Create a subdirectory underneath the backup directory with a name formed from the timestamp of the backup operation. |
| [\--write-threads](backup-capacity-options.md) | Specifies the number of write-threads for the backup operation. |