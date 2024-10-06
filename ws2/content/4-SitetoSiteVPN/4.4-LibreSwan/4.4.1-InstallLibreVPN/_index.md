---
title : "Install LibreSwan"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 4.4.1 </b> "
---

A pre-built Libreswan package is available on the following OS distributions: RHEL, Fedora, CentOS, Ubuntu, Debian, Arch, Apline, OpenWrt and FreeBSD. On NetBSD the package sources are in wip/libreswan.

We install **LibreSwan** and **Net-tools** through Ubuntu package on [EC2 Customer Gateway](/3-DataServer/3.6-createec2) by the command below:

```
sudo apt update -y && sudo apt install libreswan net-tools -y
```

Checking the result of installation:

```
ss -v && ipsec --help
```

![lb](/aws-fcj/ws1/images/4.sitetositevpn/l-01.png)
