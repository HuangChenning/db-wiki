---
title: "PL/SQL 性能问题定位最佳实践"
book: "开发"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000003967582.html"
tags:
  - oceanbase
  - best-practices
  - develop
---

# PL/SQL 性能问题定位最佳实践

#### 说明

由于当前 USER_SOURCE 表中存储的过程源码信息只有一行，在执行完 DBMS_PROFILER 分析后，数据与存储过程源码关联需要一个代理表。在 V4.4.2 版本，将会提供 USER_SOURCE 表，该表提供按照行拆分的 USER_SOURCE 视图，DBMS_PROFILER 后的数据可以与 USER_SOURCE 关联到具体的行。

#### 说明

系统触发器在 V4.2.5.bp1 开始支持。
