---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: E96081-35
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/configure-dateabase-aces-for-dbms_cloud.html
tags:
  - oracle
  - 19c
  - utilities
---

## 20.4 Configure ACEs for DBMS\_CLOUD (CDB and Non-CDB)

Create Access Control Entries (ACEs) to enable communication with Object Stores and other trusted `https` endpoints (URIs).

By default, Oracle Database does not permit outside communication. To provide access to Object Stores, you must enable the appropriate Access Control Entries using Oracle Database administrator privileges. If your database is behind a firewall, then you must obtain network and system administrator information about your Internet Gateway, and configure the Access Control Entries (ACEs) appropriately.

If you are using an HTTP proxy to connect to the Internet, then you must configure your database to enable secure use of your gateway. This configuration process requires you to enable your database to access external network services through the gateway, and then configure your database to use the HTTP proxy gateway for `DBMS_CLOUD` external network services.

1. Enable your database to access to the external network services through the gateway, so that the database can access the Object Store.
	To allow access to your HTTP proxy gateway for external network services for the schema-owning `DBMS_CLOUD`, append the access control list of your database using the parameter `DBMS_NETWORK_ACL_ADMIN` package with the `APPEND_HOST_ACE` procedure, where your-proxy-host-DNS-name is the name or IP address of your HTTP proxy gateway host:
	```
	host=your-proxy-host-DNS-name
	```
	For example, if your HTTP proxy setting is `http://myproxyhost.mydomain:99`, then enter `'myproxyhost.mydomain` '.
	```
	low_port=your_proxy_low_port
	high_port=your_proxy_high_port
	```
	Those two parameters can be null or a port number. By default, there is no port restriction for TCP connections. To limit the access to a specific port your HTTP proxy is communicating on, you can use the same port as both the low and high port. In the example that follows, both of these parameters are set to port 99.
2. Configure your database to use the HTTP proxy gateway for `DBMS_CLOUD` external network services.
	`DBMS_CLOUD` internally recursively issues REST calls leveraging `UTL_HTTP`. The proxy URI information for `DBMS_CLOUD` is set with the database property `'http_proxy'`, following the proxy URI format as set with `UTL_HTTP.SET_PROXY().                 proxy_uri=your-proxy-URI-address`. The proxy can include an optional TCP/IP port number on which the proxy server listens. The syntax is `http://host:port`. For example: `www-proxy.my-company.com:80`. If the port is not specified for the proxy, then by default port 80 is used.
	Optionally, you can specify a port number for each domain or host. If the port number is specified, then the no-proxy restriction is only applied to the request at the port of the particular domain or host. For example: `corp.my-company.com,               eng.my-company.com:80`.
	When `no_proxy_domains` is `NULL` and the proxy is set, all requests go through the proxy. When the proxy is not set, `UTL_HTTP` sends requests to the target Web servers directly.
	You can define a user name and password for the proxy that you want to be specified in the proxy string. The format is `http://user:password@host:port`. For more details about configuring access control for external network services using the `DBMS_NETWORK_ACL_ADMIN` package, see the "Syntax for Configuring Access Control for External Network Services" section link at the bottom of this topic.

Example 20-1 Configure database to use the HTTP and HTTP\_PROXY for DBMS\_CLOUD

The setup of the ACE and (optionally) HTTP proxy is done differently for content delivery networks (CDN) and non-CDB installations. Copy and paste the entire content in the code example that applies to your environment into a new SQL script (for example, `configure_ACES.sql`), and update as required for your environment. The code examples that follow contains comments in the scripts themselversthat explain how the proxy URL and host values are set.

Note:

Ensure that you set variables for your environment correctly. If you do not set them correctly, then `DBMS_CLOUD` will not function properly.

- Option 1: Set up ACEs in your container database CDB
	```
	sql
	@$ORACLE_HOME/rdbms/admin/sqlsessstart.sql
	 
	-- you must not change the owner of the functionality to avoid future issues
	define clouduser=C##CLOUD$SERVICE
	 
	-- CUSTOMER SPECIFIC SETUP, NEEDS TO BE PROVIDED BY THE CUSTOMER-- - SSL Wallet directory
	define sslwalletdir=<Set SSL Wallet Directory>
	 
	---- UNCOMMENT AND SET THE PROXY SETTINGS VARIABLES IF YOUR ENVIRONMENT NEEDS PROXYS--
	 
	-- define proxy_uri=<your proxy URI address>
	-- define proxy_host=<your proxy DNS name>
	-- define proxy_low_port=<your_proxy_low_port>
	-- define proxy_high_port=<your_proxy_high_port>
	 
	-- Create New ACL / ACE s
	begin
	-- Allow all hosts for HTTP/HTTP_PROXY
	    dbms_network_acl_admin.append_host_ace(
	        host =>'*',
	        lower_port => 443,
	        upper_port => 443,
	        ace => xs$ace_type(
	            privilege_list => xs$name_list('http', 'http_proxy'),
	            principal_name => upper('&clouduser'),
	            principal_type => xs_acl.ptype_db
	            )
	        );
	--
	-- UNCOMMENT THE PROXY SETTINGS SECTION IF YOUR ENVIRONMENT NEEDS PROXYS
	--
	-- Allow Proxy for HTTP/HTTP_PROXY
	-- dbms_network_acl_admin.append_host_ace(
	-- host =>'&proxy_host',
	-- lower_port => &proxy_low_port,
	-- upper_port => &proxy_high_port,
	-- ace => xs$ace_type(
	-- privilege_list => xs$name_list('http', 'http_proxy'),
	-- principal_name => upper('&clouduser'),
	-- principal_type => xs_acl.ptype_db));
	--
	-- END PROXY SECTION
	--
	 
	-- Allow wallet access
	    dbms_network_acl_admin.append_wallet_ace(
	        wallet_path => 'file:&sslwalletdir',
	        ace => xs$ace_type(
	            privilege_list =>xs$name_list('use_client_certificates', 'use_passwords'),
	            principal_name => upper('&clouduser'),
	            principal_type => xs_acl.ptype_db));
	end;
	/
	 
	-- Setting SSL_WALLET database property
	begin
	    if sys_context('userenv', 'con_name') = 'CDB$ROOT' then
	        execute immediate 'alter database property set ssl_wallet=''&sslwalletdir''';
	--
	-- UNCOMMENT THE FOLLOWING COMMAND IF YOU ARE USING A PROXY
	--
	--        execute immediate 'alter database property set http_proxy=''&proxy_uri''';
	    end if;
	end;
	/
	 
	@$ORACLE_HOME/rdbms/admin/sqlsessend.sql
	```
- Option 2: Set up ACEs in your non-CDB environment
	```
	sql
	@$ORACLE_HOME/rdbms/admin/sqlsessstart.sql
	 
	-- you must not change the owner of the functionality to avoid future issues
	define clouduser=C##CLOUD$SERVICE
	 
	-- CUSTOMER SPECIFIC SETUP, NEEDS TO BE PROVIDED BY THE CUSTOMER-- - SSL Wallet directory
	define sslwalletdir=<Set SSL Wallet Directory>
	 
	---- UNCOMMENT AND SET THE PROXY SETTINGS VARIABLES IF YOUR ENVIRONMENT NEEDS PROXYS--
	 
	-- define proxy_uri=<your proxy URI address>
	-- define proxy_host=<your proxy DNS name>
	-- define proxy_low_port=<your_proxy_low_port>
	-- define proxy_high_port=<your_proxy_high_port>
	 
	-- Create New ACL / ACE s
	begin
	-- Allow all hosts for HTTP/HTTP_PROXY
	    dbms_network_acl_admin.append_host_ace(
	        host =>'*',
	        lower_port => 443,
	        upper_port => 443,
	        ace => xs$ace_type(
	            privilege_list => xs$name_list('http', 'http_proxy'),
	            principal_name => upper('&clouduser'),
	            principal_type => xs_acl.ptype_db
	            )
	        );
	--
	-- UNCOMMENT THE PROXY SETTINGS SECTION IF YOUR ENVIRONMENT NEEDS PROXYS
	--
	-- Allow Proxy for HTTP/HTTP_PROXY
	-- dbms_network_acl_admin.append_host_ace(
	-- host =>'&proxy_host',
	-- lower_port => &proxy_low_port,
	-- upper_port => &proxy_high_port,
	-- ace => xs$ace_type(
	-- privilege_list => xs$name_list('http', 'http_proxy'),
	-- principal_name => upper('&clouduser'),
	-- principal_type => xs_acl.ptype_db));
	--
	-- END PROXY SECTION
	```

After running the script for your environment, confirm that the setup is correct:

- You should not see any entry for `HTTP_PROXY` if your environment does not need one.
- The property `SSL_WALLET` should show the directory where your wallet is located.