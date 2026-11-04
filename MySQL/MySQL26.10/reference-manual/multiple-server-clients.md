---
title: "MySQL :: MySQL 26.10 Reference Manual :: 7.8.4 Using Client Programs in a Multiple-Server Environment"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/multiple-server-clients.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 7.8.4 Using Client Programs in a Multiple-Server Environment

To connect with a client program to a MySQL server that is listening to different network interfaces from those compiled into your client, you can use one of the following methods:

- Start the client with [``--host=*`host_name`*``](connection-options.md) [``--port=*`port_number`*``](connection-options.md) to connect using TCP/IP to a remote server, with [`--host=127.0.0.1`](connection-options.md) [``--port=*`port_number`*``](connection-options.md) to connect using TCP/IP to a local server, or with [`--host=localhost`](connection-options.md) [``--socket=*`file_name`*``](connection-options.md) to connect to a local server using a Unix socket file or a Windows named pipe.
- Start the client with [`--protocol=TCP`](connection-options.md) to connect using TCP/IP, [`--protocol=SOCKET`](connection-options.md) to connect using a Unix socket file, [`--protocol=PIPE`](connection-options.md) to connect using a named pipe, or [`--protocol=MEMORY`](connection-options.md) to connect using shared memory. For TCP/IP connections, you may also need to specify [`--host`](connection-options.md) and [`--port`](connection-options.md) options. For the other types of connections, you may need to specify a [`--socket`](connection-options.md) option to specify a Unix socket file or Windows named-pipe name, or a [`--shared-memory-base-name`](connection-options.md) option to specify the shared-memory name. Shared-memory connections are supported only on Windows.
- On Unix, set the `MYSQL_UNIX_PORT` and `MYSQL_TCP_PORT` environment variables to point to the Unix socket file and TCP/IP port number before you start your clients. If you normally use a specific socket file or port number, you can place commands to set these environment variables in your `.login` file so that they apply each time you log in. See [Section 6.9, “Environment Variables”](environment-variables.md).
- Specify the default Unix socket file and TCP/IP port number in the `[client]` group of an option file. For example, you can use `C:\my.cnf` on Windows, or the `.my.cnf` file in your home directory on Unix. See [Section 6.2.2.2, “Using Option Files”](option-files.md).
- In a C program, you can specify the socket file or port number arguments in the [`mysql_real_connect()`](https://dev.mysql.com/doc/c-api/26.10/en/mysql-real-connect.html) call. You can also have the program read option files by calling [`mysql_options()`](https://dev.mysql.com/doc/c-api/26.10/en/mysql-options.html). See [C API Basic Function Descriptions](https://dev.mysql.com/doc/c-api/26.10/en/c-api-function-descriptions.html).
- If you are using the Perl `DBD::mysql` module, you can read options from MySQL option files. For example:
	```perl
	$dsn = "DBI:mysql:test;mysql_read_default_group=client;"
	        . "mysql_read_default_file=/usr/local/mysql/data/my.cnf";
	$dbh = DBI->connect($dsn, $user, $password);
	```
	See [Section 31.9, “MySQL Perl API”](apis-perl.md).
	Other programming interfaces may provide similar capabilities for reading option files.