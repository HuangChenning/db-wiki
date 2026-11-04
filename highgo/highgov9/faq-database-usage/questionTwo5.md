---
title: "常用psql命令"
book: "数据库使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionTwo5.html"
tags:
  - highgo
  - highgo-v9
  - faq-database-usage
---

在 瀚高V9 中，psql 是官方提供的交互式命令行客户端工具，功能强大，不仅支持标准 SQL，还提供大量元命令（以反斜杠 \\ 开头），用于数据库管理、对象查看、格式化输出等。以下是 瀚高V9 中最常用、最实用的 psql 命令分类整理，适合开发、DBA 和运维人员日常使用。

## 一、连接与会话管理

| **命令** | **说明** |
| --- | --- |
| psql -U username -d dbname -h host -p port | 连接数据库（命令行方式） |
| \\conninfo | 显示当前连接信息（用户、数据库、主机、端等） |
| \\c dbname \[username\] | 切换到另一个数据库（或用户）例：\\c mydb admin |
| \\q | 退出（等价于quit或者exit） |

## 二、查看数据库对象（\\d系列）

所有\\d命令都支持通配符（如\\dt abc\*）

| **命令** | **说明** |
| --- | --- |
| \\l\[+\] | 列出所有数据库（+显示更多详情如大小、编码） |
| \\dn\[+\] | 列出所有schema |
| \\dt\[+\] \[pattern\] | 列出表（tables） |
| \\dv\[+\] \[pattern\] | 列出视图（views） |
| \\ds\[+\] \[pattern\] | 列出序列（sequences） |
| \\df\[+\] \[pattern\] | 列出函数（functions） |
| \\di\[+\] \[pattern\] | 列出索引（indexes） |
| \\dS\[+\] \[pattern\] | 列出系统表 |
| \\d table\_name | 查看表结构（字段、类型、约束、索引等）最常用！ |
| \\d+ table\_name | 查看表结构 + 注释、存储参数等 |

## 三、查询执行与调试

| **命令** | **说明** |
| --- | --- |
| \\x | **切换扩展显示模式** （行列转置，适合宽表查看）强烈推荐！ |
| \\timing | 开启/关闭SQL执行时间统计（显示耗时）调优必备 |
| \\gdesc | 只显示查询结果的列名和类型，不执行查询，调试神器！例：SELECT 1 AS id, now() AS ts \\gdesc; |

## 四、输入与输出控制

| **命令** | **说明** |
| --- | --- |
| \\o filename | 将后续查询结果输出到文件(\\o取消) |
| \\pset null ‘NULL’ | 设置为NULL值显示为‘NULL’（默认空白） |
| \\pset format aligned/tabular/csv | 设置输出格式（对其/表格/CSV） |
| \\pset pager off | 关闭分页（避免长结果卡住） |
| \\i script.sql | SQL 脚本文件 |
| \\e | 在编辑器中打开当前查询（需设置环境变量) |

## 五、事务与配置

| **命令** | **说明** |
| --- | --- |
| begin;   commit;   rollback; | 标准sql事务控制 |
| \\set AUTOCOMMIT off; | 关闭自动提交（进入手动事务模式） |
| SHOW shared\_buffers; | 查看参数（SQL命令，非psql元命令） |
| SET work\_mem = ‘64MB’; | 会话级参数设置 |

## 六、实用技巧 & 高频组合

### 快速查看表结构 + 注释

```sql
\d+ users
```

### 导出表为 CSV

```sql
\copy (SELECT * FROM users) TO '/tmp/users.csv' WITH CSV HEADER;
-- 注意：\copy 使用客户端权限，COPY 需要超级用户
```

### 查看慢查询（结合 pg\_stat\_statements）

```sql
\timing
SELECT query, total_exec_time FROM pg_stat_statements ORDER BY total_exec_time DESC LIMIT 5;
```

### 查看当前活跃会话

```sql
SELECT pid, usename, application_name, state, query 
FROM pg_stat_activity 
WHERE state <> 'idle';
```

## 七、环境变量与配置文件

~/.bash\_profile：psql 启动时自动执行的配置文

常用环境变量：

```sql
export PATH=/home/highgo/hgdb-v9.0/bin:$PATH
export PGHOME=/home/highgo/hgdb-v9.0
export PGDATA=$PGHOME/data
export PGDATABASE=highgo
export PGUSER=highgo
export PGPORT=1521
export PGPASSWORD=yourpass  # 不安全，建议用 ~/.pgpass
```

## 八、安全提示

避免在命令行中直接写密码（会留在历史记录）正确做法：使用~/.pgpass文件（权限600）

```sql
hostname:port:database:username:password
```

## 总结：高频命令速查表

| **场景** | **命令** |
| --- | --- |
| 连接数据库 | psql -U user -d db |
| 查看表结构 | \\d table\_name |
| 切换数据库 | \\c newdb |
| 显示执行时间 | \\timing |
| 行列转置显示 | \\x |
| 退出 | \\q |
| 执行脚本 | \\i script.sql |
| 导出CSV | \\copy (query) TO ‘file.csv’ CSV HEADER |
| 查看数据库列表 | \\l |

记住：所有/开启的命令都是psql元命令，不需要分号结尾；而sql语句需要分号（;）结束