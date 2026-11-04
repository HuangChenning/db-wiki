---
title: "25.5.31 ndbxfrm — Compress, Decompress, Encrypt, and Decrypt Files Created by NDB Cluster"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster-programs-ndbxfrm.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 25.5.31 ndbxfrm — Compress, Decompress, Encrypt, and Decrypt Files Created by NDB Cluster

The **ndbxfrm** utility, introduced in NDB 8.0.22, can be used to decompress, decrypt, and output information about files created by NDB Cluster that are compressed, encrypted, or both. It can also be used to compress or encrypt files.

**Table 25.52 Command-line options used with the program ndbxfrm**

| Format | Description | Added, Deprecated, or Removed |
| --- | --- | --- |
| `--compress`,  `                  -c                  ` | Compress file | ADDED: NDB 8.0.22 |
| `                  --decrypt-key=key                  ` | Supply file decryption key | ADDED: NDB 8.0.31 |
| `                  --decrypt-key-from-stdin                  ` | Supply file decryption key from stdin | ADDED: NDB 8.0.31 |
| `                  --decrypt-password=password                  ` | Use this password to decrypt file | ADDED: NDB 8.0.22 |
| `                  --decrypt-password-from-stdin                  ` | Get decryption password in a secure fashion from STDIN | ADDED: NDB 8.0.24 |
| `                  --defaults-extra-file=path                  ` | Read given file after global files are read | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-group-suffix=string                  ` | Also read groups with concat(group, suffix) | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-file=path                  ` | Read default options from given file only | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --encrypt-block-size=#                  ` | Print info about file including file header and trailer | ADDED: NDB 8.0.31 |
| `                  --encrypt-block-size=#                  ` | Size of input data chunks encrypted as a unit. Used with XTS, set to zero for CBC mode | ADDED: NDB 8.0.29 |
| `                  --encrypt-cipher=#                  ` | Encryption cipher: 1 for CBC, 2 for XTS | ADDED: NDB 8.0.29 |
| `--encrypt-kdf-iter-count=#`,  `                  -k                 #  ` | Number of iterations used in key definition | ADDED: NDB 8.0.22 |
| `                  --encrypt-key=key                  ` | Use this key to encrypt file | ADDED: NDB 8.0.31 |
| `                  --encrypt-key-from-stdin                  ` | Use key supplied from stdin to encrypt file | ADDED: NDB 8.0.31 |
| `                  --encrypt-password=password                  ` | Use this password to encrypt file | ADDED: NDB 8.0.22 |
| `                  --encrypt-password-from-stdin                  ` | Get encryption password in a secure fashion from STDIN | ADDED: NDB 8.0.24 |
| `--help`,  `  -?                  ` | Print usage information | ADDED: NDB 8.0.22 |
| `--info`,  `  -i                  ` | Print file information | ADDED: NDB 8.0.22 |
| `                  --login-path=path                  ` | Read given path from login file | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --no-defaults                  ` | Do not read default options from any option file other than login file | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --print-defaults                  ` | Print program argument list and exit | (Supported in all NDB releases based on MySQL 8.0) |
| `--usage`,  `  -?                  ` | Prints usage information; synonym for --help | ADDED: NDB 8.0.22 |
| `--version`,  `                  -V                  ` | Output version information | ADDED: NDB 8.0.22 |

#### Usage

```
ndbxfrm --info file[ file ...]

ndbxfrm --compress input_file output_file

ndbxfrm --decrypt-password=password input_file output_file

ndbxfrm [--encrypt-ldf-iter-count=#] --encrypt-password=password input_file output_file
```

*`input_file`* and *`output_file`* cannot be the same file.

#### Options

- `--compress`, `-c`
	| Command-Line Format | `--compress` |
	| --- | --- |
	Compresses the input file, using the same compression method as is used for compressing NDB Cluster backups, and writes the output to an output file. To decompress a compressed `NDB` backup file that is not encrypted, it is necessary only to invoke **ndbxfrm** using the names of the compressed file and an output file (with no options required).
- ``--decrypt-key=*`key`*``, `-K` *`key`*
	| Command-Line Format | `--decrypt-key=key` |
	| --- | --- |
	Decrypts a file encrypted by `NDB` using the supplied key.
	Note
	This option cannot be used together with `--decrypt-password`.
- `--decrypt-key-from-stdin`
	| Command-Line Format | `--decrypt-key-from-stdin` |
	| --- | --- |
	Decrypts a file encrypted by `NDB` using the key supplied from `stdin`.
- ``--decrypt-password=*`password`*``
	| Command-Line Format | `--decrypt-password=password` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Decrypts a file encrypted by `NDB` using the password supplied.
	Note
	This option cannot be used together with `--decrypt-key`.
- [`--decrypt-password-from-stdin[=TRUE|FALSE]`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-cluster-programs-ndbxfrm.html#option_ndbxfrm_decrypt-password-from-stdin)
	| Command-Line Format | `--decrypt-password-from-stdin` |
	| --- | --- |
	Decrypts a file encrypted by `NDB`, using a password supplied from standard input. This is similar to entering a password after invoking [**mysql**](mysql.md) [`--password`](mysql-command-options.md) with no password following the option.
- `--defaults-extra-file`
	| Command-Line Format | `--defaults-extra-file=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given file after global files are read.
- `--defaults-file`
	| Command-Line Format | `--defaults-file=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read default options from given file only.
- `--defaults-group-suffix`
	| Command-Line Format | `--defaults-group-suffix=string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Also read groups with ``CONCAT(*`group`*,             *`suffix`*)``.
- `--detailed-info`
	| Command-Line Format | `--encrypt-block-size=#` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Print out file information like `--info`, but include the file's header and trailer.
	Example:
	```
	$> ndbxfrm --detailed-info S0.sysfile
	File=/var/lib/cluster-data/ndb_7_fs/D1/NDBCNTR/S0.sysfile, compression=no, encryption=yes
	header: {
	  fixed_header: {
	    magic: {
	      magic: { 78, 68, 66, 88, 70, 82, 77, 49 },
	      endian: 18364758544493064720,
	      header_size: 32768,
	      fixed_header_size: 160,
	      zeros: { 0, 0 }
	    },
	    flags: 73728,
	    flag_extended: 0,
	    flag_zeros: 0,
	    flag_file_checksum: 0,
	    flag_data_checksum: 0,
	    flag_compress: 0,
	    flag_compress_method: 0,
	    flag_compress_padding: 0,
	    flag_encrypt: 18,
	    flag_encrypt_cipher: 2,
	    flag_encrypt_krm: 1,
	    flag_encrypt_padding: 0,
	    flag_encrypt_key_selection_mode: 0,
	    dbg_writer_ndb_version: 524320,
	    octets_size: 32,
	    file_block_size: 32768,
	    trailer_max_size: 80,
	    file_checksum: { 0, 0, 0, 0 },
	    data_checksum: { 0, 0, 0, 0 },
	    zeros01: { 0 },
	    compress_dbg_writer_header_version: { ... },
	    compress_dbg_writer_library_version: { ... },
	    encrypt_dbg_writer_header_version: { ... },
	    encrypt_dbg_writer_library_version: { ... },
	    encrypt_key_definition_iterator_count: 100000,
	    encrypt_krm_keying_material_size: 32,
	    encrypt_krm_keying_material_count: 1,
	    encrypt_key_data_unit_size: 32768,
	    encrypt_krm_keying_material_position_in_octets: 0,
	  },
	  octets: {
	     102, 68, 56, 125, 78, 217, 110, 94, 145, 121, 203, 234, 26, 164, 137, 180,
	     100, 224, 7, 88, 173, 123, 209, 110, 185, 227, 85, 174, 109, 123, 96, 156,
	  }
	}
	trailer: {
	  fixed_trailer: {
	    flags: 48,
	    flag_extended: 0,
	    flag_zeros: 0,
	    flag_file_checksum: 0,
	    flag_data_checksum: 3,
	    data_size: 512,
	    file_checksum: { 0, 0, 0, 0 },
	    data_checksum: { 226, 223, 102, 207 },
	    magic: {
	      zeros: { 0, 0 }
	      fixed_trailer_size: 56,
	      trailer_size: 32256,
	      endian: 18364758544493064720,
	      magic: { 78, 68, 66, 88, 70, 82, 77, 49 },
	    },
	  }
	}
	```
- ``--encrypt-block-size=*`#`*``
	| Command-Line Format | `--encrypt-block-size=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `2147483647` |
	Size of input data chunks that are encrypted as a unit. Used with XTS; set to `0` (the default) for CBC mode.
- ``--encrypt-cipher=*`#`*``
	| Command-Line Format | `--encrypt-cipher=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `1` |
	| Minimum Value | `0` |
	| Maximum Value | `2147483647` |
	Cipher used for encryption. Set to `1` for CBC mode (the default), or `2` for XTS.
- ``--encrypt-kdf-iter-count=*`#`*``, ``-k *`#`*``
	| Command-Line Format | `--encrypt-kdf-iter-count=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `2147483647` |
	When encrypting a file, specifies the number of iterations to use for the encryption key. Requires the `--encrypt-password` option.
- ``--encrypt-key=*`key`*``
	| Command-Line Format | `--encrypt-key=key` |
	| --- | --- |
	Encrypts a file using the supplied key.
	Note
	This option cannot be used together with `--encrypt-password`.
- `--encrypt-key-from-stdin`
	| Command-Line Format | `--encrypt-key-from-stdin` |
	| --- | --- |
	Encrypt a file using the key supplied from `stdin`.
- ``--encrypt-password=*`password`*``
	| Command-Line Format | `--encrypt-password=password` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Encrypts the backup file using the password supplied by the option. The password must meet the requirements listed here:
	- Uses any of the printable ASCII characters except `!`, `'`, `"`, `$`, `%`, `\`, `` ` ``, and `^`
	- Is no more than 256 characters in length
	- Is enclosed by single or double quotation marks
	Note
	This option cannot be used together with `--encrypt-key`.
- [`--encrypt-password-from-stdin[=TRUE|FALSE]`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-cluster-programs-ndbxfrm.html#option_ndbxfrm_encrypt-password-from-stdin)
	| Command-Line Format | `--encrypt-password-from-stdin` |
	| --- | --- |
	Encrypts a file using a password supplied from standard input. This is similar to entering a password is entered after invoking [**mysql**](mysql.md) [`--password`](mysql-command-options.md) with no password following the option.
- `--help`, `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	Prints usage information for the program.
- `--info`, `-i`
	| Command-Line Format | `--info` |
	| --- | --- |
	Prints the following information about one or more input files:
	- The name of the file
	- Whether the file is compressed (`compression=yes` or `compression=no`)
	- Whether the file is encrypted (`encryption=yes` or `encryption=no`)
	Example:
	```
	$> ndbxfrm -i BACKUP-10-0.5.Data BACKUP-10.5.ctl BACKUP-10.5.log
	File=BACKUP-10-0.5.Data, compression=no, encryption=yes
	File=BACKUP-10.5.ctl, compression=no, encryption=yes
	File=BACKUP-10.5.log, compression=no, encryption=yes
	```
	Beginning with NDB 8.0.31, you can also see the file's header and trailer using the `--detailed-info` option.
- `--login-path`
	| Command-Line Format | `--login-path=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given path from login file.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than login file.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
- `--usage`, `-?`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Synonym for `--help`.
- `--version`, `-V`
	| Command-Line Format | `--version` |
	| --- | --- |
	Prints out version information.

**ndbxfrm** can encrypt backups created by any version of NDB Cluster. The `.Data`, `.ctl`, and `.log` files comprising the backup must be encrypted separately, and these files must be encrypted separately for each data node. Once encrypted, such backups can be decrypted only by **ndbxfrm**, [**ndb\_restore**](mysql-cluster-programs-ndb-restore.md), or **ndb\_print\_backup** from NDB Cluster 8.0.22 or later.

An encrypted file can be re-encrypted with a new password using the `--encrypt-password` and `--decrypt-password` options together, like this:

```
ndbxfrm --decrypt-password=old --encrypt-password=new input_file output_file
```

In the example just shown, *`old`* and *`new`* are the old and new passwords, respectively; both of these must be quoted. The input file is decrypted and then encrypted as the output file. The input file itself is not changed; if you do not want it to be accessible using the old password, you must remove the input file manually.