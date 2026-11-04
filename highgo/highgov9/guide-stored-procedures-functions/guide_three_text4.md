---
title: "条件控制"
book: "存储过程&函数"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_three_text4.html"
tags:
  - highgo
  - highgo-v9
  - guide-stored-procedures-functions
---

## 条件控制

可以通过 IF 和 CASE 两种方式进行条件控制。

### IF条件控制

```sql
(1) IF ... THEN ... END IF

(2) IF ... THEN ... ELSE ... END IF

(3) IF ... THEN ... ELSEIF ... THEN ... ELSE ... END IF （可以有多个 ELSEIF）
```

`IF ... THEN ... ELSEIF ... THEN ... ELSE ... END IF` 语法中 ，如果 ELSEIF 后面省略 ELSE，直接用 END IF 结束，函数在调用时若条件落在 ELSE区间，调用不会报错，但返回结果为空。两个 `CASE` 语法中，如果省略 ELSE，直接用 END CASE 结束，函数在调用时若条件落在 ELSE 区间，函数将报错。

可以通过以下两个例子来进行验证：

`IF ... THEN ... ELSEIF ... THEN ... ELSE ... END IF` 的例子

```sql
CREATE OR REPLACE FUNCTION elseif_demo_(IN no int) RETURNS varchar AS 
$$
DECLARE
    res varchar;
BEGIN
    IF no<10 THEN res:='no<10';
    ELSEIF no BETWEEN 10 and 100 THEN res:='10<no<100';
    END IF;
    RETURN res;
END
$$
LANGUAGE plpgsql;
```

### CASE

```sql
(1) CASE ... WHEN ... THEN ... ELSE ... END CASE  
--when 表示 case 的多种情况，可以有多个 when ... then ... 

(2) CASE WHEN ...THEN ... ELSE ... END CASE
--when 后面可以赋予不同的参数布尔表达式（即表达式左、右边两边的参数均可变）
```

`CASE WHEN ...THEN ... ELSE ... END CASE` 的例子

```sql
CREATE OR REPLACE FUNCTION else_demo_(IN no int) RETURNS varchar AS 
$$
DECLARE
    res varchar;
BEGIN
    CASE WHEN no <10 THEN res:='no<10';
    END CASE;
    RETURN res;
END 
$$
LANGUAGE plpgsql;
```

两个例子的查询结果分别如下：

```sql
highgo=# SELECT elseif_demo_(323);
 elseif_demo_ 
 
(1 行记录)

highgo=# SELECT else_demo_(323);
错误:  没有找到CASE
提示:  在CASE语句结构中丢失ELSE部分
背景:  在CASE的第5行的PL/pgSQL函数else_demo_(integer)
```

CASE 两种用法的区别在于， `CASE ... WHEN...` 将判断语句拆成了两部分， `WHEN` 可以理解为一个等于号，只有 `WHEN` 右边的内容是可变的； `CASE WHEN...` 的判断语句在 WHEN 的右面，判断条件不限于一个属性。

可以通过下面的例子进行理解：

```sql
CREATE OR REPLACE FUNCTION case1_demo(IN no int) RETURNS varchar AS
$$
DECLARE
    res varchar;
BEGIN
    CASE no 
    WHEN 1 THEN res:='no=1';
    WHEN 2 THEN res:='no=2';
    END CASE;
    RETURN res;
END 
$$
LANGUAGE plpgsql;
CREATE OR REPLACE FUNCTION case2_demo(IN no int, name varchar) RETURNS varchar AS
$$
DECLARE
    res varchar;
BEGIN
    CASE 
    WHEN no=1 THEN res:='no=1';
    WHEN name='aaa' THEN res:='no=2';
    END CASE;
    RETURN res;
END 
$$
LANGUAGE plpgsql;
```