---
title: "资源管理"
book: "安全指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeOne13.html"
tags:
  - highgo
  - highgo-v9
  - safety-security-guide
---

## 资源管理

资源管理模块是负责管理和优化数据库系统内部各种资源使用的关键部分，旨在提高数据库性能和效率。瀚高数据库管理系统V9支持CPU、并发事务和磁盘I/O（输入/输出操作）的资源管理。CPU资源限制是指对进程等计算实体可以使用的CPU资源量进行控制。这种限制对于确保系统稳定性、优化性能和实现公平的资源共享非常重要；并发事务限制指在多用户环境中，多个用户可能同时尝试访问或修改相同的数据，通过锁机制、事务管理和其他并发控制策略来保证数据的一致性和完整性；磁盘I/O资源限制指的是在存储系统中对数据读写速度的物理和技术限制。这些限制可以影响到整个系统的性能，特别是在高负载或高性能需求的情况下。

瀚高数据库使用资源组来管理和保护系统中CPU、并发事务限制和磁盘I/O的资源分配。定义资源组后，您可以将该组分配给一个或多个瀚高数据库用户，以便控制它们使用的资源。

注意

1.启用资源管理模块需要首先确认系统中是否已安装了libcgroup  
libcgroup-tools依赖，并正确配置cgroup功能。

2.磁盘IO的限制需要用到cgroup V2版本。

3.本模块仅支持在PostgreSQL兼容模式下进行资源管理操作。

## 资源管理开关

瀚高数据库中对资源管理模块设置了开关。资源管理功能打开时，我们创建的资源组才会生效。超级用户或拥有sysdba\_role角色的数据库管理员有权限通过ALTER  
SYSTEM SET方式配置资源管理相关参数。

pg\_resource\_manager为设置资源管理功能是否开启的总开关，取值为none和group、group-v2，缺省为none，参数需要重启服务生效。

- none表示关闭资源管理功能；
- group表示支持CPU、并发事务资源管理；
- group-v2表示支持CPU、并发事务和磁盘I/O资源管理。

## 资源管理参数配置

| 参数 | 生效方式 | 参数含义及合法取值 |
| --- | --- | --- |
| pg\_resource\_group\_queuing\_timeout | 立即 | 事务在资源组中排队的超时时间单位毫秒 |
| pg\_resource\_group\_bypass | 立即 | 查询是否可绕过资源组的限制on：启用off：禁用（默认） |
| pg\_resource\_group\_bypass\_catalog\_query | 立即 | 所有专门从系统catalog表中读取的查询是否可绕过资源组的并发事务限制on：启用（默认）off：禁用 |
| pg\_resource\_group\_cpu\_limit | 重启 | 标识要分配给每个主机上的资源组的系统CPU资源的最大百分比，默认90% |

## 资源组

瀚高数据库提供资源管理模块，资源管理模块以资源组为单位管理数据库的资源分配，通过使用资源组来管理和保护DBMS中CPU、并发事务限制和磁盘I/O资源。资源管理模块的使用，需要先使用操作系统root用户完成Linux控制组cgroup功能的正确配置和启动。

数据库管理员可以将资源组分配给数据库系统的角色/用户。多个角色/用户共同使用所属资源组的可用资源。当用户执行查询时，数据库系统根据资源组的限制来评估查询。如果尚未达到组的资源限制，而且查询不会导致组超过资源限制，数据库系统会立即运行查询。如果可用资源不满足查询，必须等到其他查询完成后才能运行。当资源组的限制更改为足够大的值时，数据库系统也可能会运行挂起的查询。

资源管理模块提供了三个默认资源组，分别为admin\_group、default\_group和system\_group。

- sadmin\_group管理员用户资源组
- default\_group其他未明确分配的角色资源组
- system\_group系统进程资源组

## 资源组限制

### CPU

瀚高数据库利用Linux控制组cgroup功能来实施CPU资源管理。启用CPU的资源分配时，需要在操作系统中开启cgroup功能。

可采用以下两种方式分配CPU资源：

- 通过将一定百分比的CPU资源分配给资源组。
- 通过将特定的CPU内核分配给资源组。

一个资源组只能同时使用一种分配模式，不同的资源组可同时采用两种CPU资源分配模式。使用CPUSET属性可标识出要为资源组保留的CPU核数，为资源组配置CPUSET属性时，会停用该组的CPU\_MAX\_PERCENT和CPU\_WEIGHT属性，并将CPU\_MAX\_PERCENT的值设置为-1。但是尽管瀚高数据库将您分配给资源组的CPU核专门用于该组，但这些CPU核也可能会被系统中的非瀚高数据库进程使用。

使用CPU\_MAX\_PERCENT属性配置资源组可以按百分比分配CPU资源。使用参数CPU\_WEIGHT属性来分配当前组的调度优先级，默认值为100，取值范围为1到500，该值指定资源组中任务可用的相对CPU时间份额。例如，您可以设置参数CPU\_WEIGHT来分配当前组的调度优先级。默认值为100，取值范围为1到500。该值指定资源组中任务可用的相对CPU时间份额。例如，如果一个资源组的相对份额为100，而另外两个资源组的相对份额为50，那么当所有资源组中的进程都尝试使用100%的CPU时（意味着所有资源组的CPU\_MAX\_PERCENT值都设置为100），第一个资源组将获得50%的CPU时间，另外两个资源组各获得25%的CPU时间。但是，如果添加另一个相对份额为100的组，则第一个组只允许使用33%的CPU，其余组分别获得16.5%、16.5%和33%的CPU。

### 并发事务

在角色/用户所属的资源组中，事务处理按先进先出的原则进行评估。数据库系统会定期评估系统的活动工作负载，根据需要重新分配资源并启动/排队事务。

### 磁盘I/O

瀚高数据库支持磁盘I/O限制，参数IO\_LIMIT限制了分配给特定资源组的查询的最大读/写磁盘I/O吞吐量和每秒最大读/写I/O操作。它分配带宽，确保高优先级资源组的使用，并避免过度使用磁盘带宽。磁盘I/O的分配基于Linux的控制组cgroup功能，且需要版本cgroupv2才可正常使用。cgroups有两个版本，其中Enterprise  
Linux8及更低版本默认带有cgroupv1，Enterprise  
Linux9及更高版本默认带有cgroupv2。限制资源组中最大读写磁盘I/O吞吐量的rbps和wbps值，以MB/秒为单位。默认值为-1，代表没有限制。riops和wiops的值用于限制资源组中每秒的最大读写I/O操作次数。默认值为-1，代表没有限制。参数IO\_LIMIT的值是基于每个表空间设置的。

## 创建资源组

创建资源组的语法如下：

```
CREATE RESOURCE GROUP name WITH (group_attribute=value[,...])
```

group\_attribute资源组的可用限制：

| 字符序 | 所属字符集 | 说明 |  |
| --- | --- | --- | --- |
| CONCURRENCY | 最大并发事务数 | \0- [max\_connections\] | 20 |
| CPU\_MAX\_PERCENT | 可使用CPU资源最大百分比 | \[1-100\] | \-1(无限制) |
| CPU\_WEIGHT | 使用CPU资源的优先级 | \[1-500\] | 100 |
| CPUSET | 资源组保留CPU逻辑内核，或逻辑线程 | 系统core数量 | \-1 |
| IO\_LIMIT | 磁盘I/O操作的限制；wbps：写入带宽，反映磁盘写入数据的速度；rbps：读取带宽，反映磁盘读取数据的速度；wiops：写入iops，反映磁盘执行随机写入操作的频率；riops：读取iops，反映磁盘执行随机读取操作的频率；如果配置了 wbps=10485760，这意味着磁盘的写入带宽被限制为 10MB/s | \[2-4294967295or max\] | \-1 |

创建资源组示例：

创建一个名为rgroup1的资源组，最大并发事务数为20，可用CPU资源最大百分比为20，CPU优先级为500，pg\_default表空间的磁盘I/O限制：

```
highgo=# create resource group rgroup1 with(

concurrency=20,

cpu_max_percent=20,

cpu_weight=500,

io_limit='pg_default:wbps=1000,rbps=1000,wiops=100,riops=100');

CREATE RESOURCE GROUP
```

需要注意的是，执行该语句时会给出告警信息，因为磁盘IO限制需要用到cgroup  
V2版本。

## 修改资源组

修改资源组语法,使用ALTERR ESOURCE GROUP命令更新资源组的限制。

```
修改资源组的语法如下：

ALTER RESOURCE GROUP group_name SET (group_attribute=value[,...])

修改资源组示例：

服务器有4个核的话，cpu号分是 0 1 2 3，将1,2,3号CPU分配给rgroup1：

highgo=# alter resource group rgroup1 set cpuset '1,2,3';

修改磁盘IO限制：

highgo=# alter resource group rgroup1 set io_limit
'tbspace:wbps=2000,wiops=2000;tablespace2:rbps=2024,riops=2024';

修改最大并发事务数：

highgo=# alter resource group rgroup1 set concurrency 10;
```

## 删除资源组

删除资源组语法，可使用DROP RESOURCE  
GROUP命令删除资源组。要删除资源组之前，请确保要删除的资源组未分配给任何角色，资源组中无任何活动或等待的事务。

删除资源组的语法如下：

```
DROP RESOURCE GROUP group_name
```

删除资源组示例：

```
highgo=# drop resource group rgroup1;

DROP RESOURCE GROUP
```

## 查询资源组

瀚高数据库提供系列资源组配置信息视图，通过系统视图可监控资源组和查询事务状态。

```
查询所有资源组：

highgo=# select * from pg_resgroup;

查询所有资源组具体能力和限制：

highgo=# select * from pg_resgroupcapability;

查询角色/用户所属资源组：

highgo=# select * from pg_resgroup_role ;

查询资源组配置信息：

highgo=# select * from pg_resgroup_config;

查询资源组状态和活动（可显示正在运行和排队的事务）：

highgo=# select * from pg_resgroup_status;
```

## 管理资源组

### 指定所属资源组

提供资源组管理功能，支持指定某个角色或用户所属资源组。

示例：

指定角色/用户所属资源组

```
#创建用户时指定用户所属资源组：

highgo=# create user bella resource group rgroup1;

#修改用户所属资源组为rgroup1：

highgo=# alter role mary resource group rgroup1;
```

### 管理资源组中排队事务

支持查看与所有资源组中当前活动或等待的所有语句相关联的进程信息，并取消正在运行或排队的事务操作。通过调用pg\_cancel\_backend(pid  
int4)函数来结束该进程，即可手动取消资源组中正在运行或排队的事务。

示例：查询当前活动和在等待的进程信息，取消正在运行或排队的事务操作：

查询当前活动的和等待的进程信息：

```
highgo=# select oid, rolname, groupname, pid, state, wait_event,query

from pg_roles, pg_resgroup_status , pg_stat_activity
,pg_resgroupcapability

where pg_resgroup_status.groupid =pg_resgroupcapability.resgroupid

and pg_resgroupcapability.rgroleid= pg_roles.oid

and pg_stat_activity.usename=pg_roles.rolname;

取消排队事务：

highgo=# select pg_cancel_backend (2852); # 2852指的是事务pid
```

## 系统croup配置示例

1. 编辑/etc/cgconfig.conf，增加如下内容：
```
group highgo {

perm {

task {

uid = highgo;

gid = highgo;

}

admin {

uid = highgo;

gid = highgo;

}

}

cpu {

}

cpuacct {

}

cpuset {

}

memory {

}

}
```
2. 临时创建cgroup层次结构
```
cgconfigparser -l /etc/cgconfig.conf
```
3. 设置自启动：
```
systemctl enable cgconfig.service
```
4. 启动：
```
systemctl start cgconfig.service
```