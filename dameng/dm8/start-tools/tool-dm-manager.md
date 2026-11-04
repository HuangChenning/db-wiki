---
title: "DM 管理工具"
book: "DM 数据库工具介绍"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/start/tool-dm-manager.html
tags:
  - dameng
  - dm8
  - start-tools
---

## 一、概述

DM 管理工具是数据库自带的图形化工具，可以方便快捷的对数据进行管理。在网络允许的条件下，可通过单个管理工具，对多个数据实例进行管理，方便简化 DBA 对数据库的日常运维操作要求。

## 二、启动 DM 管理工具

### 2.1 Windows 环境

点击开始界面，选择【达梦数据库】菜单，点击【DM 管理工具】，即可进入管理工具对数据库进行管理，如下图所示：

### 2.2 Linux 环境

启用图形界面前需要通过如下方法将图形界面权限放开：

```shell
[root@localhost mnt]# xhost +
access control disabled, clients can connect from any host
[root@localhost mnt]# echo $DISPLAY
[root@localhost mnt]# su - dmdba
Last login: 四 1月 25 16:41:51 CST 2024 on pts/1
[dmdba@localhost ~]$ export DISPLAY=:0.0
```

进入数据库安装路径 /tool 目录下，运行./manager 即可启动 DM 管理工具。

```shell
[dmdba@localhost ~]$ cd /home/dmdba/dmdbms/tool/
[dmdba@localhost tool]$ ll
[dmdba@localhost tool]$ ./manager
```

![image.png](img/202401301447302NAT1ARV2P3RJU6MUA.png)

## 三、数据库实例连接

- 新建连接

创建连接数据库的对象导航，不进行保存，下次开启后需重新连接。

- 注册连接

创建连接数据库的对象导航，进行保存，下次开启后对象导航存在，可直接进行连接。

![文档和图片文件夹图示](img/manger-01.png)

### 3.1 注册连接

输入主机名（IP 地址）、端口、用户名、密码，点击【测试】，测试是否连通，点击【确定】，连接数据库，如下图所示：

![文档和图片文件夹图示](img/manager-02.png)

对象导航栏自动生成对应的数据库链接信息，点击鼠标【右键】，点击【连接】即可，如下图所示：

![文档和图片文件夹图示](img/manager-03.png)

### 3.2 新建连接

点击【新建连接】，输入主机名（IP 地址）、端口、用户名、密码，点击【确认】即可直接进行数据库连接，如下图所示：

![文档和图片文件夹图示](img/manager-04.png)

## 四、信息说明和常用配置

### 4.1 窗口基本功能说明

连接数据库后，左侧显示对象导航；右侧为新建查询窗口，通过窗口可编写 SQL 语句进行执行；顶部为工具栏；底部为消息和结果集。如下图所示：

![image.png](img/20240130160544Z7TRYDQ6DKBQWIX6NX.png)

### 4.2 查看数据库实例信息

通过 DM 管理工具可查看数据库实例的信息，包含 **系统概览，表使用空间，系统管理，日志文件，归档配置** 等几个方面。

选择对应实例，右键点击【管理服务器】，即可进行查看实例相关信息，如下图所示：

![image.png](img/20240130160830ZB7CZ13W4DUUBVH2C9.png)

### 4.3 常用选项配置

通过常用选项的配置，可以帮助日常的操作，包含 **审计分析工具，快捷键，数据迁移工具，查询分析器，管理工具** 等功能。

选择管理工具的【窗口】，点击【选项】功能，可进入常用选项的配置。例如选择查询分析器的【编辑器】功能，可修改编辑器显示功能，如下图所示：

![image.png](img/20240130145353WB28GCRDQK2ZEY6VQS.png)

## 五、表空间和用户

### 5.1 创建表空间

选中连接的数据库实例，选择【表空间】，右键点击【新建表空间】，输入表空间的名称、文件路径等信息，点击【确定】，即可创建完成表空间，如下图所示：

![image.png](img/20240130145608A53H7IMJXN2CQFBQOU.png)

### 5.2 创建用户

选中连接的数据库实例，选择用户下的【管理用户】，右键点击【新建用户】，输入用户名和密码，选择用户所述的表空间和索引表空间，如下图所示：

![image.png](img/20240130150056WAWL0AJUYFKTL12OWJ.png)

对用户所属角色、系统权限、对象权限进行修改，点击【确定】即可完成用户创建，如下图所示：

![image.png](img/20240130150412ZTW70IVBDJORYUPUV8.png)

![image.png](img/20240130150509DWCVKMNLBIQNOCWGW9.png)

## 六、数据库的备份

通过 DM 管理工具可对数据库进行备份。

右键点击【备份】，根据备份的级别为库，表，表空间，归档几个类别的备份，选中备份类别，右键点击选择【新建备份】，如下图所示：

![image.png](img/20240130150803D7BZDHXPMENN23SMQ0.png)

数据库进行备份时需要开启归档，否则无法进行备份，开启归档方法可参考 [开启本地归档](https://eco.dameng.com/document/dm/zh-cn/ops/installation-install.html#2.2%20%E5%BC%80%E5%90%AF%E6%9C%AC%E5%9C%B0%E5%BD%92%E6%A1%A3) 。

进入备份界面，输入“备份名”和“备份集目录”，如下图所示：

![image.png](img/20240130152611HOI9H2BC9KR4QJJEUH.png)

高级选项可针对备份，进行操作，如备份是否进行压缩，是否生成备份日志，是否进行加密等操作，如下图所示：

![image.png](img/20240130152354A6GKHI69FFPY0V4DTQ.png)

DDL 则产生此次备份数据库的语句命令，如下图所示：

![image.png](img/20240130152531WPN04RMA2JYEB154X5.png)

配置完成后点击确定即可开始备份。

### 6.1 代理作业

通过 DM 管理工具，可创建代理环境。代理环境的主要作用在于设置数据库的定时备份，通过代理进行设置，免去了通过系统进行 crontab 定时计划执行 shell 脚本的麻烦。

#### 6.1.1 创建代理环境

右键点击【代理】，选择【创建代理环境】，数据库状态正常，管理工具正常连接，创建代理环境显示成功，如下图所示：

![image.png](img/20240130152723WI2K9PNZRCVRF68L7Y.png)

#### 6.1.2 创建定时备份作业

在代理下，右键点击【作业】，选择【新建作业】，如下图所示：

![image.png](img/2024013015282564QXP05JDC2GH4BU99.png)

在“常规”中填写设定的“作业名”和“作业描述”，如下图所示：

![image.png](img/20240130152854NAKPJIAUV4WRHS2ZNH.png)

在“作业步骤”中点击“添加”来添加作业步骤，如下图所示：

![image.png](img/20240130153253DH45265P8KM2GJ3RHF.png)

填写作业的“步骤名称”，选择“步骤类型”。

![image.png](img/20240130153423DM1B23W2CDOUDD7EIA.png)

填写“备份路径”，选择“备份方式”。

![image.png](img/20240130153504K2Z4WXHYPE2ZAV8PPP.png)

在“高级”中配置作业步骤“成功时”和“失败时”的操作，点击【确定】，生成该作业步骤。

![image.png](img/20240130153649XA80H7OMXQVYKQO36B.png)

在“作业调度”中点击“新建”，创建作业调度，如下图所示：

![image.png](img/20240130153825VLPD40BOBHMZPERMRH.png)

填写调度的“名称”，设定作业的“调度类型”、“执行周期”、“每日频次”等策略，点击【确认】，生成作业调度，如下图所示：

![image.png](img/20240130154115U45TVTC7KIT8NXLTCB.png)

作业调度配置完成后可以看到“调度频率”的描述，如下图所示：

![image.png](img/20240130154300VR4ULHHNUBFBXYNFMO.png)

点击“DDL”可以展示此次代理作业的整体的 DDL 语句，如下图所示：

![image.png](img/20240130154208CP0VY2KURZL9FUO36D.png)

点击确定即可完成作业配置。

## 七、调试工具 DMDBG

DM 提供了功能完善的 PL/SQL 调试工具 DMDBG，可调试非 DDL 语句或语句块，以便定位 PL/SQL 中存在的错误，点击左上方的小乌龟即可开启调试工具，如下图所示：

![image.png](img/20240130162954FNLCP8BTXJA5VCCYPT.png)

主菜单栏提供一些与 SQL 调试相关的按键，如下图所示：从左到右的按键分别表示开始、继续、暂停、停止、进入、下一步、跳出、选择对象。

![image.png](img/20240130162815S5D5MTNQEQ6C2F1FHU.png)

在 SQL 编辑区右键可选择添加/删除断点等功能，在下方消息区为 SQL 调试堆栈、变量、显示、断点和消息区域，界面如下图所示：

![image.png](img/20240130162826547W5QFFMJXOGNW3K7.png)