---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-7-configure-standby-nginx-reverse-proxy.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 7: Configure the Standby NGINX Reverse Proxy

Follow these steps to configure the standby NGINX reverse proxy.

1. If NGINX Reverse Proxy has not already been installed, follow the installation instructions at [https://nginx.org/en/linux\_packages.html](https://nginx.org/en/linux_packages.html).
	As the `root` user, copy the Oracle GoldenGate deployment NGINX configuration files from a primary cluster node to a single standby node directory `/etc/nginx/conf.d`.
	For example:
	```
	[root@dc2north01]# scp dc1north01:/etc/nginx/conf.d/ogg_north.conf
	 /etc/nginx/conf.d
	```
	The standby cluster will need a different CA signed certificate due to using a different VIP name/address than the primary cluster. Contact your systems administrator to follow your corporate standards to create or obtain the server certificate before proceeding. A separate certificate is required for each VIP and Service Manager pair.
2. Install server certificates for NGINX.
	Install the server CA certificates and key files in the `/etc/nginx/ssl` directory, owned by `root` with file permissions 400 (-r--------):
	```
	# mkdir /etc/nginx/ssl
	# chmod 400 /etc/nginx/ssl
	```
	For each reverse proxy configuration file copied from the primary cluster, set the correct file names for the certificate and key file using the following example:
	```
	ssl_certificate /etc/nginx/ssl/gg-stby-vip1.pem;
	ssl_certificate_key /etc/nginx/ssl/gg-stby-vip1.key;
	```
	When using CA signed certificates, the certificate named with the `ssl_certificate` NGINX parameter must include the root, intermediate, and CA signed certificates in a single file. The order is very important, otherwise NGINX fails to start and displays the error message
	`(SSL: error:0B080074:x509 certificate routines:                             X509_check_private_key:key values mismatch).`
	The root and intermediate certificates can be downloaded from the CA signed certificate provider.
	The single file can be generated using the following example command:
	```
	# cat CA_signed_cert.crt intermediate.crt root.crt
	 > gg-stby-vip1.pem
	```
	The `ssl_certificate_key` file is the key file generated when creating the Certificate Signing Request (CSR), which is required when requesting a CA signed certificate.
	Change the `server_name` parameter in the reverse proxy configuration file copied from the primary cluster, setting to the correct VIP name. For example:
	Before:
	server\_name `dc1north-vip1.example.com;`
	After:
	server\_name `dc2north-vip1.example.com;`
3. Validate and restart NGINX.
	Because the VIP will not be running on the standby cluster until the primary database service is running, there is a parameter that needs to be set in the `/etc/sysctl.conf` file.
	1. As the `root` user, make the following modifications to `/etc/sysctl.conf`.
		```
		# vi /etc/sysctl.conf
		```
	2. Add the following parameter:
		```
		# allow processes to bind to the non-local address
		net.ipv4.ip_nonlocal_bind = 1
		```
	3. Reload the modified configuration:
		```
		# sysctl -p /etc/sysctl.conf
		```
	4. Validate the NGINX configuration file to detect any errors in the configuration. If there are errors in the file, they will be reported by the following command.
		```
		# nginx -t
		nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
		nginx: configuration file /etc/nginx/nginxconf test is successful
		```
	5. Restart NGINX with the new configuration:
		```
		# systemctl restart nginx
		```
	When the NGINX configuration is complete, copy the configuration file and certificates to matching directories on the other standby cluster nodes.
4. Oracle Clusterware needs to have control over starting the NGINX reverse proxy so that it can be started automatically before the GoldenGate deployments are started.
	The NGINX resource is created with a dependency on the underlying network CRS resource, the name of which can be determined using the following command:
	```
	$ $GRID_HOME/bin/crsctl stat res -w "TYPE == ora.network.type"|grep NAME
	NAME=ora.net1.network
	```
	1. As the `root` user, use the following example command to create a Clusterware resource to manage NGINX.
		```
		# $GRID_HOME/bin/crsctl add resource nginx -type generic_application
		 -attr "ACL='owner:root:rwx,pgrp:root:rwx,other::r--,group:oinstall:r-x,user:oracle:rwx',EXECUTABLE_NAMES=nginx,START_PROGRAM='/bin/systemctl
		 start -f nginx',STOP_PROGRAM='/bin/systemctl
		 stop -f nginx',CHECK_PROGRAMS='/bin/systemctl
		 status nginx' ,START_DEPENDENCIES='hard(ora.net1.network) pullup(ora.net1.network)',
		 STOP_DEPENDENCIES='hard(intermediate:ora.net1.network)',
		 RESTART_ATTEMPTS=0, HOSTING_MEMBERS='dc1north01,dc1north02', CARDINALITY=2"
		```
		The NGINX resource created in this example runs on the named cluster nodes at the same time, specified by `HOSTING_MEMBERS`. This is recommended when multiple GoldenGate Service Manager deployments are configured, and they can independently move between cluster nodes.
	2. When the NGINX Clusterware resource is created, alter the GoldenGate XAG resources so that NGINX must be started before the GoldenGate deployments are started.
		As the `root` user, modify the XAG resources using the following example commands.
		Determine the current `--filesystems` parameter:
		```
		# agctl config goldengate GGNORTH | grep "File System"
		File System resources needed: dbfsgg
		```