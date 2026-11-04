---
title: DBV-00200 to DBV-00201
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/dbvus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 39 DBV-00200 to DBV-00201

DBV-00200: Block, DBA number, already marked corrupt

Cause: The block was previously corrupted. It has been marked as corrupt by the Oracle database server.

Action: If the block is not currently allocated to a database object, then no action is required. If the block is allocated, then the options and required action depend on the type and nature of the object which owns the block. To repair an allocated block, perform block or file media recovery.

DBV-00201: Block, DBA number, marked corrupt for invalid redo application

Cause: The block was marked corrupt by the Oracle database server for invalid redo application, ex: media recovery of a NOLOGGING object or direct loaded data.

Action: If the block is not currently allocated to a database object, then no action is required. If the block is allocated, then the object will need to be rebuilt, or data to be reloaded.