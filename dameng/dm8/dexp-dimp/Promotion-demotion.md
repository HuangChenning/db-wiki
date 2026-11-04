---
title: "升级和降级"
book: "DM8 dexp 和 dimp 手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/Promotion-demotion.html
tags:
  - dameng
  - dm8
  - dexp-dimp
---

从 V8.1.2.69 版本开始，对创建用户口令新增了 < 加盐选项 >。< 加盐选项 > 包含 SALT 和 NO SALT，V8.1.2.69 及 V8.1.4.81（不包含 V8.1.4.81）之间的版本缺省为 NO SALT，V8.1.4.81 及以上版本缺省为 SALT。

因此，当遇到下面情景：先导出 V8.1.2.69 之后的口令加盐的库，再导入到 V8.1.2.69 之前不支持 < 加盐选项 > 的库中，将不能成功。解决办法：在导出之前，DBA 先检查待导出库用户口令是否使用了加盐 SALT。 如果是，那么 DBA 需要先使用 ALTER 语句将用户口令调整为 NO SALT，再做导出导入，保证前后版本的口令都是 NO SALT，即可操作成功。