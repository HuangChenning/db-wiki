---
title: "关闭防火墙和 SELinux"
book: "部署集中式版"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006076966.html"
tags:
  - oceanbase
  - standalone
  - deploy
---

# 关闭防火墙和 SELinux

本文介绍如何关闭防火墙和 SELinux。如果您是个人用户，可以跳过此步骤。如果您是企业用户，建议您参考本文关闭防火墙和 SELinux。

## 关闭防火墙

依次执行以下命令，关闭防火墙：

```
systemctl disable firewalld 
systemctl stop firewalld
systemctl status firewalld
```

## 关闭 SELinux

执行以下命令，打开 `/etc/selinux/config` 配置文件：

```
vi /etc/selinux/config
```

在 `/etc/selinux/config` 配置文件中修改对应配置项为以下内容：

```
SELINUX=disabled
```

执行以下命令或重启服务器，使更改生效：

```
setenforce 0
```

执行以下命令，查看更改是否生效：

```
sestatus
```
