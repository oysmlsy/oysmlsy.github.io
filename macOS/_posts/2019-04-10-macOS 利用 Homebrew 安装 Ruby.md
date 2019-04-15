---
title: macOS 利用 Homebrew 安装 Ruby
---

macOS 系统自带 Ruby 和 RubyGems，可执行文件`ruby`和`gem`均位于`/usr/bin`目录。

    $ which ruby gem
    /usr/bin/ruby
    /usr/bin/gem

版本较老：

    $ ruby -v
    ruby 2.3.7p456 (2018-03-28 revision 63024) [universal.x86_64-darwin17]=

    $ gem -v
    2.5.2.3

利用 Homebrew 安装最新版 Ruby：

    $ brew install ruby

用新安装的 RubyGems 安装的二进制文件将会位于`/usr/local/lib/ruby/gems/2.6.0/bin`目录，故需将此目录加入`PATH`环境变量：

    $ echo 'export PATH="$PATH:/usr/local/lib/ruby/gems/2.6.0/bin"' >> ~/.bash_profile

Homebrew 通常会把新安装的 formula 的可执行程序软链接至`/usr/local/bin/`目录，以使其处于`PATH`环境变量中。Homebrew 对 Ruby 的安装并未按此传统进行，因为 macOS 系统自带 Ruby 和 RubyGems。

故需将新安装的 Ruby 置于`PATH`环境变量的前部：

    $ echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> ~/.bash_profile

声明如下环境变量，以使编译器能够找到新安装的 Ruby：

    $ echo 'export LDFLAGS="-L/usr/local/opt/ruby/lib"' >> ~/.bash_profile
    $ echo 'export CPPFLAGS="-I/usr/local/opt/ruby/include"' >> ~/.bash_profile

声明如下环境变量，以使 pkg-config 能够找到新安装的 Ruby：

    $ echo 'export PKG_CONFIG_PATH="/usr/local/opt/ruby/lib/pkgconfig"' >> ~/.bash_profile

重新加载 Bash 配置文件，使上述配置生效：

    $ source ~/.bash_profile

`ruby`和`gem`命令已经更新：

    $ which ruby gem
    /usr/local/opt/ruby/bin/ruby
    /usr/local/opt/ruby/bin/gem
