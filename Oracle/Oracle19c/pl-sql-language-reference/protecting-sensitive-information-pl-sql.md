---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/protecting-sensitive-information-pl-sql.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Protecting Sensitive Information in PL/SQL

Data security should be a top priority during any application development. There are several ways you can mitigate the risk of vulnerabilities while using PL/SQL.

Be aware that the content of a PL/SQL block may be written in its entirety in such places as audit logs and trace files. Similarly, stored procedure code can be accessed through dictionary views, such as `USER_SOURCE`. For this reason, it is strongly recommended that you never include any sensitive information in a literal seen in PL/SQL code.

Bind variables can be used to help protect against SQL injection attacks, however, bind values can be visible in places such as trace files, audit, and `V$SQL` and related views. Access should be strictly managed to ensure that only those who require it have privileges to view this particularly sensitive information. For more information about using bind variables, see " [Bind Variables](sql-injection.md) ".