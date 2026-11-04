---
title: "附录 PRO*C错误码汇编"
book: "DM7 PROC使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/PROC使用手册.htm"
tags:
  - dameng
  - dm7
  - proc
---

运行预编译命令行工具`dpc_new.exe`时，可能会就预编译过程中的一些错误进行报错提示。

错误码码值域如下：

1）`dpc`警告 错误码值域为：（`100,103`）

2）`dpc`错误 错误码值域为：（`-30000, -30015`）

表 `dpc`错误码

| 名称 | 代码 | 解释 |
| --- | --- | --- |
| DPC_WARN_NO_DATA | 100 | 没有数据 |
| DPC_WARN_STR_TRUNC | 101 | 字符串截断 |
| DPC_EC_INVALID_ITEM_AREA | 103 | 描述空间不足 |
| DPC_EC_STR_TRUNC | -30000 | 绑定字符参数截断 |
| DPC_EC_INVALID_CURSOR_STATUS | -30001 | 无效的游标状态 |
| DPC_EC_MEMORY_ALLOC_FAIL | -30002 | 内存分配失败 |
| DPC_EC_INVALID_PARAM_INDEX | -30003 | 无效的参数信息，参数过大 |
| DPC_EC_DESC_ALREADY_EXISTS | -30004 | 描述符已存在 |
| DPC_EC_DESC_NOT_EXISTS | -30005 | 描述符信息不存在 |
| DPC_EC_INVALID_PREPARE_NAME | -30006 | 无效的Prepare名称 |
| DPC_EC_OUT_OF_MEMORY | -30007 | 内存分配错误 |
| DPC_EC_INVALID_PARAM_TYPE | -30008 | 无效的参数类型 |
| DPC_EC_INVALID_CONDITION_NUM | -30009 | 无效的序号 |
| DPC_EC_PRE_STMT_NOT_CUR_SPEC | -30010 | 当前语句没有结果集 |
| DPC_EC_INVALID_PRE_STATEMENT | -30011 | 无效的准备语句 |
| DPC_EC_NOT_MATCH_COL | -30012 | 列不匹配 |
| DPC_EC_NOT_MATCH_PARAM | -30013 | 参数不匹配 |
| DPC_EC_PARAM_NEED_DATA | -30014 | 参数需要数据 |
| DPC_EC_INVALIAD_COUNT | -30015 | 无效的个数 |
