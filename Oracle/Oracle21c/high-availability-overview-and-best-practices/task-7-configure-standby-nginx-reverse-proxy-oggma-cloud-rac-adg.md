---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-7-configure-standby-nginx-reverse-proxy-oggma-cloud-rac-adg.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 7 - Configure Standby NGINX Reverse Proxy

The Oracle GoldenGate reverse proxy feature allows a single point of contact for all of the Oracle GoldenGate microservices associated with an Oracle GoldenGate deployment.

Without reverse proxy, the GoldenGate deployment microservices are contacted using a URL consisting of a host name or IP address and separate port numbers, one for each of the services. Reverse proxy is mandatory to ensure easy access to microservices and provide enhanced security and manageability.

Perform the following steps to complete this task:

- Step 7.1 - Install NGINX Reverse Proxy
- Step 7.2 - Copy NGINX Configuration Files from the Primary System
- Step 7.3 - Install Server Certificates for NGINX
- Step 7.4 - Test and Reload the New NGINX Configuration
- Step 7.5 - Distribute the GoldenGate NGINX Configuration Files
- Step 7.6 - Create a Clusterware Resource to Manage NGINX

Step 7.1 - Install NGINX Reverse Proxy

On the standby system, follow the instructions in “Step 8.1 - Install NGINX Reverse Proxy Server” of [Task 8 - Configure NGINX Reverse Proxy](task-8-configure-nginx-reverse-proxy1.md) to install NGINX.

Step 7.2 - Copy NGINX Configuration Files from the Primary System

1. As the `opc` user on the standby system, copy the NGINX configuration file from the primary to the standby database system:
	```
	[opc@standby_node_1 ~]$ scp 
	primary_node_1.oracle.com:/etc/nginx/conf.d/ogg_<deployment_name>.conf
	 /tmp
	```
2. As the `root` user on the standby system, copy the NGINX configuration file from the directory `/tmp` to the directory `/etc/nginx/conf.d`:
	```
	[opc@exastb-node1 ~]$ sudo su -
	[root@exastb-node1 ~]# cp /tmp/ogg_<deployment_name>.conf /etc/nginx/conf.d
	```

Step 7.3 - Install Server Certificates for NGINX

The standby system will need a different CA signed certificate due to using a different VIP name/address than the primary system. Contact your systems administrator to follow your corporate standards to create or obtain the server certificate before proceeding. A separate certificate is required for each VIP and Service Manager pair.

1. As the `root` user on the standby system, copy the server CA certificates and key files in the `/etc/nginx/ssl` directory, owned by `root` with file permissions 400 (-r--------):
	```
	[opc@exastb-node1 ~]$ sudo su -
	[root@exastb-node1 ~]# mkdir /etc/nginx/ssl
	[root@exastb-node1 ~]# chmod 400 /etc/nginx/ssl
	```
2. As the `root` user on the standby system, set the correct filenames for the certificate and key file to match the same the filenames in the NGINX configuration file:
	```
	[root@exastb-node1 ~]# grep
	 ssl_certificate /etc/nginx/conf.d/ogg_<deployment_name>.conf
	    ssl_certificate         /etc/nginx/ssl/server.chained.crt;
	    ssl_certificate_key     /etc/nginx/ssl/server.key;
	```
	Note:
	If you have copied multiple reverse proxy configuration files copied from the primary system, you will need to repeat this process for each file.
	When using CA signed certificates, the certificate named with the `ssl_certificate` NGINX parameter must include the 1) CA signed, 2) intermediate and 3) root certificates in a single file. The order is very important, otherwise NGINX fails to start and displays the error message:
	`(SSL: error:0B080074:x509                                                   certificate routines: X509_check_private_key:key                                                   values mismatch).`
	The root and intermediate certificates can be downloaded from the CA signed certificate provider.
	The single file can be generated using the following example command:
	```
	[root@exastb-node1 ~]# cat CA_signed_cert.crt intermediate.crt root.crt >
	 /etc/nginx/ssl/server.chained.crt
	```
	The `ssl_certificate_key` file is the key file generated when creating the Certificate Signing Request (CSR), which is required when requesting a CA signed certificate.
3. As the `root` user on the standby system, change the `server_name` parameter to the correct VIP name in the reverse proxy configuration file copied from the primary system:
	```
	[root@exastb-node1 ~]# vi /etc/nginx/conf.d/ogg_<deployment_name>.conf
	# Before:
	server_name             exapri-vip.oracle.com;
	# After:
	server_name             exastb-vip.oracle.com;
	```

Step 7.4 - Test and Reload the New NGINX Configuration

Because the VIP will not be running on the standby system until the primary database service is running, there is a parameter that needs to be set in the `/etc/sysctl.conf` file.

1. As the `opc` user on the standby system, add the following parameter to the file `/etc/sysctl.conf`:
	```
	[opc@exastb-node1 ~]$ sudo vi /etc/sysctl.conf
	# allow processes to bind to the non-local address
	net.ipv4.ip_nonlocal_bind = 1
	```
2. As the `opc` user on the standby system, distribute the `/etc/sysctl.conf` file:
	```
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc
	 -d /tmp -f /etc/sysctl.conf
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo
	 cp /tmp/sysctl.conf /etc/sysctl.conf
	```
3. As the `opc` user on the standby system, reload the modified configuration:
	```
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo sysctl
	 -p /etc/sysctl.conf
	```
4. As the `opc` user on the standby system, validate the NGINX configuration file to detect any errors in the configuration. If there are errors in the file, they will be reported by the following command:
	```
	[opc@exastb-node1 ~]$ sudo nginx -t
	nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
	nginx: configuration file /etc/nginx/nginxconf test is successful
	```
5. As the `opc` user on the standby system, restart NGINX with the new configuration:
	```
	[opc@exastb-node1 ~]$ sudo systemctl restart nginx
	```

Step 7.5 - Distribute the GoldenGate NGINX Configuration Files

Once all the reverse proxy configuration files have been created for the GoldenGate Service Managers, they need to be copied to all the database nodes.

1. As the `opc` OS user on the standby system, distribute the NGINX configuration files to all the database nodes:
	```
	[opc@exastb-node1 ~]$ sudo tar fczP nginx_conf.tar
	 /etc/nginx/conf.d/ /etc/nginx/ssl/
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc
	 -d /tmp -f nginx_conf.tar
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc
	 sudo tar fxzP /tmp/nginx_conf.tar
	```
2. As the `opc` OS user on the standby system, test the new NGINX configuration on all nodes the new configuration files were copied to:
	```
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo nginx -t
	 
	exastb-node1: nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
	exastb-node1: nginx: configuration file /etc/nginx/nginx.conf test is successful
	exastb-node2: nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
	exastb-node2: nginx: configuration file /etc/nginx/nginx.conf test is successful
	```
3. As the `opc` OS user on the standby system, restart NGINX to load the new configuration on all nodes:
	```
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc
	 sudo systemctl restart nginx
	```

Step 7.6 - Create a Clusterware Resource to Manage NGINX

Oracle Clusterware needs to have control over starting the NGINX reverse proxy so that it can be started automatically before the GoldenGate deployments are started.

1. As the `grid` OS user on the standby system, use the following command to get the network CRS resource name required to create the NGINX resource with a dependency on the underlying network CRS resource:
	```
	[opc@exastb-node1 ~]$ sudo su - grid
	[grid@exastb-node1 ~]$ crsctl stat res -w "TYPE == ora.network.type"|grep NAME
	NAME=ora.net1.network
	```
2. As the `root` user on the standby system, use the following example command to create a Clusterware resource to manage NGINX. Replace `HOSTING_MEMBERS` and `CARDINALITY` to match your environment:
	```
	[opc@exastb-node1 ~]$ sudo su -
	[root@exastb-node1 ~]# $(grep ^crs_home /etc/oracle/olr.loc | cut -d=
	 -f2)/bin/crsctl add resource nginx -type generic_application -attr
	 "ACL='owner:root:rwx,pgrp:root:rwx,other::r--,group:oinstall:r-x,user:oracle:rwx',
	EXECUTABLE_NAMES=nginx,START_PROGRAM='/bin/systemctl start -f nginx',
	STOP_PROGRAM='/bin/systemctl stop -f nginx',
	CHECK_PROGRAMS='/bin/systemctl status nginx' ,
	START_DEPENDENCIES='hard(ora.net1.network) pullup(ora.net1.network)', 
	STOP_DEPENDENCIES='hard(intermediate:ora.net1.network)', RESTART_ATTEMPTS=0, 
	HOSTING_MEMBERS='<exastb-node1, exastb-node2>', CARDINALITY=2"
	```

The NGINX resource created in this example will run on the named database nodes at the same time, specified by `HOSTING_MEMBERS`. This is recommended when multiple GoldenGate Service Manager deployments are configured, and they can independently move between database nodes.