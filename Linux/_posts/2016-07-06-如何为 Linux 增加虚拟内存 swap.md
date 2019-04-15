---
title: 如何为 Linux 增加虚拟内存 swap
---

最近公司一台阿里云乞丐版云服务器上的 Wordpress 网站经常挂掉，翻看日志查明原因：内存小，MySQL 不停的消耗内存，最后被操作系统 kill 了。所以解决方案是为 Linux 增加虚拟内存 swap。

查看内存占用情况：

    $ free -m

创建一个足够大的文件：

    $ dd if=/dev/zero of=/swapfile bs=1024 count=1024000
    // /swapfile 就是在跟目录下创建一个 swapfile 文件
    // 文件大小是 1G
    // 1024 * 1G = 1024 * 1000M = 1024000

把这个文件变成 swap 文件：

    $ mkswap /swapfile

加载这个 swap 文件，用起来：

    $ swapon /swapfile

这个 swap 文件已经在工作了，查看一下 swap 文件加载的情况：

    $ cat /proc/swaps

要想在每次开机的时候自动加载这个 swap 文件，需要在 /etc/fstab 文件中追加一行：

    /swapfile swap swap defaults 0 0

有 swapon 命令，相应就有 swapoff 命令。卸载这个 swap 文件：

    $ swapoff /swapfile
