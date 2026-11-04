---
title: "17.8.12 Container Detection and Configuration"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/innodb-container-detection.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 17.8.12 Container Detection and Configuration

If installed in a container, the server automatically reads the container's CPU and memory resource limits. The values for the following system variables are calculated and set based on those resource limits:

- The values of the following are calculated based on the number of logical CPUs:
- The values of the following are calculated based on the available memory: