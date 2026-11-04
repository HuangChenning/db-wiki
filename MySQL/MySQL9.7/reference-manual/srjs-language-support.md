---
title: "27.3.3 JavaScript Stored Program Language Support"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/srjs-language-support.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 27.3.3 JavaScript Stored Program Language Support

JavaScript language support in MySQL conforms to the [ECMAScript 2024 Specification](https://262.ecma-international.org/15.0/), and uses strict mode by default. Strict mode cannot be disabled. This implementation includes all of the standard ECMAScript library objects such as `Object`, `Function`, `Math`, `Date`, `String`, and so forth. `console.log()` and `console.error()` are also supported (see [Section 27.3.12, “JavaScript Stored Program Examples”](srjs-examples.md)).