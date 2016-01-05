---
layout: post
title:  "安装 CentOS 7.x Minimal 后，从头打造桌面工作站"
categories: technology
---
## 安装 CentOS 7.x 后，以前装好的 Windows 或是其它操作系统没有出现在启动项中的解决办法

在/boot/grub2/grub.cfg中添加

    menuentry 'some OS name' {
        set root=(hd0,1)
        chainloader +1
    }

(hd0,1)代表第一个分区。

## 安装 GNOME

    $ yum grouplist
    $ yum groupinstall "GNOME Desktop"
    $ startx

CentOS 6.x 与 CentOS 7.x 的 group 不一样（CentOS 7.x 的不同子版本的 group 有些也不一样），CentOS 6.x 需要这样：

    $ yum groupinstall "X Window System" "Desktop" "Chinese Support"

## 安装第三方源 EPEL 与 RPMForge

CentOS 官方文档声称严重推荐 EPEL，不推荐 RPMForge（现在叫RepoForge），因为 RPMForge 已经不再被维护了，虽然曾经被 CentOS 推荐。我的做法是这两个都安装，但都要 disable 掉，需要的时候再加上 --enablerepo=epel 或 --enablerepo=rpmforge。

去 EPEL 和 RPMForge 官网各自下载 .rpm 文件，双击安装或 `$ rpm -ivh *.rpm`，EPEL 或 RPMForge 的 repo 文件就已经在目录 /etc/yum.repos.d/ 下了。

## 支持挂载 NTFS 文件系统

CentOS 官方源没有支持 NTFS 的包，需要从 EPEL 或 RPMForge 源里安装。

    $ yum install ntfs-3g --enablerepo=epel

或

    $ yum install fuse-ntfs-3g --enablerepo=rpmforge

## 安装 C++ 编译器

    $ yum install gcc-c++

## 安装 Git

    $ yum install git

## 安装常用压缩打包命令

    $ yum install zip unzip
    $ yum install rar --enablerepo=rpmforge
    $ yum install p7zip --enablerepo=rpmforge

## 安装 Markdown 解析器 python-markdown

Linux 下 Markdown 解析器有很多，CentoOS 官方 Yum 源（extras）里有 python-markdown。

    $ yum install python-markdown
    $ markdown_py -h
    $ markdown_py *.md > *.html

## 安装 Flash Player

Adobe 官网下载 yum 安装包：

    $ rpm -ivh *.rpm
    $ yum install flash-plugin --enablerepo=adobe-linux-x86_64

或 Adobe 官网下载 rpm 安装包：

    $ rpm -ivh *.rpm

或利用 RPMforge：

    $ yum install flash-plugin --enablerepo=rpmforge

## 安装 VirtualBox

VirtualBox 需要编译操作系统内核，所以安装它之前需要先安装 kernel-devel 这个包：

    $ yum install kernel-devel

官网下载 .rpm 文件，双击安装或 `$ yum localinstall *.rpm`。

对于 VirtualBox 只能装32位系统的情况，涉及到 Host 的 CPU 是否支持虚拟化以及是否开启了虚拟化，如果没有开启，在 BIOS 里面设置，一般在 CPU 的子设置里面，且含有 “Virtualization” 或 “Virtual” 字样，将它设为 Enable 。

## 安装 wkhtmltopdf

去官网 http://wkhtmltopdf.org 下载 .rpm 文件，双击安装或 `$ yum localinstall *.rpm`。

    $ wkhtmltopdf http://google.com google.pdf
    $ wkhtmltoimage http://google.com google.jpg

## 安装 Chrome

官网下载 .rpm 文件，双击安装或 `$ yum localinstall *.rpm`。

## 安装 Apache HTTP Server

    $ yum install httpd

## 安装 MariaDB

    $ yum install mariadb-server
    $ mysql_secure_installation

## 安装 PHP

    $ yum install php php-mysql php-gd php-xml php-mbstring

## 安装 Sublime

官网下载压缩包，解压。

## 安装 Visual Studio Code

官网下载压缩包，解压。

## 安装 Tomcat

官网下载压缩包，解压。

## 安装 Gradle

官网下载压缩包，解压。

    $ vi ~/.bash_profile

将 Gradle 的 bin 目录加入到 $PATH 环境变量。

## 安装 Eclipse

官网下载压缩包，解压。去 Spring 官网下载 STS 的 Eclipse 插件，将插件安装进 Eclipse。

## 安装 Node.js

官网下载压缩包，解压。

    ./configure
    make
    make install
    $ node -v
    $ npm -v

