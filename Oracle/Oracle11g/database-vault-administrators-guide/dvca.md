---
title: "Postinstallation Oracle Database Vault Procedures"
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/dvca.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## C Postinstallation Oracle Database Vault Procedures

This appendix contains:

## Checking the Locale and NLS Settings

Ensure that the value of the `NLS_LANGUAGE` initialization parameter matches the locale and NLS settings (either the `NLS_LANG` or `LANG` environment variables) used by the operating system of the computer on which Oracle Database is installed. If these values are inconsistent, then Database Vault Administrator does not display the default realms, command rules, rule sets, or factors.

For example, if the operating system locale (the variable `$LANG`) setting is `en_US.UTF-8`, then you must set the corresponding `NLS_LANG` environment variable to `AMERICAN_AMERICA.AL32UTF8` and the database `NLS_LANGUAGE` initialization parameter value to be `AMERICAN`. The database `NLS_LANGUAGE` parameter is derived from the operating system `NLS_LANG` environment variable.

For more information about checking and configuring locale and NLS settings, see the appendix that covers globalization support in the Oracle Database Installation Guide for your platform.

## Manually Deploying Oracle Database Vault Administrator

If you have created an Oracle database manually, and have configured Oracle Enterprise Manager Database Control by using Enterprise Manager Configuration Assistant, you must manually deploy Oracle Database Vault Administrator. This procedure deploys Database Vault Administrator in the same OC4J container as the current Enterprise Manager, rather than creating a new application.

This section contains:

- Deploying Database Vault Administrator to a Standalone OC4J Container
- Deploying Database Vault Administrator to the Database Console OC4J Container

### Deploying Database Vault Administrator to a Standalone OC4J Container

You can manually deploy Database Vault Administrator to the Oracle Application Server Containers for J2EE (OC4J) home, which by default is in the `$ORACLE_HOME/oc4j/j2ee/home` directory.

To manually deploy Database Vault Administrator:

1. Edit the file `$ORACLE_HOME/oc4j/j2ee/home/config/server.xml`. Enter the following line just before the last line that reads, `</application-server>`:
	```
	<application name="dva" path="Oracle_home_dir/dv/jlib/dva_webapp.ear" auto-start="true" />
	```
	Replace `Oracle_home_dir` with the relative or direct path to the Oracle home directory. (You cannot enter the `$ORACLE_HOME` environment variable.)
	For example:
	```
	<application name="dva" path="/u00/app/oracle/oracle/product/dv12/dv/jlib/dva_webapp.ear" auto-start="true" />
	```
2. Edit the file `$ORACLE_HOME/oc4j/j2ee/home/config/http-web-site.xml`. Enter the following line just above the last line that reads, `</web-site>`:
	```
	<web-app application="dva" name="dva_webapp" root="/dva" />
	```
3. Edit the file `$ORACLE_HOME/oc4j/j2ee/home/config/global-web-application.xml`. Search for `<servlet-class>oracle.jsp.runtimev2.JspServlet</servlet-class>`. Uncomment the following lines after this:
	```
	<init-param>
	   <param-name>main_mode</param-name>
	   <param-value>justrun</param-value>
	</init-param>
	```
4. Create the following directory:
	```
	mkdir -p $ORACLE_HOME/dv/jlib/sysman/config
	```
5. Create the database connection configuration file, emoms.properties, in the configuration directory that you just created. Add the following lines to the file:
	```
	oracle.sysman.emSDK.svlt.ConsoleMode=standalone
	oracle.sysman.eml.mntr.emdRepRAC=FALSE
	oracle.sysman.eml.mntr.emdRepDBName=oracle_sid
	oracle.system.eml.mntr.emdRepConnectDescriptor=TNS_connection_string
	```
	Follow these instructions:
	- For an Oracle RAC environment, set `oracle.sysman.eml.mntr.emdRepRAC` to `TRUE`.
		- For `oracle.sysman.eml.mntr.emdRepConnectDescriptor`, you can use an alias from `$ORACLE_HOME/network/admin/tnsnames.ora`. Alternatively, you can use the following syntax:
		```
		oracle.sysman.eml.mntr.emdRepConnectDescriptor=
		  (DESCRIPTION\=
		    (ADDRESS_LIST\=(ADDRESS\=(PROTOCOL\=TCP) (HOST\=HOSTNAME)(PORT\=PORT))) 
		    (CONNECT_DATA\=
		       (SERVICE_NAME\=ORACLE_SID))
		```
6. Ensure that the correct environment variables are set.
	For example:
	```
	ORACLE_SID=orcl
	export ORACLE_SID
	ORACLE_HOME=/u00/app/oracle/product/11.2
	export ORACLE_HOME
	LD_LIBRARY_PATH=$ORACLE_HOME/bin:$ORACLE_HOME/lib:$ORACLE_HOME/jdbc/lib
	export LD_LIBRARY_PATH
	PATH=$ORACLE_HOME/bin:$ORACLE_HOME/jdk/bin:$PATH
	export PATH
	```
	Set the `LD_LIBRARY_PATH` variable to use the OCI-based JDBC libraries.
7. Start OC4J using the following syntax:
	```
	$ORACLE_HOME/jdk/bin/java -Djava.awt.headless=true -DEMDROOT=$ORACLE_HOME/dv/jlib -jar $ORACLE_HOME/oc4j/j2ee/home/oc4j.jar -userThreads -config $ORACLE_HOME/oc4j/j2ee/home/config/server.xml
	```

After you complete these steps, you can start Database Vault Administrator. The HTTP port defaults to 8888 for this environment. Use the following syntax for the URL:

```
http://hostname:8888/dva
```

### Deploying Database Vault Administrator to the Database Console OC4J Container

To manually deploy Database Vault Administrator to the Database Console OC4J container:

1. Stop Oracle Database Console.
	- UNIX: Go to the `$ORACLE_HOME/bin` directory and run the following command:
		```
		./emctl stop dbconsole
		```
		- Windows: In the Administrative Services, select the Services utility, and then right-click the OracleDBConsolesid service. Select Stop from the menu.
2. Create a backup copy and then open the `$ORACLE_HOME/oc4j/j2ee/OC4J_DBConsole_` `service_name` `/config/server.xml` file.
3. Add the following line before the `</application-server>` element:
	```
	<application name="dva" path="$ORACLE_HOME/dv/jlib/dva_webapp.ear" parent="default" start="true" />
	```
	On both UNIX and Windows systems, replace `$ORACLE_HOME` with the absolute path to your Oracle Database home.
4. Create a backup copy and then open the `$ORACLE_HOME/oc4j/j2ee/OC4J_DBConsole_` `service_name` `/config/http-web-site.xml` file.
5. Add the following line before the \</web-site> element:
	```
	<web-app application="dva" name="dva_webapp" load-on-startup="true" root="/dva" shared="true"/>
	```
6. Restart Oracle Database Console.
	- UNIX: Go to the `$ORACLE_HOME/bin` directory and run the following command:
		```
		./emctl start dbconsole
		```
		- Windows: In the Administrative Services, select the Services utility, and then right-click the OracleDBConsolesid service. Select Start from the menu.

After you complete these steps, you can start Oracle Database Vault Administrator by using the following URL:

```
https://hostname:port/dva
```

For example:

```
https://myserver:1158/dva
```

If you are unsure of the port number, open the `ORACLE_HOME` `/` `host_sid` `/sysman/config/emd.properties` file and search for `REPOSITORY_URL`. In most cases, the host name and port number are the same as Oracle Enterprise Manager Database Control.

## Setting the Time-Out Value for Oracle Database Vault Administrator

By default, an Oracle Database Vault session lasts 35 minutes. If you want the session to last for a different time, follow the steps in this section.

To set the session time for Oracle Database Vault Administrator:

1. Back up the `web.xml file`, which by default is in the `$ORACLE_HOME/dv/jlib/dva_webapp/dva_webapp/WEB-INF` directory.
2. In a text editor, open the `web.xml` file.
3. Search for the following setting:
	```
	<session-config>
	 <session-timeout>35</session-timeout>
	</session-config>
	```
4. Change the `<session-timeout>` setting to the amount of time in minutes that you prefer.
5. Save and close the `web.xml` file.
6. Stop and restart the Database Vault Administrator.
	- UNIX: Go to the `$ORACLE_HOME/bin` directory and run the following command:
		```
		./emctl stop dbconsole
		./emctl start dbconsole
		```
		- Windows: In the Administrative Services, select the Services utility, and then right-click the OracleDBConsolesid service. Select Stop from the menu. After the console stops, select Start.

## Enabling Oracle Database Vault Administrator Accessibility

You can configure Database Vault Administrator to make data accessible and usable to the disabled community. The following sections explain how to enable Database Vault Administrator for full accessibility.

- Enabling Oracle Database Vault Administrator Accessibility Mode
- Providing Textual Descriptions of Database Vault Administrator Charts

### Enabling Oracle Database Vault Administrator Accessibility Mode

Oracle Database Vault Administrator takes advantage of user interface development technologies that improve the responsiveness of some user operations. For example, when you navigate to a new record set in a table, Oracle Database Vault Administrator does not redisplay the entire HTML page. However, this performance-improving technology is generally not supported by screen readers. To disable this feature, and as a result, make the Database Vault Administrator HTML pages more accessible for disabled users, use the following procedure.

To enable the display of an entire HTML page:

1. Locate the `uix-config.xml` configuration file.
	By default, the `uix-config.xml` file is in the following directory:
	```
	$ORACLE_HOME/oc4j/j2ee/oc4j_applications/applications/em/em/WEB-INF
	```
2. Open the `uix-config.xml` file using a text editor and locate the following entry:
	```
	<!-- An alternate configuration that disables accessibility features  -->
	<default-configuration>
	  <accessibility-mode>inaccessible</accessibility-mode>
	...
	</default-configuration>
	```
3. Change the value of the accessibility-mode property from `inaccessible` to `accessible`.
4. Save and close the `uix-config.xml` file.
5. Restart Database Vault Administrator.
	See ["Starting Oracle Database Vault"](getting_started.md).

### Providing Textual Descriptions of Database Vault Administrator Charts

The Monitor page of Database Vault Administrator displays security policy data in a chart. However, charts do not convey information in a manner that can be read by a screen reader. To remedy this problem, you can configure Database Vault Administrator to provide a complete textual representation of each chart. By default, support for the textual representation of charts is disabled. When textual description for charts is enabled, Database Vault Administrator displays a textual representation of the chart data.

To enable the textual representation of charts:

1. Locate the `web.xml` configuration file.
	To locate the `web.xml` file in a Oracle Database 10g installation, change directory to the following location in the Oracle home:
	```
	$ORACLE_HOME/dv/jlib/dva_webapp/dva_webapp/WEB-INF/
	```
2. Open the `web.xml` file with your favorite text editor and locate the following six lines of the file:
	```
	<!-- Uncomment this to enable textual chart descriptions
	<context-param>
	<param-name>enableChartDescription</param-name>
	<param-value>true</param-value>
	</context-param>
	-->
	```
3. Remove comments from this section by deleting the first line and the last line of this section so that the section consists of only these four lines:
	```
	<context-param>
	<param-name>enableChartDescription</param-name>
	<param-value>true</param-value>
	</context-param>
	```
4. Save and exit the `web.xml` file.
5. Restart Database Vault Administrator.
	See ["Starting Oracle Database Vault"](getting_started.md).

## Configuring Oracle Database Vault on Oracle RAC Nodes

After you install Oracle Database Vault for an Oracle Real Application Clusters (Oracle RAC) instance, complete the following procedure for each Oracle RAC node. This procedure assumes that you have a separate Oracle home for each node.

1. Log in to SQL\*Plus as user `SYS` with the `SYSDBA` privilege.
	```
	sqlplus sys as sysdba
	Enter password: password
	```
2. Run the following `ALTER SYSTEM` statements:
	```
	ALTER SYSTEM SET AUDIT_SYS_OPERATIONS=TRUE SCOPE=SPFILE;
	ALTER SYSTEM SET OS_ROLES=FALSE SCOPE=SPFILE; 
	ALTER SYSTEM SET RECYCLEBIN='OFF' SCOPE=SPFILE; 
	ALTER SYSTEM SET REMOTE_LOGIN_PASSWORDFILE='EXCLUSIVE' SCOPE=SPFILE;
	ALTER SYSTEM SET SQL92_SECURITY=TRUE SCOPE=SPFILE;
	```
3. Restart Oracle Database.
	```
	CONNECT SYS/AS SYSOPER
	Enter password: password
	SHUTDOWN IMMEDIATE
	STARTUP
	```

## Adding Languages to Oracle Database Vault

By default, Oracle Database Vault loads only the English language tables. You can add more languages by running the `DBMS_MACADM.ADD_NLS_DATA` procedure for each new language that you want to add. You can add more than one language to Database Vault.

To add a new language to Oracle Database Vault:

1. Log into SQL\*Plus as a user who has been granted the `DV_OWNER` or `DV_ADMIN` role.
2. Run the following procedure:
	```
	EXEC DBMS_MACADM.ADD_NLS_DATA('language');
	```
	You can specify the `language` setting using any case. For example:
	```
	EXEC DBMS_MACADM.ADD_NLS_DATA('french');
	EXEC DBMS_MACADM.ADD_NLS_DATA('JAPANESE');
	```
	Replace `language` with one of the following supported languages:
	- `ENGLISH`
		- `GERMAN`
		- `SPANISH`
		- `FRENCH`
		- `ITALIAN`
		- `JAPANESE`
		- `KOREAN`
		- `BRAZILIAN PORTUGUESE`
		- `SIMPLIFIED CHINESE`
		- `TRADITIONAL CHINESE`

## Deinstalling Oracle Database Vault

The following procedure removes Oracle Database Vault from an Oracle Database installation. It applies to both single-instance and Oracle RAC installations. The deinstallation process does not affect the initialization parameter settings, even those settings that were modified during the installation process.

To deinstall Oracle Database Vault:

1. Stop the database, Database Control console process, and listener.
	For example:
	```
	sqlplus sys as sysoper
	Enter password: password
	Connected.
	SQL> SHUTDOWN IMMEDIATE
	SQL> EXIT
	$ emctl stop dbconsole
	$ lsnrctl stop [listener_name]
	```
	For Oracle RAC installations, shut down each database instance as follows:
	```
	$ srvctl stop database -d db_name
	```
	On Windows, you can stop the database, Database Control console process, and listener from the Services tool in the Control Panel. The names of Oracle Database services begin with `Oracle`.
2. Run the following commands to turn off Oracle Database Vault and Oracle Label Security:
	```
	$ cd $ORACLE_HOME/rdbms/lib
	$ make -f ins_rdbms.mk dv_off lbac_off ioracle
	```
3. Log in to SQL\*Plus and then restart the database, Database Control console process, and listener.
	For example:
	```
	SQL> STARTUP
	SQL> EXIT
	$ emctl stop dbconsole
	$ lsnrctl start [listener_name]
	```
	For each instance in an Oracle RAC installation:
	```
	$ srvctl start database -d db_name
	```
	On Windows, you can restart the database, Database Control console process, and listener from the Services tool in the Control Panel. The names of Oracle Database services begin with `Oracle`.
4. In SQL\*Plus, log in as user `SYS` with the `SYSDBA` privilege.
5. Disable the recycle bin.
	To check if the recycle bin is enabled, enter the following command:
	```
	SQL> SHOW PARAMETER RECYCLEBIN
	```
	If the recycle bin is enabled, then disable it as follows:
	```
	SQL> ALTER SYSTEM SET RECYCLEBIN = OFF SCOPE=SPFILE;
	SQL> SHUTDOWN IMMEDIATE
	SQL> STARTUP
	```
	Disabling the recycle bin does not purge or otherwise affect objects that are already in the recycle bin. For better security, keep the recycle bin disabled. See ["Security Considerations for the Recycle Bin"](guidelines.md).
6. Run the following SQL script:
	```
	SQL> @$ORACLE_HOME/rdbms/admin/dvremov.sql
	```
7. Manually drop the `DV_OWNER` and `DV_ACCTMGR` user accounts and the `DV_REALM_RESOURCE` and `DV_REALM_OWNER` roles.
	```
	SQL> DROP DBV_OWNER CASCADE;
	SQL> DROP DBV_ACCTMGR CASCADE;
	SQL> DROP DV_REALM_RESOURCE;
	SQL> DROP DV_REALM_OWNER;
	```
8. Enable Oracle Label Security.
	```
	$ cd $ORACLE_HOME/rdbms/lib
	$ make -f ins_rdbms.mk lbac_on ioracle
	```

Afterward, you can double-check that Oracle Database Vault is truly deinstalled by logging in to SQL\*Plus and entering the following statement:

```
SQL> SELECT * FROM V$OPTION WHERE PARAMETER = 'Oracle Database Vault';
```

If Oracle Database Vault is deinstalled, the following output appears:

```
PARAMETER                     VALUE
----------------------------- -----------------------
Oracle Database Vault         FALSE
```

## Reinstalling Oracle Database Vault

To reinstall Oracle Database Vault, follow the procedure under ["Registering (Enabling) Oracle Database Vault"](getting_started.md).