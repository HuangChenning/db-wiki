---
title: NEWDOMDOCUMENT
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000007021543.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# NEWDOMDOCUMENT

`NEWDOMDOCUMENT` 函数用于创建一个新的空 DOM 文档对象。可继续设置文档版本、字符集，创建根元素并追加子节点，最终序列化或转换为 `XMLType`。

<main id="notice" >
  <h4>功能适用性</h4>
  <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
</main>

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>对于 V4.4.2 版本，该子程序从 OceanBase 数据库 V4.4.2 BP3 版本开始引入。</p>
</main>

## 语法

```sql
DBMS_XMLDOM.newDOMDocument;
```

## 返回值

新创建的 `DBMS_XMLDOM.DOMDOCUMENT` 句柄。

## 使用说明

创建文档后，通常配合 `SETVERSION`、`SETCHARSET`、`CREATEELEMENT`、`APPENDCHILD` 等接口构造 DOM 树；使用完毕后应调用 `FREEDOCUMENT` 释放资源。

## 示例

```sql
DECLARE
  doc DBMS_XMLDOM.DOMDOCUMENT;
BEGIN
  doc := DBMS_XMLDOM.newDOMDocument;
  DBMS_XMLDOM.freeDocument(doc);
END;
/
```
