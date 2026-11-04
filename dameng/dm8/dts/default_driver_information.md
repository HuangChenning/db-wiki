---
title: "附录1 默认驱动信息"
book: "DM8 数据迁移工具 DTS"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/default_driver_information.html
tags:
  - dameng
  - dm8
  - dts
---

DTS 会自带数据库驱动。缺省使用自带数据库驱动，DTS 可以根据不同的数据库版本使用不同的驱动，自带驱动放在安装目录的 tool/dropins/com.dameng/plugins/com.dameng.jdbc.drivers 目录下。

## 1\. DM

DTS 提供一个驱动文件供 DM 各版本使用。

| **数据库版本** | **驱动版本** | **驱动文件名** |
| --- | --- | --- |
| \-- | 8.1 | DmJdbcDriver.jar |

## 2\. DM6

DTS 提供一个驱动文件供 DM6 各版本使用。

| **数据库版本** | **驱动版本** | **驱动文件名** |
| --- | --- | --- |
| \-- | 3.0 | Dm6JdbcDriver.jar |

## 3\. ORACLE

根据 ORACLE 不同版本，DTS 提供不同版本的驱动，如下表所示。缺省使用 Oracle12c 对应的驱动 12.2。

| **数据库版本** | **驱动版本** | **驱动文件名** |
| --- | --- | --- |
| Oracle 12c | 12.2 | ojdbc8-12.2.0.1.jar |
| Oracle 9i Oracle 10g Oracle 11g | 11.2 | ojdbc6-11.2.0.4.jar |
| Oracle 18c | 18.15 | ojdbc8-18.15.0.0.jar |
| Oracle 19c Oracle 21c Oracle 23c | 21.9 | ojdbc8-21.9.0.0.jar |

## 4\. SQLSERVER

根据 SQLSERVER 不同版本，DTS 提供多个版本的驱动，如下表所示。缺省使用 SQLServer 2008 对应的驱动 6.2。

| **数据库版本** | **驱动版本** | **驱动文件名** |
| --- | --- | --- |
| SQLServer 2008 | 6.2 | jdbc-sqlserver-6.2.2.jar |
| SQLServer 2000 SQLServer 2005 | 3.0 | sqlserver2008\_3.0.jar |
| SQLServer 2008R2 | 7.2 | jdbc-sqlserver-7.2.2.jar |
| SQLServer 2012 | 10.2 | jdbc-sqlserver-10.2.3.jar |
| SQLServer 2014 SQLServer 2016 SQLServer 2017 SQLServer 2019 SQLServer 2022 | 12.4 | jdbc-sqlserver-12.4.2.jar |

## 5\. MYSQL

根据 MYSQL 不同版本，DTS 提供不同版本的驱动，如下表所示。缺省使用 MySQL 5.7 对应的驱动 8.2。

| **数据库版本** | **驱动版本** | **驱动文件名** |
| --- | --- | --- |
| MySQL 5.5 MySQL 5.7 MySQL 8.0 | 8.2 | mysql-connector-j-8.2.0.jar |

## 6\. DB2

根据 DB2 不同版本，DTS 提供不同版本的驱动，如下表所示。缺省使用 DB2 V9 对应的驱动 4.9。

| **数据库版本** | **驱动版本** | **驱动文件名** |
| --- | --- | --- |
| DB2 V9 | 4.9 | jdbc-db2-4.9.78.jar |
| DB2 V10 | 4.23 | jdbc-db2-4.23.42.jar |
| DB2 V11 | 4.26 | jdbc-db2-4.26.14.jar |

## 7\. POSTGRESQL

根据 POSTGRESQL 不同版本，DTS 提供不同版本的驱动，如下表所示。缺省使用 PostgreSQL 16 对应的驱动 42.7。

| **数据库版本** | **驱动版本** | **驱动文件名** |
| --- | --- | --- |
| PostgreSQL 16 | 42.7 | postgresql-42.7.4.jar |

## 8\. INFORMIX

根据 INFORMIX 不同版本，DTS 提供不同版本的驱动，如下表所示。缺省使用 Informix 12 对应的驱动 4.10。

| **数据库版本** | **驱动版本** | **驱动文件名** |
| --- | --- | --- |
| Informix 11 | 3.0 | informix.jar |
| Informix 12 | 4.10 | jdbc-informix-4.10.16.jar |
| Informix 14 | 4.50 | jdbc-informix-4.50.10.jar |

## 9\. KINGBASE

根据 Kingbase 不同版本，DTS 提供不同版本的驱动，如下表所示。缺省使用 Kingbase V8R6 对应的驱动 8.6。

| **数据库版本** | **驱动版本** | **驱动文件名** |
| --- | --- | --- |
| Kingbase V7 | 6.1 | jdbc-kingbase-6.1.3.jar |
| Kingbase V8R3 | 8.2 | jdbc-kingbase8-8.2.0.jar |
| Kingbase V8R6 | 8.6 | jdbc-kingbase8-8.6.0.jar |
| Kingbase V9R1 | 9.0 | jdbc-kingbase8-9.0.0.jar |

## 10\. SHENTONG

根据 SHENTONG 不同版本，DTS 提供不同版本的驱动，如下表所示。缺省使用 ShenTong 7 对应的驱动 7.0。

| **数据库版本** | **驱动版本** | **驱动文件名** |
| --- | --- | --- |
| ShenTong 7 | 7.0 | jdbc-oscar-7.0.85.jar |

## 11\. SYBASE

根据 Sybase 不同版本，DTS 提供不同版本的驱动，如下表所示。缺省使用 Sybase 15 对应的驱动 7.0。

| **数据库版本** | **驱动版本** | **驱动文件名** |
| --- | --- | --- |
| Sybase 12 | 6.0 | jdbc-sybase-6.0.jar |
| Sybase 15 | 7.0 | jdbc-sybase-7.0.jar |
| Sybase 16 | 16.0 | jdbc-sybase-16.0.jar |

## 12\. ACCESS

DTS 提供一个驱动文件供 ACCESS 使用。

| **数据库版本** | **驱动版本** | **驱动文件名** |
| --- | --- | --- |
| \-- | \-- | ucanaccess.jar |