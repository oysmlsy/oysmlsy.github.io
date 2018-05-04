
通过 App Store 安装 Xcode。

Xcode 默认不会安装 Command Line Tools，可以通过下面的命令安装之：

    $ xcode-select --install

Command Line Tools 安装完成后，再次运行`xcode-select --install`，如果出现下述输出，则说明安装成功。

    $ xcode-select --install
    xcode-select: error: command line tools are already installed, use "Software Update" to install updates

Homebrew 依赖于 Command Line Tools。

访问 Homebrew 官网，按照官方最新方法进行安装：

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

对上述命令的解释：利用 `curl` 命令去网上获取 Homebrew 的 Ruby 安装脚本文件，然后利用系统自带的 Ruby ，即`/usr/bin/ruby`运行脚本文件。

验证一下安装是否成功：

    $ brew doctor
    Your system is ready to brew.

访问 Homebrew Cask 官网，按照官方最新方法进行安装：

    $ brew tap caskroom/cask

Homebrew 主要涉及`/usr/local/`目录下的3个子目录：`Homebrew/`、`Cellar/`和`Caskroom/`。

`/usr/local/Homebrew/`是 Homebrew 的程序安装目录。

Homebrew 的 GitHub 是 Homebrew/brew，安装脚本把 Homebrew 的 GitHub 仓库克隆至`/usr/local/Homebrew/`目录，并把里面的可执行文件`/usr/local/Homebrew/bin/brew`软链接至`/usr/local/bin/brew`。

而`/usr/local/bin/`目录是 PATH 环境变量的一部分。

`/usr/local/Cellar/`目录是通过`brew install <formula>`命令安装的软件包的安装所在路径，里面的每个子目录都是一个包，目录名即为包名，按照`Cellar/包名/版本号/`的形式来安放，包括可执行程序、文档和配置文件。

Homebrew 把软件包称为 formula。

每个软件包的可执行程序被软链接至`/usr/local/bin/`，例如：

    # 看一下在命令行里直接输入`python`命令到底执行的是哪个可执行文件
    $ type python
    python is hashed (/usr/local/bin/python)
    $ ls -l /usr/local/bin/python
    lrwxr-xr-x  1 oysmlsy  admin  38  4 26 20:21 /usr/local/bin/python -> ../Cellar/python@2/2.7.14_3/bin/python

通常`/usr/bin/`存放的是系统预装的可执行程序，会随着系统升级而改变。

`/usr/local/bin/`目录是给用户放置自己的可执行程序的地方，不会被系统升级而覆盖同名文件。

如果两个目录下有相同的可执行程序，谁优先执行受到 PATH 环境变量的影响。

看一下 PATH 环境变量：

    $ echo $PATH
    /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

`/usr/local/bin/`通常在`/usr/bin/`之前，所以`/usr/local/bin/`优先于`/usr/bin/`。

`/usr/local/Caskroom/`用于存放通过`brew cask install <cask>`命令安装的软件包，里面的每个子目录都是一个包，目录名即为包名，按照`Caskroom/包名/版本号/`的形式来安放。

Homebrew Cask 将下载安装好的二进制程序`XXX.app`文件放到`/Applications/`目录下。

Homebrew Cask 把软件包称为 cask。


    $ brew cask info  google-chrome
    $ brew cask search sublime
    $ brew cask install pycharm
    $ brew cask install vmware-fusion
    $ brew cask install dingtalk
    $ brew cask install vlc
    $ brew cask install go2shell
    App Store 只有版本1，Cask有版本2
    $ brew cask install baidunetdisk
    $ brew cask install thunder
    $ brew cask install ccleaner
    $ brew cask install docker
    $ brew cask install dash

English

Safari 浏览器中使用“开发”菜单中的开发者工具
如果未在 Safari 菜单栏中看到“开发”菜单，选取“Safari 浏览器”>“偏好设置”，点按“高级”，然后选择“在菜单栏中显示开发菜单”。

设置终端输入 exit 或 CTRL+D 关闭窗口
Mac 的终端默认输入 exit 或 CTRL+D 之后 只是结束了进程，窗口并没有关闭。
选取“终端”>“偏好设置”，点按“描述文件”，然后在“当 shell 退出时”下拉框处选择“关闭窗口”。

使用 git config 命令配置用户信息

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

生成 SSH 公钥私钥对

为了使用 GitHub 等 Git 服务器的 SSH keys 功能，利用 ssh-keygen 命令在本地生成 rsa 密钥对。

    // generate a rsa key pair in the file ~/.ssh/id_rsa & ~/.ssh/id_rsa.pub, using the provided email as a label
    $ ssh-keygen -t rsa -C "your_email@example.com"

    $ touch ~/.bash_profile
    $ vi ~/.bash_profile
    export CLICOLOR=1
    export LSCOLORS=gxfxaxdxcxegedabagacad
    alias ll='ls -l'

CLICOLOR是用来设置是否进行颜色的显示。
LSCOLORS是用来设置当CLICOLOR被启用后，各种文件类型的颜色。LSCOLORS的值中每两个字母为一组，分别设置某个文件类型的文字颜色和背景颜色。LSCOLORS中一共11组颜色设置，按照先后顺序，分别对以下的文件类型进行设置：

    1.  directory
    2.  symbolic link
    3.  socket
    4.  pipe
    5.  executable
    6.  block special
    7.  character special
    8.  executable with setuid bit set
    9.  executable with setgid bit set
    10. directory writable to others, with sticky bit
    11. directory writable to others, without sticky bit

LSCOLORS中，字母代表的颜色如下：

    a 黑色
    b 红色
    c 绿色
    d 棕色
    e 蓝色
    f 洋红色
    g 青色
    h 浅灰色
    A 黑色粗体
    B 红色粗体
    C 绿色粗体
    D 棕色粗体
    E 蓝色粗体
    F 洋红色粗体
    G 青色粗体
    H 浅灰色粗体
