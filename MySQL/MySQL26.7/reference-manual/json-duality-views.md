---
title: "MySQL :: MySQL 26.7 Reference Manual :: 27.7 JSON Duality Views"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/json-duality-views.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 27.7 JSON Duality Views

MySQL 26.7 supports JSON duality views. Also known as JSON relational duality views, these objects are stored queries that when invoked produce a set of values in JSON format. In effect, a JSON duality view acts as a virtual JSON document, or as a collection of virtual JSON documents.

With JSON duality views, you can establish a mapping between relational tables and a hierarchical multi-level JSON document, effectively unifying structured (relational) and semi-structured (JSON) data. This allows you to harness the strength of both models (perfect synergy of JSON models with REST APIs, and referential integrity of relational models), and gives your applications the option to read and write using either data model.

The discussion in the next few sections describes the syntax for creating, altering, and dropping JSON duality views, shows some examples of how to use them, and provides information about obtaining related metadata.