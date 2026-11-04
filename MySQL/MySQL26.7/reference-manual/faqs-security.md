---
title: "MySQL :: MySQL 26.7 Reference Manual :: A.9 MySQL 26.7 FAQ: Security"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/faqs-security.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## A.9 MySQL 26.7 FAQ: Security

A.9.1. Where can I find documentation that addresses security issues for MySQL?

A.9.2. What is the default authentication plugin in MySQL 26.7?

A.9.3. Does MySQL have native support for SSL?

A.9.4. Is SSL support built into MySQL binaries, or must I recompile the binary myself to enable it?

A.9.5. Does MySQL have built-in authentication against LDAP directories?

A.9.6. Does MySQL include support for Roles Based Access Control (RBAC)?

A.9.7. Does MySQL support TLS 1.0 and 1.1?

| **A.9.1.** | Where can I find documentation that addresses security issues for MySQL? |
| --- | --- |
|  | The best place to start is [Chapter 8, *Security*](security.md).  Other portions of the MySQL Documentation which you may find useful with regard to specific security concerns include the following:  - [Section 8.1.1, “Security Guidelines”](security-guidelines.md). - [Section 8.1.3, “Making MySQL Secure Against Attackers”](security-against-attack.md). - [Section B.3.3.2, “How to Reset the Root Password”](resetting-permissions.md). - [Section 8.1.5, “How to Run MySQL as a Normal User”](changing-mysql-user.md). - [Section 8.1.4, “Security-Related mysqld Options and Variables”](security-options.md). - [Section 8.1.6, “Security Considerations for LOAD DATA LOCAL”](load-data-local-security.md). - [Section 2.9, “Postinstallation Setup and Testing”](postinstallation.md). - [Section 8.3, “Using Encrypted Connections”](encrypted-connections.md). - [Loadable Function Security Precautions](https://dev.mysql.com/doc/extending-mysql/26.7/en/adding-loadable-function.html#loadable-function-security).  There is also the [Secure Deployment Guide](https://dev.mysql.com/doc/mysql-secure-deployment-guide/8.0/en/), which provides procedures for deploying a generic binary distribution of MySQL Enterprise Edition Server with features for managing the security of your MySQL installation. |
| **A.9.2.** | What is the default authentication plugin in MySQL 26.7? |
|  | The default authentication plugin as of MySQL 8.0 is `caching_sha2_password`. For information about this plugin, see [Section 8.4.1.1, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).  The `caching_sha2_password` plugin provides more secure password encryption than the deprecated `mysql_native_password` plugin (the default plugin in MySQL versions before MySQL 8.0).  For general information about pluggable authentication and other available authentication plugins, see [Section 8.2.17, “Pluggable Authentication”](pluggable-authentication.md), and [Section 8.4.1, “Authentication Plugins”](authentication-plugins.md). |
| **A.9.3.** | Does MySQL have native support for SSL? |
|  | Yes, the binaries have support for SSL connections between the client and server. See [Section 8.3, “Using Encrypted Connections”](encrypted-connections.md).  You can also tunnel a connection using SSH, if (for example) the client application does not support SSL connections. For an example, see [Section 8.3.4, “Connecting to MySQL Remotely from Windows with SSH”](windows-and-ssh.md). |
| **A.9.4.** | Is SSL support built into MySQL binaries, or must I recompile the binary myself to enable it? |
|  | Yes, the binaries have SSL enabled for client/server connections that are secured, authenticated, or both. See [Section 8.3, “Using Encrypted Connections”](encrypted-connections.md). |
| **A.9.5.** | Does MySQL have built-in authentication against LDAP directories? |
|  | The Enterprise edition includes a [PAM Authentication Plugin](pam-pluggable-authentication.md) that supports authentication against an LDAP directory. |
| **A.9.6.** | Does MySQL include support for Roles Based Access Control (RBAC)? |
|  | Not at this time. |
| **A.9.7.** | Does MySQL support TLS 1.0 and 1.1? |
|  | Support for the TLSv1 and TLSv1.1 connection protocols is removed as of MySQL 8.0.28. The protocols were deprecated from MySQL 8.0.26. For the consequences of that removal, see [Removal of Support for the TLSv1 and TLSv1.1 Protocols](https://dev.mysql.com/doc/refman/8.4/en/encrypted-connection-protocols-ciphers.html#encrypted-connection-deprecated-protocols).  Support for TLS versions 1.0 and 1.1 is removed because those protocol versions are old, released in 1996 and 2006, respectively. The algorithms used are weak and outdated.  Unless you are using very old versions of MySQL Server or connectors, you are unlikely to have connections using TLS 1.0 or 1.1. MySQL connectors and clients select the highest TLS version available by default.  *When was support for TLS 1.2 added to MySQL Server?* MySQL Community Server added TLS 1.2 support when the community server switched to OpenSSL for MySQL 5.6, 5.7, and 8.0 in 2019. For MySQL Enterprise Edition, OpenSSL added TLS 1.2 support in 2015, in MySQL Server 5.7.10.  *How can one view which TLS versions are in active use?* For MySQL 5.7 or 8.0, review whether TLS 1.0 or 1.1 is in use by running this query:  ```sql SELECT   \`session_ssl_status\`.\`thread_id\`, \`session_ssl_status\`.\`ssl_version\`,   \`session_ssl_status\`.\`ssl_cipher\`, \`session_ssl_status\`.\`ssl_sessions_reused\` FROM \`sys\`.\`session_ssl_status\`  WHERE ssl_version NOT IN ('TLSv1.3','TLSv1.2'); ```  If a thread using TLSv1.0 or TLSv1.1 is listed, you can determine where this connection is coming from by running this query:  ```sql SELECT thd_id,conn_id, user, db, current_statement, program_name  FROM sys.processlist WHERE thd_id IN (                   SELECT \`session_ssl_status\`.\`thread_id\`                   FROM \`sys\`.\`session_ssl_status\`                    WHERE ssl_version NOT IN ('TLSv1.3','TLSv1.2')                 ); ```  Alternatively, you can run this query:  ```sql SELECT *  FROM sys.session  WHERE thd_id IN (                   SELECT \`session_ssl_status\`.\`thread_id\`                   FROM \`sys\`.\`session_ssl_status\`                    WHERE ssl_version NOT IN ('TLSv1.3','TLSv1.2')                 ); ```  These queries provide details needed to determine which application is not supporting TLS 1.2 or 1.3, and target upgrades for those.  *Are there other options for testing for TLS 1.0 or 1.1?* Yes, you can disable those versions prior to upgrading your server to a newer version. Explicitly specify which version to use, either in `mysql.cnf` (or `mysql.ini`) or by using [`SET         PERSIST`](set-variable.md), for example: [`--tls-version=TLSv12`](server-system-variables.md).  *Do all MySQL Connectors (5.7 and 8.0) support TLS 1.2 and higher? What about C and C++ applications using `libmysql`?* For C and C++ applications using the community `libmysqlclient` library, use an OpenSSL-based library (that is, do *not* use YaSSL). Usage of OpenSSL was unified in 2018 (in MySQL 8.0.4 and 5.7.28, respectively). The same applies for Connector/ODBC and Connector/C++. To determine what library dependencies are used, run the following commands to see if OpenSSL is listed. On Linux, use this command:  ```svg $> sudo ldd usr/local/mysql/lib/libmysqlclient.a \| grep -i openssl ```  On MacOS, use this command:  ```svg $> sudo otool -l /usr/local/mysql/lib/libmysqlclient.a \| grep -i openssl ```  Check the documentation for each connector, but they do support TLS 1.2 and TLS 1.3. |