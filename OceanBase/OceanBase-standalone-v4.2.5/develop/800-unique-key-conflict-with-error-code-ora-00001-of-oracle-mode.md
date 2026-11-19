---
title: "插入数据时提示重复的输入，错误代码 ORA-00001"
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702087.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 插入数据时提示重复的输入，错误代码 ORA-00001

#### 说明

- 您也可以通过 `MERGE INTO` 语句来避免唯一键冲突。详细操作步骤，请参见 [替换数据](400-replace-data-of-oracle-mode-in-develop.md)。
- 如果确定不需要保留已存在的行，可以根据条件将不需要的行删除。具体操作请参见 [删除数据](300-delete-data-of-oracle-mode-in-develop.md)。
