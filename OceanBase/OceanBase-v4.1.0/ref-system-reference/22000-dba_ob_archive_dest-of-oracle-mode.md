---
title: DBA_OB_ARCHIVE_DEST
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700777.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# DBA_OB_ARCHIVE_DEST

## 功能
展示归档路径配置。
## 字段说明

| 字段名称 | 类型 | 是否可以为 NULL | 描述 |
| --- | --- | --- | --- |
| DEST_NO | NUMBER(38) | NO | 标识 log_archive_dest_n |
| NAME | VARCHAR2(1024) | NO | 字段名 |
| VALUE | VARCHAR2(4096) | NO | 字段值 |
