---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/part-iv-advanced-topics/configuring-oracle-acfs-snapshot-based-replication.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Configuring Oracle ACFS Snapshot-Based Replication

The requirements for Oracle ACFS snapshot-based replication are discussed in this section.

This section describes how to configure Oracle ACFS snapshot-based replication available with release 12.2 or higher. As with Oracle ACFS replication installations before release 12.2, the overall functional goal of snapshot-based replication is to ensure that updates from a primary cluster are replicated to a standby cluster. However, the snapshot based replication technology uses snapshots of the primary storage location and transfers the differences between successive snapshots to the standby storage location using the standard `ssh` command. Oracle ACFS replication functionality before release 12.2 replicated changes continuously, building on Oracle networking technologies, notably Network Foundation Technologies (NFT), to ensure connectivity between the primary and standby clusters.

This change in the design and implementation of Oracle ACFS replication introduces some differences in how replication is configured and used. For example, the use of `ssh` requires setting up host and user keys appropriately on the primary and standby nodes where replication is performed.

Oracle ACFS replication also provides role reversal and failover capabilites that you can configure by enabling both the primary cluster and the standby cluster to communicate with each other as required. In role reversal, the standby assumes the role of the primary and the primary becomes the standby. Failover may involve either role reversal or the establishment of a new standby for the new primary to use.

See also

- [Oracle ACFS Replication](introducing-oracle-acfs-and-oracle-advm.md) for an overview of Oracle ACFS replication
- [Oracle ACFS Command-Line Tools for Replication](managing-oracle-acfs-with-command-line-tools.md) for information about Oracle ACFS replication commands
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=OSTMG-GUID-7396FD18-628B-4026-AA55-79C6D6205EAE) for information about Oracle ASM privileges

## Configuring SSH for Use with Oracle ACFS Replication

Oracle ACFS snapshot-based replication uses SSH to authenticate the replication user and verify the identity of remote hosts.

Before you configure replication, establish passwordless SSH communication between the primary and standby clusters in both directions.

You can configure the required SSH trust relationship in either of these ways:

- Use the `acfsreplssh` key setup assistant.
- Configure the required SSH keys manually.

To support bidirectional replication, configure SSH from the primary cluster to the standby cluster and then repeat the configuration with the primary and standby roles reversed. When replication uses SSH as its transport, each cluster must trust the other cluster. Before you initialize replication, ensure that you configure the following SSH keys:

- Ensure that the public key for `repluser` on each node of the local cluster appears in the `authorized_keys2` file for `repluser` on each node of the remote cluster.
- Ensure that the `known_hosts` file on each node of the local cluster contains the host key for every node in the remote cluster, unless you disable strict host key checking.

Configuring SSH Using the Key Setup Assistant

Use the `acfsreplssh` key setup assistant to configure, verify, or remove the host and user keys that Oracle ACFS snapshot-based replication requires when it uses SSH as the transport.

Run the utility once with the primary cluster as the local cluster and the standby cluster as the remote cluster. Then repeat the procedure with the primary and standby roles reversed to complete the SSH configuration for bidirectional replication.

In this section, *local cluster* refers to the cluster on which you run the command, and *remote cluster* refers to the peer cluster.

Command Synopsis

The command syntax for `acfsreplssh` is:

```
acfsreplssh{ configure | verify | remove }
    [-v] [-m]
    [-V remote_vip]
    [-o sshStrictKey=ynvalue]
    { -c remote_cluster | remote_host1 [remote_hostn...] }
```

Where:

- `**-c remote_cluster**`:
	Uses `remote_cluster` as the name of a network endpoint to contact the remote cluster, then runs the acfsutil cluster info command on the remote cluster to identify the cluster members. Each hostname shown as a member is then processed as if it had been specified as a remote\_host directly on the command line.
- `**-m**`:
	Shows the operations that the command would perform without making any changes.
- `**-o sshStrictKey= ynvalue**`:
	Specifies whether or not host keys must already exist. A `ynvalue` starting with "y" signifies "yes"; a `ynvalue` starting with "n" signifies "no". For the `configure` command, "yes" means that host keys must already exist (the command will not configure them), while "no" means the command will accept (and configure) any host key presented by a remote node. For the `verify` command, this option has no effect - a host key must already exist for all remote nodes. (The `verify` command never adds or modifies keys.) The default value of this option is "yes" - that is, by default the local host must already possess a host key for any remote host contacted. For the initial contact with an unknown host, unless host-based authentication is in use, this option must be given with the value "no". When this is done, you must confirm manually that the intended host is being contacted. See the `-o sshStrictKey` option to the `acfsutil repl init` and `acfsutil repl update` commands for more information on host key checking.
- `**-v**`:
	Displays detailed information about command execution.
- **\-V remote\_vip**:
	Identifies `remote_vip` as an existing VIP for the remote cluster, consisting of the set of `remote_hosts` named on the command line. This means that `remote_vip` will be added to the line in the local `known_hosts` file for each `remote_host` given on the command line.
	Note:
	`acfsreplssh` will always prompt for the password to be used to log in as `repluser` on the remote cluster. The utility reads  
	the password from the standard input.
	Run the assistant on  
	each node of the local cluster to operate on the host and user keys for  
	a single remote cluster. Run it as `repluser`. The assistant displays your login name for  
	confirmation before it configures the required keys.
	To identify the  
	hosts in the remote cluster, either:
	- Specify `-c` remote\_cluster to name a  
		network endpoint in the remote cluster, which will be queried to  
		obtain the cluster members, or
	- Name each host in the remote cluster as a remote\_host  
		on the command line.

Configuring SSH on Each Local Host

Use the `acfsreplssh configure` command to configure the SSH keys required for replication. Run the command when you first configure replication or later to verify that all required keys remain configured on the participating clusters. Each run of `acfsreplssh configure` adds a user or host key only where needed while preserving existing keys.

When you contact a remote host for the first time, ordinarily `acfsreplssh` will not be able to verify the identity of the host via a known SSH host key. To permit successful contact, add the option `-o sshStrictKey=no` to the first command used to contact a remote host.

Note:

Because `acfsreplssh` cannot validate the identity of an unknown remote host during the initial connection, verify that you are connecting to the intended host by using another trusted method.

On each host, `acfsreplssh` saves the current key-related data for `repluser` before modifying it, unless a backup already exists. If the backup directory does not exist, `acfsreplssh` renames the existing \` `~*` repluser `*/.ssh` `  directory by appending the suffix  `.acfsreplssh.backup`. The utility creates the backup directory with ` 0400 `  permissions (readable only by the owner) and assigns ownership to  ` repluser\`.

The following example uses a 4-node primary cluster, `bosc26`, with nodes `n1` through `n4`, and a 2-node standby cluster, `chic26`, with nodes `n1` and `n2`. The SCAN VIP on each cluster serves as the network endpoint for replication. To avoid specifying each remote host name on the command line, the `-c` option specifies the VIP name.

To configure the full set of keys required by replication, using the VIP defined on each cluster, run `acfsreplssh` as follows.

First, run this command on each node of *bosc26*:

```
$ acfsreplssh configure -V chic26vip -c chic26vip -o sshStrictKey=no
```

Next, run this command on each node of *chic26*:

```
$ acfsreplssh configure -V bosc26vip -c bosc26vip -o sshStrictKey=no
```

The first command above configures a public key for the current user (which is assumed to be `repluser`) on the host within *bosc26* where the command is run (if a key does not exist already), then adds the key to the `authorized_keys2` file for the current user on each host within *chic26*. Then a host key for each *chic26* host is added to the `known_hosts` file for the current user on the *bosc26* host, unless `-o sshStrictKey=yes` has been specified. If that option is given, then all needed host keys must be present already on the *bosc26* host.

With these commands, acfsutil cluster info will be run using `chic26vip` or `bosc26vip`, respectively, to determine the members of the remote cluster.

The second command performs the same operations, but in the opposite direction. That is, the command configures a public key for the current user on the host within *chic26* where the command is run (if a key does not exist already), then adds the key to the `authorized_keys2` file for the current user on each host within *bosc26*. Then a host key for each *bosc26* host is added to the `known_hosts` file for the current user on the *chic26* host, unless `-o sshStrictKey=yes` has been specified. If that option is given, then all needed host keys must be present already on the *chic26* host.

The following example uses the same two clusters without a VIP configured for replication. In this example, the `-c` option specifies one of the remote node names. First, run this command on each node of `bosc26`:

```
# acfsreplssh configure -c chic26n1 -o sshStrictKey=no
```

Next, run this command on each node of `chic26`:

```
# acfsreplssh configure -c bosc26n1 -o sshStrictKey=no
```

With these commands, `acfsutil cluster info` will be run on *chic26n1* or *bosc26n1*, respectively, to determine the members of the remote cluster.

Verifying SSH Configuration on Each Local Host

Use the `acfsreplssh verify` command to verify the existing SSH keys. This command does not add or modify any keys - it simply tries to use the ones already present. To verify an existing key configuration, use the same command-line format that you used during configuration, but specify the `verify` keyword instead.

To verify the full set of keys required by replication, using the VIP defined on each cluster, run `acfsreplssh` as follows.

First, to verify the keys needed for replication from the primary cluster to the standby cluster, run this command on each node of *bosc26*:

```
# acfsreplssh verify -V chic26vip -c chic26vip
```

Next, to verify the keys needed for potential future replication from the current standby to the current primary, run this command on each node of *chic26*:

```
# acfsreplssh verify -V bosc26vip -c bosc26vip
```

Alternatively, to verify the full set of keys required by replication, without using a VIP, run `acfsreplssh` as follows. First, to verify the keys needed for replication from the primary cluster to the standby cluster, run this command on each node of *bosc26*:

```
# acfsreplssh verify -c chic26n1
```

Next, to verify the keys needed for potential future replication from the current standby to the current primary, run this command on each node of *chic26*:

```
# acfsreplssh verify -c bosc26n1
```

Removing SSH Configuration Information from Each Local Host

Use the `acfsreplssh remove` command to remove an existing set of SSH keys. The `acfsreplssh remove` command must be run on each local host where keys are to be removed. The command will remove keys associated with the named remote cluster, as well. To remove the keys that support a previous `repluser` configuration on a local host, use the same form of command line as you used to configure those keys on that host, just with the `remove` keyword specified instead of `configure`.

For instance, to return to our previous example of replication involving the use of a VIP, you can remove the set of keys that were previously configured, using the VIP defined on each cluster, by running `acfsreplssh` as follows.

First, run this command on each node of *bosc26*:

```
$ acfsreplssh remove -V chic26vip -c chic26vip
```

Next, run this command on each node of *chic26*:

```
$ acfsreplssh remove -V bosc26vip -c bosc26vip
```

Configuring SSH Manually

Perform the following procedures to manually configure SSH for replication in one direction - from the primary to the standby. To configure SSH completely, you must perform the instructions a second time with the primary and standby roles reversed. When you perform the instructions the first time, complete the steps as written for the primary cluster and the standby cluster. The second time, reverse the primary and standby roles. Perform the steps marked as necessary on the *primary* cluster on your standby cluster and perform the steps marked as necessary on the *standby* cluster on your primary cluster. The procedures that must be performed twice are described in:

After you have completed all the necessary procedures, you can use the instructions described in Validating your SSH-Related Key Configuration to confirm that you have configured SSH correctly in both directions.

### Distributing Keys for Oracle ACFS Replication

The process of distributing keys for Oracle ACFS replication includes getting a public key from the primary cluster, getting host keys for the standby cluster, ensuring permissions are configured properly for SSH-related files, configuring SSHD as necessary, and lastly validating the SSH configuration.

Note:

When creating host keys, ensure that you create keys for both fully-qualified domain hostnames and the local hostnames.

### Getting a Public Key for repluser From the Primary Cluster

A public key for `repluser` defined on each node of your primary cluster must be known to `repluser` on each node of your standby cluster.

To make this key known, the directory \` `~*` repluser `*/.ssh` `  must exist on each standby node. If this directory does not exist, then create it with access only for  ` repluser`. Ensure that an ` ls `  command for the  `.ssh\` directory displays output similar to:

```
repluser@standby $ ls -ld ~/.ssh
drwx------ 2 repluser dba 4096 Jan 27 17:01 .ssh
```

If a public key file for `repluser` exists on a given primary node, then add its contents to the set of keys authorized to log in as `repluser` on each node of the standby where replication is run. Append the key to the file \` `~*` repluser `*/.ssh/authorized_keys2` \` on each standby node, creating this file if necessary.

If a public key file does not exist, generate a public and private key pair on the primary by running the following command as `repluser`.

```
$ ssh-keygen -t rsa
```

You can press the enter key in response to each prompt issued by the command. Copy the resulting `.pub` file to each standby node.

You have the option to share the same public/private key pair for `repluser` across all of the nodes in your primary cluster, or to establish a different key pair for each primary node. If the same public key is valid for `repluser` across all nodes in your primary cluster, then only that key must be added to the file \` `~*` repluser `*/.ssh/authorized_keys2` `  on each node of your standby cluster. If each primary node has its own public key for  ` repluser`, then all the public keys must be added to the file. In either case, you can minimize work by copying the updated ` authorized\_keys2\` file on a given node of the standby to the other nodes of the cluster.

### Getting Host Keys for the Standby Cluster

A host key for each standby node where replication may run must be known on each primary node where replication may run. Generate the host key by running `ssh` manually as `repluser` from each primary node to each standby node. If your local system does not already recognize the host key, then a warning displays and you can enable SSH to add the key.

The following is an example of obtaining a host key:

```
[repluser@primary data]$ ssh repluser@standby date
The authenticity of host 'standby (10.137.13.85)' can't be established.
RSA key fingerprint is 1b:a9:c6:68:47:b4:ec:7c:df:3a:f0:2a:6f:cf:a7:0a.
Are you sure you want to continue connecting (yes/no)?
```

If you respond with `yes`, then the SSH setup is complete. A host key for host standby is stored in the `known_hosts` file (\` `~*` repluser `*/.ssh/known_hosts``) on the host _primary_ for ` repluser\`.

After the host key setup for standby nodes is complete on a given primary node, you need to perform an additional step if you use a Virtual IP address (VIP) to communicate with your standby cluster. You must add the VIP name or address at the start of each line of the `known_hosts` file that refers to a host in the standby cluster. For example, if you use a VIP with the name `standby12_vip`, and your `known_hosts` file contains the following two lines that refer to your standby:

```
standby1,10.242.20.22 ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQC3pM2YTd4UUiEWEoCKDGgaTgsmPkQToDrdtU+JtVIq/96muivU
BaJUK83aqzeNIQkh+hUULsUdgKoKT5bxrWYqhY6AlTEqNgBHjBrJt9C73BbQd9y48jsc2G+WQWyuI/
+s1Q+hIJdBNMxvMBQAfisPWWUcaIx9Y/JzlPgF6lRP2cbfqAzixDot9fqRrAKL3G6A75A/6TbwmEW07d1zqOv
l7ZGyeDYf5zQ72F/V0P9UgMEt/5DmcYTn3kTVGjOTbnRBe4A4lY4rVw5c+nZBDFre66XtORfQgwQB5ztW/Pi
08GYbcIszKoZx2HST9AZxYIAgcrnNYG2Ae0K6QLxxxScP
standby2,10.242.20.23 ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDIszcjzNtKN03SY8Kl846skFTVP1HF/ykswbmkctEjL6KTWTW+NR
U4MGbvkBqqdXxuPCR7aoGO2U3PEOg1UVf3DWUoux8IRvqKU+dJcdTibMFkDAIhTnzb14gZ/lRTjn+GYsuP5
Qz2vgL/U0ki887mZCRjWVL1b5FNH8sXBUV2QcD7bjF98VXF6n4gd5UiIC3jv6l2nVTKDwtNHpUTS1dQAi+1D
tr0AieZTsuxXMaDdUZHgKDotjciMB3mCkKm/u3IFoioDqdZE4+vITX9G7DBN4CVPXawp+b5Kg8X9P+08Eehu
tMlBJ5lafy1bxoVlXUDLVIIFBJNKrsqBvxxxpS7
```

To enable the use of the VIP, you would modify these two lines to read as follows:

```
standby12_vip,standby1,10.242.20.22 ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQC3pM2YTd4UUiEWEoCKDGgaTgsmPkQToDrdtU+JtVIq/96muivU
BaJUK83aqzeNIQkh+hUULsUdgKoKT5bxrWYqhY6AlTEqNgBHjBrJt9C73BbQd9y48jsc2G+WQWyuI/
+s1Q+hIJdBNMxvMBQAfisPWWUcaIx9Y/JzlPgF6lRP2cbfqAzixDot9fqRrAKL3G6A75A/6TbwmEW07d1zqOv
l7ZGyeDYf5zQ72F/V0P9UgMEt/5DmcYTn3kTVGjOTbnRBe4A4lY4rVw5c+nZBDFre66XtORfQgwQB5ztW/Pi
08GYbcIszKoZx2HST9AZxYIAgcrnNYG2Ae0K6QLxxxScP
standby12_vip,standby2,10.242.20.23 ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDIszcjzNtKN03SY8Kl846skFTVP1HF/ykswbmkctEjL6KTWTW+NR
U4MGbvkBqqdXxuPCR7aoGO2U3PEOg1UVf3DWUoux8IRvqKU+dJcdTibMFkDAIhTnzb14gZ/lRTjn+GYsuP5
Qz2vgL/U0ki887mZCRjWVL1b5FNH8sXBUV2QcD7bjF98VXF6n4gd5UiIC3jv6l2nVTKDwtNHpUTS1dQAi+1D
tr0AieZTsuxXMaDdUZHgKDotjciMB3mCkKm/u3IFoioDqdZE4+vITX9G7DBN4CVPXawp+b5Kg8X9P+08Eehu
tMlBJ5lafy1bxoVlXUDLVIIFBJNKrsqBvxxxpS7
```

After you configure the host keys on the first node in your primary cluster, copy the updated `known_hosts` file to every other node in the cluster. This approach minimizes the manual effort required to configure each node.

Note:

By default, replication enables SSH strict host key checking to ensure that the primary node connects to the intended standby node or cluster. If your primary and standby clusters communicate over a trusted private network, you can disable strict host key checking. For information about disabling strict host key checking, refer to the `-o sshStrictKey=no` option of the `acfsutil repl init primary` command. For information about the `acfsutil repl init` command, refer to [acfsutil repl init](managing-oracle-acfs-with-command-line-tools.md).

### Notes on Permissions for SSH-Related Files

For SSH to work with the keys you have established, you must ensure that permissions are set properly on each node for the `.ssh` directory for `repluser` and some of the files the directory contains.

For details on the permissions that should be given to each `.ssh` directory and key files within the directory, refer to the documentation for your SSH implementation, such as the `FILES` section of the `ssh(1)` manual page.

### Notes on SSHD Configuration

After you begin using replication, SSH is started frequently to perform replication operations. On some platforms, the SSH daemon (`sshd`) logs a message through `syslog` or a similar facility each time that an SSH connection is established. To avoid this, the server configuration file `/etc/ssh/sshd_config` can be modified to specify a lower frequency of logging. The parameter that controls logging is called `LogLevel`. Connection messages are issued at level `INFO`. Any lower `LogLevel` setting, such as `ERROR`, suppresses those messages. For example, you can suppress log messages by adding the following line to the file:

```
LogLevel ERROR
```

### Validating your SSH-Related Key Configuration

After you have established the host and user keys for SSH on both your primary and your standby clusters, you can use the command `acfsutil` `repl` `info` `-c` `-u` to validate the keys. You run this command as `repluser` on each node of each cluster. It takes as arguments all the hostnames or addresses on the remote cluster that the local cluster may use in the future to perform replication.

If you are not using a VIP to connect to your remote cluster, then for a given replication relationship, only one remote hostname or address is provided to `acfsutil` `repl` `init` `primary`. However, if future relationships involve other remote host addresses, specify the complete set of remote addresses when running the `acfsutil repl info -c -u` command.

If you are using a VIP to connect to your remote cluster, then you should specify the names or host-specific addresses of all remote hosts on which the VIP may be active. Do not specify the VIP name or an address associated with the VIP. When replication uses SSH to connect to a VIP, the host key returned is the key associated with the host where the VIP is currently active. Only the hostnames or addresses of individual remote nodes are used by SSH in this situation.

Run the following validation command on each node of your primary cluster:

```
$ acfsutil repl info -c -u repluser standby1 [standby2 ...] [snap_shot@]primary-mountpoint
```

In the command, `standby` `n` specifies the standby cluster hostname or address. The validation command confirms that `repluser` can use SSH to connect to each standby hostname or address given, in the same manner as replication initialization. Use the same command format if you are using a VIP, such as `standby12_vip`, to connect to the cluster. Do not specify the name of the VIP.

If you plan to disable strict host key checking, you can skip this checking by adding the `-o sshStrictKey=no` option to the command line.

After you have confirmed that each node of your primary cluster can connect to all nodes of your standby cluster, run the validation command again. This time run the command on each node of your standby cluster. Specify a hostname or IP address for all nodes of your primary cluster using the following format:

```
$ acfsutil repl info -c -u repluser primary1 [primary2 ...] [snap_shot@]standby-mountpoint
```

In the command, `primary` `n` specifies the primary cluster hostname or address.

## Installing ssh and Cygwin on Windows

This section describes how to install Cygwin and start the `ssh` daemon on Microsoft Windows hosts. This information is only applicable when you want to use Oracle ACFS snapshot-based replication on a Windows host.

### Cygwin Requirement for Oracle ACFS Replication

Oracle ACFS snapshot-based replication uses `ssh` to transfer replication-related data from the primary cluster to the standby cluster. When you use replication on a host running on Microsoft Windows, you must install Cygwin and start the `ssh` daemon on the host, as described in this section.

Cygwin is essentially a utility that offers a Linux-like environment on a Microsoft Windows host. Technically, it is a DLL (`cygwin1.dll`) that acts as a Linux API layer providing substantial Linux API functionality. After you install Cygwin, you can configure the `ssh` daemon on the host. Oracle ACFS replication is certified and supported with Cygwin 2.0.

The `ssh` daemon enables Oracle ACFS Replication to establish `ssh` connectivity from the primary cluster running replication to the standby cluster running replication.

Note:

These instructions for installing the `ssh` daemon result in a daemon that is usable only to log in and run commands as the specific user *repluser*. The daemon is not intended to work correctly when logging in and running commands as any other user. This restriction results from two factors:

- Users defined for Oracle ACFS must be domain-based users.
- Enabling the general-purpose use of the `ssh` daemon for a domain-based user involves creating a domain policy that gives that user some very powerful privileges, including `SeTcbPrivilege` which lets the user act as part of the *Trusted Computing Base*. Creating such a policy would not likely be allowed in most corporate environments, so the use of such a policy is not included in these instructions.

### Steps Before Installing Cygwin

Before starting with the `ssh` setup, ensure you are not using `OpenSSH` and `MKSNT` by performing the checks in the following steps.

Note that the navigational steps described in this section may vary for different Microsoft Windows operating systems.

1. Ensure `OpenSSH\bin` and any directory where `mksnt` executable files are stored are not in your `PATH` environment variable. If they are, remove them from the path string by performing the following:
2. Right-click on **My Computer** and go to **Properties**.
3. In the **System Properties** window, click **Advanced**.
4. In this tab, click **Environment Variables**.
5. Search for the `PATH` system variable, select it, and if `OpenSSH\bin` or `mksnt` -related values are present in `PATH` string, click **Edit**.
6. In the Edit System Variable dialog box, delete these values from `PATH` string, then click **OK**.
7. Stop and disable the `ssh` `daemon` if it is running from `OpenSSH`, `MKS` or any other source. If the `ssh` daemon is running, stop and disable it by doing the following:
8. Right-click on **My Computer**, and select **Manage**.
9. In the **Computer Management** window, in the left pane, expand **Services and Applications**, and select **Services**.
	- In the right pane, right-click the `ssh` daemon/ `MKS Secure Shell` service, then click the **Stop** entry on the menu that appears.
		- In the same pane, right-click the `ssh` daemon/ `MKS Secure Shell` service, then click the **Properties** entry on the menu that appears. In the dialog box that opens, select **Disabled** as the **Startup** type, and click **OK**.

### Installing Cygwin

To install Cygwin on a Microsoft Windows host, perform the following steps:

1. Access the following URL, then click **Install Cygwin**:
	```
	http://www.cygwin.com/
	```
2. Depending on the version of Microsoft Windows you are running, download the 32-bit version or the 64-bit version of the Cygwin setup executable.
3. Run the setup executable, then click **Next** to proceed.
4. On the **Choose Installation Type** screen, select **Install from Internet**, then click **Next**.
5. On the **Choose Installation Directory** screen, enter `C:\cygwin` as the **Root Directory**, then click **Next**.
6. On the **Select Local Package Directory** screen, select a directory on your local machine where you want to store the downloaded installation files, then click **Next**.
7. On the **Select Connection Type** screen, select appropriate settings to connect to the internet, then click **Next**.
8. On the **Choose Download Site(s)** screen, select any site from the available list, then click **Next**.
9. On the select packages screen, ensure that you select the following packages, then click **Next**. From the **Archive** category, select **unzip** and **zip**. From the **Net** category, select **openssh** and **openssl**. After selecting the packages and clicking **Next**, the **Resolving Dependencies** screen is displayed. Click **Next** to proceed.
10. On the **Installation Status and Create Icons** screen, do not make any changes. Click **Finish** to complete the installation process.

### Configuring ssh

This section describes how to configure `ssh` for Oracle ACFS replication after installing Cygwin on a host.

Choosing Replication Users

Oracle ACFS Replication uses `ssh` as the transport between the primary and standby clusters, so the user identities under which replication is performed need to be explicitly specified. In the replication process, a privileged user on the primary node uses `ssh` to log in to the standby node involved in replication. It is not desirable for `ssh` to log in as a privileged user on the standby node. Instead, a minimally-privileged user identity should be used. The user chosen must be a domain-based user, and must be a member of the `ORA_ASMADMIN` group.

In this discussion, *repladmin* and *repluser* are used to refer to the replication users; however, you would replace *repladmin* and *repladmin* with the actual user names that you have selected. The *repladmin* user refers to the user that runs the `acfsutil` `repl` `init` command on both the primary and the standby. This user must be a member of the `Administrators` group. The *repluser* user refers to the user that `ssh` uses to log in on the standby. This user must be a domain-based user, and must be a member of the `ORA_ASMADMIN` group, but not a member of the `Administrators` group. If a suitable user already exists for the use of Oracle RAC, that user should be used as *repluser*.

For information about user privileges for Oracle ASM, refer to [About Privileges for Oracle ASM](administering-oracle-asm-instances.md). For information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](managing-oracle-acfs-with-command-line-tools.md).

Configuration Steps

While configuring `ssh`, you may need to run the `cygwin.bat` script. While running `cygwin.bat` on Microsoft Windows Server 2008 and Microsoft Windows Vista, ensure that you invoke the batch file in administrator mode. To do this, right-click the `cygwin.bat` file and select `Run as administrator`.

To configure `ssh` and test your Cygwin setup, follow these steps:

1. After you install Cygwin, navigate to the `C:\cygwin` directory, open the Cygwin.bat file in edit mode using any editor, and add the following line before invoking the `bash` shell.
	```
	set CYGWIN=binmode ntsec
	```
	The following lines are the possible contents of the `Cygwin.bat` file after adding the previous line:
	```
	@echo off  
	C: 
	chdir C:\cygwin\bin 
	set CYGWIN=binmode ntsec bash --login -i
	```
2. To verify if Cygwin (`cygrunsrv`) is installed properly, run `C:\cygwin\Cygwin.bat`, and run the following command:
	```
	cygrunsrv -h
	```
	If Cygwin is installed properly, then all Cygwin help options are displayed on the screen. If the command returns an error message, then you may have to reinstall Cygwin.
3. Define the *repladmin* and *repluser* identities at the Windows level.
	You can also use existing users instead for these roles. If you define new identities for these roles, note the following:
	- The *repladmin* user must be a member of the Administrators group. It is recommended that *repladmin* also be a domain-based user. If *repladmin* is a local user, it should be defined with the same group memberships on all primary nodes.
		- The *repluser* user must be a domain-based user, and must be a member of the `ORA_ASMADMIN` group.
4. Configure the `sshd` service. Run `C:\cygwin\Cygwin.bat`, and execute the following command:
	```
	ssh-host-config
	```
	After running the command, you are prompted with the following questions. Appropriate responses are shown in bold. Other output may also appear, but is not shown here.
	```
	*** Query: Should StrictModes be used? (yes/no) yes
	*** Query: Should privilege separation be used? <yes/no>: yes
	*** Query: New local account 'sshd'? <yes/no>: yes
	*** Query: Do you want to install sshd as a service?
	*** Query: <Say "no" if it is already installed as a service> <yes/no>: yes
	*** Query: Enter the value of CYGWIN for the daemon: [] binmode ntsec
	```
	Now `ssh-host-config` outputs some notes concerning the user account required to use passwordless logins. This capability is required by Oracle ACFS replication. The *repluser* account should be specified as this account.
	```
	*** Info: The following privileged accounts were found: 'cyg_server' .
	*** Info: This script plans to use 'cyg_server'.
	*** Info: 'cyg_server' will only be used by registered services.
	*** Query: Do you want to use a different name? (yes/no) yes
	```
	You should respond **yes** to the prompt, and should specify *repluser* as the name under which you run `sshd`. You are then prompted with the following questions.
	```
	*** Query: Enter the new user name: repluser
	*** Query: Reenter: repluser
	***Warning: The specified account 'repluser' does not have the
	***Warning: required permissions or group memberships.  This may
	***Warning: cause problems if not corrected; continuing...
	*** Query: Please enter the password for user 'repluser':
	*** Query: Reenter:
	```
	The above assumes that the user *repluser* already exists. You may ignore the warning output about missing permissions or group memberships. If the configuration is successful, the following message displays.
	```
	Host configuration finished. Have fun!
	```
5. Ensure that the directory `/var/empty` exists and is owned by *repluser*.
6. Ensure that the *repluser* and *repladmin* users are known to Cygwin.
	Backup the `c:\cygwin\etc\passwd` file and then open the file in edit mode. Remove any lines from this file that refer to the *repladmin* or *repluser* users. For each user, run the following command. Both users are assumed to be domain-based users.
	```
	/bin/mkpasswd -d -u repladmin >> /etc/passwd
	```
	Ensure that the home directory named for each user in `/etc/passwd` exists. If necessary, create it. For example, if `/home/repladmin` is the directory shown for user *repladmin*, perform the following to create the necessary directory.
	```
	mkdir -p /home/repladmin
	chown repladmin /home/repladmin
	```
7. Ensure that the `ssh` daemon starts, and is configured to start automatically:
	1. Right-click on **My Computer**, and select **Manage**.
		2. In the **Computer Management** window, in the left pane, expand **Services and Applications**, and select **Services**.
		3. In the right pane, right-click the **CYGWIN** **sshd** service, then click the **Properties** entry on the menu that appears. In the dialog box that opens, select **Automatic** as the **Startup** type, and click **OK**.

If the `ssh` daemon does not start, view the `c:\cygwin\var\log\sshd.log` file for information that relates to the failure of the startup process.

Getting the public key for repladmin from the primary

A public key for *repladmin* defined on each node of your primary cluster must be known to *repluser* on each node of your standby cluster.

To make the key known, the directory `~repluser/.ssh` must exist on each standby node. If this directory does not exist, then create it with access only for *repluser*. Ensure that an `ls` command for the `.ssh` directory displays output similar to:

```
repluser@standby $ ls -ld ~/.ssh
drwx------+ 1 repluser Domain Users 4096 2016-02-23 11:27 .ssh
```

If a public key for *repladmin* is defined on a given primary node, then it resides in a `.pub` file, such as `~repladmin/.ssh/id_rsa.pub`. If a public key file exists, then add its contents to the set of keys authorized to log in as *repluser* on each node of the standby where replication is run. Append the key to the file `~repluser/.ssh/authorized_keys2` on each standby node, creating this file if necessary.

If a public key file does not exist, generate a public and private key pair on the primary by running the following command as *repladmin*.

```
# ssh-keygen -t rsa
```

You can press the enter key in response to each prompt issued by the command. Copy the resulting `.pub` file to each standby node.

You have the option to share the same public/private key pair for *repladmin* across all of the nodes in your primary cluster, or to establish a different key pair for each primary node. If the same public key is valid for *repladmin* across all nodes in your primary cluster, then only that key must be added to the file `~repluser/.ssh/authorized_keys2` on each node of your standby cluster. If each primary node has its own public key for *repladmin*, then all the public keys must be added to the file. In either case, you can minimize work by copying the updated `authorized_keys2` file on a given node of the standby to the other nodes of the cluster.

Getting the standby host key

A host key for each standby node where replication may run must be known on each primary node where replication may run. One way to generate the correct key is to run `ssh` manually as the *repladmin* user from each primary node to each standby node. If the correct host key is not known already, then a warning displays and you can enable `ssh` to add the key.

Note that there are two users involved in the `ssh` connection. While `ssh` on the primary node connects to the standby node as *repladmin*, `ssh` logs in on the standby node as *repluser*. Any command run by `ssh` on the standby runs with the privileges of *repluser*, not with *repladmin* privileges.

Because the primary node connects to the standby node as user *repladmin*, the host key for the standby node must be added to the `known_hosts` file of the *repladmin* user, not the file for *repluser*. The following is an example of obtaining a host key:

```
[repladmin@primary usm]# ssh repluser@standby date
The authenticity of host 'standby (10.137.13.85)' can't be established.
RSA key fingerprint is 1b:a9:c6:68:47:b4:ec:7c:df:3a:f0:2a:6f:cf:a7:0a.
Are you sure you want to continue connecting (yes/no)?
```

If you respond with `yes`, then the `ssh` setup is complete. A host key for host standby is stored in the `known_hosts` file (`~repladmin/.ssh/known_hosts`) on the host *primary* for the user *repladmin*.

After the host key setup for standby nodes is complete on a given primary node, you need to perform an additional step if you use a Virtual IP address (VIP) to communicate with your standby cluster. You must add the VIP name or address at the start of each line of the `known_hosts` file that refers to a host in the standby cluster. For example, if you use a VIP with the name `standby12_vip`, and your `known_hosts` file contains the following two lines that refer to your standby:

```
standby1,10.242.20.22 ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQC3pM2YTd4UUiEWEoCKDGgaTgsmPkQToDrdtU+JtVIq/96muivU
BaJUK83aqzeNIQkh+hUULsUdgKoKT5bxrWYqhY6AlTEqNgBHjBrJt9C73BbQd9y48jsc2G+WQWyuI/
+s1Q+hIJdBNMxvMBQAfisPWWUcaIx9Y/JzlPgF6lRP2cbfqAzixDot9fqRrAKL3G6A75A/6TbwmEW07d1zqOv
l7ZGyeDYf5zQ72F/V0P9UgMEt/5DmcYTn3kTVGjOTbnRBe4A4lY4rVw5c+nZBDFre66XtORfQgwQB5ztW/Pi
08GYbcIszKoZx2HST9AZxYIAgcrnNYG2Ae0K6QLxxxScP
standby2,10.242.20.23 ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDIszcjzNtKN03SY8Kl846skFTVP1HF/ykswbmkctEjL6KTWTW+NR
U4MGbvkBqqdXxuPCR7aoGO2U3PEOg1UVf3DWUoux8IRvqKU+dJcdTibMFkDAIhTnzb14gZ/lRTjn+GYsuP5
Qz2vgL/U0ki887mZCRjWVL1b5FNH8sXBUV2QcD7bjF98VXF6n4gd5UiIC3jv6l2nVTKDwtNHpUTS1dQAi+1D
tr0AieZTsuxXMaDdUZHgKDotjciMB3mCkKm/u3IFoioDqdZE4+vITX9G7DBN4CVPXawp+b5Kg8X9P+08Eehu
tMlBJ5lafy1bxoVlXUDLVIIFBJNKrsqBvxxxpS7
```

To enable the use of the VIP, you would modify these two lines to read as follows:

```
standby12_vip,standby1,10.242.20.22 ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQC3pM2YTd4UUiEWEoCKDGgaTgsmPkQToDrdtU+JtVIq/96muivU
BaJUK83aqzeNIQkh+hUULsUdgKoKT5bxrWYqhY6AlTEqNgBHjBrJt9C73BbQd9y48jsc2G+WQWyuI/
+s1Q+hIJdBNMxvMBQAfisPWWUcaIx9Y/JzlPgF6lRP2cbfqAzixDot9fqRrAKL3G6A75A/6TbwmEW07d1zqOv
l7ZGyeDYf5zQ72F/V0P9UgMEt/5DmcYTn3kTVGjOTbnRBe4A4lY4rVw5c+nZBDFre66XtORfQgwQB5ztW/Pi
08GYbcIszKoZx2HST9AZxYIAgcrnNYG2Ae0K6QLxxxScP
standby12_vip,standby2,10.242.20.23 ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDIszcjzNtKN03SY8Kl846skFTVP1HF/ykswbmkctEjL6KTWTW+NR
U4MGbvkBqqdXxuPCR7aoGO2U3PEOg1UVf3DWUoux8IRvqKU+dJcdTibMFkDAIhTnzb14gZ/lRTjn+GYsuP5
Qz2vgL/U0ki887mZCRjWVL1b5FNH8sXBUV2QcD7bjF98VXF6n4gd5UiIC3jv6l2nVTKDwtNHpUTS1dQAi+1D
tr0AieZTsuxXMaDdUZHgKDotjciMB3mCkKm/u3IFoioDqdZE4+vITX9G7DBN4CVPXawp+b5Kg8X9P+08Eehu
tMlBJ5lafy1bxoVlXUDLVIIFBJNKrsqBvxxxpS7
```

Ultimately, the host key configuration performed on this first node of your primary cluster must be performed on every node in your primary cluster; the result of the above sequence, or an equivalent, must exist on each primary node. One way to minimize the manual effort required to achieve this configuration is to update the `known_hosts` file on one node of the primary cluster, then copy the updated file to the other nodes of the cluster.

Note:

By default, replication enables strict host key checking by `ssh`, to ensure that the primary node connects to the intended standby node or cluster when it runs `ssh`. However, if you are certain that this checking is unneeded, such as the case when the primary and standby clusters communicate over a private network, the use of strict host key checking by `ssh` can be disabled. For information about disabling strict host key checking, refer to the `/o sshStrictKey=no` option of the `acfsutil` `repl` `init` `primary` command. If strict host key checking is disabled, then no host key setup is required. For information about the `acfsutil` `repl` `init` command, refer to [acfsutil repl init](managing-oracle-acfs-with-command-line-tools.md).

Adding keys for the SYSTEM user

Oracle ACFS replication uses a daemon running on a node of the primary cluster to control the progress of replication. This daemon is automatically started using the identity `NT_AUTHORITY\SYSTEM`. With this daemon, replication, using `ssh`, is able to transfer and apply primary data to the standby site.

The processes started by the daemon have the identity of the daemon. If the user is `NT_AUTHORITY\SYSTEM`, that is the user actually contacting the standby through `ssh`. `ssh` searches in the home directory for the `SYSTEM` user for a public key to present to the standby, and checks there to verify the host key presented by the standby.

To enable the daemon's successful use of `ssh`, the contents of the `.ssh` directory set up for *repladmin* on the primary should be copied to a `.ssh` directory in the home directory for `SYSTEM`. Use a location for this directory that is parallel to the locations used for other home directories.

For instance, if the home directory for user *repladmin* is `/home/repladmin`, then use `/home/SYSTEM` as the home directory for `SYSTEM`. Create the `.ssh` directory like this, while logged in as *repladmin*.

First, create the home directory for `SYSTEM` if it does not already exist:

```
$ mkdir /home/SYSTEM
```

Next, copy the `.ssh` directory for *repladmin* into the directory for `SYSTEM`:

```
$ cd  $HOME
 $ cp -p -R .ssh /home/SYSTEM
```

### Testing Your Cygwin Setup

Now test your Cygwin setup. Using a different computer that has the `ssh` client available, execute the following command as the user *repladmin*:

```
ssh -l repluser host-address date
```

where `host-address` refers to the host where you just configured `ssh`. For example:

```
ssh -l repluser standby1.us.example.com date
```

If you have completed the installation and configuring steps successfully, the previous command should run without prompting for a password.

If you experience a process fork failure, memory leak error, or a file access error after configuring `ssh`, view the following link for a workaround:

```
http://cygwin.com/faq.html
```

If you are unable to find a workaround for your problem, report your problem to the Cygwin community using the following link:

```
http://cygwin.com/problems.html
```

## Upgrading to Oracle ACFS Snapshot-Based Replication

This section describes the upgrade to Oracle ACFS snapshot-based replication. With Oracle Grid Infrastructure 12c release 2 (12.2), Oracle ACFS snapshot-based replication becomes the supported Oracle ACFS replication implementation. If you have a replication environment from a release before 12.2, then you must upgrade your existing replication installation to snapshot-based replication when you upgrade to Oracle Grid Infrastructure 12c release 2 (12.2).

Note:

- After the replication upgrade process has started, it must be completed. The process cannot be rolled back.
- Oracle Flex ASM should be enabled, and if necessary a password file conversion performed, before upgrading to snapshot-based replication.

Oracle Flex ASM must be enabled for any existing instance when the instance is upgraded to Oracle Grid Infrastructure 12c release 2 (12.2). If a password file exists in the instance to support replication, the file must be enabled for use in the new Oracle Flex ASM instance. For example, if an instance had a previous `ORACLE_SID` set to `ASM` and a current `ORACLE_SID` set to `APX1`, then the following steps must be performed:

1. Copy the existing `orapw+ASM` file to an `+APX1` version
	```
	$ cp /oraroot/app/12.2.0/has0626/dbs/orapw+ASM /oraroot/app/12.2.0/has0626/dbs/orapw+APX1
	```
2. Create a new text file called `init+APX1.ora` in the `dbs` directory and add only the following line to the new file:
	```
	remote_login_passwordfile = exclusive
	```
3. Restart the Oracle ASM proxy (APX) instance.
	```
	$ asmcmd shutdown --target APX --immediate
	```
	Ensure that the environment variable `ORACLE_SID` is set to the Oracle ASM proxy (APX) instance. Then restart the instance.
	```
	$ asmcmd startup --pfile init+APX1.ora
	```

Snapshot-based replication uses `ssh` as the transport between the primary and standby clusters. Before starting the upgrade process, you must configure `ssh` as described in Configuring SSH for Use with Oracle ACFS Replication.

Before upgrading to snapshot-based replication, you must upgrade your standby cluster system to Oracle Grid Infrastructure 12c release 2 (12.2).This cluster upgrade should be completed within 24 hours. The standby cluster continues to run existing replication during this upgrade process. Next, upgrade to Oracle Grid Infrastructure 12c release 2 (12.2) on the primary cluster. This upgrade should also be completed within 24 hours. During this upgrade, the primary cluster continues to run existing replication that was installed before 12.2. After the completion of the Oracle Grid Infrastructure 12c release 2 (12.2) upgrade of the standby and primary clusters, the existing replication implementation installed before 12.2 is not supported.

Immediately following the upgrade of the two clusters, you must set the `COMPATIBLE.ADVM` disk group attribute associated with the file systems to be involved in replication to `12.2.0.0.0`. Now you are ready to transition to snapshot-based replication. The transition can made with one of the following options:

- Terminate your existing replication and initialize to use snapshot-based replication. This option is recommended if the amount of data being replicated is small (less than a few hundred gigabytes). This option may also be preferable if your primary file system cannot easily be restricted to being mounted on only one node, or if activity on the primary cannot easily be quiesced.
- Run the `acfsutil` `repl` `upgrade` command to upgrade your existing replication environment without terminating and initializing replication. This option avoids the need to transfer the entire contents of your primary file system to the standby by enabling snapshot-based replication to continue from the point where existing replication has stopped. This option is advantageous when larger amounts of data are being replicated. Because very little data is transferred by the upgrade process, you can expect the process to complete quickly.

The following list provides details on running the `acfsutil` `repl` `upgrade` command options to upgrade to snapshot-based replication.

- Before starting the replication upgrade process, you must ensure that your primary file system is mounted on only one node of the primary cluster. In addition, it is strongly recommended that you quiesce all application updates to the primary file system, then run `acfsutil` `repl` `sync` `apply` one final time to ensure all changes on the primary are replicated.
- The initial step in the upgrade process is to run the `acfsutil` `repl` `upgrade` `prepare` command on the primary cluster. This command specifies the user and host or interface name that will be used for snapshot-based replication, as well as the primary mount point. The user and host names are given with the `-s` option, exactly as they are for the `acfsutil` `repl` `init` `primary` command used for snapshot-based replication.
- The next step in the process is to upgrade replication on the standby cluster, by running the `acfsutil` `repl` `upgrade` `standby` command. This command specifies the user to be used for snapshot-based replication, as well as the standby mount point. The user name is given with the `-u` option, exactly as it is for the `acfsutil` `repl` `init` `standby` command used for snapshot-based replication.
- The final step in the process is to run the a `acfsutil` `repl` `upgrade` `primary` command on the primary cluster. This is the command that automatically terminates the previous replication deployment and initiates snapshot-based replication. This command accepts any of the command-line options accepted by the `acfsutil` `repl` `init` `primary` command for snapshot-based replication, except for the `-m` and `-s` options, as that information is obtained from the now-terminated previous replication environment.
- After the `acfsutil` `repl` `upgrade` `primary` command completes, snapshot-based replication should be active between the affected primary and standby clusters, exactly as though the `acfsutil` `repl` `init` commands had been run with snapshot-based replication in the 12.2 release. You can use the command `acfsutil` `repl` `info` `-c` on both the primary and standby cluster to confirm the status of replication on each cluster.

Note:

If an error occurs in running either `acfsutil` `repl` `upgrade` `standby` or `acfsutil` `repl` `upgrade` `primary`, then consider the following:

- Depending on the error, replication may appear to be uninitialized (`acfsutil` `repl` `info` may indicate that) until the upgrade command has completed successfully.
- To continue with the upgrade, you should correct whatever error was indicated by the failing upgrade command, then simply re-issue the failing command. The command may be re-issued multiple times.