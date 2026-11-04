---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/pl-sql-source-text-wrapping-limitations.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## PL/SQL Source Text Wrapping Limitations

- Wrapped files are not downward-compatible between Oracle Database releases.
	For example, you cannot load files produced by the version n.1 PL/SQL Wrapper utility into a version (n-1).2 Oracle Database. Nor can you load files produced by the version n.2 PL/SQL Wrapper utility into a version n.1 Oracle Database. Wrapped files are both upward- and downward-compatible across patch sets.
- Wrapping PL/SQL source text is not a secure way to hide passwords or table names.
	For high-assurance security, use Oracle Database Vault, described in [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=DVADM-GUID-0C8AF1B2-6CE9-4408-BFB3-7B2C7F9E7284).
- You cannot wrap the PL/SQL source text of triggers.
	To hide the implementation details of a trigger, put them in a stored subprogram, wrap the subprogram, and write a one-line trigger that invokes the subprogram.