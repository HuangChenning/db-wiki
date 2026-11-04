---
title: "调用存储过程报错：invalid transaction termination"
book: "数据库使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionTwo8.html"
tags:
  - highgo
  - highgo-v9
  - faq-database-usage
---

**环境信息：**

数据库版本：hgdbv9.0.5

安装包名称：hgdbv9-05-0-0-5022-20251223-a09fff4-linux.x86\_64.bin

---

**场景描述：**

存储过程中存在COMMIT的时候，通过其他有权限的用户（非所有者）调用报错，报错信息如下：

```
> ERROR:  invalid transaction termination
CONTEXT:  PL/iSQL function update_dept_salary(number,number) line 7 at COMMIT
```

**解决方案：**

指定AUTHID 值为 CURRENT\_USER ，默认是 DEFINER

**修改前：**

```
CREATE OR REPLACE PROCEDURE exam.update_dept_salary (
    p_dept_id    IN NUMBER,
    p_raise_pct  IN NUMBER
) AUTHID CURRENT_USER IS
    v_emp_count NUMBER;
BEGIN
    UPDATE employees
    SET salary = salary * (1 + p_raise_pct / 100)
    WHERE department_id = p_dept_id;
    v_emp_count := SQL%ROWCOUNT;
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('成功更新并提交了 ' || v_emp_count || ' 名员工的薪资。');
END update_dept_salary;
/
```

**修改后：**

```
CREATE OR REPLACE PROCEDURE exam.update_dept_salary (
    p_dept_id    IN NUMBER,
    p_raise_pct  IN NUMBER
) AUTHID CURRENT_USER IS
    v_emp_count NUMBER;
BEGIN
    UPDATE employees
    SET salary = salary * (1 + p_raise_pct / 100)
    WHERE department_id = p_dept_id;
    v_emp_count := SQL%ROWCOUNT;
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('成功更新并提交了 ' || v_emp_count || ' 名员工的薪资。');
END update_dept_salary;
/
```