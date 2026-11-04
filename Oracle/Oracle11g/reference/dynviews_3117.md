---
title: "V$TYPE_SIZE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3117.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TYPE_SIZE` displays the sizes of various database components for use in estimating data block capacity.

| Column | Datatype | Description |
| --- | --- | --- |
| `COMPONENT` | `VARCHAR2(8)` | Component name, such as segment or buffer header |
| `TYPE` | `VARCHAR2(8)` | Component type |
| `DESCRIPTION` | `VARCHAR2(32)` | Description of the component |
| `TYPE_SIZE` | `NUMBER` | Size of the component |