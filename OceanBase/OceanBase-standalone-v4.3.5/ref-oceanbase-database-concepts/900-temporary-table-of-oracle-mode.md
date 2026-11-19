---
title: "临时表"
book: "系统原理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578334.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 临时表

临时表保存仅在事务或会话期间存在的数据。本文主要介绍 OceanBase 数据库的全局临时表（GTT）及其创建方法。

## 全局临时表简介

全局临时表用于保存一段时间内的数据，这里的一段时间可以是事务的生命周期也可以是 Session 的生命周期。

全局临时表的列定义可以对所有 Session 可见。但是，全局临时表中的数据是 Session 私有的，当前 Session 只能看到和修改自己的数据。

例如，在学生选课场景中，使用临时表来临时保存选课内容。在会话期间，选课数据是私有的。当学生确认选课列表时，应用程序将选课信息从临时表移动到普通表中。在会话结束时，数据库会自动删除全局临时表中的数据。

## 全局临时表的创建方法

用户可以通过 `CREATE GLOBAL TEMPORARY TABLE` 语句创建全局临时表，通过 `ON COMMIT` 子句控制是事务临时表还是 Session 临时表，具体如下：

- `ON COMMIT DELETE ROWS`：事务级临时表，提交时删除数据。
- `ON COMMIT PRESERVE ROWS`：会话级临时表，会话结束时删除数据。

全局临时表可以创建索引，全局临时表的索引表的数据也是临时性的，数据也是 Session 私有的。

## 临时外表

临时外表是一种在查询过程中临时创建的外表，用于读取数据，查询结束后该表会被自动删除。

OceanBase 集中式数据库在 V4.3.5 BP3 版本支持了通过 `SELECT URL` 和 `LOAD DATA` 语句读取或导入外表数据的功能。

## 示例

### 示例一：创建一个事务级临时表

1.  创建一个事务级临时表 `tbl1`。

    ```
    obclient [SYS]> CREATE GLOBAL TEMPORARY TABLE tbl1(col1 INT) ON COMMIT DELETE ROWS;
    ```

2.  向表临时表 `tbl1` 中插入一条数据。

    ```
    obclient [SYS]> INSERT INTO tbl1 VALUES(1);
    ```

3.  查询临时表 `tbl1` 中的数据。

    ```
    obclient [SYS]> SELECT * FROM tbl1;
    ```

    返回结果如下：

    ```
    +------+
    | COL1 |
    +------+
    |    1 |
    +------+
    1 row in set
    ```

4.  提交事务。

    ```
    obclient [SYS]> COMMIT;
    ```

5.  再次查询临时表 `tbl1` 中的数据。

    ```
    obclient [SYS]> SELECT * FROM tbl1;
    ```

    返回结果如下：

    ```
    Empty set
    ```

### 示例二：创建一个会话级临时表

**在会话 1 中进行以下操作：**

1.  创建一个会话级临时表 `tbl2`。

    ```
    obclient [SYS]> CREATE GLOBAL TEMPORARY TABLE tbl2(col1 INT) ON COMMIT PRESERVE ROWS;
    ```

2.  向表临时表 `tbl2` 中插入一条数据。

    ```
    obclient [SYS]> INSERT INTO tbl2 VALUES(1);
    ```

3.  查询临时表 `tbl2` 中的数据。

    ```
    obclient [SYS]> SELECT * FROM tbl2;
    ```

    返回结果如下：

    ```
    +------+
    | COL1 |
    +------+
    |    1 |
    +------+
    1 row in set
    ```

4.  提交事务。

    ```
    obclient [SYS]> COMMIT;
    ```

5.  再次查询临时表 `tbl2` 中的数据。

    ```
    obclient [SYS]> SELECT * FROM tbl2;
    ```

    返回结果如下：

    ```
    +------+
    | COL1 |
    +------+
    |    1 |
    +------+
    1 row in set
    ```

**在会话 2 中或者退出会话 1 重新连接数据库后进行以下操作：**

查询临时表 `tbl2` 中的数据。

```
obclient [SYS]> SELECT * FROM tbl2;
```

返回结果如下：

```
Empty set
```

## 相关文档

- [CREATE TABLE](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002017447)

- [SIMPLE SELECT](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002017919)

- [LOAD DATA](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002017398)
