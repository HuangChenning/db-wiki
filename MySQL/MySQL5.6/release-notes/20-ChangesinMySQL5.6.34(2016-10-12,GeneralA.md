---
title: "Changes in MySQL 5.6.34 (2016-10-12, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=31"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Packaging Notes
- Security Notes

> Packaging Notes

- RPM and Debian packages now create the `/var/lib/mysql-files` directory, which is now the

default value of the `secure_file_priv` system variable that specifies a directory for import and export operations. (Bug #24709892, Bug #24761774)

> Security Notes

- Incompatible Change: The `secure_file_priv` system variable is used to limit the effect of data

import and export operations. The following changes have been made to how the server handles this variable:

- `secure_file_priv` can be set to `NULL` to disable all import and export operations.
- The server checks the value of `secure_file_priv` at startup and writes a warning to the error log

if the value is insecure. A non-`NULL` value is considered insecure if it is empty, or the value is the data directory or a subdirectory of it, or a directory that is accessible by all users. If `secure_file_priv` is set to a nonexistent path, the server writes an error message to the error log and exits.

- Previously, the `secure_file_priv` system variable was empty by default. Now the default value is

platform specific and depends on the value of the `INSTALL_LAYOUT` `CMake` option, as shown in the following table.

> `INSTALL_LAYOUT` Value Default `secure_file_priv` Value

```
STANDALONE, WIN  NULL
DEB, RPM, SLES, SVR4  /var/lib/mysql-files
```

Otherwise `mysql-files` under the

```
CMAKE_INSTALL_PREFIX value
```

- To specify the default `secure_file_priv` value explicitly if you are building from source, use the

new `INSTALL_SECURE_FILE_PRIVDIR` `CMake` option. To specify a directory for the embedded server, set the new `INSTALL_SECURE_FILE_PRIV_EMBEDDEDDIR` option. Its default value is `NULL`.

(Bug #24679907, Bug #24695274, Bug #24707666, WL #6782)

- The linked OpenSSL library for the MySQL Commercial Server has been updated to version 1.0.1u. For

a description of issues fixed in this version, see http://www.openssl.org/news/vulnerabilities.html.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead. (Bug #24753389)

- yaSSL was upgraded to version 2.4.2. This upgrade corrects issues with: Potential AES side channel

leaks; DSA padding for unusual sizes; the `SSL_CTX_load_verify_locations()` OpenSSL compatibility function failing to handle long path directory names. (Bug #24512715, Bug #24740291)
