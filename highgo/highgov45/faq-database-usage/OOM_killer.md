---
title: "18、如何处理HGDB被OOM killer kill的情况"
book: "数据库使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/OOM_killer.html"
tags:
  - highgo
  - highgo-v45
  - faq-database-usage
---

## 如何处理HGDB被OOM killer kill的情况

## 1、文档用途

本文适用于HGDB在Linux下被OOM killer kill的情况，如何进行排查及解决方案。

## 2、详细信息

Linux内核管理使用OOM killer（Out Of Memory killer）机制，在系统内存不足时，选择性杀死一些进程释放内存，保证系统可以继续运行。

**OOM killer产生的原因**

Linux内核根据应用程序的要求分配内存，应用程序分配到了内存，但通常情况下，不会全部用光，为了提高性能，这部分没用的内存可以留作它用，这部分内存属于所有进程，内核直接回收利用比较麻烦，所以内核采用了过度分配内存（over-commit memory）的方法间接利用这部分“空闲”内存，提高整体内存的使用效率。一般情况下，这样做没有问题，但当大多数应用程序都消耗完自己的内存的时候就会出现问题，因为这样应用程序的内存需求加起来超过了物理内存（包括swap）的容量，内核必须杀掉一些进程，释放一部分内存，保障系统正常运行。

**OOM killer选择哪个进程**

OOM Killer通过检查所有正在运行的进程，然后根据算法给每个进程一个badness分数，拥有最高badness分数的进程将在内存不足时被杀掉。打分算法如下：

- 某个进程和它的子进程占用了较多内存，会打一个高分。
- 优先选择进程号最小的进程。
- 内核进程和其他重要的进程得分较低。

OOM killer给每个进程打的分数都存放在/proc/{pid}/oom\_score文件中。

与OOM killer相关的分数还有oom\_adj和oom\_score\_adj，这两个文件存放的是用户对进程的打分。oom\_adj已经过时，当前存在只是为了兼容旧版本的内核，oom\_score\_adj是新版官方建议使用的，这两个参数任何一个变动，另一个也会跟随变化，两个数值是线性相关的。oom\_adj取值范围是-17 ~~+15，设置为-17时，禁止OOM killer杀掉对应进程。oom\_score\_adj的取值范围是-1000~~ +1000，设置为-1000时，禁止OOM killer杀掉对应进程。

**查询被OOM killer杀掉的进程**

OOM killer杀掉进程后，会将相关日志输出到操作系统日志中，可以直接查看操作系统日志（/var/log/messages），也可以通过dmesg命令获取系统日志。查询命令及查询结果如下：

```
[root@registry ~]# dmesg | grep -i "killed process"

[2154261.752448] Killed process 31999 (postgres) total-vm:2356280kB, anon-rss:996kB, file-rss:776kB, shmem-rss:32612kB

#直接查看系统日志

[root@registry ~]# grep -i 'killed process' /var/log/messages

May  8 13:46:53 registry kernel: Killed process 31999 (postgres) total-vm:2356280kB, anon-rss:996kB, file-rss:776kB, shmem-rss:32612kB
```

如何查询OOM killer对进程的评分

可以使用如下脚本查询排名OOM killer对进程的打分，分数最高的，在内存不足的时候存在被OOM killer杀掉的风险。

```
#!/bin/bash

# Displays running processes in descending order of OOM score

printf 'PID\tOOM Score\tOOM Adj\tCommand\n'

(ps -e -o pid= -o comm=) |sort -k 2nr|while read -r pid comm; do

[ -f /proc/$pid/oom_score ] && [ $(cat /proc/$pid/oom_score) != 0 ] && printf '%d\t%d\t\t%d\t%s\n' "$pid" "$(cat /proc/$pid/oom_score)" "$(cat /proc/$pid/oom_score_adj)" "$comm"

done
```

**如何防止进程被OOM killer杀掉**

以下方式通过

**修改内核参数**

在Linux中，内核参数vm.overcommit\_memory控制内存的申请策略，有三个值，如下：

0 – Heuristic overcommit handling. 这是缺省值，它允许overcommit，但过于明目张胆的overcommit会被拒绝，比如malloc一次性申请的内存大小就超过了系统总内存。Heuristic的意思是“试探式的”，内核利用某种算法猜测你的内存申请是否合理，它认为不合理就会拒绝overcommit。

1 – Always overcommit. 允许overcommit，对内存申请来者不拒。内核执行无内存过量使用处理。使用这个设置会增大内存超载的可能性，但也可以增强大量使用内存任务的性能。

2 – Don’t overcommit. 禁止overcommit。 内存拒绝等于或者大于总可用 swap 大小以及 overcommit\_ratio 指定的物理 RAM 比例的内存请求。

如果希望减小内存过度使用的风险，将overcommit\_memory设置为2是最好的，此时单次申请的内存大小不能超过 \[free memory + free swap + pagecache的大小 + SLAB中可回收的部分\]，否则就申请失败。

怎样才算是overcommit？kernel设有一个阈值，申请的内存总数超过这个阈值就算overcommit，在/proc/memifo中可以看到这个阈值的大小：

```
# grep -i commit /proc/meminfo 

CommitLimit:     3492144 kB

Committed_AS:    4054564 kB
```

CommitLimit就是overcommit的阈值，申请的内存总数超过CommitLimit就是overcommit。这个阈值通过内核参数vm.overcommit\_ratio或vm.overcommit\_kbytes间接设置，公式如下：

CommitLimit = (Physical RAM \* vm.overcommit\_ratio / 100) + Swap

注：vm.overcommit\_ratio是内核参数，缺省值是50，表示物理内存的50%。也可以通过内核参数vm.overcommit\_kbytes直接设置字节数大小。如果使用了大页内存，就需要从物理内存中减去，公式变成：CommitLimit = (\[total RAM\] – \[total huge TLB RAM\]) \* vm.overcommit\_ratio / 100 + swap

/proc/meminfo中的 Committed\_AS 表示所有进程已经申请的内存总大小，（注意是已经申请的，不是已经分配的），如果 Committed\_AS 超过 CommitLimit 就表示发生了 overcommit，超出越多表示 overcommit 越严重。

**修改overcommit\_memory的方法**

1).以root身份登录Linux,编辑/etc/sysctl.conf ，改vm.overcommit\_memory=1，然后sysctl -p使配置文件生效

2).sysctl vm.overcommit\_memory=1

3).echo 1 > /proc/sys/vm/overcommit\_memory

**增加swap**

如果当前服务器内存不足，并且暂时无法增加内存，可以考虑增加swap交换区，避免系统波动造成OOM killer杀掉进程。如果增加swap空间可以解决OOM的问题，则说明物理内存不足，需要考虑增加内存。

临时增加swap的方法

```
dd if=/dev/zero of=swapadd bs=1024 count=5242880

mkswap swapadd

chmod   600 swapadd  -R

swapon swapadd

free -m

swapoff swapadd
```

修改进程的OOM分数值

可以直接修改进程的oom\_adj的值，方式如下

```
pgrep -f "/opt/HighGo4.3.4.7-see/bin/postgres" | while read PID;do echo -17 > /proc/$PID/oom_adj;done
```

上面的方法仅能修改单个进程的分数，因为其他进程均为主进程产生，通常情况下，保证主进程不被OOM killer杀掉就能确保数据库程序完整。