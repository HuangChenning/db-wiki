---
title: How to Complete Installation Prerequisite Tasks Manually
book: Grid Infrastructure Installation Guide for Linux
doc_id: E41961-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41961/manpreins.htm
tags:
  - oracle
  - 11g
  - grid-infrastructure-installation-guide-for-linux
---

## E How to Complete Installation Prerequisite Tasks Manually

This appendix provides instructions for how to complete configuration tasks manually that Cluster Verification Utility (CVU) and the installer (OUI) normally complete during installation. Use this appendix as a guide if you cannot use the fixup script.

This appendix contains the following information:

## E.1 Configuring SSH Manually on All Cluster Nodes

Passwordless SSH configuration is a mandatory installation requirement. SSH is used during installation to configure cluster member nodes, and SSH is used after installation by configuration assistants, Oracle Enterprise Manager, OPatch, and other features.

Automatic Passwordless SSH configuration using OUI creates RSA encryption keys on all nodes of the cluster. If you have system restrictions that require you to set up SSH manually, such as using DSA keys, then use this procedure as a guide to set up passwordless SSH.

In the examples that follow, the Oracle software owner listed is the `grid` user.

If SSH is not available, then OUI attempts to use rsh and rcp instead. However, these services are disabled by default on most Linux systems.

Note:

The supported version of SSH for Linux distributions is OpenSSH.

This section contains the following:

- Checking Existing SSH Configuration on the System
- Configuring SSH on Cluster Nodes
- Enabling SSH User Equivalency on Cluster Nodes

### E.1.1 Checking Existing SSH Configuration on the System

To determine if SSH is running, enter the following command:

```
$ pgrep sshd
```

If SSH is running, then the response to this command is one or more process ID numbers. In the home directory of the installation software owner (`grid`, `oracle`), use the command `ls -al` to ensure that the `.ssh` directory is owned and writable only by the user.

You need either an RSA or a DSA key for the SSH protocol. RSA is used with the SSH 1.5 protocol, while DSA is the default for the SSH 2.0 protocol. With OpenSSH, you can use either RSA or DSA. The instructions that follow are for SSH1. If you have an SSH2 installation, and you cannot use SSH1, then refer to your SSH distribution documentation to configure SSH1 compatibility or to configure SSH2 with DSA.

### E.1.2 Configuring SSH on Cluster Nodes

To configure SSH, you must first create RSA or DSA keys on each cluster node, and then copy all the keys generated on all cluster node members into an authorized keys file that is identical on each node. Note that the SSH files must be readable only by `root` and by the software installation user (`oracle`, `grid`), as SSH ignores a private key file if it is accessible by others. In the examples that follow, the DSA key is used.

You must configure SSH separately for each Oracle software installation owner that you intend to use for installation.

To configure SSH, complete the following:

#### E.1.2.1 Create SSH Directory, and Create SSH Keys On Each Node

Complete the following steps on each node:

1. Log in as the software owner (in this example, the `grid` user).
2. To ensure that you are logged in as `grid`, and to verify that the user ID matches the expected user ID you have assigned to the `grid` user, enter the commands `id` and `id grid`. Ensure that Oracle user group and user and the user terminal window process you are using have group and user IDs are identical. For example:
	```
	$ id 
	uid=502(grid) gid=501(oinstall) groups=501(oinstall),502(grid,asmadmin,asmdba)
	$ id grid
	uid=502(grid) gid=501(oinstall) groups=501(oinstall),502(grid,asmadmin,asmdba)
	```
3. If necessary, create the `.ssh` directory in the `grid` user's home directory, and set permissions on it to ensure that only the oracle user has read and write permissions:
	```
	$ mkdir ~/.ssh
	$ chmod 700 ~/.ssh
	```
	Note:
	SSH configuration will fail if the permissions are not set to 700.
4. Enter the following command:
	```
	$ /usr/bin/ssh-keygen -t dsa
	```
	At the prompts, accept the default location for the key file (press Enter).
	Note:
	SSH with passphrase is not supported for Oracle Clusterware 11g release 2 and later releases.
	This command writes the DSA public key to the `~/.ssh/id_dsa.pub` file and the private key to the `~/.ssh/id_dsa` file.
	Never distribute the private key to anyone not authorized to perform Oracle software installations.
5. Repeat steps 1 through 4 on each node that you intend to make a member of the cluster, using the DSA key.

#### E.1.2.2 Add All Keys to a Common authorized\_keys File

Complete the following steps:

1. On the local node, change directories to the `.ssh` directory in the Oracle Grid Infrastructure owner's home directory (typically, either `grid` or `oracle`).
	Then, add the DSA key to the `authorized_keys` file using the following commands:
	```
	$ cat id_dsa.pub >> authorized_keys
	$ ls
	```
	In the ssh directory, you should see the `id_dsa.pub` keys that you have created, and the file `authorized_keys`.
2. On the local node, use SCP (Secure Copy) or SFTP (Secure FTP) to copy the `authorized_keys` file to the `oracle` user `.ssh` directory on a remote node. The following example is with SCP, on a node called node2, with the Oracle Grid Infrastructure owner `grid`, where the `grid` user path is `/home/grid`:
	```
	[grid@node1 .ssh]$ scp authorized_keys node2:/home/grid/.ssh/
	```
	You are prompted to accept a DSA key. Enter Yes, and you see that the node you are copying to is added to the `known_hosts` file.
	When prompted, provide the password for the grid user, which should be the same on all nodes in the cluster. The `authorized_keys` file is copied to the remote node.
	Your output should be similar to the following, where `xxx` represents parts of a valid IP address:
	```
	[grid@node1 .ssh]$ scp authorized_keys node2:/home/grid/.ssh/
	The authenticity of host 'node2 (xxx.xxx.173.152) can't be established.
	DSA key fingerprint is 7e:60:60:ae:40:40:d1:a6:f7:4e:zz:me:a7:48:ae:f6:7e.
	Are you sure you want to continue connecting (yes/no)? yes
	Warning: Permanently added 'node1,xxx.xxx.173.152' (dsa) to the list
	of known hosts
	grid@node2's password:
	authorized_keys       100%             828             7.5MB/s      00:00
	```
3. Using SSH, log in to the node where you copied the `authorized_keys` file. Then change to the `.ssh` directory, and using the `cat` command, add the DSA keys for the second node to the `authorized_keys` file, clicking Enter when you are prompted for a password, so that passwordless SSH is set up:
	```
	[grid@node1 .ssh]$ ssh node2
	[grid@node2 grid]$ cd .ssh
	[grid@node2 ssh]$ cat id_dsa.pub  >> authorized_keys
	```
	Repeat steps 2 and 3 from each node to each other member node in the cluster.
	When you have added keys from each cluster node member to the `authorized_keys` file on the last node you want to have as a cluster node member, then use `scp` to copy the `authorized_keys` file with the keys from all nodes back to each cluster node member, overwriting the existing version on the other nodes.
	To confirm that you have all nodes in the `authorized_keys` file, enter the command `more authorized_keys`, and determine if there is a DSA key for each member node. The file lists the type of key (`ssh-dsa`), followed by the key, and then followed by the user and server. For example:
	```
	ssh-dsa AAAABBBB . . . = grid@node1
	```
	Note:
	The `grid` user's `/.ssh/authorized_keys` file on every node must contain the contents from all of the `/.ssh/id_dsa.pub` files that you generated on all cluster nodes.

### E.1.3 Enabling SSH User Equivalency on Cluster Nodes

After you have copied the `authorized_keys` file that contains all keys to each node in the cluster, complete the following procedure, in the order listed. In this example, the Oracle Grid Infrastructure software owner is named `grid`:

1. On the system where you want to run OUI, log in as the `grid` user.
2. Use the following command syntax, where `hostname1`, `hostname2`, and so on, are the public host names (alias and fully qualified domain name) of nodes in the cluster to run SSH from the local node to each node, including from the local node to itself, and from each node to each other node:
	```
	[grid@nodename]$ ssh hostname1 date
	[grid@nodename]$ ssh hostname2 date
	    .
	    .
	    .
	```
	For example:
	```
	[grid@node1 grid]$ ssh node1 date
	The authenticity of host 'node1 (xxx.xxx.100.101)' can't be established.
	DSA key fingerprint is 7z:60:60:zz:48:48:z1:a0:f7:4e.
	Are you sure you want to continue connecting (yes/no)? yes
	Warning: Permanently added 'node1,xxx.xxx.100.101' (DSA) to the list of
	known hosts.
	Mon Dec 4 11:08:13 PST 2006
	[grid@node1 grid]$ ssh node1.example.com date
	The authenticity of host 'node1.example.com (xxx.xxx.100.101)' can't be
	established.
	DSA key fingerprint is 7z:60:60:zz:48:48:z1:a0:f7:4e.
	Are you sure you want to continue connecting (yes/no)? yes
	Warning: Permanently added 'node1.example.com,xxx.xxx.100.101' (DSA) to the
	list of known hosts.
	Mon Dec 4 11:08:13 PST 2006
	[grid@node1 grid]$ ssh node2 date
	Mon Dec 4 11:08:35 PST 2006
	.
	.
	.
	```
	At the end of this process, the public host name for each member node should be registered in the `known_hosts` file for all other cluster nodes.
	If you are using a remote client to connect to the local node, and you see a message similar to "Warning: No xauth data; using fake authentication data for X11 forwarding," then this means that your authorized keys file is configured correctly, but your SSH configuration has X11 forwarding enabled. To correct this issue, proceed to ["Setting Display and X11 Forwarding Configuration"](prelinux.md).
3. Repeat step 2 on each cluster node member.

If you have configured SSH correctly, then you can now use the `ssh` or `scp` commands without being prompted for a password. For example:

```
[grid@node1 ~]$ ssh node2 date
Mon Feb 26 23:34:42 UTC 2009
[grid@node1 ~]$ ssh node1 date
Mon Feb 26 23:34:48 UTC 2009
```

If any node prompts for a password, then verify that the `~/.ssh/authorized_keys` file on that node contains the correct public keys, and that you have created an Oracle software owner with identical group membership and IDs.

## E.2 Configuring Kernel Parameters

This section contains the following:

- Minimum Parameter Settings for Installation
- Additional Parameter and Kernel Settings for SUSE Linux
- Checking OCFS2 Version Manually

Note:

The kernel parameter and shell limit values shown in the following section are recommended values only. For production database systems, Oracle recommends that you tune these values to optimize the performance of the system. Refer to your operating system documentation for more information about tuning kernel parameters.

### E.2.1 Minimum Parameter Settings for Installation

During installation, or when you run the Cluster Verification Utility (cluvfy) with the flag `-fixup`, a fixup script is generated. This script updates required kernel packages if necessary to minimum values.

If you cannot use the fixup scripts, then review the following table to set values manually:

| Parameter | Value | File |
| --- | --- | --- |
| semmsl   semmns   semopm   semmni | 250   32000   100   128 | `/proc/sys/kernel/sem` |
| shmmax | Minimum allocation:  536870912 (512 MB)  Maximum allocation:  - Linux x86: At least 1 byte less than 4 GB, or 4294967295. 	Recommended: More than half the physical memory. - Linux x86-64: At least 1 byte less than the physical memory 	Recommended: More than half the physical memory  See My Oracle Support Note 567506.1 for additional information about configuring shmmax. | `/proc/sys/kernel/shmmax` |
| shmmni | 4096 | `/proc/sys/kernel/shmmni` |
| shmall | 2097152 | `/proc/sys/kernel/shmall` |
| file-max | 6815744 | `/proc/sys/fs/file-max` |
| ip\_local\_port\_range | Minimum: 9000  Maximum: 65500 | `/proc/sys/net/ipv4/ip_local_port_range` |
| rmem\_default | 262144 | `/proc/sys/net/core/rmem_default` |
| rmem\_max | 4194304 | `/proc/sys/net/core/rmem_max` |
| wmem\_default | 262144 | `/proc/sys/net/core/wmem_default` |
| wmem\_max | 1048576 | `/proc/sys/net/core/wmem_max` |
| aio-max-nr | 1048576 | /proc/sys/fs/aio-max-nr |

Note:

If the current value for any parameter is greater than the value listed in this table, then the Fixup scripts do not change the value of that parameter.

### E.2.2 Additional Parameter and Kernel Settings for SUSE Linux

On SUSE systems only, complete the following steps as needed:

1. Enter the following command to cause the system to read the `/etc/sysctl.conf` file when it restarts:
	```
	# /sbin/chkconfig boot.sysctl on
	```
2. On SUSE 10 systems only, use a text editor to change the `/etc/sysconfig/boot.sysctl` parameter `RUN_PARALLEL` flag from `yes` to `no`.
3. Enter the GID of the `oinstall` group as the value for the parameter `/proc/sys/vm/hugetlb_shm_group`. Doing this grants members of `oinstall` a group permission to create shared memory segments.
	For example, where the oinstall group GID is 501:
	```
	# echo 501 > /proc/sys/vm/hugetlb_shm_group
	```
	After running this command, use `vi` to add the following text to `/etc/sysctl.conf`, and enable the `boot.sysctl` script to run on system restart:
	```
	vm.hugetlb_shm_group=501
	```
	Note:
	Only one group can be defined as the `vm.hugetlb_shm_group`.
4. Repeat steps 1 through 3 on all other nodes in the cluster.

## E.3 Checking OCFS2 Version Manually

To check your OCFS version manually, enter the following commands:

```
modinfo ocfs2
rpm -qa |grep ocfs2
```

Ensure that `ocfs2console` and `ocfs2-tools` are at least version 1.2.7, and that the other OCFS2 components correspond to the pattern ocfs2-kernel\_version-1.2.7 or greater. If you want to install Oracle RAC on a shared home, then the OCFS version must be 1.4.1 or greater.

For information about OCFS2, refer to the following Web site:

```
http://oss.oracle.com/projects/ocfs2/
```