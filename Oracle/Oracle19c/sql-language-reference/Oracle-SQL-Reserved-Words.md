---
title: Oracle SQL Reserved Words
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Oracle-SQL-Reserved-Words.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

This section lists Oracle SQL reserved words. You cannot use Oracle SQL reserved words as nonquoted identifiers. Quoted identifiers can be reserved words, although this is not recommended.

**Note:** In addition to the following reserved words, Oracle uses system-generated names beginning with “ `SYS_` ” for implicitly generated schema objects and subobjects. Oracle discourages you from using this prefix in the names you explicitly provide to your schema objects and subobjects to avoid possible conflict in name resolution.

The `V$RESERVED_WORDS` data dictionary view provides additional information on each reserved word, including whether it is always reserved or is reserved only for particular uses. Refer to [*Oracle Database Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=REFRN30204) for more information.

Words followed by an asterisk (\*) are also ANSI reserved words.

- `ACCESS`
- `ADD`
- `ALL *`
- `ALTER *`
- `AND *`
- `ANY *`
- `AS *`
- `ASC`
- `AUDIT`
- `BETWEEN *`
- `BY *`
- `CHAR *`
- `CHECK *`
- `CLUSTER`
- `COLUMN` \*
- `COLUMN_VALUE` (See Note 1 at the end of this list)