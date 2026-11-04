---
title: "MySQL :: MySQL 26.10 Reference Manual :: 27.3.3 JavaScript Stored Program Language Support"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/srjs-language-support.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 27.3.3 JavaScript Stored Program Language Support

JavaScript language support in MySQL conforms to the [ECMAScript 2024 Specification](https://262.ecma-international.org/15.0/), and uses strict mode by default. Strict mode cannot be disabled. This implementation includes all of the standard ECMAScript library objects such as `Object`, `Function`, `Math`, `Date`, `String`, and so forth. `console.log()` and `console.error()` are also supported (see [Section 27.3.12, “JavaScript Stored Program Examples”](srjs-examples.md)).