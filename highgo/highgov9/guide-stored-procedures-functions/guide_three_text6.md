---
title: "游标定义"
book: "存储过程&函数"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_three_text6.html"
tags:
  - highgo
  - highgo-v9
  - guide-stored-procedures-functions
---

## 游标定义

游标（Cursor）是瀚高数据库中用于处理结果集的一种数据结构，它允许程序逐行访问查询结果。类似于指针，游标指向结果集中的某一行，通过移动游标，可以对每一行数据进行单独处理。游标常用于需要对结果集进行复杂操作，如逐条更新、删除、计算等场景。

### 游标类型

1. **显式游标** ：由用户手动声明、打开、操作和关闭，适用于复杂数据处理逻辑。
2. **隐式游标** ：由数据库自动管理，用于单行查询（如 `SELECT... INTO` 语句），无需手动操作。

定义

```sql
cur_data CURSOR FOR
SELECT column1, column2 FROM your_table;
BEGIN
 OPEN cur_data; -- 打开游标
-- 循环遍历游标中的每一行
LOOP
    -- 从游标中提取一行数据
    FETCH cur_data INTO v_column1, v_column2;
-- 检查是否已到达游标末尾
  EXIT WHEN NOT FOUND;
-- 处理提取的数据
    END LOOP;
-- 关闭游标
    CLOSE cur_data;
END;
```

注意：

1 动态游标用r\_cur refcursor;

2表得行变量用record类型;

3 可以用move移动游标：Move next 1 from cursor\_name;

例子

```sql
CREATE OR REPLACE FUNCTION calculate_department_salary_total() 
RETURNS TABLE (department_id INTEGER, total_salary NUMERIC) AS $$
DECLARE
    dept_cursor CURSOR FOR 
    SELECT DISTINCT department_id FROM employees;
    dept_id INTEGER;
    total NUMERIC := 0;
BEGIN
    OPEN dept_cursor;
    LOOP
        FETCH dept_cursor INTO dept_id;
        EXIT WHEN NOT FOUND;
        
        total := 0;
        FOR emp_salary IN (SELECT salary FROM employees WHERE department_id = dept_id) LOOP
            total := total + emp_salary;
        END LOOP;
        
        RETURN QUERY SELECT dept_id, total;
    END LOOP;
    CLOSE dept_cursor;
END;
$$ LANGUAGE plpgsql;
```