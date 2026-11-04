---
title: Upgrade Considerations for Oracle Net Services
book: Net Services Reference
doc_id: E10835-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10835/mignet.htm
tags:
  - oracle
  - 11g
  - net-services-reference
---

## B Upgrade Considerations for Oracle Net Services

This appendix describes coexistence and upgrade issues for Oracle Net Services. This appendix covers the following topics:

## Anonymous Access to Oracle Internet Directory

Typical users of directory naming (LDAP) require anonymous access to the Oracle Internet Directory for name lookup. If your Oracle Internet Directory software is upgraded to Oracle Internet Directory 11g, then it should be noted that the default setting for Oracle Internet Directory has changed. The default now is to disallow anonymous access to the directory. The directory administrator will need to configure the directory to enable anonymous binds after upgrading the directory to release 11g. In addition, the way anonymous binds are configured in Oracle Internet Directory has changed between Oracle Database 10g and Oracle Database 11g.

See Also:

[Oracle Internet Directory Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OIDAG2565) for additional information about anonymous binds

## Migrating a Non-default Listener to Oracle Database 11g Release 2 (11.2)

When migrating Oracle Database 11g Release 1 (11.1.0.7) to Oracle Database 11g Release 2 (11.2) in an Oracle Real Application Clusters environment, non-default listeners are not migrated by Oracle Net Services Configuration Assistant. To migrate the non-default listeners, use the following procedure:

1. Use Oracle Database 11g Release 1 (11.1.0.7) Oracle Net Services Configuration Assistant to remove the non-default listeners.
2. Use Oracle Database 11g Release 2 (11.2) Oracle Net Services Configuration Assistant to create the non-default listeners.

## Removing the Listener Password

In Oracle Database 11g Release 2 (11.2), the password feature is being deprecated. This does not cause a loss of security because authentication is enforced through local operating system authentication. To migrate a listener that has a set password, do the following:

1. Remove all PASSWORDS\_listener\_name entries from the `listener.ora` file.
2. Reload the listener using the following command:
	```
	lsnrctl reload listener_name
	```

If remote administration of a listener is required, then use one of the following methods to connect to and administer the listener.

- Connect to the host where listener is running using SSH or other secure method, and then perform local administration. Local administration is enforced by the operating system authentication.
- Use Oracle Enterprise Manager to administer the listener. Oracle Enterprise Manager uses HTTPS, which ensures security.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/listenercfg.htm#NETAG0102) for more information about managing the listener

## Client and Database Coexistence Issues

Clients and database servers require compatible releases of Oracle Net Services. For example, an Oracle9i client requires an installation of Oracle Net Services, and an Oracle9i database requires an installation of Oracle Net Services with the Oracle Net Listener.

Consider the following client-to-database connection issues before you decide if upgrading is appropriate for your environment:

- Oracle9i Database Connections
- Oracle Names

### Oracle9i Database Connections

Connect descriptors, created for connections to an Oracle9i database, identify a database by its service name with the `SERVICE_NAME` parameter.

A connect descriptor to an Oracle9i or Oracle8 database uses the parameter `SERVICE_NAME`, as shown in the following example:

```
sales= 
(DESCRIPTION= 
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521))
  (CONNECT_DATA=
     (SERVICE_NAME=sales.us.example.com)))
```

Connect descriptors that are currently configured with the `SID` parameter can remain. However, to take advantage of new features, such as client load balancing and connect-time failover, Oracle recommends replacing `SID` with `SERVICE_NAME`.

To modify a connect descriptor to use `SERVICE_NAME`, use the Oracle Net Manager's compatibility mode.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/concepts.htm#NETAG002) for additional information about database identification by `SERVICE_NAME` rather than `SID`

### Oracle Names

Oracle Names is not supported as a centralized naming method. Because no new enhancements are being added to Oracle Names, consider using directory naming or upgrading an existing Oracle Names configuration to directory naming, as described in the [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/listenercfg.htm#NETAG010).