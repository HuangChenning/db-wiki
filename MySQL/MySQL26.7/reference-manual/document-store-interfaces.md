---
title: "MySQL :: MySQL 26.7 Reference Manual :: 22.1 Interfaces to a MySQL Document Store"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/document-store-interfaces.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 22.1 Interfaces to a MySQL Document Store

To work with MySQL as a document store, you use dedicated components and a choice of clients that support communicating with the MySQL server to develop document based applications.

- The following MySQL products support X Protocol and enable you to use X DevAPI in your chosen language to develop applications that communicate with a MySQL Server functioning as a document store:
	- MySQL Shell (which provides implementations of X DevAPI in JavaScript and Python)
	- Connector/C++
	- Connector/J
	- Connector/Node.js
	- Connector/NET
	- Connector/Python
- MySQL Shell is an interactive interface to MySQL supporting JavaScript, Python, or SQL modes. You can use MySQL Shell to prototype applications, execute queries and update data. [Installing MySQL Shell](https://dev.mysql.com/doc/mysql-shell/26.7/en/mysql-shell-install.html) has instructions to download and install MySQL Shell.
- The quick-start guides (tutorials) in this chapter help you to get started using MySQL Shell with MySQL as a document store.
	The quick-start guide for JavaScript is here: [Section 22.3, “JavaScript Quick-Start Guide: MySQL Shell for Document Store”](mysql-shell-tutorial-javascript.md).
	The quick-start guide for Python is here: [Section 22.4, “Python Quick-Start Guide: MySQL Shell for Document Store”](mysql-shell-tutorial-python.md).
- The *MySQL Shell User Guide* at [MySQL Shell 26.7](https://dev.mysql.com/doc/mysql-shell/26.7/en/) provides detailed information about configuring and using MySQL Shell.