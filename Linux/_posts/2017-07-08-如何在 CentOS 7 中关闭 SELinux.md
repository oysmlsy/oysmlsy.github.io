---
layout: right-sidebar
title:  '如何在 CentOS 7 中关闭 SELinux'
---

## 修改配置文件，永久生效，需要重启

SELinux 的配置文件为 `/etc/selinux/config` 。

    $ vi /etc/selinux/config

配置为 `SELINUX=disabled` ，重启机器，即可永久关闭 SELinux 。

**需要注意：**修改这个配置文件，必须重启才能生效，SELinux 没有办法重新加载这个文件。

这个文件里的注释解释的很清楚，你可以强制施行 SELinux 安全策略，可以仅输出警告，也可以将 SELinux 安全策略彻底 disable ，即 `SELINUX=` 的值可以分别是 enforcing | permissive | disabled 。

## 查看 SELinux 的运行模式

    $ getenforce

这个命令告诉我们 SELinux 的当前运行模式是 enforcing 、permissive 还是 disabled 。

还有一个命令可以告诉我们 SELinux 的运行状态：

    $ sestatus

打印出的内容里可以找到如下信息：

    SELinux status: enabled
    Current mode:   permissive

## 临时更改运行模式，不需要重启

如果 SELinux 正在运行，可以使用 `setenforce` 命令设置运行模式。

    $ setenforce

setenforce 命令打印出用法：

    usage:  setenforce [ Enforcing | Permissive | 1 | 0 ]

可见命令的参数4选1。

如临时关闭 SELinux：

    $ setenforce Permissive

将 SELinux 的运行模式改为 Permissive ，但重启之后还是会变成原来的状态。修改配置文件才能永久生效。