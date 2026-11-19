---
title: "创建用户"
book: "部署集中式版"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577362.html"
tags:
  - oceanbase
  - standalone
  - deploy
---

# 创建用户

部署 OceanBase 集中式数据库推荐使用 admin 用户，也可以使用其他用户(不推荐 root 用户)。但是要求用户具备 sudo 权限和作为数据库相关目录的所有者。本文介绍如何创建普通用户并为普通用户设置 sudo 权限。

1.  执行以下命令，创建用户组 admin 以及创建用户 admin。

    ```
    [root@test001 ~]# useradd -U admin -d /home/admin -s /bin/bash
    [root@test001 ~]# chown -R admin:admin /home/admin
    ```

2.  执行以下命令，为账户 admin 设置密码。

    ```
    [root@test001 ~]# passwd admin
    ```

3.  为账户 admin 设置 sudo 权限。

    执行以下命令，打开 `/etc/sudoers` 文件：

    ```
    [root@test001 ~]# vim /etc/sudoers
    ```

    在 `/etc/sudoers` 文件末尾添加如下内容：

    ```
    ## Same thing without a password
    # %wheel        ALL=(ALL)       NOPASSWD: ALL
    admin       ALL=(ALL)       NOPASSWD: ALL
    ```
