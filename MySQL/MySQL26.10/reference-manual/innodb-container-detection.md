---
title: "MySQL :: MySQL 26.10 Reference Manual :: 17.8.12 Container Detection and Configuration"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/innodb-container-detection.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 17.8.12 Container Detection and Configuration

If installed in a container, the server automatically reads the container's CPU and memory resource limits. The values for the following system variables are calculated and set based on those resource limits:

- The values of the following are calculated based on the number of logical CPUs:
- The values of the following are calculated based on the available memory: