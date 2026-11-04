---
title: "MySQL :: MySQL 26.7 Reference Manual :: 7.5.7 Multilingual Engine Component (MLE)"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/mle-component.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 7.5.7 Multilingual Engine Component (MLE)

The Multilingual Engine component (MLE) provides support for languages other than SQL in MySQL stored procedures and functions. The MLE Component is available as part of MySQL Enterprise Edition.

With the MLE component in MySQL 26.7, you can create and execute MySQL stored programs written in JavaScript. For more information about these, see [Section 27.3, “JavaScript Stored Programs”](stored-routines-js.md). For general information about MySQL stored routines, see [Section 27.2, “Using Stored Routines”](stored-routines.md).

- Purpose: Provide support for languages other than SQL in stored functions and stored procedures. In MySQL 26.7, only JavaScript (ECMAScript) is supported by MLE.
- URN: `file://component_mle`

For installation instructions, see [Section 7.5.1, “Installing and Uninstalling Components”](component-loading.md).

The MLE component is available on all platforms supported by MySQL Enterprise Edition, except for Solaris. See [Supported Platforms](https://www.mysql.com/support/supportedplatforms/database.html) for more information.

Note

You should be aware that not all MySQL 26.7 installations support removal of the MLE component. If your installation supports it, you can remove the component using [`UNINSTALL COMPONENT`](uninstall-component.md). See [Section 7.5.1, “Installing and Uninstalling Components”](component-loading.md), for information about how to do this.

For MySQL installations supporting the uninstallation of the MLE component, you should be aware that it is not possible to perform the uninstallation from within a user session that has created or executed any JavaScript stored procedures. For this reason, we recommend that you create and execute JavaScript stored procedures in a session separate from that used to install the MLE component; in this case it is possible, after exiting the session in which JavaScript stored procedures were created or used, to uninstall the component in a separate session.