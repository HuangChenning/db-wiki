---
title: "存储过程定义"
book: "存储过程&函数"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_three_text1.html"
tags:
  - highgo
  - highgo-v9
  - guide-stored-procedures-functions
---

## 存储过程定义

瀚高数据库的存储过程是一组为了完成特定功能的 SQL 语句集，存储在数据库中，经过第一次编译后再次调用不需要再次编译，用户通过指定存储过程的名字并给出参数（如果该存储过程带有参数）来执行它。存储过程是数据库编程中非常重要的一部分，可以实现复杂的数据处理逻辑和业务规则。

### 语法

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name (parameter_list)
LANGUAGE plpgsql AS $$
DECLARE
    -- 声明变量
BEGIN
    -- 存储过程体
    COMMIT;  -- 或 ROLLBACK
EXCEPTION
    WHEN exception_type THEN
        -- 异常处理逻辑
END;
$$;
```

### 参数类型

存储过程支持三种参数类型：

- **IN** （默认）：输入参数，在存储过程中使用，不能被修改。
- **OUT** ：输出参数，在存储过程中被赋值，返回给调用者。
- **INOUT** ：输入输出参数，既可以作为输入值，也可以在存储过程中被修改并返回。
- **复合类型** ：type

复合类型例子如下

```sql
-- 定义复合类型
CREATE TYPE employee_info_type AS (
    emp_name TEXT,
    emp_salary NUMERIC,
    emp_hire_date DATE
);

-- 存储过程返回复合类型
CREATE OR REPLACE PROCEDURE get_employee_info(
    emp_id INTEGER,
    OUT result employee_info_type
)
LANGUAGE plpgsql AS $$
BEGIN
    SELECT name, salary, hire_date INTO result
    FROM employees
    WHERE id = emp_id;
    
    IF NOT FOUND THEN
        RAISE EXCEPTION '员工 ID % 不存在', emp_id;
    END IF;
END;
$$;
```

例子

```sql
CREATE OR REPLACE PROCEDURE update_salary(
    emp_id INTEGER,           -- 输入参数
    new_salary INTEGER,       -- 输入参数
    OUT updated BOOLEAN,      -- 输出：更新是否成功
    OUT old_salary INTEGER,   -- 输出：旧工资
    OUT error_msg TEXT        -- 输出：错误信息
)
LANGUAGE plpgsql AS $$
DECLARE
    v_count INTEGER;
BEGIN
    -- 查询旧工资
    SELECT salary INTO old_salary 
    FROM employees 
    WHERE id = emp_id;
    
    -- 更新工资
    UPDATE employees 
    SET salary = new_salary 
    WHERE id = emp_id;
    
    GET DIAGNOSTICS v_count = ROW_COUNT;
    updated := v_count > 0;
    
    IF NOT updated THEN
        error_msg := '员工ID不存在';
    ELSE
        error_msg := NULL;
    END IF;
    
EXCEPTION
    WHEN OTHERS THEN
        updated := FALSE;
        error_msg := SQLERRM;  -- 捕获异常信息
END;
$$;
```

调用

```sql
DO $$
DECLARE
    v_updated BOOLEAN;
    v_old_salary INTEGER;
    v_error_msg TEXT;
BEGIN
    -- 调用存储过程，将输出参数赋值给变量
    CALL update_salary(
        emp_id => 1001, 
        new_salary => 8000,
        updated => v_updated,
        old_salary => v_old_salary,
        error_msg => v_error_msg
    );
    
    -- 打印结果（实际应用中可根据需求处理结果）
    RAISE INFO '更新结果：%，旧工资：%，错误信息：%', 
               v_updated, v_old_salary, v_error_msg;
END $$;
```