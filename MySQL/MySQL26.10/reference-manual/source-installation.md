---
title: "MySQL :: MySQL 26.10 Reference Manual :: 2.8 Installing MySQL from Source"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/source-installation.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 2.8 Installing MySQL from Source

Building MySQL from the source code enables you to customize build parameters, compiler optimizations, and installation location. For a list of systems on which MySQL is known to run, see [https://www.mysql.com/support/supportedplatforms/database.html](https://www.mysql.com/support/supportedplatforms/database.html).

Before you proceed with an installation from source, check whether Oracle produces a precompiled binary distribution for your platform and whether it works for you. We put a great deal of effort into ensuring that our binaries are built with the best possible options for optimal performance. Instructions for installing binary distributions are available in [Section 2.2, “Installing MySQL on Unix/Linux Using Generic Binaries”](binary-installation.md).

If you are interested in building MySQL from a source distribution using build options the same as or similar to those use by Oracle to produce binary distributions on your platform, obtain a binary distribution, unpack it, and look in the `docs/INFO_BIN` file, which contains information about how that MySQL distribution was configured and compiled.

Warning

Building MySQL with nonstandard options may lead to reduced functionality, performance, or security.

The MySQL source code contains internal documentation written using Doxygen. The generated Doxygen content is available at [https://dev.mysql.com/doc/index-other.html](https://dev.mysql.com/doc/index-other.html). It is also possible to generate this content locally from a MySQL source distribution using the instructions at [Section 2.8.10, “Generating MySQL Doxygen Documentation Content”](source-installation-doxygen.md).