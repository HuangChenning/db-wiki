---
title: "动态增加节点"
book: "DM8 数据共享集群"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dynamically-expand-nodes.html
tags:
  - dameng
  - dm8
  - dsc
---

DMDSC 集群支持动态增加节点，每次扩展可以在原有基础上增加一个节点。

动态增加节点要求当前 DMDSC 集群的所有节点都为 OK 状态，所有 DMSERVER 实例都处于 OPEN 状态，且可以正常访问。

> **注意**
> 
> 增加节点过程中，不应该有修改数据库状态或模式的操作。

## 14.1 动态增加节点流程

基于 DMASM 的 DMDSC 和基于 DMASM 镜像的 DMDSC 均支持动态增加节点，二者流程基本一致。基于 DMASM 的 DMDSC 动态增加节点时，需要使用相应的 DMASMSVR、DMASMTOOL 和 DMASMCMD 工具；基于 DMASM 镜像的 DMDSC 动态增加节点时，需要使用相应的 DMASMSVRM、DMASMTOOLM 和 DMASMCMDM 工具。

动态增加节点要求当前 DMDSC 集群的所有节点都为 OK 状态，所有 DMSERVER 实例都处于 OPEN 状态，且可以正常访问。每次扩展可以在原有基础上增加一个节点。

本章节主要基于 [12.1 基于 DMASM 的 DMDSC](dsc-build.md) 成功架构的数据共享集群系统，介绍如何动态扩展一个节点。

已搭建好的 DMDSC 集群实例名为 DSC01、DSC02，在此基础上扩展一个节点 DSC03。

### 14.1.1 环境说明

新增节点环境为：

操作系统：eulerosv2r7.x86\_64。

网络配置：eth0 网卡为 192.168.102.x 内网网段，新增节点为 192.168.102.106；eth1 为 192.168.100.x 外网网段，新增节点为 192.168.100.106。

DM 各种工具位于目录：/home/dmdba/dmdsc/bin。

配置文件位于目录：/home/dmdba/dmdsc/data/DSC03。

14.1 新增节点环境

<table><tbody><tr><td><b>节点机器</b></td><td><b>实例名称</b></td><td><b>IP</b></td><td><b>PORT_NUM</b></td></tr><tr><td rowspan="3">107</td><td>CSS0</td><td rowspan="3">192.168.100.107</td><td>9836</td></tr><tr><td>ASM0</td><td>5836</td></tr><tr><td>DSC01</td><td>6636</td></tr><tr><td rowspan="3">110</td><td>CSS1</td><td rowspan="3">192.168.100.110</td><td>9837</td></tr><tr><td>ASM1</td><td>5837</td></tr><tr><td>DSC02</td><td>6637</td></tr><tr><td rowspan="3">106</td><td>CSS2</td><td rowspan="3">192.168.100.106</td><td>9838</td></tr><tr><td>ASM2</td><td>5838</td></tr><tr><td>DSC03</td><td>6638</td></tr></tbody></table>

### 14.1.2 操作流程

1. 在 107 机器上使用 DMASMCMD 工具 export 出备份 DMDCR\_CFG\_BAK.INI
```
./dmasmcmd
Asm> export dcrdisk '/dev_DSC2/DCR' to '/home/dmdba/dmdsc/data/DSC01/dmdcr_cfg_bak.ini'
```

若是基于 DMASM 镜像的 DMDSC，则会存在多个 DCRV 磁盘，此时使用 DMASMCMDM 工具 export 出任意一个磁盘备份即可。

2. 为新增节点准备日志文件

1）使用 DIsql 登录任意一个节点执行添加日志文件操作：

至少两个日志文件，路径必须是 ASM 文件格式，大小可以参考其他两个活动节点。

```
SQL>alter database add node logfile '+DMLOG/log/DSC03_log1.log' size 256, '+DMLOG/log/DSC03_log2.log' size 256;
```

2）使用 dmctlcvt 工具将 dm.ctl 转换为文本文件 dmctl.txt，查看 dmctl.txt，新增节点的日志文件信息已经添加进 dm.ctl。

```
./dmctlcvt TYPE=1 SRC=+DMDATA/data/dsc2/dm.ctl DEST=/home/dmdba/dmdsc/data/DSC01/dmctl.txt DCR_INI=/home/dmdba/dmdsc/data/DSC01/dmdcr.ini
```

3）使用 dmasmtool 工具登录 ASM 文件系统，也可以看到新增的节点日志文件

```
./dmasmtool DCR_INI=/home/dmdba/dmdsc/data/DSC01/dmdcr.ini
ASM>ls +DMLOG/log
```
3. 修改 DMMAL.INI 配置文件

修改 107 机器/home/dmdba/dmdsc/data/DSC01 目录以及 110 机器/home/dmdba/dmdsc/data/DSC02 目录下的 DMMAL.INI 配置文件，添加新增节点信息。

```
[MAL_INST3]
MAL_INST_NAME    = DSC03
MAL_HOST       = 192.168.102.106
MAL_PORT       = 6538
```
4. 为新增节点准备 config\_path

将 107 机器/home/dmdba/dmdsc/data/DSC01 路径下的 DSC01\_conf 文件夹拷贝到 106 机器/home/dmdba/dmdsc/data/DSC03 路径下，修改文件夹名称为 DSC03\_conf。

修改 DSC03\_conf 文件夹下的配置文件：

1）修改 dm.ini

```
CONFIG_PATH        = /home/dmdba/dmdsc/data/DSC03/DSC03_conf
INSTANCE_NAME    = DSC03
PORT_NUM = 6638
```

2）如果打开了归档参数，修改 dmarch.ini

5. 新建 DMDCR.INI 配置文件，保存到节点 106 的/home/dmdba/dmdsc/data/DSC03 目录下面

注意设置 dmdcr\_seqo 为 2，修改 DM.INI 路径。

```
DMDCR_PATH     = /dev_DSC2/DCR
DMDCR_MAL_PATH =/home/dmdba/dmdsc/data/DSC03/dmasvrmal.ini  #DMASMSVR使用的MAL配置文件路径
DMDCR_SEQNO   = 2
#ASM重启参数，命令行方式启动
DMDCR_ASM_RESTART_INTERVAL = 0
DMDCR_ASM_STARTUP_CMD        = /home/dmdba/dmdsc/bin/dmasmsvr dcr_ini=/home/dmdba/dmdsc/data/DSC03/dmdcr.ini
#DB重启参数，命令行方式启动
DMDCR_DB_RESTART_INTERVAL    = 0  
DMDCR_DB_STARTUP_CMD         = /home/dmdba/dmdsc/bin/dmserver path=/home/dmdba/dmdsc/data/DSC03/DSC03_conf/dm.ini dcr_ini=/home/dmdba/dmdsc/data/DSC03/dmdcr.ini
DMDCR_LINK_CHECK_IP=192.168.1.88
```

设置了 DMDCR\_LINK\_CHECK\_IP，须为 106 节点的 DMSERVER、DMASMSVR、DMCSS 赋予 ping 权限。

```
sudo setcap cap_net_raw,cap_net_admin=eip /home/dmdba/dmdsc/bin/dmserver
sudo setcap cap_net_raw,cap_net_admin=eip /home/dmdba/dmdsc/bin/dmasmsvr
sudo setcap cap_net_raw,cap_net_admin=eip /home/dmdba/dmdsc/bin/dmcss
```
6. 修改当前环境的 DMASVRMAL.INI 配置文件

直接修改当前环境的 DMASVRMAL.INI 文件，添加新增节点信息，使用 DMASM 的所有节点都要配置，内容完全一样，并且将新增信息后的 DMASVRMAL.INI 文件拷贝到 106 机器的/home/dmdba/dmdsc/data/DSC03 目录下。

```
[MAL_INST2]
MAL_INST_NAME= ASM2
MAL_HOST= 192.168.102.106
MAL_PORT= 4838
```
7. 修改 dmdcr\_cfg\_bak.ini，添加新增节点信息，CSS/ASMSVR/DB 都要配置所有组信息修改：
```
DCR_GRP_N_EP = 3
DCR_GRP_EP_ARR = {0,1,2}
```

每个组增加一个节点信息，注意 DCR\_EP\_SHM\_KEY、端口号不能冲突；各组信息要放在各自的后面，即\[GRP\_CSS\]中 CSS2 放在 CSS1 后面，\[GRP\_ASM\]中 ASM2 放在 ASM1 后面，DSC03 放在 DSC02 后面。

```
[GRP_CSS]
DCR_EP_NAME = CSS2
DCR_EP_HOST = 192.168.102.106
DCR_EP_PORT = 9838

[GRP_ASM]
DCR_EP_NAME    =     ASM2
DCR_EP_SHM_KEY     =     93362
DCR_EP_SHM_SIZE =     512
DCR_EP_HOST =         192.168.102.106
DCR_EP_PORT =         5838
DCR_EP_ASM_LOAD_PATH= /dev_DSC2

[GRP_DSC] 
DCR_EP_NAME        =    DSC03
DCR_EP_SEQNO       =    2
DCR_EP_PORT        =    6638
```
8. 使用 DMASMCMD 工具将新增节点信息写回磁盘，新增节点作为 error 节点
```
./dmasmcmd
Asm> extend dcrdisk '/dev_DSC2/DCR' from '/home/dmdba/dmdsc/data/DSC01/dmdcr_cfg_bak.ini'
```

若是基于 DMASM 镜像的 DMDSC，则会存在多个 DCRV 磁盘，此时需要使用 DMASMCMDM 工具将新增节点信息写回所有 DCRV 磁盘。

9. 在 dmcssm 控制台执行增加节点命令
```
extend node
```

程序会通知所有实例(CSS/ASMSVR/dmserver)更新信息，在 CSS 控制台执行 SHOW 命令，能看到新增节点信息，ASMSVR/dmserver 是 error 节点，程序会通知 ASMSVR/dmserver 更新 MAL 信息。

10. 启动新的 DMCSS、DMASM 服务程序

在 106 机器启动 DMCSS、DMASMSVR 程序。

手动启动新的 DMCSS，dcr\_ini 指向新的 DMDCR.INI 文件：

```
./dmcss DCR_INI=/home/dmdba/dmdsc/data/DSC03/dmdcr.ini
```

手动启动新的 DMASMSVR，dcr\_ini 指向新的 DMDCR.INI 文件，DMASMSVR 启动故障重加入流程：

```
./dmasmsvr DCR_INI=/home/dmdba/dmdsc/data/DSC03/dmdcr.ini
```

如果 DMCSS 配置有自动拉起 DMASMSVR 的功能，可以等待 DMCSS 自动拉起 DMASMSVR 程序，不需要手动启动。

11. 启动新的数据库服务器

如果 DMCSS 配置有自动拉起 DMSERVER 的功能，可以等待 DMCSS 自动拉起实例，不需要手动启动。

如果需要手动启动，可参考下面的操作步骤：

106 机器：

```
./dmserver    /home/dmdba/dmdsc/data/DSC03/DSC03_conf/dm.ini DCR_INI=/home/dmdba/dmdsc/data/DSC03/dmdcr.ini
```
12. 修改 dmcssm.ini

修改 DMCSSM.INI，增加新扩节点 DMCSS 的 IP:PORT 配置项 CSSM\_CSS\_IP，并重启 DMCSSM。

```
#增加新增节点的CSS的连接信息
#和DMDCR_CFG.INI中CSS配置项的DCR_EP_HOST和DCR_EP_PORT保持一致
CSSM_CSS_IP = 192.168.102.106:9838
```

> **注意**
> 
> 如果由于配置文件错误，动态增加节点失败，只能停掉所有实例，重新init dcr磁盘，不影响dmserver数据。

### 14.1.3 注意事项

1. 增加节点前由用户保证所有 dmcss/dmasmsvr/dmserver 节点都是 OK 的，且都是活动的；
2. 每次增加节点只能扩一个节点，扩展完成后可以再继续增加节点；
3. 增加节点的过程中不能出现修改实例状态或模式的操作；
4. 增加节点的过程中，如果发生 dmcss/dmasmsvr/dmserver 实例故障，会导致扩展失败；
5. 扩展过程中操作失误（比如未修改 dmasvrmal.ini，未增加日志文件），会导致扩展失败；
6. 执行完 extend node 命令，用户需要查看 log 文件，确认扩展操作是否成功；
7. 扩展失败可能会导致集群环境异常，需要退出所有 dmcss/dmasmsvr/dmserver，重新 init dcr 磁盘。

## 14.2 动态删除节点流程

DMDSC 集群（基于 DMASM 的或基于 DMASM 镜像的）不支持动态删除节点。