---
title: "锁表"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577908.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 锁表

#### 注意

当指定 `WAIT integer` 时，语句执行的超时时间取决于 `integer` 、[ob_query_timeout](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015911) 及 [ob_trx_timeout](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015962) 的值，并以三者中的最小值作为语句执行的实际超时时间。例如，指定 `WAIT 10`，且 `ob_query_timeout`、`ob_trx_timeout`均为默认值，则等待锁冲突的超时时间为 1000000 us 即 1s。

#### 注意

当指定 `WAIT integer` 时，语句执行的超时时间取决于 `integer` 、[ob_query_timeout](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015911) 及 [ob_trx_timeout](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015962) 的值，并以三者中的最小值作为语句执行的实际超时时间。例如，指定 `WAIT 10`，且 `ob_query_timeout`、`ob_trx_timeout`均为默认值，则等待锁冲突的超时时间为 1000000 us 即 1s。
