---
title: "2.1.2 Which MySQL Version and Distribution to Install"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/which-version.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 2.1.2 Which MySQL Version and Distribution to Install

When preparing to install MySQL, decide which version and distribution format (binary or source) to use.

First, decide whether to install from a bugfix series like MySQL 8.4, or use an innovation release like MySQL 9.6. Both tracks include bug fixes while an innovation release includes the newest features. Both bugfix and innovation releases are meant for production use.

The naming scheme in MySQL 8.0 uses release names that consist of three numbers and an optional suffix (for example, **mysql-8.0.34**). The numbers within the release name are interpreted as follows:

- The first number (**8**) is the major version number.
- The second number (**0**) is the minor version number. Taken together, the major and minor numbers constitute the release series number. The series number describes the stable feature set.
- The third number (**34**) is the version number within the release series. This is incremented for each new bugfix release; for an innovation release, it will likely always be 0. For a bugfix series such as MySQL 8.0, the most recent version within the series is the best choice.

After choosing which MySQL version to install, decide which distribution format to install for your operating system. For most use cases, a binary distribution is the right choice. Binary distributions are available in native format for many platforms, such as RPM packages for Linux or DMG packages for macOS. Distributions are also available in more generic formats such as Zip archives or compressed **tar** files. On Windows, you can use [the MySQL Installer](mysql-installer.md) to install a binary distribution.

Under some circumstances, it may be preferable to install MySQL from a source distribution:

- You want to install MySQL at some explicit location. The standard binary distributions are ready to run at any installation location, but you might require even more flexibility to place MySQL components where you want.
- You want to configure [**mysqld**](mysqld.md) with features that might not be included in the standard binary distributions. Here is a list of the most common extra options used to ensure feature availability:
	- [`-DWITH_LIBWRAP=1`](source-configuration-options.md) for TCP wrappers support.
	- [`-DWITH_ZLIB={system|bundled}`](source-configuration-options.md) for features that depend on compression
	- [`-DWITH_DEBUG=1`](source-configuration-options.md) for debugging support
	For additional information, see [Section 2.8.7, “MySQL Source-Configuration Options”](source-configuration-options.md).
- You want to configure [**mysqld**](mysqld.md) without some features that are included in the standard binary distributions.
- You want to read or modify the C and C++ code that makes up MySQL. For this purpose, obtain a source distribution.
- Source distributions contain more tests and examples than binary distributions.