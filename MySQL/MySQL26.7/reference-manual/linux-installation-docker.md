---
title: "MySQL :: MySQL 26.7 Reference Manual :: 2.5.6 Deploying MySQL on Linux with Docker Containers"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/linux-installation-docker.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 2.5.6 Deploying MySQL on Linux with Docker Containers

This section explains how to deploy MySQL Server using Docker containers.

While the `docker` client is used in the following instructions for demonstration purposes, in general, the MySQL container images provided by Oracle work with any container tools that are compliant with the [OCI 1.0 specification](https://opencontainers.org/posts/announcements/2021-05-04-oci-dist-spec-v1/).

Warning

Before deploying MySQL with Docker containers, make sure you understand the security risks of running containers and mitigate them properly.