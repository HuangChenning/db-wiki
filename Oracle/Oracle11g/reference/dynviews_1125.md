---
title: "V$ENCRYPTION_WALLET"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1125.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ENCRYPTION_WALLET` displays information on the status of the wallet and the wallet location for transparent data encryption.

| Column | Datatype | Description |
| --- | --- | --- |
| `WRL_TYPE` | `VARCHAR2(20)` | Type of the wallet resource locator (for example, `FILE`) |
| `WRL_PARAMETER` | `VARCHAR2(4000)` | Parameter of the wallet resource locator (for example, absolute filename if `WRL_TYPE` = `FILE`) |
| `STATUS` | `VARCHAR2(9)` | Status of the wallet: |