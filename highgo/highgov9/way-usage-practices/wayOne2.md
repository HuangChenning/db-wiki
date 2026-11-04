---
title: "批量处理smallint 转 boolean"
book: "使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/way/wayOne2.html"
tags:
  - highgo
  - highgo-v9
  - way-usage-practices
---

**TL；DR：**

- 本文介绍一个存储过程专门用于批量修改列类型，如： `smallint -> boolean` 的转换场景。
- 强烈不推荐让存储过程直接批量修改，除非确认没有问题的情况下，不一定所有类型都适合转换成目标类型，有的是默认值，有的是约束影响的。

---

## 一、存储过程

```sql
CREATE OR REPLACE PROCEDURE public.bulk_modify_column_type(
    IN p_schema_name text,
    IN p_source_type text,
    IN p_target_type text,
    IN p_modify_default boolean DEFAULT false,
    IN p_dry_run boolean DEFAULT true
)
LANGUAGE plpgsql
AS $$
DECLARE
    rec record;
    v_alter_sql text;
    v_drop_default_sql text;
    v_set_default_sql text;
    v_using_expr text;
    v_default_expr text;
    v_old_default text;
    v_new_default text;
    v_executed_sql text;
    v_success_count int := 0;
    v_fail_count int := 0;
    v_total_count int := 0;
    v_source_regtype regtype;
    v_target_regtype regtype;
BEGIN
    EXECUTE $DDL$
        CREATE TABLE IF NOT EXISTS public.column_conversion_log (
            id bigserial PRIMARY KEY,
            schema_name text NOT NULL,
            table_name text NOT NULL,
            column_name text NOT NULL,
            old_data_type text,
            new_data_type text,
            old_default text,
            new_default text,
            executed_sql text,
            status text NOT NULL,
            error_message text,
            conversion_time timestamp DEFAULT now()
        );
    $DDL$;

    v_source_regtype := to_regtype(p_source_type);
    v_target_regtype := to_regtype(p_target_type);

    IF v_source_regtype IS NULL THEN
        RAISE EXCEPTION 'Source type "%" does not exist', p_source_type;
    END IF;

    IF v_target_regtype IS NULL THEN
        RAISE EXCEPTION 'Target type "%" does not exist', p_target_type;
    END IF;

    FOR rec IN
        SELECT
            n.nspname AS schema_name,
            c.relname AS table_name,
            a.attname AS column_name,
            a.atttypid AS source_atttypid,
            t.typcategory AS source_typcategory,
            format_type(a.atttypid, a.atttypmod) AS old_data_type,
            pg_get_expr(d.adbin, d.adrelid) AS column_default,
            a.attidentity,
            a.attgenerated
        FROM pg_attribute a
        JOIN pg_class c
          ON c.oid = a.attrelid
        JOIN pg_namespace n
          ON n.oid = c.relnamespace
        JOIN pg_type t
          ON t.oid = a.atttypid
        LEFT JOIN pg_attrdef d
          ON d.adrelid = a.attrelid
         AND d.adnum = a.attnum
        WHERE n.nspname = p_schema_name
          AND c.relkind = 'r'
          AND a.attnum > 0
          AND NOT a.attisdropped
          AND a.atttypid = v_source_regtype
        ORDER BY c.relname, a.attnum
    LOOP
        v_total_count := v_total_count + 1;
        v_old_default := rec.column_default;
        v_new_default := rec.column_default;
        v_drop_default_sql := NULL;
        v_set_default_sql := NULL;
        v_executed_sql := NULL;
        v_using_expr := NULL;
        v_default_expr := NULL;

        IF rec.attidentity IS NOT NULL AND rec.attidentity <> '' THEN
            RAISE NOTICE 'Skip identity column %.%.%', rec.schema_name, rec.table_name, rec.column_name;

            INSERT INTO public.column_conversion_log (
                schema_name, table_name, column_name,
                old_data_type, new_data_type,
                old_default, new_default,
                executed_sql, status, error_message
            )
            VALUES (
                rec.schema_name, rec.table_name, rec.column_name,
                rec.old_data_type, p_target_type,
                v_old_default, v_new_default,
                NULL, 'SKIPPED',
                'identity column'
            );

            CONTINUE;
        END IF;

        IF rec.attgenerated IS NOT NULL AND rec.attgenerated <> '' THEN
            RAISE NOTICE 'Skip generated column %.%.%', rec.schema_name, rec.table_name, rec.column_name;

            INSERT INTO public.column_conversion_log (
                schema_name, table_name, column_name,
                old_data_type, new_data_type,
                old_default, new_default,
                executed_sql, status, error_message
            )
            VALUES (
                rec.schema_name, rec.table_name, rec.column_name,
                rec.old_data_type, p_target_type,
                v_old_default, v_new_default,
                NULL, 'SKIPPED',
                'generated column'
            );

            CONTINUE;
        END IF;

        IF v_target_regtype = 'boolean'::regtype
           AND rec.source_typcategory = 'N' THEN
            v_using_expr := format('%I::int::boolean', rec.column_name);
            v_default_expr := format('(%s)::int::boolean', v_old_default);
        ELSE
            v_using_expr := format('%I::%s', rec.column_name, v_target_regtype::text);
            v_default_expr := format('(%s)::%s', v_old_default, v_target_regtype::text);
        END IF;

        v_alter_sql := format(
            'ALTER TABLE %I.%I ALTER COLUMN %I TYPE %s USING %s',
            rec.schema_name,
            rec.table_name,
            rec.column_name,
            v_target_regtype::text,
            v_using_expr
        );

        IF p_modify_default AND v_old_default IS NOT NULL THEN
            v_drop_default_sql := format(
                'ALTER TABLE %I.%I ALTER COLUMN %I DROP DEFAULT',
                rec.schema_name, rec.table_name, rec.column_name
            );

            v_set_default_sql := format(
                'ALTER TABLE %I.%I ALTER COLUMN %I SET DEFAULT %s',
                rec.schema_name, rec.table_name, rec.column_name, v_default_expr
            );

            v_new_default := v_default_expr;
        END IF;

        v_executed_sql := array_to_string(
            array_remove(ARRAY[
                CASE WHEN v_drop_default_sql IS NOT NULL THEN v_drop_default_sql || ';' END,
                v_alter_sql || ';',
                CASE WHEN v_set_default_sql IS NOT NULL THEN v_set_default_sql || ';' END
            ], NULL),
            E'\n'
        );

        RAISE NOTICE 'Table: %, Column: %, Old Type: %, New Type: %',
            rec.table_name, rec.column_name, rec.old_data_type, p_target_type;

        IF v_drop_default_sql IS NOT NULL THEN
            RAISE NOTICE 'Drop default SQL: %', v_drop_default_sql;
        END IF;

        RAISE NOTICE 'Alter type SQL: %', v_alter_sql;

        IF v_set_default_sql IS NOT NULL THEN
            RAISE NOTICE 'Set default SQL: %', v_set_default_sql;
        END IF;

        IF p_dry_run THEN
            INSERT INTO public.column_conversion_log (
                schema_name, table_name, column_name,
                old_data_type, new_data_type,
                old_default, new_default,
                executed_sql, status, error_message
            )
            VALUES (
                rec.schema_name, rec.table_name, rec.column_name,
                rec.old_data_type, p_target_type,
                v_old_default, v_new_default,
                v_executed_sql,
                'DRY_RUN',
                NULL
            );

            CONTINUE;
        END IF;

        BEGIN
            IF v_drop_default_sql IS NOT NULL THEN
                EXECUTE v_drop_default_sql;
            END IF;

            EXECUTE v_alter_sql;

            IF v_set_default_sql IS NOT NULL THEN
                EXECUTE v_set_default_sql;
            END IF;

            INSERT INTO public.column_conversion_log (
                schema_name, table_name, column_name,
                old_data_type, new_data_type,
                old_default, new_default,
                executed_sql, status, error_message
            )
            VALUES (
                rec.schema_name, rec.table_name, rec.column_name,
                rec.old_data_type, p_target_type,
                v_old_default, v_new_default,
                v_executed_sql,
                'SUCCESS',
                NULL
            );

            v_success_count := v_success_count + 1;

        EXCEPTION
            WHEN OTHERS THEN
                INSERT INTO public.column_conversion_log (
                    schema_name, table_name, column_name,
                    old_data_type, new_data_type,
                    old_default, new_default,
                    executed_sql, status, error_message
                )
                VALUES (
                    rec.schema_name, rec.table_name, rec.column_name,
                    rec.old_data_type, p_target_type,
                    v_old_default, v_new_default,
                    v_executed_sql,
                    'FAILED',
                    SQLERRM
                );

                v_fail_count := v_fail_count + 1;

                RAISE NOTICE 'Failed on %.%.%: %',
                    rec.schema_name, rec.table_name, rec.column_name, SQLERRM;
        END;
    END LOOP;

    RAISE NOTICE 'Total checked: %, Success: %, Failed: %, Mode: %',
        v_total_count,
        v_success_count,
        v_fail_count,
        CASE WHEN p_dry_run THEN 'DRY_RUN' ELSE 'EXECUTE' END;
END;
$$;
```

---

## 二、测试环境搭建

如果你想一次性全建好，可以直接用下面这个整包脚本。

```sql
CREATE SCHEMA IF NOT EXISTS test_schema;

DROP TABLE IF EXISTS test_schema.t_bool_ok;
DROP TABLE IF EXISTS test_schema.t_bool_bad;
DROP TABLE IF EXISTS test_schema.t_bool_default;
DROP TABLE IF EXISTS test_schema.t_bool_notnull;
DROP TABLE IF EXISTS test_schema.t_bool_multi;
DROP TABLE IF EXISTS test_schema.t_bool_check;

CREATE TABLE test_schema.t_bool_ok (
    id bigserial PRIMARY KEY,
    flag smallint,
    is_enabled smallint DEFAULT 0,
    is_deleted smallint DEFAULT 1,
    remark text
);

INSERT INTO test_schema.t_bool_ok (flag, is_enabled, is_deleted, remark) VALUES
(0, 0, 1, 'all zero or one'),
(1, 1, 0, 'all zero or one'),
(NULL, 0, 1, 'contains null'),
(0, NULL, NULL, 'default related test'),
(1, 1, 1, 'all one');

CREATE TABLE test_schema.t_bool_bad (
    id bigserial PRIMARY KEY,
    status smallint,
    active_flag smallint DEFAULT 0,
    note text
);

INSERT INTO test_schema.t_bool_bad (status, active_flag, note) VALUES
(0, 0, 'valid'),
(1, 1, 'valid'),
(2, 0, 'invalid value 2'),
(-1, 1, 'invalid value -1'),
(9, NULL, 'invalid value 9'),
(NULL, 0, 'null test');

CREATE TABLE test_schema.t_bool_default (
    id bigserial PRIMARY KEY,
    flag_a smallint DEFAULT 0,
    flag_b smallint DEFAULT 1,
    flag_c smallint DEFAULT NULL,
    description text
);

INSERT INTO test_schema.t_bool_default (description) VALUES
('use all defaults'),
('use all defaults again');

INSERT INTO test_schema.t_bool_default (flag_a, flag_b, flag_c, description) VALUES
(0, 1, NULL, 'manual values'),
(1, 0, 1, 'manual values 2');

CREATE TABLE test_schema.t_bool_notnull (
    id bigserial PRIMARY KEY,
    checked_flag smallint NOT NULL DEFAULT 0,
    approved_flag smallint NOT NULL DEFAULT 1,
    memo text
);

INSERT INTO test_schema.t_bool_notnull (checked_flag, approved_flag, memo) VALUES
(0, 1, 'row 1'),
(1, 0, 'row 2'),
(1, 1, 'row 3');

CREATE TABLE test_schema.t_bool_multi (
    id bigserial PRIMARY KEY,
    col_a smallint DEFAULT 0,
    col_b smallint DEFAULT 1,
    col_c smallint,
    col_d smallint,
    info text
);

INSERT INTO test_schema.t_bool_multi (col_a, col_b, col_c, col_d, info) VALUES
(0, 1, 0, 1, 'row 1'),
(1, 0, 1, 0, 'row 2'),
(0, 1, NULL, 1, 'row 3'),
(1, 1, 1, NULL, 'row 4');

CREATE TABLE test_schema.t_bool_check (
    id bigserial PRIMARY KEY,
    flag smallint,
    visible smallint DEFAULT 1,
    remark text,
    CONSTRAINT chk_t_bool_check_flag
        CHECK (flag IN (0, 1) OR flag IS NULL),
    CONSTRAINT chk_t_bool_check_visible
        CHECK (visible IN (0, 1) OR visible IS NULL)
);

INSERT INTO test_schema.t_bool_check (flag, visible, remark) VALUES
(0, 1, 'valid'),
(1, 0, 'valid'),
(NULL, 1, 'null allowed');
```

---

## 三、测试前先检查哪些列可能有风险

在真正改类型前，你最好先检查所有 `smallint` 列里是否存在非 `0` ／ `1` 的值。

## 1．先看有哪些 smallint 列

```sql
SELECT
    table_schema,
    table_name,
    column_name,
    data_type,
    column_default
FROM information_schema.columns
WHERE table_schema = 'test_schema'
  AND data_type = 'smallint'
ORDER BY table_name, ordinal_position;
```

---

## 2．手工检查某张表某列

例如检查 `t_bool_bad.status` ：

```sql
SELECT
    count(*) AS total_rows,
    count(*) FILTER (WHERE status IS NULL) AS null_rows,
    count(*) FILTER (WHERE status IN (0, 1)) AS valid_rows,
    count(*) FILTER (WHERE status NOT IN (0, 1) AND status IS NOT NULL) AS invalid_rows
FROM test_schema.t_bool_bad;
```

再看非法值明细：

```sql
SELECT DISTINCT status
FROM test_schema.t_bool_bad
WHERE status NOT IN (0, 1) AND status IS NOT NULL
ORDER BY status;
```

---

## 四、测试过程

## 第一轮：只做 dry run

```sql
CALL public.bulk_modify_column_type(
    p_schema_name => 'test_schema',
    p_source_type => 'smallint',
    p_target_type => 'boolean',
    p_modify_default => TRUE,
    p_dry_run => TRUE
);
```

先看它打出来的 SQL 和日志。

---

## 第二轮：只拿“干净表”实测

更稳妥的做法是先单表测试，而不是一上来扫整个 schema。

因为你这个 schema 里已经有故意制造失败的数据。

---

## 五、额外给你一组“单表验证 SQL”

建完后，你可以这样看表结构：

```sql
SELECT
    table_name,
    column_name,
    data_type,
    column_default
FROM information_schema.columns
WHERE table_schema = 'test_schema'
  AND table_name IN (
      't_bool_ok',
      't_bool_bad',
      't_bool_default',
      't_bool_notnull',
      't_bool_multi',
      't_bool_check'
  )
ORDER BY table_name, ordinal_position;
```

查看数据：

```sql
SELECT * FROM test_schema.t_bool_ok ORDER BY id;
SELECT * FROM test_schema.t_bool_bad ORDER BY id;
SELECT * FROM test_schema.t_bool_default ORDER BY id;
SELECT * FROM test_schema.t_bool_notnull ORDER BY id;
SELECT * FROM test_schema.t_bool_multi ORDER BY id;
SELECT * FROM test_schema.t_bool_check ORDER BY id;
```

---

## 九、我的建议

你这次测试最好分两类：

这样你能很快看出：

- 类型改得对不对
- 默认值有没有被错误改成常量
- 非法值时是中断、跳过，还是记录失败

---

## 十、直接可执行的行动方案

你现在就按下面顺序做：

1. 执行上面的“一键初始化脚本”
2. 先查询 `information_schema.columns` ，确认所有测试列都是 `smallint`
3. 先执行 `dry run`
4. 查看日志表 `public.column_conversion_log`
5. 再决定要不要正式执行

如果你要，我下一条可以直接给你补一版： **专门支持 **`smallint -> boolean`** 的安全转换过程** ，把 `USING %I::boolean` 改成 `CASE WHEN %I = 0 THEN FALSE WHEN %I = 1 THEN TRUE ELSE NULL END` 。