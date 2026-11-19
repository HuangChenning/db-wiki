---
title: "DBMS_XPROFILE 概述"
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286772.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# DBMS_XPROFILE 概述

`DBMS_XPROFILE` 系统包是性能分析工具包，用于深度解析 SQL 执行过程中的资源消耗和算子级性能指标。

## DBMS_XPROFILE 权限说明

拥有执行 PL SQL 权限的用户可以使用该功能。

## DBMS_XPROFILE 子程序概览

下表列出了 OceanBase 数据库当前版本所支持的 `DBMS_XPROFILE` 子程序和简要描述。

| 子程序 | 描述 |
|--------|------|
| [DISPLAY_PROFILE](200.display-profile-of-mysql-mode.md)| 用于展示 SQL 执行计划的性能分析数据，可查看指定 `trace_id` 对应的执行的算子级诊断信息。|
