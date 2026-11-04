---
title: "8、客户端工具函数调试插件安装与配置"
book: "配置类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/windows_client_tools.html"
tags:
  - highgo
  - highgo-v45
  - way-configuration
---

## 文档目的

瀚高数据库客户端默认不具备函数调试功能，需手动安装调试插件并创建扩展后，方可通过客户端图形化界面进行 PL/SQL 函数调试，本文档详细说明不同数据库版本的插件安装、配置及使用方法。

## 适用范围

适用于瀚高数据库 V4.5.x 系列版本，区分自带插件与独立安装插件场景。

---

## 一、前置说明

1. 函数调试功能为数据库可选扩展能力， **必须安装调试插件并创建 pldbgapi 扩展** 后才能使用；
2. 操作账号：统一使用 **highgo** 数据库用户执行所有操作；
3. 核心插件： `pldbgapi` （调试底层接口）、 `pldebugger` （调试上层工具）。

---

## 二、分版本安装配置步骤

### 场景 1：数据库自带 pldbgapi 插件（V4.5.8、V4.5.10.3 等版本）

该版本数据库内置调试插件，无需额外安装安装包，直接创建扩展即可。

1. 登录数据库使用 highgo 用户通过命令行连接数据库：

shell

```
psql -U highgo -d highgo
```
1. 创建调试扩展执行 SQL 语句创建 pldbgapi 扩展模块：

sql

```
create extension pldbgapi;
```
1. 验证扩展安装结果查询系统表，确认插件安装成功：

sql

```
select * from pg_extension;
```

✅ 验证标准：查询结果中包含 `pldbgapi` 记录，即为安装成功。

---

### 场景 2：需独立安装 pldebugger 插件（V4.5.11 等版本）

该版本数据库未内置调试插件，需手动上传、安装插件安装包后，再创建扩展。

1. 上传并安装插件包将 `pldebugger1.1-e2dc4e7-20251117.x86_64.rpm` 插件包上传至服务器，执行 rpm 安装命令：

shell

```
rpm -ivh pldebugger1.1-e2dc4e7-20251117.x86_64.rpm
```
1. 登录数据库

shell

```
psql -U highgo -d highgo
```
1. 创建调试扩展

sql

```
create extension pldbgapi;
```
1. 验证扩展安装结果

sql

```
select * from pg_extension;
```

✅ 验证标准：查询结果中包含 `pldbgapi` 记录，即为安装成功。

---

## 三、函数调试功能使用方法

扩展创建成功后，重启 / 刷新数据库客户端工具，按以下路径开启调试：

1. 客户端中找到目标 **函数** ；
2. 右键单击函数；
3. 选择 **调试** 选项，即可使用图形化调试功能。

---

## 四、核心插件说明

### 4.1 pldbgapi 插件

- 定位： **函数调试底层工具包**
- 作用：瀚高数据库调试功能的核心底层接口插件，提供 PL/SQL（plpgsql）代码调试的基础能力，包括调用栈获取、断点设置、单步执行、变量查看等底层函数实现。

### 4.2 pldebugger 插件

- 定位： **函数调试上层交互工具**
- 作用：基于 pldbgapi 底层接口进行封装，对接 pgAdmin、DBeaver 等数据库客户端工具；不实现调试核心逻辑，仅将底层调试能力转换为图形化交互方式，支持用户可视化操作。