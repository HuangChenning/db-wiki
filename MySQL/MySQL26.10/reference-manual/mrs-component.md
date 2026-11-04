---
title: "MySQL :: MySQL 26.10 Reference Manual :: 7.5.10 MySQL REST Service Component"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/mrs-component.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 7.5.10 MySQL REST Service Component

MySQL REST Service component is an HTTPS data-access layer providing relational-to-JSON mapping, authentication, and authorization This component embeds MySQL REST Service in MySQL Server and exposes published REST services over HTTPS. This enables MySQL Server to serve as the application’s HTTPS API without a separate MySQL Router deployment to host MySQL REST Service. Database operations execute through local Server services, avoiding the network hop between a separate runtime and MySQL.

- Purpose: Hosts MySQL REST Service inside MySQL Server.
- URN: `file://component_mysql_rest_service`

The component does not support MySQL REST Service developer mode and serves only published REST services. This document does not describe MySQL REST Service, just the configuration of the MySQL REST Service component in MySQL Server. For information on MySQL REST Service, see [MySQL REST Service Reference Manual](https://dev.mysql.com/doc/dev/mysql-rest-service/latest/).