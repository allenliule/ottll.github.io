---
layout: post
title: "基于GitHub Pages和Jekyll搭建静态博客"
date: 2016-02-03
categories: jekyll
excerpt: Jekyll Github Pages 搭建静态博客
---

* content
{:toc}

## 创建GitHub Pages

---

### 创建Pages

---

GitHub Pages支持User/Organization Pages和Project Pages两种模式。可以通过User/Organization Pages建立主站，而通过Project Pages挂载二级应用页面。

按照正常流程创建repository，名称命名为username.github.io。

然后通过“Settings”，点击“Automatic Page Generator”生成页面，选择主题并发布。

可以访问username.github.io访问你的页面。

---

### 绑定域名

在“Settings”页面，可以将自己的域名绑定到username.github.io。如无域名则忽略。

---

## 本地Jekyll的环境配置

---

### 安装Ruby和DevKit

---

ruby和Devkit[下载](http://rubyinstaller.org/downloads/)

ruby直接安装，并配置环境变量，path中配置C:\Ruby22-x64\bin目录，通过查看版本号验证安装是否成功。

	ruby -v

然后在命令行终端下升级gem：

	gem update --system


DevKit是windows平台下编译和使用本地C/C++扩展包的工具。它就是用来模拟Linux平台下的make,gcc,sh来进行编译。但是这个方法目前仅支持通过RubyInstaller安装的Ruby，并双击运行解压到C:\DevKit。然后打开终端cmd，输入下列命令进行安装

	cd C:\DevKit
	ruby dk.rb init
	ruby dk.rb install

---

### 安装jekyll

由于国内屏蔽，部分安装包可能无法下载，修改下载镜像为taobao：gem sources --add https://ruby.taobao.org/ --remove https://rubygems.org/

	gem install jekyll

检查安装是否成功：

	jekyll --version


安装Rdiscount，这个用来解析Markdown标记的包：

	gem install rdiscount

安装bundle：

	gem install bundle

---

### 创建博客

cd到博客目录下，创建文件Gemfile，并增加如下内容

	source 'https://ruby.taobao.org/'
	gem 'github-pages'

然后运行。命令会根据当前目录下的Gemfile，安装所需要的所有软件。

	bundle install

后期需要更新环境时，使用如下命令

	bundle update

启动服务：

	bundle exec jekyll serve

访问http://localhost:4000/，即可看到

---

### 选择模板

Jekyll有很多现成的[模板](http://jekyllthemes.org/)，可以直接访问选择。

---

### 绑定评论

国内可以使用多说，参见[多说官网](http://duoshuo.com/)。

---

## 开始写博客

---

### 配置_config.yml

修改博客标题

	title: My Blog

修改个人信息

    author:
    name: Name Lastname
    email: blah@email.test
    github: username

引用：_config.yml中的键值均引用到其他页面{{ site.title }}

### 写文章

按照_config.yml的格式permalink: /:categories/:year/:month/:day/:title，可以修改格式，创建markdown格式文件，就可以当初博客发布了。

### 发布

本地预览修改：运行bundle exec jekyll serve，预览localhost:4000。

发布到github上：通过命令提交或者客户端提交。

    git clone git@github.com:username/username.github.com.git //本地如果无远程代码，先做这步，不然就忽略
    cd .ssh/username.github.com //定位到你blog的目录下
    git pull origin master //先同步远程文件，后面的参数会自动连接你远程的文件
    git status //查看本地自己修改了多少文件
    git add . //添加远程不存在的git文件
    git commit * -m "what I want told to someone"
    git push origin master //更新到远程服务器上

---

## 参考文章
1. [jekyll官网](http://jekyllrb.com/)
2. [Jekyll 搭建静态博客](http://gaohaoyang.github.io/2015/02/15/create-my-blog-with-jekyll/)
3. [通过GitHub Pages建立个人站点](http://www.cnblogs.com/purediy/archive/2013/03/07/2948892.html)