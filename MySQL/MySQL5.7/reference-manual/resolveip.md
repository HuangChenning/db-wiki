---
title: "4.8.4 resolveip — Resolve Host name to IP Address or Vice Versa"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/resolveip.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 4.8.4 resolveip — Resolve Host name to IP Address or Vice Versa

The **resolveip** utility resolves host names to IP addresses and vice versa.

Note

**resolveip** is deprecated and is removed in MySQL 8.0. **nslookup**, **host**, or **dig** can be used instead.

Invoke **resolveip** like this:

```
resolveip [options] {host_name|ip-addr} ...
```

**resolveip** supports the following options.