---
title: "5.5 MySQL Server Plugins"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/server-plugins.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

MySQL supports an plugin API that enables creation of server plugins. Plugins can be loaded at server startup, or loaded and unloaded at runtime without restarting the server. The plugins supported by this interface include, but are not limited to, storage engines, `INFORMATION_SCHEMA` tables, full-text parser plugins, partitioning support, and server extensions.

MySQL distributions include several plugins that implement server extensions:

- Plugins for authenticating attempts by clients to connect to MySQL Server. Plugins are available for several authentication protocols. See [Section 6.2.13, “Pluggable Authentication”](pluggable-authentication.md).
- A connection control plugin that enables administrators to introduce an increasing delay after a certain number of consecutive failed client connection attempts. See [Section 6.4.2, “Connection Control Plugins”](connection-control-plugin.md).
- A password-validation plugin implements password strength policies and assesses the strength of potential passwords. See [Section 6.4.3, “The Password Validation Plugin”](validate-password.md).
- Semisynchronous replication plugins implement an interface to replication capabilities that permit the source to proceed as long as at least one replica has responded to each transaction. See [Section 16.3.9, “Semisynchronous Replication”](replication-semisync.md).
- Group Replication enables you to create a highly available distributed MySQL service across a group of MySQL server instances, with data consistency, conflict detection and resolution, and group membership services all built-in. See [Chapter 17, *Group Replication*](group-replication.md).
- MySQL Enterprise Edition includes a thread pool plugin that manages connection threads to increase server performance by efficiently managing statement execution threads for large numbers of client connections. See [Section 5.5.3, “MySQL Enterprise Thread Pool”](thread-pool.md).
- MySQL Enterprise Edition includes an audit plugin for monitoring and logging of connection and query activity. See [Section 6.4.5, “MySQL Enterprise Audit”](audit-log.md).
- MySQL Enterprise Edition includes a firewall plugin that implements an application-level firewall to enable database administrators to permit or deny SQL statement execution based on matching against allowlists of accepted statement patterns. See [Section 6.4.6, “MySQL Enterprise Firewall”](firewall.md).
- A query rewrite plugin examines statements received by MySQL Server and possibly rewrites them before the server executes them. See [Section 5.5.4, “The Rewriter Query Rewrite Plugin”](rewriter-query-rewrite-plugin.md).
- Version Tokens enables creation of and synchronization around server tokens that applications can use to prevent accessing incorrect or out-of-date data. Version Tokens is based on a plugin library that implements a `version_tokens` plugin and a set of loadable functions. See [Section 5.5.5, “Version Tokens”](version-tokens.md).
- Keyring plugins provide secure storage for sensitive information. See [Section 6.4.4, “The MySQL Keyring”](keyring.md).
- X Plugin extends MySQL Server to be able to function as a document store. Running X Plugin enables MySQL Server to communicate with clients using the X Protocol, which is designed to expose the ACID compliant storage abilities of MySQL as a document store. See [Section 19.4, “X Plugin”](x-plugin.md).
- Test framework plugins test server services. For information about these plugins, see the Plugins for Testing Plugin Services section of the MySQL Server Doxygen documentation, available at [https://dev.mysql.com/doc/index-other.html](https://dev.mysql.com/doc/index-other.html).

The following sections describe how to install and uninstall plugins, and how to determine at runtime which plugins are installed and obtain information about them. For information about writing plugins, see [The MySQL Plugin API](https://dev.mysql.com/doc/extending-mysql/5.7/en/plugin-api.html).