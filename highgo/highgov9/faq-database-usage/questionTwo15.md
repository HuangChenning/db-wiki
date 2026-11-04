---
title: "游标使用报错问题"
book: "数据库使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionTwo15.html"
tags:
  - highgo
  - highgo-v9
  - faq-database-usage
---

### 错误现象

- **错误信息** ： `maximum open cursors exceeded`
- **出现场景** ：分页存储过程中使用了游标，但由于打开的游标数量超过了数据库允许的最大值，导致报错。

---

### 原因分析

- 瀚高数据库 V9 版本中， **默认游标打开数（open\_cursors）为 50** 。
- 当分页存储过程并发执行或一次性打开过多游标时，容易超出该限制，从而引发上述错误。

---

### 解决方法

通过调整数据库参数 `open_cursors` 来增加允许打开的游标数量。

#### 参数说明

- **参数名** ： `open_cursors`
- **默认值** ：50
- **取值范围** ：0 ～ 65535
- **作用** ：控制单个会话同时最多能打开的游标数量。

---

### 配置步骤

#### 1\. 修改参数值

执行以下 SQL 命令，将 `open_cursors` 的值修改为 200（可根据实际服务器资源配置适当调整，不宜过大）：

```sql
alter system set open_cursors to 200;
```

#### 2\. 使配置生效

执行以下命令重新加载配置文件，使修改生效：

```sql
select pg_reload_conf();
```

---

### 注意事项

- **配置值不宜过大** ：需根据服务器内存、并发量等资源情况合理设置，避免因游标过多占用系统资源。
- **生效方式** ：使用 `pg_reload_conf()` 可在不重启数据库的情况下使参数生效。
- **适用版本** ：瀚高数据库 V9。