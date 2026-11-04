---
title: DBMS_AQIN
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_aquin.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 25 DBMS\_AQIN

The `DBMS_AQIN` package plays a part in providing secure access to the Oracle JMS interfaces.

See Also:

[Oracle Streams Advanced Queuing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11013/toc.htm) for detailed information about `DBMS_AQIN`

This chapter contains the following topic:

- Using DBMS\_AQIN
	- Over view

---

## Using DBMS\_AQIN

This section contains topics which relate to using the `DBMS_AQIN` package.

- Overview

---

### Overview

While you should not call any subprograms in the `DBMS_AQIN` package directly, you must have the `EXECUTE` privilege on the `DBMS_AQIN` and `DBMS_AQJMS` packages to use the Oracle JMS interfaces. Use the following syntax to accomplish this with regard to the `DBMS_AQIN` package:

```
GRANT EXECUTE ON DBMS_AQIN to user;
```

Note that you can also acquire these rights through the `AQ_USER_ROLE` or the `AQ_ADMINSTRATOR_ROLE`.