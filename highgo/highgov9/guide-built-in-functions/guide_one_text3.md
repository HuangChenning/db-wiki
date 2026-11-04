---
title: "几何函数"
book: "常用内置函数"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_one_text3.html"
tags:
  - highgo
  - highgo-v9
  - guide-built-in-functions
---

## 几何函数

| 函数 | 返回类型 | 描述 | 例子 |
| --- | --- | --- | --- |
| area(object) | double precision | 面积 | area(box ‘((0,0), (1, 1))’) |
| center(object) | point | 中心 | center(box’((0,0), (1,2))’) |
| diameter(circle) | double precision | 圆的直径 | diameter(circle ‘((0,0),2.0)’) |
| height(box) | double precision | 方框的垂直尺寸 | height(box’((0,0), |
| isclosed(path) | boolean | 一个封闭路径？ | isclosed(path’((0,0),(1, 1), (2,0))’) |
| isopen(path) | boolean | 一个开放路径？ | isopen(path’\[(0,0),(1, 1), (2,0)\]’) |
| length(object) | double precision | 长度 | length(path’((-1,0),(1,0))’) |
| npoints(path) | int | 点数 | npoints(path’\[(0,0),(1, 1), (2,0)\]’) |
| npoints(polygon) | int | 点数 | npoints(polygon ‘((1, 1),(0,0))’) |
| pclose(path) | path | 将路径转换成封 闭的 | pclose(path’\[(0,0),(1, 1), (2,0)\]’) |
| popen(path) | path | 将路径转换成开 放 | popen(path ‘((0,0), (1, 1),(2,0))’) |
| radius(circle) | double precision | 圆的半径 | radius(circle’((0,0),2.0)’) |
| width(box) | double precision | 方框的水平尺寸 | width(box ‘((0,0), (1, 1))’) |
| box(circle) | box | 圆到方框 | box(circle’((0,0),2.0)’) |
| box(point) | box | 点到空方框 | box(point ‘(0,0)’) |
| box(point, point) | box | 点到方框 | box(point ‘(0,0)’, point ‘(1, 1)’) |
| box(polygon) | box | 多边形到方 框 | box(polygon’((0,0),(1, 1), (2,0))’) |
| bound\_box(box, box) | box | 方框到外包 框 | bound\_box(box’((0,0),(1, 1))’, box ‘((3,3), (4,4))’) |
| circle(box) | circle | 方框到圆 | circle(box ‘((0,0), (1, 1))’) |
| circle(point,double precision) | circle | 中心和半径 到圆 | circle(point ‘(0,0)’, 2.0) |
| circle(polygon) | circle | 多边形到圆 | circle(polygon ‘((0,0),(1, 1), (2,0))’) |
| line(point, point) | line | 点到线 | line(point ‘(-1,0)’, point ‘(1,0)’) |
| lseg(box) | lseg | 方框对角线 到线段 | lseg(box ‘((-1,0), (1,0))’) |
| lseg(point, point) | lseg | 点到线段 | lseg(point ‘(-1,0)’, point ‘(1,0)’) |
| path(polygon) | path | 多边形到路 径 | path(polygon ‘((0,0),(1, 1), (2,0))’) |
| point(doubleprecision,double precision) | point | 构造点 | point(23.4, -44.5) |
| point(box) | point | 方框的中心 | point(box ‘((-1,0), (1,0))’) |
| point(circle) | point | 圆的中心 | point(circle ‘((0,0),2.0)’) |
| point(lseg) | point | 线段的中心 | point(lseg’((-1,0),(1,0))’) |
| point(polygon) | point | 多边形的中 心 | point(polygon ‘((0,0),(1, 1), (2,0))’) |
| polygon(box) | polygon | 方框到 4 点 | polygon(box ‘((0,0),(1, 1))’) |
| polygon(circle) | polygon | 圆到 12 点多 边形 | polygon(circle ‘((0,0),2.0)’) |
| polygon(npts, circle) | polygon | 点到 npts 点 多边形 | polygon(12, circle ‘((0,0),2.0)’) |