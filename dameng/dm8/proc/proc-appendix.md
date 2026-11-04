---
title: "附录"
book: "DM8 PROC 使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/proc-appendix.html
tags:
  - dameng
  - dm8
  - proc
---

运行预编译命令行工具 dpc\_new.exe 时，可能会就预编译过程中的一些错误进行报错提示。

错误码码值域如下：

1）dpc 警告错误码值域为：（100,103）

2）dpc 错误错误码值域为：（-30000, -30028）

表dpc错误码

| **名称** | **代码** | **解释** |
| --- | --- | --- |
| DPC\_WARN\_NO\_DATA | 100 | 没有数据 |
| DPC\_WARN\_STR\_TRUNC | 101 | 字符串截断 |
| DPC\_EC\_INVALID\_ITEM\_AREA | 103 | 描述空间不足 |
| DPC\_EC\_INVALID\_CURSOR\_STATUS | \-30001 | 无效的游标状态 |
| DPC\_EC\_MEMORY\_ALLOC\_FAIL | \-30002 | 内存分配失败 |
| DPC\_EC\_INVALID\_PARAM\_INDEX | \-30003 | 无效的参数信息，参数过大 |
| DPC\_EC\_DESC\_ALREADY\_EXISTS | \-30004 | 描述符已存在 |
| DPC\_EC\_DESC\_NOT\_EXISTS | \-30005 | 描述符信息不存在 |
| DPC\_EC\_INVALID\_PREPARE\_NAME | \-30006 | 无效的 Prepare 名称 |
| DPC\_EC\_OUT\_OF\_MEMORY | \-30007 | 内存不足 |
| DPC\_EC\_INVALID\_PARAM\_TYPE | \-30008 | 无效的参数类型 |
| DPC\_EC\_INVALID\_CONDITION\_NUM | \-30009 | 无效的序号 |
| DPC\_EC\_PRE\_STMT\_NOT\_CUR\_SPEC | \-30010 | 未指定游标 |
| DPC\_EC\_INVALID\_PRE\_STATEMENT | \-30011 | 无效的句柄 |
| DPC\_EC\_NOT\_MATCH\_COL | \-30012 | 列不匹配 |
| DPC\_EC\_NOT\_MATCH\_PARAM | \-30013 | 参数不匹配 |
| DPC\_EC\_PARAM\_NEED\_DATA | \-30014 | 需要数据 |
| DPC\_EC\_INVALIAD\_COUNT | \-30015 | COUNT 不合法 |
| DPC\_EC\_INVALIAD\_INDICATOR\_TYPE | \-30016 | 无效的指示符类型 |
| DPC\_EC\_UNDECLARED\_CONTEXT | \-30017 | CONTEXT 未被声明 |
| DPC\_EC\_INVALID\_CONTEXT | \-30018 | 无效的 CONTEXT |
| DPC\_EC\_CONTEXT\_NUMBER\_LIMIT | \-30019 | CONTEXT 数目达到上限 |
| DPC\_EC\_INVALIAD\_OBJECT | \-30020 | 无效的对象 |
| DPC\_EC\_CONN\_CLOESD | \-30021 | 连接已关闭 |
| DPC\_EC\_CONN\_FAILED | \-30022 | 连接失败 |
| DPC\_EC\_VARCHAR\_BUF\_NEED | \-30023 | 无效的变长字符长度 |
| DPC\_EC\_CONN\_LEN\_INVALID | \-30024 | 连接名长度不能大于 128 |
| DPC\_EC\_INVALID\_PARAM | \-30025 | 无效的参数 |
| DPC\_EC\_INVALID\_INDICATE\_PTR | \-30026 | 无效指示符指针 |
| DPC\_EC\_STR\_TRUNC | \-30027 | STR 绑定值 \[参数名\] 的结尾 Null 字符缺失 |
| DPC\_EC\_INVALID\_BATCH\_SIZE | \-30028 | 无效的批量大小\[参数值\] |