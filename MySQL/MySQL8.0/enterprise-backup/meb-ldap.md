---
title: "Chapter 16 Using LDAP for Server Authentication"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/meb-ldap.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

*For MySQL Enterprise Backup 8.0.22 and later:* [LDAP pluggable authentication](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/ldap-pluggable-authentication.html) is a feature supported by the MySQL Enterprise Edition; the user by which **mysqlbackup** connects to the server can be authenticated using LDAP. Beyond proper setup for LDAP on the server side, the following requirements apply for LDAP authentication to work with **mysqlbackup**:

- If the user is using simple LDAP authentication, the password is communicated to the server in cleartext; enable [Client-Side Cleartext Pluggable Authentication](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/cleartext-pluggable-authentication.html) by using the [`--enable-cleartext-plugin`](standard-options.md) option in your **mysqlbackup** command, or set the environment variable `LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN=[1|Y|y]` in the environment you run the command.
- If the user is using SASL-based LDAP authentication and the client-side plugin (`authentication_ldap_sasl_client`) is not located in the server's plugin folder, the [`--plugin-dir`](standard-options.md) option should be used with the **mysqlbackup** command to specify the location of the plugin, or the same information should be provided by setting the environment variable `LIBMYSQL_PLUGIN_DIR` in the environment you run the command.

The following are some sample commands for using LDAP authentication:

**Example 16.1 Backup Using Simple LDAP Authentication**

```
mysqlbackup --user=mysqlbackup --password=password --host=127.0.0.1 \
  --backup-dir=/home/mysqlbackup/backup-tmp  --backup-image=/home/mysqlbackup/backups/my.mbi \
  --enable-cleartext-plugin backup-to-image
```

**Example 16.2 TTS Restore Using Simple LDAP Authentication**

```
mysqlbackup --user=mysqlbackup --password=password  --host=127.0.0.1 \
  --backup-dir=/home/mysqlbackup/backup-tmp  --backup-image=/home/mysqlbackup/backups/my.mbi \
  --include-tables=REGEX --enable-cleartext-plugin copy-back-and-apply-log
```

**Example 16.3 Backup Using SALS-based LDAP Authentication**

```
mysqlbackup --user=mysqlbackup --password=password --host=127.0.0.1 \
  --backup-dir=/home/mysqlbackup/backup-tmp  --backup-image=/home/mysqlbackup/backups/my.mbi \
  --plugin-dir=SASL_plugin-dir backup-to-image
```

**Example 16.4 TTS Restore Using SALS-based Authentication**

```
mysqlbackup --user=mysqlbackup --password=password  --host=127.0.0.1 \
  --backup-dir=/home/mysqlbackup/backup-tmp  --backup-image=/home/mysqlbackup/backups/my.mbi \
   --include-tables=REGEX --plugin-dir=SASL_plugin-dir copy-back-and-apply-log
```