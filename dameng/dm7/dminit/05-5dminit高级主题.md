---
title: "5 dminit高级主题"
book: "DM7 dminit使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/dminit使用手册.htm"
tags:
  - dameng
  - dm7
  - dminit
---

`DM`既支持在裸设备上创建数据库，又支持在`RAC`环境下创建数据库。操作非常简单，只要在使用`dminit`工具创建数据库的时候，指定`CONTROL`参数即可。

例如：初始化配置文件为`dminit.ctl`。

```
./dminit CONTROL=/home/test/dminit.ctl
```

初始化配置文件是一个保存了各数据文件路径设置等信息的文本，名称由用户自己选取。

初始化配置文件内容如何书写，裸设备和`RAC`环境下略有不同，下面分别详细介绍。

## 5.1 支持在裸设备上创建数据库

裸设备就是指没有经过格式化的磁盘。`DM`支持在裸设备上创建数据库，将数据文件、日志文件、`dm.ctl`等文件存储在裸设备上。

裸设备的初始化库配置文件，涉及到的参数较多，详细请参考下表。

表`5.1` 裸设备初始化配置文件参数介绍

| 参数 | 说明 |
| --- | --- |
| system_path | 初始数据库存放的相对路径。文件路径长度最大为256个字符。必选。 与dminit工具的参数PATH等价。选择了此参数，PATH参数要省略 |
| rac_node | RAC节点个数（大于等于2），单站点时不写。 非RAC环境下不用指定 |
| main | 指定MAIN.DBF文件相对路径。 可选，若不指定使用dminit.exe当前所在的工作目录； 若指定，则main_size不能为空 |
| main_size | 指定MAIN.DBF文件大小，以M为单位。 建议指定裸设备大小减一。 裸设备大小由用户保证，若超出实际大小系统会崩溃 |
| system | 指定SYSTEM.DBF文件相对路径。 可选，若不指定使用dminit.exe当前所在的工作目录； 若指定，则system_size不能为空 |
| system_size | 指定SYSTEM.DBF文件大小，以M为单位。 建议指定裸设备大小减一。 裸设备大小由用户保证，若超出实际大小系统会崩溃 |
| roll | 指定ROLL.DBF文件相对路径。 可选，若不指定使用dminit.exe当前所在的工作目录； 若指定，则roll_size不能为空 |
| roll_size | 指定ROLL.DBF文件大小，以M为单位。 建议指定裸设备大小减一。 裸设备大小由用户保证，若超出实际大小系统会崩溃 |
| hmain | 指定HMAIN表空间，huge 表存放相对路径。 可选，若不指定若不指定使用dminit.exe当前所在的工作目录。 若指定了会在指定目录下建HMAIN目录 |
| dmctl | 指定dm.ctl文件相对路径。 若可选，不指定使用dminit.exe当前所在的工作目录。 不需要指定dm.ctl文件大小 |
| dmrac | 指定dm.rac文件相对路径。 可选，若不指定使用dminit.exe当前所在的工作目录。 不需要指定dm.ctl文件大小。 非RAC环境下不用指定 |
| log_count | 日志文件个数。可选，默认为2 |
| log_size | 日志文件大小，若要使用裸设备。 必选，若为普通文件默认为256 |
| log[n] | 日志文件地址。 可选，若不指定，则路径为system_path，文件名为默认 |

例如，在裸设备上创建数据库。参数`system_path`、`main`、`system`、`roll`、`hmain`、`dmctl`、`log01`、`log02`都指定了裸设备。裸设备初始化配置文件（命名`dminit.ctl`）书写如下：

```
system_path = /dm-sharedisk/singledata
main = /dev/raw/raw1
main_size = 2509
system = /dev/raw/raw2
system_size = 2509
roll = /dev/raw/raw3
roll_size = 2509
hmain = /dm-sharedisk/singledata/HMAIN
dmctl = /dev/raw/raw9
log_count = 2
log_size = 2509
log01 = /dev/raw/raw4
log02 = /dev/raw/raw5
```

## 5.2 支持在RAC环境下创建数据库

`DM RAC`是一个单数据库、多实例的集群系统，数据库部署在共享存储上，供所有节点访问，具有高可用性、高性能、低成本等特性。`DM`支持在`RAC`环境下创建数据库。

`RAC`的初始化库配置文件`dminit.ctl`中涉及到的参数，是在裸设备`dminit.ctl`基础上，增加了`[rac[n]]`节点信息。同时，把裸设备`dminit.ctl`中`log_count`，`log_size`，`log[n]`三个参数下放到每个`[rac[n]]`节点里。详细的`[rac[n]]`节点信息请参考下表:

表`5.2 RAC`节点信息

| 参数 | 说明 |
| --- | --- |
| ini | dm.ini文件完整路径。必选 |
| inst_name | 实例名。必选 |
| port | 数据库实例端口号。必选 |
| mal_host | mal系统IP。必选 |
| mal_port | mal系统端口号。必选 |
| log_count | 日志文件个数。可选，默认为2 |
| log_size | 日志文件大小，若要使用裸设备。必选，若为普通文件默认为256 |
| log[n] | 日志文件地址。 可选，若不指定，则路径为system_path，文件名为默认 |

例如，在`RAC`环境下创建数据库。`RAC`环境是搭建在裸设备上。`RAC`环境初始化配置文件（命名`dminit.ctl`）书写如下：

```
system_path = /dm-sharedisk/racdata
rac_node = 2
system = /dev/raw/raw1
system_size = 2509
main = /dev/raw/raw2
main_size = 2509
hmain = /dm-sharedisk/racdata/HMAIN
roll = /dev/raw/raw3
roll_size = 2509
dmctl = /dev/raw/raw10
dmrac = /dev/raw/raw11
[rac01]
ini = /dm-sharedisk/racdata/dm01.ini
inst_name = rac01
port = 6000
mal_host = localhost
mal_port = 7000
log_count = 2
log_size = 2509
log01 = /dev/raw/raw4
log02 = /dev/raw/raw5
[rac02]
ini = /dm-sharedisk/racdata/dm02.ini
inst_name = rac02
port = 6001
mal_host = localhost
mal_port = 7001
log_count = 2
log_size = 2509
log01 = /dev/raw/raw6
log02 = /dev/raw/raw7
```
