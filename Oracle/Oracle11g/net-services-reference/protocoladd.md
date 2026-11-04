---
title: Protocol Address Configuration
book: Net Services Reference
doc_id: E10835-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10835/protocoladd.htm
tags:
  - oracle
  - 11g
  - net-services-reference
---

## 4 Protocol Address Configuration

A network object is identified by a [protocol address](glossary.md). When a connection is made, the client and the receiver of the request ([listener](glossary.md) or [Oracle Connection Manager](glossary.md)) are configured with identical protocol addresses.

The client uses this address to send the connection request to a particular network object location, and the recipient "listens" for requests on this address, and grants a connection based on its address information matching the client information.

This chapter contains the following topics:

## Protocol Addresses

The protocol address is comprised of ADDRESS and ADDRESS\_LIST elements.

### ADDRESS

Purpose

To define a protocol address.

Usage Notes

Put this parameter under an `ADDRESS_LIST` or `DESCRIPTION` parameter. A `DESCRIPTION` is used in a `tnsnames.ora` or a `listener.ora` file.

Example

```
(ADDRESS=
 (PROTOCOL=tcp)
 (HOST=sales-server)
 (PORT=1521))
```

See Also:

"Protocol Parameters" for each protocol's required parameters

### ADDRESS\_LIST

Purpose

To define a list of protocol addresses that share common characteristics.

Example

```
(ADDRESS_LIST=
 (LOAD_BALANCE=on)
 (ADDRESS=
  (PROTOCOL=tcp)
  (HOST=sales-server)
  (PORT=1521))
 (ADDRESS=
  (PROTOCOL=tcp)
  (HOST=hr-server)
  (PORT=1521)))
```

## Protocol Parameters

The listener and Oracle Connection Manager are identified by protocol addresses. Table 4-1, "Protocol-Specific Parameters" lists the parameters used by the Oracle protocol support.

Table 4-1 Protocol-Specific Parameters

| Protocol | Parameter | Description |
| --- | --- | --- |
| IPC | `PROTOCOL` | Specify `ipc` as the value. |
|  | `KEY` | Specify a unique name for the service. Oracle recommends using the service name or the [Oracle System Identifier (SID)](glossary.md) of the service.  Example:  ``` (PROTOCOL=ipc)(KEY=sales) ``` |
| Named Pipes | `PROTOCOL` | Specify `nmp` as the value. |
|  | `SERVER` | Specify the name of the Oracle server. |
|  | `PIPE` | Specify the pipe name used to connect to the database server. This is the same `PIPE` keyword specified on server with Named Pipes. This name can be any name.  Example:  ``` (PROTOCOL=nmp)(SERVER=sales)(PIPE=dbpipe0) ``` |
| SDP | `PROTOCOL` | Specify `sdp` as the value. |
|  | `HOST` | Specify the host name or IP address of the computer. |
|  | `PORT` | Specify the listening port number.  Example:  ``` (PROTOCOL=sdp)(HOST=sales-server)(PORT=1521) (PROTOCOL=sdp)(HOST=192.168.2.204)(PORT=1521) ``` |
| TCP/IP | `PROTOCOL` | Specify `tcp` as the value. |
|  | `HOST` | Specify the host name or IP address of the computer. |
|  | `PORT` | Specify the listening port number.  Example:  ``` (PROTOCOL=tcp)(HOST=sales-server)(PORT=1521) (PROTOCOL=tcp)(HOST=192.168.2.204)(PORT=1521) ``` |
| TCP/IP with SSL | `PROTOCOL` | Specify `tcps` as the value. |
|  | `HOST` | Specify the host name or IP address of the computer. |
|  | `PORT` | Specify the listening port number.  Example:  ``` (PROTOCOL=tcps)(HOST=sales-server)(PORT=2484) (PROTOCOL=tcps)(HOST=192.168.2.204)(PORT=2484) ``` |

## Recommended Port Numbers

Table 4-2, "Recommended Port Numbers" lists the recommends the port numbers.

Table 4-2 Recommended Port Numbers

| Port | Description |
| --- | --- |
| 1521 | Default listening port for client connections to the listener.  This port number may change to the officially registered port number of 2483 for TCP/IP and 2484 for TCP/IP with SSL. |
| 1521 | Default and officially registered listening port for client connections to Oracle Connection Manager. |
| 1830 | Default and officially registered listening port for administrative commands to Oracle Connection Manager. |

## Port Number Limitations

Oracle allows port numbers from 1 to 65535. However, many operating systems reserve port numbers less than 1024. For example, on certain operating systems, only privileged processes can listen for TCP connections on ports less than 1024.

If you need to configure listener to listen on a port number less than 1024, then do the following:

Note:

Your operating system may require a different procedure.
1. Use Oracle Net Configuration Assistant or Oracle Net Manager to configure the listener with protocol addresses and other configuration parameters.
	See Also:
	[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/dispatcher.htm#NETAG012)
2. Log in as the `root` user on the machine that has the listener.
3. Set file ownership and access permissions for the listener executable (`tnslsnr`) and the dependent shared libraries so that these files can be modified only by the `root` user.
4. Ensure that the permissions of the individual directories found in the path names to these files, starting with the root directory have the same ownership and access permissions.
5. Start the listener as the `root` user.
6. Enter the following command at the system prompt:
	```
	tnslsnr listener_name
	 -user user
	 -group group
	```
	In the preceding command, the following options are used:
	Table 4-3 tnslsnr Utility Options
	| Options | Description |
	| --- | --- |
	| listener\_name | Specify the name of the listener. If omitted, then the default name `LISTENER` is used. |
	| user | Specify the user whose privileges the listener will use when super user (`root`) privileges are not needed. After performing the privileged operations, the listener will give up `root` privileges irreversibly. |
	| group | Specify the group whose privileges the listener will use when super user (`root`) group privileges are not needed. After performing the privileged operations, the listener will give up `root` group privileges irreversibly. |
	During this step, the listener switches to the specified user and group. All operations are done with the specified user and group privileges, except the system calls necessary to listen on configured endpoints. The listener reverts to the `root` user to listen on reserved addresses, such as TCP ports less than 1024.
	After the listener starts listening on all of its endpoints configured in `listener.ora`, it switches to the specified user and group irreversibly. Therefore, the listener will give up the `root` privilege that it initially had. The `-user` and `-group` command line arguments only accept user and group identifiers specified in numeric form.
	For example, to run a listener with root privileges called `mylsnr` and have it use privileges of a user identified as 37555 with a group identifier of 16, enter the following at the operating system command prompt:
	```
	tnslsnr mylsnr -user 37555 -group 16
	```
	In the preceding example, 37555 could be the identifier for the `oracle` user, and 16 could be the identifier for the `dba` group.
7. After the listener has been started, you can administer it with the Listener Control utility.
	Important Notes:
	- Oracle recommends that the user which the listener process runs be the `oracle` user, or a user that the listener process normally runs on the operating system.
	- Do not leave the listener process running as the `root` user because doing so is a security vulnerability.