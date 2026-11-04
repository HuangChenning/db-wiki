---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/acfs-commands-encryption.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

This topic provides a summary of the commands for Oracle ACFS encryption.

Table 6-34 lists the Oracle ACFS encryption commands with brief descriptions. For an overview of Oracle ACFS encryption, refer to [Oracle ACFS Encryption](understand-acfs-admin.md).

For information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

Note:

Starting with Oracle ACFS 21c, Oracle ACFS encryption is desupported on Solaris and Microsoft Windows operating systems. Oracle ACFS Encryption on Oracle Solaris and Microsoft Windows is based on RSA technology. Retirement of RSA technology has been announced. Oracle ACFS Encryption continues to be supported on Linux, and is unaffected by this deprecation, because Linux uses an alternative technology.

Table 6-34 Summary of commands for Oracle ACFS encryption

| Command | Description |
| --- | --- |
| acfsutil encr info | Displays encryption-related information about Oracle ACFS file systems. |
| acfsutil encr init | Initializes ACFS encryption. Creates encryption key store within OCR and sets up Oracle Key Vault as an alternative encryption key store. |
| acfsutil encr off | Disables encryption for an Oracle ACFS file system. |
| acfsutil encr on | Encrypts an Oracle ACFS file system. |
| acfsutil encr passwd | Changes password for password-protected PKCS wallets in OCR encryption key store, or changes password stored in autologin wallet for Oracle Key Vault endpoint. |
| acfsutil encr rekey | Generates a new key and re-encrypts an Oracle ACFS file system. |
| acfsutil encr set | Sets or changes encryption parameters for an Oracle ACFS file system. |
| acfsutil keystore migrate | Migrates OCR encryption key store between password-protected PKCS wallets and passwordless SSO wallets. |

### acfsutil encr info

Purpose

Displays encryption-related information about Oracle ACFS file systems, directories, or files.

Syntax and Description

```
acfsutil encr info -h
acfsutil encr info -m mount_point [[-r] path [path …]]
```

`acfsutil` `encr` `info` `-h` displays help text and exits.

Table 6-35 contains the options available with the `acfsutil` `encr` `info` command.

Table 6-35 Options for the acfsutil encr info command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-r` | Specifies recursive action under an existing directory folder identified by `path`. |
| `path` | Specifies the absolute or relative path of a directory. Multiple path values are allowed. |

If `-m` is specified without a `path`, the encryption status, algorithm, and key length are displayed for the file system level.

If `-r` is specified with a `path`, the encryption status, algorithm, and key length are displayed for all objects under the directory specified by `path`.

The `acfsutil` `encr` `info` command displays encryption status and parameters for files in a snapshot if the files are specified with the `path` option.

Any user can run this command to display encryption information about a file system, directory, or file.

If the `acfsutil` `encr` `info` command is run as a system administrator, then the output displays the types of key store used. The types are ACFS encryption key store with passwordless SSO wallets, ACFS encryption key store with password-protected PKCS wallets, and Oracle Key Vault as the key store (OKV).

Examples

The following are examples of the use of `acfsutil` `encr` `info`.

Example 6-31 Using the acfsutil encr info command

```
# /sbin/acfsutil encr info -m /acfsmounts/acfs1

# /sbin/acfsutil encr info -m /acfsmounts/acfs1 
                           -r /acfsmounts/acfs1/myfiles
```

### acfsutil encr init

Purpose

Initializes ACFS encryption. Creates encryption key store within OCR and sets up Oracle Key Vault as an alternative encryption key store.

Syntax and Description

```
acfsutil encr init -h
acfsutil encr init [-p ] [-o]
```

`acfsutil` `encr` `init` `-h` displays help text and exits.

Table 6-36 contains the options available with the `acfsutil` `encr` `init` command.

Table 6-36 Options for the acfsutil encr init command

| Option | Description |
| --- | --- |
| `-p` | If not specified, create encryption key store within OCR using passwordless SSO wallets for key storage. If specified, create encryption key store within OCR using password-protected PKCS wallets for key storage. |
| `-o` | Create Oracle Key Vault autologin wallet to allow ACFS to autologin to Oracle Key Vault. This enables automounts and passwordless `acfsutil ` encryption operations for ACFS file systems that use the Oracle Key Vault as the encryption key store. |

The `acfsutil` `encr` `init` command must be run before any other `acfsutil` encryption commands can be run. This command must be run once for each cluster on which Oracle ACFS encryption is run. This command must be run in either case of using the OCR as the encryption key store or Oracle Key Vault as the encryption key store.

If the `-p` option is not specified, an encryption key store will be created within the OCR using passwordless SSO wallets. If the `-p` option is specified, an encryption key store will be created within the OCR using password-protected PKCS wallets. You must provide a password for the PKCS wallets when prompted. The password must conform to the format:
- The maximum number of characters is 20.
- The minimum number of characters is 8.
- The password must contain at least one digit.
- The password must contain at least one letter.

If the `-o` option is specified, then in addition to creating an encryption key store within the OCR, an autologin wallet will also be created for the Oracle Key Vault. This Oracle Key Vault autologin wallet will enable ACFS to autologin to the Oracle Key Vault.

The Oracle Key Vault autologin wallet enables the following functionality:

- Creating the Oracle Key Vault autologin wallet enables all forms of automount (e.g. CRS automount, OS-level automount, etc) to correctly mount ACFS file systems that use the Oracle Key Vault as the encryption key store. Without the Oracle Key Vault autologin wallet, those ACFS file systems will not be correctly mounted by automounts, causing the encrypted files within the ACFS file system to be inaccessible.
- Creating the Oracle Key Vault autologin wallet enables `acfsutil` encryption operations to be performed passwordless for ACFS file systems that use the Oracle Key Vault as the encryption key store.

When the `-o` option is used to create the Oracle Key Vault autologin wallet, note that the `ORACLE_BASE`, `ORACLE_HOME`, `ORACLE_SID`, and `OKV_HOME` environment variables must be set appropriately for a login to the Oracle Key Vault endpoint. Additionally, if the Oracle Key Vault endpoint requires a password for login, the `-o` option will prompt for the Oracle Key Vault endpoint password. The Oracle Key Vault endpoint password will be saved within the autologin wallet to enable ACFS to autologin to the Oracle Key Vault.

Note that all Oracle Key Vault endpoints within the same cluster must share the same endpoint password to allow ACFS to autologin to the Oracle Kev Vault from all nodes. If any Oracle Key Vault endpoint has a different endpoint password from the password stored in the Oracle Key Vault autologin wallet, ACFS will be unable to autologin to the Oracle Key Vault through that endpoint.

If the `-o` option is specified and an encryption key store within the OCR already exists, then the creation of the encryption key store within the OCR will be skipped and only the creation of the Oracle Key Vault autologin wallet will be performed.

If both the -p and `-o` options are specified, note that two passwords may be requested, one for the PKCS wallets in the OCR encryption key store, one for the Oracle Key Vault endpoint.

Only a user with root or system administrator privileges can run this command.

Examples

The following is an example of the use of `acfsutil` `encr` `init`.

Example 6-32 Using the acfsutil encr init command

```
# /sbin/acfsutil encr init
```

### acfsutil encr off

Purpose

Disables encryption for an Oracle ACFS file system, directories, or individual files.

Syntax and Description

```
acfsutil encr off -h
acfsutil encr off -m mount_point [[-r] path [ path ...]]
```

`acfsutil` `encr` `off` `-h` displays help text and exits.

Table 6-38 contains the options available with the `acfsutil` `encr` `off` command.

Table 6-37 Options for the acfsutil encr off command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-r` | Specifies to disable encryption recursively under an existing directory identified by `path`. |
| `path` | Specifies the absolute or relative path of a directory. Multiple path values are allowed. |

Only an administrator can run this command on an Oracle ACFS file system (`-m` option without a `path` specified). When the `-m` option is specified without a `path`, all the files under the mount point are decrypted.

The `path` option can specify a path to a file or directory in a read-write snapshot. If the `-r` option is specified with the command on the root directory, the command does not transverse the snapshots under the `.ACFS` directory. If a decryption operation is specified at the file system level, then the operation does not process files and directories of snapshots in the `.ACFS/snaps/` directory.

Only a user with root or system administrator privileges can run this command to disable encryption on a file system. The file owner can also run this command to disable encryption on a directory or file.

Examples

The following are examples of the use of `acfsutil` `encr` `off`.

Example 6-33 Using the acfsutil encr off command

```
# /sbin/acfsutil encr off -m /acfsmounts/acfs1

# /sbin/acfsutil encr off -m /acfsmounts/acfs1
                          -r /acfsmounts/acfs1/myfiles
```

### acfsutil encr on

Purpose

Encrypts an Oracle ACFS file system, directories, or individual files.

Syntax and Description

```
acfsutil encr on -h
acfsutil encr on -m mount_point
          [-a {AES} -k {128|192|256}] [[-r] path [path...]]
```

`acfsutil` `encr` `on` `-h` displays help text and exits.

Table 6-38 contains the options available with the `acfsutil` `encr` `on` command.

Table 6-38 Options for the acfsutil encr on command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-a` `algorithm` | Specifies the encryption algorithm type for a directory or file. Advanced Encryption Standard (AES) is the only encryption algorithm supported for this release. |
| `-k` `key_length` | Specifies the encryption key length for a directory or file. |
| `-r` | Specifies encryption recursively under existing directory folder identified by `path`. |
| `path` | Specifies the absolute or relative path of a directory. Multiple path values are allowed. |

The default values for the `-a` and `-k` are determined by the volume parameters specified when `acfsutil` `encr` `set` was run. To set the key length at the volume level, use the `acfsutil` `encr` `set` command.

Only an administrator can run this command on an Oracle ACFS file system (`-m` option without a `path` specified). When the `-m` option is specified without a `path`, all the files under the mount point are encrypted.

The `path` option can specify a path to a file or directory in a read-write snapshot. If the `-r` option is specified with the command on the root directory, the command does not transverse the snapshots under the `.ACFS` directory. If an encryption operation is specified at the file system level, then the operation does not process files and directories of snapshots in the `.ACFS/snaps/` directory.

When you run `acfsutil` `encr` `on` with the `-r` option, the command encrypts the specified directory recursively, but does not enable encryption on the file system level.

Only a user with root or system administrator privileges can run this command to enable encryption on a file system. The file owner can also run this command to enable encryption on a directory or file.

Examples

The following are examples of the use of `acfsutil` `encr` `on`.

Example 6-34 Using the acfsutil encr on command

```
# /sbin/acfsutil encr on -m /acfsmounts/acfs1

# /sbin/acfsutil encr on -m /acfsmounts/acfs1
                         -a AES -k 128 -r /acfsmounts/acfs1/myfiles
```

### acfsutil encr passwd

Purpose

Changes password for password-protected PKCS wallets in OCR encryption key store, or changes password stored in autologin wallet for Oracle Key Vault endpoint.

Syntax and Description

```
acfsutil encr passwd -h
acfsutil encr passwd [-o]
```

`acfsutil` `encr` `passwd` `-h` displays help text and exits.

Options for the Table 6-38 contains the options available with the `acfsutil` `encr` `passwd` command.

Table 6-39 Options for the acfsutil encr passwd command

| Option | Description |
| --- | --- |
| `-o` | If not specified, change password for password-protected PKCS wallets in OCR encryption key store. If specified, change password stored in Oracle Key Vault autologin wallet for the Oracle Key Vault endpoint. |

If the -o option is not specified, this command changes the password for the password-protected PKCS wallets in the OCR encryption key store. The command must be run on an OCR encryption key store that uses password-protected PKCS wallets for key storage. The command cannot be run on an OCR encryption key store that uses passwordless SSO wallets for key storage.

The command will prompt for the existing password of the password-protected PKCS wallets, then prompt for a new password. The new password must conform to the format:

- The maximum number of characters is 20.
- The minimum number of characters is 8.
- The password must contain at least one digit.
- The password must contain at least one letter.

If the `-o` option is specified, this command changes the password stored in the Oracle Key Vault autologin wallet for the Oracle Key Vault endpoint. The command will prompt for the existing password of the Oracle Key Vault endpoint, then prompt for the new password. The command will verify that the new password can correctly login to the Oracle Key Vault endpoint, then store the new password in the Oracle Key Vault autologin wallet.

Only a user with root or system administrator privileges can run this command.

Examples

The following is an example of the use of `acfsutil` `encr` `passwd` command.

Example 6-35 Using the acfsutil encr passwd command

```
# /sbin/acfsutil encr passwd
```

### acfsutil encr rekey

Purpose

Generates a new key and re-encrypts volume or file.

Syntax and Description

```
acfsutil encr rekey -h
acfsutil encr rekey -m mount_point
    {-f [-r] path [path…] |-v } [-a {AES} -k {128|192 |256}]
```

`acfsutil` `encr` `rekey` `-h` displays help text and exits.

Table 6-40 contains the options available with the `acfsutil` `encr` `rekey` command.

Table 6-40 Options for the acfsutil encr rekey command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-f` \[`-r`\] `path`... | Generates a new file encryption key for the specified path and then encrypts the data with the new key.  If -r is specified, the rekey operation is performed recursively under `path`.  `path` specifies the absolute or relative path of a directory. Multiple path values are allowed. |
| `-v` | Generates a new volume encryption key (VEK) for the specified mount point and then encrypts all the file encryption keys in file system with the new key. Prompts for the wallet password because the wallet must be accessed to store the new VEK.  The generated key is stored in the key store that was previously configured with the `acfsutil` `encr` `init` command. |
| `-a` `algorithm` | Specifies the algorithm. Advanced Encryption Standard (AES) is the only encryption supported for this release. |
| `-k` `key_length` | Specifies the key length for the directory or file specified by `path`. |

The default values for the `-a` and `-k` are determined by the volume parameters specified when `acfsutil` `encr` `set` was run.

The `path` option can specify a path to a file or directory in a read-write snapshot. If the `-r` option is specified with the command on the root directory, the command does not transverse the snapshots under the `.ACFS` directory. If a rekey operation is specified at the file system level, then the operation does not process files and directories of snapshots in the `.ACFS/snaps/` directory.

If Oracle Key Vault is the key store for the file system, then the Oracle Key Vault home environmental variable (`OKV_HOME`) must be set when using the `-v` option to generate a new volume key. If the client was configured to use a password with Oracle Key Vault, then the same password must be entered when prompted.

See Also:

[Oracle Key Vault Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OKVAG10489) for information about Oracle Key Vault

Only a user with root or system administrator privileges can run this command with the `-v` option. The file owner can also run this command with the `-f` option to rekey encryption on the directory or file.

Examples

The following are examples of the use of `acfsutil` `encr` `rekey`.

Example 6-36 Using the acfsutil encr rekey command

```
# /sbin/acfsutil encr rekey -m /acfsmounts/acfs1 -v

# /sbin/acfsutil encr rekey -m /acfsmounts/acfs1 -f
                            -r /acfsmounts/acfs1/myfiles
```

### acfsutil encr set

Purpose

Sets or changes encryption parameters for an Oracle ACFS file system.

Syntax and Description

```
acfsutil encr set -h
acfsutil encr set [ [-a {AES} -k {128|192|256}] [-e] | -u ] -m mount_point
```

`acfsutil` `encr` `set` `-h` displays help text and exits.

Table 6-41 contains the options available with the `acfsutil` `encr` `set` command.

Table 6-41 Options for the acfsutil encr set command

| Option | Description |
| --- | --- |
| `-a` `algorithm` | Specifies the algorithm. Advanced Encryption Standard (`AES`) is the default value and the only encryption supported for this release. The algorithm must be specified if `-k` is specified. |
| `-k` { `128` \| `192` \| `256` } | Specifies the key length. The key length is set at the volume level. The default is `192`. Must be specified if `-a` is specified. |
| `-e` | Specifies to use Oracle Key Vault as the key store. |
| `-u` | Backs out encryption. Decrypts all encrypted files in the file system and reverts the file system to the state before `acfsutil` `encr` `set` was run on the file system. |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |

Before running the `acfsutil` `encr` `set` command, you must first run the `acfsutil` `encr` `init` command.

The `acfsutil` `encr` `set` command configures encryption parameters for a file system, transparently generates a volume encryption key, and stores that the generated key in the key store that was previously configured with the `acfsutil` `encr` `init` command.

In addition `acfsutil` `encr` `set` creates the `mount_point` `/.Security` `/encryption/logs/` directory that contains the log file (`encr-` `hostname` `_fsid.log`) that collects auditing and diagnostic data.

Password requirements when storing the key are dependent on how the encryption key storage was configured. If `-p` was specified with `acfsutil` `encr` `init`, then a password is required to run this command.

Before using the `-e` option to specify Oracle Key Vault as the key store, Oracle Key Vault must be configured first. If you want to choose Oracle Key Vault as the key store for the file system, then the Oracle Key Vault home environmental variable (`OKV_HOME`) must be set when running the command with the `-e` option. If the client was configured to use a password with Oracle Key Vault, then the same password must be entered when prompted.

See Also:

[Oracle Key Vault Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OKVAG-GUID-0D169EB8-C355-459A-9ABD-325CA5B46DD0) for information about configuring Oracle Key Vault

The `acfsutil` `encr` `set` `–u` command is not allowed if any snapshots exist in the file system.

Only a user with root or system administrator privileges can run the `acfsutil` `encr` `set` command.

Examples

The following example shows the use of `acfsutil` `encr` `set` command.

Example 6-37 Using the acfsutil encr set command

```
# /sbin/acfsutil encr set -a AES -k 256 -m /acfsmounts/acfs1
```

### acfsutil keystore migrate

Purpose

Migrates the ACFS encryption key store between PKCS and SSO wallets.

Syntax and Description

```
acfsutil keystore migrate -h
acfsutil keystore migrate [-p ]
```

`acfsutil` `keystore migrate` `-h` displays help text and exits.

Table 6-36 contains the options available with the `acfsutil` `keystore migrate` command.

Table 6-42 Options for the acfsutil keystore migrate command

| Option | Description |
| --- | --- |
| `-p` | Converts the ACFS encryption key store from passwordless SSO wallets to password-protected PKCS wallets for key storage. |

If the `-p` option is specified, `acfsutil` `keystore` `migrate` converts the ACFS encryption key store from passwordless SSO wallets to password-protected PKCS wallets for key storage. If the `-p` option is not specified, `acfsutil` `keystore` `migrate` converts the ACFS encryption key store from password-protected PKCS wallets to passwordless SSO wallets for key storage.

If the `-p` option is specified, you must provide a password when prompted. The password must conform to the format:
- The maximum number of characters is 20.
- The minimum number of characters is 8.
- The password must contain at least one digit.
- The password must contain at least one letter.

Only a user with root or system administrator privileges can run this command.

Examples

The following is an example of the use of `acfsutil` `keystore` `migrate`.

Example 6-38 Using the acfsutil keystore migrate command

```
# /sbin/acfsutil keystore migrate
```