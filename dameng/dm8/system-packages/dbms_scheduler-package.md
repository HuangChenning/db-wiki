---
title: "DBMS_SCHEDULER 包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dbms_scheduler-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

DBMS\_SCHEDULER 包提供一系列调度相关的存储过程及方法供 PL/SQL 调用。

## 31.1 相关方法

### 31.1.1 SCHEDULE 对象

1. CREATE\_SCHEDULE 过程

创建一个调度。

**语法如下：**

```
PROCEDURE DBMS_SCHEDULER.CREATE_SCHEDULE(
    SCHEDULE_NAME        IN         VARCHAR,
    START_DATE            IN         TIMESTAMP WITH TIME ZONE DEFAULT NULL,
    REPEAT_INTERVAL        IN         VARCHAR,
    END_DATE            IN         TIMESTAMP WITH TIME ZONE DEFAULT NULL, 
    COMMENTS            IN         VARCHAR     DEFAULT NULL
);
```

**参数详解**

- SCHEDULE\_NAME
	调度名称。调度名称不区分大小写，要求在包模式下名称唯一。不能为空，若未设置，则报错。
- START\_DATE
	调度第一次有效日期或者时间。对于重复的调度，START\_DATE 是个参照值，这种情况 START\_DATE 不是调度的开始时间，调用的开始决定于 REPEAT\_INTERVAL 的设置。START\_DATE 用于决定调度的第一个实例。
- REPEAT\_INTERVAL
	调度重复间隔，用于指定调用隔多久重复一次。它是基于日历语法的表达式。对于命名的调度，REPEAT\_INTERVAL 不支持 PL/SQL 表达式。
- END\_DATE
	作业停止运行时间。如果为未设置，作业则一直有效。