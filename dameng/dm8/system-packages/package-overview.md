---
title: "概述"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/package-overview.html
tags:
  - dameng
  - dm8
  - system-packages
---

本文档主要介绍达梦支持的系统包功能、相关方法和举例说明等。包括 DBMS\_ALERT、DBMS\_OUTPUT、UTL\_FILE 和 UTL\_MAIL 等系统包。

## 1 概述

## 1.1 系统包创建、删除语句

DM 在新建库第一次启动服务器时会自动创建所有系统包。

用户也可以通过调用系统过程来创建、删除指定系统包：一是创建、删除指定的系统包；二是创建、删除所有系统包。用户须具有 DBA 角色权限。

> **注意**
> 
> **SP\_INIT\_XXX\_SYS()，SP\_CREATE\_SYSTEM\_PACKAGES()使用限制  
> 1.不能在MPP全局模式下的存储过程中直接调用，在MPP LOCAL模式下可在存储过程中直接调用；  
> 2.不能在存储过程中带参数进行动态调用**

## 1.2 创建、删除指定的包

SP\_CREATE\_SYSTEM\_PACKAGES 用来创建或删除指定的系统包。：一是 SP\_INI\_XXX\_SYS(create\_flag)；二是 SP\_CREATE\_SYSTEM\_PACKAGES(create\_flag, pkgname)。

### 1.2.1 使用 SP\_INIT\_XXX\_SYS()语句

使用 SP\_INI\_XXX\_SYS 过程创建或删除指定的系统包。该方法仅支持 DBMS\_JOB、DBMS\_WORKLOAD\_REPOSITORY、DBMS\_SCHEDULER 和 DBMS\_RLS 包。

这些系统包和创建语句对应关系如下：

| **包名** | 创建语句 SP\_INIT\_XXX\_SYS() |
| --- | --- |
| DBMS\_JOB | SP\_INIT\_JOB\_SYS(create\_flag); |
| DBMS\_WORKLOAD\_REPOSITORY | SP\_INIT\_AWR\_SYS(create\_flag); |
| DBMS\_SCHEDULER | SP\_INIT\_DBMS\_SCHEDULER\_SYS(create\_flag); |
| DBMS\_RLS | SP\_INIT\_RLS\_SYS(create\_flag); |

SP\_INIT\_XXX\_SYS()详细介绍如下：

**语法如下：**

```
SP_INIT_JOB_SYS(CREATE_FLAG  INT);
SP_INIT_AWR_SYS(CREATE_FLAG  INT);
SP_INIT_DBMS_SCHEDULER_SYS(CREATE_FLAG  INT);
SP_INIT_RLS_SYS(CREATE_FLAG INT);
```

**参数详解**

- CREATE\_FLAG

为 1 时表示创建对应的系统包；为 0 表示删除对应的系统包。

**返回值**

无。

**举例说明**

例 创建 DBMS\_JOB 包。

```
SP_INIT_JOB_SYS(1);
```

### 1.2.2 使用 SP\_CREATE\_SYSTEM\_PACKAGES()语句

SP\_CREATE\_SYSTEM\_PACKAGES 用来创建或删除指定的系统包。除了使用 SP\_INIT\_XXX\_SYS 建、删除的系统包之外，均可使用 SP\_CREATE\_SYSTEM\_PACKAGES 创建或删除。

SP\_CREATE\_SYSTEM\_PACKAGES()的详细介绍如下：

**语法如下：**

```
SP_CREATE_SYSTEM_PACKAGES (
    CREATE_FLAG        INT,
    PKGNAME            VARCHAR(128)
)
```

**参数详解**

- CREATE\_FLAG

为 0 时表示删除指定的系统包；为 1 时表示创建指定的系统包；为 2 时表示仅重建指定的系统包定义，即包头和包体，不会重建关联的包系统表、包关联对象（例如：包中的数据类型）等。

- PKGNAME

指定要创建的包名。

**返回值**

无。

**举例说明**

例 创建 DBMS\_LOB 系统包。

```
SP_CREATE_SYSTEM_PACKAGES(1, 'DBMS_LOB');
```

## 1.3 创建、删除所有系统包

SP\_CREATE\_SYSTEM\_PACKAGES 用来创建或删除所有系统包，其中不包含 DBMS\_JOB、DBMS\_WORKLOAD\_REPOSITORY、DBMS\_SCHEDULER 和 DBMS\_RLS 包。若在创建过程中某个系统包由于特定原因未能创建成功，会跳过继续创建后续的系统包。

**语法如下：**

```
SP_CREATE_SYSTEM_PACKAGES (
    CREATE_FLAG        INT
)
```

**参数详解**

- CREATE\_FLAG

为 0 时表示删除所有系统包；为 1 时表示创建所有系统包，不包括 UTL\_MAIL；为 2 时表示仅重建所有系统包的定义，即包头和包体，不会重建关联的包系统表、包关联对象（例如：包中的数据类型）等，不包括 UTL\_MAIL。

**返回值**

无。

**举例说明**

例 创建所有系统包（不包括 UTL\_MAIL）。

```
SP_CREATE_SYSTEM_PACKAGES (1);
```

## 1.4 检测系统包是否启用

1. **SF\_CHECK\_SYSTEM\_PACKAGES**

SF\_CHECK\_SYSTEM\_PACKAGES 用来检测系统包的启用状态。系统包的启用状态由是否执行过 SP\_CREATE\_SYSTEM\_PACKAGES(1)过程决定，若执行过，则状态为已启用。

**语法如下：**

```
INT
SF_CHECK_SYSTEM_PACKAGES()
```

**返回值**

0：未启用；1：已启用

**举例说明**

获得系统包的启用状态。

```
SELECT SF_CHECK_SYSTEM_PACKAGES();
```
2. **SF\_CHECK\_SYSTEM\_PACKAGE**

SF\_CHECK\_SYSTEM\_PACKAGE 可用来检查某个特定的系统包是否启用。

**语法如下：**

```
INT
SF_CHECK_SYSTEM_PACKAGE(
    PACKAGE_NAME        VARCHAR
)
```

**返回值**

0：未启用；1：已启用

**举例说明**

例 获得系统包 DBMS\_SCHEDULER 的启用状态。

```
SELECT SF_CHECK_SYSTEM_PACKAGE('DBMS_SCHEDULER');
```

## 1.5 包间依赖关系

部分系统包之间有依赖关系，被依赖包一旦被删除，依赖包就会失效。在 DPC 环境下创建系统包时，若未创建系统包所依赖的包就直接创建系统包，建包语句在 MP 节点执行后，将在该节点打印警告信息，不会向 SP 节点返回警告信息，此时，SP 节点虽然收到了最终执行语句成功的消息，但实际上该系统包没有创建成功。

针对以下存在依赖关系的系统包，当用户创建这些系统包时，系统会自动创建它们所依赖的包：

- DBMS\_ALERT 依赖 DBMS\_LOCK 和 DBMS\_UTILITY
- DBMS\_METADATA 依赖 DBMS\_LOB 和 UTL\_RAW
- DBMS\_LOB 依赖 UTL\_RAW
- DBMS\_XMLGEN 依赖 DBMS\_LOB
- UTL\_I18N 依赖 UTL\_RAW
- DBMS\_AQ 依赖 DBMS\_AQADM
- DBMS\_SQL 依赖 DBMS\_LOB
- DBMS\_DDL 依赖 DBMS\_SQL

针对以下存在依赖关系的系统包，用户需要先手动创建它们所依赖的包，然后才能成功创建这些系统包：

- DBMS\_PIPE 依赖 DBMS\_XMLGEN