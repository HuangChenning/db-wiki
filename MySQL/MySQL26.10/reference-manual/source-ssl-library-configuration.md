---
title: "MySQL :: MySQL 26.10 Reference Manual :: 2.8.6 Configuring SSL Library Support"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/source-ssl-library-configuration.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 2.8.6 Configuring SSL Library Support

An SSL library is required for support of encrypted connections, entropy for random number generation, and other encryption-related operations.

If you compile MySQL from a source distribution, **CMake** configures the distribution to use the installed OpenSSL library by default.

To compile using OpenSSL, use this procedure:

1. Ensure that OpenSSL 1.0.1 or newer is installed on your system. If the installed OpenSSL version is older than 1.0.1, **CMake** produces an error at MySQL configuration time. If it is necessary to obtain OpenSSL, visit [http://www.openssl.org](http://www.openssl.org/).
2. The [`WITH_SSL`](source-configuration-options.md) **CMake** option determines which SSL library to use for compiling MySQL (see [Section 2.8.7, “MySQL Source-Configuration Options”](source-configuration-options.md)). The default is [`-DWITH_SSL=system`](source-configuration-options.md), which uses OpenSSL. To make this explicit, specify that option. For example:
	```svg
	cmake . -DWITH_SSL=system
	```
	That command configures the distribution to use the installed OpenSSL library. Alternatively, to explicitly specify the path name to the OpenSSL installation, use the following syntax. This can be useful if you have multiple versions of OpenSSL installed, to prevent **CMake** from choosing the wrong one:
	```svg
	cmake . -DWITH_SSL=path_name
	```
	Alternative OpenSSL system packages are supported by using `WITH_SSL=openssl3` on EL8. Authentication plugins, such as LDAP and Kerberos, are disabled since they do not support these alternative versions of OpenSSL.
3. Compile and install the distribution.

To check whether a [**mysqld**](mysqld.md) server supports encrypted connections, examine the value of the [`tls_version`](server-system-variables.md) system variable:

```sql
mysql> SHOW VARIABLES LIKE 'tls_version';
+---------------+-----------------+
| Variable_name | Value           |
+---------------+-----------------+
| tls_version   | TLSv1.2,TLSv1.3 |
+---------------+-----------------+
```

If the value contains TLS versions then the server supports encrypted connections, otherwise it does not.

For additional information, see [Section 8.3.1, “Configuring MySQL to Use Encrypted Connections”](using-encrypted-connections.md).