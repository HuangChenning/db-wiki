---
title: Oracle ACFS Command-Line Tools for Encryption
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfs_util009.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

Table 13-66 contains a summary of the commands for Oracle ACFS encryption.

You can run `acfsutil` `help` on all platforms to display help text. You can run `acfsutil` `version` on all platforms to display the Oracle ACFS version.

When the options are entered with commands on a Windows platform, use `/` instead of `-` with the option. For example, you can display help for `acfsutil` on a Linux platform with `acfsutil` `-h`. On a Windows platform, use `acfsutil` `/h`.

Note that a mount point on a Windows operating system can be a drive letter or a directory including the drive letter.

Table 13-66 Summary of commands for Oracle ACFS encryption

| Command | Description |
| --- | --- |
| acfsutil encr info | Displays encryption-related information about Oracle ACFS file systems. |
| acfsutil encr init | Creates storage for encryption keys. |
| acfsutil encr off | Disables encryption for an Oracle ACFS file system. |
| acfsutil encr on | Encrypts an Oracle ACFS file system. |
| acfsutil encr rekey | Generates a new key and re-encrypts an Oracle ACFS file system. |
| acfsutil encr set | Sets or changes encryption parameters for an Oracle ACFS file system. |

## acfsutil encr info

Purpose

Displays encryption-related information about Oracle ACFS file systems, directories, or files.

Syntax and Description

  
`acfsutil` `encr` `info` `-h`  
`acfsutil` `encr` `info` `-m` `mount_point` \[\[`-r`\] `path` \[`path` …\]\]  

`acfsutil` `encr` `info` `-h` displays help text and exits.

Table 13-67 contains the options available with the `acfsutil` `encr` `info` command.

Table 13-67 Options for the acfsutil encr info command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-r` | Specifies recursive action under an existing directory folder identified by `path`. |
| `path` | Specifies the absolute or relative path of a directory. Multiple path values are allowed. |

If `-m` is specified without a `path`, the encryption status, algorithm, and key length are displayed for the file system level.

If `-r` is specified with a `path`, the encryption status, algorithm, and key length are displayed for all objects under the directory specified by `path`.

The `acfsutil` `encr` `info` command displays encryption status and parameters for files in a snapshot if the files are specified with the `path` option.

This command fails when it is run on realm-secured objects.

Any user can run this command to display encryption information about a file system, directory, or file.

Examples

The following are examples of the use of `acfsutil` `encr` `info`.

Example 13-59 Using the acfsutil encr info command

```
# /sbin/acfsutil encr info -m /u01/app/acfsmounts/myacfs

# /sbin/acfsutil encr info -m /u01/app/acfsmounts/myacfs 
                           -r /u01/app/acfsmounts/myacfs/myfiles
```

## acfsutil encr init

Purpose

Creates storage for encryption keys.

Syntax and Description

  
`acfsutil` `encr` `init` `-h`  
`acfsutil` `encr` `init` \[`-p` \]  

`acfsutil` `encr` `init` `-h` displays help text and exits.

Table 13-68 contains the options available with the `acfsutil` `encr` `init` command.

Table 13-68 Options for the acfsutil encr init command

| Option | Description |
| --- | --- |
| `-p` | Creates PKCS (password-protected) storage for keys. |

The `acfsutil` `encr` `init` command must be run before any other encryption `acfsutil` commands can be run. This command must be run once for each cluster on which Oracle ACFS encryption is run.

If the `-p` option is specified, you must provide a password when prompted. The password must conform to the format that is described in ["acfsutil sec init"](asmfs_util008.md).

If the `-p` option is not specified, a single sign-on (SSO) wallet is created.

Only a user with root or system administrator privileges can run this command.

Examples

The following is an example of the use of `acfsutil` `encr` `init`.

Example 13-60 Using the acfsutil encr init command

```
# /sbin/acfsutil encr init
```

## acfsutil encr off

Purpose

Disables encryption for an Oracle ACFS file system, directories, or individual files.

Syntax and Description

  
`acfsutil` `encr` `off` `-h`  
`acfsutil` `encr` `off` `-m` `mount_point` \[\[`-r`\] `path` \[ `path`...\]\]  

`acfsutil` `encr` `off` `-h` displays help text and exits.

Table 13-70 contains the options available with the `acfsutil` `encr` `off` command.

Table 13-69 Options for the acfsutil encr off command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-r` | Specifies to disable encryption recursively under an existing directory identified by `path`. |
| `path` | Specifies the absolute or relative path of a directory. Multiple path values are allowed. |

This command cannot be run on security realm-protected files.

Only an administrator can run this command on an Oracle ACFS file system (`-m` option without a `path` specified). When the `-m` option is specified without a `path`, all the files under the mount point are decrypted.

The `path` option can specify a path to a file or directory in a read-write snapshot. If the `-r` option is specified with the command on the root directory, the command does not transverse the snapshots under the `.ACFS` directory. If a decryption operation is specified at the file system level, then the operation does not process files and directories of snapshots in the `.ACFS/snaps/` directory.

Only a user with root or system administrator privileges can run this command to disable encryption on a file system. The file owner can also run this command to disable encryption on a directory or file.

Examples

The following are examples of the use of `acfsutil` `encr` `off`.

Example 13-61 Using the acfsutil encr off command

```
# /sbin/acfsutil encr off -m /u01/app/acfsmounts/myacfs

# /sbin/acfsutil encr off -m /u01/app/acfsmounts/myacfs
                          -r /u01/app/acfsmounts/myacfs/myfiles
```

## acfsutil encr on

Purpose

Encrypts an Oracle ACFS file system, directories, or individual files.

Syntax and Description

  
`acfsutil` `encr` `on` `-h`  
`acfsutil` `encr` `on` `-m` `mount_point`  
 \[`-a` { `AES` } `-k` { `128` | `192` | `256` }\] \[\[`-r`\] `path` \[ `path`...\]\]  

`acfsutil` `encr` `on` `-h` displays help text and exits.

Table 13-70 contains the options available with the `acfsutil` `encr` `on` command.

Table 13-70 Options for the acfsutil encr on command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-a` `algorithm` | Specifies the encryption algorithm type for a directory or file. Advanced Encryption Standard (AES) is the only encryption algorithm supported for this release. |
| `-k` `key_length` | Specifies the encryption key length for a directory or file. |
| `-r` | Specifies encryption recursively under existing directory folder identified by `path`. |
| `path` | Specifies the absolute or relative path of a directory. Multiple path values are allowed. |

This command cannot be run on realm-protected files.

The default values for the `-a` and `-k` are determined by the volume parameters specified when `acfsutil` `encr` `set` was run. To set the key length at the volume level, use the `acfsutil` `encr` `set` command.

Only an administrator can run this command on an Oracle ACFS file system (`-m` option without a `path` specified). When the `-m` option is specified without a `path`, all the files under the mount point are encrypted.

The `path` option can specify a path to a file or directory in a read-write snapshot. If the `-r` option is specified with the command on the root directory, the command does not transverse the snapshots under the `.ACFS` directory. If an encryption operation is specified at the file system level, then the operation does not process files and directories of snapshots in the `.ACFS/snaps/` directory.

Only a user with root or system administrator privileges can run this command to enable encryption on a file system. The file owner can also run this command to enable encryption on a directory or file.

Examples

The following are examples of the use of `acfsutil` `encr` `on`.

Example 13-62 Using the acfsutil encr on command

```
# /sbin/acfsutil encr on -m /u01/app/acfsmounts/myacfs

# /sbin/acfsutil encr on -m /u01/app/acfsmounts/myacfs
                         -a AES -k 128 -r /u01/app/acfsmounts/myacfs/myfiles
```

## acfsutil encr rekey

Purpose

Generates a new key and re-encrypts volume or file.

Syntax and Description

  
`acfsutil` `encr` `rekey` `-h`  
`acfsutil` `encr` `rekey` `-m` `mount_point`  
 { `-f` \[`-r`\] `path` \[`path` …\] | `-v` } \[`-a` { `AES` } `-k` { `128` | `192` | `256` }\]  

`acfsutil` `encr` `rekey` `-h` displays help text and exits.

Table 13-71 contains the options available with the `acfsutil` `encr` `rekey` command.

Table 13-71 Options for the acfsutil encr rekey command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-f` \[`-r`\] `path`... | Generates a new file encryption key for the specified path and then encrypts the data with the new key.  If -r is specified, the rekey operation is performed recursively under `path`.  `path` specifies the absolute or relative path of a directory. Multiple path values are allowed. |
| `-v` | Generates a new volume encryption key (VEK) for the specified mount point and then encrypts all the file encryption keys in file system with the new key. Prompts for the wallet password because the wallet must be accessed to store the new VEK. |
| `-a` `algorithm` | Specifies the algorithm. Advanced Encryption Standard (AES) is the only encryption supported for this release. |
| `-k` `key_length` | Specifies the key length for the directory or file specified by `path`. |

This command cannot be run on security realm-protected files.

The default values for the `-a` and `-k` are determined by the volume parameters specified when `acfsutil` `encr` `set` was run.

The `path` option can specify a path to a file or directory in a read-write snapshot. If the `-r` option is specified with the command on the root directory, the command does not transverse the snapshots under the `.ACFS` directory. If a rekey operation is specified at the file system level, then the operation does not process files and directories of snapshots in the `.ACFS/snaps/` directory.

Only a user with root or system administrator privileges can run this command with the `-v` option. The file owner can also run this command with the `-f` option to rekey encryption on the directory or file.

You should back up the Oracle Cluster Registry (OCR) after running this command with the `-v` option to ensure there is an OCR backup that contains all of the volume encryption keys (VEKs) for the file system.

Examples

The following are examples of the use of `acfsutil` `encr` `rekey`.

Example 13-63 Using the acfsutil encr rekey command

```
# /sbin/acfsutil encr rekey -m /u01/app/acfsmounts/myacfs -v

# /sbin/acfsutil encr rekey -m /u01/app/acfsmounts/myacfs -f
                            -r /u01/app/acfsmounts/myacfs/myfiles
```

## acfsutil encr set

Purpose

Sets or changes encryption parameters for an Oracle ACFS file system.

Syntax and Description

  
`acfsutil` `encr` `set` `-h`  
`acfsutil` `encr` `set` \[`-a` { `AES` } `-k` { `128` | `192` | `256` } | `-u`\] `-m` `mount_point`  

`acfsutil` `encr` `set` `-h` displays help text and exits.

Table 13-72 contains the options available with the `acfsutil` `encr` `set` command.

Table 13-72 Options for the acfsutil encr set command

| Option | Description |
| --- | --- |
| `-a` `algorithm` | Specifies the algorithm. Advanced Encryption Standard (`AES`) is the default value and the only encryption supported for this release. The algorithm must be specified if `-k` is specified. |
| `-k` { `128` \| `192` \| `256` } | Specifies the key length. The key length is set at the volume level. The default is `192`. Must be specified if `-a` is specified. |
| `-u` | Backs out encryption. Decrypts all encrypted files in the file system and reverts the file system to the state before `acfsutil` `encr` `set` was run on the file system. If security is being used, then this command can only be run after security has been backed out. To remove security, refer to ["acfsutil sec prepare"](asmfs_util008.md). |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |

Before running the `acfsutil` `encr` `set` command, you must first run the `acfsutil` `encr` `init` command.

The `acfsutil` `encr` `set` command configures encryption parameters for a file system, transparently generates a volume encryption key, and stores that the generated key in the key store that was previously configured with the `acfsutil` `encr` `init` command.

In addition `acfsutil` `encr` `set` creates the `mount_point` `/.Security` `/encryption/logs/` directory that contains the log file (`encr-` `host_name``.log`) that collects auditing and diagnostic data.

Password requirements when storing the key are dependent on how the encryption key storage was configured. If `-p` was specified with `acfsutil` `encr` `init`, then a password is required to run this command.

The `acfsutil` `encr` `set` `–u` command is not allowed if any snapshots exist in the file system.

Only a user with root or system administrator privileges can run the `acfsutil` `encr` `set` command.

You should back up the Oracle Cluster Registry (OCR) after running this command to ensure there is an OCR backup that contains all of the volume encryption keys (VEKs) for the file system.

Examples

The following example shows the use of `acfsutil` `encr` `set` command.

Example 13-64 Using the acfsutil encr set command

```
# /sbin/acfsutil encr set -a AES -k 256 -m /u01/app/acfsmounts/myacfs
```