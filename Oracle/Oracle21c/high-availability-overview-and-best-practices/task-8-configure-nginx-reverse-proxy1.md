---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-8-configure-nginx-reverse-proxy1.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 8 - Configure NGINX Reverse Proxy

The Oracle GoldenGate reverse proxy feature allows a single point of contact for all of the Oracle GoldenGate Microservices associated with an Oracle GoldenGate deployment.

Without a reverse proxy, the Oracle GoldenGate deployment microservices are contacted using a URL consisting of a host name or IP address and separate port numbers, one for each of the services.

For example, to contact the Service Manager, you could use http://gghub.example.com:9100, then the Administration Server is http://gghub.example.com:9101, the second Service Manager may be accessed using http://gghub.example.com:9110, and so on.

When running Oracle GoldenGate in a High Availability (HA) configuration on Oracle Exadata Database Service with the Grid Infrastructure agent (XAG), there is a limitation preventing more than one deployment from being managed by a GoldenGate Service Manager. Because of this limitation, creating a separate virtual IP address (VIP) for each Service Manager and deployment pair is recommended. This way, the microservices can be accessed directly using the VIP.

With a reverse proxy, port numbers are not required to connect to the microservices because they are replaced with the deployment name and the host name’s VIP. For example, to connect to the console with a web browser, use the URLs.

| Service | URL |
| --- | --- |
| Service Manager | https://localhost:localPort |
| Administration Server | https://localhost:localPort/instance\_name/adminsrvr |
| Distribution Server | https://localhost:localPort/instance\_name/distsrvr |
| Performance Metric Server | https://localhost:localPort/instance\_name/pmsrvr |
| Receiver Server | https://localhost:localPort/instance\_name/recvsrvr |

Note:

To connect to Oracle GoldenGate in OCI, you must create a bastion and an SSH port forwarding session (see Step 6.1). After this, you can connect to the Oracle GoldenGate Services using https://locahost:\<localPort>.

A reverse proxy is mandatory to ensure easy access to microservices and enhance security and manageability.

Follow the instructions to install and configure NGINX Reverse Proxy with an SSL connection and ensure all external communication is secure.

Note:

When using CA Signed Certificates with NGINX, make sure the NGINX `ssl_certificate` parameter points to a certificate file that contains the certificates in the correct order of CA signed certificate, intermediate certificate, and root certificate.

Perform the following steps to complete this task:

- Step 8.1 - Install NGINX
- Step 8.2 - Configure NGINX Reverse Proxy
- Step 8.3 - Securing GoldenGate Microservices to Restrict Non-secure Direct Access
- Step 8.4 - Create a Clusterware Resource to Manage NGINX

Step 8.1 - Install NGINX Reverse Proxy Server

1. As the `root` OS user on all nodes, set up the YUM repository by creating the file `/etc/yum.repos.d/nginx.repo` with the following contents:
	```
	[opc@exadb-node1 ~]$ sudo su -
	[root@exadb-node1 ~]# cat > /etc/yum.repos.d/nginx.repo <<EOF
	[nginx-stable]
	name=nginx stable repo
	baseurl=http://nginx.org/packages/rhel/7/\$basearch/
	gpgcheck=1
	enabled=1
	gpgkey=https://nginx.org/keys/nginx_signing.key
	module_hotfixes=true
	EOF
	```
2. As the `root` OS user, run the following commands to install, enable, and start NGINX:
	```
	[root@exadb-node1 ~]# yum install -y python-requests python-urllib3 nginx
	[root@exadb-node1 ~]# systemctl enable nginx
	```
3. As the `root` OS user, disable the NGINX repository after the software has been installed:
	```
	[root@exadb-node1 ~]# yum-config-manager --disable nginx-stable
	```

Step 8.2 - Configure NGINX Reverse Proxy

A separate reverse proxy configuration is required for each Oracle GoldenGate Home.

When running multiple Service Managers, the following instructions will provide configuration using a separate VIP for each Service Manager. NGINX uses the VIP to determine which Service Manager an HTTPS connection request is routed to.

An SSL certificate is required for clients to authenticate the server they connect to through NGINX. Contact your systems administrator to follow your corporate standards to create or obtain the server certificate before proceeding. A separate certificate is required for each VIP and Service Manager pair.

Note:

The common name in the CA-signed certificate must match the target hostname/VIP used by NGINX.

Perform the following sub-steps to complete this step:

- Step 8.2.1 - Create the NGINX Configuration File
- Step 8.2.2 - Modify NGINX Configuration Files
- Step 8.2.3 - Install Server Certificates for NGINX
- Step 8.2.4 - Install the NGINX Configuration File
- Step 8.2.5 - Test the New NGINX Configuration
- Step 8.2.6 - Reload NGINX and the New Configuration
- Step 8.2.7 - Test GoldenGate Microservices Connectivity
- Step 8.2.8 - Distribute the GoldenGate NGINX Configuration Files

Step 8.2.1 - Create the NGINX Configuration File

You can configure Oracle GoldenGate Microservices Architecture to use a reverse proxy. Oracle GoldenGate Microservices Architecture includes a script called `ReverseProxySettings` that generates a configuration file for only the NGINX reverse proxy server.

The script requires the following parameters:

- The `--user` parameter should mirror the GoldenGate administrator account specified with the initial deployment creation.
- The GoldenGate administrator password will be prompted.
- The reverse proxy port number specified by the `--port` parameter should be the default HTTPS port number (443) unless you are running multiple GoldenGate Service Managers using the same `--host`. In this case, specify an HTTPS port number that does not conflict with previous Service Manager reverse proxy configurations.
	For example, if you are running two Service Managers using the same hostname/VIP, the first reverse proxy configuration is created with `--port 443 --host hostvip01`, and the second is created with `--port 444 --host hostvip01`.
	If you are using separate hostnames/VIPs, the two Service Manager reverse proxy configurations would be created with `--port 443 --host                             hostvip01` and `--port 443 --host                     hostvip02`.
- Lastly, the HTTP port number (9100) should match the Service Manager port number specified during the deployment creation.

Repeat this step for each additional GoldenGate Service Manager.

As the `oracle` OS user, use the following command to create the Oracle GoldenGate NGINX configuration file:

```
[opc@exadb-node1 ~]$ sudo su - oracle
[oracle@exadb-node1 ~]$ export OGG_HOME=/u02/app/oracle/goldengate/gg21c
[oracle@exadb-node1 ~]$ export PATH=$PATH:$OGG_HOME/bin
[oracle@exadb-node1 ~]$ cd /u02/app_acfs/goldengate
[oracle@exadb-node1 ~]$ $OGG_HOME/lib/utl/reverseproxy/ReverseProxySettings
 --user oggadmin --port 443 --output ogg_<instance_name>.conf http://localhost:9100
 --host <VIP hostname/IP>
Password: <oggadmin_password>
```

Step 8.2.2 - Modify NGINX Configuration Files

When multiple GoldenGate Service Managers are configured to use their IP/VIPs with the same HTTPS 443 port, some small changes are required to the NGINX reverse proxy configuration files generated in the previous step.

With all Service Managers sharing the same port number, they are independently accessed using their VIP/IP specified by the `--host` parameter.

1. As the `oracle` OS user, determine the deployment name managed by this Service Manager. If not already known, the deployment name is listed in the reverse proxy configuration file:
	```
	[opc@exadb-node1 ~]$ sudo su - oracle
	[oracle@exadb-node1 ~]$ cd /u02/app_acfs/goldengate
	[oracle@exadb-node1 ~]$ grep "Upstream Servers" ogg_<instance_name>.conf
	## Upstream Servers for Deployment '<instance_name>'
	```
	In this example, the deployment is called `SOURCE`.
2. As the `oracle` OS user, change all occurrences of `_ServiceManager` by prepending the deployment name before the underscore:
	```
	$ sed -i 's/_ServiceManager/<instance_name>_ServiceManager/'
	        ogg_<instance_name>.conf
	```

Step 8.2.3 - Install Server Certificates for NGINX

1. As the `root` OS user, copy the server certificates and key files in the `/etc/nginx/ssl` directory, owned by `root` with file permissions 400 (-r--------):
	```
	[opc@exadb-node1 ~]$ sudo su -
	[root@exadb-node1 ~]# mkdir /etc/nginx/ssl
	[root@exadb-node1 ~]# chmod 400 /etc/nginx/ssl
	```
2. As the `root` OS user, set the correct filenames for the certificate and key files for each reverse proxy configuration file generated in Step 8.2.1:
	```
	[oracle@exadb-node1 ~]$ vi /u02/app_acfs/goldengate/ogg_<instance_name>.conf
	# Before
	    ssl_certificate         /etc/nginx/ogg.pem;
	    ssl_certificate_key     /etc/nginx/ogg.pem;
	# After
	    ssl_certificate         /etc/nginx/ssl/server.chained.crt;
	    ssl_certificate_key     /etc/nginx/ssl/server.key;
	```

When using CA-signed certificates, the certificate named with the `ssl_certificate` NGINX parameter must include the 1) CA signed, 2) intermediate, and 3) root certificates in a single file. The order is significant; otherwise, NGINX fails to start and displays the error message:

`(SSL: error:0B080074:x509 certificate routines:                     X509_check_private_key:key values mismatch)`

The root and intermediate certificates can be downloaded from the CA-signed certificate provider.

The SSL certificate single file can be generated using the following example command:

```
[root@exadb-node1 ~]# cat
 CA_signed_cert.crt intermediate.crt root.crt > server.chained.crt
```

The `ssl_certificate_key` file is generated when creating the Certificate Signing Request (CSR), which is required when requesting a CA-signed certificate.

Step 8.2.4 - Install the NGINX Configuration File

As the `root` OS user, copy the deployment configuration file (or files if multiple files were created in Step 8.2.1) to `/etc/nginx/conf.d` directory:

```
[root@exadb-node1 ~]# mv /u02/app_acfs/goldengate/ogg_<instance_name>.conf
 /etc/nginx/conf.d
```

Step 8.2.5 - Test the New NGINX Configuration

As the `root` OS user, validate the NGINX configuration file.

If there are errors in the file, they will be reported with the following command:

```
[root@exadb-node1 ~]# nginx -t

nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginxconf test is successful
```

Step 8.2.6 - Reload NGINX and the New Configuration

As the `root` OS user, restart NGINX to load the new configuration:

```
[root@exadb-node1 ~]# systemctl restart nginx
```
Step 8.2.7 - Test GoldenGate Microservices Connectivity
1. As the `root` OS user, create a curl configuration file (`access.cfg`) that contains the deployment username and password:
	```
	[root@exadb-node1 ~]# vi access.cfg
	user = "oggadmin:<password>"
	```
2. As the `root` OS user, query the health of the deployments using the following command:
	```
	[root@exadb-node1 ~]# curl -svf
	 -K access.cfg https://<VIP hostname/IP>:<port#>/services/v2/config/health
	 -XGET && echo -e "\n*** Success"
	```
	Sample output:
	```
	{"$schema":"api:standardResponse","links":
	[{"rel":"canonical","href":"https://gg-prmy-vip1/services/v2/config/health",
	"mediaType":"application/json"},
	{"rel":"self","href":"https://gg-prmy-vip1/services/v2/config/health",
	"mediaType":"application/json"},{"rel":"describedby",
	"href":"https://gg-prmy-vip1/services/ServiceManager/v2/metadata-catalog/health",
	"mediaType":"application/schema+json"}],"messages":[],
	"response":{"$schema":"ogg:health","deploymentName":"ServiceManager",
	"serviceName":"ServiceManager","started":"2021-12-09T23:33:03.425Z","healthy":true,
	"criticalResources":[{"deploymentName":"SOURCE","name":"adminsrvr","type":"service",
	"status":"running","healthy":true},{"deploymentName":"SOURCE","name":"distsrvr",
	"type":"service","status":"running","healthy":true},
	{"deploymentName":"SOURCE","name":"recvsrvr","type":"service","status":"running",
	"healthy":true}]}}
	*** Success ***
	```
3. As the `root` OS user, remove the `curl` configuration file (`access.cfg`) that contains the deployment username and password:
	```
	[root@exadb-node1 ~]# rm access.cfg
	rm: remove regular file ‘access.cfg’? y
	```
Step 8.2.8 - Distribute the GoldenGate NGINX Configuration Files

When all of the reverse proxy configuration files have been created for the GoldenGate Service Managers, they must be copied to all the database nodes.

1. As the `opc` OS user, distribute the NGINX configuration files to all database nodes:
	```
	[opc@exadb-node1 ~]$ sudo tar fczP nginx_conf.tar
	 /etc/nginx/conf.d/ /etc/nginx/ssl/
	[opc@exadb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc -d /tmp
	 -f nginx_conf.tar
	[opc@exadb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo tar fxzP
	 /tmp/nginx_conf.tar
	```
2. As the `opc` OS user, test the new NGINX configuration on all nodes the new configuration files were copied to:
	```
	[opc@exadb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo nginx -t
	exadb-node1: nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
	exadb-node1: nginx: configuration file /etc/nginx/nginx.conf test is successful
	exadb-node2: nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
	exadb-node2: nginx: configuration file /etc/nginx/nginx.conf test is successful
	```
3. As the `opc` OS user, restart NGINX to load the new configuration on all nodes:
	```
	[opc@exadb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo systemctl
	 restart nginx
	```

Step 8.3 - Securing GoldenGate Microservices to Restrict Non-secure Direct Access

After configuring the NGINX reverse proxy with an unsecured Oracle GoldenGate Microservices deployment, the microservices can continue accessing HTTP (non-secure) using the configured microservices port numbers.

For example, the following non-secure URL could be used to access the Administration Server: `http://<vip-name>:9101`.

Oracle GoldenGate Microservices' default behavior for each server (Service Manager, `adminserver`, `pmsrvr`. `distsrvr`, and `recsrvr`) is to listen using a configured port number on all network interfaces. This is undesirable for more secure installations, where direct access using HTTP to the microservices needs to be disabled and only permitted using NGINX HTTPS.

Use the following commands to alter the Service Manager and deployment services listener address to use only the localhost address. Access to the Oracle GoldenGate Microservices will only be permitted from the localhost, and any access outside of the localhost will only succeed using the NGINX HTTPS port.

Step 8.3.1 - Stop the Service Manager

As the `grid` OS user, stop the service manager:

```
[opc@exadb-node1 ~]$ sudo su - grid
[grid@exadb-node1 ~]$ agctl stop goldengate <instance_name>
[grid@exadb-node1 ~]$ agctl status goldengate
Goldengate  instance '<instance_name>' is not running
```

Step 8.3.2 - Modify the Service Manager Listener Address

As the `oracle` OS user, modify the listener address with the following commands.

Use the correct port number for the Service Manager being altered. The server will fail to start, ignore the error, and proceed with the next step:

```
[opc@exadb-node1 ~]$ sudo su - oracle
[oracle@exadb-node1 ~]$ export OGG_HOME=/u02/app/oracle/goldengate/gg21c
[oracle@exadb-node1 ~]$ export
 OGG_VAR_HOME=<acfs or dbfs mount point>/deployments/ggsm01/var
[oracle@exadb-node1 ~]$ export OGG_ETC_HOME=<acfs or
 dbfs mount point>/deployments/ggsm01/etc
[oracle@exadb-node1 ~]$ $OGG_HOME/bin/ServiceManager
 --prop=/config/network/serviceListeningPort
 --value='{"port":9100,"address":"127.0.0.1"}'
 --type=array --persist --exit
[oracle@exadb-node1 ~]$
```

Step 8.3.3 - Restart the Service Manager and Deployment

As the `grid` OS user, restart the Service Manager and deployment:

```
[opc@exadb-node1 ~]$ sudo su - grid
[grid@exadb-node1 ~]$ agctl start goldengate <instance_name>
[grid@exadb-node1 ~]$ agctl status goldengate
Goldengate  instance '<instance_name>' is running on exadb-node1
```

Step 8.3.4 - Modify the GoldenGate Microservices listener address

As the `oracle` OS user, modify all the GoldenGate microservices (`adminsrvr`, `pmsrvr`, `distsrvr`, `recvsrvr`) listening address to `localhost` for the deployments managed by the Service Manager using the following command:

```
[opc@exadb-node1 ~]$ sudo su - oracle
[oracle@exadb-node1 ~]$ cd /u02/app_acfs/goldengate
[oracle@exadb-node1 ~]$ chmod u+x secureServices.py
[oracle@exadb-node1 ~]$ ./secureServices.py http://localhost:9100 --user oggadmin
Password for 'oggadmin': <oggadmin_password>

*** Securing deployment - ogg_deployment

Current value of "/network/serviceListeningPort" for "<instance_name>/adminsrvr" is
{
    "address": "127.0.0.1",
    "port": 9101
}
Current value of "/network/serviceListeningPort" for "<instance_name>/distsrvr" is
{
    "address": "127.0.0.1",
    "port": 9102
}
Current value of "/network/serviceListeningPort" for "<instance_name>/pmsrvr" is
{
    "address": "127.0.0.1",
    "port": 9104
}
Current value of "/network/serviceListeningPort" for "<instance_name>/recvsrvr" is
{
    "address": "127.0.0.1",
    "port": 9103
}
```

Note:

To modify a single deployment (`adminsrvr`, `pmsrvr`, `distsrvr`, `recvsrvr`), add the flag `--deployment                             instance_name`

Step 8.3.5 - Remove NGINX default.conf Configuration File

As the `opc` OS user, remove the default configuration file (`default.conf`) created in `/etc/nginx/conf.d`:

```
[opc@exadb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo rm
 -f /etc/nginx/conf.d/default.conf
[opc@exadb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo nginx -s reload
```
Step 8.4 - Create a Clusterware Resource to Manage NGINX

Oracle Clusterware needs to have control over starting the NGINX reverse proxy so that it can be started automatically before the Oracle GoldenGate deployments are started.

1. As the `grid` OS user, use the following command to get the network CRS resource name required to create the NGINX resource with a dependency on the underlying network CRS resource:
	```
	[opc@exadb-node1 ~]$ sudo su - grid
	[grid@exadb-node1 ~]$ crsctl stat res -w "TYPE == ora.network.type"|grep NAME
	NAME=ora.net1.network
	```
2. As the `root` OS user, use the following example command to create a Clusterware resource to manage NGINX. Replace the `HOSTING_MEMBERS` and `CARDINALITY` to match your environment:
	```
	[opc@exadb-node1 ~]$ sudo su -
	[root@exadb-node1 ~]# $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/bin/crsctl
	 add resource nginx -type generic_application -attr
	 "ACL='owner:root:rwx,pgrp:root:rwx,other::r--,group:oinstall:r-x,user:oracle:rwx',
	EXECUTABLE_NAMES=nginx,START_PROGRAM='/bin/systemctl start
	 -f nginx',STOP_PROGRAM='/bin/systemctl stop
	 -f nginx',CHECK_PROGRAMS='/bin/systemctl status nginx'
	 ,START_DEPENDENCIES='hard(ora.net1.network) pullup(ora.net1.network)',
	 STOP_DEPENDENCIES='hard(intermediate:ora.net1.network)',
	 RESTART_ATTEMPTS=0, HOSTING_MEMBERS='<exadb-node1, exadb-node2>', CARDINALITY=2"
	```
	The NGINX resource created in this example will run on the named database nodes simultaneously, specified by `HOSTING_MEMBERS`. This is recommended when multiple GoldenGate Service Manager deployments are configured and can independently move between database nodes.
	Once the NGINX Clusterware resource is created, the GoldenGate XAG resources need to be altered so that NGINX must be started before the GoldenGate deployments are started.
3. As the `root` OS user, modify the XAG resources using the following example commands.
	```
	# Determine the current --filesystems parameter:
	[opc@exadb-node1 ~]$ sudo su - grid
	[grid@exadb-node1 ~]$ agctl config goldengate <instance_name> |grep "File System"
	File System resources needed: <file_system_resource_name>
	# Modify the --filesystems parameter:
	[opc@exadb-node1 ~]$ sudo su -
	[root@exadb-node1 ~]# /u01/app/grid/xag/bin/agctl modify goldengate <instance_name>
	 --filesystems <file_system_resource_name>,nginx
	```
4. Repeat the above commands for each XAG GoldenGate registration relying on NGINX.