---
title: "V$SYSTEM_EVENT"
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700817.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# V$SYSTEM_EVENT

V$SYSTEM_EVENT
===================================

## 功能

展示当前服务器上租户系统级别的一些等待事件，统计每一类等待事件的发生次数、等待时间、超时次数等。

## 字段说明

| **字段名称** | **类型** | **是否可以为 NULL** | **描述** |
| --- | --- | --- | --- |
| CON_ID | NUMBER | NO | 租户 ID |
| SVR_IP | VARCHAR2(46) | NO | 信息所在 Server 的 IP |
| SVR_PORT | NUMBER(38) | NO | 信息所在 Server 的端口号 |
| EVENT_ID | NUMBER | NO | 等待事件的 ID |
| EVENT | VARCHAR2(64) | NO | 等待事件的描述 |
| WAIT_CLASS_ID | NUMBER | NO | 等待事件的所属 Class ID |
| WAIT_CLASS# | NUMBER | NO | 等待事件的所属的 Class下标 |
| WAIT_CLASS | VARCHAR2(64) | NO | 等待事件所属的 Class |
| TOTAL_WAITS | NUMBER | NO | 该等待事件的总等待次数 |
| TOTAL_TIMEOUTS | NUMBER | NO | 该等待事件的总超时次数 |
| TIME_WAITED | NUMBER | NO | 该等待事件的总等待时间，单位为 10 ms |
| AVERAGE_WAIT | NUMBER | NO | 该等待事件的平均等待时间，单位为 10 ms |
| TIME_WAITED_MICRO | NUMBER | NO | 该等待事件的总等待时间（微秒） |
