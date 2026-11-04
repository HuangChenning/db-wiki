---
title: "概况"
book: "数据操纵DML"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_four_text1.html"
tags:
  - highgo
  - highgo-v9
  - guide-dml
---

## 概况

当一个表被创建后，表是空的，需要先向里面插入数据，数据插入后可以进行更新和删除，在概念上数据的插入、删除操作每次都是以整行地方式进行的，没有办法一次插入或删除少于一行的数据。

HGDB 通过 `INSERT` 、 `UPDATE` 、 `DELETE` 关键字来对表进行插入、更新和删除操作。