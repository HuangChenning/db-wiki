---
title: "Chapter 15 Using MySQL Enterprise Backup with MySQL Enterprise Firewall"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/meb-enterprise-firewall.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

MySQL Enterprise Edition includes MySQL Enterprise Firewall, an application-level firewall that enables database server administrators to permit or deny SQL statement execution based on matching against allowlists of accepted statement patterns.

When using MySQL Enterprise Firewall with MySQL Enterprise Backup, record the statement `FLUSH     ENGINE LOGS` explicitly in the statement allowlist; otherwise some MySQL Enterprise Backup might then fail. Because MySQL Enterprise Backup 9.7 only uses the statement sporadically, it is easy to miss it in the training phase for the MySQL Enterprise Firewall.