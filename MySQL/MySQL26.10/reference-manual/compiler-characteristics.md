---
title: "MySQL :: MySQL 26.10 Reference Manual :: 2.1.6 Compiler-Specific Build Characteristics"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/compiler-characteristics.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 2.1.6 Compiler-Specific Build Characteristics

In some cases, the compiler used to build MySQL affects the features available for use. The notes in this section apply for binary distributions provided by Oracle Corporation or that you compile yourself from source.

****icc** (Intel C++ Compiler) Builds**

A server built with **icc** has these characteristics:

- SSL support is not included.