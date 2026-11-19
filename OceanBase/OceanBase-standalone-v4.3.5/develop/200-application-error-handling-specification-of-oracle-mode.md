---
title: "Oracle 兼容应用错误处理规范"
book: "应用开发"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578128.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# Oracle 兼容应用错误处理规范

#### 注意

对于这些 `OBE-00600` 错误码，应用程序需要从错误消息中提取具体的内部错误码。通过下面的格式化字符串，提取占位符 \`%d\` 位置的整数，即为内部错误码。
