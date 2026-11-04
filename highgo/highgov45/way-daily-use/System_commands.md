---
title: "27、通过数据库执行系统命令"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/System_commands.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 通过数据库执行系统命令

## 一、说明

通过数据库的COPY…PROGRAM…命令可以直接执行操作系统命令。该命令必须使用数据库管理员执行，因该命令执行具有一定破坏性，建议数据库日常使用中尽量不要使用数据库管理员，并经常修改数据库管理员的密码。

该命令适用于瀚高数据库3.0.0及以后版本

## 二、测试过程

### 1、创建执行记录的保存表

```
CREATE TABLE cmd_exec(cmd_output text);
```

### 2、使用COPY…PROGRAM…执行操作系统命令，下面是几个测试案例

（1）切换目录，查看目录下的文件。默认执行目录是$PGDATA

```
COPY cmd_exec FROM PROGRAM 'cd /root;pwd;ls -lrth';
```

（2）创建可执行脚本并执行

```
COPY cmd_exec FROM PROGRAM 'echo "touch /tmp/test.txt">/tmp/test.sh;sh /tmp/test.sh';
```

（3）删除文件

```
COPY cmd_exec FROM PROGRAM 'rm -f /tmp/test.*';
```