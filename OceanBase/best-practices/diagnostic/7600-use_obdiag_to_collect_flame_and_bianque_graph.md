---
title: "使用 obdiag 收集火焰图和扁鹊图最佳实践"
book: "诊断"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000001489657.html"
tags:
  - oceanbase
  - best-practices
  - diagnostic
---

# 使用 obdiag 收集火焰图和扁鹊图最佳实践

#### 说明

- obdiag 部署简单，可以部署到任一台能够连接到集群各节点的服务器上，并不局限于 OBServer 节点。
- obdiag 具备集中式收集的特点，程序单点部署，无需每台服务器部署。使用时只需要在部署机器上执行收集、巡检或分析命令即可。

#### 说明

生成的火焰图为 SVG 格式，主要展示调用栈信息以及调用的抽样次数，可以使用 `scp` 命令传输到本地之后进行查看。

#### 注意

X 轴不代表时间，而是所有的调用栈合并后，按字母顺序排列的函数。

#### 说明

生成的扁鹊图为 SVG 格式，可以使用 `scp` 命令传输到本地之后进行查看。

#### 说明

`-p` 后面是进程 ID，请改成需要 perf 的进程。
