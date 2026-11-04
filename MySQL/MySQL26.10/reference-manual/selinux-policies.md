---
title: "MySQL :: MySQL 26.10 Reference Manual :: 8.7.3 MySQL Server SELinux Policies"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/selinux-policies.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 8.7.3 MySQL Server SELinux Policies

MySQL Server SELinux policy modules are typically installed by default. You can view installed modules using the **semodule -l** command. MySQL Server SELinux policy modules include:

For information about MySQL Server SELinux policy modules, refer to the SELinux manual pages. The manual pages provide information about types and Booleans associated with the MySQL service. Manual pages are named in the ``*`service-name`*_selinux`` format.

```svg
man mysqld_selinux
```

If SELinux manual pages are not available, refer to your distribution's SELinux documentation for information about how to generate manual pages using the `sepolicy       manpage` utility.