---
title: "DMCSS 介绍"
book: "DM8 数据共享集群"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/css-introduction.html
tags:
  - dameng
  - dm8
  - dsc
---

达梦集群同步服务（Dameng Cluster Synchronization Services，简称 DMCSS）使用 DMASM 集群或 DMDSC 集群都必须配置 DMCSS 服务。在 DMASM 集群或 DMDSC 集群中，每个节点都需要配置一个 DMCSS 服务。这些 DMCSS 服务自身也构成一个集群，DMCSS 集群中负责监控、管理整个 DMASM 集群和 DMDSC 集群的节点称为控制节点(Control Node)，其他 DMCSS 节点称为普通节点(Normal Node)。DMCSS 普通节点不参与 DMASM 集群和 DMDSC 集群管理，当 DMCSS 控制节点故障时，会从活动的普通节点中重新选取一个 DMCSS 控制节点。

DMCSS 工作的基本原理是：在 VOTE 磁盘（非镜像环境下）或 DCRV 磁盘（镜像环境下）中，为每个被监控对象（DMASMSVR、DMSERVER、DMCSS）分配一片独立的存储区域，被监控对象定时向 VOTE 或 DCRV 磁盘写入信息（包括时间戳、状态、命令、以及命令执行结果等）；DMCSS 控制节点定时从 VOTE 或 DCRV 磁盘读取信息，检查被监控对象的状态变化，启动相应的处理流程；被监控对象只会被动的接收 DMCSS 控制节点命令，执行并响应。

DMCSS 主要功能包括：写入心跳信息、选举 DMCSS 控制节点、选取 DMASM/DMDSC 控制节点、管理被监控对象的启动流程、集群状态监控、节点故障处理、节点重加入等，DMCSS 还可以接收并执行 DMCSSM 指令。

## 5.1 启动命令

```
dmcss V8
version: 03134284389-20250411-268655-10000
书写格式: ./dmcss KEYWORD=<value> {KEYWORD=<value>}
          其中{}表示大括号内的关键词可为0~N个，N为正整数，{}本身无需出现在语句中
使用示例: ./dmcss DCR_INI=/opt/data/DAMENG/dmdcr.ini
-------------------------------------------------------------------
关键词（KEYWORD）        说明                  缺省值        是否必选项
-------------------------------------------------------------------
DCR_INI                  dmdcr.ini路径         无            是  
-NOCONSOLE               以服务方式启动        无            否  
LISTEN_IPV6              是否监听IPV6          Y             否  
HELP                     打印帮助信息          无            否  
-------------------------------------------------------------------
```

## 5.2 心跳信息

DMCSS 实例启动后，每间隔 1 秒向 Voting Disk 指定区域写入心跳信息（包括自身的状态、时间戳等），表示 DMCSS 节点处于活动状态。

## 5.3 选举 DMCSS 控制节点

DMCSS 启动后向 VOTE 磁盘（非镜像环境下）或 DCRV 磁盘（镜像环境下）写入信息，并读取其他 DMCSS 节点的信息，如果 DMCSS 集群中还没有活动的控制节点，则选举 DMCSS 控制节点。DMCSS 选举的原则有两条：

1. 先启动的 DMCSS 作为控制节点。
2. 如果 DMCSS 同时启动，那么则选择节点号小的节点为控制节点。
3. 如果 DMCSS 控制节点挂掉，那么会将先向 VOTE 磁盘（非镜像环境下）或 DCRV 磁盘（镜像环境下）写入心跳信息的节点设置为控制节点；若同时有多个节点先向 VOTE 磁盘（非镜像环境下）或 DCRV 磁盘（镜像环境下）写入心跳信息，那么选择节点号小的节点为控制节点。

## 5.4 选取监控对象控制节点

DMCSS 控制节点启动后，会为基于 DMASM/裸设备的 DMDSC 集群指定控制节点。DMCSS 选取监控对象控制节点的原则有两条：

1. 只有一个活动节点，则设置活动节点为控制节点。
2. 存在多个活动节点，则选择节点号小的节点为控制节点。

## 5.5 启动流程管理

DMASM 和 DMDSC 集群中的实例启动后，一直处于 waiting 状态，等待 DMCSS 的启动命令。DMCSS 控制节点在选取监控对象控制节点后，通知控制节点启动，在控制节点启动完成后，再依次通知其他普通节点启动。

## 5.6 状态检测

DMCSS 维护集群状态，随着节点活动信息的变化，集群状态也会产生变化，DMCSS 控制节点会通知被监控节点执行不同命令，来控制节点启动、故障处理、故障重加入等操作。

DMCSS 控制节点每秒从 VOTE 磁盘（非镜像环境下）或 DCRV 磁盘（镜像环境下）读取被监控对象的心跳信息。一旦被监控对象的时间戳在 DCR\_GRP\_DSKCHK\_CNT 秒内没有变化，则认为被监控对象出现异常。

DMCSS 普通节点定时读取 DMCSS 控制节点的心跳信息，监控 DMCSS 运行状态。

## 5.7 故障处理

DMCSS 控制节点检测到实例故障后，首先向故障实例的 VOTE 磁盘（非镜像环境下）或 DCRV 磁盘（镜像环境下）区域写入 Kill 命令（所有实例一旦发现 Kill 命令，无条件自杀），避免故障实例仍然处于活动状态，引发脑裂，然后启动故障处理流程，不同类型实例的故障处理流程存在一些差异。

- DMCSS 控制节点故障处理流程
1. 活动节点重新选举 DMCSS 控制节点
2. 新的 DMCSS 控制节点通知出现 DMCSS 故障节点对应的 dmasmsvr、dmserver 强制退出
- DMASMSVR 实例故障处理流程
1. 挂起工作线程
2. 更新 DCR（参考 [10 DMASM 介绍](dmasm-introduce.md) ）故障节点信息
3. 通知故障节点对应 DMSERVER 强制退出
4. DMASMSVR 进行故障恢复
5. 恢复工作线程
- DMSERVER 实例故障处理流程
1. 更新 DCR 故障节点信息
2. 重新选取一个控制节点
3. 通知 DMSERVER 控制节点启动故障处理流程（参考 [7 DMDSC 故障处理](dsc-fault-handling.md) ）
4. 等待 DMSERVER 故障处理结束

## 5.8 节点重加入

如果检测到故障节点恢复，DMCSS 会通知控制节点启动节点重加入流程。

- 数据库实例重加入
1. 挂起工作线程
2. 修改节点的状态为故障节点重加入状态
3. 执行恢复操作
4. 节点进入 STARTUP 状态，准备启动
5. OPEN 重加入的节点
6. 重启工作线程
7. 执行 OPEN 数据库实例的操作
- DMASM 实例重加入
1. 挂起工作线程
2. 修改节点的状态为故障节点重加入状态
3. 执行恢复操作
4. 节点进入 STARTUP 状态，准备启动
5. OPEN 重加入的节点
6. 重启工作线程

## 5.9 集群指令

DMCSS 控制节点通过一系列的集群指令控制被监控对象的启动、故障处理、状态切换等。DMCSS 控制节点向目标对象的 VOTE 磁盘（非镜像环境下）或 DCRV 磁盘（镜像环境下）指令区写入命令，通知目标对象执行相应命令，并等待执行响应。每条指令的功能都比较单一，比如修改状态、设置控制节点、执行一条 SQL 等，复杂的集群流程控制就是由这些简单的指令组合起来完成的。

## 5.10 控制台命令

1. help

显示帮助信息。

2. show

查看集群状态。DMCSS 控制节点会显示 DMCSS、DMASM、DMDSC 三个集群的信息，而 DMCSS 普通节点只会显示 DMCSS 集群的信息。

具体显示的内容如下所示。

**group\[\]行显示的内容为：**

name： 集群名称。

seq： 集群编号。

type： 集群组类型。包含：CSS、ASM、DB。

control\_node： 集群内控制节点。

**css 集群组额外显示的内容为：**

DCRV\_STATUS: dcrv 磁盘状态，仅在 dsc 镜像环境中展示。包括：OK(正常状态)、FAILED(故障状态)、UNUSED(未使用状态)、UNKNOWN(未知状态)。

**ep 行显示的内容为：**

css\_time：取得 ep 信息的 css 当前时间,仅 dmcssm 显示。

inst\_name：节点实例名。

seqno：节点编号。

port：实例对外提供服务的端口号。

mode：节点模式。包括：CONTROL（控制节点）、NORMAL（普通节点）。

inst\_status：实例系统状态。包括：INSTALL（初始化数据库）、STARTUP（节点启动）、AFTER REDO（启动，REDO 完成）、MOUNT（挂载）、OPEN（正常打开）、SUSPEND（挂起）、SHUTDOWN（关闭）、CRASH\_RECV（出现节点故障）、INVALID EP STATUS（集群非 OPEN 状态下，不支持故障处理，可能是集群同步服务 DMCSS 或监视器 DMCSSM 版本过旧导致）。

vtd\_status：实例的集群状态。包括：STARTUP（启动）、STARTUP2（启动第二步）、WORKING（工作中）、TO SHUTDOWN（准备关闭）、SHUTDOWN（已经关闭）、SYSHALT（系统崩溃）、STOP（停止）、ADD\_DCRV（添加 DCRV 磁盘）、DEL\_DCRV（删除 DCRV 磁盘）。

is\_ok：实例在集群内是否正常。OK 是，ERROR 否。ERROR 节点暂时从集群内踢出。

active： 实例是否活动。TRUE 是，FALSE 否。

guid：实例的 GUID 值。

pid:实例进程 id。

ts：实例的时间戳。

**css 集群组额外显示的内容为：**

auto check:CSS 是否允许自动执行故障处理/故障恢复。TRUE 是，FALSE 否。该参数仅 dmcssm 可查看。

auto restart:节点是否能够被自动拉起。TRUE 是，FALSE 否。

DCRV\_STATUS: dcrv 磁盘状态，仅在 dsc 镜像环境中展示。包括：OK(正常状态)、FAILED(故障状态)、UNUSED(未使用状态)、UNKNOWN(未知状态)。

**asm/db 集群组额外显示的内容为：**

n\_ok\_ep:当前集群中 OK 状态的站点个数。

ok\_ep\_arr(index,seqno):当前集群中 OK 状态的站点号。index 表示内存中 ok\_ep\_arr 数组下标，seqno 表示 index 下标对应的 ok 状态站点号。

sta:当前集群组状态。包括：STARTUP（控制节点选举）、OPEN（节点启动）、Control Node STARTUP（控制节点启动）、Normal Node STARTUP（非控制节点启动）、EP\_OPEN（节点启动到 OPEN 状态）、PROCESS\_CRASH(节点故障处理)、PROCESS\_RECOVER（节点故障恢复）、SYS\_HALT（系统 halt）、SHUTDOWN（组退出）、LINK\_CHECK（链路检查）、STOP（节点单独退出）、INVALID GRP STATUS（无效状态）。

sub\_sta:当前集群组子状态。包括：STARTUP（节点启动）、WAIT\_CSS\_MASTER（等待控制节点选举）、WAIT\_STARTUP（等待节点启动）、WAIT\_EP\_OPEN（等待节点启动到 open 状态）、WAIT\_CRASH\_RECV（等待故障恢复结束）、SUB\_WAIT\_ERROR\_EP\_ADD（等待故障节点重加入结束)、WAIT\_EP\_RECOVER（等待节点故障恢复结束）、WAIT\_SYS\_HALT（等待系统 HALT 结束）、PRE\_SUSPEND（准备挂起工作线程）、SUSPEND\_WORKER（挂起工作线程）、WAIT\_SUSPEND\_WORKER（等待工作线程挂起）、WAIT\_RESUME\_WORKER（等待恢复工作线程）、WAIT\_REAL\_OPEN（等待节点启动到 REAL\_OPEN 状态）、WAIT\_REDO（主机 redo 执行完，等待从机启动）、AFTER\_REDO（redo 执行完成）、MASTER\_CONFIG\_VIP（控制节点配置 vip）、SLAVE\_CONFIG\_VIP（非控制节点配置 vip）、WAIT\_SLAVE\_CONFIG\_VIP（等待非控制节点配置 vip）、WAIT\_MASTER\_CONFIG\_VIP（等待控制节点配置 vip）、EP\_CONFIG\_VIP（dmserver 销毁 VIP 监听线程）、WAIT\_EP\_CONFIG\_VIP（等待 dmserver 销毁 VIP 监听线程）、EP\_CRASH（节点故障处理）、WAIT\_EP\_CRASH（等待节点故障处理）、STOP\_EP\_CRASH（单节点故障处理）、WAIT\_LINK\_CHECK（等待链路检查）、WAIT\_DCR\_LOAD（等待 dcr 信息加载）、WAIT\_ADJUST\_MASTER（等待执行 ADJUST\_MASTER\_EP 命令完成）、CRASH\_ROLLBACK（回滚故障处理）、WAIT\_CRASH\_ROLLBACK（等待回滚故障处理）、WAIT\_CMD\_CLEAR（等待命令清理）。

break ep:正在进行故障处理的站点。

recover ep:正在进行故障恢复的站点。

例 下面展示一段 show 信息。

```
======== group[name = GRP_CSS, seq = 0, type = CSS, Control Node = 0]=========

[CSS0] auto check = TRUE, global info:
[ASM0] auto restart = FALSE
[DSC0] auto restart = FALSE
[CSS1] auto check = TRUE, global info:
[ASM1] auto restart = FALSE
[DSC1] auto restart = FALSE

ep:     css_time           inst_name    seqno   port     mode         inst_status vtd_status    is_ok   active     guid           pid          ts
        2024-11-18 17:00:48   CSS0        0      9941   Control Node       OPEN      WORKING        OK      TRUE    892779205       50328     892779531
        2024-11-18 17:00:48   CSS1        1      9942   Normal Node       OPEN     WORKING        OK      TRUE    893084408       80628     893084733

======== group[name = GRP_ASM, seq = 1, type = ASM, Control Node = 0]==========

n_ok_ep = 1
ok_ep_arr(index, seqno):
(0, 0)

sta = OPEN, sub_sta = STARTUP
break ep = NULL
recover ep = NULL

crash process over flag is TRUE
ep:     css_time          inst_name  seqno   port      mode         inst_status       vtd_status    is_ok     active    guid         pid       ts
        2024-11-18 17:00:48    ASM0     0     9949   Control Node       OPEN         WORKING        OK        TRUE   894305753     151772    894306070
        2024-11-18 17:00:48    ASM1     1     9950   Normal Node        OPEN            WORKING        ERROR     FALSE  894611051     43264     894611275

======= group[name = GRP_DSC, seq = 2, type = DB, Control Node = 255]=========

n_ok_ep = 2
ok_ep_arr(index, seqno):
(0, 0)
(1, 1)

sta = OPEN, sub_sta = STARTUP
break ep = NULL
recover ep = NULL

crash process over flag is FALSE
ep:     css_time           inst_name   seqno   port      mode         inst_status   vtd_status   is_ok    active     guid         pid         ts
        2024-11-18 17:00:48    DSC0       0     5236   Normal Node     SHUTDOWN   SHUTDOWN     OK       FALSE   901786929      126008    901787096
        2024-11-18 17:00:48    DSC1       1      5237   Normal Node     SHUTDOWN   SHUTDOWN     OK       FALSE   901940019      79784     901940183

===========================================================
```
3. open force group\_name

在启动 ASM 或 DB 组时，如果某个节点故障一直无法启动，可借助此命令将 ASM 或 DB 组强制 OPEN。

此命令需要在 DMCSS 控制节点上执行，并且 DMCSS 控制节点的监控需要处于打开状态。

4. extend node

DMDSC 集群联机增加节点时使用。

程序会通知所有实例(DMCSS/DMASMSVR/DMSERVER)更新 dcr 信息。

使用 show 命令能看到新增节点信息，新增 DMASMSVR/DMSERVER 为 ERROR 状态。

5. set master force

该命令用于强制设置当前节点为控制节点，该命令不能在 DSC 集群处于启动、故障处理或故障节点重加入过程中进行。

6. halt css ep\_seqno

该命令用于使指定的 DMCSS 节点故障，ep\_seqno 为 DMCSS 节点号。控制节点可以将 ep\_seqno 设置为任意需要故障的节点号；非控制节点只能将 ep\_seqno 设置为自身节点号，如果设置 ep\_seqno 为非自身节点号，则会报错。

7. exit

退出 DMCSS。

## 5.11 注意事项

如果节点 A 的 DMCSS 退出或者故障，活动 DMCSS 会给节点 A 上所监控的 DMASMSVR 和 DMSERVER 发送 halt 命令，确保节点 A 上的 DMASMSVR 和 DMSERVER 自动退出。

单站点 ASM 也支持启动 css，但单站点 css 仅支持状态监控功能，在检测到单站点 ASM/DB 节点故障后，自动拉起故障节点。单站点 css 和其连接的 cssm 也仅支持执行 show 命令和自动拉起相关命令。