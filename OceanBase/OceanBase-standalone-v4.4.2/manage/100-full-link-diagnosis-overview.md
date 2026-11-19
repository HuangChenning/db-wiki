---
title: "全链路追踪概述"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077307.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 全链路追踪概述

## 什么是全链路追踪？

OceanBase 数据库拥有复杂的调用链路。当出现超时问题时，往往无法快速定位是 OceanBase 内部组件或是网络的问题，运维人员只能根据经验和 observer 日志进行分析。为了提高诊断效率，本次更新引入了一种全新的全链路追踪机制，能够追踪用户 SQL 请求在数据库全链路过程中，在不同组件、不同阶段执行的相关信息，并以可视化方式展现给用户，从而帮助用户快速定位问题所在位置，旨在助力用户快速精准地发现组件内部问题。

### 全链路追踪路径

全链路追踪覆盖了主要的数据流路径，具体如下。

请求直接从应用程序通过客户端发送至 OBServer，然后结果直接返回。

全链路追踪的目的是对这两条路径上的所有组件进行问题定位。 用户可以通过客户端连接到 OceanBase 数据库，在客户端发送请求时，请求直接到达 OBServer。通过全链路追踪功能，运维人员可以使用 PL/SQL 的 [DBMS_MONITOR](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005287014) 包中的方法，根据需要控制和监控应用程序是否开启全链路跟踪（trace），以及跟踪信息的打印细节。

### 全链路追踪的日志

全链路追踪的日志，即跟踪日志（trace logs），它会根据数据访问路径来决定其记录细节。直接访问 OBServer，则只在 OBServer 的日志文件中记录。具体而言，OBServer 的命名为 `trace.log`。每个日志文件的大小限制为 256MB，当日志达到这一大小限制时，系统将创建新的日志文件，并将旧文件归档。归档文件的数量由配置项 [max_syslog_file_count](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286046) 控制，超出的文件将被自动删除。 运维人员可通过搜集和分析所有跟踪日志，来追踪每个事务或 SQL 查询在整个调用链路上的执行时间和其他相关信息。这不仅为问题的准确定位提供了重要线索，还大大提升了运维效率。
