---
title: "mysql兼容模式适配问题"
book: "数据库使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionTwo10.html"
tags:
  - highgo
  - highgo-v9
  - faq-database-usage
---

本文档总结了在瀚高数据库（V9 版本）MySQL 兼容模式下常见的适配问题、原因分析及解决方案。

## 1\. SHOW 语法不支持

### 问题描述

在 MySQL 兼容模式下，若执行 `SHOW COLUMNS`, `SHOW TABLE STATUS`, `SHOW TRIGGERS` 等命令时，提示语法错误或不支持。

### 原因分析

手动升级至 V9.05 版本后，若直接拷贝了旧版本的 `data` 目录而未执行 `initdb` 或升级脚本，导致系统扩展库 `ivorysql_my` 中的兼容函数未创建。

### 解决方案

手动执行以下 SQL 脚本，创建缺失的兼容函数。

```sql
CREATE OR REPLACE FUNCTION ivymy.show_columns_internal(
  IN  tb_name char,
  IN  db_name char DEFAULT NULL,
  OUT "Field" varchar,
  OUT "Type" longtext,
  OUT "Collation" varchar,
  OUT "Null" varchar,
  OUT "Key" varchar,
  OUT "Default" longtext,
  OUT "Extra" varchar,
  OUT "Privileges" varchar,
  OUT "Comment" varchar)
RETURNS SETOF record AS $$
BEGIN
        IF db_name IS NOT NULL AND to_regclass(concat(db_name, '.', tb_name)) IS NULL THEN
                RAISE EXCEPTION 'Table ''%'' doesn''t exist', concat(db_name, '.', tb_name);
        END IF;

        IF db_name IS NULL AND to_regclass(tb_name) IS NULL THEN
                RAISE EXCEPTION 'Table ''%'' doesn''t exist', tb_name;
        END IF;

        IF db_name IS NULL THEN
                RETURN QUERY SELECT
                        COLUMN_NAME, COLUMN_TYPE, COLLATION_NAME, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA, PRIVILEGES, COLUMN_COMMENT
                FROM mys_information_schema.showcolumns
                WHERE table_name = tb_name
                ORDER BY ORDINAL_POSITION;
        ELSE
                RETURN QUERY SELECT
                        COLUMN_NAME, COLUMN_TYPE, COLLATION_NAME, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA, PRIVILEGES, COLUMN_COMMENT
                FROM mys_information_schema.showcolumns
                WHERE table_name = tb_name AND
                          table_schema = db_name
                ORDER BY ORDINAL_POSITION;
        END IF;
END
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION ivymy.show_columns_normal(
  IN  tb_name char,
  IN  db_name char DEFAULT NULL,
  OUT "Field" varchar,
  OUT "Type" longtext,
  OUT "Null" varchar,
  OUT "Key" varchar,
  OUT "Default" longtext,
  OUT "Extra" varchar)
RETURNS SETOF record AS $$
        SELECT
                field, type, "null", "key", "default", extra
        FROM ivymy.show_columns_internal(tb_name, db_name);
$$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION ivymy.show_columns_full(
  IN  tb_name char,
  IN  db_name char DEFAULT NULL,
  OUT "Field" varchar,
  OUT "Type" longtext,
  OUT "Collation" varchar,
  OUT "Null" varchar,
  OUT "Key" varchar,
  OUT "Default" longtext,
  OUT "Extra" varchar,
  OUT "Privileges" varchar,
  OUT "Comment" varchar)
RETURNS SETOF record AS $$
        SELECT
                field, type, "collation", "null", "key", "default", extra, privileges, comment
        FROM ivymy.show_columns_internal(tb_name, db_name);
$$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION ivymy.show_indexes(
  IN  tb_name char,
  IN  db_name char DEFAULT NULL,
  OUT "Table" varchar,
  OUT "Non_unique" bigint,
  OUT "Key_name" varchar,
  OUT "Seq_in_index" bigint,
  OUT "Column_name" varchar,
  OUT "Collation" varchar,
  OUT "Cardinality" bigint,
  OUT "Sub_part" bigint,
  OUT "Packed" varchar,
        OUT "Null" varchar,
        OUT "Index_type" varchar,
        OUT "Comment" varchar,
        OUT "Index_comment" varchar)
RETURNS SETOF record AS $$
BEGIN
        IF db_name IS NOT NULL AND to_regclass(concat(db_name, '.', tb_name)) IS NULL THEN
                RAISE EXCEPTION 'Table ''%'' doesn''t exist', concat(db_name, '.', tb_name);
        END IF;

        IF db_name IS NULL AND to_regclass(tb_name) IS NULL THEN
                RAISE EXCEPTION 'Table ''%'' doesn''t exist', tb_name;
        END IF;

        IF db_name IS NULL THEN
                RETURN QUERY SELECT
                        TABLE_NAME, NON_UNIQUE, INDEX_NAME, SEQ_IN_INDEX, COLUMN_NAME, "COLLATION",
                        CARDINALITY, SUB_PART, PACKED, NULLABLE, INDEX_TYPE, COMMENT, INDEX_COMMENT
                FROM mys_information_schema.showstatistics
                WHERE table_name = tb_name;
        ELSE
                RETURN QUERY SELECT
                        TABLE_NAME, NON_UNIQUE, INDEX_NAME, SEQ_IN_INDEX, COLUMN_NAME, "COLLATION",
                        CARDINALITY, SUB_PART, PACKED, NULLABLE, INDEX_TYPE, COMMENT, INDEX_COMMENT
                FROM mys_information_schema.showstatistics
                WHERE table_name = tb_name AND
                          index_schema = db_name;
        END IF;
END
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION ivymy.show_table_status(
        IN  db_name char DEFAULT NULL,
        OUT "Name" varchar,
        OUT "Engine" varchar,
        OUT "Version" uint8,
        OUT "Row_format" varchar,
        OUT "Rows" uint8,
        OUT "Avg_row_length" uint8,
        OUT "Data_length" uint8,
        OUT "Max_data_length" uint8,
        OUT "Index_length" uint8,
        OUT "Data_free" uint8,
        OUT "Auto_increment" uint8,
        OUT "Create_time" datetime,
        OUT "Update_time" datetime,
        OUT "Check_time" datetime,
        OUT "Collation" varchar,
        OUT "Checksum" uint8,
        OUT "Create_options" varchar,
        OUT "Comment" varchar)
RETURNS SETOF record AS $$
BEGIN
        IF db_name IS NOT NULL AND to_regnamespace(db_name) IS NULL THEN
                RAISE EXCEPTION 'Unknown database ''%''', db_name;
        END IF;

        IF db_name IS NULL THEN
                RETURN QUERY SELECT
                        "TABLE_NAME", "ENGINE", "VERSION", "ROW_FORMAT", "TABLE_ROWS", "AVG_ROW_LENGTH", "DATA_LENGTH",
                        "MAX_DATA_LENGTH", "INDEX_LENGTH", "DATA_FREE", "AUTO_INCREMENT", "CREATE_TIME", "UPDATE_TIME",
                        "CHECK_TIME", "TABLE_COLLATION", "CHECKSUM", "CREATE_OPTIONS", "TABLE_COMMENT"
                FROM mys_information_schema.showtables;
        ELSE
                RETURN QUERY SELECT
                        "TABLE_NAME", "ENGINE", "VERSION", "ROW_FORMAT", "TABLE_ROWS", "AVG_ROW_LENGTH", "DATA_LENGTH",
                        "MAX_DATA_LENGTH", "INDEX_LENGTH", "DATA_FREE", "AUTO_INCREMENT", "CREATE_TIME", "UPDATE_TIME",
                        "CHECK_TIME", "TABLE_COLLATION", "CHECKSUM", "CREATE_OPTIONS", "TABLE_COMMENT"
                FROM mys_information_schema.showtables
                WHERE table_schema = db_name;
        END IF;
END
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION ivymy.show_triggers(
        IN  db_name char DEFAULT NULL,
        OUT "Trigger" varchar,
        OUT "Event" varchar,
        OUT "Table" varchar,
        OUT "Statement" longtext,
        OUT "Timing" varchar,
        OUT "Created" datetime(2),
        OUT "sql_mode" varchar,
        OUT "Definer" varchar,
        OUT "character_set_client" varchar,
        OUT "collation_connection" varchar,
        OUT "Database Collation" varchar)
RETURNS SETOF record AS $$
BEGIN
        IF db_name IS NOT NULL AND to_regnamespace(db_name) IS NULL THEN
                RAISE EXCEPTION 'Unknown database ''%''', db_name;
        END IF;

        IF db_name IS NULL THEN
                RETURN QUERY SELECT
                        "TRIGGER_NAME", "EVENT_MANIPULATION", "EVENT_OBJECT_TABLE", "ACTION_STATEMENT",
                        "ACTION_TIMING", "CREATED", "SQL_MODE", "DEFINER", "CHARACTER_SET_CLIENT",
                        "COLLATION_CONNECTION", "DATABASE_COLLATION"
                FROM mys_information_schema.triggers;
        ELSE
                RETURN QUERY SELECT
                        "TRIGGER_NAME", "EVENT_MANIPULATION", "EVENT_OBJECT_TABLE", "ACTION_STATEMENT",
                        "ACTION_TIMING", "CREATED", "SQL_MODE", "DEFINER", "CHARACTER_SET_CLIENT",
                        "COLLATION_CONNECTION", "DATABASE_COLLATION"
                FROM mys_information_schema.triggers
                WHERE trigger_schema = db_name;
        END IF;
END
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION ivymy.show_databases(OUT "Database" varchar)
RETURNS SETOF varchar AS $$
        SELECT
                "SCHEMA_NAME"
        FROM mys_information_schema.schemata;
$$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION ivymy.show_processlist(
        OUT "Id" varchar,
        OUT "User" varchar,
        OUT "Host" varchar,
        OUT "db" varchar,
        OUT "Command" varchar,
        OUT "Time" varchar,
        OUT "State" varchar,
        OUT "Info" varchar)
RETURNS SETOF record AS $$
        SELECT
                "ID", "USER","HOST", "DB", "COMMAND", "TIME", "STATE", "INFO"
        FROM mys_information_schema.processlist;
$$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION ivymy.show_tables(
        IN db_name char DEFAULT current_schema())
RETURNS SETOF record AS $$
BEGIN
        IF db_name IS NOT NULL AND to_regnamespace(db_name) IS NULL THEN
                RAISE EXCEPTION 'Unknown database ''%''', db_name;
        END IF;

        RETURN QUERY
        SELECT
                "TABLE_NAME", "TABLE_TYPE"
        FROM mys_information_schema.tables
        WHERE table_schema = db_name;
END
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION ivymy.show_create_views(
        IN  view_name char,
        IN  db_name char DEFAULT current_schema(),
        OUT "View" varchar,
        OUT "Create View" varchar,
        OUT "character_set_client" varchar,
        OUT "collation_connection" varchar)
RETURNS SETOF record AS $$
DECLARE
        rkind char;
BEGIN
        IF to_regclass(concat(db_name, '.', view_name)) IS NULL AND
           to_regclass(view_name) IS NULL THEN
                RAISE EXCEPTION 'Table ''%'' doesn''t exist', concat(db_name, '.', view_name);
        END IF;

        SELECT relkind INTO rkind
        FROM pg_class
        WHERE
                relnamespace = to_regnamespace(db_name)::oid AND
                relname = view_name;

        IF rkind != 'v' THEN
                RAISE EXCEPTION '''%'' is not VIEW', concat(db_name, '.', view_name);
        END IF;

        RETURN QUERY SELECT
                v.TABLE_NAME AS "View",
                CASE WHEN c.relpersistence = 't'
                        THEN concat('CREATE TEMP VIEW ', v.TABLE_NAME, ' AS', v.VIEW_DEFINITION)
                ELSE
                        concat('CREATE VIEW ', v.TABLE_NAME, ' AS', v.VIEW_DEFINITION)
                END AS "Create View",
                v.CHARACTER_SET_CLIENT AS character_set_client,
                v.COLLATION_CONNECTION AS collation_connection
        FROM mys_information_schema.views v
        JOIN pg_catalog.pg_namespace n ON v.TABLE_SCHEMA = n.nspname
        JOIN pg_catalog.pg_class c ON v.TABLE_NAME = c.relname AND c.relnamespace = n.oid
        WHERE v.TABLE_SCHEMA = db_name AND
                  v.TABLE_NAME = view_name;
END
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION ivymy.show_create_table(
        IN  tb_name char,
        IN  db_name char DEFAULT current_schema(),
        OUT "Table" varchar,
        OUT "Create Table" varchar)
RETURNS SETOF record AS $$
DECLARE
        reloid  Oid;
BEGIN
        -- consider temp table
        IF to_regclass(concat(db_name, '.', tb_name)) IS NULL AND
           to_regclass(tb_name) IS NULL THEN
                RAISE EXCEPTION 'Table ''%'' doesn''t exist', concat(db_name, '.', tb_name);
        END IF;

        IF to_regclass(concat(db_name, '.', tb_name)) IS NOT NULL THEN
                reloid := to_regclass(concat(db_name, '.', tb_name))::oid;
        ELSE
                reloid := to_regclass(tb_name)::oid;
        END IF;

        RETURN QUERY SELECT
                tb_name::varchar as "Table",
                ivymy.mys_show_create_table(reloid)::varchar as "Create Table";
END
$$ LANGUAGE plpgsql;
```

---

## 2\. DATE\_FORMAT 函数不支持

### 问题描述

MySQL 的 `DATE_FORMAT` 函数在 V9 中默认不存在。

### 解决方案

创建兼容函数，将 MySQL 格式符转换为 PostgreSQL 的 `TO_CHAR` 格式。

```sql
-- 支持 TIMESTAMP 类型
CREATE OR REPLACE FUNCTION date_format(input_timestamp TIMESTAMP WITHOUT TIME ZONE, format_string TEXT)
RETURNS TEXT AS $$
DECLARE
    pg_format TEXT := format_string;
BEGIN
    -- 格式符转换映射
    pg_format := REPLACE(pg_format, '%Y', 'YYYY');
    pg_format := REPLACE(pg_format, '%y', 'YY');
    pg_format := REPLACE(pg_format, '%m', 'MM');
    pg_format := REPLACE(pg_format, '%c', 'FMmm');  -- 不补零月份
    pg_format := REPLACE(pg_format, '%d', 'DD');
    pg_format := REPLACE(pg_format, '%e', 'FMdd');  -- 不补零日期
    pg_format := REPLACE(pg_format, '%H', 'HH24');
    pg_format := REPLACE(pg_format, '%h', 'HH12');
    pg_format := REPLACE(pg_format, '%i', 'MI');
    pg_format := REPLACE(pg_format, '%s', 'SS');
    pg_format := REPLACE(pg_format, '%p', 'AM');
    pg_format := REPLACE(pg_format, '%%', '%');     -- 转义 %

    RETURN TO_CHAR(input_timestamp, pg_format);
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- 重载支持 TIMESTAMPTZ
CREATE OR REPLACE FUNCTION date_format(input_timestamptz TIMESTAMPTZ, format_string TEXT)
RETURNS TEXT AS $$
BEGIN
    -- 根据需求选择时区，此处示例转为 UTC，也可用 AT TIME ZONE current_setting('TimeZone')
    RETURN date_format(input_timestamptz AT TIME ZONE 'UTC', format_string);
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- 重载支持 DATE
CREATE OR REPLACE FUNCTION date_format(input_date DATE, format_string TEXT)
RETURNS TEXT AS $$
BEGIN
    RETURN date_format(input_date::TIMESTAMP, format_string);
END;
$$ LANGUAGE plpgsql IMMUTABLE;
```

---

## 3\. TO\_CHAR 函数兼容性增强

### 问题描述

虽然 `TO_CHAR` 是 PG 原生函数，但在某些 MySQL 兼容模式场景下，因参数类型匹配严格（如传入 `DATETIME` 别名），可能提示语法错误。

### ⚠️ 风险提示

**不建议直接在 **`pg_catalog`** schema 下创建或替换系统函数** ，这可能导致数据库升级冲突或内部组件异常。  
\*\* 推荐做法\*\*：确保应用连接时的 `search_path` 包含自定义兼容函数的 schema，或者仅在测试环境使用以下方案。

若必须在全局生效，可尝试以下重载（请谨慎评估生产环境风险）：

```sql
-- 重载 DATE 类型输入
CREATE OR REPLACE FUNCTION to_char(date, text) 
RETURNS text AS $$
    SELECT pg_catalog.to_char($1::pg_catalog.date, $2);
$$ LANGUAGE sql STRICT PARALLEL SAFE IMMUTABLE;

-- 重载 DATETIME (timestamp) 类型输入
CREATE OR REPLACE FUNCTION to_char(timestamp, text) 
RETURNS text AS $$
    SELECT pg_catalog.to_char($1::pg_catalog.timestamp, $2);
$$ LANGUAGE sql STRICT PARALLEL SAFE IMMUTABLE;

-- 测试
SELECT to_char(now(), 'YYYY-MM-DD HH24:MI:SS');
```

---

## 4\. AUTO\_INCREMENT (自增列) 适配

### 问题描述

V9 MySQL 兼容模式支持 `AUTO_INCREMENT` 属性，但使用迁移工具从 MySQL 迁移数据时，往往只迁移了表结构和数据，丢失了自增序列属性。

### 解决方案

手动为迁移后的表添加自增属性（Identity Column）。

```sql
-- 1. 假设已有表且无自增属性
CREATE TABLE test (id INT NOT NULL, name TEXT);
INSERT INTO test VALUES (1, 'Alice'), (2, 'Bob');

-- 2. 添加自增属性 (PostgreSQL 10+ 语法)
-- 注意：列必须定义为 NOT NULL，否则会报错
ALTER TABLE test ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY;

-- 3. 修复序列起始值 (防止主键冲突)
-- 将序列当前值设为表中最大的 ID
SELECT setval(
    pg_get_serial_sequence('test', 'id'),
    (SELECT MAX(id) FROM test)
);

-- 4. 验证
INSERT INTO test (name) VALUES ('Charlie'); -- id 应自动生成为 3
SELECT * FROM test;
```

**注意事项** ：

- 列必须是整数类型（如 `INT`, `BIGINT` ），不能是 `TEXT` 等。
- 列必须定义为 `NOT NULL` ，否则执行 `ADD GENERATED` 时会报错：\_错误：在添加标识之前，必须声明关系 “test” 的列 “id” 为 NOT NULL\_。
- 若表中已有数据， **务必** 执行步骤 3 同步序列值，否则新插入数据会报主键冲突错误。

---

## 5\. 反引号 (\`) 与转义字符处理

### 问题描述

MySQL 中反引号 `` ` `` 用于引用标识符，双引号 `"` 用于字符串时需转义。而在标准 PG 模式中，双引号用于标识符，单引号用于字符串。  
当插入含双引号的 JSON 字符串时，MySQL 习惯用 `\"` 转义，而 PG 默认遵循 SQL 标准，可能不识别 `\"` 为转义，导致存入反斜杠。

### 解决方案

调整 `standard_conforming_strings` 参数以兼容 MySQL 的转义习惯。

```sql
-- 方法：关闭标准字符串 conforming 模式 (允许 \ 作为转义符)
-- 警告：此参数为全局或会话级，开启后 \n, \t 等也会被解析为特殊字符
ALTER SYSTEM SET standard_conforming_strings TO off;
SELECT pg_reload_conf();

-- 验证
SHOW standard_conforming_strings; -- 应显示 off
```

**⚠️** \*\* 重要风险提示\*\*：

- 该参数修改后，字符串中的 `\n` (换行), `\t` (制表符) 等将被解释为控制字符，而非字面量的 “\\n”。
- 如果业务代码中依赖字面量反斜杠，此修改可能导致数据异常。
- **建议** ：优先修改应用程序代码，使用标准的单引号 `'` 包裹字符串，并在 PG 中使用 `E'...'` 语法处理转义，而非修改数据库全局参数。

## 6\. 分区表适配

### 差异对比

| 特性 | MySQL | PostgreSQL (≥10) / V9 |
| --- | --- | --- |
| **实现方式** | 原生表级物理分区 | 声明式分区 (基于继承 + 约束) |
| **子表管理** | 自动管理 | 需显式创建子表 (`PARTITION OF`) |
| **分区类型** | RANGE, LIST, HASH, KEY | RANGE, LIST, HASH (11+) |
| **默认分区** | `VALUES LESS THAN MAXVALUE` | `DEFAULT` 分区 (捕获未匹配数据) |
| **索引管理** | 支持全局/本地索引 | 仅支持本地索引 (每个分区独立建索引) |
| **主键要求** | 分区键必须包含在主键中 | 分区键必须包含在主键中 |
| **添加分区** | `ALTER TABLE ... ADD PARTITION` | `CREATE TABLE ... PARTITION OF` |
| **删除分区** | `ALTER TABLE ... DROP PARTITION` (删数据) | `DROP TABLE <子表名>` (删数据) |

### 案例演示

#### MySQL 写法

```sql
CREATE TABLE event_log (
  id BIGINT NOT NULL AUTO_INCREMENT,
  event_time DATETIME NOT NULL,
  message TEXT,
  PRIMARY KEY (id, event_time)
)
PARTITION BY RANGE COLUMNS (event_time) (
  PARTITION p202401 VALUES LESS THAN ('2024-02-01'),
  PARTITION p202402 VALUES LESS THAN ('2024-03-01'),
  PARTITION p_future VALUES LESS THAN (MAXVALUE)
);

-- 删除旧分区 (数据随之删除)
ALTER TABLE event_log DROP PARTITION p202401;
```

#### V9 (PostgreSQL) 兼容写法

```sql
-- Step 1: 创建主表 (分区父表)
CREATE TABLE event_log (
    id BIGSERIAL,
    event_time TIMESTAMP NOT NULL,
    message TEXT,
    PRIMARY KEY (id, event_time)
) PARTITION BY RANGE (event_time);

-- Step 2: 创建子分区
CREATE TABLE event_log_202401 
PARTITION OF event_log 
FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE event_log_202402 
PARTITION OF event_log 
FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');

-- 可选：创建 DEFAULT 分区 (捕获超出范围的数据，防止报错)
CREATE TABLE event_log_default 
PARTITION OF event_log DEFAULT;

-- 删除旧分区 (直接删除子表，数据随之删除)
DROP TABLE event_log_202401;
```

### 💡 优化总结

1. **代码清洗** ：去除了所有无效空格和 HTML 标签，确保 SQL 可直接复制执行。
2. **风险警示** ：针对 `pg_catalog` 修改和全局参数调整增加了明显的警告提示。
3. **结构清晰** ：采用“问题 - 原因 - 方案 - 代码 - 注意”的结构，便于查阅。
4. **术语修正** ：修正了“否者”、“copy的”等语病，统一了专业术语。

## 7.字段值忽略大小写

### 问题描述

瀚高V9 mysql兼容模式下，进行like模糊匹配时，默认不支持忽略字符串大小写匹配，导致匹配失败，可通过设置collate值或修改字段表结构来处理。

### 解决方案

测试数据：

```sql
highgo=# select * from test;
 id |  name
----+---------
|
|
|
```

方案一：

```sql
highgo=# select * from test where name='bob' collate utf8_general_ci;
 id | name
----+------
|
(1 行记录)
```

方案二：

```sql
-- 查看表原结构
highgo=# show create table test;
 Table |        Create Table
-------+----------------------------
 test  | CREATE TABLE "test" (     +
       |     "id" integer NOT NULL,+
       |     "name" text           +
       | )
(1 行记录)

-- 修改表字段排序规则
highgo=# alter table test alter COLUMN name type varchar(100) collate utf8_general_ci;
ALTER TABLE
highgo=# select * from test where name='bob' ;
 id | name
----+------
|
(1 行记录)

highgo=# show create table test;
 Table |                       Create Table
-------+-----------------------------------------------------------
 test  | CREATE TABLE "test" (                                    +
       |     "id" integer NOT NULL,                               +
       |     "name" character varying(100) COLLATE utf8_general_ci+
       | )
(1 行记录)
```

## 8.date\_sub函数兼容

### 问题描述

```
- 不支持interval语法运算。
```
```sql
highgo=# select current_date + interval '3' month;
ERROR:  operator does not exist: date + interval
第1行select current_date + interval '3' month;
```
```
- 不支持mysql date_sub函数兼容。
```
```sql
highgo=# select date_sub(current_date,interval '3' month);
ERROR:  function date_sub(date, interval) does not exist
第1行select date_sub(current_date,interval '3' month);
```

### 解决方案

创建date\_sub兼容函数。

```
create or replace
function ivymy.date_sub(datetime,interval) returns datetime language sql parallel safe immutable as $$
select
    ($1::pg_catalog.timestamp - $2);
$$;

-- 重载一个同名函数
create or replace
function ivymy.date_sub(date,interval) returns date language sql parallel safe immutable as $$
select
    ($1::pg_catalog.date - $2);
$$;
```

测试

```
highgo=# select
highgo-# DATE_SUB(NOW(), interval '3' month);
      DATE_SUB
---------------------
 2025-12-13 09:19:17
(1 行记录)

highgo=# select
highgo-# DATE_SUB(CURDATE(), interval '3' month);
  DATE_SUB
------------
 2025-12-13
(1 行记录)
```