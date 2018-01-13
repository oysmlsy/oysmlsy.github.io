---
layout: right-sidebar
title:  "安装 CentOS 7.x Minimal 后，从头打造桌面工作站"
---

## 安装 CentOS 7.x 后，以前装好的 Windows 或是其它操作系统没有出现在启动项中的解决办法

在 /boot/grub2/grub.cfg 中添加

    menuentry 'some OS name' {
        set root=(hd0,1)
        chainloader +1
    }

(hd0,1)代表第一个分区。

## 没有 ifconfig 命令的解决办法

CentOS 7.x Minimal 版本在没有安装桌面环境之前是没有 ifconfig 命令的，看一看哪个包提供了 ifconfig 命令：

    $ yum provides ifconfig
    or
    $ yum whatprovides ifconfig

输出中可以看到 net-tools 包提供 ifconfig 命令，那么安装它吧：

    # yum install net-tools

## 安装 GNOME

    // 查看一下 YUM 仓库提供了哪些 groups
    $ yum grouplist

    // 那就安装吧
    $ yum groupinstall "GNOME Desktop"

    // 启动 X Window
    $ startx

CentOS 6.x 与 CentOS 7.x 的 group 是不一样的（CentOS 7.x 的不同子版本的 group 有些也不一样），CentOS 6.x 需要这样：

    $ yum groupinstall "X Window System" "Desktop" "Chinese Support"

## 安装第三方源 EPEL 与 RPMForge

CentOS 的官方文档声称严重推荐 EPEL，不推荐 RPMForge（现在叫RepoForge），因为 RPMForge 已经不再被维护了，虽然曾经被 CentOS 推荐。可以将这两个都安装，然后 disable 掉，需要的时候再加上 --enablerepo=epel 或 --enablerepo=rpmforge。

EPEL 官网说的很清楚，直接：

    $ yum install epel-release

RPMForge 则去官网下载 .rpm 文件：

    $ rpm -ivh *.rpm

EPEL 或 RPMForge 的 repo 文件就已经在目录 /etc/yum.repos.d/ 下了。

## 支持挂载 NTFS 文件系统

CentOS 的官方 YUM 仓库没有支持 NTFS 的包，需要从 EPEL 或 RPMForge 里安装。

    $ yum install ntfs-3g --enablerepo=epel
    or
    $ yum install fuse-ntfs-3g --enablerepo=rpmforge

## 安装常用压缩打包工具

    $ yum install zip unzip
    $ zip *.zip file1 file2
    $ unzip *.zip

    $ yum install rar --enablerepo=rpmforge
    $ rar a *.rar file1 file2
    $ rar x *.rar

    $ yum install p7zip --enablerepo=epel
    $ 7za a *.7z file1 file2
    $ 7za x *.7z

    $ tar xzvf *.tar.gz
    $ tar czvf *.tar.gz file1 file2
    $ tar xjvf *.tar.bz2
    $ tar cjvf *.tar.bz2 file1 file2
    $ tar xJvf *.tar.xz
    $ tar cJvf *.tar.xz file1 file2

## 安装 C++ 编译器

    $ yum install gcc-c++

## 安装 Apache HTTP Server

    $ yum install httpd

## 安装 MariaDB

    $ yum install mariadb-server

    // 然后进行初始化配置
    $ mysql_secure_installation

## 安装 PHP

    $ yum install php

    // 然后安装一些常用模块
    $ yum install php-mysql php-gd php-xml php-mbstring

    // PHP 的配置文件：/etc/php.int
    // 通常修改一下这个配置项：upload_max_filesize = 2M

## 安装 Tomcat

    $ yum install tomcat
    // 默认安装在 /usr/share/tomcat/

## 安装 Qt Creator

    $ yum install qt-creator qt-creator-doc qt-creator-data qt-creator-translations --enablerepo=epel

## 安装 Node.js

官网下载 Source Code

    $ ./configure
    $ make
    $ sudo make install
    $ node -v
    $ npm -v

## 安装 Java OpenJDK 开发包

查看一下当前 Java 版本：

    $ java -version
    openjdk version "1.8.0_91"
    OpenJDK Runtime Environment (build 1.8.0_91-b14)
    OpenJDK 64-Bit Server VM (build 25.91-b14, mixed mode)

1.8.0 版本，那么 search 一下就安装吧：

    $ yum search java-1.8.0
    $ yum install java-1.8.0-openjdk-devel

## 安装 Gradle 和 Maven

官网下载压缩包，解压。

    $ vi ~/.bash_profile

将 Gradle 和 Maven 的 bin 目录加入到 $PATH 环境变量。





## 安装 Git

    $ yum install git

## 使用 git config 命令配置用户信息

安装 Git 之后需要用 git config 命令配置 user name 和 user email，否则不能 commit，只能 clone。

    // 配置 user email
    $ git config --global user.email "your_email@example.com"

    // 配置 user name
    $ git config --global user.name "your_name"

    // 查看一下配置好的 user name 和 user email
    $ git config --list

git config 命令有3个选项，对应修改不同的配置文件。

1. `--system` 对应 /etc/gitconfig
2. `--global` 对应 ~/.gitconfig
3. no option 对应 .git/config

## 生成 SSH 公钥私钥对

为了使用 GitHub 等 Git 服务器的 SSH keys 功能，利用 ssh-keygen 命令在本地生成 rsa 密钥对。

    // generate a rsa key pair in the file ~/.ssh/id_rsa & ~/.ssh/id_rsa.pub, using the provided email as a label
    $ ssh-keygen -t rsa -C "your_email@example.com"

## 搭建 Git 服务器

首先安装 Git：

    $ yum install git

打开文件 /etc/ssh/sshd_config，找到并修改以下3个配置项。这么做的目的是为了让 Git 服务器的使用者能够利用 SSH 进行身份认证。

    StrictModes no
    RSAAuthentication yes
    PubkeyAuthentication yes

重启 sshd 服务：

    $ systemctl restart sshd

创建 git 用户：

    $ adduser git

可以为 git 用户创建一个密码，这样 Git 服务器的使用者如果不能利用 SSH 进行身份认证的话还能利用密码进行身份认证。

    $ passwd git

不要把刚刚创建的 git 用户当作普通的 Linux 用户使用，git 用户只用于 git 服务，不允许 git 用户登录 shell。打开 /etc/passwd 文件，找到类似下面的一行：

    git:x:1001:1001:,,,:/home/git:/bin/bash

改为：

    git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell

创建 /home/git/.ssh/authorized_keys 文件，并保证 owner 为 git 用户。

    $ cd /home/git/
    $ mkdir .ssh
    $ cd .ssh
    $ touch authorized_keys
    $ cd ..
    $ chown -R git:git .ssh/

收集 Git 服务器使用者的公钥，就是他们自己的 ~/.ssh/id_rsa.pub 文件，把所有公钥导入到 /home/git/.ssh/authorized_keys 文件里，一行一个。

选定一个目录作为 Git 仓库，比如 /home/git/sample.git/。

    $ cd /home/git/
    $ mkdir sample.git
    $ cd sample.git
    $ git init --bare
    $ cd ..
    $ chown -R git:git sample.git

现在可以通过 git clone 命令克隆远程仓库了：

    $ git clone git@server_name:sample.git

## 关于 .gitignore 文件的一些说明

各种类型的 gitignore 模板在 https://github.com/github/gitignore 查看。

    # 此为注释
    *.a 忽略所有目录下.a结尾的文档
    !lib.a 但不忽略lib.a文档
    *.[oa] 忽略所有目录下.a或.o结尾的文档
    *~ 忽略所有目录下~结尾的文档
    TODO 忽略所有目录下的TODO文档
    /TODO 仅仅忽略根目录下的TODO文档
    build/ 忽略所有目录下的build文件夹
    /build/ 仅仅忽略根目录下的build文件夹
    doc/**/*.txt 忽略doc文件夹下的所有.txt文档
    星号*匹配零个或多个任意字符
    [abc] 匹配任何一个列在方括号中的字符（这个例子要么匹配一个 a，要么匹配一个 b，要么匹配一个 c）
    问号?只匹配一个任意字符
    如果在方括号中使用短划线分隔两个字符，表示所有在这两个字符范围内的都可以匹配，比如 [0-9] 表示匹配所有 0 到 9 的数字

## 安装 Markdown 解析器 python-markdown

Linux 下 Markdown 解析器有很多，CentoOS 官方 Yum 仓库（extras）里有 python-markdown。

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

## 安装 MPlayer

安装 MPlayer 通常需要以下3个东西：

* source code（源代码 tarball 文件）
* binary codecs（一堆二进制的解码器文件）
* a skin（皮肤）

官网下载 source code。

    $ ./configure --enable-gui --language=zh_CN --disable-ossaudio

`--enable-gui`告诉 configure 以后运行 MPlayer 需要图形界面，不仅只从 command line 运行。

`--language=zh_CN`告诉 configure 安装中文环境。

`--disable-ossaudio`是因为 linux2.4 以后的内核逐渐抛弃 oss 音频架构而转向 alsa（详细说明请参考http://blog.csdn.net/meizum10/article/details/17437959）。

提示`No FFmpeg checkout, press enter to download one with git or CTRL+C to abort`，按下回车键。

通常 configure 会失败，因为需要一些依赖。它告诉缺什么就装什么。

提示`./configure: line 1522: git: command not found Failed to get a FFmpeg checkout`，configure 需要利用 git 下载 ffmpeg，如果 git 没有安装，那么就安装 git。

    $ yum install git

提示`Error: Compiler is not functioning correctly. Check your installation and custom CFLAGS  .`，源代码编译安装当然需要 gcc，如果没有安装，那么就安装它。g++ 依赖于 gcc，直接安装 g++。

    $ yum install gcc-c++

提示`Error: yasm not found, use --yasm='' if you really want to compile without`，缺少 yasm，去 yasm 官网 http://yasm.tortall.net 下载源代码 tarball，简单的三步走：

    $ ./configure
    $ make
    $ sudo make install

提示`Error: The GUI requires X11.`，缺少 X11，安装 gtk2-devel，**注意要安装 gtk2-devel，gtk3-devel 不行**。

    $ yum install gtk2-devel

configure 通过，接着

    $ make
    $ sudo make install

OK，安装完成，在 shell 里运行`mplayer 媒体文件名`一般可以播放。

官网下载 binary codecs，是个 tarball，解压，得到一堆解码器文件，将这些解码器文件放到 /usr/local/lib/codecs/ 里。/usr/local/lib/ 下如果没有codecs文件夹，那就手动创建一个。

官网下载 skin 文件，是个 tarball，解压，得一文件夹，将这文件夹放到 /usr/local/share/mplayer/skins/ 里，之后建立一个叫 default 的符号链接，指向皮肤文件夹。

    $ ln -s <文件夹名字> default

当然，也可以把文件夹名字直接改成 default。

如果播放没有声音，那么：

    $ yum install *alsa*

至于 CentOS 6.x，RPMforge（现在叫 RepoForge ）仓库里有 smplayer：

    $ yum install smplayer --enablerepo=rpmforge

## 安装 VirtualBox

VirtualBox 需要编译操作系统内核，所以安装它之前需要先安装 kernel-devel 这个包：

    $ yum install kernel-devel

编译内核需要编译器，要保证 gcc 已经安装：

    $ yum install gcc-c++

官网下载 .rpm 文件，双击安装或 `$ yum localinstall *.rpm`。

对于 VirtualBox 只能装32位系统的情况，涉及到 Host 的 CPU 是否支持虚拟化以及是否开启了虚拟化，如果没有开启，在 BIOS 里面设置，一般在 CPU 的子设置里面，且含有 “Virtualization” 或 “Virtual” 字样，将它设为 Enable 。

## 安装 wkhtmltopdf

去官网 http://wkhtmltopdf.org 下载 .rpm 文件，双击安装或 `$ yum localinstall *.rpm`。

    $ wkhtmltopdf http://google.com google.pdf
    $ wkhtmltoimage http://google.com google.jpg





