---
title: "22.5.3 Using Encrypted Connections with X Plugin"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/x-plugin-encrypted-connections.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 22.5.3 Using Encrypted Connections with X Plugin

This section explains how to configure X Plugin to use encrypted connections. For more background information, see [Section 8.3, “Using Encrypted Connections”](encrypted-connections.md).

To enable configuring support for encrypted connections, X Plugin has ``mysqlx_ssl_*`xxx`*`` system variables, which can have different values from the ``ssl_*`xxx`*`` system variables used with MySQL Server. For example, X Plugin can have SSL key, certificate, and certificate authority files that differ from those used for MySQL Server. These variables are described at [Section 22.5.6.2, “X Plugin Options and System Variables”](x-plugin-options-system-variables.md). Similarly, X Plugin has its own ``Mysqlx_ssl_*`xxx`*`` status variables that correspond to the MySQL Server encrypted-connection ``Ssl_*`xxx`*`` status variables. See [Section 22.5.6.3, “X Plugin Status Variables”](x-plugin-status-variables.md).

At initialization, X Plugin determines its TLS context for encrypted connections as follows:

- If all ``mysqlx_ssl_*`xxx`*`` system variables have their default values, X Plugin uses the same TLS context as the MySQL Server main connection interface, which is determined by the values of the ``ssl_*`xxx`*`` system variables.
- If any ``mysqlx_ssl_*`xxx`*`` variable has a nondefault value, X Plugin uses the TLS context defined by the values of its own system variables. (This is the case if any ``mysqlx_ssl_*`xxx`*`` system variable is set to a value different from its default.)

This means that, on a server with X Plugin enabled, you can choose to have MySQL Protocol and X Protocol connections share the same encryption configuration by setting only the ``ssl_*`xxx`*`` variables, or have separate encryption configurations for MySQL Protocol and X Protocol connections by configuring the ``ssl_*`xxx`*`` and ``mysqlx_ssl_*`xxx`*`` variables separately.

To have MySQL Protocol and X Protocol connections use the same encryption configuration, set only the ``ssl_*`xxx`*`` system variables in `my.cnf`:

```
[mysqld]
ssl_ca=ca.pem
ssl_cert=server-cert.pem
ssl_key=server-key.pem
```

To configure encryption separately for MySQL Protocol and X Protocol connections, set both the ``ssl_*`xxx`*`` and ``mysqlx_ssl_*`xxx`*`` system variables in `my.cnf`:

```
[mysqld]
ssl_ca=ca1.pem
ssl_cert=server-cert1.pem
ssl_key=server-key1.pem

mysqlx_ssl_ca=ca2.pem
mysqlx_ssl_cert=server-cert2.pem
mysqlx_ssl_key=server-key2.pem
```

For general information about configuring connection-encryption support, see [Section 8.3.1, “Configuring MySQL to Use Encrypted Connections”](using-encrypted-connections.md). That discussion is written for MySQL Server, but the parameter names are similar for X Plugin. (The X Plugin ``mysqlx_ssl_*`xxx`*`` system variable names correspond to the MySQL Server ``ssl_*`xxx`*`` system variable names.)

The [`tls_version`](server-system-variables.md) system variable that determines the permitted TLS versions for MySQL Protocol connections also applies to X Protocol connections. The permitted TLS versions for both types of connections are therefore the same.

Encryption per connection is optional, but a specific user can be required to use encryption for X Protocol and MySQL Protocol connections by including an appropriate `REQUIRE` clause in the [`CREATE USER`](create-user.md) statement that creates the user. For details, see [Section 15.7.1.3, “CREATE USER Statement”](create-user.md). Alternatively, to require all users to use encryption for X Protocol and MySQL Protocol connections, enable the [`require_secure_transport`](server-system-variables.md) system variable. For additional information, see [Configuring Encrypted Connections as Mandatory](using-encrypted-connections.md).