---
title : "LibreSwan"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 4.4 </b> "
---

Libreswan is an Internet Key Exchange (IKE) implementation for Linux, FreeBSD, NetBSD and OpenBSD. It supports IKEv1 and IKEv2 and has support for most of the extensions (RFC + IETF drafts) related to IPsec, including IKEv2, X.509 Digital Certificates, NAT Traversal, and many others.

[Libreswan](https://libreswan.org/) was forked from **Openswan 2.6.38**, which was forked from FreeS/WAN 2.04.

The Libreswan Project 

```
https://libreswan.org/
```

A Git repository is available at:

```
https://github.com/libreswan/libreswan/
```

We need this program to simulate a VPN gateway in the [Data Server](/3-DataServer). OpenSwan does not support Debian linux for Ubuntu, and also does not available at Fedora linux for Amazon Linux. The last version has been released since 2021, [github project](https://github.com/xelerance/Openswan).