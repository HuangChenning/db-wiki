---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_AQIN.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 27 DBMS\_AQIN

The `DBMS_AQIN` package plays a part in providing secure access to the Oracle JMS interfaces.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADQUE0400) for detailed information about `DBMS_AQIN`

This chapter contains the following topic:

- Security Model

### 27.1 DBMS\_AQIN Security Model

While you should not call any subprograms in the `DBMS_AQIN` package directly, you must have the `EXECUTE` privilege on the `DBMS_AQIN` and `DBMS_AQJMS` packages to use the Oracle JMS interfaces.

Use the following syntax to accomplish this with regard to the `DBMS_AQIN` package:

```
GRANT EXECUTE ON DBMS_AQIN to user;
```

You must have `EXECUTE` privilege on the `DBMS_AQIN` and `DBMS_AQJMS` packages to use the Oracle JMS interfaces. You can also acquire these rights through the `AQ_USER_ROLE` or the `AQ_ADMINSTRATOR_ROLE`.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADQUE2541) for more information on accessing standard and Oracle JMS applications.