---
title: "4.2.1 OS User for Running mysqlbackup"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/mysqlbackup-os-user.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

### 4.2.1 OS User for Running mysqlbackup

*For Linux and other Unix-like platforms:* **mysqlbackup** does not record file ownership or permissions of the files that are backed up. To ensure no file permission issues prevent a server to be backed up, restored, and restarted successfully, *it is highly recommended that you run mysqlbackup with the same OS user who runs the MySQL server (typically `mysql`)*.

For Linux and other Unix-like platforms, the `mysql` user was typically created using the `-r` and `-s /bin/false` options of the `useradd` command, so that it does not have login permissions to your server host (see [Creating the mysql User and Group](https://dev.mysql.com/doc/mysql-secure-deployment-guide/8.0/en/secure-deployment-install.html#secure-deployment-mysql-user) for details). To switch to the `mysql` user on your OS, use the `--shell=/bin/bash` option for the `su` command:

```
su - mysql --shell=/bin/bash
```

If it is not possible run **mysqlbackup** with the OS user `mysql`, pay attention to the following guidelines:

- For backups, **mysqlbackup** should be run by a user that can read all the server files and directories and can execute all server directories. To satisfy that requirement, the OS user that runs **mysqlbackup** should, for example, have the group owner of the server files and directories (typically `mysql`) as its primary group or secondary group.
- For restores, unless **mysqlbackup** is run by the same user that runs the server, it can be very hard to ensure that the server has access to all the restored server files and folders, especially in the case of an online restore, where the server must be able to access the files immediately after they are restored. For an offline restore, you might need to, for example, set a `umask` to the user before the restore and adjust the permissions of the restored files and folders using a series of `chmod` and `chown` commands, so that the original permissions for the backed-up files and folders are reproduced.