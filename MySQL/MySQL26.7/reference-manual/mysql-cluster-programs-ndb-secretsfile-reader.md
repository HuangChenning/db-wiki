---
title: "MySQL :: MySQL 26.7 Reference Manual :: 25.5.24 ndb_secretsfile_reader — Obtain Key Information from an Encrypted NDB\n        Data File"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/mysql-cluster-programs-ndb-secretsfile-reader.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 25.5.24 ndb\_secretsfile\_reader — Obtain Key Information from an Encrypted NDB Data File

**ndb\_secretsfile\_reader** gets the encryption key from an `NDB` encryption secrets file, given the password.

#### Usage

```svg
ndb_secretsfile_reader options file
```

The *`options`* must include one of `--filesystem-password` or `--filesystem-password-from-stdin`, and the encryption password must be supplied, as shown here:

```svg
> ndb_secretsfile_reader --filesystem-password=54kl14 ndb_5_fs/D1/NDBCNTR/S0.sysfile
ndb_secretsfile_reader: [Warning] Using a password on the command line interface can be insecure.
cac256e18b2ddf6b5ef82d99a72f18e864b78453cc7fa40bfaf0c40b91122d18
```

These and other options that can be used with **ndb\_secretsfile\_reader** are shown in the following table. Additional descriptions follow the table.

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
	Also read groups with concat(group, suffix).
- `--filesystem-password`
	| Command-Line Format | `--filesystem-password=password` |
	| --- | --- |
	Pass the filesystem encryption and decryption password to **ndb\_secretsfile\_reader** using `stdin`, `tty`, or the `my.cnf` file.
- `--filesystem-password-from-stdin`
	| Command-Line Format | `--filesystem-password-from-stdin={TRUE\|FALSE}` |
	| --- | --- |
	Pass the filesystem encryption and decryption password to **ndb\_secretsfile\_reader** from `stdin` (only).
- `--help`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display help text and exit.
- `--login-path`
	| Command-Line Format | `--login-path=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given path from login file.
- `--no-login-paths`
	| Command-Line Format | `--no-login-paths` |
	| --- | --- |
	Skips reading options from the login path file.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than login file.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
- `--usage`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Display help text and exit; same as --help.
- `--version`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.