---
title: "17.6.2 Group Replication Secure Socket Layer (SSL) Support"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/group-replication-secure-socket-layer-support-ssl.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 17.6.2 Group Replication Secure Socket Layer (SSL) Support

Group communication connections as well as recovery connections, are secured using SSL. The following sections explain how to configure connections.

#### Configuring SSL for Group Replication Recovery

Recovery is performed through a regular asynchronous replication connection. Once the donor is selected, the server joining the group establishes an asynchronous replication connection. This is all automatic.

However, a user that requires an SSL connection must have been created before the server joining the group connects to the donor. Typically, this is set up at the time one is provisioning a server to join the group.

```
donor> SET SQL_LOG_BIN=0;
donor> CREATE USER 'rec_ssl_user'@'%' REQUIRE SSL;
donor> GRANT replication slave ON *.* TO 'rec_ssl_user'@'%';
donor> SET SQL_LOG_BIN=1;
```

Assuming that all servers already in the group have a replication user set up to use SSL, you configure the server joining the group to use those credentials when connecting to the donor. That is done according to the values of the SSL options provided for the Group Replication plugin.

```
new_member> SET GLOBAL group_replication_recovery_use_ssl=1;
new_member> SET GLOBAL group_replication_recovery_ssl_ca= '.../cacert.pem';
new_member> SET GLOBAL group_replication_recovery_ssl_cert= '.../client-cert.pem';
new_member> SET GLOBAL group_replication_recovery_ssl_key= '.../client-key.pem';
```

And by configuring the recovery channel to use the credentials of the user that requires an SSL connection.

```
new_member> CHANGE MASTER TO MASTER_USER="rec_ssl_user" FOR CHANNEL "group_replication_recovery";
new_member> START GROUP_REPLICATION;
```

#### Configuring SSL for Group Communication

Secure sockets can be used to establish communication between members in a group. The configuration for this depends on the server's SSL configuration. As such, if the server has SSL configured, the Group Replication plugin also has SSL configured. For more information on the options for configuring the server SSL, see [Command Options for Encrypted Connections](connection-options.md). The options which configure Group Replication are shown in the following table.

**Table 17.2 SSL Options**

| Server Configuration | Plugin Configuration Description |
| --- | --- |
| ssl\_key | Path of key file. To be used as client and server certificate. |
| ssl\_cert | Path of certificate file. To be used as client and server certificate. |
| ssl\_ca | Path of file with SSL Certificate Authorities that are trusted. |
| ssl\_capath | Path of directory containing certificates for SSL Certificate Authorities that are trusted. |
| ssl\_crl | Path of file containing the certificate revocation lists. |
| ssl\_crlpath | Path of directory containing revoked certificate lists. |
| ssl\_cipher | Permitted ciphers to use while encrypting data over the connection. |
| tls\_version | Secure communication uses this version and its protocols. |

These options are MySQL Server configuration options which Group Replication relies on for its configuration. In addition there is the following Group Replication specific option to configure SSL on the plugin itself.

- [`group_replication_ssl_mode`](group-replication-system-variables.md) - specifies the security state of the connection between Group Replication members.

**Table 17.3 group\_replication\_ssl\_mode configuration values**

| Value | Description |
| --- | --- |
| *DISABLED* | Establish an unencrypted connection (*default*). |
| REQUIRED | Establish a secure connection if the server supports secure connections. |
| VERIFY\_CA | Like REQUIRED, but additionally verify the server TLS certificate against the configured Certificate Authority (CA) certificates. |
| VERIFY\_IDENTITY | Like VERIFY\_CA, but additionally verify that the server certificate matches the host to which the connection is attempted. |

The following example shows an example my.cnf file section used to configure SSL on a server and how activate it for Group Replication.

```
[mysqld]
ssl_ca = "cacert.pem"
ssl_capath = "/.../ca_directory"
ssl_cert = "server-cert.pem"
ssl_cipher = "DHE-RSA-AEs256-SHA"
ssl_crl = "crl-server-revoked.crl"
ssl_crlpath = "/.../crl_directory"
ssl_key = "server-key.pem"
group_replication_ssl_mode= REQUIRED
```

The only plugin specific configuration option that is listed is [`group_replication_ssl_mode`](group-replication-system-variables.md). This option activates the SSL communication between members of the group, by configuring the SSL framework with the `ssl_*` parameters that are provided to the server.